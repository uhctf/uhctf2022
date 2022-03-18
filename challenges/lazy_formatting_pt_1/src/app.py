from subprocess import CalledProcessError, check_output, STDOUT
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', replace_rule='', input_text='', output_text='')


@app.route('/', methods=['POST'])
def format():
    replace_rule = request.form.get('replace_rule', type=str)
    input_text = request.form.get('input_text', type=str)
    output_text = ''

    try:
        output_text = check_output(
            ['/bin/bash', '-c', f'sed -e {replace_rule}'], input=bytes(input_text, 'utf-8'), stderr=STDOUT).decode('utf-8')
    except CalledProcessError as e:
        output_text = e.output.decode('utf-8')

    return render_template('index.html',
                           replace_rule=replace_rule,
                           input_text=input_text,
                           output_text=output_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
