from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Freelance', 'Freelance'),
    ('Temporary', 'Temporary'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey("Company", on_delete=models.CASCADE, null=True, blank=True)

    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name