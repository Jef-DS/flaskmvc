from flask import render_template
from .model import UserModel

class UserListView():
    def __init__(self, model:UserModel):
        self.model = model
        self.template = "index_view.html"
    def return_html(self):
        users = self.model.get_users()
        return render_template(self.template, klanten=users)

class NewUserListView():
    def __init__(self, model:UserModel):
        self.model = model
        self.template = "new_klant_view.html"
    def return_html(self):
        nr = ""
        naam = ""
        error = ""
        if self.model.error is not None:
            nr = self.model.current_user.nr
            naam = self.model.current_user.naam
            error = self.model.error
        return render_template(self.template, nr=nr, naam=naam, error=error)