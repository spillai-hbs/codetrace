from flask import Flask, request, jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/add')
def add():
    data = request.args.get('data', None)
    if data:
        try:
            _list = list(map(int, data.split(',')))
            total = sum(_list)
            return 'Result= ' + str(total)
        except ValueError:
            return jsonify(error="Invalid input. Data should be a comma-separated list of integers."), 400
    else:
        return jsonify(error="No data provided."), 400

def sum(arg):
    total = 0
    try:
        for val in arg:
            total += val
    except Exception:
        return "Error occurred!", 500
    return total
