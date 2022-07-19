from datetime import date
from django.shortcuts import render
import datetime
from datetime import date
import holidays

# Create your views here.
def index(request):
    sa_holidays = holidays.SA()
    sa_holidays = holidays.country_holidays('SA')  # this is a dict
    now = datetime.datetime.now()
    return render(request , "itseid/index.html", {
       "eid": date(now.year, now.month, now.day) in sa_holidays
         #from https://github.com/dr-prodigy/python-holidays
   })
   