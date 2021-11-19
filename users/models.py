from django.db import models


USER_TYPE = (
    ('sender', "Sender"),
    ('transporter', "Transporter"),
)


class Account(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    user_type = models.CharField(max_length=50, choices=USER_TYPE, default='sender')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.TextField()
    address = models.TextField()
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.email
