Feature: Statistik

  Scenario: View book statistics
    Given the user is on the main page of Läslistan
    When the user navigates to "Statistik"
    Then the user can see statistics about how many books are in the list
    And the user can see statistics about how many books are marked as favorites