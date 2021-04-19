'''
Date: 2021-03-30 19:32:22
'''
from django.test import TestCase

# Create your tests here.
import sys

import sys

query = sys.argv[1]
x = query.split(' ')
# print(type(x))
a = None
b = None
a = x[0]
b = x[1] if (len(x) >= 2) else None
#############简书##############
if a == 'js' and b:
    result = "https://www.jianshu.com/search?q=%s&page=1&type=note" % b
elif a == 'js' and not b:
    result = 'https://www.jianshu.com/u/64f259fce8f5'
#############思否##############
elif a == 'sf' and b:
    result = 'https://segmentfault.com/search?q=%s' % b
elif a == 'sf'and not b:
    result = 'https://segmentfault.com/'

#############思否##############
elif a == 'sf' and b:
    result = 'https://segmentfault.com/search?q=%s' % b
elif a == 'sf'and not b:
    result = 'https://segmentfault.com/'
#############bilibili##############
elif a == 'bl' and b:
    result = 'https://search.bilibili.com/all?keyword=%s&from_source=nav_search_new' % b
elif a == 'bl'and not b:
    result = 'https://www.bilibili.com/'

#############bilibili##############
elif a == 'zh' and b:
    result = 'https://search.bilibili.com/all?keyword=%s&from_source=nav_search_new' % b
elif a == 'zh'and not b:
    result = 'https://www.bilibili.com/'


sys.stdout.write(result)
