from django.db import models

# Create your models here.
class Program(models.Model):
	program_id = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.program_id

class Word_count(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	word_text = models.CharField(max_length=200)
	cnt = models.IntegerField(default=0)