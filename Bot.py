from datetime import datetime
from disco.bot import Plugin
from disco.bot import parser
from disco.types.message import MessageEmbed
from Database import *
from disco.types.base import Unset
import disco.util.snowflake as snowflake
from Queries import *


class Bot(Plugin):
    def __init__(self, bot, config):
        Plugin.__init__(self, bot=bot, config=config)
        if not self.client.config.configured_db:
            setupDb(self.client.config.db)

    @Plugin.listen('PresenceUpdate')
    def greeting(self, event):
        # print(event.guild.members[event.presence.user.id])
        if getExistsUser(event.user.id):
            # print('if branch')
            if not getAnnoyance(event.user.id):
                # print('success')
                event.guild.channels[548064811607392258].send_message(getMessage(event.user.id))
        else:
            # print('else branch')
            event.guild.channels[548064811607392258].send_message("HELLO, {}".format(event.guild.members[event.presence.user.id]))
        # print(dir(event))
        # event.guild.channels[548064811607392258].send_message("HELLO, {}".format(str(event.user)))



    @Plugin.command('change', '<content:str...>', group='~greet')
    def change(self, event, content):
        if getExistsUser(event.author.id):
            updateMessage(event.author.id, content)
        else:
            insertUser(event.author.id, content)
        # print('Command went through with contents: {}'.format(content))



    @Plugin.command('annoyed', group='~greet')
    def annoyed(self, event):
        if getExistsUser(event.author.id):
            updateAnnoyance(event.author.id)



    @Plugin.command('remove', group='~greet')
    def remove(self, event):
        if getExistsUser(event.author.id):
            removeUser(event.author.id)

