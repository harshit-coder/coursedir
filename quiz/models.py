from django.db import models
import random
from random import shuffle

LEVEL_CHOICES = (

    ('BEGINNERS', 'BEGINNERS'),
    ('INTERMEDIATE', 'INTERMEDIATE'),
    ('ADVANCE', 'ADVANCE')
)


class quiz(models.Model):
    name = models.CharField(
        max_length=600, verbose_name="Enter  the categroy name")
    no_of_quest = models.IntegerField(
        verbose_name="Enter the no. of questions in this quiz")
    time = models.IntegerField(
        verbose_name="Enter the time  (only minutes) for quiz")
    basic_min_score = models.IntegerField(
        verbose_name="minimum no. of correct answers required for Beginners courses")
    basic_max_score = models.IntegerField(
        verbose_name="maximum no. of correct answers required for Beginners courses")
    medium_min_score = models.IntegerField(
        verbose_name="minimum no. of correct answers required for Intermediate courses")
    medium_max_score = models.IntegerField(
        verbose_name="maximum  no. of correct answers required for Intermediate courses")
    advance_min_score = models.IntegerField(
        verbose_name="minimum no. of correct answers required for Advance courses")
    advance_max_score = models.IntegerField(
        verbose_name="maximum no. of correct answers required for Advance courses")

    def __str__(self):
        return self.name

    def get_questions(self):
        qu = list(self.question_set.all())
        print(qu)
        random.shuffle(qu)
        return qu[:self.no_of_quest]

    class Meta:
        verbose_name_plural = 'Categories'


class Question(models.Model):
    question_text = models.TextField(verbose_name="Enter the question")
    quiz = models.ForeignKey(
        'quiz', on_delete=models.CASCADE, verbose_name="Select the category")

    def __str__(self):
        return str(self.question_text)


    def save(self, *args, **kwargs):
        self.question_text = "\n".join(self.question_text.split())
        self.question_text = "\r".join(self.question_text.split())
        self.question_text = "\t".join(self.question_text.split())
        self.question_text = "   ".join(self.question_text.split())
        self.question_text = "  ".join(self.question_text.split())
        self.question_text = " ".join(self.question_text.split())
        super(Question, self).save(*args, **kwargs)

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Question'


class Answer(models.Model):
    answer_text = models.CharField(
        max_length=4000, verbose_name="Enter the answers")
    correct_answer = models.BooleanField(
        verbose_name="Tick the one which is correct")
    question_text1 = models.ForeignKey('question', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.answer_text)


class course(models.Model):
    level = models.CharField(
        max_length=500, choices=LEVEL_CHOICES, default="BASIC", verbose_name="Select the level of course")
    course_name = models.CharField(
        max_length=500, verbose_name="Enter the course name")
    category = models.ForeignKey(
        'quiz', on_delete=models.CASCADE, verbose_name="Select the category of course")
    course_link = models.URLField(verbose_name="Add the course weblink url")

    course_imageurl = models.URLField(
        verbose_name="Add the course thumbnail URL", blank=True, null=True)
    course_image = models.ImageField(upload_to="images/",
                                     verbose_name="OR  upload the thumbnail", null=True,blank=True)
    course_price = models.CharField(
        max_length=200, verbose_name="Enter the price if course is paid otherwise leave it empty", blank=True,
        null=True)
    course_company = models.CharField(
        max_length=200, verbose_name="Enter the mai site owner name like coursera, khan academy, udemy, swayam etc",
        blank=True, null=True)

    def __str__(self):
        return str(self.course_name)

    class Meta:
        verbose_name = 'Course'