Feature: ThingManagement
  As a user,
  I want to magage all the things,
  So that I can add, remove and have control of them.

  Scenario: Add a thing to the cloud
    Given I have a thing to add
    When a thing is added to the cloud
    Then the cloud integrates the thing