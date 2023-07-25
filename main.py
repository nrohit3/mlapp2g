from flask import Flask
from mltrain import prep_data

app=Flask(__name__)

@app.route("/")
def route1():
    return prep_data()


if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=8084)