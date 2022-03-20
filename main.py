
def on_button_pressed_a():
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("1", 0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("2", 0, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    I2C_LCD1602.lcd_init(39)
    I2C_LCD1602.on()
    I2C_LCD1602.backlight_on()
basic.forever(on_forever)
