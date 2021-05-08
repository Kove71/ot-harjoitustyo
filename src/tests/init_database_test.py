import unittest
from initialize_database import create_table, drop_table
from database_connection import get_test_connection

class TestInit(unittest.TestCase):

    def setUp(self):
        self.con = get_test_connection()
        self.cur = self.con.cursor()
        self.test_case = True

    def test_create_table(self):
        create_table(self.test_case)
        self.cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Movies'")
        found_value = self.cur.fetchone()[0]
        self.assertEqual(found_value, 1)

    def test_drop_table(self):
        drop_table(self.test_case)
        self.cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Movies'")
        found_value = self.cur.fetchone()[0]
        self.assertEqual(found_value, 0)