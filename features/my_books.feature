Feature: Favorite Books

  Scenario: Add a book to favorites
    Given the user is on the Katalog page
    When the user clicks the heart symbol for "Ormar på ett plan: En Python-berättelse"
    Then the book is marked as a favorite
    When the user navigates to "Mina böcker"
    Then the book "Ormar på ett plan: En Python-berättelse" is visible in the favorites list