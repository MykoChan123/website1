from flask import Flask, render_template, request, jsonify, session, redirect, url_for,send_from_directory
from datetime import timedelta
import os
app = Flask(__name__)


@app.route('/res/<path:filename>')
def serve_res(filename):
    return send_from_directory(os.path.join(os.getcwd(), 'static/res'), filename)


@app.route("/")
def home():
    return render_template("webchoose.html")

@app.route("/installguide")
def installguide():
    return render_template("installguide.html")

@app.route('/pincard')
def pincard():
    return render_template('pincard.html')

@app.route('/tier')
def tier():
    return render_template('tier.html')

@app.route('/website')
def website():
    return render_template('website.html')

@app.route('/website-lite')
def website_lite():
    return render_template('website-lite.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
