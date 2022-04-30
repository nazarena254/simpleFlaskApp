from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/child')
def child():
    return render_template('child.html')    
