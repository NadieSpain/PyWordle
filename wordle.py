import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from pathlib import Path
import random, string, sys, io,webbrowser,string,os,playsound



__VERSION__="1.10.5"
__CREDITOS__=f"Version: {__VERSION__}\nProgramador: NadieSpain\nTester: NadieSpain"

__Actual__="MainScreen"

WORD_LEN = 5
MAX_TRIES = 6

COLOR_INCORRECT="#38383d"
COLOR_BORDER_HIGHLIGHT = "#565758"
COLOR_BLANK = "#121213"
COLOR_INCORRECT = "#3a3a3c"
COLOR_HALF_CORRECT = "#b59f3b"
COLOR_CORRECT = "#538d4e"

BOX_SIZE = 55
PADDING = 3

try:
    BASE_PATH = Path(sys._MEIPASS)
except AttributeError:
    BASE_PATH = Path(".")

INFO_WORDLIST="wordlists/Info.txt"
VALID_WORDS_WORDLIST = BASE_PATH / "wordlists/Spanish.txt"
ANSWERS_WORDLIST = BASE_PATH / "wordlists/SpanishAnswers.txt"



APP_ICON = BASE_PATH / "assets/wordle_logo_32x32.png"
BACKSPACE_ICON = BASE_PATH / "assets/backspace.png"
HELP_ICON = BASE_PATH / "assets/help.png"
SETTINGS_ICON = BASE_PATH / "assets/settings.png"
BACK_ICON= BASE_PATH / "assets/back.png"
OPENEYE_ICON= BASE_PATH / "assets/openEye.png"
CLOSEEYE_ICON= BASE_PATH / "assets/closeEye.png"

MARIO_ICON=BASE_PATH / "assets/mario1-1.png"


ANSWERS = set(word.upper() for word in io.open(ANSWERS_WORDLIST).read().splitlines())


ALL_WORDS = (
    set(word.upper() for word in io.open(VALID_WORDS_WORDLIST).read().splitlines())
    | ANSWERS
)
Info=["Wordle es un juego sencillo se trata de averiguar la palabra secreta de 5 letras y tendrás 6 intentos para ello.","Si el recuadro es amarillo está pero no en su sitio, si esta verde está en su sitio y si es gris no está.","A diferencia del wordle en web aquí puedes jugar sin límite."]

__secretWord__=""

def check_word(word):
    Wlen=len(word)
    InList=word not in ALL_WORDS
    Bool=(True if Wlen==5 and InList else False)

    T=(Bool, Wlen, InList)
    return T


def new_game(menu):
    P.new_game(menu)



