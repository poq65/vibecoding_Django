from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def memo_list(request):
    return render(request, 'memos/memo_list.html')
