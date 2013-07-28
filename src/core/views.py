from flask import render_template

def index():
    return render_template('index.html')

def example():
    return render_template('scrollstrap.html')