class HelpScreen(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.controller = controller
        #X_button
        self.im=tk.PhotoImage(file=BACK_ICON)
        self.backbtn=tk.Button(self, image=self.im,cursor="hand2",
            border=0, bg=COLOR_INCORRECT,
            command= self._close_)
        self.backbtn.grid(row=0, column=10, sticky="E")

        self.title=tk.Label(self, text="Ayuda:",font=("Helvetica bold",16), bg=COLOR_INCORRECT,fg="white")
        self.title.grid(row=0, column=0,)

        self.HowPlB=tk.Button(self, text="¿Como jugar?", fg=COLOR_INCORRECT,border=0,command=self.ComoJugar,cursor="hand2")
        self.HowPlB.grid(row=1,column=0,pady=5,sticky="w")

        self.CredL=tk.Button(self, text="Creditos",fg=COLOR_INCORRECT,border=0,command=self.creditos,cursor="hand2")
        self.CredL.grid(row=2,column=0,pady=5,sticky="w")

    def _close_(self):
        global __Actual__
        self.place_forget()
        __Actual__="MainScreen"

    def ComoJugar(self):
        def Cerrar():
            global __Actual__
            F.place_forget()
            __Actual__="MainScreen"
            
        self.place_forget()
        F=tk.Frame(self.master, bg=COLOR_INCORRECT, highlightthickness=2)
        F.place(relx=0.5, rely=0.5, anchor="center")
        title=tk.Label(F, text="COMO JUGAR:", bg=COLOR_INCORRECT,fg="white")
        title.grid(row=0, column=0)
        Final=0
        for i in range(len(Info)): 
            HelpL=tk.Label(F, text=Info[i], bg=COLOR_INCORRECT,fg="white")       
            HelpL.grid(row=i+1,column=0, columnspan=10, sticky="w")
            Final=i+1

        button=tk.Button(F,text="Cerrar",command=Cerrar,bg="tomato",
                font=("Helvetica Neue", 12),fg="white", border=0,cursor="hand2")
        button.grid(row=Final+1, column=0,columnspan=10,sticky="ew")



    def creditos(self):
        def Cerrar():
            global __Actual__
            F.place_forget()
            __Actual__="MainScreen"
            
        self.place_forget()
        F=tk.Frame(self.master, bg=COLOR_INCORRECT, highlightthickness=2)
        F.place(relx=0.5, rely=0.5, anchor="center")
        ll=tk.Label(F,text=f"Creditos:\n{__CREDITOS__}",bg=COLOR_INCORRECT,fg="white",justify="left")
        ll.grid(row=0, column=0, columnspan=3)
        button=tk.Button(F,text="Cerrar",command=Cerrar,bg="tomato",
                font=("Helvetica Neue", 12),fg="white", border=0,cursor="hand2")
        button.grid(row=1, column=0,columnspan=3,ipadx=100)
        




class SettingsScreen(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master=master
        self.controller = controller

        self.im=tk.PhotoImage(file=BACK_ICON)
        self.backbtn=tk.Button(self, image=self.im,cursor="hand2",
            border=0, bg=COLOR_INCORRECT,
            command= self._close_)
        self.backbtn.grid(row=0, column=10, sticky="E")

        self.title=tk.Label(self, text="AJUSTES:", bg=COLOR_INCORRECT,fg="white")
        self.title.grid(row=0, column=0,)

        self.NewGamebtn=tk.Button(self, text="Nueva Partida",command=self.new_gamebtn
            ,bg="#e1e1e1",
            fg=COLOR_INCORRECT,border=0, cursor="hand2")
        self.NewGamebtn.grid(row=1, column=0,columnspan=3,pady=5)


    def _close_(self):
        global __Actual__
        self.place_forget()
        __Actual__="MainScreen"

    def chooseMenu(self):
        F=chooseScreen(self.master,self.controller,bg=COLOR_INCORRECT)
        F.place(relx=0.5,rely=0.5,anchor="center")

        
    def new_gamebtn(self):
        self.place_forget()
        F=chooseScreen(self.master,self.controller,bg=COLOR_INCORRECT,highlightthickness=2)
        F.place(relx=0.5,rely=0.5,anchor="center")

        

    

        
class chooseScreen(tk.Frame):
    def __init__(self,master,controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master=master
        self.controller = controller

        self.ll=tk.Label(self,text="La palabra era: "+__secretWord__,bg=COLOR_BLANK,fg="white",font=("Helvetica Neue", 24))
        self.ll.grid(row=0, column=0, columnspan=3,ipadx=20)

        ttk.Separator(self).grid(sticky="ew",columnspan=3)
        self.top_separator = tk.Frame(self, bg=COLOR_INCORRECT, height=45)
        self.top_separator.grid_rowconfigure(1, weight=10)
        self.top_separator.grid_columnconfigure(0, weight=10)
        self.top_separator.grid_propagate(False)
        self.top_separator.grid(sticky="news")

        self.Title=tk.Label(self,text="Elige el modo de juego:",bg=COLOR_INCORRECT,fg="white",font=("Helvetica Neue", 22))
        self.Title.grid(row=2,column=0,columnspan=3)           

        for col in (0,2):
            btn_text = "Partida rápida" if col == 0 else "Elige la palabra"
            func = ( self.normalGame if col == 0 else self.chooseGame )
            bg = "#3b4b66" 
            

            btn=tk.Button(self, text=btn_text,border=0,bg=COLOR_INCORRECT,fg="white",
                font=("Helvetica Neue", 18), command=func)


            btn.bind("<Enter>", lambda e, btn=btn, bg=bg: btn.config(bg=bg))
            btn.bind("<Leave>", lambda e, btn=btn: btn.config(bg=COLOR_INCORRECT))

            btn.grid(row=3, column=col, sticky="ew",)

    def normalGame(self):
        global __Actual__

        new_game(False)
        __Actual__="MainScreen"
        self.place_forget()
        self.controller.frames["MainScreen"].focus_set()

    def chooseGame(self):
        def Aceptar(event=None):
            global __secretWord__, __Actual__
            w=E.get().upper()

            if len(w)==5:
                for i in w: 
                    if i not in string.ascii_uppercase:
                        E.config(fg="red")
                        return

                    
                __secretWord__=w
                new_game(True)

                __Actual__="MainScreen"
                F.place_forget()
                self.controller.frames["MainScreen"].focus_set()

        def Cancelar(event=None):
            global __Actual__
            __Actual__="MainScreen"

            self.controller.frames["MainScreen"].toast("Se cambio la palabra secreta")
            new_game(False)
            F.place_forget()
            self.controller.frames["MainScreen"].focus_set()

        def check_word(event=None):
            w=St.get().upper()

            if len(event.keysym)==1:
                w=w+event.keysym.upper()
            elif event.keysym=="BackSpace":
                w=w[0:-1]

            

            if len(w) ==5:
                l.config(text="Correcta")
                E.config(fg=COLOR_CORRECT)
                

            else:
                if len(w)>5:
                    l.config(text="La palabra es demasiado larga")
                    E.config(fg="red")
                    
                elif len(w)<5:
                    l.config(text="La palabra es demasiado corta")
                    E.config(fg="red")

            for i in w: 
                if i not in string.ascii_uppercase:
                    l.config(text="Caracter invalido")
                    E.config(fg="red")

        def showPassOrNot():
            if E["show"]=="":
                E.config(show="*")
                B.config(image=icons["O"])
            else:
                E.config(show="")
                B.config(image=icons["/"])

        icons={
        "/":tk.PhotoImage(file=CLOSEEYE_ICON),
        "O":tk.PhotoImage(file=OPENEYE_ICON)
        }

        self.place_forget()

        F=tk.Frame(self.master,highlightthickness=1,bg=COLOR_INCORRECT)
        F.place(relx=0.5,rely=0.5,anchor="center")
        Title=tk.Label(F,text="Elige una palabra de 5 letras:",bg=COLOR_INCORRECT,fg="white",font=("Helvetica Neue",24))
        Title.grid(row=0,column=0,columnspan=2)

        St=tk.StringVar()
        E=tk.Entry(F, textvariable=St, show="*",font=("Helvetica Neue",20))
        E.bind("<Key>",check_word)
        E.bind("<Return>",Aceptar)
        E.grid(row=1,column=0,columnspan=3,sticky="w", padx=25)

        B=tk.Button(F,image=icons["O"],bg=COLOR_INCORRECT,fg="white", command=showPassOrNot)
        B.grid(row=1, column=1,sticky="e" )


        l=tk.Label(F,text=" ",fg="white",bg=COLOR_INCORRECT,font=("Helvetica Neue ",20))
        l.grid(row=2,column=0,columnspan=2,sticky="we")



        for col in (0,1):
            btn_text = "Cancelar" if col == 0 else "Aceptar"
            func = ( Cancelar if col == 0 else Aceptar )
            bg = "tomato" if col == 0 else COLOR_CORRECT
                        

            btn=tk.Button(F, text=btn_text,border=0,bg=bg,fg="white",
                font=("Helvetica Neue", 10), command=func)

            btn.grid(row=3, column=col, sticky="ew",)


class MainScreen(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master=master
        self.controller = controller

        self.bind("<Return>", self.check_word)
        self.bind("<BackSpace>", self.remove_letter)
        self.bind("<Key>", self.enter_letter)

        self.init_ui()
        self.new_game(False)

    def new_game(self,menu):
        global __secretWord__
        if not menu:
            __secretWord__ = random.choice(list(ANSWERS)).upper()
        self.words = [""] * 6
        self.correct_letters = set()
        self.half_correct_letter = set()
        self.incorrect_letters = set()

        # reset the grid and keyboard
        for i in range(MAX_TRIES):
            self.current_word = i
            self.update_labels()
        self.current_word = 0
        self.update_keyboard()

        # hide the game over dialog
        self.game_over_dialog.place_forget()
        
    def congratulate(self):
        praises = ["El 1º de la clase","Genio", "Magnífico", "Espléndido", "Muy bien", "No esta mal"]
        self.game_over_dialog_title.set("¡"+praises[(self.current_word-1)] + "!")
        self.game_over_dialog_message.set("¿Quieres jugar otra partida?")
        self.game_over_dialog.place(relx=0.5, rely=0.5, anchor="center")

    def humiliate(self):
        self.game_over_dialog_title.set("¡Más suerte la próxima vez!")
        self.game_over_dialog_message.set(
            "¿Una más?\nLa respuesta era: "+__secretWord__
        )
        self.game_over_dialog.place(relx=0.5, rely=0.5, anchor="center")

    def init_ui(self):

        self.icons = {
            "settings": tk.PhotoImage(file=SETTINGS_ICON),
            "help": tk.PhotoImage(file=HELP_ICON),
            "backspace": tk.PhotoImage(file=BACKSPACE_ICON),
            "MARIO": tk.PhotoImage(file=MARIO_ICON)
        }

        # ==> top bar ==>
        container = tk.Frame(self, bg=COLOR_BLANK, height=40)
        container.grid(sticky="we")
        container.grid_columnconfigure(1, weight=1)

        # help button
        self.helpButton=tk.Button(
            container,
            image=self.icons["help"],
            bg=COLOR_BLANK,
            border=0,
            cursor="hand2",
            command=lambda: self.controller.show_frame("HelpScreen"),
        ).grid(row=0, column=0)

        # Title
        self.Title=tk.Button(
            container,
            text="WORDLE",
            fg="#d7dadc",
            bg=COLOR_BLANK,
            font=("Helvetica Neue", 28, "bold"),
            border=0,
            cursor="hand2",
            command=lambda: self.Title.config(text=self.Title.config(text="⅀ℕ")) if self.Title["text"]=="WORDLE" else self.Title.config(text="WORDLE"),
        )
        self.Title.grid(row=0, column=1)

        # settings button
        tk.Button(
            container,
            image=self.icons["settings"],
            bg=COLOR_BLANK,
            border=0,
            cursor="hand2",
            command=lambda: self.controller.show_frame("SettingsScreen"),
        ).grid(row=0, column=2)
        # <== top bar <==

        # top separator
        ttk.Separator(self).grid(sticky="ew")
        self.top_separator = tk.Frame(self, bg=COLOR_BLANK, height=45)
        self.top_separator.grid_rowconfigure(0, weight=1)
        self.top_separator.grid_columnconfigure(0, weight=1)
        self.top_separator.grid_propagate(False)
        self.top_separator.grid(sticky="news")

        # ==> main game grid ==>
        # if there is extra space then give it to main game grid
        self.rowconfigure(3, weight=1)

        container = tk.Frame(self, bg=COLOR_BLANK)
        container.grid()

        self.labels = []
        for i in range(MAX_TRIES):
            row = []
            for j in range(WORD_LEN):
                cell = tk.Frame(
                    container,
                    width=BOX_SIZE,
                    height=BOX_SIZE,
                    highlightthickness=1,
                    highlightbackground=COLOR_INCORRECT,
                )
                cell.grid_propagate(0)
                cell.grid_rowconfigure(0, weight=1)
                cell.grid_columnconfigure(0, weight=1)
                cell.grid(row=i, column=j, padx=PADDING, pady=PADDING)
                t = tk.Label(
                    cell,
                    text="",
                    justify="center",
                    font=("Helvetica Neue", 24, "bold"),
                    bg=COLOR_BLANK,
                    fg="#d7dadc",
                    highlightthickness=1,
                    highlightbackground=COLOR_BLANK,
                )
                t.grid(sticky="nswe")
                row.append(t)
            self.labels.append(row)
        # <== main game grid <==

        # bottom empty separator
        tk.Frame(self, bg=COLOR_BLANK, height=45).grid()

        # ==> virtual keyboard ==>
        container = tk.Frame(self, bg=COLOR_BLANK)
        container.grid()

        # add all the alphabets
        self.keyboard_buttons = {}
        for i, keys in enumerate(["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]):
            row = tk.Frame(container, bg=COLOR_BLANK)
            row.grid(row=i, column=0)

            for j, c in enumerate(keys):
                if i == 2:  # leave one column for the ENTER button in the last row
                    j += 1

                cell = tk.Frame(
                    row,
                    width=40,
                    height=55,
                    highlightthickness=1,
                    highlightbackground=COLOR_INCORRECT,
                )
                cell.grid_propagate(0)
                cell.grid_rowconfigure(0, weight=1)
                cell.grid_columnconfigure(0, weight=1)
                cell.grid(row=0, column=j, padx=PADDING, pady=PADDING)
                btn = tk.Button(
                    cell,
                    text=c,
                    justify="center",
                    font=("Helvetica Neue", 13),
                    bg=COLOR_BLANK,
                    fg="#d7dadc",
                    cursor="hand2",
                    border=0,
                    command=lambda c=c: self.enter_letter(key=c),
                )
                btn.grid(sticky="nswe")
                self.keyboard_buttons[c] = btn

        for col in (0, 8):
            text = "ENTER" if col == 0 else ""
            func = self.check_word if col == 0 else self.remove_letter
            cell = tk.Frame(
                row,
                width=75,
                height=55,
                highlightthickness=1,
                highlightbackground=COLOR_INCORRECT,
            )
            cell.grid_propagate(0)
            cell.grid_rowconfigure(0, weight=1)
            cell.grid_columnconfigure(0, weight=1)
            cell.grid(row=0, column=col, padx=PADDING, pady=PADDING)
            btn = tk.Button(
                cell,
                text=text,
                justify="center",
                font=("Helvetica Neue", 13),
                bg=COLOR_BLANK,
                fg="#d7dadc",
                cursor="hand2",
                border=0,
                command=func,
            )
            btn.grid(row=0, column=0, sticky="nswe",)

        # set the image for delete button
        btn.configure(image=self.icons["backspace"])
        # <== virtual keyboard <==

        # ==> game over dialog ==>
        # create game over dialog but dont place it yet
        self.game_over_dialog = tk.Frame(self, bg=COLOR_INCORRECT, highlightthickness=2)

        # title text
        self.game_over_dialog_title = tk.StringVar()
        tk.Label(
            self.game_over_dialog,
            textvariable=self.game_over_dialog_title,
            font=("Helvetica Neue", 22),
            bg=COLOR_INCORRECT,
            fg="white",
        ).grid(sticky="news", padx=10, pady=10)

        # message body
        self.game_over_dialog_message = tk.StringVar()
        tk.Label(
            self.game_over_dialog,
            textvariable=self.game_over_dialog_message,
            font=("Arial", 16),
            bg=COLOR_INCORRECT,
            fg="white",
        ).grid(sticky="news", padx=10, pady=10)

        # yes/no buttons
        self.game_over_dialog.grid_rowconfigure(4, weight=1)
        f = tk.Frame(self.game_over_dialog, bg=COLOR_INCORRECT)
        f.grid(sticky="news")
        f.grid_columnconfigure(0, weight=1)
        f.grid_columnconfigure(2, weight=1)
        for col in (0, 2):
            btn_text = "Sí" if col == 0 else "No"
            func = (lambda: self.new_game(False)) if col == 0 else self.controller.destroy
            bg = "#4caf50" if col == 0 else "tomato"
            btn = tk.Button(
                f,
                text=btn_text,
                bg=COLOR_INCORRECT,
                fg="white",
                font=("Helvetica Neue", 13),
                border=0,
                cursor="hand2",
                command=func,
            )
            btn.bind("<Enter>", lambda e, btn=btn, bg=bg: btn.config(bg=bg))
            btn.bind("<Leave>", lambda e, btn=btn: btn.config(bg=COLOR_INCORRECT))
            btn.grid(row=1, column=col, sticky="ew")

        # <== game over dialog <==
        Frame_init=tk.Frame(self)
        Frame_init.place(relx=0.5, rely=0.5, anchor="center")
        

    def toast(self, message, duration=2):
        """show a toast message which will disappear after {duration} seconds"""
        t = tk.Label(self, text=message, font=("Helvetica Neue", 16))
        t.grid(row=2, column=0, sticky="news", padx=5, pady=5)
        self.master.after(int(duration * 1000), lambda: t.grid_remove())

    def update_keyboard(self):
        for key, btn in self.keyboard_buttons.items():
            if key in self.correct_letters:
                btn["bg"] = COLOR_CORRECT
            elif key in self.half_correct_letter:
                btn["bg"] = COLOR_HALF_CORRECT
            elif key in self.incorrect_letters:
                btn["bg"] = COLOR_INCORRECT
            else:
                btn["bg"] = COLOR_BLANK

    def update_labels(self, colors=None):
        word = self.words[self.current_word]
        for i, label in enumerate(self.labels[self.current_word]):
            try:
                letter = word[i]
            except IndexError:
                letter = ""

            label["text"] = letter
            if colors:
                label["bg"] = colors[i]
                label["highlightbackground"] = colors[i]
            else:
                label["bg"] = COLOR_BLANK
                label["highlightbackground"] = (
                    COLOR_BORDER_HIGHLIGHT if letter else COLOR_BLANK
                )

    def check_word(self, event=None):
        print("checking word:", self.words[self.current_word])
        word = self.words[self.current_word]
        if len(word) < WORD_LEN:
            self.toast("No hay suficientes letras")
            return

        if word not in ALL_WORDS and word!=__secretWord__:
            if word=="NEVER":
                self.toast("No esta en la lista de palabras")
                webbrowser.open_new_tab("http://news.rr.nihalnavath.com/posts/Techno-never-dies--26c9e039")
                self.master.after(5000, lambda: self.toast("RickRolled!",5))
                
                
            elif word=="MARIO":
                t = tk.Label(self, image=self.icons["MARIO"],)
                t.place(relx=0.5,y=100,anchor="center")
                self.master.after(2000, lambda: t.place_forget())
                playsound.playsound("MusicMario.wav")  


            else:
                self.toast("No esta en la lista de palabras")
            return


        nums=range(5)
        colors = ["","","","",""]
        freq = {c: __secretWord__.count(c) for c in __secretWord__}
        for x, y, i in zip(word, __secretWord__,nums):
            if x == y:
                colors[i]=COLOR_CORRECT
                self.correct_letters.add(x)
                freq[x] -= 1

        for x, y, i in zip(word, __secretWord__,nums):
            if x in __secretWord__ and freq[x]>0 and colors[i]=="":
                colors[i]=COLOR_HALF_CORRECT
                self.half_correct_letter.add(x)
                freq[x] -= 1
            elif colors[i]=="":
                self.incorrect_letters.add(x)
                colors[i]=COLOR_INCORRECT


        self.update_labels(colors)
        self.update_keyboard()

        self.current_word += 1
        if word == __secretWord__:
            self.congratulate()
        elif self.current_word >= MAX_TRIES:
            self.humiliate()

    def remove_letter(self, event=None):
        if self.words[self.current_word] and __Actual__=="MainScreen":
            print(self.words[self.current_word][-1], "was deleted.")
            self.words[self.current_word] = self.words[self.current_word][:-1]
            self.update_labels()

    def enter_letter(self, event=None, key=None):
        key = key or event.keysym.upper()
        if key in string.ascii_uppercase and __Actual__=="MainScreen":
            print(key, "was entered.")
            self.words[self.current_word] += key
            # prevent user from enterering excess letters
            self.words[self.current_word] = self.words[self.current_word][:WORD_LEN]
            self.update_labels()


class WordleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Wordle - A Word Game")
        self.state("zoomed")
        # self.resizable(False, False)
        self.app_icon=tk.PhotoImage(file=APP_ICON)
        self.iconphoto(False, self.app_icon)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, bg=COLOR_BLANK)
        container.grid(sticky="news")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["MainScreen"] = MainScreen(
            master=container, controller=self, bg=COLOR_BLANK
        )
        self.frames["SettingsScreen"] = SettingsScreen(master=container, controller=self,
        bg=COLOR_INCORRECT, border=5, highlightthickness=2
        )
        self.frames["HelpScreen"] = HelpScreen(master=container, controller=self,
        bg=COLOR_INCORRECT, border=5, highlightthickness=2
        )

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        self.frames["MainScreen"].grid(row=0, column=0, sticky="ns")
        self.frames["MainScreen"].focus_set()
        self.frames["SettingsScreen"]
        self.frames["HelpScreen"]


        self.fullscreen = False
        self.bind("<F11>", self.fullscreen_toggle)
    def on_closing(self):
        global __Actual__
        if __Actual__=="MainScreen":
            __Actual__="Close_menu"
            def cerrar():
                btn1.grid_forget()
                btn.grid_forget()
                ll.config(text="La palabra era: "+__secretWord__,font=("Helvetica Neue", 14))
                button=tk.Button(F,text="aceptar",command=lambda: self.destroy(),bg=COLOR_CORRECT,
                    font=("Helvetica Neue", 12),fg="white", border=0,cursor="hand2")
                button.grid(row=1, column=0,columnspan=3,ipadx=100)

            def continuar():
                global __Actual__
                __Actual__="MainScreen"
                F.place_forget()
                self.frames["MainScreen"].focus_set()
                

            F=tk.Frame(self, bg=COLOR_INCORRECT, highlightthickness=2)
            F.place(relx=0.5, rely=0.5, anchor="center")
            ll=tk.Label(F,text="¿Quieres cerrar Wordle?",bg=COLOR_INCORRECT,fg="white",font=("Helvetica Neue", 14))
            ll.grid(row=0, column=0, columnspan=3)
            for col in (0, 2):
                btn_text = "Aceptar" if col == 0 else "Cancelar"
                func = cerrar if col == 0 else continuar
                bg = "#4caf50" if col == 0 else "tomato"
                btn = tk.Button(
                    F,
                    text=btn_text,
                    bg=COLOR_INCORRECT,
                    fg="white",
                    font=("Helvetica Neue", 13),
                    border=0,
                    cursor="hand2",
                    command=func,
                )
                btn.bind("<Enter>", lambda e, btn=btn, bg=bg: btn.config(bg=bg))
                btn.bind("<Leave>", lambda e, btn=btn: btn.config(bg=COLOR_INCORRECT))
                btn.grid(row=1, column=col, sticky="ew", ipadx=5)
                if col==0: 
                    btn1=btn
        else: 
            self.frames["MainScreen"].toast("Cierra los dialogos pendientes")


    def new_game(self,menu):
        self.frames["MainScreen"].new_game(menu)
   
    def show_frame(self, page_name):
        global __Actual__
        frame = self.frames[page_name]
        if page_name!="MainScreen" and __Actual__!="Close_menu":
            if page_name=="SettingsScreen" and __Actual__!="HelpScreen":
                frame.place(relx=0.5, rely=0.5, anchor="center")
                __Actual__=page_name
            elif page_name=="HelpScreen" and __Actual__!="SettingsScreen":
                frame.place(relx=0.5, rely=0.5, anchor="center")
                __Actual__=page_name
        elif page_name=="MainScreen" and __Actual__!="Close_menu":
            __Actual__=page_name

    def fullscreen_toggle(self, event=None):
        """Toggle fullscreen mode"""
        if self.fullscreen:
            self.wm_attributes("-fullscreen", False)
            self.fullscreen = False
        else:
            self.wm_attributes("-fullscreen", True)
            self.fullscreen = True


if __name__ == "__main__":
    P=WordleApp()
    P.mainloop()

