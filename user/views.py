from django.forms import model_to_dict
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def joinform(request):
    return render(request, 'user/joinform.html')


def join(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save()
    return HttpResponseRedirect('/user/joinsuccess')


def modifyform(request):
    return render(request, 'user/modifyform.html' )

def modify(request):
    user = User()
    user.id = request.POST['id']
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save()

    request.session['authuser'] = model_to_dict(user)  # 객체를 딕셔너리로 저장하는 함수
    return HttpResponseRedirect('/')



def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    result = User.objects.filter(email=request.POST['email']).filter(password=request.POST['password'])
    #리스트로 리턴옴

    if len(result) == 0: # 로그인실패
        return HttpResponseRedirect('/user/loginform?result=false')
    #로그인 처리
    authuser = result[0] #로그인한 유저 객체를  request sesson 에 저장 #브라우져 끄전가지 session저장해서 request달려 있는 세션은 같다 로그인 성공할때만 저장 함
    request.session['authuser'] = model_to_dict(authuser) # 객체를 딕셔너리로 저장하는 함수
    #return HttpResponse(' 인증이 성공했어요 ') # 인증성공시 브라우져에 텍스트출력 하고 싶을때
    #return HttpResponse(authuser)
    return HttpResponseRedirect('/')

def logout(request): #logout - session안에 있는 객체 삭제
    del request.session['authuser']
    return HttpResponseRedirect('/')














