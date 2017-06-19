#!/usr/bin/python

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init("Hello world")

Hello = Notify.Notification.new(
    "Hello world", "This is an example notification.", "dialog-information")

Hello.show()

# You will need to use a 3rd party python GUI library or the pywin32 library.
# TkInter, the GUI toolkit that comes bundled with python does not support system tray pop ups.

# Multiform neutral libraries that support working with the system tray:

# wxPython
# PyGTK
# PyQT
# Windows specific library that supports working with the system tray:

# pywin32
# Information/example of system tray pop ups using wxpython on window

# para windows 10

# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
#               "Python is 10 seconds awsm!",
#               icon_path="custom.ico",
#               duration=10)
# toaster.show_toast("Hello World!!!",
#              "Python is awsm by default!")

# from plyer import notification
# notification.notify(
#     title='Here is the title',
#     message='Here is the message',
#     app_name='Here is the application name',
#     app_icon='path/to/the/icon.png')


# import os
# import signal
# import json
# from urllib2 import Request, urlopen, URLError

# from gi.repository import Gtk as gtk
# from gi.repository import AppIndicator3 as appindicator
# from gi.repository import Notify as notify

# APPINDICATOR_ID = 'myappindicator'


# def main():
#     indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('sample_icon.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
#     indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
#     indicator.set_menu(build_menu())
#     notify.init(APPINDICATOR_ID)
#     gtk.main()


# def build_menu():
#     menu = gtk.Menu()
#     item_joke = gtk.MenuItem('Joke')
#     item_joke.connect('activate', joke)
#     menu.append(item_joke)
#     item_quit = gtk.MenuItem('Quit')
#     item_quit.connect('activate', quit)
#     menu.append(item_quit)
#     menu.show_all()
#     return menu


# def fetch_joke():
#     request = Request('http://api.icndb.com/jokes/random?limitTo=[nerdy]')
#     response = urlopen(request)
#     joke = json.loads(response.read())['value']['joke']
#     return joke


# def joke(_):
#     print 'loco'
#     notify.Notification.new("<b>Joke</b>", fetch_joke(), None).show()


# def quit(_):
#     notify.uninit()
#     gtk.main_quit()


# if __name__ == "__main__":
#     signal.signal(signal.SIGINT, signal.SIG_DFL)
#     main()
