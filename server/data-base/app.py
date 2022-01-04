import pymysql
from flask import Flask
from model_tables.db_connect import db

from setting_db import mysql_db

from api import user
# from analysis import sales
from api_sales import sales_graph
from api_foot_traffic import foot_traffic_graph
from api_sector_sales import sector_sales_graph
from api_income_expense import income_expense_graph
from api_facilities import facilities_graph

app = Flask(__name__)
app.register_blueprint(user)
# app.register_blueprint(sales)
app.register_blueprint(sales_graph)
app.register_blueprint(foot_traffic_graph)
app.register_blueprint(sector_sales_graph)
app.register_blueprint(income_expense_graph)
app.register_blueprint(facilities_graph)

# korean encoding
app.config['JSON_AS_ASCII'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{mysql_db.id}:{mysql_db.pw}@{mysql_db.ip}:3306/{mysql_db.name}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
    
