# The script of the game goes in this file.

# Callbacks for Text Voice
init python: 
    def callbackSal (event, **kwargs):
        if event == "show":
            renpy.music.play("male_standard_1.ogg", channel="sound", loop=True)
            renpy.music.play("male_standard_2.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

init python: 
    def callbackAxe (event, **kwargs):
        if event == "show":
            renpy.music.play("quick_3.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

init python: 
    def callbackRazz (event, **kwargs):
        if event == "show":
            renpy.music.play("demon_1.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

init python: 
    def callbackJJ (event, **kwargs):
        if event == "show":
            renpy.music.play("robot_2.ogg",channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

init python: 
    def callbackRoh (event, **kwargs):
        if event == "show":
            renpy.music.play("male_deep_4.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")
   

define s = Character("Salmon", color="#fcc203", callback=callbackSal)
define a = Character("Axe", color="#00c90a", callback=callbackAxe)
define r = Character("Razz", color="#858585", callback=callbackRazz)
define j = Character("John Jameston John", color="#00b9c9", callback=callbackJJ)
define roh = Character("Rohan", color="#8dab4b", callback=callbackRoh)

define narr = Character(color="#f7ad57ff")

# The game starts here.

label start:
    narr "Transferring to Pathfind High after your freshman year in 
    D&D High was not an easy choice"

label test: 
    narr "{color=#f7ad57ff} test {/color}"

    j "My name is John...{p=0.5}Jameston John, {p=1.0}At your service."

    r "{size=70} WHO CARES!!!{/sze} {p=0.3}My name is more important!"
    r "It's Razz nyehehe..."

    a "I'm Axe !!!!!!"

    s "And I'm Salmon. It's nice to meet you."

    a "And I'm Axe !!!!!!!!!!!!!!!"

    narr "Salmon smiles at Axe."

    s "You already said that Axe."

    a " I know, I just wanted to say it again hehehe!!!"

    roh "Hello, my name is Rohan. Pleasure to meet you."

    return
