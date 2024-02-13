import wx
import requests
import wx.lib.scrolledpanel as scrolled

SCREEN_WIDTH = 600 // 2
SCREEN_HEIGHT = 780 // 2




import json
#  TR JSON file
file_path = "examples/cities_of_turkey.json"

#  JSON OKU
with open(file_path, "r") as file:
    data = json.load(file)
print(data)

# 
# # for test api rate limit# 81 ILE ISTEK AT
# MAMAK ICIN LIMIT
# NUMBER_OF_CITY = 10

cities = []
for item in data:
    # 
    # # for test api rate limit# 
    # if item["id"] == NUMBER_OF_CITY:
    # #     break
    # print(f"Name: {item['name']},
    # Age: {item['age']}")
    print(item["name"])
    cities.append( (item["id"],item["name"], item["name"], item["latitude"], item["longitude"]))

 


 




class MyPanel(scrolled.ScrolledPanel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        self.SetAutoLayout(1)
        self.SetupScrolling()

class WeatherPage( wx.Frame ):
    def __init__( self, parent, ID, title ):
        wx.Frame.__init__( self, parent, ID, title, wx.DefaultPosition, wx.Size( 400, 300 ) )
        self.list_temperature_labels = []

        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):
        MPanel = MyPanel(self)
        grid_sizer = wx.GridBagSizer(hgap=81, vgap=5)
        POSX, POSY = 0, 0

        
        for city in cities:
            # POSITION ORIENTATION
            if POSY >= 3:
                POSX += 1
                POSY  = 0
            print(city)
            print(POSX, POSY)

            label0 = wx.StaticText(MPanel, label=f"{str(city[0])}")
            grid_sizer.Add(label0, pos=(POSX, POSY), flag=wx.ALL, border=5)
            POSY += 1
            print(POSX, POSY)
            
            label1 = wx.StaticText(MPanel, label=f"{str(city[1])}")
            print(label1) # debug icin
            self.list_temperature_labels.append(label1)


            grid_sizer.Add(label1, pos=(POSX, POSY), flag=wx.ALL, border=5)
            POSY += 1
            print(POSX, POSY)
            
            label2 = wx.StaticText(MPanel, label=f"{city[2]}")
            grid_sizer.Add(label2, pos=(POSX, POSY), flag=wx.ALL, border=5)
            POSY += 1
            print(POSX, POSY)
            
            label3 = wx.StaticText(MPanel, label=f"{str(city[3])} {str(city[4])}")
            grid_sizer.Add(label3, pos=(POSX, POSY), flag=wx.ALL, border=5)
            POSY += 1
            print(POSX, POSY)

        grid_sizer.AddGrowableCol(1)
        MPanel.SetSizerAndFit(grid_sizer)

        # Timer oluştur
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.auto_refresh_weather, self.timer)

        # THREAD arayuzde olustur...
        self.timer.Start(30000)  # 600000 milisaniye (10 dakika)

        # hava durumu func yenıleme...
        self.refresh_weather()

    def refresh_weather(self):
     
 

        for  city in  cities:
            print(city)
            # api key ONLY  02-03.2024 to do add config file etc...
            response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city[2]}&appid=eef452dbaecb031a04d46c7ad88eda57&units=metric")
            data = response.json()

            print(data)
            # data response 
            # {'coord': {'lon': 30.7178, 'lat': 36.7741},
                # 'weather': [{'id': 803, 'main': 'Clouds', 
            # 'description': 'broken clouds',
            # 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 13.95, 'feels_like': 13.59,
            # 'temp_min': 13.94, 'temp_max': 16.12, 'pressure': 1022, 'humidity': 84},
            # 'visibility': 10000, 'wind': {'speed': 2.57, 'deg': 90},
            # 'clouds': {'all': 75},
            # 'dt': 1707691240, 'sys': {'type': 2, 'id': 2042930, 'country': 'TR', 'sunrise': 1707713386, 'sunset': 1707751988},
            # 'timezone': 10800, 'id': 323776, 'name': 'Antalya Province', 'cod': 200}
            
            temperature_celsius = data["main"]["temp"]
            # print(temperature_kelvin) 
            # temperature_celsius = temperature_kelvin - 273.15

 
            print(city[1])
            #new_label_text = f"Temperature:  {temperature_kelvin}"
            # label.SetLabel(str(temperature_celsius))
            print(self.list_temperature_labels)
            # -1  importtant plaka 1den baslar 
            self.list_temperature_labels[ int(city[0]) -1  ].SetLabel(f"Temperature: {temperature_celsius} °C")
            
            # for test api rate limit
            # if city[0]  == NUMBER_OF_CITY :
            #     break
            


    def auto_refresh_weather(self, event):
        # Otomatik olarak hava durumu verilerini güncelle
        self.refresh_weather()










