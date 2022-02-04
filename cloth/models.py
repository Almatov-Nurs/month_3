from django.db import models

class CustomerCL(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"Customer: {self.name}"

class TagCL(models.Model):
    tags_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tags_name

class ProductCL(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.product_name

class StatusOrderCL(models.Model):
    STATUS_ORDER = (
        ("Заказ готовится","Заказ готовится"),
        ("Заказ на пути","Заказ на пути"),
        ("Заказ доставлен","Заказ доставлен")
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCL, on_delete=models.CASCADE, related_name='product_order')
    status_choice = models.CharField(max_length=100, choices=STATUS_ORDER)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer.name