from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# import random

class MyAccountManager(BaseUserManager):
	def create_user(self, first_name, last_name, email, password=None):
		if not email:
			raise ValueError('Users must have an email address.')
		if "@" not in email and ".com" not in email:
			raise ValueError("Invalid email input")
		if len(password) < 8:
			raise ValueError("Password must contain at least 8 characters")

		user = self.model(
			first_name=first_name,
            last_name=last_name,
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, first_name, last_name, email, password):
		user = self.create_user(
			first_name=first_name,
            last_name=last_name,
			email=self.normalize_email(email),
			password=password
		)
		user.is_admin = True
		user.is_superuser = True
		user.is_staff = True
		user.is_active = True

		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
    # =====================================
    # General fields
    # =====================================
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=200)
    # userId = models.CharField(max_length=13, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='media/profile-pics', blank=True, null=True)            

        
    # =====================================
    # General default fields
    # =====================================
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



    # def generate_userId():
    # 	getNum = ''.join(random.choice('0123456789') for i in range(10))
    # 	getAlpha = ''.join(random.choice('ABCEFGHIJKLMNOPQRSTUVWXYZ') for i in range(2))
    # 	getUserId = getAlpha + getNum

    # 	while User.objects.filter(userId=getUserId).exists():
    # 		generate_userId()
    # 	return getUserId