from .db_connect import db

class District_map(db.Model):
    __tablename__ ='district_map'
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, primary_key = True, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)
    x_coordi	=	db.Column(db.Integer, nullable=False)
    y_coordi	=	db.Column(db.Integer, nullable=False)
    city_code	=	db.Column(db.Integer, nullable=False)
    town_code	=	db.Column(db.Integer, nullable=False)
    latitude	=	db.Column(db.Integer, nullable=False)
    longitude	=	db.Column(db.Integer, nullable=False)


    def __init__(self, commercial_class_code, commercial_class_code_kr, commercial_code, commercial_code_kr, x_coordi, y_coordi, city_code, town_code, latitude, longitude):
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.commercial_code_kr	=	commercial_code_kr
        self.x_coordi	=	x_coordi
        self.y_coordi	=	y_coordi
        self.city_code	=	city_code
        self.town_code	=	town_code
        self.latitude	=	latitude
        self.longitude	=	longitude
