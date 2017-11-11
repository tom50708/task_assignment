# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mylibrary.message import show_message
# Create your views here.
def index(request):
	dics = {'content' : 'This is Index Page'}
	return render(request,'ta_app/index.html', context=dics)

def task(request):
	dics = {'content' : 'This is Task Page'}
	return render(request, 'ta_app/task.html', context=dics)

def report(request):
	dics = {'content' : 'This is report Page'}
	return render(request, 'ta_app/report.html', context=dics) 

def user_login(request):
	message = {}

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user :
			if user.is_active :
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				message = show_message('red', '登入系統發生問題')
		else:
			message = show_message('red', '無效的帳號或密碼')
 
	return render(request, 'ta_app/user_login.html', context=message)

@login_required
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('user_login.html')