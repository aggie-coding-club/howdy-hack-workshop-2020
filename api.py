from flask import Flask, jsonify, request

data = {
    'names': ['Joe', 'Susan', 'Aggie', 'Ol\' Rock'],
    'info': {
        'location': 'College Station'
    }
}

app = Flask(__name__)

@app.route('/')
def home():
    return 'Try the /data, /names, and /location (POST) routes'

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/names', methods=['GET'])
def get_names():
    return jsonify(data['names'])

@app.route('/location', methods=['POST'])
def update_loc():
    city = request.json['name']
    data['info']['location'] = city
    return 'A OK'

if __name__ == '__main__':
    app.run(port=3000)
