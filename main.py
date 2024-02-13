import wx
import sqlite3
from page_login import LoginPage
import platform


py_version = 'Python version:' + platform.python_version()
wx_version = 'wxPython version: ' + wx.version()
os_version = 'Operating System: ' + platform.platform()
# ID_LOGBUTTON = wx.NewId()

import sqlite3

# SQLite veritabanı bağlantısı oluştur
conn = sqlite3.connect('users.db')

# Cursor oluştur
cursor = conn.cursor()

# Kullanıcı tablosunu oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

 
conn.commit()
conn.close()



def add_user( email, username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (email, username, password) VALUES (?, ?, ? )', (email, username, password))
    conn.commit()
    conn.close()



SCREEN_WIDTH = 600 // 2
SCREEN_HEIGHT = 780 //2
 
 


class WelcomePage(wx.Frame):
    def __init__(self, *args, **kw):
        super(WelcomePage, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.CreateStatusBar()
        # https://docs.wxwidgets.org/3.0/classwx_colour.html
        self.SetBackgroundColour(wx.Colour(wx.LIGHT_GREY))


        self.projectname = wx.StaticText(self.panel, label="Weather App")
        

        # Kullanıcı adı ve parola  email
        self.username_label = wx.StaticText(self.panel, label="İsim Soyisim")
        self.username_textctrl = wx.TextCtrl(self.panel)

        # email control
        self.email = wx.StaticText(self.panel, label="e-mail")
        self.email_textctrl = wx.TextCtrl(self.panel)

        self.password_label = wx.StaticText(self.panel, label="Parola:")
        self.password_textctrl = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)

        # Giriş 
        self.register_button = wx.Button(self.panel, label="Kayit Ol", size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.on_register, self.register_button)

        self.login_button = wx.Button(self.panel, label="Uyeliginiz Var mi! Giris yap", size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.on_login, self.login_button)


        # vertical dik
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.projectname, 10, wx.EXPAND |wx.ALL, 10)

        # username 
        sizer.Add(self.username_label, 10, wx.ALL, 10)
        sizer.Add(self.username_textctrl, 0, wx.EXPAND | wx.ALL, 10)
        
        # email
        sizer.Add(self.email, 0, wx.ALL, 10)
        sizer.Add(self.email_textctrl, 0, wx.EXPAND | wx.ALL, 10)
        
        # password
        sizer.Add(self.password_label, 0, wx.ALL, 10)
        sizer.Add(self.password_textctrl, 0, wx.EXPAND | wx.ALL, 10)

        sizer.Add(self.register_button, 10, wx.EXPAND |wx.ALL, 10)
        sizer.Add(self.login_button, 10, wx.EXPAND |wx.ALL, 10)

        self.panel.SetSizerAndFit(sizer)
        self.SetMinSize((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.Fit()
         
    

    def on_register(self,event):
        email = self.email_textctrl.GetValue()
        username = self.username_textctrl.GetValue()
        password = self.password_textctrl.GetValue()

        # email password sqlite kullanildi 
        if email != "" and username != "" and password != "":
            wx.MessageBox("Girdiler Bos değil... Kayit Ok... Login Ekranina Yonlendiriliyorsunuz")
            # go to login page
            add_user(email,username,password) # free....
            self.on_login(event)
        else:
            wx.MessageBox("Girdiler bos ve hatalı.", "Hata")

 

    def on_login(self, event):
        # TO DO OPEN NEW PAGE
         
        username = self.username_textctrl.GetValue()
        password = self.password_textctrl.GetValue()
        
        # if self.panel.IsShown():
        # self.panel.Hide()
        frame.Hide()
         
        login_frame = LoginPage(None, title="Login Ekranı") # 

        login_frame.Centre()
        login_frame.Show()

        

if __name__ == '__main__':
    app = wx.App(False)
    frame = WelcomePage(None, title="Giriş Ekranı")
    frame.Centre()
    frame.Show()
    app.MainLoop()

  