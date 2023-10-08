from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


class Location(models.Model):
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    name = models.CharField(
        verbose_name="Название локации",
        max_length=64,
    )

    address = models.CharField(
        verbose_name="Фактический адрес локации",
        max_length=300,
        blank=True,
    )

    slug = models.SlugField(
        verbose_name="Строка в адресе",
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.name


class Regularity(models.Model):
    class Meta:
        verbose_name = "Регулярность"
        verbose_name_plural = "Регулярность"

    name = models.CharField(
        verbose_name="Название",
        max_length=32,
    )

    def __str__(self):
        return self.name


class Ticket(models.Model):
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    header = models.CharField(
        verbose_name="Заголовок",
        max_length=128,
    )

    text = models.TextField(
        verbose_name="Текст",
    )

    location = models.ForeignKey(
        Location,
        related_name="tickets_location",
        verbose_name="Место",
        on_delete=models.PROTECT,
    )

    regularity = models.ForeignKey(
        Regularity,
        related_name="tickets_regularity",
        verbose_name="Регулярность",
        on_delete=models.PROTECT,
    )

    manager = models.CharField(
        verbose_name="Ответственный",
        max_length=64,
    )

    contact = models.CharField(
        verbose_name="Контакт в telegram",
        max_length=64,
    )

    updated = models.DateField(
        verbose_name="Опубликовано",
        auto_now=True,
    )

    validated = models.BooleanField(
        verbose_name="Проверено",
        default=False,
    )

    rejected = models.BooleanField(
        verbose_name="Отклонено",
        default=False,
    )

    owner = models.ForeignKey(
        "auth.User",
        verbose_name="Владелец",
        related_name="tickets_owner",
        on_delete=models.PROTECT,
        default=1,
    )

    def __str__(self):
        return self.header


class ToValidate(models.Model):
    class Meta:
        verbose_name = "На валидации"
        verbose_name_plural = "На валидации"

    id = models.ManyToManyField(
        Ticket,
        verbose_name="Объявления на проверке",
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Время последнего обновления",
    )
