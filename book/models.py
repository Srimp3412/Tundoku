from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=50) #タイトルの文字数はこれくらいで十分
    isbn = models.IntegerField()
    author = models.CharField(max_length=20)
    description = models.TextField(null=True)
    book_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


