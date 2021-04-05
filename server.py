from flask import Flask, redirect, url_for, render_template, request
import base64
from io import BytesIO
# import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import csv
import numpy as np


app = Flask(__name__)

@app.route("/<name>")
def admin(name):
  return render_template("index.html", content=name)

@app.route("/", methods=["POST", "GET"])
def home():
 
  if request.method == "POST":
    chs = list(map(int, request.form["input"].split(" ")))
    firedata = np.genfromtxt('data-fire-only.csv',delimiter=',')
    firedata = firedata[1:,:]
    time = (firedata[:,0] - 750002617) / 10000000

    # print(firedata[:,input])
    graph = Figure()
    graph.subplots().plot(time, firedata[:,chs])
    buf = BytesIO()
    graph.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
  else:
    return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)