from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	adress = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_provience = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	webisite = models.URLField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Author(models.Model):
	first_name = models.CharField(max_length=30, verbose_name="Imię")
	last_name = models.CharField(max_length=50)
	email = models.EmailField(blank=True, verbose_name='e-mail')

	def __str__(self): 
		return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.title



