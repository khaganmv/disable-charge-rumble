import json


file = open("resources/sfx_map.json", "r")
data = [
    entry for entry in json.load(file) if 
        "w_gun" in entry and 
        "charge" in entry and
        not "npc" in entry and
        not "perfect" in entry and
        not "stop" in entry and
        not "Stop" in entry and
        not "silverhand" in entry
]
file.close()

custom_sounds = [{"name": entry, "type": "mod_sfx_2d", "file": "silent.wav", "gain": 1.0, "pitch": 0.0} for entry in data]

file = open("mods/SilentTechWeapons/info.json", "w")
json.dump({
    "name": "Silent Tech Weapons",
    "version": "1.0",
    "customSounds": custom_sounds
}, file, indent=4)
file.close()
