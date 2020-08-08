from datetime import datetime
from disco.bot import Plugin
from disco.bot import parser
from disco.types.message import MessageEmbed
from Database import *
from disco.types.base import Unset
import disco.util.snowflake as snowflake


class Bot(Plugin):
    def __init__(self, bot, config):
        Plugin.__init__(self, bot=bot, config=config)
        if not self.client.config.configured_db:
            setupDb(self.client.config.db)

    @Plugin.listen('PresenceUpdate')
    def greeting(self, event):
        if
        # print(dir(event))
        # event.guild.channels[548064811607392258].send_message("HELLO, {}".format(str(event.user)))
        return


    @Plugin.command('change', '<content:str...>', group='greet')
    def change(self, event):

        return


    @Plugin.command('annoyed', group='greet')
    def annoyed(self, event):
        return


    @Plugin.command('remove', group='greet')
    def remove(self, event):
        return
