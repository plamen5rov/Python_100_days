"""Using Jinja to Produce Dynamic HTML Pages"""

import random
import datetime
from flask import Flask, render_template

random_number = random.randint(1,10)
x = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', num=random_number, year = x.year)

if __name__ == '__main__':
    app.run(debug=True)