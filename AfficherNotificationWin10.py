import os
from win10toast import ToastNotifier

def notification():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()
    title = "Notification"
    message = "Test de notification réussi :)"
    length = 20
    toast.show_toast(title, message, duration=length)

notification()