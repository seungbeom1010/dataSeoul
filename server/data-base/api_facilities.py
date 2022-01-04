from flask import jsonify, Blueprint
from sqlalchemy import func
from models import Facility, District_map

from model_tables.db_connect import db

import pandas as pd

facilities_graph = Blueprint('facilities_graph',__name__)

@facilities_graph.route('/graph/facilities-by-city')
def facilities_by_city():

    label = []
    dataset = []

    get_dataset = Facility.query.\
        join(District_map, Facility.commercial_code==District_map.commercial_code).\
        with_entities(District_map.city_code, func.sum(Facility.facility_count).label('facility_count')).\
        group_by(District_map.city_code).\
        order_by(District_map.city_code)

    for get_data in get_dataset:
        label.append(int(get_data.city_code))
        dataset.append(int(get_data.facility_count))

    data = {
        'labels' : label, # [구]
        'datasets' : [{
            'label': 'facilities', 
            'data' : dataset # [구별 집객시설 총 수]
        }]
    }
    
    return jsonify({'status':'success', 'data': data})

@facilities_graph.route('/graph/facilities-by-type')
def facilities_by_type():

    dataset = []

    facilities = [m.key for m in Facility.__table__.columns] 
    label = facilities[8:] # 집객시설 종류 public_office ~ bus_stop ... 19개 columns 

    get_dataset = Facility.query.\
        with_entities(func.sum(Facility.public_office).label('public_office'), func.sum(Facility.bank).label('bank'), func.sum(Facility.hospital).label('hospital'), func.sum(Facility.clinic).label('clinic'), func.sum(Facility.pharmacy).label('pharmacy'), func.sum(Facility.kindergarden).label('kindergarden'), func.sum(Facility.elem_school).label('elem_school'), func.sum(Facility.mid_school).label('mid_school'), func.sum(Facility.high_school).label('high_school'), func.sum(Facility.university).label('university'), func.sum(Facility.dept_store).label('dept_store'), func.sum(Facility.supermarket).label('supermarket'), func.sum(Facility.theater).label('theater'), func.sum(Facility.accomm).label('accomm'), func.sum(Facility.airport).label('airport'), func.sum(Facility.train_station).label('train_station'), func.sum(Facility.bus_terminal).label('bus_terminal'), func.sum(Facility.subway_station).label('subway_station'), func.sum(Facility.bus_stop).label('bus_stop')).\
        filter(Facility.base_year_code==2021, Facility.base_qu_code==2).one()

    for get_data in get_dataset:
        if get_data == None:
            dataset.append(0)
        else:
            dataset.append(int(get_data))

    data = {
        'labels' : label, # [집객시설 종류]
        'datasets' : [{
            'label': 1,
            'data' : dataset # [각 시설 수]
        }]
    }
    
    return jsonify({'status':'success', 'data': data})

@facilities_graph.route('/graph/facilities-by-type/<city_code>')
def facilities_by_type_qtr(city_code):

    label = []
    dataset = []

    facilities = [m.key for m in Facility.__table__.columns] 
    label = facilities[8:] # 19개 columns

    get_commercial_code = District_map.query.\
        with_entities(District_map.commercial_code).filter(District_map.city_code == city_code)
    df_commercial_code = pd.read_sql(get_commercial_code.statement, get_commercial_code.session.bind)
    list_commercial_code = df_commercial_code['commercial_code'].values.tolist()

    get_dataset = Facility.query.\
        with_entities(func.sum(Facility.public_office).label('public_office'), func.sum(Facility.bank).label('bank'), func.sum(Facility.hospital).label('hospital'), func.sum(Facility.clinic).label('clinic'), func.sum(Facility.pharmacy).label('pharmacy'), func.sum(Facility.kindergarden).label('kindergarden'), func.sum(Facility.elem_school).label('elem_school'), func.sum(Facility.mid_school).label('mid_school'), func.sum(Facility.high_school).label('high_school'), func.sum(Facility.university).label('university'), func.sum(Facility.dept_store).label('dept_store'), func.sum(Facility.supermarket).label('supermarket'), func.sum(Facility.theater).label('theater'), func.sum(Facility.accomm).label('accomm'), func.sum(Facility.airport).label('airport'), func.sum(Facility.train_station).label('train_station'), func.sum(Facility.bus_terminal).label('bus_terminal'), func.sum(Facility.subway_station).label('subway_station'), func.sum(Facility.bus_stop).label('bus_stop')).\
        filter(Facility.base_year_code==2021, Facility.base_qu_code==2, Facility.commercial_code.in_(list_commercial_code)).one()

    for get_data in get_dataset:
        if get_data == None:
            dataset.append(0)
        else:
            dataset.append(int(get_data))

    data = {
        'labels' : label, # [집객시설 종류]
        'datasets' : [{
            'label': city_code, # [구]
            'data' : dataset # [각 시설 수]
        }]
    }

    return jsonify({'status':'success', 'data': data})
