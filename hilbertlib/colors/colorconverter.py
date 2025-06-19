import colorsys

class ColorConverter:
    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError("Invalid HEX format")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb):
        return '#{:02X}{:02X}{:02X}'.format(*rgb)

    @staticmethod
    def rgb_to_cmyk(rgb):
        r, g, b = [x / 255.0 for x in rgb]
        k = 1 - max(r, g, b)
        if k == 1:
            return (0, 0, 0, 100)
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)
        return tuple(round(x * 100) for x in (c, m, y, k))

    @staticmethod
    def cmyk_to_rgb(cmyk):
        c, m, y, k = [x / 100.0 for x in cmyk]
        r = 255 * (1 - c) * (1 - k)
        g = 255 * (1 - m) * (1 - k)
        b = 255 * (1 - y) * (1 - k)
        return tuple(int(round(x)) for x in (r, g, b))

    @staticmethod
    def rgb_to_hsl(rgb):
        r, g, b = [x / 255.0 for x in rgb]
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (round(h * 360), round(s * 100), round(l * 100))

    @staticmethod
    def hsl_to_rgb(hsl):
        h, s, l = [hsl[0] / 360, hsl[1] / 100, hsl[2] / 100]
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return tuple(int(round(x * 255)) for x in (r, g, b))

    @staticmethod
    def rgb_to_hsv(rgb):
        r, g, b = [x / 255.0 for x in rgb]
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        return (round(h * 360), round(s * 100), round(v * 100))

    @staticmethod
    def hsv_to_rgb(hsv):
        h, s, v = [hsv[0] / 360, hsv[1] / 100, hsv[2] / 100]
        r, g, b = colorsys.rgb_to_hsv(h, s, v)
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return tuple(int(round(x * 255)) for x in (r, g, b))

    @staticmethod
    def convert(color, from_type, to_type):
        from_type = from_type.lower()
        to_type = to_type.lower()

        # Step 1: convert to RGB
        if from_type == 'rgb':
            rgb = color
        elif from_type == 'hex':
            rgb = ColorConverter.hex_to_rgb(color)
        elif from_type == 'cmyk':
            rgb = ColorConverter.cmyk_to_rgb(color)
        elif from_type == 'hsl':
            rgb = ColorConverter.hsl_to_rgb(color)
        elif from_type == 'hsv':
            rgb = ColorConverter.hsv_to_rgb(color)
        else:
            raise ValueError(f"Unsupported from_type: {from_type}")

        # Step 2: convert RGB to target format
        if to_type == 'rgb':
            return rgb
        elif to_type == 'hex':
            return ColorConverter.rgb_to_hex(rgb)
        elif to_type == 'cmyk':
            return ColorConverter.rgb_to_cmyk(rgb)
        elif to_type == 'hsl':
            return ColorConverter.rgb_to_hsl(rgb)
        elif to_type == 'hsv':
            return ColorConverter.rgb_to_hsv(rgb)
        else:
            raise ValueError(f"Unsupported to_type: {to_type}")
