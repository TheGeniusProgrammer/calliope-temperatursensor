Temperatur = 0

def on_forever():
    global Temperatur
    Temperatur = input.temperature()
basic.forever(on_forever)

def on_forever2():
    basic.show_string("" + str(Temperatur) + "C")
basic.forever(on_forever2)