from flask import render_template, request, redirect # ADDED
from app import app
from models.event_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['post'])
def create():
    date = request.form['Date']
    event_name = request.form['Event']
    number_of_guests = request.form['Number_of_Guests']
    room_location = request.form['Room_Location']
    description = request.form['Description']
    new_task = Event(date, event_name, number_of_guests, room_location, description)
    events.append(new_task)
    return redirect('/events')

