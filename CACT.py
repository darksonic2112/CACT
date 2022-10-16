import cassiopeia as cass
import json
import tkinter as tk

from cassiopeia import Summoner
from dotenv import load_dotenv
from tkinter.ttk import *

# getting Championinfo out of json file
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
    
# Window to display info
master = tk.Tk()
master.title("CACT")
master.geometry("200x100")

# Creates Textbox
summoner_entry = Entry(master, width = 20)
summoner_entry.insert(0, "Summoner Name")
summoner_entry.pack(padx = 5, pady = 5)

# Function to delete sample text in textbox
def temp_text(e):
    summoner_entry.delete(0, "end")
    
summoner_entry.bind("<FocusIn>", temp_text)

# Opens window where information gets displayed
def open_new_window():
    new_window = tk.Toplevel(master)
    new_window.title("CACT")
    new_window.geometry("1000x500")
    Label(new_window,
            text= "This is a new window").pack

btn = Button(master,
        text= "Search",
        comman = open_new_window)
btn.pack(pady = 10)

tk.mainloop()
    

#load_dotenv()
#API = os.getenv('LOL_API')

#cass.set_riot_api_key(API)  # This overrides the value set in your configuration/settings.

#DARKSONIC = Summoner(name="TSO DARKSONIC", region="EUW")
#print("{name} is a level {level} summoner on the {region} server.".format(name=DARKSONIC.name,
#                                                                          level=DARKSONIC.level,
#                                                                          region=DARKSONIC.region))
