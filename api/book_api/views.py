from django.shortcuts import render
from django.http import JsonResponse
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# *************************************************************
@api_view(['GET', 'POST'])
def books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        #books_list = list(books.values())
        #return JsonResponse({"books": books_list})
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save otomatik olarak create çalıştırır.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
# *************************************************************

@api_view(['GET','PUT','DELETE'])
def book_id(request, id):
    try:
        books = Book.objects.get(pk=id)
    except:
        content = {"error":"Eşleşen bir kayıt bulunamadı"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BookSerializer(books)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = BookSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)