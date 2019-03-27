from django.db import models
from django.test import TestCase
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# class Editor(models.Model):

#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()
#     #add NULL values to our database
#     phone_number = models.CharField(max_length = 10,blank =True)

#     def __str__(self):
#         return self.first_name

   
#     # define method
#     def save_editor(self):
#         self.save()


#     def delete_editor(self):
#         self.delete()

#     def update_editor(self):
#         self.update()
    
#     def display_editor(self):
#         self.display()

#     class Meta:
#         ordering = ['first_name']



#Database Relationships

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name



#One to Many relationships
 
class Article(models.Model):

    title = models.CharField(max_length =60)
    # post = models.TextField()
    post = HTMLField()
    # editor = models.ForeignKey(Editor)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)

    # Many to Many relationships
    tags = models.ManyToManyField(tags)

    # Adding a Timestamp
    pub_date = models.DateTimeField(auto_now_add=True)

    # update model ImageField
    # article_image = models.ImageField(upload_to = 'articles/')
    article_image = models.ImageField(upload_to='articles/', blank=True)

    # query database
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news


    @classmethod
    def days_news(cls,date):
            news = cls.objects.filter(pub_date__date = date)
            return news


# Testing Django Apps

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method
    def test_save_method(self):

        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

# Displaying Model Data

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

#NewsLetter-------------------------------

class NewsLetterRecipients(models.Model):

    name = models.CharField(max_length = 30)
    email = models.EmailField()



    




























