import turtle


s = turtle.getscreen()
t = turtle.Turtle()


def main():
    # initialize
    turtle.title('Plutchiks')
    turtle.setup(800, 700)


# This is where we need to add the sub-divides into the pedals
def pedal(angle: int, colors, emotion: str, words):
    # Color
    t.home()
    t.fillcolor(colors[2])
    t.begin_fill()
    t.lt(angle + 45)
    t.circle(-200, 90)
    t.rt(90)
    t.circle(-200, 90)
    t.rt(90)
    t.end_fill()

    # Sub-divide code
    # Larger Sub-division
    t.fillcolor(colors[1])
    t.begin_fill()
    t.circle(-200, 60)
    t.rt(60)
    t.circle(-200, 30)
    t.rt(60)
    t.circle(-200, 60)
    t.end_fill()

    # Closest Sub-division
    t.fillcolor(colors[0])
    t.begin_fill()
    t.rt(90)
    t.circle(-200, 30)
    t.rt(90)
    t.circle(-200, 30)
    t.rt(90)
    t.circle(-200, 30)
    t.end_fill()

    # Labeling
    # Emotion
    t.pu()
    t.home()
    if emotion == 'Anticipation/Hope':
        t.setpos(-325, 0)
    elif emotion == 'Like':
        t.setpos(0, 300)
    elif emotion == "Joy/Happiness":
        t.setpos(325, 0)
    t.write(emotion, False, "center")
    t.home()
    t.pd()

    # Labeling
    # Words
    for i in range(3):
        t.pu()
        t.home()
        # Edit style within each of the if statements & 
        # use the i number to change the fontsize
        style = ("Arial", 8, "normal")
        if emotion == 'Anticipation/Hope':
            t.setpos(-65 + (- 80 * i), -10)
            t.write(words[i], False, "center", style)
            t.setpos(-65 + (- 80 * i), 10)
            t.write(words[i + 1], False, "center", style)
        elif emotion == 'Like':
            t.setpos(0, 50 + (80 * i))
            t.write(words[i], False, "center", style)
            t.setpos(0, 70 + (80 * i))
            t.write(words[i + 1], False, "center", style)
        elif emotion == "Joy/Happiness":
            t.setpos(65 + (80 * i), -10)
            t.write(words[i], False, "center", style)
            t.setpos(65 + (80 * i), 10)
            t.write(words[i + 1], False, "center", style)
        t.home()
        t.pd()


# These might need to be edited later if the edits in the above
# Land the arrow in an uneven spot.
# Settings includes angle & color for the respective petal
settings = {
    'Joy/Happiness': {'angle': 0, 'colors': ['#E0EC5F', '#E3EC84', '#E6ECAC'], 'words': ['blank', 'blank1', 'blank', 'blank1', 'blank', 'blank1']},
    'Like': {'angle': 90, 'colors': ['#79EC5F', '#9FEB8E', '#BCEDB1'], 'words': ['blank', 'blank1', 'blank', 'blank1', 'blank', 'blank1']},
    'Anticipation/Hope': {'angle': 180, 'colors': ['#5FECE9', '#89ECEA', '#B5EBEA'], 'words': ['blank', 'blank1', 'blank', 'blank1', 'blank', 'blank1']}
}


main()
# Uses the angles above to create three pedals
for emotion, setting in settings.items():
    angle = setting['angle']
    colors = setting['colors']
    words = setting['words']
    pedal(angle, colors, emotion, words)


# End
turtle.done()
