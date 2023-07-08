from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from App.models import Product
from django.http import HttpResponseRedirect
from django.http import JsonResponse

# Frontend
def index(request):
    total = Product.objects.count()
    todos_produtos = Product.objects.all().order_by('-Data_Criacao')
    context = {
        'products': todos_produtos,
        'total_products': total,
    }
    return render(request, 'index.html', context)


# homepage
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    todos_produtos = Product.objects.all().order_by('-Data_Criacao')
    context = {
        'products': todos_produtos,
    }
    return render(request, 'home.html', context)
    
# add_product
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_product(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        produto = request.POST.get('produto')
        entradas = request.POST.get('entradas')
        saidas = request.POST.get('saidas')
        quantidade = request.POST.get('quantidade')
        genero = request.POST.get('genero')
        status = request.POST.get('status')
        contexto = request.POST.get('contexto')
        
        product = Product(
            nome=nome,
            telefone=telefone,
            produto=produto,
            entradas=entradas,
            saidas=saidas,
            quantidade=quantidade,
            genero=genero,
            contexto=contexto,
            status=status
        )
        product.save()
        
        return redirect('add_product')  # redirecionar para a página inicial após o salvamento
    
    return render(request, 'produto.html')

# view_product
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'edit_product.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponseRedirect('/')

# edit_product
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_product(request):
    if request.method == 'POST':
        product = Product.objects.get(id=request.POST.get('id'))
        if product:
            product.nome = request.POST.get('nome')
            product.telefone = request.POST.get('telefone')
            product.produto = request.POST.get('produto')
            product.entradas = request.POST.get('entradas')
            product.saidas = request.POST.get('saidas')
            product.quantidade = request.POST.get('quantidade')
            product.genero = request.POST.get('genero')
            product.status = request.POST.get('status')
            product.contexto = request.POST.get('contexto')
            product.save()
            return HttpResponseRedirect('/')

# delete_product
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect('/')

#lista dos produtos
def get_products(request):
    products = Product.objects.all().values()  # Obtém todos os produtos como um dicionário de valores
    return JsonResponse(list(products), safe=False)