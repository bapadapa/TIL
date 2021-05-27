from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse ,QueryDict
from .models import Products
from .forms import ProductForm


# Create your views here.
def Product_List(request):
    # 저장
    if request.method == 'POST':
        form =ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            post = form.cleaned_data
            return JsonResponse(post)
        return JsonResponse(form.errors)
    else:
        return JsonResponse(Products.objects.all())


def Product_detail(request,pk):
    product = get_object_or_404(Products,pk =pk)
    # 글 갱신
    if request.method =='PUT':
        put_data =QueryDict(request.body)
        form =ProductForm(put_data,instance=product)
        if form.is_valid():
            product = form.save()
            return JsonResponse(product)       
        return JsonResponse(form.errors)
    # 글 삭제
    elif request.method =='DELETE':
        product.delete()
        return HttpRequest()
    # 글 응답
    else:
        return JsonResponse(product)

