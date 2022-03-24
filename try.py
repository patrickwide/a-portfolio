from os.path import join, dirname, realpath

from flask import Flask,render_template,request,redirect,session,jsonify,json
import pymysql
import re
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os



from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import utils
import random

app = Flask(__name__)
app.secret_key = "ssfks6787"#just a rundom string of characters.

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/signs')

#UPLOAD_FOLDER = "static/signs"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST', 'GET'])
def index():
    a = random.random()

    return render_template("index.html",number=a)


@app.route('/pdf', methods=['POST', 'GET'])
def pdf():
    if request.method == "POST":
        number = request.form['number']
        name = str(request.form['name'])

        home = str(request.form['home'])

        date001 = request.form['date001']

        Area001 = request.form['Area001']
        total001 = request.form['total001']

        #<---------------------------------new data here--------------------->
        date002 = request.form['date002']

        Area002 = request.form['Area002']
        total002 = request.form['total002']

        #<---------------------------------new data here--------------------->
        date003 = request.form['date003']

        Area003 = request.form['Area003']
        total003 = request.form['total003']

        #<---------------------------------new data here--------------------->
        date004 = request.form['date004']

        Area004 = request.form['Area004']
        total004 = request.form['total004']


        #<---------------------------------new data here--------------------->
        date005 = request.form['date005']

        Area005 = request.form['Area005']
        total005 = request.form['total005']

        #<---------------------------------new data here--------------------->

        date006 = request.form['date006']

        Area006 = request.form['Area006']
        total006 = request.form['total006']

        file = request.files['image']

        if file == "" or home == "" or date001 == "" or  date002 == "" or  date003 == "" or  date004 == ""or  date005 == "" or  date006 == "" or  Area001 == "" or Area002 == "" or Area003 == "" or Area004 == "" or Area005 == "" or Area006 == "" or total001 == ""  or total002 == ""  or total003 == ""  or total004 == ""  or total005 == ""  or total006 == "":
           return render_template('index.html',msg='please fill all fields')
        else:
            myFilename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], myFilename))

            #we edit a new pdf
            styles = getSampleStyleSheet()
            style = styles["BodyText"]

            canv = canvas.Canvas(f"static/pdf/fareSheet({number}).pdf", pagesize=letter)



            header = Paragraph("<font size=18><h2>AMPLUS INTERNATIONAL LTD</h2>"
                               "<br/><br/>"
                               "<h2>Fare sheet</h2>"
                               "<br/><br/>"
                               "Date:7/9/2021"
                               "</font>", style)

            footer = Paragraph(f"<font size=18><h2>{name}</h2>"
                               "<br/><br/>"
                               "<br/><br/>"
                               "</font>", style)

            total = int(total001) + int(total002) + int(total003) + int(total004) + int(total005) + int(total006)

            data = [['Date', 'From', 'To', 'Amount(ksh)'],
                    ['', '', '', ''],
                    [date001, home, Area001, total001],
                    ['', '', '', ''],
                    [date002 ,home, Area002, total002],
                    ['', '', '', ''],
                    [date003,home, Area003, total003],
                    ['', '', '', ''],
                    [date004, home,Area004, total004],
                    ['', '', '', ''],
                    [date005, home,Area005, total005],
                    ['', '', '', ''],
                    [date006, home,Area006, total006],

                    ['', '', '', ''],
                    ['', '', 'Total:', f"Ksh:{total}"]]

            t = Table(data)
            t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                                   ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
            data_len = len(data)

            for each in range(data_len):
                if each % 2 == 0:
                    bg_color = colors.whitesmoke
                else:
                    bg_color = colors.lightgrey

                t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

            aW = 540  # wrap width
            aH = 650  # wrap height

            w, h = header.wrap(aW, 0)
            header.drawOn(canv, 72, aH)
            aH = aH - h + 20
            # table
            w, h = t.wrap(aW, aH)
            t.drawOn(canv, 72, aH - h)
            aH = (aH - h) - h

            # footer
            w, h = footer.wrap(aW, aH)
            footer.drawOn(canv, 72, aH + 200)

            # sign
            img = file
            img = utils.ImageReader(img)
            img_width, img_height = img.getSize()
            aspect = img_height / float(img_width)
            canv = canv
            canv.saveState()
            canv.drawImage(img, 72, 150, width=100, height=(100 * aspect))
            canv.save()

            name = f"static/pdf/fareSheet({number}).pdf"



            return render_template('canvas.html',name=name)
    else:
        return "error"


# return pymysql.connect("127.0.0.1","root","","login_example")

if __name__ == "__main__":
    app.run(debug=True, port=4890)
