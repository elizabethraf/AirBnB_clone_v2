#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import MySQLdb

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_db_state(self):
        """Display Database Test"""
         db = MySQLdb.connect(host="localhost",
                         user="username", password="password", db="database")
    query = "SELECT * FROM states\
             ORDER BY states.id ASC"
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        counter_before++
    cursor.close()
    db.close()

