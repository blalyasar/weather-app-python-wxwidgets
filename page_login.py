import wx
import sys
from page_weather import WeatherPage
import sqlite3

SCREEN_WIDTH = 600 // 2
SCREEN_HEIGHT = 780 // 2



def check_credentials(email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    conn.close()

    return user is not None

class LoginPage(wx.Frame):
    def __init__(self, *args, **kw):
        super(LoginPage, self).__init__(*args, **kw)

        self.panel2 = wx.Panel(self)
        self.SetBackgroundColour(wx.Colour(wx.LIGHT_GREY))

        # email control
        self.email = wx.StaticText(self.panel2, label="e-mail")
        self.email_textctrl = wx.TextCtrl(self.panel2)

        self.password_label = wx.StaticText(self.panel2, label="Parola:")
        self.password_textctrl = wx.TextCtrl(self.panel2, style=wx.TE_PASSWORD)

        # Giriş button
        self.login_button = wx.Button(self.panel2, label="Giris Yap", size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.on_login, self.login_button)


        # Çıkış button
        self.exit_button = wx.Button(self.panel2, label="Cikis Yap", size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.on_exit, self.exit_button)

        # dikey box
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # email
        sizer.Add(self.email, 0, wx.ALL, 10)
        sizer.Add(self.email_textctrl, 0, wx.EXPAND | wx.ALL, 10)
        
        # password
        sizer.Add(self.password_label, 0, wx.ALL, 10)
        sizer.Add(self.password_textctrl, 0, wx.EXPAND | wx.ALL, 10)

        sizer.Add(self.login_button, 5, wx.EXPAND |wx.ALL, 10)
        sizer.Add(self.exit_button, 5, wx.EXPAND |wx.ALL, 10)

        self.panel2.SetSizerAndFit(sizer)
        self.Fit()
        self.SetMinSize((SCREEN_WIDTH,SCREEN_HEIGHT))
        # second screen ortalama.....
        self.CentreOnScreen(wx.BOTH)

    def on_exit(self,event):
        # self.Hide()
        # self.Close()
        # self.Destroy()
        # TO DO close wxapp...
        sys.exit()

    def on_login(self,event):
        self.email = self.email_textctrl.GetValue()
        self.password = self.password_textctrl.GetValue()

        # Kullanıcı adı ve parola doğrulaması (örnek amaçlı sadece)
        
        if check_credentials(self.email, self.password):
            wx.MessageBox("Girdiler Bos değil... Kayit Ok")
            self.Hide()
            weather_frame = WeatherPage(None, -1, title='Weather Ekranı',)
            # Center it with the 'Centre' method
            weather_frame.Centre()
            weather_frame.Show()
        else:
            wx.MessageBox("Girdiler bos ve hatalı.", "Hata")

