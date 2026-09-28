from django.db.migrations import serializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

import contacts
from .serializers import Contact, ContactSerializer
from .models import Contact


class ContactList(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


class ContactCreate(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, )

class ContactDetail(APIView):
    def get(self, request, pk):
        contact = get_object_or_404(Contact, id=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

class ContactDelete(APIView):
    def delete(self, request, pk):
        contact = get_object_or_404(Contact, id=pk)
        contact.delete()
        return Response({'deleted': True})

class ContactUpdate(APIView):
    def put(self, request, pk):
        contact = get_object_or_404(Contact, id=pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ContactPatch(APIView):
    def patch(self, request, pk):
        contact = get_object_or_404(Contact, id=pk)
        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
