from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User



def inquiry(request):
	if request.method == 'POST':
		car_id = request.POST['car_id']
		car_title = request.POST['car_title']
		user_id = request.POST['user_id']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		customer_need = request.POST['customer_need']
		city = request.POST['city']
		state = request.POST['state']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']

		if request.user.is_authenticated:
			user_id = request.user.id 
			has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
			if has_contacted:
				messages.success(request, "Nous avons bien reçu votre demande suite à cette article. Nous vous prions de patienter notre équipe de communication vous répondra dans les plus bref délai !")
				return redirect('/cars/'+car_id)

		contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)

		admin_info = User.objects.get(is_superuser=True)
		admin_email = admin_info.email
		send_mail(
			'Acquisition de nouvelle voiture',
			"Nous avons une nouvelle demande d'acquisition pour la voiture " + car_title + ". S'il vous plait, connectez vous au paneau d'administration.",
			'dorianlenoumi@gmail.com',
			[admin_email],
			fail_silently=False,
		)

		contact.save()
		messages.success(request, 'Votre requête est bien soumise, notre équipe de communtication vous répondra dans les plus bref délai !')
		return redirect('/cars/'+car_id)
