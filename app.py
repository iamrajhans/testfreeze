from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    print('in hello ')
    return render_template('index.html')

app.run()
