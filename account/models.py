from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from account.managers import UserManager


class Role(models.Model):
    title = models.CharField(max_length=255)
    access_lvl = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.title} [{self.access_lvl}]'


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    activation_code = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatars/default_avatar.jpg')
    role = models.ForeignKey(Role, related_name='roles', on_delete=models.CASCADE)

    is_active = models.BooleanField(
        _("active"),
        default=True,  # !!!!!!! email_verify
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        code = str(uuid4)
        self.activation_code = code
