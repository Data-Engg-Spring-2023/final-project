from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/find_language", methods=['GET', 'POST'])
def find_language():
    field = request.form.get("field")
    country = request.form.get("country")
    languages = request.form.get("programminglanguages")

   #convert data to json
    input_data = json.dumps({"field": field, "country": country, "languages": languages })


    #url for model
    url = "http://127.0.0.1:5000/api"
  
    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", results=results.content.decode('UTF-8'))
  
