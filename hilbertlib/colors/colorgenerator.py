import random
import colorsys

class RandomColorGenerator:
    @staticmethod
    def generate_rgb():
        """Return a random RGB color tuple (0-255)."""
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    @staticmethod
    def generate_hex():
        """Return a random HEX color string like '#A1B2C3'."""
        r, g, b = RandomColorGenerator.generate_rgb()
        return f"#{r:02X}{g:02X}{b:02X}"

    @staticmethod
    def generate_cmyk():
        """Return a random CMYK color tuple (0-100%)."""
        r, g, b = RandomColorGenerator.generate_rgb()
        # Convert RGB 0-255 to 0-1
        r_, g_, b_ = r / 255, g / 255, b / 255

        k = 1 - max(r_, g_, b_)
        if k == 1:
            # Black
            return (0, 0, 0, 100)

        c = (1 - r_ - k) / (1 - k)
        m = (1 - g_ - k) / (1 - k)
        y = (1 - b_ - k) / (1 - k)

        # Convert to percentage
        return (round(c * 100), round(m * 100), round(y * 100), round(k * 100))

    @staticmethod
    def generate_hsv():
        """Return a random HSV tuple (hue 0-360, saturation 0-100%, value 0-100%)."""
        r, g, b = RandomColorGenerator.generate_rgb()
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        return (round(h * 360), round(s * 100), round(v * 100))

    @staticmethod
    def generate_hsl():
        """Return a random HSL tuple (hue 0-360, saturation 0-100%, lightness 0-100%)."""
        r, g, b = RandomColorGenerator.generate_rgb()
        h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        return (round(h * 360), round(s * 100), round(l * 100))
