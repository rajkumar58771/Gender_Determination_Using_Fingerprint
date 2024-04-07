from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    # Run the Python script
    subprocess.run(['python', 'final_fp_gender.py'])
    return 'Script executed successfully'

if __name__ == '__main__':
    app.run(debug=True)
