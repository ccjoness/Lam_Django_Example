from django.db import models
from django.utils.text import slugify


class ToDoList(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def first_char(self):
        return self.name[0]


class Item(models.Model):
    todo_list = models.ForeignKey('ToDoList', related_name='items', on_delete=models.CASCADE)
    description = models.TextField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.todo_list.name, self.description)
