from flask import jsonify, Blueprint
from sqlalchemy import func, desc
from models import Estimated_sales, District_map

from model_tables.db_connect import db

import pandas as pd
# import numpy as np

sector_sales_graph = Blueprint('sector_sales_graph',__name__)

@sector_sales_graph.route('/graph/sales-by-sector')
def sector_by_sales():

    get_dataset = Estimated_sales.query.\
        with_entities(Estimated_sales.service_industry_code_kr, func.avg(Estimated_sales.qu_sales_money).label('money_sum')).\
        group_by(Estimated_sales.service_industry_code).\
        filter(Estimated_sales.base_year_code==2021, Estimated_sales.base_qu_code==2).\
        order_by(desc('money_sum'))

    df_dataset = pd.read_sql(get_dataset.statement, get_dataset.session.bind)
    df_dataset_limit = pd.concat([df_dataset[:3], df_dataset[-3:]])
    label = df_dataset_limit['service_industry_code_kr'].values.tolist()
    # use numpy for change data_type to int
    # dataset = df_dataset_limit['money_sum'].astype(np.uint).values.tolist()
    dataset = df_dataset_limit['money_sum'].values.tolist()
    dataset = [int (i) for i in dataset]

    data = {
        'labels' : label,
        'datasets' : [{
            'label': 1,
            'data' : dataset
        }]
    }
    
    return jsonify({'status':'success', 'data': data})

@sector_sales_graph.route('/graph/sales-by-sector/<city_code>')
def sector_by_sales_city(city_code):

    get_commercial_code = District_map.query.\
        with_entities(District_map.commercial_code).filter(District_map.city_code == city_code)
    df_commercial_code = pd.read_sql(get_commercial_code.statement, get_commercial_code.session.bind)
    list_commercial_code = df_commercial_code['commercial_code'].values.tolist()

    get_dataset = Estimated_sales.query.\
        with_entities(Estimated_sales.service_industry_code_kr, func.avg(Estimated_sales.qu_sales_money).label('money_sum')).\
        group_by(Estimated_sales.service_industry_code).\
        filter(Estimated_sales.base_year_code==2021, Estimated_sales.base_qu_code==2, Estimated_sales.commercial_code.in_(list_commercial_code)).\
        order_by(desc('money_sum'))

    df_dataset = pd.read_sql(get_dataset.statement, get_dataset.session.bind)
    df_dataset_limit = pd.concat([df_dataset[:3], df_dataset[-3:]])
    label = df_dataset_limit['service_industry_code_kr'].values.tolist()
    dataset = df_dataset_limit['money_sum'].values.tolist()
    dataset = [int (i) for i in dataset]

    data = {
        'labels' : label,
        'datasets' : [{
            'label': city_code,
            'data' : dataset
        }]
    }
    
    return jsonify({'status':'success', 'data': data})