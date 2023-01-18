#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage_t, storage

class State(BaseModel):
    """ State class """
    name = ""
    if storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """Define State"""
        super().__init__(*args, **kwargs)

    if storage_t != "db":
        @property
        def cities(self):
            """Define getter for list of city instances"""
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
