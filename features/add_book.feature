Feature: Add Book

Scenario Outline: Add a new book

  Given the user is on the Add Book page
  When the user enters <titel> as the title
  And the user enters <author> as the author
  And the user clicks the "Lägg till ny bok" button
  And the user navigates to the catalogue
  Then the book <titel> by <author> is visible in the catalogue

  Examples:
    | titel                                    | author           |
    | Pride and Prejudice                      | Jane Austen      |
    | Harry Potter and the Philosopher's Stone | J. K. Rowling    |
    | The Hobbit                               | J. R. R. Tolkien |
