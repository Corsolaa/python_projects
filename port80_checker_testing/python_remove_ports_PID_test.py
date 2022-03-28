#     |\__/,|   (`\
#   _.|o o  |_   ) )
# -(((---(((--------
#
# Made by : Corsolaa
# Date    : 28/03/2022
import psutil
import os
import PySimpleGUI as sg
import os.path

sg.theme('DarkAmber')
layout = [
    [sg.Text("portnumbers here which to inspect:")],
    [sg.Text("     port 1:"), sg.Text("                  port 2:")],
    [sg.InputText(size=(11, 1)), sg.Text("     "), sg.InputText(size=(11, 1))],
    [sg.Text("                "), sg.Button('Search')],
    [sg.Multiline(size=(30, 5), disabled=True, key='textbox')],
    [sg.Button("Exit"), sg.Button("yes", key="yes", visible=False), sg.Button("no", key="no", visible=False)]
]
win = sg.Window("port_reader", layout, size=(500, 500))
ml_obj = win.find_element("textbox")

while True:
    event, values = win.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Search":
        win.find_element('yes').Update(visible=True)
        win.find_element('no').Update(visible=True)
        t = 2
    # if event == "":

# def test():
#     ml_obj.Update(t)


# * * * * * * *
# * Why: checking if any application is using the ports of input
# * Input: ports that you want to check
# * Return: N/A
# * Exception: TypeError returned if input is not a digit / integer
# * * * * * * *
def PortCheckingGui(p1, p2):
    # Checking if the incoming parameter is a digit / integer.
    if isinstance(p1, int) and isinstance(p1, int):
        # Grabbing a list of all connections
        ports = psutil.net_connections('inet')
        terminate_prog = []
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
                    print(msg)
        # Checking if the program filtered something out
        if len(terminate_prog) == 0:
            print("no process running on port 80 and 443...")
        else:
            ProcessRemoveGui(terminate_prog)
    else:
        raise TypeError("Input needs to be an digit / integer")


# * * * * * * *
# * Why: to terminate programs using program names given in an array.
# * Input: array[] whit program names inside.
# * Return: N/A
# * Exception: TypeError returned if input in not an array[].
# * * * * * * *
def ProcessRemoveGui(terminate_prog):
    # Checking if the incoming parameter is an array[].
    if isinstance(terminate_prog, list):
        while True:
            print("\n" + r"do you want to terminate the programs above /\ (y/n): ")
            answer = input().lower()
            if answer == "y":
                for prog in terminate_prog:
                    # Giving system the kill task command with the name that inputted.
                    os.system("TASKKILL /F /IM " + prog)
                break
            elif answer == "n":
                print("Probably working whit XAMPP are you hehe")
                break
    else:
        raise TypeError("Input needs to be an array[]")
