"""Using Jinja to Produce Dynamic HTML Pages"""
import requests
import random
import datetime
from flask import Flask, render_template

random_number = random.randint(1,10)
x = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', num=random_number, year = x.year)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_data = requests.get(blog_url).json()
    return render_template('blog.html', posts=blog_data)
    

if __name__ == '__main__':
    app.run(debug=True)