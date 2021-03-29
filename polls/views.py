'''
Date: 2021-03-23 10:20:15
'''

from django.core.serializers.json import Serializer
from django.db.models.fields.json import JSONField
from django.http.response import Http404
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Blog, Choice, Question
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from django.urls import reverse


class ResponseData(object):
    def __init__(self, code=1, data=None, error_msg=None):
        self.code = code
        self.data = data
        self.error_msg = error_msg

    # def to_json(self):
    #     return json.dumps(self, skipkeys=True, ensure_ascii=False)


def index(request):
    # 主页
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    data = [q.question_text for q in latest_question_list]
    obj = {
        'code': 1,
        'data': {
            'd1': [1, 2, 3, 4],
            'd2': '中文数据',
            'd3': 10086,
            'd4': {
                'd4-1': 1,
                'd4-2': '哈哈哈'},
            'd5': data},
        'error_msg': None}
    return JsonResponse(obj, content_type="application/json,charset=utf-8")
    # return HttpResponse(j_data, content_type="application/json,charset=utf-8")


def detail(request, question_id):
    # 细节
    try:
        question = Question.objects.get(pk=question_id)
        content = {'question': question}
    except Question.DoesNotExist:
        raise Http404("提问ID并不存在")
    return render(request=request, template_name='polls/detail.html', context=content)


def result(request, question_id):
    # 结果
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # 投票页


def blog(request, page_id):
    if request.method == 'GET':
        try:
            blog = Blog.objects.get(id=page_id)
        except:
            blog = {"author": "无", "title": "无", "content": "无"}
        return JsonResponse(blog)
