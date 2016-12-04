"""
"""
from django.contrib import auth
from django.http import (
    Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.template import loader
from django.template.context_processors import csrf
from django.urls import NoReverseMatch, reverse
from django.utils import six
from django.utils.encoding import force_text

class LoginProcess:

    def login(request):
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)

    def auth_view(request):
        username = request.Post.get('username','')  # if the username doesnt exist an empty string should return an invalid variable
        password = request.Post.get('password' '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
        return HttpResponseRedirect( '/accounts/loggedin' )

        else:
        return HttpResponseRedirect('accounts/invalid')


    def loggedin(request):
        return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

    def invalid_login(request):
        return render_to_response('invalid_login.html')

    def logout(request):
        auth.logout(request)
        return render_to_response('logout.html')


import unittest

username = username
password = password


class loginProcess ( unittest.TestCase ):
    def test_login ( self ):
        self.assertTrue ( username ( valid ) , True )


if __name__ == '_main':
    unittest.main ( )

-----------------------------------------------

class login:
    def__init__(self, id, pas):
        self.id = id
        self.pas = pas

    def check(self, id, pas):
        print self.id == id and self.pas == pas:
            print= "Login successful"

log = login("admin", "admin")
log.check(rawinput("Enter Login ID:")),
          raw_input("Enter password:"))
