#     |\__/,|   (`\
#   _.|o o  |_   ) )
# -(((---(((--------
#
# Made by : Corsolaa
# Date    : 02/04/2022

# Maak een applicatie die om een bepaalde tijd een website pingt
# om te kijken of die online is. Als de website niet online is
# wordt er een mailtje gestuurd om te laten weten dat de website
# offline is 😉

import os


def start_program(ip_list):
    for ip in ip_list:
        cmd_response = os.popen(f"ping {ip}").read()
        if "Received = 4" in cmd_response:
            print("Yeey on: " + ip + " the ping is successful")
        else:
            print("Shit on: " + ip + " the ping is unsuccessful")


test_array = ["google.com", "192.168.474.85"]
start_program(test_array)
