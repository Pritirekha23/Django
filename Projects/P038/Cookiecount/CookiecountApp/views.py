from django.shortcuts import render,HttpResponse

def page_count_view(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count'])+1
    else:
        count=1
    response=HttpResponse()
    response.set_cookie('count',count)
    return response
