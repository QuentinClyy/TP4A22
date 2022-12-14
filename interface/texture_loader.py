from PIL import Image, ImageTk


class GameTextureLoader:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.arene_bg = resize_image("arena.png", self.width, self.height)
        self.canvas_arene_bg = resize_image("arena_bg.png", self.width, self.height)
        self.arene_tile = resize_image("tile.png", self.width // 32, self.height // 18)
        self.arene_tile_dark = resize_image("tile_dark.png", self.width // 32, self.height // 18)
        self.de_1 = resize_image("DeX.png", self.width // 32, self.height // 13)
        self.de_2 = resize_image("De2.png", self.width // 32, self.height // 13)
        self.de_3 = resize_image("De3.png", self.width // 32, self.height // 13)
        self.de_4 = resize_image("De4.png", self.width // 32, self.height // 13)
        self.de_5 = resize_image("De5.png", self.width // 32, self.height // 13)
        self.de_6 = resize_image("De6.png", self.width // 32, self.height // 13)
        self.button_panel = resize_image("Panel.png", int(self.width / 7.2), int(self.height / 15))
        self.tableau_panel = resize_image("menu_panel.png", int(self.width // 9.7),
                                          int(self.width // 8))

    def resize_arena_objects(self, dimension_arene):
        width_factor = dimension_arene * 4.57
        height_factor_de = dimension_arene * 1.88
        height_factor_tile = dimension_arene * 2.57

        self.arene_tile = resize_image("tile.png", self.width // width_factor,
                                       self.height // height_factor_tile)
        self.arene_tile_dark = resize_image("tile_dark.png", self.width // width_factor,
                                            self.height // height_factor_tile)
        self.de_1 = resize_image("DeX.png", self.width // width_factor, self.height // height_factor_de)
        self.de_2 = resize_image("De2.png", self.width // width_factor, self.height // height_factor_de)
        self.de_3 = resize_image("De3.png", self.width // width_factor, self.height // height_factor_de)
        self.de_4 = resize_image("De4.png", self.width // width_factor, self.height // height_factor_de)
        self.de_5 = resize_image("De5.png", self.width // width_factor, self.height // height_factor_de)
        self.de_6 = resize_image("De6.png", self.width // width_factor, self.height // height_factor_de)


class MenuTextureLoader:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.menu_bg = resize_image("background.png", self.width, self.height)
        self.menu_left_char = resize_image("leftWarrior.png", self.width, self.height)
        self.menu_right_char = resize_image("rightWarrior.png", self.width, self.height)
        self.menu_title = resize_image("title.png", self.width, self.height)
        self.menu_panel = resize_image("menu_panel.png", self.width // 3.27,
                                       self.height // 2.73)
        self.button_panel = resize_image("Panel.png", int(self.width // 2.367),
                                         int(self.height // 5))
        self.small_button_panel = resize_image("smallButton.png", self.width // 38.4,
                                               self.height // 21.6)
        self.mid_button_panel = resize_image("Panel.png", int(self.width // (2 * 2.367)),
                                             int(self.height // 5))


def resize_image(img_name, width, height):
    load_img = Image.open(f"./interface/Images/{img_name}")
    res_img = load_img.resize((int(width), int(height)), resample=Image.NEAREST)
    return ImageTk.PhotoImage(res_img)
