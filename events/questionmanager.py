import discord
from discord.ext import commands
from redbot.core import Config, bank
import random

class QuestionManager:

    def __init__(self):
        self.config = Config.get_conf(self, 8358350000, force_registration=True)
        
        # self.config.register_guild(**VALUES)