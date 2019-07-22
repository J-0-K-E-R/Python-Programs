from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def json():
    # value = request.json
    # res = 90
    return jsonify({'result': ['A','37','87Par']})
    # return value

if __name__ == '__main__':
    app.run(debug=True)