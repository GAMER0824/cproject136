from flask import Flask,request,jsonify 
from project_data import data

app = Flask(__name__)

@app.route("/stars")
def star():
    name = request.args.get("name")
    stars = next(i for i in data if i['name'] == name)
    return jsonify({
        "data":stars,
        "message":"success"
    })

if __name__ == "__main__":
    app.run()