# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cathy Kuhlmeier", image="player")
define leslie = Character("Leslie Smart", image="leslie")
define leanne = Character("Leanne Tippett", image="leanne")
define rey = Character("Principal Reynolds", image="reynolds")

image player neutral = "side player neutral.png"
image leslie neutral = "Miley.webp"
image leanne neutral = "chaewon.png"
image reynolds neutral = "performative_neutral.png"

#backgrounds
image bg classroom = "classroom_morning.webp"
image bg corridor = "school_corridor_background.webp"
image bg black = "black.jpg"

image myText = Text("{color=#ffffff}Hazelwood East High School, 1983{/color}", size=50)
image myText2 = Text("{color=#ffffff}The next day or something...{/color}", size=50)


# The game starts here.

label start:

    scene bg black
    show myText at truecenter
    with dissolve
    pause
    hide myText with dissolve

    scene bg classroom with dissolve
    c happy "OKAY, I submitted our articles to The Spectrum."

    show leslie neutral at center:
        zoom 2.25
    with dissolve

    leslie neutral "About those students who got pregnant right?"
    hide leslie neutral with dissolve

    show leanne neutral at center:
        zoom 2.25
    with dissolve
    leanne neutral "Yep, plus the kid whose parents got divorced."
    c neutral "I’m so glad we’re bringing up these issues. We need to accurately represent student life."
    hide leanne neutral with dissolve

    scene bg black with dissolve

    show myText2 at truecenter
    with dissolve
    pause
    hide myText2 with dissolve

    scene bg corridor with fade

    show leslie neutral at center:
        zoom 2.25
    with dissolve
    leslie neutral "Girl, look. Everyone’s articles got posted here, except for the pregnancy and divorce ones that we wrote."
    hide leslie neutral with dissolve

    show reynolds neutral at center:
        zoom 2.25
    with dissolve

    rey neutral "No, duh. These topics are really sensitive. You can’t write about them in Spectrum."
    c deadpan "Principal Reynolds…?"
    c shocked "*gasp* YOU CENSORED OUR ARTICLES!"
    c angry "This is a violation of free speech! I am SO gonna sue."

    scene bg black with fade

    return
