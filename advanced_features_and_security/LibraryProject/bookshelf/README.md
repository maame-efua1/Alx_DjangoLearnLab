# Django Permissions and Groups Setup

This app implements custom permissions and role-based access using Django's built-in auth system.

## Permissions
Custom permissions are defined in `relationship_app/models.py` under the `Article` model:
- `can_view` — Allows user to view articles
- `can_create` — Allows user to create new articles
- `can_edit` — Allows user to modify existing articles
- `can_delete` — Allows user to delete articles

## Groups
Configured groups:
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Enforcing Permissions
Views are protected using `@permission_required` decorators in `views.py`.

Example:
```python
@permission_required('relationship_app.can_edit', raise_exception=True)
def article_edit(request, pk):
    ...
