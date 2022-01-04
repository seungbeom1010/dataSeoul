import React, { useState, useEffect } from 'react';
import {
  Chart as ChartJS,
  LineElement,
  BarElement,
  PointElement,
  BarController,
  LineController,
  CategoryScale,
  LinearScale,
  Legend,
  Tooltip,
} from 'chart.js';
import { Chart } from 'react-chartjs-2';
import { useInView } from 'react-intersection-observer';
import axios from 'axios';


ChartJS.register(
  LineElement,
  BarElement,
  PointElement,
  BarController,
  LineController,
  CategoryScale,
  LinearScale,
  Legend,
  Tooltip,
);

const LINE_CHART_STYLES = [
  {
    backgroundColor: 'rgba(255, 99, 132, 0.5)',
    borderColor: 'rgb(255, 99, 132)',
    pointBorderWidth: 1,
    pointRadius: 5,
    pointStyle: 'circle',
  },
  {
    backgroundColor: 'rgba(255, 159, 64, 0.5)',
    borderColor: 'rgb(255, 159, 64)',
    pointBorderWidth: 2,
    pointRadius: 6,
    pointStyle: 'star',
  },
  {
    backgroundColor: 'rgba(255, 205, 86, 0.5)',
    borderColor: 'rgb(255, 205, 86)',
    pointBorderWidth: 1,
    pointRadius: 6,
    pointStyle: 'rectRot',
  },
  {
    backgroundColor: 'rgba(75, 192, 192, 0.5)',
    borderColor: 'rgb(75, 192, 192)',
    pointBorderWidth: 2,
    pointRadius: 6,
    pointStyle: 'crossRot',
  },
  {
    backgroundColor: 'rgba(54, 162, 235, 0.5)',
    borderColor: 'rgb(54, 162, 235)',
    pointBorderWidth: 1,
    pointRadius: 6,
    pointStyle: 'triangle',
  },
  {
    backgroundColor: 'rgba(153, 102, 255, 0.5)',
    borderColor: 'rgb(153, 102, 255)',
    pointBorderWidth: 1,
    pointRadius: 6,
    pointStyle: 'rect',
  },
];

const BACKGROUND_COLORS = [
  'rgba(255, 99, 132, 0.8)',
  'rgba(255, 159, 64, 0.8)',
  'rgba(255, 205, 86, 0.8)',
  'rgba(75, 192, 192, 0.8)',
  'rgba(54, 162, 235, 0.8)',
  'rgba(153, 102, 255, 0.8)',
  'rgba(201, 203, 207, 0.8)',
];

const CITY_NAMES = {
  '11740': '강동구',
  '11710': '송파구',
  '11680': '강남구',
  '11650': '서초구',
  '11620': '관악구',
  '11590': '동작구',
  '11560': '영등포구',
  '11545': '금천구',
  '11530': '구로구',
  '11500': '강서구',
  '11470': '양천구',
  '11440': '마포구',
  '11410': '서대문구',
  '11380': '은평구',
  '11350': '노원구',
  '11320': '도봉구',
  '11305': '강북구',
  '11290': '성북구',
  '11260': '중랑구',
  '11230': '동대문구',
  '11215': '광진구',
  '11200': '성동구',
  '11170': '용산구',
  '11140': '중구',
  '11110': '종로구',
  '1': '서울특별시'
};

const chartContainerStyle = {
  position: "relative",
  margin: "auto",
  height: "100%",
  width: "100%",
};

function currencyTooltipLabel(context) {
  let label = '';
  if (context.parsed.y !== null) {
    if (context.parsed.y >= 1000000000000) {
      label += new Intl.NumberFormat('ko', { maximumSignificantDigits: 4 }).format(context.parsed.y / 1000000000000) + '조원';
    } else if (context.parsed.y >= 100000000) {
      label += new Intl.NumberFormat('ko', { maximumSignificantDigits: 4 }).format(context.parsed.y / 100000000) + '억원';
    } else if (context.parsed.y >= 10000) {
      label += new Intl.NumberFormat('ko', { maximumSignificantDigits: 4 }).format(context.parsed.y / 10000) + '만원';
    } else {
      label += new Intl.NumberFormat().format(context.parsed.y) + '원';
    }
  }
  return label;
}

const salesByQtrGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      usePointStyle: true,
      callbacks: {
        label: currencyTooltipLabel,
      },
    },
  },
  scales: {
    y: {
      suggestedMin: 0,
    },                  
  },
};

export function SalesByQtrGraph(props) {
  const [data, setData] = useState({labels: [], datasets: []});
  const [isUpdated, setIsUpdated] = useState(false);
  const [ref, inView] = useInView({
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    const url = 'graph/sales-by-qtr' + (props.cityId ? '/' + props.cityId : '');
    if (!isUpdated && inView) {
      axios.get(url).then(response => {
        setData({
          labels: response.data.data.labels,
          datasets: [{
            ...response.data.data.datasets[0],
            ...LINE_CHART_STYLES[4],
          }],
        });
        setIsUpdated(true);
      }).catch(error => {
        console.log(error);
      });
    }
  }, [props.cityId, isUpdated, inView]);
  
  useEffect(() => {
    setData({labels: [], datasets: []});
    setIsUpdated(false);
  }, [props.cityId])

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='line' data={data} options={salesByQtrGraphOptions} />
    </div>
  );
}

const salesByCityGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      callbacks: {
        label: currencyTooltipLabel,
      },
    },
  },
  scales: {
    y: {
      suggestedMin: 0,
    },                  
  },
};

export function SalesByCityGraph() {
  const [data, setData] = useState({labels: [], datasets: []});
  const [ref, inView] = useInView({
    triggerOnce: true,
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    if (inView) {
      axios.get('graph/sales-by-city').then(response => {
        setData({
          labels: response.data.data.labels.map(code => CITY_NAMES[code]),
          datasets: [{
            ...response.data.data.datasets[0],
            backgroundColor: BACKGROUND_COLORS,
          }],
        });
      }).catch(error => {
        console.log(error);
      });
    }
  }, [inView]);

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='bar' data={data} options={salesByCityGraphOptions} />
    </div>
  );
}

function populationTooltipLabel(context) {
  let label = '';
  if (context.parsed.y !== null) {
    if (context.parsed.y >= 100000000) {
      label += new Intl.NumberFormat('ko', { maximumSignificantDigits: 4 }).format(context.parsed.y / 100000000) + '억명';
    } else if (context.parsed.y >= 10000) {
      label += new Intl.NumberFormat('ko', { maximumSignificantDigits: 4 }).format(context.parsed.y / 10000) + '만명';
    } else {
      label += new Intl.NumberFormat().format(context.parsed.y) + '명';
    }
  }
  return label;
}

const footTrafficByQtrGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      usePointStyle: true,
      callbacks: {
        label: populationTooltipLabel,
      },
    },
  },
  scales: {
    y: {
      suggestedMin: 0
    }                
  }
};

export function FootTrafficByQtrGraph(props) {
  const [data, setData] = useState({labels: [], datasets: []});
  const [isUpdated, setIsUpdated] = useState(false);
  const [ref, inView] = useInView({
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    const url = 'graph/foot-traffic-by-qtr' + (props.cityId ? '/' + props.cityId : '');
    if (!isUpdated && inView) {
      axios.get(url).then(response => {
        setData({
          labels: response.data.data.labels,
          datasets: [{
            ...response.data.data.datasets[0],
            ...LINE_CHART_STYLES[4],
          }],
        });
        setIsUpdated(true);
      }).catch(error => {
        console.log(error);
      });
    }
  }, [props.cityId, isUpdated, inView]);

  useEffect(() => {
    setData({labels: [], datasets: []});
    setIsUpdated(false);
  }, [props.cityId])

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='line' data={data} options={footTrafficByQtrGraphOptions} />
    </div>
  );
}

const footTrafficByCityGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      callbacks: {
        label: populationTooltipLabel,
      },
    },
  },
  scales: {
    y: {
      suggestedMin: 0,
    },                  
  },
};

