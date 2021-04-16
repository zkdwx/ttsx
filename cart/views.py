from django.shortcuts import render, redirect


# Create your views here.

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
