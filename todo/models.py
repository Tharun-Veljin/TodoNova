from django.db import models 

# Create your models here.
class task(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10, 
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], 
        default='medium'
    )


    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title



        