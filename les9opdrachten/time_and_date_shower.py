#     |\__/,|   (`\
#   _.|o o  |_   ) )
# -(((---(((--------
#
# Made by : Corsolaa
# Date    : 29/03/2022
import datetime


def GetMonth(index_month):
    months = ["januari", "februari", "maart", "april", "mei", "juni", "juli",
              "augustus", "september", "oktober", "november", "december"]
    return months[index_month - 1]


def GetDay(index_days):
    days = ["maanday", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
    return days[index_days - 1]


def PrintDate():
    e = datetime.datetime.now()
    print("Vandaag is het: %s %s %s %s:%s:%s" % (GetDay(e.today().isoweekday()), e.day, GetMonth(e.month), e.hour, e.minute, e.second))


PrintDate()
