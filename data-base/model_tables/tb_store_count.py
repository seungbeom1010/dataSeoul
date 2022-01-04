from .db_connect import db

class Store_count(db.Model):
    __tablename__ ='store_count'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)
    service_industry_code	=	db.Column(db.String(10), nullable=False)
    service_industry_code_kr	=	db.Column(db.String(15), nullable=False)
    general_store_count	=	db.Column(db.Integer, nullable=False)
    store_count	=	db.Column(db.Integer, nullable=False)
    open_store_rate	=	db.Column(db.Integer, nullable=False)
    open_store	=	db.Column(db.Integer, nullable=False)
    closed_store_rate	=	db.Column(db.Integer, nullable=False)
    closed_store	=	db.Column(db.Integer, nullable=False)
    franchise_store_count	=	db.Column(db.Integer, nullable=False)

    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, commercial_code, commercial_code_kr, service_industry_code, service_industry_code_kr, general_store_count, store_count, open_store_rate, open_store, closed_store_rate, closed_store, franchise_store_count):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.commercial_code_kr	=	commercial_code_kr
        self.service_industry_code	=	service_industry_code
        self.service_industry_code_kr	=	service_industry_code_kr
        self.general_store_count	=	general_store_count
        self.store_count	=	store_count
        self.open_store_rate	=	open_store_rate
        self.open_store	=	open_store
        self.closed_store_rate	=	closed_store_rate
        self.closed_store	=	closed_store
        self.franchise_store_count	=	franchise_store_count