export function FootTrafficByCityGraph() {
  const [data, setData] = useState({labels: [], datasets: []});
  const [ref, inView] = useInView({
    triggerOnce: true,
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    if (inView) {
      axios.get('graph/foot-traffic-by-city').then(response => {
        setData({
          labels: response.data.data.labels.map(code => CITY_NAMES[code]),
          datasets: [{
            ...response.data.data.datasets[0],
            backgroundColor: BACKGROUND_COLORS,
          }],
        });
      }).catch(error => {
        console.log(error);
      });
    }
  }, [inView]);

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='bar' data={data} options={footTrafficByCityGraphOptions} />
    </div>
  );
}

function currencyXAxisTooltipLabel(context) {
  let label = '';
  if (context.parsed.x !== null) {
    if (context.parsed.x >= 1000000000000) {
      label += new Intl.NumberFormat('ko', { maximumSignificantDigits: 4 }).format(context.parsed.x / 1000000000000) + '조원';
    } else if (context.parsed.x >= 100000000) {
      label += new Intl.NumberFormat('ko', { maximumSignificantDigits: 4 }).format(context.parsed.x / 100000000) + '억원';
    } else if (context.parsed.x >= 10000) {
      label += new Intl.NumberFormat('ko', { maximumSignificantDigits: 4 }).format(context.parsed.x / 10000) + '만원';
    } else {
      label += new Intl.NumberFormat().format(context.parsed.x) + '원';
    }
  }
  return label;
}

const salesBySectorGraphOptions = {
  maintainAspectRatio: false,
  indexAxis: 'y',
  interaction: {
    mode: 'y',
    intersect: false,
  },
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      callbacks: {
        label: currencyXAxisTooltipLabel,
      },
    },
  },
  scales: {
    x: {
      suggestedMin: 0,
    },         
  }
};

export function SalesBySectorGraph(props) {
  const [data1, setData1] = useState({labels: [], datasets: []});
  const [data2, setData2] = useState({labels: [], datasets: []});
  const options1 = {...salesBySectorGraphOptions, scales: { x: {...salesBySectorGraphOptions.scales.x, position: 'top'}}};
  const [options2, setOptions2] = useState(salesBySectorGraphOptions);
  const [isUpdated, setIsUpdated] = useState(false);
  const [ref, inView] = useInView({
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    const url = 'graph/sales-by-sector' + (props.cityId ? '/' + props.cityId : '');
    if (!isUpdated && inView) {
      axios.get(url).then(response => {
        const labelMaxLength = Math.max(...response.data.data.labels.map(label => label.length));
        setData1({
          labels: response.data.data.labels.slice(0, 3).map(label => label.padEnd(labelMaxLength, '　')),
          datasets: [{
            label: response.data.data.datasets[0].label,
            data: response.data.data.datasets[0].data.slice(0, 3),
            backgroundColor: BACKGROUND_COLORS.slice(0, 3),
          }],
        });
        setData2({
          labels: response.data.data.labels.slice(-3).map(label => label.padEnd(labelMaxLength, '　')),
          datasets: [{
            label: response.data.data.datasets[0].label,
            data: response.data.data.datasets[0].data.slice(-3),
            backgroundColor: BACKGROUND_COLORS.slice(-3),
          }],
        });
        setOptions2(prevOptions2 => {
          return {
            ...prevOptions2,
            scales: {
              x: {
                ...prevOptions2.scales.x,
                suggestedMax: response.data.data.datasets[0].data[3] * (Math.ceil(response.data.data.datasets[0].data[0] / response.data.data.datasets[0].data[2]) + 1),
              },
            },
          }
        });
        setIsUpdated(true);
      }).catch(error => {
        console.log(error);
      });
    }
  }, [props.cityId, isUpdated, inView]);

  useEffect(() => {
    setData1({labels: [], datasets: []});
    setData2({labels: [], datasets: []});
    setOptions2(salesBySectorGraphOptions)
    setIsUpdated(false);
  }, [props.cityId])

  return (
    <div ref={ref} style={chartContainerStyle}>
      <div style={{height: '50%'}}>
        <Chart type='bar' data={data1} options={options1} />
      </div>
      <div style={{height: '50%'}}>
        <Chart type='bar' data={data2} options={options2} />
      </div>
    </div>
  );
}

