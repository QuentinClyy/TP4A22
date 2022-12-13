import interface.texture_loader as tl
import tkinter as tk
import tkinter.font as font


class Menu(tk.Frame):

    def __init__(self, master, width, height):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        self.textures = tl.MenuTextureLoader(self.width, self.height)

        self.nb_players_canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.nb_dice_canvas = tk.Canvas(self.master, width=self.width, height=self.height)

    def bg_init(self, canvas):
        canvas.create_image(0, 0, image=self.textures.menu_bg, anchor="nw")
        canvas.create_image(0, 0, image=self.textures.menu_left_char, anchor="nw")
        canvas.create_image(0, 0, image=self.textures.menu_right_char, anchor="nw")
        canvas.create_image(0, 0, image=self.textures.menu_title, anchor="nw")

    def create_menu_button(self, text, width, height, textures):
        created_button = tk.Button(self.master,
                                   height=int(height / 5),
                                   width=int(width / 2.4),
                                   borderwidth=0,
                                   bg='#4d330f', activebackground='#4d330f',
                                   fg='#ad2513', activeforeground='#63170d')
        created_button.config(image=textures.button_panel, text=text, compound="center")
        button_font = font.Font(family='Roman', size=50)
        created_button['font'] = button_font
        created_button.pack(padx=10, pady=10)
        return created_button

    def create_back_button(self, text, textures):
        created_button = tk.Button(self.master,
                                   height=50,
                                   width=50,
                                   borderwidth=0,
                                   bg='#4d330f', activebackground='#4d330f',
                                   fg='#ad2513', activeforeground='#63170d')
        created_button.config(image=textures.small_button_panel, text=text, compound="center")
        button_font = font.Font(family='Roman', size=10, weight='bold')
        created_button['font'] = button_font
        created_button.pack(padx=10, pady=10)
        return created_button
