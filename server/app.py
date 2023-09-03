#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f"<h1>{title}</h1>"

@app.route('/print/<string:string_parameter>')
def print_string(string_parameter):
    print(f"{string_parameter}")
    return f"{string_parameter}"

@app.route('/count/<int:int_parameter>')
def count(int_parameter):
    numbers = range(int_parameter)
    numbers_text = "\n".join(map(str, numbers))
    numbers_text += '\n'
    return numbers_text

@app.route('/math/<path:parameters>')
def math(parameters):
    try:
        num1, operator, num2 = parameters.split('/')
        num1 = float(num1)
        num2 = float(num2)

        result = None

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == 'div':
            if num2 != 0:
                result = num1 / num2
                return f"{result:.1f}"
            else:
                return ValueError
        elif operator == '%':
            result = num1 % num2
        else:
            return ValueError

        return str(int(result))
    except ValueError:
        return ValueError