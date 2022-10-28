radio.onReceivedNumber(function (receivedNumber) {
    music.playTone(392, music.beat(BeatFraction.Whole))
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
})
radio.onReceivedString(function (receivedString) {
    music.playTone(587, music.beat(BeatFraction.Quarter))
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("short")
})
radio.setGroup(69)
