from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request , "itseid/index.html", {
        "eid":False 
        #True
         #now.month == 4 and now.day == 20
    })
