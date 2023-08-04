from django.db import models

# Create your models here.
class Invate(models.Model):
    is_multi = models.BooleanField(verbose_name="Для нескольких человек", default=True)
    is_men = models.BooleanField(verbose_name="Для музчины", default=True)
    name = models.CharField(verbose_name="Для кого", max_length=255, blank=False)

    def __str__(self) -> str:
        return "Приглошение для " + self.name.__str__()

    class Meta:
        verbose_name = "Приглошение"
        verbose_name = "Приглошения"