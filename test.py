from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to flask"
  
@app.route('/route1')
def route1():
  return 'Welcome to route 1'

@app.route('/route2')
def route2():
  return 'Welcome to route 2'

if __name__ == '__main__':
  app.run(debug=True)
