from django.shortcuts import render
from datetime import datetime

def wish_view(request):
    # time=3
    current_date_time=datetime.now()
    time=int(current_date_time.strftime
    ('%H'))
    #the strftime method is used to format the current date and time as a string.
    #int() function is used to convert the string to integer so that we can compare.
    #render function is a function which takes requests as 1st argument then template file location then context dictionary and return HTTP response to the location.
    #IT is used to transfer the control one file to another file.
    
    if time>=4 and time<12:
        wish='Good Morning'
    elif time>=12 and time<17:
        wish='Good Afternoon'
    elif time>=17 and time<22:
        wish='Good evening'
    else:
        wish='Good Night'
    d={'time':time,'wish':wish}
    return render(request,'WishMsgApp/home.html',d)

