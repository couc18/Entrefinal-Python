from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class ProfileViewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))  # Cambia 'profile' al nombre de tu URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')