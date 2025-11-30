BookListView

Endpoint: /books/

Method: GET

Returns list of all books.

Permissions: Public


BookDetailView

Endpoint: /books/<pk>/

Method: GET

Returns one book by ID.

Permissions: Public


BookCreateView

Endpoint: /books/create/

Method: POST

Creates a new book object.

Permissions: Authenticated users only

Custom behavior:

perform_create() ensures the data is validated before saving.


BookUpdateView

Endpoint: /books/<pk>/update/

Method: PUT / PATCH

Updates a book.

Permissions: Authenticated users only


BookDeleteView

Endpoint: /books/<pk>/delete/

Method: DELETE

Removes a book.

Permissions: Authenticated users only