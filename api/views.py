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

    def get(self, request, ifsc):
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False)


class ListView(ListAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    pagination_class = CustomPagination

    def get(self, request, city, bank):
        serializer_classes = BranchSerializer
        all_branch = Branch.objects.filter(city__iexact=city, bank__name__icontains=bank)
        paginate_queryset = self.paginate_queryset(all_branch)
        serializer = serializer_classes(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)






