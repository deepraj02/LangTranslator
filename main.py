
# & <==========Importing the Modules ============>

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tmsg
from googletrans import Translator


# $ <================== Functions ===================>

#!----------- Main Translator Function ---------------


def translate():
    language1 = t1.get("1.0", "end-1c")
    cl = choose_language.get()

    if language1 == "":
        tmsg.showerror("Translating Error",
                       "Please Make sure that the Box is Filled.")
    else:
        t2.delete(1.0, "end")
        translator = Translator()
        output = translator.translate(language1, dest=cl)
        t2.insert("end", output.text)

    # ^ --------------- Clear Function ---------------


def clear():
    t1.delete(1.0, "end")
    t2.delete(1.0, "end")


# * <================================= UI Body ==================================>

root = Tk()
root.title("Translate IT.")
root.wm_iconbitmap(r"Resources/icon.ico")
root.geometry("560x530")

a = tk.StringVar()
auto_detect = ttk.Combobox(
    root, width=20, textvariable=a, state="readonly", font="FiraCode 13")
auto_detect["values"] = (
    'Auto Detect',
)

auto_detect.place(x=30, y=70)
auto_detect.current(0)

l = tk.StringVar()

choose_language = ttk.Combobox(
    root, width=20, textvariable=a, state="readonly", font="FiraCode 13")
auto_detect["values"] = (
    "Afrikaans", "Albanian", "Arabic", "Armenian", "Azerbaijani",
    "Basque", "Belarusian", "Bengali", "Bosnian", "Bulgarian",
    "Catalan", "Cebuano", "Chichewa", "Chinese", "Corsican",
    "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto",
    "Estonian", "Filipino", "Finnish", "French", "Frisian", "Galician",
    "Georgian", "German", "Greek", "Gujarati", "Haitian Creole", "Hausa",
    "Hawaiian", "Hebrew", "Hindi", "Hmong", "Hungarian", "Icelandic",
    "Igbo", "Indonesian", "Irish", "Italian", "Japanese", "Javanese",
    "Kannada", "Kazakh", "Khmer", "Kinyarwanda", "Korean", "Kurdish",
    "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian", "Luxembourgish",
    "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori",
    "Marathi", "Mongolian", "Myanmar", "Nepali", "Norwegian""Odia",
    "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian",
    "Russian", "Samoan", "Scots Gaelic", "Serbian", "Sesotho", "Shona", "Sindhi",
    "Sinhala", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili",
    "Swedish", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Turkish",
)

choose_language.place(x=290, y=70)
choose_language.current()

t1 = Text(root, width=30, height=10, relief=SUNKEN, font="Consolas 12")
t1.place(x=10, y=100)

t2 = Text(root, width=30, height=10, relief=SUNKEN, font="Consolas 12")
t2.place(x=260, y=100)

trans = Button(root, text="Translate", relief=RIDGE, borderwidth=3,
               font="consolas 13 bold", cursor="hand2", command=translate)
trans.place(x=170, y=320)

clr = Button(root, text="Clear", relief=RIDGE, borderwidth=3,
             font="consolas 13 bold", cursor="hand2", command=clear)
clr.place(x=300, y=320)

root.mainloop()
