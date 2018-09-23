from django.shortcuts import render

# Create your views here.
def index(request):
	return render(
		request,
		'index.html'
		##context = {'':, '':,}
		)

def profile(request):
	return render(
		request,
		'profile.html'
		##context = {'':, '':,}
		)