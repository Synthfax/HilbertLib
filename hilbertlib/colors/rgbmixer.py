class RGBMixer:
    def __init__(self, *rgbs):
        """
        Initialize with one or more RGB tuples.
        Example: RGBMixer((255,0,0), (0,255,0), (0,0,255))
        """
        self.colors = [self._validate_rgb(rgb) for rgb in rgbs]

    def _validate_rgb(self, rgb):
        if (not isinstance(rgb, tuple) or len(rgb) != 3 or 
            any(not (0 <= v <= 255) for v in rgb)):
            raise ValueError("Each color must be an RGB tuple with values 0-255")
        return rgb

    @staticmethod
    def rgb_to_cmy(rgb):
        r, g, b = rgb
        return (1 - r/255, 1 - g/255, 1 - b/255)

    @staticmethod
    def cmy_to_rgb(cmy):
        c, m, y = cmy
        return (int(round((1 - c) * 255)),
                int(round((1 - m) * 255)),
                int(round((1 - y) * 255)))

    def mix_cmy(self):
        """
        Mix all colors using CMY model by averaging.
        Returns an RGB tuple.
        """
        c_sum = m_sum = y_sum = 0
        n = len(self.colors)
        for rgb in self.colors:
            c, m, y = self.rgb_to_cmy(rgb)
            c_sum += c
            m_sum += m
            y_sum += y
        avg_cmy = (c_sum / n, m_sum / n, y_sum / n)
        return self.cmy_to_rgb(avg_cmy)

    def mix_rgb_average(self):
        """
        Mix all colors by averaging RGB components directly.
        Returns an RGB tuple.
        """
        r_sum = g_sum = b_sum = 0
        n = len(self.colors)
        for r, g, b in self.colors:
            r_sum += r
            g_sum += g
            b_sum += b
        return (int(round(r_sum / n)),
                int(round(g_sum / n)),
                int(round(b_sum / n)))

    def add_color(self, rgb):
        """Add another color to the mixer."""
        self.colors.append(self._validate_rgb(rgb))

    def clear_colors(self):
        """Clear all colors."""
        self.colors = []

    def get_colors(self):
        """Get current list of colors."""
        return self.colors.copy()