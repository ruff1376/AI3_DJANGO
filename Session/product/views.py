from django.shortcuts import redirect, render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'product/index.html')

# 상품 목록
def product_list(request):
    # 상품 목록 요청
    products = Product.objects.all()    # Product 모델에서 모든 상품을 가져옵니다.
    return render(request, 'product/product_list.html', {'products': products})

# 장바구니 목록
def cart_list(request):
    # 세션에서 장바구니 정보를 가져옵니다.
    # { '상품ID': 수량, ... }
    # { '1': 2, '2': 1, ...}
    cart = request.session.get('cart', {})
    
    # 상품ID로 상품 정보를 가져옵니다.
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    
    # 장바구니 정보를 상품 정보와 함께 매핑합니다.
    carts = []
    for product in products:
        quantity = cart.get(str(product.id), 0)
        total_price = product.price * quantity
        carts.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price
        })
    
    return render(request, 'product/cart_list.html', {'carts': carts})

# 장바구니 추가
def cart_add(request, product_id):
    # 세션에서 장바구니 정보를 가져옵니다.
    cart = request.session.get('cart', {})
    
    # 상품ID가 이미 장바구니에 있는지 확인합니다.
    if str(product_id) in cart:
        cart[str(product_id)] += 1  # 수량을 증가시킵니다.
    else:
        cart[str(product_id)] = 1  # 새로 추가합니다.
    
    # 세션에 장바구니 정보를 저장합니다.
    request.session['cart'] = cart
    
    # product 앱의 cart_list(name) 뷰로 리다이렉트합니다.
    return redirect('product:cart_list')

# 장바구니 삭제
def cart_remove(request, product_id):
    # 세션에서 장바구니 정보를 가져옵니다.
    cart = request.session.get('cart', {})
    
    # 상품ID가 장바구니에 있는지 확인합니다.
    if str(product_id) in cart:
        del cart[str(product_id)]   # 해당 상품을 삭제합니다.

    # 세션에 장바구니 정보를 저장합니다.
    request.session['cart'] = cart
    
    # product 앱의 cart_list(name) 뷰로 리다이렉트합니다.
    return redirect('product:cart_list')
