from django.shortcuts import render
import mysql.connector as sql
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def my_view(request):
    c = {}
    # ...
    return render(request, "", c)
un=''
pwd=''
# Create your views here.
def loginaction(request):
    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="28mg",database='website1')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="uname":
                un=value
            if key=="password":
                pwd=value
        
        c="select * from users where uname='{}' and password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')