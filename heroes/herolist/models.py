from django.db import models


class Hero(models.Model):
    generic_name = models.CharField(max_length=15, blank=False, null=False, unique=True)
    display_name = models.CharField(max_length=45, blank=False, null=False)

    HERO_TYPE = (
        ('INT', 'Intelligence'),
        ('AGI', 'Agility'),
        ('STR', 'Strength')
    )

    hero_type = models.CharField(max_length=3,choices=HERO_TYPE, blank=False, null=False, db_index=True)
    short_desc = models.CharField(max_length=255, blank=True, null=True)
    image_filename = models.CharField(max_length=255, blank=False, null=False, default='default.jpg')

    # Some methods to get answers about heroes
    def __str__(self):
        return self.generic_name+' - '+self.display_name+' ('+self.hero_type+')'

    @property
    def is_strength(self):
        return self.hero_type == 'STR'

    @property
    def is_agility(self):
        return self.hero_type == 'AGI'

    @property
    def is_int(self):
        return self.hero_type == 'INT'


class Synergy(models.Model):
    hero = models.OneToOneField(Hero, primary_key=True, related_name='rel_hero')
    counters = models.ManyToManyField(Hero, blank=False, related_name='rel_hero_foes')
    friends = models.ManyToManyField(Hero, blank=False, related_name='rel_hero_friends')

    def __str__(self):
        return self.hero.display_name+' ('+self.hero.hero_type+')'
