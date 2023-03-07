import factory
from Upload_Images.apps.profiles.models import Profile
from django.db.models.signals import post_save
from faker import Factory as FakerFactory
from Upload_Images.Upload_Images.settings import AUTH_USER_MODEL

faker = FakerFactory.create()


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):

    """create faker Profil"""

    TIER = (
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ENTERPRISE', 'Enterprise'),
        ('CUSTOM', 'Custom')
    )
    user = factory.SubFactory("tests.factories.UserFactory")
    tier = factory.LazyAttribute("BASIC")
    custom_resolution = factory.LazyAttribute(500)

    class Meta:
        model = Profile


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
