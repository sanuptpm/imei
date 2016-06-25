from django.test import TestCase, Client
from employee.views import *
from django.core.urlresolvers import resolve, reverse
from employee.models import Profile
from employee.forms import ProfileForm
# Create your tests here.

class Test(TestCase):

    def test_login(self):
        #Check login Success/Failed
        user = Profile(imei='444', mac='555')
        user.save()
        response = self.client.post(reverse('login'),{'imei':'444', 'mac':'555'})
        self.assertEqual(response.status_code, 200)


    def test_form_required(self):
        #Check forms field required=True
        form = ProfileForm()
        self.assertTrue(form.fields['imei'].required)
        self.assertTrue(form.fields['mac'].required)

    def test_next_redirect(self):
        #Check next redirect path
        c = Client() 
        response = c.get('/login_test', follow=True)
        print response.redirect_chain
        response = c.get('/login', follow=True)
        print response.redirect_chain
        response = c.get('/', follow=True)
        print response.redirect_chain
        response = c.get('/employee', follow=True)
        print response.redirect_chain
        response = c.get('/employees', follow=True)
        print response.redirect_chain
        response = c.get('/logout', follow=True)
        print response.redirect_chain

    def test_urls(self):
        #Check for url pointing to correct view 
        response = self.client.get('/')
        self.assertEqual(response.resolver_match.func, index)
        response = self.client.get('/employee')
        self.assertEqual(response.resolver_match.func, add_employee)
        response = self.client.get('/employees')
        self.assertEqual(response.resolver_match.func, list_employee)
        response = self.client.get('/login')
        self.assertEqual(response.resolver_match.func, login_view)
        response = self.client.get('/login_test')
        self.assertEqual(response.resolver_match.func, login_test)
        response = self.client.get('/logout')
        self.assertEqual(response.resolver_match.func, logout_view)

    def test_logout(self):
        #Check logout success
        response = self.client.get('/logout')
        response.status_code
        self.assertEqual(response.status_code, 200)