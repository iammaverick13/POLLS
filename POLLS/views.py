from django.shortcuts import render, redirect

def home(request):
	context = {
		'pageTitle':'HOME',
	}
	return render(request, 'index.html', context)