from flask import redirect, request, url_for
from flask.views import View
from .views import NewUserListView, UserListView

from .model import User, UserModel
class UserListController(View):
    def __init__(self):
        self.model = UserModel()
    def dispatch_request(self):
        return UserListView(self.model).return_html()

class NewUserController(View):
    methods = ["GET", "POST"]
    def __init__(self):
        self.model = UserModel()
    def dispatch_request(self):
        if request.method == 'POST':
            nr = int(request.form['nr'])
            naam = request.form['naam']
            try:
                self.model.insert_user(User(nr, naam))
                return redirect(url_for('get_lijst'))
            except ValueError:
                return NewUserListView(self.model).return_html()
        return NewUserListView(self.model).return_html()