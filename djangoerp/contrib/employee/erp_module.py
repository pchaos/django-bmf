#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from djangoerp.sites import site

from .models import Employee
from .views import EmployeeCreateView

site.register(Employee, **{
    'create': EmployeeCreateView,
})
