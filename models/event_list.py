from models.event import *
import datetime

datetime1 = datetime.date(2022, 12, 24)
datetime2 = datetime.date(2022, 12, 12)
event1 = Event(datetime1, "Christmas Celebrtation", 200, "Edinburgh Castle", "Having fun with friends")
event2 = Event(datetime2, "Birthday Celebration", 1, "39 Gardeners Crescent", "Drinking Whiskey In A Dark Room")

events = [event1, event2]
