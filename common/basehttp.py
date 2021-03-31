'''
Date: 2021-03-30 19:41:00
'''
from django.http import JsonResponse


class SuccessResponse(JsonResponse):
    def __init__(self, data):
        data = {'code': 1, 'data': data, 'message': None}
        JsonResponse.__init__(
            self, data, content_type="application/json,charset=utf-8")


class ErrorResponse(JsonResponse):
    def __init__(self, data=None, error_msg='请求错误'):
        data = {'code': 0, 'data': data, 'message': error_msg}
        JsonResponse.__init__(
            self, data, content_type="application/json,charset=utf-8")
