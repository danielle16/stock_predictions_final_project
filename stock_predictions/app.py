# import necessary libraries
import os
import pandas as pd 
from sqlalchemy import create_engine, Column, Integer, String, Float, inspect
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################


# from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../stock.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# from .models import Pet


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]

#         pet = Pet(name=name, lat=lat, lon=lon)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("form.html")


# @app.route("/api/pals")StaticPool
#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]

#     pet_data = [{
#         "type": "scattergeo",
#         "locationmode": "USA-states",results
#         "hoverinfo": "text",
#         "marker": {
#             "size": 15,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]async

#     return jsonify(pet_data)
@app.route("/api/db")
def localdb():
    engine = create_engine('sqlite:///stock.db', connect_args={'check_same_thread': False}, poolclass = StaticPool)
    inspector = inspect(engine)
    results = inspector.get_table_names()
    session = Session(bind=engine)
    session.commit()
    session.close()
    return render_template('stocks.html', results=results)
@app.route("/api/stock_table/<stock>", methods=("POST", "GET"))
def localstock(stock):
    engine = create_engine('sqlite:///stock.db', connect_args={'check_same_thread': False}, poolclass = StaticPool).connect()
    session = Session(bind=engine)
    df = pd.read_sql_table(stock, engine)
    session.commit()
    session.close()
    df.sort_values(by=['index'], inplace=True, ascending=False)
    clean_df = df.head(10)
    return render_template('stocks_detail.html', tables=[clean_df.to_html(classes='table table-striped', index=False, table_id = "data")], titles=clean_df.columns.values)
@app.route("/api/stock_submit/<stock>/<days>")
def submit(stock, days):
    stream= os.popen(f"python3 ./predict2v.py {stock} {days} >output.txt &")
    cmd_output = stream.read()
    print(cmd_output)
    return render_template('stocks_submit.html')



if __name__ == "__main__":
    app.run()
