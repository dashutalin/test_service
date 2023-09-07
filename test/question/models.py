from django.db import models


class Set(models.Model):
    title = models.CharField('название', max_length=100)
    desc = models.TextField('описание')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'набор'
        verbose_name_plural = 'Наборы'

    def __str__(self):
        return self.title


class Group(models.Model):
    title = models.CharField('название', max_length=100)
    desc = models.TextField('описание')
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.TextField('вопрос')
    group = models.ForeignKey(Group, on_delete=models.CASCADE,
                              verbose_name='название теста',)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


class Answer(models.Model):
    ans = models.CharField('ответ', max_length=100)
    is_right = models.BooleanField('правильный ответ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 verbose_name='вопрос')

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.ans
