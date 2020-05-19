from pytest_bdd import scenario, given, when, then
from thing import Thing
from cloud import Cloud


# Add the path to teh feature file and the name of the scenario
@scenario('../features/things.feature', 'Add a thing to the cloud')
def test_add():
    pass


# This method implements the provided step
@given('I have a thing to add')
def setup():
    test_thing = Thing(id='01',
                       token='aaaa',
                       name='aaaa')
    test_cloud = Cloud()
    assert test_cloud.connect(arguments="'wss' 'ws.knot.cloud' 443")
    return test_thing, test_cloud


@when('a thing is added to the cloud')
def add_thing(setup):
    test_thing = setup[0]
    test_cloud = setup[1]
    assert test_cloud.count(option="all") == 0
    assert test_cloud.register("knot:thing ArCondicionado")
    result = test_cloud.add(option='thing',
                            object=test_thing)
    assert result


@then('the cloud integrates the thing')
def check_cloud(setup):
    test_cloud = setup[1]
    assert test_cloud.count(option="things") == 1
