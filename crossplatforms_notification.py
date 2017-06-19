#!/usr/bin/python
import platform
print platform.system()

############################################################################
msg_title = 'Hello my Friend'
msg_body = 'Here is the message'

# Detect Windows version
if platform.system() == 'Windows':
    # Windows 10
    if platform.release() == '10':
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(
            msg_title, msg_body, icon_path='custom.ico', duration=10)
        toaster.show_toast(msg_title, msg_body)

    # Window 8
    if platform.release() == '8.0':
        from plyer import notification

        notification.notify(title=msg_title,
                            message=msg_body,
                            app_name='Here is the application name',
                            app_icon='path/to/the/icon.png')

if platform.system() == 'Linux':
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify

    Notify.init(msg_title)
    msg = Notify.Notification.new(msg_title, msg_body, 'dialog-information')
    msg.show()
