from django.test import TestCase
from accounts.forms import ProfileUpdateForm

class ProfileFormTest(TestCase):
    def test_invalid_form(self):
        form_data = {
            # Aquí podrías dejar un campo vacío o incorrecto para que el formulario sea inválido
            'name': '',  # Supongamos que 'name' es un campo requerido
            # Agrega otros campos necesarios, pero asegurate de que al menos uno sea inválido
        }
        form = ProfileUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())  # Debe ser falso
        self.assertIn('This field is required.', str(form.errors))  # Verifica que haya un error específico