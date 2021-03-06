from flask import Flask, render_template, request
import os
import requests
import json



app = Flask(__name__)

def get_stock_data(symbol):
    # generate request URL
    url = "https://cloud.iexapis.com/v1/"
    token = os.environ.get("API_KEY")
    params = {"token": token}
    stock = 'stock/' + str(symbol) + '/chart'
    
    # get response
    resp = requests.get(url + stock, params=params)

    # jsonify response
    result = resp.json()
    
    return result

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/quote")
def get_stock_price():
    symbol = request.args.get("symbol")
    stock_data = get_stock_data(symbol)
    stock_data = stock_data[0]

    return render_template("quote.html", symbol=symbol, stock_data=stock_data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
