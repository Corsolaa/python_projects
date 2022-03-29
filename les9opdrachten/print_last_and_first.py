#     |\__/,|   (`\
#   _.|o o  |_   ) )
# -(((---(((--------
#
# Made by : Corsolaa
# Date    : 29/03/2022

def PrintLastAndFirst(checklist):
    printlists = ""
    if len(checklist) != 0:
        printlists = checklist[0]
        if len(checklist) > 1:
            printlists += ", "
            printlists += checklist[len(checklist) - 1]
    print(printlists)


color_list = ["Red", "Green", "White", "Black"]
color_list2 = ["Red", "Green", "White", "Black", "Yellow"]
PrintLastAndFirst(color_list)
PrintLastAndFirst(color_list2)
