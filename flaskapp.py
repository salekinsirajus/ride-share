#for Flask app
from flask import Flask, render_template, request, url_for, redirect, session
#for SQLAlchemy session and mapping
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import *
#for WTForms
from wtforms import Form
from wtforms import StringField, TextAreaField, DateField, FloatField, SubmitField, IntegerField
from wtforms import  validators
#for Bootstrap
from flask_bootstrap import Bootstrap

#Binding sqlalchemy to the existing postgresql db
#and producing metadata object
metadata = MetaData()
engine = create_engine("postgresql+psycopg2://dbUsername:passcode@/ecrideshare_db")
metadata.reflect(engine, only=['passengers', 'users', 'trips'])
Base = automap_base(metadata=metadata)
Base.prepare()

#mapping ORM classes to existing PostgreSQL classes
passengers = Base.classes.passengers
users = Base.classes.users
trips = Base.classes.trips

#Global session
Session = sessionmaker(bind=engine)

app = Flask(__name__)
Bootstrap(app)
app.config.from_object('config')

app.secret_key = 'you_cant_know'

class UserInput(Form):
    fName = StringField(u'First Name', [validators.required("Enter your First Name")])
    lName = StringField(u'Last Name', [validators.required("Enter your Last Name")])
    origin = TextAreaField(u'Origin', [validators.required("Where are you leaving from?")])
    destination = TextAreaField(u'Destination', [validators.required("And where are you going to?")])
    dateEarly = DateField(u'Earliest Leaving',[validators.required("Enter the earliest\
                                                                    date you are leaving.")])
    dateLate = DateField(u'Latest Leaving',[validators.required("Enter the latest date\
                                                                    you'll be leaving")])
    money = FloatField(u'Gas Money', [validators.optional("How much do you want from your riders?")])
    seats = IntegerField(u'Number of seats', [validators.optional("Is there enough room?")])
    submit = SubmitField(u'Post')

@app.route('/', methods = ['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/dataInput', methods = ['GET','POST'])
def dataInput():
    form = UserInput(request.form)

    if request.method == 'POST' and form.validate():
        name = request.form[u'fName'] +" " +  request.form['lName']
        origin = request.form[u'origin']
        destination = request.form[u'destination']
        dateearly = request.form[u'dateEarly']
        datelate = request.form[u'dateLate']
        money = request.form[u'money']
        seats = request.form[u'seats']
        session['name'] = name
        sessionSA = Session()

        matchedTrip = []
        print (matchedTrip)
        for trip in sessionSA.query(trips):
            if trip.origin==origin and trip.destination==destination:
                matchedTrip.append(trip)
        if len(matchedTrip) > 0:
            print ("showing the list")
            return render_template("landing.html", matchedTrip = matchedTrip, name = name)
        newUser = users(name=name)
        newTrip = trips(origin=origin, destination=destination, dateearly=dateearly, datelate=datelate, price=money)
        sessionSA.add(newUser)
        sessionSA.add(newTrip)
        sessionSA.commit()

        return redirect(url_for('landing'))
    return render_template('dataInput.html', form = form)

@app.route('/landing')
def landing():
    return render_template('landing.html', name=session['name'])

if __name__ == '__main__':
    app.debug= True
    app.run()
