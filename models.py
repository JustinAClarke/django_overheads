"""
    Django Overheads Justin Fuhrmeister-Clarke, a Church Overhead Presentor Submission System.
    Copyright (C) 2018  Justin Fuhrmeiser-Clarke <justin@fuhrmeister-clarke.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """

from django.db import models

# Create your models here.

class Church(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=200)
    service_date = models.DateField('Service Date')
    submission_date = models.DateField('Submission Date')
    description = models.TextField(null=True)
    church = models.OneToOneField(Church)
    submission_file = models.ImageField(upload_to='overheads/upload')
    
    def __str__(self):
        return self.title

