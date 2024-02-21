import tkinter
import os
from tkinter import *
from tkinter import ttk, Tk
import tkinter.messagebox


def msgbox(msg):
    window = tkinter.Tk()
    window.wm_withdraw()
    tkinter.messagebox.showinfo(title="Pay Attention", message=msg)
    window.destroy()
    return None

msgbox("Attention this is a KMS script, it is better to buy an official key from Microsoft.")

# Окно
root = Tk()
root.title("Windows Activation(KMS)")
root.geometry("302x210")
img = PhotoImage(file='C:\\Users\\PC\\Desktop\\Project\\key.png')
root.iconphoto(False, img)

# Натписи
label = Label(text="Welcome!")
label.pack(anchor=CENTER)
label = Label(text="Chose option:")
label.pack(anchor=CENTER)


# Функции и код
def select1(button_num):
    root.destroy()
    if button_num == 1:
        window = Tk()
        window.title("Windows Activation(KMS)")
        window.geometry("302x175")
        img = PhotoImage(file='C:\\Users\\PC\\Desktop\\Project\\key.png')
        window.iconphoto(False, img)
        label = ttk.Label(window, text="Select KMS server: ")
        label.pack(expand=0)
        button = ttk.Button(window, text="kms.lotro.cc", command=lambda: WindowsPro(1))
        button.pack(expand=0)
        button = ttk.Button(window, text="kms.chinancce.com", command=lambda: WindowsPro(2))
        button.pack(expand=0)
        button = ttk.Button(window, text="NextLevel.uk.to", command=lambda: WindowsPro(3))
        button.pack(expand=0)
        button = ttk.Button(window, text="GuangPeng.uk.to", command=lambda: WindowsPro(4))
        button.pack(expand=0)
        button = ttk.Button(window, text="AlwaysSmile.uk.to", command=lambda: WindowsPro(5))
        button.pack(expand=0)
        button = ttk.Button(window, text="kms.shuax.com", command=lambda: WindowsPro(6))
        button.pack(expand=0)



def WindowsPro(button_num):
    if button_num == 1:
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms kms.lotro.cc")
        os.system("slmgr /ato")
    elif button_num == 2:
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms kms.chinancce.com")
        os.system("slmgr /ato")
    elif button_num == 3:
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms NextLevel.uk.to")
        os.system("slmgr /ato")
    elif button_num == 4:
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms GuangPeng.uk.to")
        os.system("slmgr /ato")
    elif button_num == 5:
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms AlwaysSmile.uk.to")
        os.system("slmgr /ato")
    elif button_num == 6:
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms kms.shuax.com")
        os.system("slmgr /ato")

def select2(button_num):
    root.destroy()
    if button_num == 1:
        window = Tk()
        window.title("Windows Activation(KMS)")
        window.geometry("302x175")
        img = PhotoImage(file='C:\\Users\\PC\\Desktop\\Project\\key.png')
        window.iconphoto(False, img)
        label = ttk.Label(window, text="Select KMS server: ")
        label.pack(expand=0)
        button = ttk.Button(window, text="kms.lotro.cc", command=lambda: WindowsHome(1))
        button.pack(expand=0)
        button = ttk.Button(window, text="kms.chinancce.com", command=lambda: WindowsHome(2))
        button.pack(expand=0)
        button = ttk.Button(window, text="NextLevel.uk.to", command=lambda: WindowsHome(3))
        button.pack(expand=0)
        button = ttk.Button(window, text="GuangPeng.uk.to", command=lambda: WindowsHome(4))
        button.pack(expand=0)
        button = ttk.Button(window, text="AlwaysSmile.uk.to", command=lambda: WindowsHome(5))
        button.pack(expand=0)
        button = ttk.Button(window, text="kms.shuax.com", command=lambda: WindowsHome(6))
        button.pack(expand=0)

def WindowsHome(button_num):
    if button_num == 1:
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms kms.lotro.cc")
        os.system("slmgr /ato")
    elif button_num == 2:
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms kms.chinancce.com")
        os.system("slmgr /ato")
    elif button_num == 3:
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms NextLevel.uk.to")
        os.system("slmgr /ato")
    elif button_num == 4:
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms GuangPeng.uk.to")
        os.system("slmgr /ato")
    elif button_num == 5:
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms AlwaysSmile.uk.to")
        os.system("slmgr /ato")
    elif button_num == 6:
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
        os.system("slmgr /skms kms.shuax.com")
        os.system("slmgr /ato")

