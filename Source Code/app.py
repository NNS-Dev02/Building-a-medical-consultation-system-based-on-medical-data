import os
import subprocess
import time
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

last_modified = 0

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/write_params', methods=['POST'])
def write_params():
    global last_modified
    current_time = request.form['current_time']
    params = [current_time] + [request.form[f'param{i+1}'] for i in range(6)]
    params_str = ', '.join(params)

    with open('params.txt', 'w') as file:
        file.write(params_str)

    subprocess.Popen(["python", "program.py"])

    return 'OK', 200

@app.route('/check_program', methods=['GET'])
def check_program():
    global last_modified
    try:
        if os.path.getmtime('params.txt') > last_modified:
            last_modified = os.path.getmtime('params.txt')
            return 'File params.txt đã được cập nhật, chương trình program.py sẽ được chạy.'
        else:
            return 'File params.txt chưa có sự thay đổi.'
    except FileNotFoundError:
        return 'File params.txt không tồn tại.'

@app.route('/upload', methods=['POST'])
def upload_file():
    request.files['file'].save('params.txt')
    subprocess.Popen(["python", "program.py"])
    return 'File đã được lưu và chương trình program.py đang chạy'

@app.route('/download')
def download_file():
    return send_file('params.txt', as_attachment=True)

def display_result():
    try:
        time.sleep(10)
        with open('result.txt', 'r') as file:
            content = file.readlines()
            second_line = content[1].strip() if len(content) > 1 else None
        return render_template('result.html', second_line=second_line)
    except FileNotFoundError:
        return 'File result.txt không tồn tại.'
    
@app.route('/get_result_content', methods=['GET'])
def get_result_content():
    try:
        with open('result.txt', 'r') as file:
            content = file.read().strip()
        return content, 200
    except FileNotFoundError:
        return 'File result.txt không tồn tại.', 404

@app.route('/show_results', methods=['GET'])
def show_results():
    return display_result()

@app.route('/KetQuaChuanDoan')
def execute_code_and_display_results():
    subprocess.Popen(["python", "program.py"])
    return display_result()

if __name__ == "__main__":
    app.run(debug=True)