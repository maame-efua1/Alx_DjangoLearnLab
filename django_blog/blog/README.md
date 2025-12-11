Blog Post CRUD
- List: GET /posts/ (public)
- Detail: GET /posts/<pk>/ (public)
- Create: GET/POST /posts/new/ (authenticated users)
- Update: GET/POST /posts/<pk>/edit/ (only post author)
- Delete: GET/POST /posts/<pk>/delete/ (only post author)

Permissions:
- Create requires login.
- Edit/Delete require the logged-in user to be the author.

Templates:
- blog/post_list.html
- blog/post_detail.html
- blog/post_form.html
- blog/post_confirm_delete.html
