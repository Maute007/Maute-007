from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from App import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', (views.index), name='index'),
    #homepage
    path('home/', login_required(views.home), name='home'),
    #adicionar produto
    path('add_product', login_required(views.add_product), name='add_product'),
    #ver o produto individual
    path('product/<str:product_id>', login_required(views.view_product), name='view_product'),
    #listar total de produto
    path('get_products/', views.get_products, name='get_products'),
    #editar produto
    path('edit_product', login_required(views.edit_product), name='edit_product'),
    #apagar o produto
    path('delete_product/<str:product_id>', login_required(views.delete_product), name='delete_product'),
    # Login/Logout
    path('login/', include('django.contrib.auth.urls'), name='login'),

]

