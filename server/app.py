#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:text>')
def print_string(text):
    print(text) #  print the string in the console
    return text # Display it in the web browser

@app.route('/count/<int:num>')
def count(num):
    numbers = [str(i) for i in range(num + 1)] 
    return "<br>".join(numbers)


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "div" and num2 != 0:
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "%" and num2 != 0:
        result = num1 % num2
    
    if result is not None:
        
        return str(result)
    else:
        return "Error: Invalid operation"

    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
