from .db_connect import db

class District_city_kr(db.Model):
    __tablename__ ='district_city_kr'
    city_code	=	db.Column(db.Integer, primary_key = True, nullable=False)
    city_code_kr	=	db.Column(db.String(10), nullable=False)


    def __init__(self, city_code_kr, city_code):
        self.city_code_kr	=	city_code_kr
        self.city_code	=	city_code