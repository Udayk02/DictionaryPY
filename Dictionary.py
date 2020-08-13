from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from PyDictionary import PyDictionary
from googletrans import Translator

root = Tk()
root.title('Dictionary')
root.iconbitmap('G:/C/Py/Dictionary.ico')
root.geometry('560x295')
root.maxsize(560, 295)
root.minsize(560, 295)


def find():
    dictionary = PyDictionary()
    word = enter_text.get(1.0, 'end-1c')
    language = translate.get()

    if word == "":
        messagebox.showerror('Dictionary Error', 'Please Enter the word')

    elif language == 'English to English':
        key_word = StringVar()
        key = ttk.Combobox(root, textvariable=key_word, font=('Century Gothic', 10), width=15, state='readonly')
        key['values'] = [
            'Noun', 'Verb', 'Adjective', 'Adverb',
        ]
        key.current(0)
        key.place(x=350, y=55)

        def find_word():
            try:
                meaning_ = dictionary.meaning(word)
                text_box.insert(END, "; ".join(meaning_[key.get()]))
            except KeyError:
                messagebox.showerror('Dictionary Error', 'Please select valid parts of speech !!')
            except TypeError:
                messagebox.showerror('Dictionary Error', 'Please spell the word correctly !!')

        search1 = Button(root, text='Search', font=('Century Gothic', 10), relief=GROOVE, command=find_word)
        search1.place(x=480, y=19)

        def clear_():
            key.destroy()
            search1.destroy()
            text_box.delete(1.0, END)
            enter_text.delete(1.0, END)

        clear1 = Button(root, text='Clear', font=('Century Gothic', 10), relief=GROOVE, command=clear_)
        clear1.place(x=484, y=52)

    elif language == 'English to Hindi':
        translator = Translator()
        meaning = translator.translate(word, dest='hi')
        text_box.insert(END, meaning.text)

    elif language == 'English to Telugu':
        translator = Translator()
        meaning = translator.translate(word, dest='te')
        text_box.insert(END, meaning.text)


def clear():
    enter_text.delete(1.0, END)
    text_box.delete(1.0, END)


dict_image = ImageTk.PhotoImage(Image.open('Dictionary-icon.png'))
image_label = Label(root, image=dict_image)
image_label.place(x=20, y=80)

enter_word = Label(root, text='Enter word: ', font=('Century Gothic', 15, 'bold'))
enter_word.place(x=40, y=20)

enter_text = Text(root, width=35, borderwidth=3, height=1)
enter_text.place(x=170, y=22)

search = Button(root, text='Search', font=('Century Gothic', 10), relief=GROOVE, command=find)
search.place(x=480, y=19)

clear = Button(root, text='Clear', font=('Century Gothic', 10), relief=GROOVE, command=clear)
clear.place(x=484, y=52)

lang = StringVar()
translate = ttk.Combobox(root, textvariable=lang, width=20, state='readonly', font=('Century Gothic', 10))
translate['values'] = [
    'English to English',
    'English to Hindi',
    'English to Telugu',
]
translate.current(0)
translate.place(x=170, y=55)

text_box = Text(root, width=50, height=10, borderwidth=5, relief=GROOVE, font=('Comic Sans', 10))
text_box.place(x=170, y=100)

quit_ = Button(root, text='Quit', font=('Century Gothic', 10), relief=GROOVE, command=root.quit)
quit_.place(x=70, y=220)

root.mainloop()
