from flask import Flask, render_template, make_response, send_from_directory
import random
app = Flask(__name__)

temp = '13'

def level_1():
    options = ["rock", "paper", "scissors"]
    answer = random.choice(options)
    return answer

def level_2():
    options = ["rock", "paper", "scissors", "fire", "water"]
    answer = random.choice(options)
    return answer

def level_3():
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    answer = random.choice(options)
    return answer



@app.route('/weather')
def hello():
    vxml = render_template('weather.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1')
def lab1():
    vxml = render_template('lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1-booking')
def lab1_booking():
    vxml = render_template('lab1-booking.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1-information')
def lab1_information():
    vxml = render_template('lab1-information.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab2')
def lab2():
    vxml = render_template('lab2.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab3')
def lab3():
    vxml = render_template('lab3.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab4')
def lab4():
    vxml = render_template('lab4.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)


@app.route('/final')
def final():
    vxml = render_template('final.xml', standard=level_1(), funny=level_2(), hard=level_3())
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response