def select3(button_num):
    root.destroy()
    if button_num == 1:
        window = Tk()
        window.title("Windows Activation(KMS)")
        window.geometry("302x175")
        img = PhotoImage(file='C:\\Users\\PC\\Desktop\\Project\\key.png')
        window.iconphoto(False, img)
        label = ttk.Label(window, text="Select KMS server: ")
        label.pack(expand=0)
        button = ttk.Button(window, text="kms.lotro.cc", command=lambda: WindowsEnterprise(1))
        button.pack(expand=0)
        button = ttk.Button(window, text="kms.chinancce.com", command=lambda: WindowsEnterprise(2))
        button.pack(expand=0)
        button = ttk.Button(window, text="NextLevel.uk.to", command=lambda: WindowsEnterprise(3))
        button.pack(expand=0)
        button = ttk.Button(window, text="GuangPeng.uk.to", command=lambda: WindowsEnterprise(4))
        button.pack(expand=0)
        button = ttk.Button(window, text="AlwaysSmile.uk.to", command=lambda: WindowsEnterprise(5))
        button.pack(expand=0)
        button = ttk.Button(window, text="kms.shuax.com", command=lambda: WindowsEnterprise(6))
        button.pack(expand=0)

def WindowsEnterprise(button_num):
    if button_num == 1:
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms kms.lotro.cc")
        os.system("slmgr /ato")
    elif button_num == 2:
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms kms.chinancce.com")
        os.system("slmgr /ato")
    elif button_num == 3:
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms NextLevel.uk.to")
        os.system("slmgr /ato")
    elif button_num == 4:
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms GuangPeng.uk.to")
        os.system("slmgr /ato")
    elif button_num == 5:
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms AlwaysSmile.uk.to")
        os.system("slmgr /ato")
    elif button_num == 6:
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
        os.system("slmgr /skms kms.shuax.com")
        os.system("slmgr /ato")

# кнопки
Button1 = ttk.Button(text="Windows 10/11 Pro", command=lambda: select1(1))
Button1.pack(expand=0)

Button2 = ttk.Button(text="Windows 10/11 Home", command=lambda: select2(1))
Button2.pack(expand=0)

Button3 = ttk.Button(text="Windows 10/11 Enterprise", command=lambda: select3(1))
Button3.pack(expand=0)

Deactivation = ttk.Button(text="Deactivate", command=lambda: Deactivate(1))
Deactivation.pack(expand=0, anchor=CENTER)

label = Label(text="Youtube: zeroXone")
label.pack(anchor=CENTER)
label = Label(text="TG: t.me/zeroxone_yt")
label.pack(anchor=CENTER)


Button4 = ttk.Button(text="Change Log", command=lambda: changes(1))
Button4.pack(expand=-0, anchor=SE)

def changes(button_num):
    root.destroy()
    if button_num == 1:
        window = Tk()
        window.title("Change log")
        window.geometry("302x175")
        img = PhotoImage(file='C:\\Users\\PC\\Desktop\\Project\\key.png')
        window.iconphoto(False, img)
        label = ttk.Label(window, text="Change Log")
        label.pack(expand=0)
        label = ttk.Label(window, text="- Added Windows versions: Pro/Home/Enterprise")
        label.pack(expand=0)
        label = ttk.Label(window, text="- Added Different KMS Servers")
        label.pack(expand=0)
        label = ttk.Label(window, text="- Added Change Log Button")
        label.pack(expand=0)
        label = ttk.Label(window, text="- Added Message after first startup application")
        label.pack(expand=0)
        label = ttk.Label(window, text="- Added Button Deactivate")
        label.pack(expand=0)
        label = ttk.Label(window, text="ver 5.0")
        label.pack(expand=1, anchor=S)


def Deactivate(button_num):
    if button_num == 1:
        os.system("slmgr /upk")


root.mainloop()
