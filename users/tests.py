from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile
from .forms import UserRegisterForm

class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.test_user = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }

    def test_user_registration_view(self):
        # GET 요청 테스트
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

        # POST 요청 테스트 (유효한 데이터)
        response = self.client.post(self.register_url, self.test_user)
        self.assertEqual(response.status_code, 302)  # 리다이렉트
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_registration_form(self):
        form = UserRegisterForm(data=self.test_user)
        self.assertTrue(form.is_valid())

    def test_user_login(self):
        # 사용자 생성
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        # 로그인 테스트
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # 리다이렉트
        self.assertTrue(response.wsgi_request.user.is_authenticated)

class ProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_profile_creation(self):
        # 사용자 생성 시 프로필도 자동 생성되는지 테스트
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_profile_str_method(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(str(profile), 'testuser Profile')
