from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class CustomPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 100