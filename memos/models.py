from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Memo(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memos', verbose_name='작성자')

    class Meta:
        ordering = ['-created_at']
        verbose_name = '메모'
        verbose_name_plural = '메모들'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('memo_detail', kwargs={'pk': self.pk})
