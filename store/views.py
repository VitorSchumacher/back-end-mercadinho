from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import CategorySerializer , UserSerializer, OrderSerializer, ProductsSerializer, CustomerSerializer


from .models import Category, Order, Products, Customer

class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        category = Category()
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class UserView(APIView):
    def get(self, request):
        user = User.objects.all()
        print(user)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        user = User()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class OrderView(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        order = Order()
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class ProductView(APIView):
    def get(self, request):
        product = Products.objects.all()
        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        product = Products()
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else: 
            return Response(serializer.errors, status=400)

class CustomerView(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        customer = Customer()
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class OneProductView(APIView):
    def get(self, request):
        print(request)
        product = Products.get_products_by_id(request.query_params.get('ids'))
        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data, status=200)

class CategoriesView(APIView): 
    def get(self, request):
        print(request)
        product = Products.get_all_products_by_categoryid(request.query_params.get('category_id'))
        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data, status=200)