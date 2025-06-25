let Temperatur = 0
basic.forever(function on_forever() {
    basic.showString("" + ("" + Temperatur) + "C")
})
basic.forever(function on_forever2() {
    if (Temperatur < 15) {
        music.playTone(262, music.beat(BeatFraction.Whole))
    } else if (Temperatur > 35) {
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
    
})
basic.forever(function on_forever3() {
    
    Temperatur = input.temperature()
})
