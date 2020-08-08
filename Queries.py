from pony.orm import *
from Database import *


# This function checks if the user's record is in the database
@db_session
def getExistsUser(user_id):
    return exists(u for u in 'MessageConfiguration' if u.user_id == user_id)


# This function checks if a user has been annoyed by greetings
@db_session
def getAnnoyance(user_id):
    if getExistsUser(user_id):
        user = select(u for u in 'MessageConfiguration' if u.user_id == user_id)
        return user.annoyance
    else:
        return False


# This function inserts a user's records into the database
# The function is intended to be called when a user wants to go from a default greeting message to a personalised one
@db_session
def insertUser(user_id, guild_id, message):
    db.insert('MessageConfiguration', user_id=user_id, guild_id=guild_id, message=message, annoyance=False)
    return


# This function updates a user's personalised message
@db_session
def updateMessage(user_id, guild_id, message):
    user = select(u for u in 'MessageConfiguration' if (u.user_id == user_id and u.guild_id == guild_id))
    user.message = message
    return


# This function updates a user's annoyance level
@db_session
def updateAnnoyance(user_id):
    for user in select(u for u in 'MessageConfiguration' if (u.user_id == user_id)):
        user.annoyance = True
    return


# This function removes a user's record from the database, returning their greeting message to the default option
@db_session
def removeUser(user_id, guild_id):
    delete(u for u in 'MessageConfiguration' if (u.user_id == user_id and u.guild_id == guild_id))
    return