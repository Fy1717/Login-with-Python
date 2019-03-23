import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.title( "kodlarinicinde 31-01-2019" )

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 320
window_height = 250

window_position_x = 0
window_position_y = 0
root.geometry("320x250")

frame = tk.Frame(root, bg='cyan')
frame.pack(side="bottom", fill='both', expand='no')

userLabel = Label(root,width=20,height=3,text="KULLANICI ADI   :" , font="Times 10 bold")
userLabel.place(x=5 ,y=26)

passwordLabel = Label(root,width=20,height=3,text="PAROLA               :" , font="Times 10 bold")
passwordLabel.place(x=5,y=66)

userLabel = Label(root,width=40,height=3,text="www.frknyldz.com" , font="Times 10 bold")
userLabel.place(x=5 ,y=206)


userName_edit = Entry(root,width=15)
userName_edit.place(x=150,y=40)
userName_edit.config(font="bold")
userName_edit.insert(END,"")

password_edit = Entry(root,width=15)
password_edit.place(x=150,y=80)
password_edit.config(font="bold")
password_edit.insert(END,"")


# Kullanýcý Kontrol Fonksiyonu
def UserControl():
    if userName_edit.get() == 'kodlarinicinde' and password_edit.get() == 'python':
        tk.messagebox.showinfo(" TEBRİKLER !! \r\n", "UMARIM HAWKING YILDIZLARIN ARASINDA EĞLENİYORDUR ")


    else:
        tk.messagebox.showinfo(
            "TEKRAR DENE BAKALIM !\r\n", "HAYALİMİN BAŞLADIĞI YER BURASIYDI")

# Giriþ Alanlarýný Temizleme Fonksiyonu
def Clear():
    userName_edit.delete('1.0',END)
    password_edit.delete('1.0',END)



# Giriþ Butonu
controlButton = Button(root,text="GİRİŞ",width=30,command=UserControl)
controlButton.config(font="bold")
controlButton.place(x=10,y=150)



root.mainloop()