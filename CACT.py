import random
import cassiopeia as cass
import os
import json

from cassiopeia import Summoner
from dotenv import load_dotenv

with open('ChampionInfo.json', encoding="utf8") as f:
    data = json.load(f)

    def getChampionCooldowns(champions):

        for name in champions:
            Q = data[name]["abilities"]["Q"][0]["cooldown"]["modifiers"][0]["values"]
            W = data[name]["abilities"]["W"][0]["cooldown"]["modifiers"][0]["values"]
            E = data[name]["abilities"]["E"][0]["cooldown"]["modifiers"][0]["values"]
            R = data[name]["abilities"]["R"][0]["cooldown"]["modifiers"][0]["values"]
    
            print(name + " hat folgende CD's")
            print("Q:", Q)
            print("W:", W)
            print("E:", E)
            print("R:", R)
    
    getChampionCooldowns(["Aatrox"])
    

#load_dotenv()
#API = os.getenv('LOL_API')

#cass.set_riot_api_key(API)  # This overrides the value set in your configuration/settings.

#DARKSONIC = Summoner(name="TSO DARKSONIC", region="EUW")
#print("{name} is a level {level} summoner on the {region} server.".format(name=DARKSONIC.name,
#                                                                          level=DARKSONIC.level,
#                                                                          region=DARKSONIC.region))
