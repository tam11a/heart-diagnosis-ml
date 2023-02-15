from flask import Flask, request, render_template
from ml import calculate


app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('form.html')


@app.route('/calculate', methods=['GET'])
def calculateApi():
    input_age = request.args.get('input_age')
    input_systolicBP = request.args.get('input_systolicBP')
    input_diastolicBP = request.args.get('input_diastolicBP')
    input_troponin = request.args.get('input_troponin')
    input_chestpainandpainilefthandnadjaw = request.args.get(
        'input_chestpainandpainilefthandnadjaw')
    input_ECG = request.args.get('input_ECG')
    result = calculate(input_age, input_systolicBP, input_diastolicBP,
                       input_troponin, input_chestpainandpainilefthandnadjaw, input_ECG)
    return render_template('result.html', score=result['score'])


if __name__ == '__main__':
    app.run()
