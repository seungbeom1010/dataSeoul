from .db_connect import db

class Covid_qu_city(db.Model):
    __tablename__ = 'covid_qu_city'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    date = db.Column(db.Integer, nullable=False)
    date_kr = db.Column(db.String(20), nullable=False)
    city_code_kr = db.Column(db.String(20), nullable=False)
    covid_population = db.Column(db.Integer, nullable=False)

    def __init__(self, id, date, date_kr, city_code_kr, covid_population):
        self.id = id
        self.date = date
        self.date_kr = date_kr
        self.city_code_kr = city_code_kr
        self.covid_population = covid_population