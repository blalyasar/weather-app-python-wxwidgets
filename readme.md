This project run on the Linux ubuntu20 5.15.0-94-generic #104~20.04.1-Ubuntu SMP Tue Jan 16 13:34:09 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux

sudo apt install python3.8-venv install vim openssh-client openssh-server libsdl2-dev git

python3 -m venv basic-weather-app-gtk

source basic-weather-app-gtk/bin/activate

pip install -U -f  https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-20.04/ wxPython

pip install websocket-client

pip install requests

git clone https://github.com/blalyasar/weather-app-python-wxwidgets.git

cd /weather-app-python-wxwidgets

python main.py
