from django.shortcuts import render
from django.http import HttpResponse



data = {
  "Mukhil": "KG",
  "Anto": "GM",
}
def home(request):
	if request.method =="POST":
		name = request.POST['fname']
		# lastname = request.POST['lname']


		print(name)
	return render(request,'home.html')

