from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    # category_id = models.IntegerField(primary_key=True, db_index=True)
    category_name = models.CharField(max_length=45)
    # meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('data:corporation_in_category', args=[self.name])


class Corporation(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    corp_code = models.CharField(max_length=6)
    name = models.CharField(max_length=45, db_index=True)
    sales = models.IntegerField(default=0)
    op_profit = models.IntegerField(default=0)
    net_income = models.IntegerField(default=0)
    op_margin = models.FloatField(default=0)
    net_profit_margin = models.FloatField(default=0)
    roe = models.FloatField(default=0)
    debt_ratio = models.FloatField(default=0)
    quick_ratio = models.FloatField(default=0)
    reserve_ratio = models.FloatField(default=0)
    eps = models.IntegerField(default=0)
    per = models.FloatField(default=0)
    bps = models.IntegerField(default=0)
    pbr = models.FloatField(default=0)
    current_stock = models.PositiveIntegerField(default=0)
    market_cap = models.PositiveIntegerField(default=0)
    quarter = models.TextField(max_length=45)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='corporations')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['corp_code', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('data:corporation_detail', args=[self.name])
