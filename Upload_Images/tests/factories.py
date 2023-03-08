import factory
from django.utils import timezone
from apps.images.models import Image
from apps.profiles.models import Profile, Custom
from django.db.models.signals import post_save
from faker import Factory as FakerFactory
from Upload_Images.settings import AUTH_USER_MODEL

faker = FakerFactory.create()


@factory.django.mute_signals(post_save)
class ImageFactory(factory.django.DjangoModelFactory):
    """create faker Image"""

    class Meta:
        model = Image

    user = factory.SubFactory("tests.factories.UserFactory")
    title = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=6))
    alt = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=8))
    date_creation = factory.LazyAttribute(lambda x: timezone.now())
    image = factory.LazyAttribute(lambda x: faker.file_extension(category="image"))
    image_200 = factory.LazyAttribute(lambda x: faker.file_extension(category="image"))
    image_400 = factory.LazyAttribute(lambda x: faker.file_extension(category="image"))
    image_custom = factory.LazyAttribute(lambda x: faker.file_extension(category="image"))



@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    """create faker Profil"""

    class Meta:
        model = Profile

    user = factory.RelatedFactory("tests.factories.UserFactory")
    tier = factory.LazyAttribute(lambda x: "BASIC")
    custom_resolution = factory.RelatedFactory("tests.factories.CustomFactory")


@factory.django.mute_signals(post_save)
class CustomFactory(factory.django.DjangoModelFactory):
    """create faker CUSTOM"""
    class Meta:
        model = Custom

    resolution = factory.LazyAttribute(lambda x: 100)


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    """create faker User"""
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    username = factory.LazyAttribute(lambda x: faker.first_name())
    email = factory.LazyAttribute(lambda x: f"alpha@uploadapi.com")
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    is_staff = False

    class Meta:
        model = AUTH_USER_MODEL

    @classmethod
    def _create(cls, model_class, *args, **kwargs):

        """method for define user or superuser"""
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)
