Temperatur = 0

def on_forever():
    basic.show_string("" + str(Temperatur) + "C")
basic.forever(on_forever)

def on_forever2():
    if Temperatur < 15:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    elif Temperatur > 35:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever2)

def on_forever3():
    global Temperatur
    Temperatur = input.temperature()
basic.forever(on_forever3)