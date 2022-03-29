#     |\__/,|   (`\
#   _.|o o  |_   ) )
# -(((---(((--------
#
# Made by : Corsolaa
# Date    : 29/03/2022

def PiCalc():
    denom = 1
    pisum = 0
    for i in range(1000000):
        if i % 2 == 0:
            pisum += 4 / denom
        else:
            pisum -= 4 / denom
        denom += 2
    return pisum


def CalcSurfaceCircle(r):
    r2 = r * r
    surfacecirclem2 = PiCalc() * r2
    print("{:.2f}".format(surfacecirclem2))


CalcSurfaceCircle(6)
