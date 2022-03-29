#     |\__/,|   (`\
#   _.|o o  |_   ) )
# -(((---(((--------
#
# Made by : Corsolaa
# Date    : 28/03/2022
import psutil
import PySimpleGUI as sg
import os.path

sg.theme('Black')
layout = [
    [sg.Text("          Which port numbers would you like to inspect?:")],
    [sg.Text("                         port 1:"), sg.Text("                  port 2:")],
    [sg.Text("                "), sg.InputText(size=(11, 1)), sg.Text("     "), sg.InputText(size=(11, 1))],
    [sg.Text("                                    "), sg.Button('Listen')],
    [sg.Multiline(size=(50, 8), disabled=True, key='textbox')],
    [sg.Button("Exit"), sg.Text("                       "), sg.Button("Terminate", disabled=True)]
]
win = sg.Window("port listener", layout, icon=r'.\python.ico',
                size=(400, 300))
ml_obj = win.find_element("textbox")
yes_but = win.find_element("Terminate")
terminate_prog = []


# * * * * * * *
# * Why: checking if any application is using the ports of input
# * Input: ports that you want to check
# * Return: N/A
# * Exception: TypeError returned if input is not a digit / integer
# * * * * * * *
def PortCheckingGui(p1, p2):
    # Grabbing a list of all connections
    ports = psutil.net_connections('inet')
    # Looping through every port
    for p in ports:
        (ip, port) = p.laddr
        pid_s = str(p.pid)
        # Making a list of all processes
        process_info = psutil.Process(int(pid_s))
        # Creating message block
        msg = "PID " + pid_s + " is listening on port " + str(port) + " named: " + process_info.name()
        # Filtering out every process that has port 80 and or 443
        if port == p1 or port == p2:
            # Checking if it doesn't have a duplicated name
            if process_info.name() not in terminate_prog:
                # Giving non-duplicate names towards array
                terminate_prog.append(process_info.name())
                # Prints towards screen
                ml_obj.print(msg + "\n")
    # Checking if the program filtered something out
    if len(terminate_prog) == 0:
        ml_obj.update("no process running on port " + str(p1) + " or " + str(p2) + "...")
    else:
        yes_but.update(disabled=False)


while True:
    event, value = win.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Listen":
        if value[0].isdigit() and value[1].isdigit():
            value[0] = int(value[0])
            value[1] = int(value[1])
            ml_obj.update('')
            PortCheckingGui(value[0], value[1])
        else:
            ml_obj.update("Please input a digit of 6 characters!!!")
    if event == "Terminate":
        ml_obj.print("terminating listeners...\n")
        for prog in terminate_prog:
            # Giving system the kill task command with the name that inputted.
            os.system("TASKKILL /F /IM " + prog)
            terminate_prog = []
            yes_but.update(disabled=True)
            ml_obj.print("success")
