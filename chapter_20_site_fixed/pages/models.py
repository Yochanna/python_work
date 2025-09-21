from django.db import models                           # [import]

class Page(models.Model):                              # [model]
    title = models.CharField(max_length=200)           # [field-title]
    content = models.TextField()                       # [field-content]
    date_added = models.DateTimeField(auto_now_add=True)  # [timestamp]

    def __str__(self):
        return self.title
