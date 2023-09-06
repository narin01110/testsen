let water = 0
basic.forever(function () {
    water = pins.analogReadPin(AnalogPin.P1)
    serial.writeValue("x", water)
})
