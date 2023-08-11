from django.db import models
from django.utils.crypto import get_random_string

def slug_save(obj):
    """ A function to generate a 5 character slug and see if it has been used and contains naughty words."""
    if not obj.slug: # if there isn't a slug
        obj.slug = get_random_string(15) # create one
        slug_is_wrong = True  
        while slug_is_wrong: # keep checking until we have a valid slug
            slug_is_wrong = False
            other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
            if len(other_objs_with_slug) > 0:
                # if any other objects have current slug
                slug_is_wrong = True
            naughty_words = ['']
            if obj.slug in naughty_words:
                slug_is_wrong = True
            if slug_is_wrong:
                # create another slug and check it again
                obj.slug = get_random_string(5)

# Create your models here.
class Invate(models.Model):
    is_multi = models.BooleanField(verbose_name="Для нескольких человек", default=True)
    is_men = models.BooleanField(verbose_name="Для музчины", default=True)
    name = models.CharField(verbose_name="Для кого", max_length=255, blank=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        """ Add Slug creating/checking to save method. """
        slug_save(self) # call slug_save, listed below
        super(Invate, self).save(*args, **kwargs)
# ...


    def __str__(self) -> str:
        return "Приглошение для " + self.name.__str__()

    class Meta:
        verbose_name = "Приглошение"
        verbose_name = "Приглошения"