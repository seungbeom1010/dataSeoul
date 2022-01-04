from flask import jsonify, Blueprint
from sqlalchemy import func
from models import Estimated_sales, District_map

from model_tables.db_connect import db

import pandas as pd

sales_graph = Blueprint('sales_graph',__name__)

@sales_graph.route('/graph/sales-by-qtr')
def sales_by_qtr():

    label=[]
    dataset = []

    get_dataset = Estimated_sales.query.\
        with_entities(Estimated_sales.base_year_code, Estimated_sales.base_qu_code, func.sum(Estimated_sales.qu_sales_money).label('money_sum')).\
        group_by(Estimated_sales.base_year_code, Estimated_sales.base_qu_code).\
        order_by(Estimated_sales.base_year_code, Estimated_sales.base_qu_code)

    for get_data in get_dataset:
        label.append(str(get_data.base_year_code)+'년도 '+str(get_data.base_qu_code)+'분기')
        dataset.append(int(get_data.money_sum))

    data = {
        'labels' : label,
        'datasets' : [{
            'label': 1,
            'data' : dataset
        }]
    }
    
    return jsonify({'status':'success', 'data': data})

@sales_graph.route('/graph/sales-by-qtr/<city_code>')
def sales_by_qtr_city(city_code):

    label=[]
    dataset = []

    get_commercial_code = District_map.query.\
        with_entities(District_map.commercial_code).filter(District_map.city_code == city_code)
    df_commercial_code = pd.read_sql(get_commercial_code.statement, get_commercial_code.session.bind)
    list_commercial_code = df_commercial_code['commercial_code'].values.tolist()

    get_dataset = Estimated_sales.query.\
        with_entities(Estimated_sales.base_year_code, Estimated_sales.base_qu_code, func.sum(Estimated_sales.qu_sales_money).label('money_sum')).\
        group_by(Estimated_sales.base_year_code, Estimated_sales.base_qu_code).\
        filter(Estimated_sales.commercial_code.in_(list_commercial_code)).\
        order_by(Estimated_sales.base_year_code, Estimated_sales.base_qu_code)

    for get_data in get_dataset:
        label.append(str(get_data.base_year_code)+'년도 '+str(get_data.base_qu_code)+'분기')
        dataset.append(int(get_data.money_sum))

    data = {
        'labels' : label,
        'datasets' : [{
            'label': city_code,
            'data' : dataset
        }]
    }

    return jsonify({'status':'success', 'data': data})

@sales_graph.route('/graph/sales-by-city')
def sales_by_city():

    label=[]
    dataset = []

    get_dataset = Estimated_sales.query.\
        join(District_map, Estimated_sales.commercial_code==District_map.commercial_code).\
        with_entities(District_map.city_code, func.sum(Estimated_sales.qu_sales_money).label('money_sum')).\
        group_by(District_map.city_code).\
        filter(Estimated_sales.base_year_code==2021, Estimated_sales.base_qu_code==2).\
        order_by(District_map.city_code)

    for get_data in get_dataset:
        label.append(int(get_data.city_code))
        dataset.append(int(get_data.money_sum))

    data = {
        'labels' : label,
        'datasets' : [{
            'label': 'sales',
            'data' : dataset
        }]
    }

    return jsonify({'status':'success', 'data': data})