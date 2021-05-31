from language.Language import Language

dict_text = {
    'main_title': 'Agar Skin Maker',
    'adding_a_border_text': '添加边框',
    'cut_to_square_text': '裁剪成正方形',
    'gradient_transparency': '渐变透明'
}


class Chinese(Language):
    def __init__(self):
        super().__init__(dict_text)
