from .db_connect import db

class Population_foot(db.Model):
    __tablename__= 'population_foot'
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    base_year_code	=	db.Column(db.Integer, nullable=False)
    base_qu_code	=	db.Column(db.Integer, nullable=False)
    commercial_class_code	=	db.Column(db.String(2), nullable=False)
    commercial_class_code_kr	=	db.Column(db.String(10), nullable=False)
    commercial_code	=	db.Column(db.Integer, nullable=False)
    commercial_code_kr	=	db.Column(db.String(50), nullable=False)
    total_foot	=	db.Column(db.Integer, nullable=False)
    M_foot	=	db.Column(db.Integer, nullable=False)
    F_foot	=	db.Column(db.Integer, nullable=False)
    age_10_foot	=	db.Column(db.Integer, nullable=False)
    age_20_foot	=	db.Column(db.Integer, nullable=False)
    age_30_foot	=	db.Column(db.Integer, nullable=False)
    age_40_foot	=	db.Column(db.Integer, nullable=False)
    age_50_foot	=	db.Column(db.Integer, nullable=False)
    age_60_foot	=	db.Column(db.Integer, nullable=False)
    t00t06_foot	=	db.Column(db.Integer, nullable=False)
    t06t11_foot	=	db.Column(db.Integer, nullable=False)
    t11t14_foot	=	db.Column(db.Integer, nullable=False)
    t14t17_foot	=	db.Column(db.Integer, nullable=False)
    t17t21_foot	=	db.Column(db.Integer, nullable=False)
    t21t24_foot	=	db.Column(db.Integer, nullable=False)
    mon_foot	=	db.Column(db.Integer, nullable=False)
    tue_foot	=	db.Column(db.Integer, nullable=False)
    wed_foot	=	db.Column(db.Integer, nullable=False)
    thu_foot	=	db.Column(db.Integer, nullable=False)
    fri_foot	=	db.Column(db.Integer, nullable=False)
    sat_foot	=	db.Column(db.Integer, nullable=False)
    sun_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_10_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_20_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_30_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_40_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_50_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    M_age_60_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_10_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_20_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_30_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_40_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_50_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_mon_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_mon_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_mon_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_mon_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_mon_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_mon_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_tue_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_tue_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_tue_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_tue_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_tue_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_tue_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_wed_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_wed_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_wed_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_wed_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_wed_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_wed_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_thu_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_thu_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_thu_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_thu_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_thu_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_thu_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_fri_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_fri_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_fri_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_fri_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_fri_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_fri_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sat_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sat_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sat_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sat_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sat_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sat_21t24_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sun_00t06_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sun_06t11_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sun_11t14_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sun_14t17_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sun_17t21_foot	=	db.Column(db.Integer, nullable=False)
    F_age_60_sun_21t24_foot	=	db.Column(db.Integer, nullable=False)

    def __init__(self, base_year_code, base_qu_code, commercial_class_code, commercial_class_code_kr, commercial_code, commercial_code_kr, total_foot, M_foot, F_foot, age_10_foot, age_20_foot, age_30_foot, age_40_foot, age_50_foot, age_60_foot, t00t06_foot, t06t11_foot, t11t14_foot, t14t17_foot, t17t21_foot, t21t24_foot, mon_foot, tue_foot, wed_foot, thu_foot, fri_foot, sat_foot, sun_foot, M_age_10_mon_00t06_foot, M_age_10_mon_06t11_foot, M_age_10_mon_11t14_foot, M_age_10_mon_14t17_foot, M_age_10_mon_17t21_foot, M_age_10_mon_21t24_foot, M_age_10_tue_00t06_foot, M_age_10_tue_06t11_foot, M_age_10_tue_11t14_foot, M_age_10_tue_14t17_foot, M_age_10_tue_17t21_foot, M_age_10_tue_21t24_foot, M_age_10_wed_00t06_foot, M_age_10_wed_06t11_foot, M_age_10_wed_11t14_foot, M_age_10_wed_14t17_foot, M_age_10_wed_17t21_foot, M_age_10_wed_21t24_foot, M_age_10_thu_00t06_foot, M_age_10_thu_06t11_foot, M_age_10_thu_11t14_foot, M_age_10_thu_14t17_foot, M_age_10_thu_17t21_foot, M_age_10_thu_21t24_foot, M_age_10_fri_00t06_foot, M_age_10_fri_06t11_foot, M_age_10_fri_11t14_foot, M_age_10_fri_14t17_foot, M_age_10_fri_17t21_foot, M_age_10_fri_21t24_foot, M_age_10_sat_00t06_foot, M_age_10_sat_06t11_foot, M_age_10_sat_11t14_foot, M_age_10_sat_14t17_foot, M_age_10_sat_17t21_foot, M_age_10_sat_21t24_foot, M_age_10_sun_00t06_foot, M_age_10_sun_06t11_foot, M_age_10_sun_11t14_foot, M_age_10_sun_14t17_foot, M_age_10_sun_17t21_foot, M_age_10_sun_21t24_foot, M_age_20_mon_00t06_foot, M_age_20_mon_06t11_foot, M_age_20_mon_11t14_foot, M_age_20_mon_14t17_foot, M_age_20_mon_17t21_foot, M_age_20_mon_21t24_foot, M_age_20_tue_00t06_foot, M_age_20_tue_06t11_foot, M_age_20_tue_11t14_foot, M_age_20_tue_14t17_foot, M_age_20_tue_17t21_foot, M_age_20_tue_21t24_foot, M_age_20_wed_00t06_foot, M_age_20_wed_06t11_foot, M_age_20_wed_11t14_foot, M_age_20_wed_14t17_foot, M_age_20_wed_17t21_foot, M_age_20_wed_21t24_foot, M_age_20_thu_00t06_foot, M_age_20_thu_06t11_foot, M_age_20_thu_11t14_foot, M_age_20_thu_14t17_foot, M_age_20_thu_17t21_foot, M_age_20_thu_21t24_foot, M_age_20_fri_00t06_foot, M_age_20_fri_06t11_foot, M_age_20_fri_11t14_foot, M_age_20_fri_14t17_foot, M_age_20_fri_17t21_foot, M_age_20_fri_21t24_foot, M_age_20_sat_00t06_foot, M_age_20_sat_06t11_foot, M_age_20_sat_11t14_foot, M_age_20_sat_14t17_foot, M_age_20_sat_17t21_foot, M_age_20_sat_21t24_foot, M_age_20_sun_00t06_foot, M_age_20_sun_06t11_foot, M_age_20_sun_11t14_foot, M_age_20_sun_14t17_foot, M_age_20_sun_17t21_foot, M_age_20_sun_21t24_foot, M_age_30_mon_00t06_foot, M_age_30_mon_06t11_foot, M_age_30_mon_11t14_foot, M_age_30_mon_14t17_foot, M_age_30_mon_17t21_foot, M_age_30_mon_21t24_foot, M_age_30_tue_00t06_foot, M_age_30_tue_06t11_foot, M_age_30_tue_11t14_foot, M_age_30_tue_14t17_foot, M_age_30_tue_17t21_foot, M_age_30_tue_21t24_foot, M_age_30_wed_00t06_foot, M_age_30_wed_06t11_foot, M_age_30_wed_11t14_foot, M_age_30_wed_14t17_foot, M_age_30_wed_17t21_foot, M_age_30_wed_21t24_foot, M_age_30_thu_00t06_foot, M_age_30_thu_06t11_foot, M_age_30_thu_11t14_foot, M_age_30_thu_14t17_foot, M_age_30_thu_17t21_foot, M_age_30_thu_21t24_foot, M_age_30_fri_00t06_foot, M_age_30_fri_06t11_foot, M_age_30_fri_11t14_foot, M_age_30_fri_14t17_foot, M_age_30_fri_17t21_foot, M_age_30_fri_21t24_foot, M_age_30_sat_00t06_foot, M_age_30_sat_06t11_foot, M_age_30_sat_11t14_foot, M_age_30_sat_14t17_foot, M_age_30_sat_17t21_foot, M_age_30_sat_21t24_foot, M_age_30_sun_00t06_foot, M_age_30_sun_06t11_foot, M_age_30_sun_11t14_foot, M_age_30_sun_14t17_foot, M_age_30_sun_17t21_foot, M_age_30_sun_21t24_foot, M_age_40_mon_00t06_foot, M_age_40_mon_06t11_foot, M_age_40_mon_11t14_foot, M_age_40_mon_14t17_foot, M_age_40_mon_17t21_foot, M_age_40_mon_21t24_foot, M_age_40_tue_00t06_foot, M_age_40_tue_06t11_foot, M_age_40_tue_11t14_foot, M_age_40_tue_14t17_foot, M_age_40_tue_17t21_foot, M_age_40_tue_21t24_foot, M_age_40_wed_00t06_foot, M_age_40_wed_06t11_foot, M_age_40_wed_11t14_foot, M_age_40_wed_14t17_foot, M_age_40_wed_17t21_foot, M_age_40_wed_21t24_foot, M_age_40_thu_00t06_foot, M_age_40_thu_06t11_foot, M_age_40_thu_11t14_foot, M_age_40_thu_14t17_foot, M_age_40_thu_17t21_foot, M_age_40_thu_21t24_foot, M_age_40_fri_00t06_foot, M_age_40_fri_06t11_foot, M_age_40_fri_11t14_foot, M_age_40_fri_14t17_foot, M_age_40_fri_17t21_foot, M_age_40_fri_21t24_foot, M_age_40_sat_00t06_foot, M_age_40_sat_06t11_foot, M_age_40_sat_11t14_foot, M_age_40_sat_14t17_foot, M_age_40_sat_17t21_foot, M_age_40_sat_21t24_foot, M_age_40_sun_00t06_foot, M_age_40_sun_06t11_foot, M_age_40_sun_11t14_foot, M_age_40_sun_14t17_foot, M_age_40_sun_17t21_foot, M_age_40_sun_21t24_foot, M_age_50_mon_00t06_foot, M_age_50_mon_06t11_foot, M_age_50_mon_11t14_foot, M_age_50_mon_14t17_foot, M_age_50_mon_17t21_foot, M_age_50_mon_21t24_foot, M_age_50_tue_00t06_foot, M_age_50_tue_06t11_foot, M_age_50_tue_11t14_foot, M_age_50_tue_14t17_foot, M_age_50_tue_17t21_foot, M_age_50_tue_21t24_foot, M_age_50_wed_00t06_foot, M_age_50_wed_06t11_foot, M_age_50_wed_11t14_foot, M_age_50_wed_14t17_foot, M_age_50_wed_17t21_foot, M_age_50_wed_21t24_foot, M_age_50_thu_00t06_foot, M_age_50_thu_06t11_foot, M_age_50_thu_11t14_foot, M_age_50_thu_14t17_foot, M_age_50_thu_17t21_foot, M_age_50_thu_21t24_foot, M_age_50_fri_00t06_foot, M_age_50_fri_06t11_foot, M_age_50_fri_11t14_foot, M_age_50_fri_14t17_foot, M_age_50_fri_17t21_foot, M_age_50_fri_21t24_foot, M_age_50_sat_00t06_foot, M_age_50_sat_06t11_foot, M_age_50_sat_11t14_foot, M_age_50_sat_14t17_foot, M_age_50_sat_17t21_foot, M_age_50_sat_21t24_foot, M_age_50_sun_00t06_foot, M_age_50_sun_06t11_foot, M_age_50_sun_11t14_foot, M_age_50_sun_14t17_foot, M_age_50_sun_17t21_foot, M_age_50_sun_21t24_foot, M_age_60_mon_00t06_foot, M_age_60_mon_06t11_foot, M_age_60_mon_11t14_foot, M_age_60_mon_14t17_foot, M_age_60_mon_17t21_foot, M_age_60_mon_21t24_foot, M_age_60_tue_00t06_foot, M_age_60_tue_06t11_foot, M_age_60_tue_11t14_foot, M_age_60_tue_14t17_foot, M_age_60_tue_17t21_foot, M_age_60_tue_21t24_foot, M_age_60_wed_00t06_foot, M_age_60_wed_06t11_foot, M_age_60_wed_11t14_foot, M_age_60_wed_14t17_foot, M_age_60_wed_17t21_foot, M_age_60_wed_21t24_foot, M_age_60_thu_00t06_foot, M_age_60_thu_06t11_foot, M_age_60_thu_11t14_foot, M_age_60_thu_14t17_foot, M_age_60_thu_17t21_foot, M_age_60_thu_21t24_foot, M_age_60_fri_00t06_foot, M_age_60_fri_06t11_foot, M_age_60_fri_11t14_foot, M_age_60_fri_14t17_foot, M_age_60_fri_17t21_foot, M_age_60_fri_21t24_foot, M_age_60_sat_00t06_foot, M_age_60_sat_06t11_foot, M_age_60_sat_11t14_foot, M_age_60_sat_14t17_foot, M_age_60_sat_17t21_foot, M_age_60_sat_21t24_foot, M_age_60_sun_00t06_foot, M_age_60_sun_06t11_foot, M_age_60_sun_11t14_foot, M_age_60_sun_14t17_foot, M_age_60_sun_17t21_foot, M_age_60_sun_21t24_foot, F_age_10_mon_00t06_foot, F_age_10_mon_06t11_foot, F_age_10_mon_11t14_foot, F_age_10_mon_14t17_foot, F_age_10_mon_17t21_foot, F_age_10_mon_21t24_foot, F_age_10_tue_00t06_foot, F_age_10_tue_06t11_foot, F_age_10_tue_11t14_foot, F_age_10_tue_14t17_foot, F_age_10_tue_17t21_foot, F_age_10_tue_21t24_foot, F_age_10_wed_00t06_foot, F_age_10_wed_06t11_foot, F_age_10_wed_11t14_foot, F_age_10_wed_14t17_foot, F_age_10_wed_17t21_foot, F_age_10_wed_21t24_foot, F_age_10_thu_00t06_foot, F_age_10_thu_06t11_foot, F_age_10_thu_11t14_foot, F_age_10_thu_14t17_foot, F_age_10_thu_17t21_foot, F_age_10_thu_21t24_foot, F_age_10_fri_00t06_foot, F_age_10_fri_06t11_foot, F_age_10_fri_11t14_foot, F_age_10_fri_14t17_foot, F_age_10_fri_17t21_foot, F_age_10_fri_21t24_foot, F_age_10_sat_00t06_foot, F_age_10_sat_06t11_foot, F_age_10_sat_11t14_foot, F_age_10_sat_14t17_foot, F_age_10_sat_17t21_foot, F_age_10_sat_21t24_foot, F_age_10_sun_00t06_foot, F_age_10_sun_06t11_foot, F_age_10_sun_11t14_foot, F_age_10_sun_14t17_foot, F_age_10_sun_17t21_foot, F_age_10_sun_21t24_foot, F_age_20_mon_00t06_foot, F_age_20_mon_06t11_foot, F_age_20_mon_11t14_foot, F_age_20_mon_14t17_foot, F_age_20_mon_17t21_foot, F_age_20_mon_21t24_foot, F_age_20_tue_00t06_foot, F_age_20_tue_06t11_foot, F_age_20_tue_11t14_foot, F_age_20_tue_14t17_foot, F_age_20_tue_17t21_foot, F_age_20_tue_21t24_foot, F_age_20_wed_00t06_foot, F_age_20_wed_06t11_foot, F_age_20_wed_11t14_foot, F_age_20_wed_14t17_foot, F_age_20_wed_17t21_foot, F_age_20_wed_21t24_foot, F_age_20_thu_00t06_foot, F_age_20_thu_06t11_foot, F_age_20_thu_11t14_foot, F_age_20_thu_14t17_foot, F_age_20_thu_17t21_foot, F_age_20_thu_21t24_foot, F_age_20_fri_00t06_foot, F_age_20_fri_06t11_foot, F_age_20_fri_11t14_foot, F_age_20_fri_14t17_foot, F_age_20_fri_17t21_foot, F_age_20_fri_21t24_foot, F_age_20_sat_00t06_foot, F_age_20_sat_06t11_foot, F_age_20_sat_11t14_foot, F_age_20_sat_14t17_foot, F_age_20_sat_17t21_foot, F_age_20_sat_21t24_foot, F_age_20_sun_00t06_foot, F_age_20_sun_06t11_foot, F_age_20_sun_11t14_foot, F_age_20_sun_14t17_foot, F_age_20_sun_17t21_foot, F_age_20_sun_21t24_foot, F_age_30_mon_00t06_foot, F_age_30_mon_06t11_foot, F_age_30_mon_11t14_foot, F_age_30_mon_14t17_foot, F_age_30_mon_17t21_foot, F_age_30_mon_21t24_foot, F_age_30_tue_00t06_foot, F_age_30_tue_06t11_foot, F_age_30_tue_11t14_foot, F_age_30_tue_14t17_foot, F_age_30_tue_17t21_foot, F_age_30_tue_21t24_foot, F_age_30_wed_00t06_foot, F_age_30_wed_06t11_foot, F_age_30_wed_11t14_foot, F_age_30_wed_14t17_foot, F_age_30_wed_17t21_foot, F_age_30_wed_21t24_foot, F_age_30_thu_00t06_foot, F_age_30_thu_06t11_foot, F_age_30_thu_11t14_foot, F_age_30_thu_14t17_foot, F_age_30_thu_17t21_foot, F_age_30_thu_21t24_foot, F_age_30_fri_00t06_foot, F_age_30_fri_06t11_foot, F_age_30_fri_11t14_foot, F_age_30_fri_14t17_foot, F_age_30_fri_17t21_foot, F_age_30_fri_21t24_foot, F_age_30_sat_00t06_foot, F_age_30_sat_06t11_foot, F_age_30_sat_11t14_foot, F_age_30_sat_14t17_foot, F_age_30_sat_17t21_foot, F_age_30_sat_21t24_foot, F_age_30_sun_00t06_foot, F_age_30_sun_06t11_foot, F_age_30_sun_11t14_foot, F_age_30_sun_14t17_foot, F_age_30_sun_17t21_foot, F_age_30_sun_21t24_foot, F_age_40_mon_00t06_foot, F_age_40_mon_06t11_foot, F_age_40_mon_11t14_foot, F_age_40_mon_14t17_foot, F_age_40_mon_17t21_foot, F_age_40_mon_21t24_foot, F_age_40_tue_00t06_foot, F_age_40_tue_06t11_foot, F_age_40_tue_11t14_foot, F_age_40_tue_14t17_foot, F_age_40_tue_17t21_foot, F_age_40_tue_21t24_foot, F_age_40_wed_00t06_foot, F_age_40_wed_06t11_foot, F_age_40_wed_11t14_foot, F_age_40_wed_14t17_foot, F_age_40_wed_17t21_foot, F_age_40_wed_21t24_foot, F_age_40_thu_00t06_foot, F_age_40_thu_06t11_foot, F_age_40_thu_11t14_foot, F_age_40_thu_14t17_foot, F_age_40_thu_17t21_foot, F_age_40_thu_21t24_foot, F_age_40_fri_00t06_foot, F_age_40_fri_06t11_foot, F_age_40_fri_11t14_foot, F_age_40_fri_14t17_foot, F_age_40_fri_17t21_foot, F_age_40_fri_21t24_foot, F_age_40_sat_00t06_foot, F_age_40_sat_06t11_foot, F_age_40_sat_11t14_foot, F_age_40_sat_14t17_foot, F_age_40_sat_17t21_foot, F_age_40_sat_21t24_foot, F_age_40_sun_00t06_foot, F_age_40_sun_06t11_foot, F_age_40_sun_11t14_foot, F_age_40_sun_14t17_foot, F_age_40_sun_17t21_foot, F_age_40_sun_21t24_foot, F_age_50_mon_00t06_foot, F_age_50_mon_06t11_foot, F_age_50_mon_11t14_foot, F_age_50_mon_14t17_foot, F_age_50_mon_17t21_foot, F_age_50_mon_21t24_foot, F_age_50_tue_00t06_foot, F_age_50_tue_06t11_foot, F_age_50_tue_11t14_foot, F_age_50_tue_14t17_foot, F_age_50_tue_17t21_foot, F_age_50_tue_21t24_foot, F_age_50_wed_00t06_foot, F_age_50_wed_06t11_foot, F_age_50_wed_11t14_foot, F_age_50_wed_14t17_foot, F_age_50_wed_17t21_foot, F_age_50_wed_21t24_foot, F_age_50_thu_00t06_foot, F_age_50_thu_06t11_foot, F_age_50_thu_11t14_foot, F_age_50_thu_14t17_foot, F_age_50_thu_17t21_foot, F_age_50_thu_21t24_foot, F_age_50_fri_00t06_foot, F_age_50_fri_06t11_foot, F_age_50_fri_11t14_foot, F_age_50_fri_14t17_foot, F_age_50_fri_17t21_foot, F_age_50_fri_21t24_foot, F_age_50_sat_00t06_foot, F_age_50_sat_06t11_foot, F_age_50_sat_11t14_foot, F_age_50_sat_14t17_foot, F_age_50_sat_17t21_foot, F_age_50_sat_21t24_foot, F_age_50_sun_00t06_foot, F_age_50_sun_06t11_foot, F_age_50_sun_11t14_foot, F_age_50_sun_14t17_foot, F_age_50_sun_17t21_foot, F_age_50_sun_21t24_foot, F_age_60_mon_00t06_foot, F_age_60_mon_06t11_foot, F_age_60_mon_11t14_foot, F_age_60_mon_14t17_foot, F_age_60_mon_17t21_foot, F_age_60_mon_21t24_foot, F_age_60_tue_00t06_foot, F_age_60_tue_06t11_foot, F_age_60_tue_11t14_foot, F_age_60_tue_14t17_foot, F_age_60_tue_17t21_foot, F_age_60_tue_21t24_foot, F_age_60_wed_00t06_foot, F_age_60_wed_06t11_foot, F_age_60_wed_11t14_foot, F_age_60_wed_14t17_foot, F_age_60_wed_17t21_foot, F_age_60_wed_21t24_foot, F_age_60_thu_00t06_foot, F_age_60_thu_06t11_foot, F_age_60_thu_11t14_foot, F_age_60_thu_14t17_foot, F_age_60_thu_17t21_foot, F_age_60_thu_21t24_foot, F_age_60_fri_00t06_foot, F_age_60_fri_06t11_foot, F_age_60_fri_11t14_foot, F_age_60_fri_14t17_foot, F_age_60_fri_17t21_foot, F_age_60_fri_21t24_foot, F_age_60_sat_00t06_foot, F_age_60_sat_06t11_foot, F_age_60_sat_11t14_foot, F_age_60_sat_14t17_foot, F_age_60_sat_17t21_foot, F_age_60_sat_21t24_foot, F_age_60_sun_00t06_foot, F_age_60_sun_06t11_foot, F_age_60_sun_11t14_foot, F_age_60_sun_14t17_foot, F_age_60_sun_17t21_foot, F_age_60_sun_21t24_foot):
        self.base_year_code	=	base_year_code
        self.base_qu_code	=	base_qu_code
        self.commercial_class_code	=	commercial_class_code
        self.commercial_class_code_kr	=	commercial_class_code_kr
        self.commercial_code	=	commercial_code
        self.commercial_code_kr	=	commercial_code_kr
        self.total_foot	=	total_foot
        self.M_foot	=	M_foot
        self.F_foot	=	F_foot
        self.age_10_foot	=	age_10_foot
        self.age_20_foot	=	age_20_foot
        self.age_30_foot	=	age_30_foot
        self.age_40_foot	=	age_40_foot
        self.age_50_foot	=	age_50_foot
        self.age_60_foot	=	age_60_foot
        self.t00t06_foot	=	t00t06_foot
        self.t06t11_foot	=	t06t11_foot
        self.t11t14_foot	=	t11t14_foot
        self.t14t17_foot	=	t14t17_foot
        self.t17t21_foot	=	t17t21_foot
        self.t21t24_foot	=	t21t24_foot
        self.mon_foot	=	mon_foot
        self.tue_foot	=	tue_foot
        self.wed_foot	=	wed_foot
        self.thu_foot	=	thu_foot
        self.fri_foot	=	fri_foot
        self.sat_foot	=	sat_foot
        self.sun_foot	=	sun_foot
        self.M_age_10_mon_00t06_foot	=	M_age_10_mon_00t06_foot
        self.M_age_10_mon_06t11_foot	=	M_age_10_mon_06t11_foot
        self.M_age_10_mon_11t14_foot	=	M_age_10_mon_11t14_foot
        self.M_age_10_mon_14t17_foot	=	M_age_10_mon_14t17_foot
        self.M_age_10_mon_17t21_foot	=	M_age_10_mon_17t21_foot
        self.M_age_10_mon_21t24_foot	=	M_age_10_mon_21t24_foot
        self.M_age_10_tue_00t06_foot	=	M_age_10_tue_00t06_foot
        self.M_age_10_tue_06t11_foot	=	M_age_10_tue_06t11_foot
        self.M_age_10_tue_11t14_foot	=	M_age_10_tue_11t14_foot
        self.M_age_10_tue_14t17_foot	=	M_age_10_tue_14t17_foot
        self.M_age_10_tue_17t21_foot	=	M_age_10_tue_17t21_foot
        self.M_age_10_tue_21t24_foot	=	M_age_10_tue_21t24_foot
        self.M_age_10_wed_00t06_foot	=	M_age_10_wed_00t06_foot
        self.M_age_10_wed_06t11_foot	=	M_age_10_wed_06t11_foot
        self.M_age_10_wed_11t14_foot	=	M_age_10_wed_11t14_foot
        self.M_age_10_wed_14t17_foot	=	M_age_10_wed_14t17_foot
        self.M_age_10_wed_17t21_foot	=	M_age_10_wed_17t21_foot
        self.M_age_10_wed_21t24_foot	=	M_age_10_wed_21t24_foot
        self.M_age_10_thu_00t06_foot	=	M_age_10_thu_00t06_foot
        self.M_age_10_thu_06t11_foot	=	M_age_10_thu_06t11_foot
        self.M_age_10_thu_11t14_foot	=	M_age_10_thu_11t14_foot
        self.M_age_10_thu_14t17_foot	=	M_age_10_thu_14t17_foot
        self.M_age_10_thu_17t21_foot	=	M_age_10_thu_17t21_foot
        self.M_age_10_thu_21t24_foot	=	M_age_10_thu_21t24_foot
        self.M_age_10_fri_00t06_foot	=	M_age_10_fri_00t06_foot
        self.M_age_10_fri_06t11_foot	=	M_age_10_fri_06t11_foot
        self.M_age_10_fri_11t14_foot	=	M_age_10_fri_11t14_foot
        self.M_age_10_fri_14t17_foot	=	M_age_10_fri_14t17_foot
        self.M_age_10_fri_17t21_foot	=	M_age_10_fri_17t21_foot
        self.M_age_10_fri_21t24_foot	=	M_age_10_fri_21t24_foot
        self.M_age_10_sat_00t06_foot	=	M_age_10_sat_00t06_foot
        self.M_age_10_sat_06t11_foot	=	M_age_10_sat_06t11_foot
        self.M_age_10_sat_11t14_foot	=	M_age_10_sat_11t14_foot
        self.M_age_10_sat_14t17_foot	=	M_age_10_sat_14t17_foot
        self.M_age_10_sat_17t21_foot	=	M_age_10_sat_17t21_foot
        self.M_age_10_sat_21t24_foot	=	M_age_10_sat_21t24_foot
        self.M_age_10_sun_00t06_foot	=	M_age_10_sun_00t06_foot
        self.M_age_10_sun_06t11_foot	=	M_age_10_sun_06t11_foot
        self.M_age_10_sun_11t14_foot	=	M_age_10_sun_11t14_foot
        self.M_age_10_sun_14t17_foot	=	M_age_10_sun_14t17_foot
        self.M_age_10_sun_17t21_foot	=	M_age_10_sun_17t21_foot
        self.M_age_10_sun_21t24_foot	=	M_age_10_sun_21t24_foot
        self.M_age_20_mon_00t06_foot	=	M_age_20_mon_00t06_foot
        self.M_age_20_mon_06t11_foot	=	M_age_20_mon_06t11_foot
        self.M_age_20_mon_11t14_foot	=	M_age_20_mon_11t14_foot
        self.M_age_20_mon_14t17_foot	=	M_age_20_mon_14t17_foot
        self.M_age_20_mon_17t21_foot	=	M_age_20_mon_17t21_foot
        self.M_age_20_mon_21t24_foot	=	M_age_20_mon_21t24_foot
        self.M_age_20_tue_00t06_foot	=	M_age_20_tue_00t06_foot
        self.M_age_20_tue_06t11_foot	=	M_age_20_tue_06t11_foot
        self.M_age_20_tue_11t14_foot	=	M_age_20_tue_11t14_foot
        self.M_age_20_tue_14t17_foot	=	M_age_20_tue_14t17_foot
        self.M_age_20_tue_17t21_foot	=	M_age_20_tue_17t21_foot
        self.M_age_20_tue_21t24_foot	=	M_age_20_tue_21t24_foot
        self.M_age_20_wed_00t06_foot	=	M_age_20_wed_00t06_foot
        self.M_age_20_wed_06t11_foot	=	M_age_20_wed_06t11_foot
        self.M_age_20_wed_11t14_foot	=	M_age_20_wed_11t14_foot
        self.M_age_20_wed_14t17_foot	=	M_age_20_wed_14t17_foot
        self.M_age_20_wed_17t21_foot	=	M_age_20_wed_17t21_foot
        self.M_age_20_wed_21t24_foot	=	M_age_20_wed_21t24_foot
        self.M_age_20_thu_00t06_foot	=	M_age_20_thu_00t06_foot
        self.M_age_20_thu_06t11_foot	=	M_age_20_thu_06t11_foot
        self.M_age_20_thu_11t14_foot	=	M_age_20_thu_11t14_foot
        self.M_age_20_thu_14t17_foot	=	M_age_20_thu_14t17_foot
        self.M_age_20_thu_17t21_foot	=	M_age_20_thu_17t21_foot
        self.M_age_20_thu_21t24_foot	=	M_age_20_thu_21t24_foot
        self.M_age_20_fri_00t06_foot	=	M_age_20_fri_00t06_foot
        self.M_age_20_fri_06t11_foot	=	M_age_20_fri_06t11_foot
        self.M_age_20_fri_11t14_foot	=	M_age_20_fri_11t14_foot
        self.M_age_20_fri_14t17_foot	=	M_age_20_fri_14t17_foot
        self.M_age_20_fri_17t21_foot	=	M_age_20_fri_17t21_foot
        self.M_age_20_fri_21t24_foot	=	M_age_20_fri_21t24_foot
        self.M_age_20_sat_00t06_foot	=	M_age_20_sat_00t06_foot
        self.M_age_20_sat_06t11_foot	=	M_age_20_sat_06t11_foot
        self.M_age_20_sat_11t14_foot	=	M_age_20_sat_11t14_foot
        self.M_age_20_sat_14t17_foot	=	M_age_20_sat_14t17_foot
        self.M_age_20_sat_17t21_foot	=	M_age_20_sat_17t21_foot
        self.M_age_20_sat_21t24_foot	=	M_age_20_sat_21t24_foot
        self.M_age_20_sun_00t06_foot	=	M_age_20_sun_00t06_foot
        self.M_age_20_sun_06t11_foot	=	M_age_20_sun_06t11_foot
        self.M_age_20_sun_11t14_foot	=	M_age_20_sun_11t14_foot
        self.M_age_20_sun_14t17_foot	=	M_age_20_sun_14t17_foot
        self.M_age_20_sun_17t21_foot	=	M_age_20_sun_17t21_foot
        self.M_age_20_sun_21t24_foot	=	M_age_20_sun_21t24_foot
        self.M_age_30_mon_00t06_foot	=	M_age_30_mon_00t06_foot
        self.M_age_30_mon_06t11_foot	=	M_age_30_mon_06t11_foot
        self.M_age_30_mon_11t14_foot	=	M_age_30_mon_11t14_foot
        self.M_age_30_mon_14t17_foot	=	M_age_30_mon_14t17_foot
        self.M_age_30_mon_17t21_foot	=	M_age_30_mon_17t21_foot
        self.M_age_30_mon_21t24_foot	=	M_age_30_mon_21t24_foot
        self.M_age_30_tue_00t06_foot	=	M_age_30_tue_00t06_foot
        self.M_age_30_tue_06t11_foot	=	M_age_30_tue_06t11_foot
        self.M_age_30_tue_11t14_foot	=	M_age_30_tue_11t14_foot
        self.M_age_30_tue_14t17_foot	=	M_age_30_tue_14t17_foot
        self.M_age_30_tue_17t21_foot	=	M_age_30_tue_17t21_foot
        self.M_age_30_tue_21t24_foot	=	M_age_30_tue_21t24_foot
        self.M_age_30_wed_00t06_foot	=	M_age_30_wed_00t06_foot
        self.M_age_30_wed_06t11_foot	=	M_age_30_wed_06t11_foot
        self.M_age_30_wed_11t14_foot	=	M_age_30_wed_11t14_foot
        self.M_age_30_wed_14t17_foot	=	M_age_30_wed_14t17_foot
        self.M_age_30_wed_17t21_foot	=	M_age_30_wed_17t21_foot
        self.M_age_30_wed_21t24_foot	=	M_age_30_wed_21t24_foot
        self.M_age_30_thu_00t06_foot	=	M_age_30_thu_00t06_foot
        self.M_age_30_thu_06t11_foot	=	M_age_30_thu_06t11_foot
        self.M_age_30_thu_11t14_foot	=	M_age_30_thu_11t14_foot
        self.M_age_30_thu_14t17_foot	=	M_age_30_thu_14t17_foot
        self.M_age_30_thu_17t21_foot	=	M_age_30_thu_17t21_foot
        self.M_age_30_thu_21t24_foot	=	M_age_30_thu_21t24_foot
        self.M_age_30_fri_00t06_foot	=	M_age_30_fri_00t06_foot
        self.M_age_30_fri_06t11_foot	=	M_age_30_fri_06t11_foot
        self.M_age_30_fri_11t14_foot	=	M_age_30_fri_11t14_foot
        self.M_age_30_fri_14t17_foot	=	M_age_30_fri_14t17_foot
        self.M_age_30_fri_17t21_foot	=	M_age_30_fri_17t21_foot
        self.M_age_30_fri_21t24_foot	=	M_age_30_fri_21t24_foot
        self.M_age_30_sat_00t06_foot	=	M_age_30_sat_00t06_foot
        self.M_age_30_sat_06t11_foot	=	M_age_30_sat_06t11_foot
        self.M_age_30_sat_11t14_foot	=	M_age_30_sat_11t14_foot
        self.M_age_30_sat_14t17_foot	=	M_age_30_sat_14t17_foot
        self.M_age_30_sat_17t21_foot	=	M_age_30_sat_17t21_foot
        self.M_age_30_sat_21t24_foot	=	M_age_30_sat_21t24_foot
        self.M_age_30_sun_00t06_foot	=	M_age_30_sun_00t06_foot
        self.M_age_30_sun_06t11_foot	=	M_age_30_sun_06t11_foot
        self.M_age_30_sun_11t14_foot	=	M_age_30_sun_11t14_foot
        self.M_age_30_sun_14t17_foot	=	M_age_30_sun_14t17_foot
        self.M_age_30_sun_17t21_foot	=	M_age_30_sun_17t21_foot
        self.M_age_30_sun_21t24_foot	=	M_age_30_sun_21t24_foot
        self.M_age_40_mon_00t06_foot	=	M_age_40_mon_00t06_foot
        self.M_age_40_mon_06t11_foot	=	M_age_40_mon_06t11_foot
        self.M_age_40_mon_11t14_foot	=	M_age_40_mon_11t14_foot
        self.M_age_40_mon_14t17_foot	=	M_age_40_mon_14t17_foot
        self.M_age_40_mon_17t21_foot	=	M_age_40_mon_17t21_foot
        self.M_age_40_mon_21t24_foot	=	M_age_40_mon_21t24_foot
        self.M_age_40_tue_00t06_foot	=	M_age_40_tue_00t06_foot
        self.M_age_40_tue_06t11_foot	=	M_age_40_tue_06t11_foot
        self.M_age_40_tue_11t14_foot	=	M_age_40_tue_11t14_foot
        self.M_age_40_tue_14t17_foot	=	M_age_40_tue_14t17_foot
        self.M_age_40_tue_17t21_foot	=	M_age_40_tue_17t21_foot
        self.M_age_40_tue_21t24_foot	=	M_age_40_tue_21t24_foot
        self.M_age_40_wed_00t06_foot	=	M_age_40_wed_00t06_foot
        self.M_age_40_wed_06t11_foot	=	M_age_40_wed_06t11_foot
        self.M_age_40_wed_11t14_foot	=	M_age_40_wed_11t14_foot
        self.M_age_40_wed_14t17_foot	=	M_age_40_wed_14t17_foot
        self.M_age_40_wed_17t21_foot	=	M_age_40_wed_17t21_foot
        self.M_age_40_wed_21t24_foot	=	M_age_40_wed_21t24_foot
        self.M_age_40_thu_00t06_foot	=	M_age_40_thu_00t06_foot
        self.M_age_40_thu_06t11_foot	=	M_age_40_thu_06t11_foot
        self.M_age_40_thu_11t14_foot	=	M_age_40_thu_11t14_foot
        self.M_age_40_thu_14t17_foot	=	M_age_40_thu_14t17_foot
        self.M_age_40_thu_17t21_foot	=	M_age_40_thu_17t21_foot
        self.M_age_40_thu_21t24_foot	=	M_age_40_thu_21t24_foot
        self.M_age_40_fri_00t06_foot	=	M_age_40_fri_00t06_foot
        self.M_age_40_fri_06t11_foot	=	M_age_40_fri_06t11_foot
        self.M_age_40_fri_11t14_foot	=	M_age_40_fri_11t14_foot
        self.M_age_40_fri_14t17_foot	=	M_age_40_fri_14t17_foot
        self.M_age_40_fri_17t21_foot	=	M_age_40_fri_17t21_foot
        self.M_age_40_fri_21t24_foot	=	M_age_40_fri_21t24_foot
        self.M_age_40_sat_00t06_foot	=	M_age_40_sat_00t06_foot
        self.M_age_40_sat_06t11_foot	=	M_age_40_sat_06t11_foot
        self.M_age_40_sat_11t14_foot	=	M_age_40_sat_11t14_foot
        self.M_age_40_sat_14t17_foot	=	M_age_40_sat_14t17_foot
        self.M_age_40_sat_17t21_foot	=	M_age_40_sat_17t21_foot
        self.M_age_40_sat_21t24_foot	=	M_age_40_sat_21t24_foot
        self.M_age_40_sun_00t06_foot	=	M_age_40_sun_00t06_foot
        self.M_age_40_sun_06t11_foot	=	M_age_40_sun_06t11_foot
        self.M_age_40_sun_11t14_foot	=	M_age_40_sun_11t14_foot
        self.M_age_40_sun_14t17_foot	=	M_age_40_sun_14t17_foot
        self.M_age_40_sun_17t21_foot	=	M_age_40_sun_17t21_foot
        self.M_age_40_sun_21t24_foot	=	M_age_40_sun_21t24_foot
        self.M_age_50_mon_00t06_foot	=	M_age_50_mon_00t06_foot
        self.M_age_50_mon_06t11_foot	=	M_age_50_mon_06t11_foot
        self.M_age_50_mon_11t14_foot	=	M_age_50_mon_11t14_foot
        self.M_age_50_mon_14t17_foot	=	M_age_50_mon_14t17_foot
        self.M_age_50_mon_17t21_foot	=	M_age_50_mon_17t21_foot
        self.M_age_50_mon_21t24_foot	=	M_age_50_mon_21t24_foot
        self.M_age_50_tue_00t06_foot	=	M_age_50_tue_00t06_foot
        self.M_age_50_tue_06t11_foot	=	M_age_50_tue_06t11_foot
        self.M_age_50_tue_11t14_foot	=	M_age_50_tue_11t14_foot
        self.M_age_50_tue_14t17_foot	=	M_age_50_tue_14t17_foot
        self.M_age_50_tue_17t21_foot	=	M_age_50_tue_17t21_foot
        self.M_age_50_tue_21t24_foot	=	M_age_50_tue_21t24_foot
        self.M_age_50_wed_00t06_foot	=	M_age_50_wed_00t06_foot
        self.M_age_50_wed_06t11_foot	=	M_age_50_wed_06t11_foot
        self.M_age_50_wed_11t14_foot	=	M_age_50_wed_11t14_foot
        self.M_age_50_wed_14t17_foot	=	M_age_50_wed_14t17_foot
        self.M_age_50_wed_17t21_foot	=	M_age_50_wed_17t21_foot
        self.M_age_50_wed_21t24_foot	=	M_age_50_wed_21t24_foot
        self.M_age_50_thu_00t06_foot	=	M_age_50_thu_00t06_foot
        self.M_age_50_thu_06t11_foot	=	M_age_50_thu_06t11_foot
        self.M_age_50_thu_11t14_foot	=	M_age_50_thu_11t14_foot
        self.M_age_50_thu_14t17_foot	=	M_age_50_thu_14t17_foot
        self.M_age_50_thu_17t21_foot	=	M_age_50_thu_17t21_foot
        self.M_age_50_thu_21t24_foot	=	M_age_50_thu_21t24_foot
        self.M_age_50_fri_00t06_foot	=	M_age_50_fri_00t06_foot
        self.M_age_50_fri_06t11_foot	=	M_age_50_fri_06t11_foot
        self.M_age_50_fri_11t14_foot	=	M_age_50_fri_11t14_foot
        self.M_age_50_fri_14t17_foot	=	M_age_50_fri_14t17_foot
        self.M_age_50_fri_17t21_foot	=	M_age_50_fri_17t21_foot
        self.M_age_50_fri_21t24_foot	=	M_age_50_fri_21t24_foot
        self.M_age_50_sat_00t06_foot	=	M_age_50_sat_00t06_foot
        self.M_age_50_sat_06t11_foot	=	M_age_50_sat_06t11_foot
        self.M_age_50_sat_11t14_foot	=	M_age_50_sat_11t14_foot
        self.M_age_50_sat_14t17_foot	=	M_age_50_sat_14t17_foot
        self.M_age_50_sat_17t21_foot	=	M_age_50_sat_17t21_foot
        self.M_age_50_sat_21t24_foot	=	M_age_50_sat_21t24_foot
        self.M_age_50_sun_00t06_foot	=	M_age_50_sun_00t06_foot
        self.M_age_50_sun_06t11_foot	=	M_age_50_sun_06t11_foot
        self.M_age_50_sun_11t14_foot	=	M_age_50_sun_11t14_foot
        self.M_age_50_sun_14t17_foot	=	M_age_50_sun_14t17_foot
        self.M_age_50_sun_17t21_foot	=	M_age_50_sun_17t21_foot
        self.M_age_50_sun_21t24_foot	=	M_age_50_sun_21t24_foot
        self.M_age_60_mon_00t06_foot	=	M_age_60_mon_00t06_foot
        self.M_age_60_mon_06t11_foot	=	M_age_60_mon_06t11_foot
        self.M_age_60_mon_11t14_foot	=	M_age_60_mon_11t14_foot
        self.M_age_60_mon_14t17_foot	=	M_age_60_mon_14t17_foot
        self.M_age_60_mon_17t21_foot	=	M_age_60_mon_17t21_foot
        self.M_age_60_mon_21t24_foot	=	M_age_60_mon_21t24_foot
        self.M_age_60_tue_00t06_foot	=	M_age_60_tue_00t06_foot
        self.M_age_60_tue_06t11_foot	=	M_age_60_tue_06t11_foot
        self.M_age_60_tue_11t14_foot	=	M_age_60_tue_11t14_foot
        self.M_age_60_tue_14t17_foot	=	M_age_60_tue_14t17_foot
        self.M_age_60_tue_17t21_foot	=	M_age_60_tue_17t21_foot
        self.M_age_60_tue_21t24_foot	=	M_age_60_tue_21t24_foot
        self.M_age_60_wed_00t06_foot	=	M_age_60_wed_00t06_foot
        self.M_age_60_wed_06t11_foot	=	M_age_60_wed_06t11_foot
        self.M_age_60_wed_11t14_foot	=	M_age_60_wed_11t14_foot
        self.M_age_60_wed_14t17_foot	=	M_age_60_wed_14t17_foot
        self.M_age_60_wed_17t21_foot	=	M_age_60_wed_17t21_foot
        self.M_age_60_wed_21t24_foot	=	M_age_60_wed_21t24_foot
        self.M_age_60_thu_00t06_foot	=	M_age_60_thu_00t06_foot
        self.M_age_60_thu_06t11_foot	=	M_age_60_thu_06t11_foot
        self.M_age_60_thu_11t14_foot	=	M_age_60_thu_11t14_foot
        self.M_age_60_thu_14t17_foot	=	M_age_60_thu_14t17_foot
        self.M_age_60_thu_17t21_foot	=	M_age_60_thu_17t21_foot
        self.M_age_60_thu_21t24_foot	=	M_age_60_thu_21t24_foot
        self.M_age_60_fri_00t06_foot	=	M_age_60_fri_00t06_foot
        self.M_age_60_fri_06t11_foot	=	M_age_60_fri_06t11_foot
        self.M_age_60_fri_11t14_foot	=	M_age_60_fri_11t14_foot
        self.M_age_60_fri_14t17_foot	=	M_age_60_fri_14t17_foot
        self.M_age_60_fri_17t21_foot	=	M_age_60_fri_17t21_foot
        self.M_age_60_fri_21t24_foot	=	M_age_60_fri_21t24_foot
        self.M_age_60_sat_00t06_foot	=	M_age_60_sat_00t06_foot
        self.M_age_60_sat_06t11_foot	=	M_age_60_sat_06t11_foot
        self.M_age_60_sat_11t14_foot	=	M_age_60_sat_11t14_foot
        self.M_age_60_sat_14t17_foot	=	M_age_60_sat_14t17_foot
        self.M_age_60_sat_17t21_foot	=	M_age_60_sat_17t21_foot
        self.M_age_60_sat_21t24_foot	=	M_age_60_sat_21t24_foot
        self.M_age_60_sun_00t06_foot	=	M_age_60_sun_00t06_foot
        self.M_age_60_sun_06t11_foot	=	M_age_60_sun_06t11_foot
        self.M_age_60_sun_11t14_foot	=	M_age_60_sun_11t14_foot
        self.M_age_60_sun_14t17_foot	=	M_age_60_sun_14t17_foot
        self.M_age_60_sun_17t21_foot	=	M_age_60_sun_17t21_foot
        self.M_age_60_sun_21t24_foot	=	M_age_60_sun_21t24_foot
        self.F_age_10_mon_00t06_foot	=	F_age_10_mon_00t06_foot
        self.F_age_10_mon_06t11_foot	=	F_age_10_mon_06t11_foot
        self.F_age_10_mon_11t14_foot	=	F_age_10_mon_11t14_foot
        self.F_age_10_mon_14t17_foot	=	F_age_10_mon_14t17_foot
        self.F_age_10_mon_17t21_foot	=	F_age_10_mon_17t21_foot
        self.F_age_10_mon_21t24_foot	=	F_age_10_mon_21t24_foot
        self.F_age_10_tue_00t06_foot	=	F_age_10_tue_00t06_foot
        self.F_age_10_tue_06t11_foot	=	F_age_10_tue_06t11_foot
        self.F_age_10_tue_11t14_foot	=	F_age_10_tue_11t14_foot
        self.F_age_10_tue_14t17_foot	=	F_age_10_tue_14t17_foot
        self.F_age_10_tue_17t21_foot	=	F_age_10_tue_17t21_foot
        self.F_age_10_tue_21t24_foot	=	F_age_10_tue_21t24_foot
        self.F_age_10_wed_00t06_foot	=	F_age_10_wed_00t06_foot
        self.F_age_10_wed_06t11_foot	=	F_age_10_wed_06t11_foot
        self.F_age_10_wed_11t14_foot	=	F_age_10_wed_11t14_foot
        self.F_age_10_wed_14t17_foot	=	F_age_10_wed_14t17_foot
        self.F_age_10_wed_17t21_foot	=	F_age_10_wed_17t21_foot
        self.F_age_10_wed_21t24_foot	=	F_age_10_wed_21t24_foot
        self.F_age_10_thu_00t06_foot	=	F_age_10_thu_00t06_foot
        self.F_age_10_thu_06t11_foot	=	F_age_10_thu_06t11_foot
        self.F_age_10_thu_11t14_foot	=	F_age_10_thu_11t14_foot
        self.F_age_10_thu_14t17_foot	=	F_age_10_thu_14t17_foot
        self.F_age_10_thu_17t21_foot	=	F_age_10_thu_17t21_foot
        self.F_age_10_thu_21t24_foot	=	F_age_10_thu_21t24_foot
        self.F_age_10_fri_00t06_foot	=	F_age_10_fri_00t06_foot
        self.F_age_10_fri_06t11_foot	=	F_age_10_fri_06t11_foot
        self.F_age_10_fri_11t14_foot	=	F_age_10_fri_11t14_foot
        self.F_age_10_fri_14t17_foot	=	F_age_10_fri_14t17_foot
        self.F_age_10_fri_17t21_foot	=	F_age_10_fri_17t21_foot
        self.F_age_10_fri_21t24_foot	=	F_age_10_fri_21t24_foot
        self.F_age_10_sat_00t06_foot	=	F_age_10_sat_00t06_foot
        self.F_age_10_sat_06t11_foot	=	F_age_10_sat_06t11_foot
        self.F_age_10_sat_11t14_foot	=	F_age_10_sat_11t14_foot
        self.F_age_10_sat_14t17_foot	=	F_age_10_sat_14t17_foot
        self.F_age_10_sat_17t21_foot	=	F_age_10_sat_17t21_foot
        self.F_age_10_sat_21t24_foot	=	F_age_10_sat_21t24_foot
        self.F_age_10_sun_00t06_foot	=	F_age_10_sun_00t06_foot
        self.F_age_10_sun_06t11_foot	=	F_age_10_sun_06t11_foot
        self.F_age_10_sun_11t14_foot	=	F_age_10_sun_11t14_foot
        self.F_age_10_sun_14t17_foot	=	F_age_10_sun_14t17_foot
        self.F_age_10_sun_17t21_foot	=	F_age_10_sun_17t21_foot
        self.F_age_10_sun_21t24_foot	=	F_age_10_sun_21t24_foot
        self.F_age_20_mon_00t06_foot	=	F_age_20_mon_00t06_foot
        self.F_age_20_mon_06t11_foot	=	F_age_20_mon_06t11_foot
        self.F_age_20_mon_11t14_foot	=	F_age_20_mon_11t14_foot
        self.F_age_20_mon_14t17_foot	=	F_age_20_mon_14t17_foot
        self.F_age_20_mon_17t21_foot	=	F_age_20_mon_17t21_foot
        self.F_age_20_mon_21t24_foot	=	F_age_20_mon_21t24_foot
        self.F_age_20_tue_00t06_foot	=	F_age_20_tue_00t06_foot
        self.F_age_20_tue_06t11_foot	=	F_age_20_tue_06t11_foot
        self.F_age_20_tue_11t14_foot	=	F_age_20_tue_11t14_foot
        self.F_age_20_tue_14t17_foot	=	F_age_20_tue_14t17_foot
        self.F_age_20_tue_17t21_foot	=	F_age_20_tue_17t21_foot
        self.F_age_20_tue_21t24_foot	=	F_age_20_tue_21t24_foot
        self.F_age_20_wed_00t06_foot	=	F_age_20_wed_00t06_foot
        self.F_age_20_wed_06t11_foot	=	F_age_20_wed_06t11_foot
        self.F_age_20_wed_11t14_foot	=	F_age_20_wed_11t14_foot
        self.F_age_20_wed_14t17_foot	=	F_age_20_wed_14t17_foot
        self.F_age_20_wed_17t21_foot	=	F_age_20_wed_17t21_foot
        self.F_age_20_wed_21t24_foot	=	F_age_20_wed_21t24_foot
        self.F_age_20_thu_00t06_foot	=	F_age_20_thu_00t06_foot
        self.F_age_20_thu_06t11_foot	=	F_age_20_thu_06t11_foot
        self.F_age_20_thu_11t14_foot	=	F_age_20_thu_11t14_foot
        self.F_age_20_thu_14t17_foot	=	F_age_20_thu_14t17_foot
        self.F_age_20_thu_17t21_foot	=	F_age_20_thu_17t21_foot
        self.F_age_20_thu_21t24_foot	=	F_age_20_thu_21t24_foot
        self.F_age_20_fri_00t06_foot	=	F_age_20_fri_00t06_foot
        self.F_age_20_fri_06t11_foot	=	F_age_20_fri_06t11_foot
        self.F_age_20_fri_11t14_foot	=	F_age_20_fri_11t14_foot
        self.F_age_20_fri_14t17_foot	=	F_age_20_fri_14t17_foot
        self.F_age_20_fri_17t21_foot	=	F_age_20_fri_17t21_foot
        self.F_age_20_fri_21t24_foot	=	F_age_20_fri_21t24_foot
        self.F_age_20_sat_00t06_foot	=	F_age_20_sat_00t06_foot
        self.F_age_20_sat_06t11_foot	=	F_age_20_sat_06t11_foot
        self.F_age_20_sat_11t14_foot	=	F_age_20_sat_11t14_foot
        self.F_age_20_sat_14t17_foot	=	F_age_20_sat_14t17_foot
        self.F_age_20_sat_17t21_foot	=	F_age_20_sat_17t21_foot
        self.F_age_20_sat_21t24_foot	=	F_age_20_sat_21t24_foot
        self.F_age_20_sun_00t06_foot	=	F_age_20_sun_00t06_foot
        self.F_age_20_sun_06t11_foot	=	F_age_20_sun_06t11_foot
        self.F_age_20_sun_11t14_foot	=	F_age_20_sun_11t14_foot
        self.F_age_20_sun_14t17_foot	=	F_age_20_sun_14t17_foot
        self.F_age_20_sun_17t21_foot	=	F_age_20_sun_17t21_foot
        self.F_age_20_sun_21t24_foot	=	F_age_20_sun_21t24_foot
        self.F_age_30_mon_00t06_foot	=	F_age_30_mon_00t06_foot
        self.F_age_30_mon_06t11_foot	=	F_age_30_mon_06t11_foot
        self.F_age_30_mon_11t14_foot	=	F_age_30_mon_11t14_foot
        self.F_age_30_mon_14t17_foot	=	F_age_30_mon_14t17_foot
        self.F_age_30_mon_17t21_foot	=	F_age_30_mon_17t21_foot
        self.F_age_30_mon_21t24_foot	=	F_age_30_mon_21t24_foot
        self.F_age_30_tue_00t06_foot	=	F_age_30_tue_00t06_foot
        self.F_age_30_tue_06t11_foot	=	F_age_30_tue_06t11_foot
        self.F_age_30_tue_11t14_foot	=	F_age_30_tue_11t14_foot
        self.F_age_30_tue_14t17_foot	=	F_age_30_tue_14t17_foot
        self.F_age_30_tue_17t21_foot	=	F_age_30_tue_17t21_foot
        self.F_age_30_tue_21t24_foot	=	F_age_30_tue_21t24_foot
        self.F_age_30_wed_00t06_foot	=	F_age_30_wed_00t06_foot
        self.F_age_30_wed_06t11_foot	=	F_age_30_wed_06t11_foot
        self.F_age_30_wed_11t14_foot	=	F_age_30_wed_11t14_foot
        self.F_age_30_wed_14t17_foot	=	F_age_30_wed_14t17_foot
        self.F_age_30_wed_17t21_foot	=	F_age_30_wed_17t21_foot
        self.F_age_30_wed_21t24_foot	=	F_age_30_wed_21t24_foot
        self.F_age_30_thu_00t06_foot	=	F_age_30_thu_00t06_foot
        self.F_age_30_thu_06t11_foot	=	F_age_30_thu_06t11_foot
        self.F_age_30_thu_11t14_foot	=	F_age_30_thu_11t14_foot
        self.F_age_30_thu_14t17_foot	=	F_age_30_thu_14t17_foot
        self.F_age_30_thu_17t21_foot	=	F_age_30_thu_17t21_foot
        self.F_age_30_thu_21t24_foot	=	F_age_30_thu_21t24_foot
        self.F_age_30_fri_00t06_foot	=	F_age_30_fri_00t06_foot
        self.F_age_30_fri_06t11_foot	=	F_age_30_fri_06t11_foot
        self.F_age_30_fri_11t14_foot	=	F_age_30_fri_11t14_foot
        self.F_age_30_fri_14t17_foot	=	F_age_30_fri_14t17_foot
        self.F_age_30_fri_17t21_foot	=	F_age_30_fri_17t21_foot
        self.F_age_30_fri_21t24_foot	=	F_age_30_fri_21t24_foot
        self.F_age_30_sat_00t06_foot	=	F_age_30_sat_00t06_foot
        self.F_age_30_sat_06t11_foot	=	F_age_30_sat_06t11_foot
        self.F_age_30_sat_11t14_foot	=	F_age_30_sat_11t14_foot
        self.F_age_30_sat_14t17_foot	=	F_age_30_sat_14t17_foot
        self.F_age_30_sat_17t21_foot	=	F_age_30_sat_17t21_foot
        self.F_age_30_sat_21t24_foot	=	F_age_30_sat_21t24_foot
        self.F_age_30_sun_00t06_foot	=	F_age_30_sun_00t06_foot
        self.F_age_30_sun_06t11_foot	=	F_age_30_sun_06t11_foot
        self.F_age_30_sun_11t14_foot	=	F_age_30_sun_11t14_foot
        self.F_age_30_sun_14t17_foot	=	F_age_30_sun_14t17_foot
        self.F_age_30_sun_17t21_foot	=	F_age_30_sun_17t21_foot
        self.F_age_30_sun_21t24_foot	=	F_age_30_sun_21t24_foot
        self.F_age_40_mon_00t06_foot	=	F_age_40_mon_00t06_foot
        self.F_age_40_mon_06t11_foot	=	F_age_40_mon_06t11_foot
        self.F_age_40_mon_11t14_foot	=	F_age_40_mon_11t14_foot
        self.F_age_40_mon_14t17_foot	=	F_age_40_mon_14t17_foot
        self.F_age_40_mon_17t21_foot	=	F_age_40_mon_17t21_foot
        self.F_age_40_mon_21t24_foot	=	F_age_40_mon_21t24_foot
        self.F_age_40_tue_00t06_foot	=	F_age_40_tue_00t06_foot
        self.F_age_40_tue_06t11_foot	=	F_age_40_tue_06t11_foot
        self.F_age_40_tue_11t14_foot	=	F_age_40_tue_11t14_foot
        self.F_age_40_tue_14t17_foot	=	F_age_40_tue_14t17_foot
        self.F_age_40_tue_17t21_foot	=	F_age_40_tue_17t21_foot
        self.F_age_40_tue_21t24_foot	=	F_age_40_tue_21t24_foot
        self.F_age_40_wed_00t06_foot	=	F_age_40_wed_00t06_foot
        self.F_age_40_wed_06t11_foot	=	F_age_40_wed_06t11_foot
        self.F_age_40_wed_11t14_foot	=	F_age_40_wed_11t14_foot
        self.F_age_40_wed_14t17_foot	=	F_age_40_wed_14t17_foot
        self.F_age_40_wed_17t21_foot	=	F_age_40_wed_17t21_foot
        self.F_age_40_wed_21t24_foot	=	F_age_40_wed_21t24_foot
        self.F_age_40_thu_00t06_foot	=	F_age_40_thu_00t06_foot
        self.F_age_40_thu_06t11_foot	=	F_age_40_thu_06t11_foot
        self.F_age_40_thu_11t14_foot	=	F_age_40_thu_11t14_foot
        self.F_age_40_thu_14t17_foot	=	F_age_40_thu_14t17_foot
        self.F_age_40_thu_17t21_foot	=	F_age_40_thu_17t21_foot
        self.F_age_40_thu_21t24_foot	=	F_age_40_thu_21t24_foot
        self.F_age_40_fri_00t06_foot	=	F_age_40_fri_00t06_foot
        self.F_age_40_fri_06t11_foot	=	F_age_40_fri_06t11_foot
        self.F_age_40_fri_11t14_foot	=	F_age_40_fri_11t14_foot
        self.F_age_40_fri_14t17_foot	=	F_age_40_fri_14t17_foot
        self.F_age_40_fri_17t21_foot	=	F_age_40_fri_17t21_foot
        self.F_age_40_fri_21t24_foot	=	F_age_40_fri_21t24_foot
        self.F_age_40_sat_00t06_foot	=	F_age_40_sat_00t06_foot
        self.F_age_40_sat_06t11_foot	=	F_age_40_sat_06t11_foot
        self.F_age_40_sat_11t14_foot	=	F_age_40_sat_11t14_foot
        self.F_age_40_sat_14t17_foot	=	F_age_40_sat_14t17_foot
        self.F_age_40_sat_17t21_foot	=	F_age_40_sat_17t21_foot
        self.F_age_40_sat_21t24_foot	=	F_age_40_sat_21t24_foot
        self.F_age_40_sun_00t06_foot	=	F_age_40_sun_00t06_foot
        self.F_age_40_sun_06t11_foot	=	F_age_40_sun_06t11_foot
        self.F_age_40_sun_11t14_foot	=	F_age_40_sun_11t14_foot
        self.F_age_40_sun_14t17_foot	=	F_age_40_sun_14t17_foot
        self.F_age_40_sun_17t21_foot	=	F_age_40_sun_17t21_foot
        self.F_age_40_sun_21t24_foot	=	F_age_40_sun_21t24_foot
        self.F_age_50_mon_00t06_foot	=	F_age_50_mon_00t06_foot
        self.F_age_50_mon_06t11_foot	=	F_age_50_mon_06t11_foot
        self.F_age_50_mon_11t14_foot	=	F_age_50_mon_11t14_foot
        self.F_age_50_mon_14t17_foot	=	F_age_50_mon_14t17_foot
        self.F_age_50_mon_17t21_foot	=	F_age_50_mon_17t21_foot
        self.F_age_50_mon_21t24_foot	=	F_age_50_mon_21t24_foot
        self.F_age_50_tue_00t06_foot	=	F_age_50_tue_00t06_foot
        self.F_age_50_tue_06t11_foot	=	F_age_50_tue_06t11_foot
        self.F_age_50_tue_11t14_foot	=	F_age_50_tue_11t14_foot
        self.F_age_50_tue_14t17_foot	=	F_age_50_tue_14t17_foot
        self.F_age_50_tue_17t21_foot	=	F_age_50_tue_17t21_foot
        self.F_age_50_tue_21t24_foot	=	F_age_50_tue_21t24_foot
        self.F_age_50_wed_00t06_foot	=	F_age_50_wed_00t06_foot
        self.F_age_50_wed_06t11_foot	=	F_age_50_wed_06t11_foot
        self.F_age_50_wed_11t14_foot	=	F_age_50_wed_11t14_foot
        self.F_age_50_wed_14t17_foot	=	F_age_50_wed_14t17_foot
        self.F_age_50_wed_17t21_foot	=	F_age_50_wed_17t21_foot
        self.F_age_50_wed_21t24_foot	=	F_age_50_wed_21t24_foot
        self.F_age_50_thu_00t06_foot	=	F_age_50_thu_00t06_foot
        self.F_age_50_thu_06t11_foot	=	F_age_50_thu_06t11_foot
        self.F_age_50_thu_11t14_foot	=	F_age_50_thu_11t14_foot
        self.F_age_50_thu_14t17_foot	=	F_age_50_thu_14t17_foot
        self.F_age_50_thu_17t21_foot	=	F_age_50_thu_17t21_foot
        self.F_age_50_thu_21t24_foot	=	F_age_50_thu_21t24_foot
        self.F_age_50_fri_00t06_foot	=	F_age_50_fri_00t06_foot
        self.F_age_50_fri_06t11_foot	=	F_age_50_fri_06t11_foot
        self.F_age_50_fri_11t14_foot	=	F_age_50_fri_11t14_foot
        self.F_age_50_fri_14t17_foot	=	F_age_50_fri_14t17_foot
        self.F_age_50_fri_17t21_foot	=	F_age_50_fri_17t21_foot
        self.F_age_50_fri_21t24_foot	=	F_age_50_fri_21t24_foot
        self.F_age_50_sat_00t06_foot	=	F_age_50_sat_00t06_foot
        self.F_age_50_sat_06t11_foot	=	F_age_50_sat_06t11_foot
        self.F_age_50_sat_11t14_foot	=	F_age_50_sat_11t14_foot
        self.F_age_50_sat_14t17_foot	=	F_age_50_sat_14t17_foot
        self.F_age_50_sat_17t21_foot	=	F_age_50_sat_17t21_foot
        self.F_age_50_sat_21t24_foot	=	F_age_50_sat_21t24_foot
        self.F_age_50_sun_00t06_foot	=	F_age_50_sun_00t06_foot
        self.F_age_50_sun_06t11_foot	=	F_age_50_sun_06t11_foot
        self.F_age_50_sun_11t14_foot	=	F_age_50_sun_11t14_foot
        self.F_age_50_sun_14t17_foot	=	F_age_50_sun_14t17_foot
        self.F_age_50_sun_17t21_foot	=	F_age_50_sun_17t21_foot
        self.F_age_50_sun_21t24_foot	=	F_age_50_sun_21t24_foot
        self.F_age_60_mon_00t06_foot	=	F_age_60_mon_00t06_foot
        self.F_age_60_mon_06t11_foot	=	F_age_60_mon_06t11_foot
        self.F_age_60_mon_11t14_foot	=	F_age_60_mon_11t14_foot
        self.F_age_60_mon_14t17_foot	=	F_age_60_mon_14t17_foot
        self.F_age_60_mon_17t21_foot	=	F_age_60_mon_17t21_foot
        self.F_age_60_mon_21t24_foot	=	F_age_60_mon_21t24_foot
        self.F_age_60_tue_00t06_foot	=	F_age_60_tue_00t06_foot
        self.F_age_60_tue_06t11_foot	=	F_age_60_tue_06t11_foot
        self.F_age_60_tue_11t14_foot	=	F_age_60_tue_11t14_foot
        self.F_age_60_tue_14t17_foot	=	F_age_60_tue_14t17_foot
        self.F_age_60_tue_17t21_foot	=	F_age_60_tue_17t21_foot
        self.F_age_60_tue_21t24_foot	=	F_age_60_tue_21t24_foot
        self.F_age_60_wed_00t06_foot	=	F_age_60_wed_00t06_foot
        self.F_age_60_wed_06t11_foot	=	F_age_60_wed_06t11_foot
        self.F_age_60_wed_11t14_foot	=	F_age_60_wed_11t14_foot
        self.F_age_60_wed_14t17_foot	=	F_age_60_wed_14t17_foot
        self.F_age_60_wed_17t21_foot	=	F_age_60_wed_17t21_foot
        self.F_age_60_wed_21t24_foot	=	F_age_60_wed_21t24_foot
        self.F_age_60_thu_00t06_foot	=	F_age_60_thu_00t06_foot
        self.F_age_60_thu_06t11_foot	=	F_age_60_thu_06t11_foot
        self.F_age_60_thu_11t14_foot	=	F_age_60_thu_11t14_foot
        self.F_age_60_thu_14t17_foot	=	F_age_60_thu_14t17_foot
        self.F_age_60_thu_17t21_foot	=	F_age_60_thu_17t21_foot
        self.F_age_60_thu_21t24_foot	=	F_age_60_thu_21t24_foot
        self.F_age_60_fri_00t06_foot	=	F_age_60_fri_00t06_foot
        self.F_age_60_fri_06t11_foot	=	F_age_60_fri_06t11_foot
        self.F_age_60_fri_11t14_foot	=	F_age_60_fri_11t14_foot
        self.F_age_60_fri_14t17_foot	=	F_age_60_fri_14t17_foot
        self.F_age_60_fri_17t21_foot	=	F_age_60_fri_17t21_foot
        self.F_age_60_fri_21t24_foot	=	F_age_60_fri_21t24_foot
        self.F_age_60_sat_00t06_foot	=	F_age_60_sat_00t06_foot
        self.F_age_60_sat_06t11_foot	=	F_age_60_sat_06t11_foot
        self.F_age_60_sat_11t14_foot	=	F_age_60_sat_11t14_foot
        self.F_age_60_sat_14t17_foot	=	F_age_60_sat_14t17_foot
        self.F_age_60_sat_17t21_foot	=	F_age_60_sat_17t21_foot
        self.F_age_60_sat_21t24_foot	=	F_age_60_sat_21t24_foot
        self.F_age_60_sun_00t06_foot	=	F_age_60_sun_00t06_foot
        self.F_age_60_sun_06t11_foot	=	F_age_60_sun_06t11_foot
        self.F_age_60_sun_11t14_foot	=	F_age_60_sun_11t14_foot
        self.F_age_60_sun_14t17_foot	=	F_age_60_sun_14t17_foot
        self.F_age_60_sun_17t21_foot	=	F_age_60_sun_17t21_foot
        self.F_age_60_sun_21t24_foot	=	F_age_60_sun_21t24_foot
