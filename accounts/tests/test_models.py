from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile

class ProfileModelTest(TestCase):
    def setUp(self):
        # Crea un usuario para las pruebas
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(
            user=self.user,  # Usa la instancia del usuario creado
            # otros campos necesarios...
        )

    def test_profile_creation(self):
        self.assertIsInstance(self.profile, Profile)
        self.assertEqual(self.profile.user.username, 'testuser')

    def test_profile_string_representation(self):
        self.assertEqual(str(self.profile), f'{self.profile.user.username} Profile')