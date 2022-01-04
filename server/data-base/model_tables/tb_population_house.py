
from .db_connect import db

class Population_house(db.Model):
    __tablename__ ='population_house'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, nullable=False)
    total_house	=	db.Column(db.Integer, nullable=False)
    M_house	=	db.Column(db.Integer, nullable=False)
    F_house	=	db.Column(db.Integer, nullable=False)
    age_10_house	=	db.Column(db.Integer, nullable=False)
    age_20_house	=	db.Column(db.Integer, nullable=False)
    age_30_house	=	db.Column(db.Integer, nullable=False)
    age_40_house	=	db.Column(db.Integer, nullable=False)
    age_50_house	=	db.Column(db.Integer, nullable=False)
    age_60_house	=	db.Column(db.Integer, nullable=False)
    M_age_10_house	=	db.Column(db.Integer, nullable=False)
    M_age_20_house	=	db.Column(db.Integer, nullable=False)
    M_age_30_house	=	db.Column(db.Integer, nullable=False)
    M_age_40_house	=	db.Column(db.Integer, nullable=False)
    M_age_50_house	=	db.Column(db.Integer, nullable=False)
    M_age_60_house	=	db.Column(db.Integer, nullable=False)
    F_age_10_house	=	db.Column(db.Integer, nullable=False)
    F_age_20_house	=	db.Column(db.Integer, nullable=False)
    F_age_30_house	=	db.Column(db.Integer, nullable=False)
    F_age_40_house	=	db.Column(db.Integer, nullable=False)
    F_age_50_house	=	db.Column(db.Integer, nullable=False)
    F_age_60_house	=	db.Column(db.Integer, nullable=False)
    total_household_count	=	db.Column(db.Integer, nullable=False)
    apt_household_count	=	db.Column(db.Integer, nullable=False)
    non_apt_household_count	=	db.Column(db.Integer, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)


    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, commercial_code, total_house, M_house, F_house, age_10_house, age_20_house, age_30_house, age_40_house, age_50_house, age_60_house, M_age_10_house, M_age_20_house, M_age_30_house, M_age_40_house, M_age_50_house, M_age_60_house, F_age_10_house, F_age_20_house, F_age_30_house, F_age_40_house, F_age_50_house, F_age_60_house, total_household_count, apt_household_count, non_apt_household_count, commercial_code_kr):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.total_house	=	total_house
        self.M_house	=	M_house
        self.F_house	=	F_house
        self.age_10_house	=	age_10_house
        self.age_20_house	=	age_20_house
        self.age_30_house	=	age_30_house
        self.age_40_house	=	age_40_house
        self.age_50_house	=	age_50_house
        self.age_60_house	=	age_60_house
        self.M_age_10_house	=	M_age_10_house
        self.M_age_20_house	=	M_age_20_house
        self.M_age_30_house	=	M_age_30_house
        self.M_age_40_house	=	M_age_40_house
        self.M_age_50_house	=	M_age_50_house
        self.M_age_60_house	=	M_age_60_house
        self.F_age_10_house	=	F_age_10_house
        self.F_age_20_house	=	F_age_20_house
        self.F_age_30_house	=	F_age_30_house
        self.F_age_40_house	=	F_age_40_house
        self.F_age_50_house	=	F_age_50_house
        self.F_age_60_house	=	F_age_60_house
        self.total_household_count	=	total_household_count
        self.apt_household_count	=	apt_household_count
        self.non_apt_household_count	=	non_apt_household_count
        self.commercial_code_kr	=	commercial_code_kr
