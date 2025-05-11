from flask import Flask, request, jsonify, render_template
from openpyxl import load_workbook
import os

# Tell Flask to look for templates in the current directory
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_value = float(request.json['input'])

    wb = load_workbook('template.xlsx')
    ws = wb.active
    ws['A1'] = input_value

    wb.save('template.xlsx')
    wb = load_workbook('template.xlsx', data_only=True)
    ws = wb.active

    result = ws['B1'].value
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
