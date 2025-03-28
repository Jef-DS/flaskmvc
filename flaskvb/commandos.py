import click    
from flask.cli import with_appcontext

from .storage import init_db#, get_klanten, insert_klant

@click.command('create')
@with_appcontext
def init_db_command():
    init_db()
def register_commands(app):
    app.cli.add_command(init_db_command)