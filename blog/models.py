from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.urls import reverse
from django.contrib.auth.models import User

# models for post   

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = HTMLField()
    create_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media', null=True)
    # approved_comment = models.BooleanField(default=False)
    # publish_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-create_date"]

    def get_absolute_url(self):
        return reverse("blog_detail_page", kwargs={"pk": self.pk})
    

    # Python code to update the publish date of an object and save it

    # def publish(self):
    #     self.publish_date = timezone.now()
    #     self.save()

    # # This code defines a method in the model class that filters and returns only the approved comments.

    # def approve_comments(self):
    #     return self.comments.filter(approved_comment=True)
    

    def __str__(self):
        return self.title
    
# models for comment

# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     create_date = models.DateTimeField(default=timezone.now())
#     approved_comment = models.BooleanField(default=False)


#     # This code defines a method in the model class that filters and returns only the approved comments.
#     def approve(self):
#         self.approved_comment = True
#         self.save()


#     def get_absolute_url(self):
#          pass
#         # return reverse("model_detail", kwargs={"pk": self.pk})
    

#     def __str__(self):
#         return self.text

