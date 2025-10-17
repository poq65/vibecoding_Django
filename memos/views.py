from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Memo
from .forms import MemoForm

def memo_list(request):
    memos = Memo.objects.all()
    return render(request, 'memos/memo_list.html', {'memos': memos})

@login_required
def memo_create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.author = request.user
            memo.save()
            messages.success(request, '메모가 생성되었습니다.')
            return redirect('memo_detail', pk=memo.pk)
    else:
        form = MemoForm()
    return render(request, 'memos/memo_form.html', {'form': form})

def memo_detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'memos/memo_detail.html', {'memo': memo})

@login_required
def memo_update(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if memo.author != request.user:
        messages.error(request, '다른 사용자의 메모는 수정할 수 없습니다.')
        return redirect('memo_detail', pk=pk)
    
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            messages.success(request, '메모가 수정되었습니다.')
            return redirect('memo_detail', pk=pk)
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memos/memo_form.html', {'form': form})

@login_required
def memo_delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if memo.author != request.user:
        messages.error(request, '다른 사용자의 메모는 삭제할 수 없습니다.')
        return redirect('memo_detail', pk=pk)
    
    if request.method == 'POST':
        memo.delete()
        messages.success(request, '메모가 삭제되었습니다.')
        return redirect('home')
    return render(request, 'memos/memo_confirm_delete.html', {'memo': memo})
