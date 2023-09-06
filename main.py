sensor = 0

def on_forever():
    global sensor
    sensor = pins.analog_read_pin(AnalogPin.P0)
    serial.write_value("x", sensor)
basic.forever(on_forever)
