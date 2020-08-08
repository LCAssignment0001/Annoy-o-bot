from pony.orm import *

db = Database()


def setupDb(name):
    set_sql_debug(False)
    db.bind(provider='sqlite', filename=name, create_db=True)
    db.generate_mapping(create_tables=True)
    commit()


# Primary table - contains information on whom to greet with what message
class MessageConfiguration(db.Entity):
    # guild_id = Required(int, size=64)
    user_id = PrimaryKey(int, size=64)
    message = Required(str)
    annoyance = Required(bool)
    # PrimaryKey(guild_id, user_id)


# Auxiliary table - contains information on what channels to greet people in
class WelcomeChannelConfiguration(db.Entity):
    guild_id = PrimaryKey(int, size=64)
    channel_id = Required(int, size=64)
