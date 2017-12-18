# Renpy initial Game

# Background images
image bg meadow = "backgrounds/bg_meadow.jpg"
image bg club = "backgrounds/bg_club.jpg"
image bg lecturehall = "backgrounds/bg_lecturehall.jpg"
image bg uni = "backgrounds/bg_uni.jpg"

# Character images
image sylvie blue giggle = "sylvie/sylvie_blue_giggle.png"
image sylvie blue normal = "sylvie/sylvie_blue_normal.png"
image sylvie blue smile = "sylvie/sylvie_blue_smile.png"
image sylvie blue surprised = "sylvie/sylvie_blue_surprised.png"

# Characters
define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

# True if player decides to ask the question
default asked = False

# Starts the Game
label start:

    scene bg lecturehall
    with fade
    show sylvie blue normal
    with dissolve

    s "Hi there! How was class?"

    m "Good..."

    "I can't bring myself to admit that it all went in one ear and out the other."

    m "Are you going home now? Wanna walk back with me?"

    s "Sure! Maybe we can stop by the meadows along the way."

    scene bg meadow
    with fade
    show sylvie blue normal at right
    with dissolve

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie blue smile at center
    with dissolve


    "She turns to me and smiles. She seems so welcoming..."

    menu:
        "Ask her.":
            jump asked
        "Don't ask her.":
            jump noAsked

    label asked:
        $ asked = True

        "I'll ask her...!"

        m "Ummm... Will you..."

        m "Will you be my artist for a visual novel?"

        show sylvie blue surprised

        "Silence."

        show sylvie blue smile

        s "Of course I will! Lets head home and talk about it more."

        jump goHome

    label noAsked:

        "Maybe I'll ask her later..."

        m "Never mind! We should be getting home soon."

        show sylvie blue giggle

        s "Oh! Yes, it's getting late."

        jump goHome

    label goHome:

        "And with that, we walked home."

        scene bg club
        with fade
        show sylvie blue normal
        with dissolve

        "We eventually made it home."

        m "See you later!"

        s "Bye!"

        hide sylvie
        with dissolve

        if asked:

            "I can't wait to start working on this project together!"

            hide bg club
            with dissolve

            ".:. Good Ending."

            return

        else:

            "I guess I'll never be able to ask..."

            hide bg club
            with dissolve
            
            ".:. Bad Ending."

            return
