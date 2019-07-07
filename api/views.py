from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, render
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
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

    def get_queryset(self):
        movies = Movie.objects.all()
        return movies


    def get(self, request):
        movies = self.get_queryset()
        paginate_queryset = self.paginate_queryset(movies)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def get(self, request, city, bank):
        branch_qset = Branch.objects.filter(
            city__iexact=city, bank__name__icontains=bank)
        serializer = BranchSerializer(branch_qset, many=True)
        return JsonResponse(serializer.data, safe=False)



