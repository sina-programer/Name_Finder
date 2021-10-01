from tkinter import *
from tkinter import messagebox
from datetime import datetime
import webbrowser
import csv
import os

class App:
    def __init__(self, master):
        master.config(menu=self.init_menu(master))
        
        self.lengthVar = IntVar()
        Label(master, text='Word length: ').place(x=130, y=10)
        Spinbox(master, from_=2, to=20, width=3, textvariable=self.lengthVar).place(x=210, y=11)      
        
        self.nth_letterVar = IntVar()
        Label(master, text='Which letter: ').place(x=130, y=40)
        Spinbox(master, from_=1, to=20, width=3, textvariable=self.nth_letterVar).place(x=210, y=41)
        
        self.letterVar = StringVar()
        Label(master, text='What letter: ').place(x=130, y=70)
        Entry(master, width=5, textvariable=self.letterVar).place(x=210, y=71)
        
        self.maleVar = IntVar()
        Checkbutton(master, text='Male', variable=self.maleVar, onvalue=1, offvalue=0).place(x=20, y=10)
        
        self.femaleVar = IntVar()
        Checkbutton(master, text='Female', variable=self.femaleVar, onvalue=1, offvalue=0).place(x=20, y=30)
        
        Button(master, text='Export', width=31, command=self.export).place(x=20, y=100)
                
    def export(self):
        names = self.read_file(names_file)
        character = self.letterVar.get()
        idx = self.nth_letterVar.get()
        isfemale = self.femaleVar.get()
        ismale = self.maleVar.get()
        length = self.lengthVar.get()
        filtered_names = [] 
        
        if character.strip():
            if ismale or isfemale:
                for i in range(len(names)):
                    name = names[i][0]
                    if len(name) == length:
                        if name[idx-1] == character: 
                            if (ismale and names[i][1]
                          ) or (isfemale and names[i][2]):
                                filtered_names.append(name)
                
                code = f'{ismale}{isfemale}{idx}{length}_{ord(character)}'
                file_name = f'Names_{code}.txt'
                self.write_file(file_name, filtered_names)
                
                messagebox.showinfo('Complete', f'Your request saved with code: {code}')
                
            else:
                messagebox.showwarning('ERROR', 'Please select a gender')
                
        else:
            messagebox.showwarning('ERROR', 'Please enter a valid letter for search')

    @staticmethod
    def write_file(file_name, names):
        with open(file_name, 'w', encoding='utf-8') as file:
            for name in names:
                file.write(name+'\n')
        
    @staticmethod
    def read_file(file_name):
        with open(file_name, encoding='utf-8') as file:
            names = list(csv.reader(file))
        
        return names
    
    def show_about(self):
        dialog = Tk()
        dialog.title('About us')
        dialog.iconbitmap(icon)
        dialog.geometry('300x100+550+350')
        dialog.focus_force()
        
        print('\a')
        Label(dialog, text='This program made by Sina.f').pack(pady=12)
        
        Button(dialog, text='GitHub', width=8, command=lambda: webbrowser.open('https://github.com/sina-programer')).place(x=30, y=50)
        Button(dialog, text='Instagram', width=8, command=lambda: webbrowser.open('https://www.instagram.com/sina.programer')).place(x=120, y=50)
        Button(dialog, text='Telegram', width=8, command=lambda: webbrowser.open('https://t.me/sina_programer')).place(x=210, y=50)
        
        dialog.mainloop()
            
    def init_menu(self, master):
        menu = Menu(master)
        menu.add_command(label='Help', command=lambda: messagebox.showinfo('Help', help_msg))
        menu.add_command(label='About us', command=self.show_about)
        
        return menu  
    

help_msg = '''1_ Set the gender of the name
2_ Set the length of the word
3_ Choose a letter & set in which letter do you want to put it

* Just for persian names *'''

icon = r'Files\icon.ico'
names_file = r'Files\Names.csv'

if __name__ == "__main__":
    root = Tk()
    root.title('Name Finder')
    root.geometry('270x140+550+250')
    root.resizable(False, False)
    
    if os.path.exists(names_file):
        if os.path.exists(icon):  
            root.geometry('270x160+550+250')
            root.iconbitmap(icon)
            
        app = App(root)
        
    else:
        print('\a')
        Label(root, text='Please run the app in the default folder!', fg='red').pack()

    root.mainloop()
   