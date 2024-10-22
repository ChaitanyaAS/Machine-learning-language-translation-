from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator 
from tkinter import messagebox

root = tk.Tk()
root.title('Language translator')
root.geometry('590x370')
framel = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#F7DC6F')
framel.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#F7DC6F').pack(pady=10)


def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to Translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert('end', output.text)


def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')


a = tk.StringVar()

text_entry1 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=('vardan', 15))

auto_select = ttk.Combobox(framel, width=27, textvariable=a, state='readonly', font=('vardan', 10, 'bold'))
auto_select['values'] = (
    'auto select',
)
auto_select.place(x=15, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(framel, width=27, textvariable=l, state='readonly', font=('vardan', 10, 'bold'))
choose_language['values'] = (
    "Kannada", "Hindi", "Chinese (Mandarin)", "Russian", "Arabic", "Portuguese", "Japanese", "Korean", "Bengali",
    "German", "Italian", "Swahili", "Tamil", "Telugu", "Thai", "Turkish", "Urdu", "Vietnamese", "Yoruba",
    "Afrikaans", "Hungarian", "Polish", "Persian (Farsi)", "Ukrainian", "Hebrew", "Malay", "Indonesian", "Dutch",
    "Greek", "French", "Spanish", "English", "Finnish", "Danish", "Norwegian", "Swedish", "Czech", "Slovak",
    "Slovenian", "Croatian", "Bosnian", "Serbian", "Macedonian", "Bulgarian", "Romanian", "Catalan", "Basque",
    "Galician", "Estonian", "Latvian", "Lithuanian", "Irish", "Welsh", "Scottish Gaelic", "Breton"
)
choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1.place(x=10, y=100)

text_entry2 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=('vardan', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(framel, command=translate, text="Translate", relief=RAISED, borderwidth=2, font=('vardan', 10, 'bold'),
              bg='#248aa2', fg="white", cursor="hand2")
btn1.place(x=185, y=300)

btn2 = Button(framel, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=('vardan', 10, 'bold'),
              bg='#248aa2', fg="white", cursor="hand2")
btn2.place(x=300, y=300)

root.mainloop()
