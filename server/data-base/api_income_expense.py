from flask import jsonify, Blueprint
from sqlalchemy import func, desc
from models import Income_expense_around, District_map

from model_tables.db_connect import db

import pandas as pd

income_expense_graph = Blueprint('income_expense_graph',__name__)

@income_expense_graph.route('/graph/income-expense-by-city')
def income_expense_by_city():
    label=[]
    in_dataset = []
    ex_dataset = []

    get_dataset = Income_expense_around.query.\
        join(District_map, Income_expense_around.commercial_code==District_map.commercial_code).\
        with_entities(District_map.city_code, func.avg(Income_expense_around.month_avg_income).label('income_avg'), func.avg(Income_expense_around.total_expense).label('expense_avg')).\
        group_by(District_map.city_code).\
        filter(Income_expense_around.base_year_code==2021, Income_expense_around.base_qu_code==2).\
        order_by(District_map.city_code)

    for get_data in get_dataset:
        label.append(int(get_data.city_code))
        in_dataset.append(int(get_data.income_avg))
        ex_dataset.append(int(get_data.expense_avg / 3))

    data = {
        'labels' : label,
        'datasets' : [{
            'label': 'income',
            'data' : in_dataset
        },
        {
            'label': 'expense',
            'data' : ex_dataset
        }]
    }
    
    return jsonify({'status':'success', 'data': data})


@income_expense_graph.route('/graph/expense-by-type')
def expense_by_type():

    get_dataset = Income_expense_around.query.\
        with_entities(func.sum(Income_expense_around.food_expense).label('food_expense'), func.sum(Income_expense_around.culture_expense).label('culture_expense'), func.sum(Income_expense_around.leisure_expense).label('leisure_expense'), func.sum(Income_expense_around.medical_expense).label('medical_expense'), func.sum(Income_expense_around.clothing_expense).label('clothing_expense'), func.sum(Income_expense_around.education_expense).label('education_expense'), func.sum(Income_expense_around.daily_supply_expense).label('daily_supply_expense'), func.sum(Income_expense_around.entertainment_expense).label('entertainment_expense'), func.sum(Income_expense_around.transportation_expense).label('transportation_expense')).\
        filter(Income_expense_around.base_year_code==2021, Income_expense_around.base_qu_code==2).one()
    label = []
    for data in get_dataset.keys():
        label.append(data)
    ex_dataset = []
    for get_data in get_dataset:
        ex_dataset.append(int(get_data))
    data = {
        'labels' : label,
        'datasets' : [{
            'label': 'expense',
            'data' : ex_dataset
        }]
    }
    
    return jsonify({'status':'success', 'data': data})