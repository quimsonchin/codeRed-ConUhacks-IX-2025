from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "this is the home page. We gna win hackathon baby!!!"

if __name__ == '__main__':
    app.run(debug=True,port=8000)