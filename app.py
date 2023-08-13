from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def hello_world():
    try:
        message = request.get_json()['message']
        print(message)
        return message
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
