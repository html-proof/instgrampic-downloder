from tkinter import *
from tkinter import Entry
import pyttsx3
import instaloader
from win10toast import ToastNotifier
import pyautogui
from threading import *

newVoiceRate = 145
engine =pyttsx3.init()
engine.setProperty("rate", newVoiceRate)
root = Tk()
root.geometry("500x250")
root.title("Instagram .!@")
root.resizable(0, 0)
root.config(bg="Black")
root.iconbitmap('./download.ico')
user_var = StringVar()
while True:
    try:
        def threading():
            t1 = Thread(target=pic)
            t1.start()


        def pic():
            try:
                txt = user_entry.get()
                user_entry.delete(0, END)
                mod = instaloader.Instaloader()
                mod.download_profile(txt, profile_pic_only=True)
                lbl1 = Label(root, text=' Pic is downloaded!', font='arial 15', fg="White", bg="#EC7067")
                engine.say(" Pic is downloaded!")
                engine.runAndWait()
                lbl1.pack()
                lbl1.after(3000, lambda: lbl1.destroy())
            except instaloader.ProfileNotExistsException:
                lbl2 = Label(root, text='ProfileNotExists!', font='arial 15', fg="White", bg="#EC7089")
                engine.say('ProfileNotExists')
                engine.runAndWait()
                lbl2.pack()
                lbl2.after(3000, lambda: lbl2.destroy())
            except instaloader.ProfileHasNoPicsException:
                lbl3 = Label(root, text='ProfileHasNoPics!', font='arial 15', fg="White", bg="#EC7063")
                engine.say("ProfileHasNoPics")
                engine.runAndWait()
                lbl3.pack()
                lbl3.after(3000, lambda: lbl3.destroy())
            except instaloader.BadResponseException:
                lbl4 = Label(root, text='BadResponseException!', font='arial 15', fg="White", bg="#EC7063")
                engine.say("BadResponseException")
                engine.runAndWait()
                lbl4.pack()
                lbl4.after(3000, lambda: lbl4.destroy())
            except instaloader.QueryReturnedBadRequestException:
                lbl5 = Label(root, text='BadResponseExceptioQueryReturnedBadRequestException!', font='arial 15',fg="White",bg="#EC7063")
                engine.say("BadResponseExceptioQueryReturnedBadRequestException")
                engine.runAndWait()
                lbl5.pack()
                lbl5.after(3000, lambda: lbl5.destroy())
            except instaloader.ConnectionException:
                lbl6 = Label(root, text='Please Check !', font='arial 15', fg="White", bg="#EC7063")
                engine.say("Please check")
                engine.runAndWait()
                lbl6.pack()
                lbl6.after(3000, lambda: lbl6.destroy())
            else:
                toast = ToastNotifier()
                toast.show_toast(f"{txt}  Instagram pic", "downloaded", duration=40, icon_path='download.ico')
                pyautogui.alert("Downloaded")


        lbl = Label(root, text="Instagram", font='arial 15', fg="Blue", bg="Black")
        lbl.pack(anchor="center")
        user_label = Label(root, text='Enter the UserName: ', font=('calibre', 10, 'bold'))
        user_entry: Entry = Entry(root, width=60, textvariable=user_var, font=('calibre', 10, 'normal'))
        download_button = Button(root, text="Click Me", command=threading)
    except RuntimeError:
        pass
        user_label.pack()
    except TclError:
        lbl7 = Label(root, text="Exiting...",font='arial 15', fg="Blue", bg="Black")
        lbl7.pack(anchor="center")
    user_entry.pack()
    download_button.pack()
    root.mainloop()
