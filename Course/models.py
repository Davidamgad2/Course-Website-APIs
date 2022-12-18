from wsgiref.validate import validator
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator,FileExtensionValidator
import datetime
from django.db.models import Sum
from django.db.models import F
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
# Create your models here.

class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("User must choose Email Address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    # we need super user to have password
    def create_superuser(self, email, name, password):
        """create and save a new super user with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database model for users in the system """
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name


    def __str__(self):
        """return string represent of our user"""
        return self.email

class Course(models.Model):
    """Hnadling courses model"""
    name = models.CharField(max_length=300)
    reviews = models.ManyToManyField('Review') # b7ot single quote
    price = models.IntegerField()
    includes = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Courses_images')
    description = models.TextField()
    overview = models.TextField()
    instructor = models.ManyToManyField('Instructor')
    language = models.CharField(max_length=30)
    rate = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    date = models.DateTimeField(auto_now_add=True)


class Instructor(models.Model):
    """Handling instructor model"""
    name = models.CharField(max_length=300)
    description=models.TextField()
    number=models.IntegerField()
    courses=models.TextField() #hna al mfrod a5od al courses ali ll ragl dh


class Review(models.Model):
    """Handling Reviews model"""
    name=models.CharField(max_length=300) #hna al mfrod a5od asm al user ali hy3ml al review
    comment=models.TextField()
    rate = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )



class Content(models.Model):
    """Handling the content of the course"""
    session = models.FileField(upload_to='videos_uploaded',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    description=models.TextField()
    session_summary=models.TextField()
    attached_files=models.FileField("Attached Files")
    
     

class Chapter(models.Model):
    """Handling the chapters of content"""
    chapter=models.TextField()
    content=models.ManyToManyField('content')


class q_a(models.Model):
    """Handling Q&A part"""






class Cart(models.Model):
    """Handling cart model"""
    creation_date = models.DateTimeField(verbose_name=('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=('checked out'))
    
    class Meta:
        verbose_name = ('cart')
        verbose_name_plural = ('carts')
        ordering = ('-creation_date',)

    def __unicode__(self):
        return UnicodeDecodeError(self.creation_date)
    
    def __init__(self, request):
        CART_ID = 'CART-ID'
        cart_id = request.session.get(CART_ID)
        if cart_id:
            cart = models.Cart.objects.filter(id=cart_id, checked_out=False).first()
            if cart is None:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        CART_ID = 'CART-ID'
        cart = models.Cart.objects.create(creation_date=datetime.datetime.now())
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, unit_price, quantity=1):
        item = models.Course.objects.filter(cart=self.cart, product=product).first()
        if item:
            item.unit_price = unit_price
            item.quantity += int(quantity)
            item.save()
        else:
            models.Item.objects.create(cart=self.cart, product=product, unit_price=unit_price, quantity=quantity)

    def remove(self, product):
        item = models.Course.objects.filter(cart=self.cart, product=product).first()
        if item:
            item.delete()
        else:
            raise ItemDoesNotExist

    def update(self, product, quantity, unit_price=None):
        item = models.Course.objects.filter(cart=self.cart, product=product).first()
        if item:
            if quantity == 0:
                item.delete()
            else:
                item.unit_price = unit_price
                item.quantity = int(quantity)
                item.save()
        else:
            raise ItemDoesNotExist

    def count(self):
        return self.cart.item_set.all().aggregate(Sum('quantity')).get('quantity__sum', 0)

    def summary(self):
        return self.cart.item_set.all().aggregate(total=Sum(F('quantity')*F('unit_price'))).get('total', 0)

    def clear(self):
        self.cart.item_set.all().delete()

    def is_empty(self):
        return self.count() == 0

    def cart_serializable(self):
        representation = {}
        for item in self.cart.item_set.all():
            item_id = str(item.object_id)
            item_dict = {
                'total_price': item.total_price,
                'quantity': item.quantity
            }
            representation[item_id] = item_dict
        return representation


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass
