/**
 * https://github.com/makecode-extensions/i2cLCD1602
 */
input.onButtonPressed(Button.A, function () {
    I2C_LCD1602.clear()
    I2C_LCD1602.ShowString("1", 0, 0)
})
input.onButtonPressed(Button.B, function () {
    I2C_LCD1602.clear()
    I2C_LCD1602.ShowString("2", 0, 0)
})
basic.forever(function () {
    I2C_LCD1602.LcdInit(39)
    I2C_LCD1602.on()
    I2C_LCD1602.BacklightOn()
})
