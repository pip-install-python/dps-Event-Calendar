from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_profile(request):
    user_agent = request.META['HTTP_USER_AGENT']
    current_date = datetime.now()

    # Create a list to hold the current date and the last day of the past five months
    dates_list = [current_date.strftime('%B, %d, %Y')]  # Add current date in formatted form

    for _ in range(4):
        # Get the last day of the previous month
        last_day_previous_month = current_date.replace(day=1) - timedelta(days=1)

        # Format the date as "Month, DD, YYYY"
        formatted_date = last_day_previous_month.strftime('%B, %d, %Y')

        # Add the formatted date to the list
        dates_list.append(formatted_date)

        # Update current_date to the first day of the previous month
        current_date = last_day_previous_month.replace(day=1)

    if 'Mobile' in user_agent:
        return render(request, 'user_account/account_payment_settings.html', )
    else:
        return render(request, 'user_account/account_payment_settings.html', context={'months_list': dates_list})

def account_settings(request):
    user_agent = request.META['HTTP_USER_AGENT']

    # Get user's IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Pass IP address to the template
    context = {'user_ip': ip}

    if 'Mobile' in user_agent:
        return render(request, 'user_account/account_settings.html', )
    else:
        return render(request, 'user_account/account_settings.html', context)

def reset_password(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'user_account/reset_password.html', )
    else:
        return render(request, 'user_account/reset_password.html', )

def sign_in(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('shop')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'user_account/sign_in.html', {'error': 'Invalid credentials'})

    if 'Mobile' in user_agent:
        return render(request, 'user_account/sign_in.html', )
    else:
        return render(request, 'user_account/sign_in.html', )

def sign_up(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        terms = request.POST.get('terms', False)

        if not terms:
            messages.error(request, "You must agree to the terms and conditions.")
            return redirect('sign_up')

        # Create the user
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
            user_login = authenticate(request, username=email, password=password)

            login(request, user_login)
            return redirect('shop')  # Redirect to a home or profile page
        except Exception as e:
            messages.error(request, str(e))
            return redirect('sign_up')

    if 'Mobile' in user_agent:
        return render(request, 'user_account/sign_up.html', )
    else:
        return render(request, 'user_account/sign_up.html', )

def logout_view(request):
    logout(request)
    return redirect('/coffee')
