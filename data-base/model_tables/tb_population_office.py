from .db_connect import db

class Population_office(db.Model):
    __tablename__ ='population_office'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)
    total_office	=	db.Column(db.Integer, nullable=False)
    M_office	=	db.Column(db.Integer, nullable=False)
    F_office	=	db.Column(db.Integer, nullable=False)
    age_10_office	=	db.Column(db.Integer, nullable=False)
    age_20_office	=	db.Column(db.Integer, nullable=False)
    age_30_office	=	db.Column(db.Integer, nullable=False)
    age_40_office	=	db.Column(db.Integer, nullable=False)
    age_50_office	=	db.Column(db.Integer, nullable=False)
    age_60_office	=	db.Column(db.Integer, nullable=False)
    M_age_10_office	=	db.Column(db.Integer, nullable=False)
    M_age_20_office	=	db.Column(db.Integer, nullable=False)
    M_age_30_office	=	db.Column(db.Integer, nullable=False)
    M_age_40_office	=	db.Column(db.Integer, nullable=False)
    M_age_50_office	=	db.Column(db.Integer, nullable=False)
    M_age_60_office	=	db.Column(db.Integer, nullable=False)
    F_age_10_office	=	db.Column(db.Integer, nullable=False)
    F_age_20_office	=	db.Column(db.Integer, nullable=False)
    F_age_30_office	=	db.Column(db.Integer, nullable=False)
    F_age_40_office	=	db.Column(db.Integer, nullable=False)
    F_age_50_office	=	db.Column(db.Integer, nullable=False)
    F_age_60_office	=	db.Column(db.Integer, nullable=False)


    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, commercial_code, commercial_code_kr, total_office, M_office, F_office, age_10_office, age_20_office, age_30_office, age_40_office, age_50_office, age_60_office, M_age_10_office, M_age_20_office, M_age_30_office, M_age_40_office, M_age_50_office, M_age_60_office, F_age_10_office, F_age_20_office, F_age_30_office, F_age_40_office, F_age_50_office, F_age_60_office):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.commercial_code_kr	=	commercial_code_kr
        self.total_office	=	total_office
        self.M_office	=	M_office
        self.F_office	=	F_office
        self.age_10_office	=	age_10_office
        self.age_20_office	=	age_20_office
        self.age_30_office	=	age_30_office
        self.age_40_office	=	age_40_office
        self.age_50_office	=	age_50_office
        self.age_60_office	=	age_60_office
        self.M_age_10_office	=	M_age_10_office
        self.M_age_20_office	=	M_age_20_office
        self.M_age_30_office	=	M_age_30_office
        self.M_age_40_office	=	M_age_40_office
        self.M_age_50_office	=	M_age_50_office
        self.M_age_60_office	=	M_age_60_office
        self.F_age_10_office	=	F_age_10_office
        self.F_age_20_office	=	F_age_20_office
        self.F_age_30_office	=	F_age_30_office
        self.F_age_40_office	=	F_age_40_office
        self.F_age_50_office	=	F_age_50_office
        self.F_age_60_office	=	F_age_60_office
