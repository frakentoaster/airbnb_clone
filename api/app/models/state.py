from peewee import *
from base import *


class State(BaseModel):
    name = CharField(128, null = False, unique = True)

    def to_hash(self):
        return {'id' : self.id,
                'create_at' : self.create_at,
                'updated_at' : self.updated_at,
                'name' : self.name
                }
