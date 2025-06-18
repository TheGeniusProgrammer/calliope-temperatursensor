let Temperatur = 0
basic.forever(function on_forever() {
    
    Temperatur = input.temperature()
})
basic.forever(function on_forever2() {
    basic.showString("" + ("" + Temperatur) + "C")
})
