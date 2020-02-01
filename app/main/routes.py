from app.main import bp as app
from flask import render_template
from flask_login import login_required

@app.route('/',methods=['GET'])
@login_required
def index():
    return render_template('main/index.html', title="Dashboard")