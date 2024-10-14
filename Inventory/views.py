from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class ProductsView(APIView):

#without using serializers
    # def get(self, request):  #here i get objects after post is completed. i can take this code using for loop and iterate one by one.

    #     all_products = Products.objects.all()

    #     products_data = []

    #     for product in all_products:


    #         single_product = {
    #             "id": product.id,
    #             "product_name":product.product_name,
    #             "code":product.code,
    #             "price":product.price,
    #             "category_reference_id" = product.category_reference_id

    #         }

    #         products_data.append(single_product)
            
    #     return Response(products_data)


#using serializers

    def get(self, request):  #here i get objects after post is completed. i can take this code using for loop and iterate one by one.

        all_products = Products.objects.all()

        serialized_products = Products_Serializers(all_products, many=True).data

        print(serialized_products)
            
        return Response(serialized_products)


    # def post(self, request): #in this place i created new objects

    #     # print(request.data)
    #     new_product = Products(
    #         product_name = request.data["product_name"],

    #         code = request.data["code"], 
    #         price = request.data["price"], 
    #         category_reference_id = request.data['category_reference_id'] #this line of code is manually created so that i can used  category_reference_id, it shows in mysql same column name so that i defined same here. inside of request.data['category_reference_id' = this is postman code why i use '_id' because same way to define the code what shows in mysql].
    #                         )
    #     new_product.save()

    #     return Response("Data Saved") 

    #using serializers

    def post(self, request): #in this place i created new objects using serializers 

        # print(request.data)
        new_product = Products_Serializers(data = request.data)

        if new_product.is_valid():

            new_product.save()

            return Response("Data Saved")
        
        else:

            return Response(new_product.errors) 

    
class ProductsViewById(APIView): #here i used single object to viewthe values 

#without serializers
    # def get(self, request, id):

    #     Product = Products.objects.get(id=id)

    #     # print(Product)
    #     single_product = {
    #             "id": Product.id,
    #             "product_name":Product.product_name,
    #             "code":Product.code,
    #             "price":Product.price,
    #             "category_reference_id" = product.category_reference_id #idhu manual ah use pannumbothu mysql la vara column name madhiriye tharanum so that ipdi pannitu irukken.
    #         }

    #     return Response(single_product)
    

    #using serializers

    def get(self, request, id):

        Product = Products.objects.get(id=id)

        # print(Product)
        single_product = Products_Serializers(Product).data

        return Response(single_product)
  

    #this function used to update the objects

    #without serializers
    # def patch(self, request, id):

    #     Product = Products.objects.filter(id=id)

    #     print(request.data)

    #     Product.update(product_name = request.data["product_name"],
    #                         code = request.data["code"], price = request.data["price"],
    #                         category_reference_id = request.data['category_reference_id']) #here the user want to make changesall of them so that i can use this all.

    #     return Response("updated")

    #using serializers
    def patch(self, request, id):

        Product = Products.objects.get(id=id)

        new_values = Products_Serializers(Product, data=request.data, partial = True)

        if new_values.is_valid():

            new_values.save()

            return Response("updated")
        else:

            return Response(new_values.errors)
    
    
    #this function used to delete the objects
     
    def delete(self, request, id):

        product = Products.objects.get(id = id)

        product.delete()

        return Response("Deleted")
     

class CategoryView(APIView):

    def get(self, request):

        all_category = Category_Serializer(Category.objects.all(), many=True)

        return Response(all_category)
    
    def post(self, request):

        new_category = Category_Serializer(data=request.data)
        print(request.data)

        if new_category.is_valid():

            new_category.saved()

            return Response("Data Saved")
        
        else:

            return Response(new_category.errors)
        
class CategoryViewById(APIView):

    def delete(self, request, id):

        category = Category.objects.get(id=id)

        category.delete()
        
        return Response("Deleted")