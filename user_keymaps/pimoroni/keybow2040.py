import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.leds import keybow2040
from kmk.scanners import gpio
from kmk.matrix import intify_coordinate as ic

from kmk.keys import KC

class KMKKeyboard(_KMKKeyboard):
    rgb_pixel_pin = (board.SDA, board.SCL)
    rgb = keybow2040.RGB
    matrix_scanner = gpio.GPIOScanner([
        board.SW0,
        board.SW1,
        board.SW2,
        board.SW3,
        board.SW4,
        board.SW5,
        board.SW6,
        board.SW7,
        board.SW8,
        board.SW9,
        board.SW10,
        board.SW11,
        board.SW12,
        board.SW13,
        board.SW14,
        board.SW15
    ])

    col_pins = (None,)
    row_pins = (None,) 
    diode_orientation = True

    coord_mapping = [
        ic(0, 0), ic(1, 0), ic(2, 0), ic(3, 0), 
        ic(0, 1), ic(1, 1), ic(2, 1), ic(3, 1), 
        ic(0, 2), ic(1, 2), ic(2, 2), ic(3, 2), 
        ic(0, 3), ic(1, 3), ic(2, 3), ic(3, 3)
    ]

keyboard = KMKKeyboard()

keyboard.debug_enabled = False

keyboard.rgb_config['pixel_pin'] = (board.SDA, board.SCL)
keyboard.rgb_config['num_pixels'] = 16
keyboard.rgb_config['val_limit'] = 100
keyboard.rgb_config['hue_step'] = 1
keyboard.rgb_config['sat_step'] = 5
keyboard.rgb_config['val_step'] = 5
keyboard.rgb_config['hue_default'] = 0
keyboard.rgb_config['sat_default'] = 100
keyboard.rgb_config['val_default'] = 100
keyboard.rgb_config['knight_effect_length'] = 4
keyboard.rgb_config['animation_mode'] = 'static'
keyboard.rgb_config['animation_speed'] = 1

keyboard.keymap = [
    [
        KC.RGB_MODE_RAINBOW, KC.N2, KC.N3, KC.N4,
        KC.A,  KC.B,  KC.C,  KC.D,
        KC.E,  KC.F,  KC.G,  KC.H,
        KC.I,  KC.J,  KC.K,  KC.L
    ]
]

if __name__ == '__main__':
    keyboard.go()