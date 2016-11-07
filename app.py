# creation of Web application for SHU Financial portal#

import flask
__import__(render_template)

from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def main():
   return render_template('index.html')

if __name__=="__main__":
   app.run()

#from flask import Flask, render_template

#def main():
    #return render_template('index.html')
#if __name__=="__main__":


