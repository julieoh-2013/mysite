from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def writeform(request):
    # 인증 체크 : 인증된 사람만 호추랗게
    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')





