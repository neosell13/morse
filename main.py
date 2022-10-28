def on_received_number(receivedNumber):
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(1)
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    music.play_tone(587, music.beat(BeatFraction.QUARTER))
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("short")
    music.play_tone(587, music.beat(BeatFraction.QUARTER))
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(69)