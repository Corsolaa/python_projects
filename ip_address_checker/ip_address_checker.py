import socket
import time
from requests import get
from win10toast import ToastNotifier

current_local_ip_address = socket.gethostbyname(socket.gethostname())
current_public_ip_address = get('https://api.ipify.org').text
toaster = ToastNotifier()


while True:
    time.sleep(8)
    temp_local_ip_address = socket.gethostbyname(socket.gethostname())
    temp_public_ip_address = get('https://api.ipify.org').text

    if (temp_local_ip_address != current_local_ip_address) or (temp_public_ip_address != current_public_ip_address):
        toaster.show_toast("Server notification", "ip-address changed!!")
