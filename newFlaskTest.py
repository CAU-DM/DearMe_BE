from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('newIndex.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    user_info = request.form['user']
    message_info = request.form['message']
    
    time.sleep(3)
    
    print("Received user name:", user_info, " | Received message:", message_info)
    response_data = {
        'status': 'success',
        'message': 'Form data received correctly!'
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
