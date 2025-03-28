from flask import Flask, redirect, render_template, request, url_for

from pathlib import Path

from .storage import get_klanten, insert_klant
from .commandos import register_commands

def create_app():
    app = Flask(__name__)
    app.config.from_mapping({"DATABASE_URI":Path(__name__, "data.db")})

    register_commands(app)
    @app.route('/')
    def get_lijst():
        klanten = get_klanten()
        return render_template('index.html', klanten= klanten)
    
    @app.route('/nieuw', methods=['GET', 'POST'])
    def nieuwe_klant():
        if request.method == 'POST':
            nr = int(request.form['nr'])
            naam = request.form['naam']
            try:
                insert_klant(nr, naam)
                #klanten = get_klanten()
                #return render_template('index.html', klanten=klanten)
                return redirect(url_for('get_lijst'))
            except ValueError:
                return render_template('new_klant.html', nr=nr, naam=naam,error='klantnr bestaat al')
        return render_template('new_klant.html')
    return app