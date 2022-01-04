from flask import Blueprint, render_template, request, redirect, url_for, jsonify, json
from models import Sales

sales = Blueprint('sales',__name__)

@sales.route("/commercialAnalysis", methods=["POST"])
def analysis():
    targetyear = request.form['yearforanalysis']
    targetdynamic = Sales.query.filter(Sales.year == targetyear, Sales.commercialratechangename == "다이나믹").count()
    targetbigger = Sales.query.filter(Sales.year == targetyear, Sales.commercialratechangename == "상권확장").count()
    targetstagnate = Sales.query.filter(Sales.year == targetyear, Sales.commercialratechangename == "정체").count()
    targetreduction = Sales.query.filter(Sales.year == targetyear, Sales.commercialratechangename == "상권축소").count()

    data = [{
        "year": targetyear,
        "dynamic": targetdynamic,
        "bigger": targetbigger,
        "stagnate" : targetstagnate,
        "reduction": targetreduction
    }]

    return json.dumps(data)