from flask import jsonify, Blueprint
from sqlalchemy import func
from models import Population_foot, District_map

from model_tables.db_connect import db

import pandas as pd

foot_traffic_graph = Blueprint('foot_traffic_graph',__name__)

@foot_traffic_graph.route('/graph/foot-traffic-by-qtr')
def foot_traffic_by_qtr():

    label=[]
    dataset = []

    get_dataset = Population_foot.query.\
        with_entities(Population_foot.base_year_code, Population_foot.base_qu_code, func.sum(Population_foot.total_foot).label('total_foot_sum')).\
        group_by(Population_foot.base_year_code, Population_foot.base_qu_code).\
        order_by(Population_foot.base_year_code, Population_foot.base_qu_code)

    for get_data in get_dataset:
        label.append(str(get_data.base_year_code)+'년도 '+str(get_data.base_qu_code)+'분기')
        dataset.append(int(get_data.total_foot_sum))

    data = {
        'labels' : label,
        'datasets' : [{
            'label': 1,
            'data' : dataset
        }]
    }

    return jsonify({'status':'success', 'data': data})

@foot_traffic_graph.route('/graph/foot-traffic-by-qtr/<city_code>')
def foot_traffic_by_qtr_city(city_code):

    label=[]
    dataset = []

    get_commercial_code = District_map.query.\
        with_entities(District_map.commercial_code).filter(District_map.city_code == city_code)
    df_commercial_code = pd.read_sql(get_commercial_code.statement, get_commercial_code.session.bind)
    list_commercial_code = df_commercial_code['commercial_code'].values.tolist()

    get_dataset = Population_foot.query.\
        with_entities(Population_foot.base_year_code, Population_foot.base_qu_code, func.sum(Population_foot.total_foot).label('total_foot_sum')).\
        group_by(Population_foot.base_year_code, Population_foot.base_qu_code).\
        filter(Population_foot.commercial_code.in_(list_commercial_code)).\
        order_by(Population_foot.base_year_code, Population_foot.base_qu_code)

    for get_data in get_dataset:
        label.append(str(get_data.base_year_code)+'년도 '+str(get_data.base_qu_code)+'분기')
        dataset.append(int(get_data.total_foot_sum))

    data = {
        'labels' : label,
        'datasets' : [{
            'label': city_code,
            'data' : dataset
        }]
    }

    return jsonify({'status':'success', 'data': data})

@foot_traffic_graph.route('/graph/foot-traffic-by-city')
def foot_traffic_by_city():

    label=[]
    dataset = []

    get_dataset = Population_foot.query.\
        join(District_map, Population_foot.commercial_code==District_map.commercial_code).\
        with_entities(District_map.city_code, District_map.city_code, func.sum(Population_foot.total_foot).label('total_foot_sum')).\
        group_by(District_map.city_code).\
        filter(Population_foot.base_year_code==2021, Population_foot.base_qu_code==2).\
        order_by(District_map.city_code)

    for get_data in get_dataset:
        label.append(int(get_data.city_code))
        dataset.append(int(get_data.total_foot_sum))

    data = {
        'labels' : label,
        'datasets' : [{
            'label': 'foot_traffic',
            'data' : dataset
        }]
    }

    return jsonify({'status':'success', 'data': data})