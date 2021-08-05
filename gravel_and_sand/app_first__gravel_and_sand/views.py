import datetime
import json

# для внешних ключей
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from app_first__gravel_and_sand.models import Products, Orders, Areas, OrderStatus
from app_first__gravel_and_sand.serializers import ProductsSerializer, ProductsSerializer_info, OrdersSerializer, \
    AreasSerializer


class ProductsViewSet(ModelViewSet):
    """ Для списков продуктов """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Все только для авторизованных пользователей
    # permission_classes = [IsAuthenticated]
    # Получать могут все, менять только авторизованные
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['product_id']
    search_fields = ['product_name', 'product_price', 'product_description']
    ordering_fields = ['product_price', 'product_name']


class AreasViewSet(ModelViewSet):
    """ Для списков районов """
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Все только для авторизованных пользователей
    # permission_classes = [IsAuthenticated]
    # Получать могут все, менять только авторизованные
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['area_id']
    search_fields = ['area_name', 'area_price', 'area_description']
    ordering_fields = ['area_price', 'area_name']


class OrdersViewSet(ModelViewSet):
    """ Для списков заказов """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Все только для авторизованных пользователей
    # permission_classes = [IsAuthenticated]
    # Получать могут все, менять только авторизованные
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['order_id']
    search_fields = ['order_date', 'order_name', 'order_phone']
    ordering_fields = ['order_id', 'order_date']


def new_order(request):
    """ Страница нового заказа """
    # передаем списки для вывода на форме
    context = {}

    # products = Products.objects.all()
    # products = ProductsSerializer_info(Products.objects.all(), many=True).data
    products = Products.objects.order_by('product_name')

    # areas = Areas.objects.all()
    # areas = AreasSerializer(Areas.objects.all(), many=True).data
    areas = Areas.objects.order_by('area_name')

    context = {
        'products': products,
        'areas': areas
    }
    # return render(request, 'order.html')
    return render(request, 'order/new_order.html', context={'data': context})
    #return render(request, 'order/new_order.html', {'products': products, 'areas': areas})


def save_new_order(request):
    """ Сохранение нового заказа (не стал работать через OrdersViewSet (POST))"""
    answer = 0

    # def myview(request):
    #    qs = Diary.get_entry(record.pk, request.user.pk)
    #    return qs

    # print(datetime.datetime.now(tz=timezone.utc))

    try:
        if request.method == "POST":

            #print(request.POST)
            #print('user.pk')
            #print(request.user.pk)
            #print('user.timezone')
            ## profile = request.user.get_profile()
            #profile = request.session
            #print(profile)
            #print('END Print')

            # для присвоения внешних ключей
            user = User.objects.get(id=request.user.pk)
            product = Products.objects.get(product_id=request.POST.get('select_product'))
            area = Areas.objects.get(area_id=request.POST.get('select_area'))
            # по умолчанию всегда новый
            status = OrderStatus.objects.get(status_id=2)

            order = Orders.objects.create(
                user_id=user,
                order_date=timezone.now(),
                #order_date=datetime.datetime.now(tz=timezone.utc),
                order_timezone=request.POST.get('input_timezone'),
                order_name=request.POST.get('input_name'),
                order_phone=request.POST.get('input_phone'),
                product_id=product,  # select_product
                order_count=request.POST.get('input_count_unit'),
                area_id=area,  # select_area
                order_address=request.POST.get('input_address'),
                order_date_delivery=request.POST.get('input_date_delivery'),
                order_time_delivery=request.POST.get('input_time_delivery'),
                order_description=request.POST.get('input_description'),
                order_cost=request.POST.get('input_all_cost'),
                status_id=status
            )

            #print('order')
            #print(order)

            now = timezone.now()
            #localtime = timezone.localtime(arg)
            print('now')
            print(now)

            answer = 200
            return HttpResponse("<h2>Сохранено</h2>")

        else:
            HttpResponseNotFound("<h2>method not found</h2>")
    except:
        answer = 500
        #print(request.error)

    return HttpResponse(status=answer)
    #return HttpResponse("<h2>Сохранено</h2>")


def auth(request):
    ''' Страница авторизации '''
    return render(request, 'oauth.html')