function percentageTooltipLabel(context) {
  let label = context.dataset.label || ''
  if (label) {
    label += ': '
  }
  if (context.parsed.y !== null) {
    label += new Intl.NumberFormat('ko', { style: 'percent', maximumFractionDigits: 2 }).format(context.parsed.y);
  }
  return label
}

const sectorSalesChangesByQtrGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      position: 'top',
      align: 'start',
      labels: {
        usePointStyle: true
      },
    },
    tooltip: {
      usePointStyle: true,
      callbacks: {
        label: percentageTooltipLabel,
      },
    },
  },
  scales: {
    y: {
      suggestedMin: 0,
    },                  
  },
};

export function SectorSalesChangesByQtrGraph(props) {
  const [data, setData] = useState({labels: [], datasets: []});
  const [isUpdated, setIsUpdated] = useState(false);
  const [ref, inView] = useInView({
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    const url = 'graph/sector-sales-changes-by-qtr' + (props.cityId ? '/' + props.cityId : '');
    if (!isUpdated && inView) {
      axios.get(url).then(response => {
        const datasets = []
        for (let i = 0; i < response.data.data.datasets.length; i++) {
          datasets.push({
            ...response.data.data.datasets[i],
            ...LINE_CHART_STYLES[i % 6],
          });
        }
        setData({
          labels: response.data.data.labels,
          datasets: datasets,
        });
        setIsUpdated(true);
      }).catch(error => {
        console.log(error);
      });
    }
  }, [props.cityId, isUpdated, inView]);

  useEffect(() => {
    setData({labels: [], datasets: []});
    setIsUpdated(false);
  }, [props.cityId])

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='line' data={data} options={sectorSalesChangesByQtrGraphOptions} />
    </div>
  );
}

const incomeExpenseByCityGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      display: false,
      position: 'top',
      align: 'start',
    },
    tooltip: {
      callbacks: {
        label: context => {
          let label = context.dataset.label || '';
          if (label) {
            label += ': '
          }
          return label + currencyTooltipLabel(context)
        },
      },
    },
  },
  scales: {
    x: {
      stacked: true,
    },   
    y: {
      stacked: true,
      suggestedMin: 0,
    },                  
  },
};

export function IncomeExpenseByCityGraph() {
  const [data, setData] = useState({labels: [], datasets: []});
  const [ref, inView] = useInView({
    triggerOnce: true,
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    if (inView) {
      axios.get('graph/income-expense-by-city').then(response => {
        setData({
          labels: response.data.data.labels.map(code => CITY_NAMES[code]),
          datasets: [
            {
              ...response.data.data.datasets[0],
              backgroundColor: BACKGROUND_COLORS,
            },
            // {
            //   label: response.data.data.datasets[1].label,
            //   data: response.data.data.datasets[1].data.map(value => -value),
            //   backgroundColor: BACKGROUND_COLORS[4],
            // },
          ],
        });
      }).catch(error => {
        console.log(error);
      });
    }
  }, [inView]);

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='bar' data={data} options={incomeExpenseByCityGraphOptions} />
    </div>
  );
}

const expenseByTypeGraphOptions = salesBySectorGraphOptions;

export function ExpenseByTypeGraph(props) {
  const [data, setData] = useState({labels: [], datasets: []});
  const [isUpdated, setIsUpdated] = useState(false);
  const [ref, inView] = useInView({
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    const url = 'graph/expense-by-type' + (props.cityId ? '/' + props.cityId : '');
    if (!isUpdated && inView) {
      axios.get(url).then(response => {
        setData({
          labels: response.data.data.labels,
          datasets: [{
            label: response.data.data.datasets[0].label,
            data: response.data.data.datasets[0].data,
            backgroundColor: BACKGROUND_COLORS,
          }],
        });
        setIsUpdated(true);
      }).catch(error => {
        console.log(error);
      });
    }
  }, [props.cityId, isUpdated, inView]);

  useEffect(() => {
    setData({labels: [], datasets: []});
    setIsUpdated(false);
  }, [props.cityId])

  return (
    <div ref={ref} style={chartContainerStyle}>
        <Chart type='bar' data={data} options={expenseByTypeGraphOptions} />
    </div>
  );
}

const typeExpenseChangesByQtrGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      position: 'top',
      align: 'start',
      labels: {
        usePointStyle: true
      }
    },
    tooltip: {
      usePointStyle: true,
      callbacks: {
        label: percentageTooltipLabel,
      },
    },
  },
  scales: {
    y: {
      suggestedMin: 0,
    },                  
  },
};

export function TypeExpenseChangesByQtrGraph(props) {
  const [data, setData] = useState({labels: [], datasets: []});
  const [isUpdated, setIsUpdated] = useState(false);
  const [ref, inView] = useInView({
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    const url = 'graph/type-expense-changes-by-qtr' + (props.cityId ? '/' + props.cityId : '');
    if (!isUpdated && inView) {
      axios.get(url).then(response => {
        const datasets = []
        for (let i = 0; i < response.data.data.datasets.length; i++) {
          datasets.push({
            ...response.data.data.datasets[i],
            ...LINE_CHART_STYLES[i % 6],
          });
        }
        setData({
          labels: response.data.data.labels,
          datasets: datasets,
        });
        setIsUpdated(true);
      }).catch(error => {
        console.log(error);
      });
    }
  }, [props.cityId, isUpdated, inView]);

  useEffect(() => {
    setData({labels: [], datasets: []});
    setIsUpdated(false);
  }, [props.cityId])

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='line' data={data} options={typeExpenseChangesByQtrGraphOptions} />
    </div>
  );
}

const facilitiesByCityGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      callbacks: {
        label: context => (context.parsed.y !== null) ? context.parsed.y : '',
      },
    },
  },
  scales: {
    y: {
      suggestedMin: 0,
    },                  
  },
};

export function FacilitiesByCityGraph() {
  const [data, setData] = useState({labels: [], datasets: []});
  const [ref, inView] = useInView({
    triggerOnce: true,
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    if (inView) {
      axios.get('graph/facilities-by-city').then(response => {
        setData({
          labels: response.data.data.labels.map(code => CITY_NAMES[code]),
          datasets: [{
            ...response.data.data.datasets[0],
            backgroundColor: BACKGROUND_COLORS,
          }],
        });
      }).catch(error => {
        console.log(error);
      });
    }
  }, [inView]);

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='bar' data={data} options={facilitiesByCityGraphOptions} />
    </div>
  );
}

const facilitiesByTypeGraphOptions = {
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      callbacks: {
        label: context => (context.parsed.y !== null) ? context.parsed.y : '',
      },
    },
  },
  scales: {
    y: {
      suggestedMin: 0,
    },                  
  },
};

export function FacilitiesByTypeGraph(props) {
  const [data, setData] = useState({labels: [], datasets: []});
  const [isUpdated, setIsUpdated] = useState(false);
  const [ref, inView] = useInView({
    rootMargin: '-100px 0px',
  });

  useEffect(() => {
    const url = 'graph/facilities-by-type' + (props.cityId ? '/' + props.cityId : '');
    if (!isUpdated && inView) {
      axios.get(url).then(response => {
        setData({
          labels: response.data.data.labels,
          datasets: [{
            ...response.data.data.datasets[0],
            backgroundColor: BACKGROUND_COLORS,
          }],
        });
        setIsUpdated(true);
      }).catch(error => {
        console.log(error);
      });
    }
  }, [props.cityId, isUpdated, inView]);

  useEffect(() => {
    setData({labels: [], datasets: []});
    setIsUpdated(false);
  }, [props.cityId])

  return (
    <div ref={ref} style={chartContainerStyle}>
      <Chart type='bar' data={data} options={facilitiesByTypeGraphOptions} />
    </div>
  );
}
