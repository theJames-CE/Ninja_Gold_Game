#Ninja Gold Game

# Create a new Flask project called ninja_gold
# Create the template as shown in the wireframe above, with 4 separate forms

from flask import Flask, render_template, request, session, redirect
from datetime import datetime, timedelta
import random

app = Flask(__name__)
app.secret_key = 'James wuz here!'

# Have the root route render this page
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        session.permanent = True
        app.permanent_session_lifetime = timedelta(days=1)
    return render_template('index.html', gold=session['gold'], activities=session['activities'])

# Have the "/process_money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route
@app.route('/process_money', methods=['GET', 'POST'])
def process_money():
    if request.method == 'POST' and 'reset_game' in request.form:
        reset_game()
        return redirect('/')

    building = request.form['building']
    earn_min = 0
    earn_max = 0
    activity = ''

    if building == 'farm':
        earn_min = 10
        earn_max = 20
        activity = 'Earned'
    elif building == 'cave':
        earn_min = 5
        earn_max = 10
        activity = 'Earned'
    elif building == 'house':
        earn_min = 2
        earn_max = 5
        activity = 'Earned'
    elif building == 'casino':
        earn_min = -50
        earn_max = 50
        if random.random() < 0.5:
            activity = 'Earned'
        else:
            activity = 'Lost'

    earnings = random.randint(earn_min, earn_max)
    session['gold'] += earnings
    timestamp = datetime.now().strftime('%Y/%m/%d %I:%M%p')
    if earnings < 0:
        activity_message = f"Entered a casino and lost {abs(earnings)} gold... Ouch! ({timestamp})"
    else:
        activity_message = f"Entered a casino and earned {earnings} gold! ({timestamp})"
    session['activities'].append(activity_message)

    return redirect('/')

def reset_game():
    session['gold'] = 0
    session['activities'] = []

if __name__ == '__main__':
    app.run(debug=True)
