# The script of the game goes in this file.

# Callbacks for Text Voice
init python: 
    def callbackSal (event, **kwargs):
        if event == "show":
            renpy.music.play("voices/male_standard_1.ogg",channel="sound",loop=True)
            renpy.music.play("voices/male_standard_2.ogg",channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

init python: 
    def callbackAxe (event, **kwargs):
        if event == "show":
            renpy.music.play("voices/quick_3.ogg",channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

init python: 
    def callbackRazz (event, **kwargs):
        if event == "show":
            renpy.music.play("voices/demon_1.ogg",channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

init python: 
    def callbackJJ (event, **kwargs):
        if event == "show":
            renpy.music.play("voices/robot_2.ogg",channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

init python: 
    def callbackRoh (event, **kwargs):
        if event == "show":
            renpy.music.play("voices/male_deep_4.ogg",channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

init python: 
    def callbackRain (event, **kwargs):
        if event == "show":
            renpy.music.play("voices/female_light_2.ogg",channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

init python: 
    def callbackNarr (event, **kwargs):
        if event == "show":
            renpy.music.play("voices/narr/Single Keys/keypress-013.wav",channel="sound",loop=True)
            renpy.music.play("voices/narr/Single Keys/keypress-012.wav",channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel = "sound")

# Temp Background
image bg school = "temp/bg school.png"
image bg classroom = "temp/bg classroom.jpg"
# Temp Image Sprites
image axe = "temp/chara/base_00008.png"
image sal = "temp/chara/base_00006.png"
   
# Character Establishment: Names, Color Hex, and Voice Sounds

define s = Character("Salmon", color="#fcc203", callback=callbackSal)
define a = Character("Axe", color="#00c90a", callback=callbackAxe)
define r = Character("Razz", color="#858585", callback=callbackRazz)
define j = Character("John Jameston John", color="#00b9c9", callback=callbackJJ)
define roh = Character("Rohan", color="#8dab4b", callback=callbackRoh)
define rain = Character("Prof. Raine",color = "#6c84a4",callback=callbackRain)

define narr = Character(color="#f7ad57ff", callback=callbackNarr)

# The game starts here.

label start:
    play music "audio/since_2_a.m.mp3" volume 0.4

    scene bg school
    narr"Transferring to Pathfind High after your freshman year in 
    D&D High was not an easy choice"
    narr"Afterall, transferring to {i}this{/i} school is weird."
    narr"Not that it hasn’t been done before but, going to a 
    \nschool with mostly humanoid to hardly any is a dramatic change."
    narr"Especially since Principal A informed you that you are the only human in the school."
    narr"But, that doesn’t stop you from going through the entrance."
label intro:
    scene bg classroom
    narr "After a bit of trouble navigating the school hallways, 
    \nyou finally find yourself inside the classroom of your Forensic Science Class."
    narr"It seems that everyone has already reached the class before you and you are the last one to arrive."

    rain "Ah, welcome, you must be new here, yes?"
    rain "My name is Severina Raine but you can just call me Professor Raine."
    rain "Please, have a seat, I was just discussing who shall be paired with 
    \nwho for the new project that is due in 3 days."
    rain "You can sit with...{p=0.5}Over there-"

    narr "She points to a group of 5 individuals, {p=0.1}
    who already seemed bored by the class."

    rain "-with those five, you’ll get along quite well."

    narr "Walking over there, you hear a couple of students whispering to each other."

    narr "{i}\"No way the new kid is going to stand those five!\"\n{p=0.1} 
    \"They’ll pull their hair out before the class ends with how those five are\"{/i}"

    narr " -And many other things but you pull your seat and sit down."
    narr "Taking a look at your new groupmates. They seem to be an interesting bunch."
    narr "A frog and a fog-like person, a snake and a robot, and a giant goloma." 
    narr "You’ve never seen a goloma before."

    r "Whatchu starin' at?!"
    return
