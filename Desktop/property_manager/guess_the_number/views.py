from django.shortcuts import render
import random

def index(request):
    return render(request, 'guess_the_number/index.html')

def guess(request):
    message = ""
    if request.method == "POST":
        guess = int(request.POST.get('guess', 0))
        if 'number' not in request.session:
            request.session['number'] = random.randint(1, 100)
            request.session['attempts'] = 0
        
        request.session['attempts'] += 1
        number = request.session['number']

        if guess < number:
            message = "Too low!"
        elif guess > number:
            message = "Too high!"
        else:
            message = f"Correct! It took you {request.session['attempts']} attempts."
            del request.session['number']
            del request.session['attempts']

    return render(request, 'guess_the_number/guess.html', {'message': message, 'attempts': request.session.get('attempts', 0)})
