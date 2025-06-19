from hilbertlib.colors.rgbmixer import RGBMixer

mixer = RGBMixer((255, 255, 255), (255, 0, 0))  # red, blue, green

print("Mix by CMY:", mixer.mix_cmy())        # mixing using CMY
print("Mix by RGB avg:", mixer.mix_rgb_average())  # mixing by averaging RGB

mixer.add_color((128, 128, 0))  # add olive-ish color
print("Colors now:", mixer.get_colors())
