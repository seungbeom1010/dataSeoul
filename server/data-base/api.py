from flask import Blueprint, render_template, request, jsonify

user = Blueprint('user', __name__)

@user.route("/")
def home():
    return render_template("/index.html")

@user.route("/success")
def success():
    tasks = [
        {
            'id':1,
            'task':'this is first task'
        },
        {
            'id':2,
            'task':'this is another task'
        },
        {
            'id':3,
            'task':'안녕'
        }
    ]
    return jsonify({'status':'success', 'data':tasks})  #will return the json

@user.route("/error")
def error():
    # 서버 문제
    tasks = [
        {
            'id':1,
            'task':'현재 데이터를 불러올 수 없습니다.'
        }
    ]
    return jsonify({'status':'error', 'data':tasks})

@user.route("/fail")
def fail():
    # request 문제
    tasks = [
        {
            'id':1,
            'task':'22년 데이터는 없습니다'
        }
    ]
    return jsonify({'status':'fail', 'data':tasks})


