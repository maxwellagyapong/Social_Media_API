from rest_framework import pagination

class PostListPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 20
    
    
class CommentListPagination(pagination.CursorPagination):
    page_size = 3
    ordering = 'date_commented'
    
    
class ReplyListPagination(pagination.CursorPagination):
    page_size = 3
    ordering = 'date_created'
    
    
class GroupListPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 20
    offset_query_param = 'start'