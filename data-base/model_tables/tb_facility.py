from .db_connect import db

class Facility(db.Model):
    __tablename__ ='facility'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)
    facility_count	=	db.Column(db.Integer, nullable=False)
    public_office	=	db.Column(db.Integer)
    bank	=	db.Column(db.Integer)
    hospital	=	db.Column(db.Integer)
    clinic	=	db.Column(db.Integer)
    pharmacy	=	db.Column(db.Integer)
    kindergarden	=	db.Column(db.Integer)
    elem_school	=	db.Column(db.Integer)
    mid_school	=	db.Column(db.Integer)
    high_school	=	db.Column(db.Integer)
    university	=	db.Column(db.Integer)
    dept_store	=	db.Column(db.Integer)
    supermarket	=	db.Column(db.Integer)
    theater	=	db.Column(db.Integer)
    accomm	=	db.Column(db.Integer)
    airport	=	db.Column(db.Integer)
    train_station	=	db.Column(db.Integer)
    bus_terminal	=	db.Column(db.Integer)
    subway_station	=	db.Column(db.Integer)
    bus_stop	=	db.Column(db.Integer)

    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, commercial_code, commercial_code_kr, facility_count, public_office, bank, hospital, clinic, pharmacy, kindergarden, elem_school, mid_school, high_school, university, dept_store, supermarket, theater, accomm, airport, train_station, bus_terminal, subway_station, bus_stop):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.commercial_code_kr	=	commercial_code_kr
        self.facility_count	=	facility_count
        self.public_office	=	public_office
        self.bank	=	bank
        self.hospital	=	hospital
        self.clinic	=	clinic
        self.pharmacy	=	pharmacy
        self.kindergarden	=	kindergarden
        self.elem_school	=	elem_school
        self.mid_school	=	mid_school
        self.high_school	=	high_school
        self.university	=	university
        self.dept_store	=	dept_store
        self.supermarket	=	supermarket
        self.theater	=	theater
        self.accomm	=	accomm
        self.airport	=	airport
        self.train_station	=	train_station
        self.bus_terminal	=	bus_terminal
        self.subway_station	=	subway_station
        self.bus_stop	=	bus_stop
