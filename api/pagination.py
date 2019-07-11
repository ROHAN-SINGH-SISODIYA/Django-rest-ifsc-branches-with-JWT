from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class CustomPagination(LimitOffsetPagination):
    PAGE_SIZE=2
    default_limit =5
    max_limit = 100