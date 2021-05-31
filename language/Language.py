class Language:
    def __init__(self, dict_text):
        self.main_title = dict_text['main_title']
        self.adding_a_border_text = dict_text['adding_a_border_text']
        self.cut_to_square_text = dict_text['cut_to_square_text']
        self.gradient_transparency_text = dict_text['gradient_transparency']

    def get_main_title(self):
        return self.main_title

    def get_adding_a_border_text(self):
        return self.adding_a_border_text

    def get_cut_to_square_text(self):
        return self.cut_to_square_text

    def get_gradient_transparency(self):
        return self.gradient_transparency_text
