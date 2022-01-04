from .db_connect import db

class People_per_ground(db.Model):
    __tablename__ ='people_per_ground'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    city_town_code	=	db.Column(db.String(50), nullable=False)
    exist_population_per_road	=	db.Column(db.Integer, nullable=False)
    exist_population_per_building	=	db.Column(db.Integer, nullable=False)
    house_population_per_ha	=	db.Column(db.Integer, nullable=False)
    office_population_per_ha	=	db.Column(db.Integer, nullable=False)


    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, city_town_code, exist_population_per_road, exist_population_per_building, house_population_per_ha, office_population_per_ha):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.city_town_code	=	city_town_code
        self.exist_population_per_road	=	exist_population_per_road
        self.exist_population_per_building	=	exist_population_per_building
        self.house_population_per_ha	=	house_population_per_ha
        self.office_population_per_ha	=	office_population_per_ha