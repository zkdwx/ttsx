from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# 视图是一个函数
# 必须传一个参数 request 请求对象 里面有用户发送的请求信息 比如url地址和其他数据 参3需要传入到模板的数据
def index(request):
    return render(request, 'index.html', {'name': '张三', 'age': '20'})
