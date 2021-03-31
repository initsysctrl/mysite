'''
Date: 2021-03-30 19:32:22
'''
from .models import Blog
from common.basehttp import SuccessResponse, ErrorResponse


def blog(request, page_id):
    if request.method == 'GET':
        try:
            blog = Blog.objects.get(id=page_id)
            data = {
                'title': blog.title,
                'author': blog.author,
                'content': blog.content,
            }
            return SuccessResponse(data=data)
        except Exception as e:
            print(e)
            return ErrorResponse(error_msg=str(e))
