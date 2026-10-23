Feature: Add Book

Scenario: Add a new book
  Given the user is on the Add Book page
  When the user enters "Pride and Prejudice" as the title
  And the user enters "Jane Austen" as the author
  And the user clicks the "Lägg till ny bok" button
  And the user navigates to the catalogue
  Then the new book is visible in the catalogue