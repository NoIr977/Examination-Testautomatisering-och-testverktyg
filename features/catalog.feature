Feature: Catalog

Scenario: Open the book catalogue

  Given the user is on the main page of Läslistan
  When the user navigates to My Books and then returns to the Catalogue
  Then the page with the book list is opened