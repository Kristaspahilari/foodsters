from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    f = open('grains.txt')
    grains= f.read().splitlines()
    f = open('vegetables.txt')
    vegetables= f.read().splitlines()
    f = open('fruits.txt')
    fruits= f.read().splitlines()
    f = open('dairy.txt')
    dairy= f.read().splitlines()
    f = open('meat.txt')
    meat= f.read().splitlines()
    return render_template('home.html', grains_list=grains, vegetables_list=vegetables, fruits_list=fruits, dairy_list=dairy, meat_list=meat) 


    
@app.route("/recipes")
def recipes():
    return render_template('recipes.html')


@app.route("/recipes/<string:name>")
def profile(username):
    return render_template('recipe.html')