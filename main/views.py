from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request,'main/home.html')

def about(request):
	return render(request,'main/about.html')	

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			Full_Name = form.cleaned_data['Full_Name']
			Email = form.cleaned_data['Email']
			Phone_No = form.cleaned_data['Phone_No']
			Message = form.cleaned_data['Message']

			Subject = "Response From Contact Form"
			Message = "Name: "+Full_Name+"\nEmail: "+Email+"\nPhone_No: "+Phone_No+'\nMessage'+Message
			Recipient = ['aswinithas@gmail.com']
			sender = 'sekaranjana25@gmail.com'

			send_mail(Subject,Message,sender,Recipient)

	else:	
	    form = ContactForm()
	return render(request,'main/contact.html',{'form':form})		