from .db_connect import db

class Income_expense_around(db.Model):
    __tablename__ ='income_expense_around'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)
    month_avg_income	=	db.Column(db.Integer, nullable=False)
    income_class_code	=	db.Column(db.Integer, nullable=False)
    total_expense	=	db.Column(db.Integer, nullable=False)
    food_expense	=	db.Column(db.Integer, nullable=False)
    clothing_expense	=	db.Column(db.Integer, nullable=False)
    daily_supply_expense	=	db.Column(db.Integer, nullable=False)
    medical_expense	=	db.Column(db.Integer, nullable=False)
    transportation_expense	=	db.Column(db.Integer, nullable=False)
    leisure_expense	=	db.Column(db.Integer, nullable=False)
    culture_expense	=	db.Column(db.Integer, nullable=False)
    education_expense	=	db.Column(db.Integer, nullable=False)
    entertainment_expense	=	db.Column(db.Integer, nullable=False)


    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, commercial_code, commercial_code_kr, month_avg_income, income_class_code, total_expense, food_expense, clothing_expense, daily_supply_expense, medical_expense, transportation_expense, leisure_expense, culture_expense, education_expense, entertainment_expense):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.commercial_code_kr	=	commercial_code_kr
        self.month_avg_income	=	month_avg_income
        self.income_class_code	=	income_class_code
        self.total_expense	=	total_expense
        self.food_expense	=	food_expense
        self.clothing_expense	=	clothing_expense
        self.daily_supply_expense	=	daily_supply_expense
        self.medical_expense	=	medical_expense
        self.transportation_expense	=	transportation_expense
        self.leisure_expense	=	leisure_expense
        self.culture_expense	=	culture_expense
        self.education_expense	=	education_expense
        self.entertainment_expense	=	entertainment_expense