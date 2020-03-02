from django.shortcuts import render,HttpResponse

# Create your views here.


def test_view(request):
    print("执行业务逻辑中，计算第一次多少钱。")
    return HttpResponse("500一次")

def index_view(request):
    return  render(request,'index.html')