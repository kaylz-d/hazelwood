# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cathy Kuhlmeier", image="player")
define leslie = Character("Leslie Smart", image="leslie")
define leanne = Character("Leanne Tippett", image="leanne")

image player neutral = "side player neutral.png"
image leslie neutral = "Miley.webp"
image leanne neutral = "performative_neutral.png"

#backgrounds
image bg classroom = "classroom_morning.webp"
image bg corridor = "school_corridor_background.webp"


# The game starts here.

label start:

    scene bg black
    show text "Hazelwood East High School, 1983" at truecenter

    scene bg classroom with dissolve
    c happy "OKAY, I submitted our articles to The Spectrum."
    

    return
