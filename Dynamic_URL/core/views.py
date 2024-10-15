from django.shortcuts import render

def index(request):
    return render(request,'core/index.html')

def product(request,id):
    return render(request,'core/product.html',{'id': id})

# def product(request,id,sub_id):
#     return render(request,'core/product.html',{'id': id})