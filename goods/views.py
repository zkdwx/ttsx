from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 视图是一个函数
# 必须传一个参数 request 请求对象 里面有用户发送的请求信息 比如url地址和其他数据 参3需要传入到模板的数据
from goods.models import GoodsCategory, GoodsInfo


def index(request):
    # 查询商品的分类
    categories = GoodsCategory.objects.all()
    # 从每个分类中获取4个商品（每一类的最后4个最新的）
    for cag in categories:
        # 一对多关系 查询多的一方 会在一的这一方有一个属性 多的一方的 模型类名小写_set
        # order_by 是排序 这里是根据id反向排序（大->小）,[:4]获取结果里的前四个
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]

    # 获取购物车里的所有商品 cookies key:value 商品的id: 数量 cookies 存的都是字符串
    # 购物车商品的列表
    cart_goods_list = []
    # 购物车的商品总数量
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 商品id都是数字 通过判断来验证当前是不是商品数据 如果不是继续下次的循环
        if not goods_id.isdigit():
            continue
        # 获取当前遍历到的商品对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        # 把商品存放到列表里
        cart_goods_list.append(cart_goods)
        # 累加所有的商品的数量 注意goods_num是字符串 需要强制转成数字类型
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'index.html',
                  {'categories': categories, 'cart_goods_list': cart_goods_list, 'cart_goods_count': cart_goods_count})
