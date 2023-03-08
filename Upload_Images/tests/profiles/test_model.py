import pytest

from pytest_factoryboy import register

from apps.profiles.exceptions import ResolutionValueNegative
from tests.factories import ProfileFactory, UserFactory, CustomFactory

register(ProfileFactory)
register(UserFactory)
register(CustomFactory)


@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user


@pytest.fixture
def profile(db, profile_factory):
    user_profile = profile_factory.create()
    return user_profile


@pytest.fixture
def custom(db, custom_factory):
    custom_res = custom_factory.create()
    return custom_res


def test_custom_str(custom):
    """Test the profile model string representation"""
    assert custom.__str__() == f"Height in px: {custom.resolution}"


def test_custom_resolution(custom):
    """Test the profile resolution """
    assert custom.resolution == 100


def test_custom_resolution_edit(custom_factory):
    """Test negative resolution error"""
    with pytest.raises(ResolutionValueNegative) as err:
        custom_factory.create(resolution=-200)
    assert str(err.value) == "The resolution can't be negative"


def test_profile_str(profile):
    """Test the profile model string representation"""
    assert profile.__str__() == f'{profile.user.username} {profile.tier} Profile'


def test_profile_tier(profile):
    """Test the profile model tier"""
    assert profile.tier == "BASIC"


def test_profile_basic_custom_resolution(profile):
    """Test the profile model tier basic, custom_resolution should be None """
    assert profile.custom_resolution == None


def test_profile__basic_with_custom_resolution_value(profile, custom_factory):
    """Test the profile model tier basic, custom_resolution should be None """
    custom_obj = custom_factory.create(resolution=200)
    profile.custom_resolution = custom_obj
    profile.save()
    assert profile.custom_resolution == None
