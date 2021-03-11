from micropython import const
from adafruit_is31fl3731 import keybow2040
import board

from .. import rgb


class RGB(rgb.RGB):
    def setup(self):
        self.pin_data = self.pixel_pin[0]
        self.pin_clock = self.pixel_pin[1]

        self.i2c = board.I2C() # self.pin_data, self.pin_clock)
        self.display = keybow2040.Keybow2040(self.i2c)
        self.num_pixels = 16

    def _to_dict(self):
        # TODO what's `dict(RGB instance)` used for?
        # do we care that it leaks a "neopixel" value enough to overload it?
        return {
            'hue': self.hue,
            'sat': self.sat,
            'val': self.val,
            'time': self.time,
            'intervals': self.intervals,
            'animation_mode': self.animation_mode,
            'animation_speed': self.animation_speed,
            'enabled': self.enabled,
            'disable_auto_write': self.disable_auto_write,
        }

    def show(self):
        '''
        Does nothing. LEDs display when changed.
        '''
        return self

    def set_rgb(self, rgb, index):
        '''
        Takes an RGB or RGBW and displays it on a single LED
        :param rgb: RGB or RGBW
        :param index: Index of LED/Pixel
        '''
        if 0 <= index <= self.num_pixels - 1:
            x = index % 4
            y = index // 4
            r, g, b = rgb[0:3]
            self.display.pixelrgb(x, y, r, g, b)

        return self

    def set_rgb_fill(self, rgb):
        '''
        Takes an RGB or RGBW and displays it on all LEDs
        :param rgb: RGB or RGBW
        '''
        r, g, b = rgb[0:3]

        for index in range(self.num_pixels):
            x = index % 4
            y = index // 4
            self.display.pixelrgb(x, y, r, g, b)

        return self
