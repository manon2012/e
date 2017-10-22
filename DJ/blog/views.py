from django.shortcuts import render,HttpResponse, render_to_response
from django.db import models
# Create your views here.

alist=[]
def index(requst):
    if requst.method == 'POST':
        e = requst.POST.get('name')
        t = requst.POST.get('title')
        c = requst.POST.get('content')
        print locals()
        # user={'name':name,'title':title,'content':content}
        # alist.append(user)
        # print alist

        models.BlogInfo.objects.create(
            name = e,
            title = t,
            content =c,
        )
    alist= models.BlogInfo.objects.all()
    return render_to_response('index.html',{'alist':alist})
