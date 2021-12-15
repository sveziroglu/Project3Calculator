import csv
from datetime import datetime

from flask import Flask, render_template, url_for, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Pylintandothers')
def Pylintandothers():
    return render_template('Pylintandothers.html')

@app.route('/aaatesting')
def aaatesting():
    return render_template('AAAtesting.html')

@app.route('/oop')
def oop():
    return render_template('OOP.html')

@app.route('/solid')
def solid():
    return render_template('SOLID.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        val1 = int(request.form['val1'])
        val2 = int(request.form['val2'])
        opr = request.form['rbOpr']
        res = 0
        if opr == 'add':
            res = val1 + val2
        elif opr == 'sub':
            res = val1 - val2
        elif opr == 'multiply':
            res = val1 * val2
        elif opr == 'divide':
            res = val1/val2
        data = {
            'res':res,
        }
        write_csv(val1,val2,opr,res)
    except Exception as e:
        data = {
            'res':str(e)
        }
    return render_template('result.html', data=data)


@app.route('/calculations_history')
def calculations_history():
    time = []
    val1 = []
    val2 = []
    opr = []
    res = []
    history = []

    with open('cal_history.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if len(row) < 1:
                break
            history.append(row)
            # time.append(row[0])
            # val1.append(row[1])
            # val2.append(row[2])
            # opr.append(row[3])
            # res.append(row[4])
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')
        data = {
            'history': history,
            # 'time':time,
            # 'val1':val1,
            # 'val2':val2,
            # 'opr':opr,
            # 'res':res
        }
        return render_template('calculation_history.html', data=data)
def write_csv(val1,val2,opr, res):
    file = open('cal_history.csv', mode='a', newline='')
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M'), val1,val2,opr,res])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
