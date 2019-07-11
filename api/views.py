from django.contrib import messages
from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import HttpResponseRedirect, render
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView,
)
from .pagination import CustomPagination
from .models import Bank, Branch
from .serializers import BranchSerializer
from .permissions import IsOwnerOrReadOnly, IsAuthenticated



class DetailView(ListAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get(self, request):
        ifsc = request.GET.get('ifsc','')
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False)


class ListView(generics.ListAPIView):
   model = Branch
   permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
   pagination_class = CustomPagination
   
   def get_queryset(self):
       queryset = Branch.objects.all()
       bank = self.request.query_params.get('bank_nam')
       city = self.request.query_params.get('city')
       all_branch = queryset.filter(bank__name__icontains=bank,city__iexact=city)
       return all_branch
       
   def get(self, request):
           all_branches=self.get_queryset()
           paginate_queryset = self.paginate_queryset(all_branches)
           serializer_classes = BranchSerializer
           serializer = serializer_classes(paginate_queryset, many=True)
           return self.get_paginated_response(serializer.data)
    





