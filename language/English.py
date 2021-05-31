from language.Language import Language

dict_text = {
    'main_title': 'Agar Skin Maker',
    'adding_a_border_text': 'Adding a border',
    'cut_to_square_text': 'Cut to square',
    'gradient_transparency': 'Gradient transparency'
}


class English(Language):
    def __init__(self):
        super().__init__(dict_text)
