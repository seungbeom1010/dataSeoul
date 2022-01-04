from .db_connect import db

class District_town_kr(db.Model):
    __tablename__ ='district_town_kr'
    town_code	=	db.Column(db.Integer, primary_key = True, nullable=False)
    town_code_kr	=	db.Column(db.String(10), nullable=False)



    def __init__(self, town_code_kr, town_code):
        self.town_code_kr	=	town_code_kr
        self.town_code	=	town_code