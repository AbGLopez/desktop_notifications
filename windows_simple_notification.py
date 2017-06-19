#!/usr/bin/python


# You will need to use a 3rd party python GUI library or the pywin32 library.
# TkInter, the GUI toolkit that comes bundled with python does not support system tray pop ups.

# Multiform neutral libraries that support working with the system tray:

# wxPython
# PyGTK
# PyQT
# Windows specific library that supports working with the system tray:

# pywin32
# Information/example of system tray pop ups using wxpython on window

############################################################################
# Detect Windows version

# Windows 10
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast('Hello World!!!', 'Python is 10 seconds awsm!',
                   icon_path='custom.ico', duration=10)
toaster.show_toast('Hello World!!!', 'Python is awsm by default!')

# window 8
from plyer import notification
notification.notify(
    title='Here is the title',
    message='Here is the message',
    app_name='Here is the application name',
    app_icon='path/to/the/icon.png')
