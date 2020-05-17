from pytest_bdd import scenario, given, when, then


@scenario('../features/things.feature', 'Add a thing to the cloud')
def test_add():
    pass


@given('I have a thing to add')
def thing():
    pass


@when('a thing is added to the cloud')
def add_thing():
    pass


@then('the cloud integrates the thing')
def check_cloud():
    pass
