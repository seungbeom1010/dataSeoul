from .db_connect import db

class Estimated_sales(db.Model):
    __tablename__= 'estimated_sales'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)
    service_industry_code	=	db.Column(db.String(10), nullable=False)
    service_industry_code_kr	=	db.Column(db.String(15), nullable=False)
    qu_sales_money	=	db.Column(db.BigInteger, nullable=False)
    qu_sales_count	=	db.Column(db.Integer, nullable=False)
    weekday_sales_rate	=	db.Column(db.Integer, nullable=False)
    weekend_sales_rate	=	db.Column(db.Integer, nullable=False)
    mon_sales_rate	=	db.Column(db.Integer, nullable=False)
    tue_sales_rate	=	db.Column(db.Integer, nullable=False)
    wed_sales_rate	=	db.Column(db.Integer, nullable=False)
    thu_sales_rate	=	db.Column(db.Integer, nullable=False)
    fri_sales_rate	=	db.Column(db.Integer, nullable=False)
    sat_sales_rate	=	db.Column(db.Integer, nullable=False)
    sun_sales_rate	=	db.Column(db.Integer, nullable=False)
    t00t06_sales_rate	=	db.Column(db.Integer, nullable=False)
    t06t11_sales_rate	=	db.Column(db.Integer, nullable=False)
    t11t14_sales_rate	=	db.Column(db.Integer, nullable=False)
    t14t17_sales_rate	=	db.Column(db.Integer, nullable=False)
    t17t21_sales_rate	=	db.Column(db.Integer, nullable=False)
    t21t24_sales_rate	=	db.Column(db.Integer, nullable=False)
    M_sales_rate	=	db.Column(db.Integer, nullable=False)
    F_sales_rate	=	db.Column(db.Integer, nullable=False)
    age_10_sales_rate	=	db.Column(db.Integer, nullable=False)
    age_20_sales_rate	=	db.Column(db.Integer, nullable=False)
    age_30_sales_rate	=	db.Column(db.Integer, nullable=False)
    age_40_sales_rate	=	db.Column(db.Integer, nullable=False)
    age_50_sales_rate	=	db.Column(db.Integer, nullable=False)
    age_60_sales_rate	=	db.Column(db.Integer, nullable=False)
    weekday_sales_money	=	db.Column(db.BigInteger, nullable=False)
    weekend_sales_money	=	db.Column(db.BigInteger, nullable=False)
    mon_sales_money	=	db.Column(db.BigInteger, nullable=False)
    tue_sales_money	=	db.Column(db.BigInteger, nullable=False)
    wed_sales_money	=	db.Column(db.BigInteger, nullable=False)
    thu_sales_money	=	db.Column(db.BigInteger, nullable=False)
    fri_sales_money	=	db.Column(db.BigInteger, nullable=False)
    sat_sales_money	=	db.Column(db.BigInteger, nullable=False)
    sun_sales_money	=	db.Column(db.BigInteger, nullable=False)
    t00t06_sales_money	=	db.Column(db.BigInteger, nullable=False)
    t06t11_sales_money	=	db.Column(db.BigInteger, nullable=False)
    t11t14_sales_money	=	db.Column(db.BigInteger, nullable=False)
    t14t17_sales_money	=	db.Column(db.BigInteger, nullable=False)
    t17t21_sales_money	=	db.Column(db.BigInteger, nullable=False)
    t21t24_sales_money	=	db.Column(db.BigInteger, nullable=False)
    M_sales_money	=	db.Column(db.BigInteger, nullable=False)
    F_sales_money	=	db.Column(db.BigInteger, nullable=False)
    age_10_sales_money	=	db.Column(db.BigInteger, nullable=False)
    age_20_sales_money	=	db.Column(db.BigInteger, nullable=False)
    age_30_sales_money	=	db.Column(db.BigInteger, nullable=False)
    age_40_sales_money	=	db.Column(db.BigInteger, nullable=False)
    age_50_sales_money	=	db.Column(db.BigInteger, nullable=False)
    age_60_sales_money	=	db.Column(db.BigInteger, nullable=False)
    weekday_sales_count	=	db.Column(db.Integer, nullable=False)
    weekend_sales_count	=	db.Column(db.Integer, nullable=False)
    mon_sales_count	=	db.Column(db.Integer, nullable=False)
    tue_sales_count	=	db.Column(db.Integer, nullable=False)
    wed_sales_count	=	db.Column(db.Integer, nullable=False)
    thu_sales_count	=	db.Column(db.Integer, nullable=False)
    fri_sales_count	=	db.Column(db.Integer, nullable=False)
    sat_sales_count	=	db.Column(db.Integer, nullable=False)
    sun_sales_count	=	db.Column(db.Integer, nullable=False)
    t00t06_sales_count	=	db.Column(db.Integer, nullable=False)
    t06t11_sales_count	=	db.Column(db.Integer, nullable=False)
    t11t14_sales_count	=	db.Column(db.Integer, nullable=False)
    t14t17_sales_count	=	db.Column(db.Integer, nullable=False)
    t17t21_sales_count	=	db.Column(db.Integer, nullable=False)
    t21t24_sales_count	=	db.Column(db.Integer, nullable=False)
    M_sales_count	=	db.Column(db.Integer, nullable=False)
    F_sales_count	=	db.Column(db.Integer, nullable=False)
    age_10_sales_count	=	db.Column(db.Integer, nullable=False)
    age_20_sales_count	=	db.Column(db.Integer, nullable=False)
    age_30_sales_count	=	db.Column(db.Integer, nullable=False)
    age_40_sales_count	=	db.Column(db.Integer, nullable=False)
    age_50_sales_count	=	db.Column(db.Integer, nullable=False)
    age_60_sales_count	=	db.Column(db.Integer, nullable=False)
    store_count	=	db.Column(db.Integer, nullable=False)

    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, commercial_code, commercial_code_kr, service_industry_code, service_industry_code_kr, qu_sales_money, qu_sales_count, weekday_sales_rate, weekend_sales_rate, mon_sales_rate, tue_sales_rate, wed_sales_rate, thu_sales_rate, fri_sales_rate, sat_sales_rate, sun_sales_rate, t00t06_sales_rate, t06t11_sales_rate, t11t14_sales_rate, t14t17_sales_rate, t17t21_sales_rate, t21t24_sales_rate, M_sales_rate, F_sales_rate, age_10_sales_rate, age_20_sales_rate, age_30_sales_rate, age_40_sales_rate, age_50_sales_rate, age_60_sales_rate, weekday_sales_money, weekend_sales_money, mon_sales_money, tue_sales_money, wed_sales_money, thu_sales_money, fri_sales_money, sat_sales_money, sun_sales_money, t00t06_sales_money, t06t11_sales_money, t11t14_sales_money, t14t17_sales_money, t17t21_sales_money, t21t24_sales_money, M_sales_money, F_sales_money, age_10_sales_money, age_20_sales_money, age_30_sales_money, age_40_sales_money, age_50_sales_money, age_60_sales_money, weekday_sales_count, weekend_sales_count, mon_sales_count, tue_sales_count, wed_sales_count, thu_sales_count, fri_sales_count, sat_sales_count, sun_sales_count, t00t06_sales_count, t06t11_sales_count, t11t14_sales_count, t14t17_sales_count, t17t21_sales_count, t21t24_sales_count, M_sales_count, F_sales_count, age_10_sales_count, age_20_sales_count, age_30_sales_count, age_40_sales_count, age_50_sales_count, age_60_sales_count, store_count):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.commercial_code_kr	=	commercial_code_kr
        self.service_industry_code	=	service_industry_code
        self.service_industry_code_kr	=	service_industry_code_kr
        self.qu_sales_money	=	qu_sales_money
        self.qu_sales_count	=	qu_sales_count
        self.weekday_sales_rate	=	weekday_sales_rate
        self.weekend_sales_rate	=	weekend_sales_rate
        self.mon_sales_rate	=	mon_sales_rate
        self.tue_sales_rate	=	tue_sales_rate
        self.wed_sales_rate	=	wed_sales_rate
        self.thu_sales_rate	=	thu_sales_rate
        self.fri_sales_rate	=	fri_sales_rate
        self.sat_sales_rate	=	sat_sales_rate
        self.sun_sales_rate	=	sun_sales_rate
        self.t00t06_sales_rate	=	t00t06_sales_rate
        self.t06t11_sales_rate	=	t06t11_sales_rate
        self.t11t14_sales_rate	=	t11t14_sales_rate
        self.t14t17_sales_rate	=	t14t17_sales_rate
        self.t17t21_sales_rate	=	t17t21_sales_rate
        self.t21t24_sales_rate	=	t21t24_sales_rate
        self.M_sales_rate	=	M_sales_rate
        self.F_sales_rate	=	F_sales_rate
        self.age_10_sales_rate	=	age_10_sales_rate
        self.age_20_sales_rate	=	age_20_sales_rate
        self.age_30_sales_rate	=	age_30_sales_rate
        self.age_40_sales_rate	=	age_40_sales_rate
        self.age_50_sales_rate	=	age_50_sales_rate
        self.age_60_sales_rate	=	age_60_sales_rate
        self.weekday_sales_money	=	weekday_sales_money
        self.weekend_sales_money	=	weekend_sales_money
        self.mon_sales_money	=	mon_sales_money
        self.tue_sales_money	=	tue_sales_money
        self.wed_sales_money	=	wed_sales_money
        self.thu_sales_money	=	thu_sales_money
        self.fri_sales_money	=	fri_sales_money
        self.sat_sales_money	=	sat_sales_money
        self.sun_sales_money	=	sun_sales_money
        self.t00t06_sales_money	=	t00t06_sales_money
        self.t06t11_sales_money	=	t06t11_sales_money
        self.t11t14_sales_money	=	t11t14_sales_money
        self.t14t17_sales_money	=	t14t17_sales_money
        self.t17t21_sales_money	=	t17t21_sales_money
        self.t21t24_sales_money	=	t21t24_sales_money
        self.M_sales_money	=	M_sales_money
        self.F_sales_money	=	F_sales_money
        self.age_10_sales_money	=	age_10_sales_money
        self.age_20_sales_money	=	age_20_sales_money
        self.age_30_sales_money	=	age_30_sales_money
        self.age_40_sales_money	=	age_40_sales_money
        self.age_50_sales_money	=	age_50_sales_money
        self.age_60_sales_money	=	age_60_sales_money
        self.weekday_sales_count	=	weekday_sales_count
        self.weekend_sales_count	=	weekend_sales_count
        self.mon_sales_count	=	mon_sales_count
        self.tue_sales_count	=	tue_sales_count
        self.wed_sales_count	=	wed_sales_count
        self.thu_sales_count	=	thu_sales_count
        self.fri_sales_count	=	fri_sales_count
        self.sat_sales_count	=	sat_sales_count
        self.sun_sales_count	=	sun_sales_count
        self.t00t06_sales_count	=	t00t06_sales_count
        self.t06t11_sales_count	=	t06t11_sales_count
        self.t11t14_sales_count	=	t11t14_sales_count
        self.t14t17_sales_count	=	t14t17_sales_count
        self.t17t21_sales_count	=	t17t21_sales_count
        self.t21t24_sales_count	=	t21t24_sales_count
        self.M_sales_count	=	M_sales_count
        self.F_sales_count	=	F_sales_count
        self.age_10_sales_count	=	age_10_sales_count
        self.age_20_sales_count	=	age_20_sales_count
        self.age_30_sales_count	=	age_30_sales_count
        self.age_40_sales_count	=	age_40_sales_count
        self.age_50_sales_count	=	age_50_sales_count
        self.age_60_sales_count	=	age_60_sales_count
        self.store_count	=	store_count
