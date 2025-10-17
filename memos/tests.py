from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Memo
from .forms import MemoForm

class MemoTests(TestCase):
    def setUp(self):
        # 테스트 사용자 생성
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # 테스트 메모 생성
        self.memo = Memo.objects.create(
            title='Test Memo',
            content='Test Content',
            author=self.user
        )
        # URL 패턴
        self.list_url = reverse('home')
        self.detail_url = reverse('memo_detail', args=[self.memo.id])
        self.create_url = reverse('memo_create')
        self.update_url = reverse('memo_update', args=[self.memo.id])
        self.delete_url = reverse('memo_delete', args=[self.memo.id])

    def test_memo_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memos/memo_list.html')
        self.assertContains(response, 'Test Memo')

    def test_memo_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memos/memo_detail.html')
        self.assertContains(response, 'Test Memo')
        self.assertContains(response, 'Test Content')

    def test_memo_create_view(self):
        # 로그인
        self.client.login(username='testuser', password='testpass123')
        
        # GET 요청 테스트
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memos/memo_form.html')
        
        # POST 요청 테스트
        response = self.client.post(self.create_url, {
            'title': 'New Memo',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)  # 리다이렉트
        self.assertTrue(Memo.objects.filter(title='New Memo').exists())

    def test_memo_update_view(self):
        # 로그인
        self.client.login(username='testuser', password='testpass123')
        
        # POST 요청 테스트
        response = self.client.post(self.update_url, {
            'title': 'Updated Memo',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.memo.refresh_from_db()
        self.assertEqual(self.memo.title, 'Updated Memo')

    def test_memo_delete_view(self):
        # 로그인
        self.client.login(username='testuser', password='testpass123')
        
        # POST 요청 테스트
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Memo.objects.filter(id=self.memo.id).exists())

    def test_memo_create_by_unauthorized_user(self):
        # 로그인하지 않은 사용자 테스트
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 302)  # 로그인 페이지로 리다이렉트

class MemoFormTests(TestCase):
    def test_memo_form_valid(self):
        form_data = {
            'title': 'Test Memo',
            'content': 'Test Content'
        }
        form = MemoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_memo_form_invalid(self):
        form_data = {
            'title': '',  # 제목은 필수 필드
            'content': 'Test Content'
        }
        form = MemoForm(data=form_data)
        self.assertFalse(form.is_valid())
