from tkinter import ttk
from tkinter import N, W, E, S

from method.AddingABorder import AddingABorder


class Main:
    def __init__(self, root, language):
        self.language = language

        self.method = None

        root.title(self.language.get_main_title())

        style = ttk.Style()
        style.configure('myname.TFrame', background='blue')
        style.configure('myname1.TFrame', background='blue')

        self.main_frame = ttk.Frame(root, style='myname.TFrame')
        self.method_frame = ttk.Frame(self.main_frame, style='myname1.TFrame')
        self.method_detail_frame = ttk.Frame(self.main_frame)
        self.image_detail_frame = ttk.Frame(self.main_frame)

        image_label = ttk.Label(self.main_frame)

        self.select_method = SelectMethod(language)
        self.select_method_button_list = []
        self.get_select_method_button_list(self.method_frame)

        self.pack_select_method_button()

        self.main_frame.grid(column=0, row=0, sticky=N)
        self.method_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.method_detail_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        self.image_detail_frame.grid(column=0, row=200, sticky=(N, W, E, S))
        image_label.grid(column=1, row=0,sticky=(N, W, E, S))

    def get_select_method_button_list(self, frame):
        for key, value in self.select_method.get_method_name_dict().items():
            self.select_method_button_list.append(
                ttk.Button(frame, text=key, command=lambda: self.click_select_method_button(value))
            )

    def pack_select_method_button(self):
        for index, value in enumerate(self.select_method_button_list):
            value.grid(column=0, row=index)

    def click_select_method_button(self, method):
        self.method = method
        self.method.get_method_detail_weight(self.method_detail_frame)


class SelectMethod:
    def __init__(self, language):
        self.language = language
        self.method_name_dict = {
            language.get_adding_a_border_text(): self.get_adding_a_border(),
            language.get_cut_to_square_text(): self.get_adding_a_border()   # 这里记得要改
        }

    def get_method_name_dict(self):
        return self.method_name_dict

    def get_adding_a_border(self):
        return AddingABorder(self.language)
