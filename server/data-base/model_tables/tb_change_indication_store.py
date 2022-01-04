from .db_connect import db

class Change_indication_store(db.Model):
    __tablename__ ='change_indication_store'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)
    commercial_change_ind	=	db.Column(db.String(5), nullable=False)
    commercial_change_ind_kr	=	db.Column(db.String(10), nullable=False)
    sales_month	=	db.Column(db.Integer, nullable=False)
    closed_month	=	db.Column(db.Integer, nullable=False)
    seoul_sales_month	=	db.Column(db.Integer, nullable=False)
    seoul_closed_month	=	db.Column(db.Integer, nullable=False)

    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, commercial_code, commercial_code_kr, commercial_change_ind, commercial_change_ind_kr, sales_month, closed_month, seoul_sales_month, seoul_closed_month):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.commercial_code_kr	=	commercial_code_kr
        self.commercial_change_ind	=	commercial_change_ind
        self.commercial_change_ind_kr	=	commercial_change_ind_kr
        self.sales_month	=	sales_month
        self.closed_month	=	closed_month
        self.seoul_sales_month	=	seoul_sales_month
        self.seoul_closed_month	=	seoul_closed_month

