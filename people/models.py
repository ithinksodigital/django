from django.db import models


class Buddy(models.Model):
	name = models.CharField(max_length=30, verbose_name="Imię")
	last_name = models.CharField(max_length=30, verbose_name="Nazwisko")
	nickname = models.CharField(max_length=30, verbose_name="Ksywa", blank=True)
	knowage = models.TextField(verbose_name="Kilka zdań o...")
	tabu = models.TextField(verbose_name="Nie rozmawiaj o...")

	def __str__(self):
			return u'%s %s' % (self.name, self.last_name)