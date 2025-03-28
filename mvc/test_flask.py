import unittest
from .model import User, UserModel
from .storage import init_db
from .config import TestingConfig
from . import create_app

class ModelTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
    
    def test_insert_user_ok(self):
        with self.app.app_context():
            init_db()
            model = UserModel()
            klanten_voor = model.get_users()
            aantal_klanten_voor = len(klanten_voor)
            laatste_nr = max([klant.nr for klant in klanten_voor])
            laatste_nr += 1
            model.insert_user(User(laatste_nr, "nieuwe klant"))
            klanten_na = model.get_users() 
            aantal_klanten_na = len(klanten_na)
            self.assertEqual(aantal_klanten_na, aantal_klanten_voor + 1)
        
    def test_insert_user_niet_ok(self):
        with self.app.app_context():
            init_db()
            model = UserModel()
            klanten_voor = model.get_users()
            aantal_klanten_voor = len(klanten_voor)
            bestaand_nr = max([klant.nr for klant in klanten_voor]) 
            with self.assertRaises(ValueError):
                model.insert_user(User(bestaand_nr, "nieuwe klant"))
            klanten_na = model.get_users()
            aantal_klanten_na = len(klanten_na)
            self.assertEqual(aantal_klanten_voor, aantal_klanten_na)
            self.assertIsNotNone(model.error)
            self.assertIsNotNone(model.current_user)
            self.assertEqual(model.current_user.nr, bestaand_nr)
            self.assertEqual(model.current_user.naam, "nieuwe klant")

if __name__ == '__main__':
    unittest.main()