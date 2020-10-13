# coding: utf-8
import re

a = "<WSGIRequest: POST '/app_home/32/change_auth/'>"

print(a)
ret = re.findall(r'\'[\w/]+\'',a)
print(ret)