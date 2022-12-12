from django.shortcuts import *
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas = pizza.objects.order_by('pizza_name')
    context = {
        'all_pizzas':pizzas
    }
    return render(request,'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    j = pizza.objects.get(id=pizza_id)
    toppings = toppings.objects.filter(pizza=j)
    comments = Comment.objects.filter(pizza=j).order_by('date_added')
    context = {
        'pizza':j, 'toppings':toppings, 'comments':comments
    }
    return render(request, 'MainApp/pizza.html', context)

def new_comment(request, pizza_id):
    pizza = pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        print(request.POST)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save()
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
    context = {'form':form, 'pizza':pizza}
    return render (request, 'pizzas/new_comment.html', context)