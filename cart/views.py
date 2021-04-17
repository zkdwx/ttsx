from django.shortcuts import render, redirect

# Create your views here.
from goods.models import GoodsInfo


def add_cart(request):
    '''添加到购物车'''
    # 获取传过来的商品id
    goods_id = request.GET.get('id', '')
    if goods_id:
        # 获取上一个页面的地址
        prev_url = request.META['HTTP_REFERER']
        print(prev_url)
        # 获取response
        response = redirect(prev_url)
        # 把商品存到cookies里
        # 获取之前商品在购物车的数量
        goods_count = request.COOKIES.get(goods_id)
        # 如果之前购物车里有商品，那么在之前的数量上加1
        # 如果之前没有，那么就添加1
        if goods_count:
            goods_count = int(goods_count) + 1
        else:
            goods_count = 1
        # 把商品id和数量保存到cookie
        response.set_cookie(goods_id, goods_count)
    return response


def show_cart(request):
    '''显示购物车商品'''
    # 获取购物车商品列表
    cart_goods_list = []
    # 购物车商品的总数量
    cart_goods_count = 0
    # 购物车总价
    cart_goods_money = 0

    # 从cookies获取数据 遍历cookies goods_id:cart_goods
    for goods_id, goods_num in request.COOKIES.items():
        # 判断id是不是数字，来确定是不是商品数据
        if not goods_id.isdigit():
            continue
        # 根据id获取商品对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 把商品数量存放到对应的对象里
        cart_goods.goods_num = goods_num
        # 当前商品价格小计
        cart_goods.total_money = int(goods_num) * cart_goods.goods_price
        # 把商品添加到列表
        cart_goods_list.append(cart_goods)
        # 累加所有商品数量
        cart_goods_count += int(goods_num)
        # 累加所有商品总价
        cart_goods_money += int(goods_num) * cart_goods.goods_price
    return render(request, 'cart.html', {'cart_goods_list': cart_goods_list,
                                             'cart_goods_count': cart_goods_count,
                                             'cart_goods_money': cart_goods_money})
