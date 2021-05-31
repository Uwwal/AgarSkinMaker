from tkinter import Tk, ttk

from language.Chinese import Chinese
from language.English import English

from Main import Main

TITLE = 'starter'
SELECT_TEXT = 'Please select a language.'

ChineseText = '简体中文'
EnglishText = 'English'


class Starter:
    def __init__(self, root):
        root.title(TITLE)

        self.language = None

        content = ttk.Frame(root)

        text = ttk.Label(content, text=SELECT_TEXT)
        button_chinese = ttk.Button(content,
                                    text=ChineseText,
                                    command=lambda: self.click_button(ChineseText))
        button_english = ttk.Button(content,
                                    text=EnglishText,
                                    command=lambda: self.click_button(EnglishText))

        content.grid(column=0, row=0)
        text.grid(column=0, row=1)
        button_chinese.grid(column=0, row=2)
        button_english.grid(column=0, row=3)

    def click_button(self, language_id):
        self.get_language(language_id)

        global starter, main
        starter.destroy()

        main = Tk()
        Main(main, self.language)
        main.mainloop()

    def get_language(self, language_id):
        if language_id == ChineseText:
            self.language = Chinese()
        if language_id == EnglishText:
            self.language = English()


main = None

starter = Tk()
Starter(starter)
starter.mainloop()
