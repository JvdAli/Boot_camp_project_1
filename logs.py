from flask import Flask
from src.logger import logging

app = Flask(__name__)   #creating a flask object  

@app.route('/', methods = ['GET','POST'])     #defining flask route
def index():                                  # defining function
    logging.info("We are testing our logging file")
    return "1st DS project by Javed Ali"

if __name__ == "__main__":
    app.run(debug = True)  # running flask app using port 5000