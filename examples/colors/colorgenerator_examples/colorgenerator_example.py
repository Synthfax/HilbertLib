from hilbertlib.colors.colorgenerator import RandomColorGenerator

gen = RandomColorGenerator()

print("RGB:", gen.generate_rgb())
print("HEX:", gen.generate_hex())
print("CMYK:", gen.generate_cmyk())
print("HSV:", gen.generate_hsv())
print("HSL:", gen.generate_hsl())
