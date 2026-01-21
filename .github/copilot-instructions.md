# Longdon Foods - Django Project Instructions

## Project Overview

This is a Django 6.0.1 food company website for "Longdon Foods" (plantain chips and coated peanuts). Simple view-based architecture with minimal backend logic—primarily a content presentation site.

## Architecture

### App Structure

- **Main app**: `main/` - handles all page routing (index, menu, gallery, about, contact)
- **Project config**: `longdon/` - settings, root URLs
- **Database**: SQLite (`db.sqlite3`) - currently unused, no models defined
- **Templates**: `templates/` - shared across project (configured in `TEMPLATES['DIRS']`)
- **Static assets**: `static/` - CSS, JS, images, vendors

### Key Files

- `main/views.py` - simple function-based views rendering templates
- `main/urls.py` - all user-facing routes (/, /menu/, /gallery/, /aboutus/, /contact/)
- `longdon/urls.py` - root URL config including admin
- `longdon/settings.py` - Django config with `sass_processor` integration

## Critical Conventions

### Template & Static Files

- **Always use `{% load static %}`** at the top of templates
- **Logo location**: `static/img/lomgdon foods logo 2.jpeg` (note: "lomgdon" typo in filename)
- **Asset references**: Use `{% static 'path/to/file' %}` for all CSS/JS/images
- **URL references**: Use `{% url 'view_name' %}` (e.g., `{% url 'index' %}`, `{% url 'menu' %}`)

### SCSS/CSS Management

- SCSS source files in `static/scss/` and `scss/`
- Uses `sass_processor` app (installed in `INSTALLED_APPS`)
- Custom finder: `sass_processor.finders.CssFinder` in `STATICFILES_FINDERS`
- Compiled CSS output: `static/css/`

### View Patterns

All views follow this pattern:

```python
def view_name(request):
    return render(request, 'template_name.html')
```

Exception: `contact_process` handles POST for form submission (basic implementation, no email/DB yet)

## Development Workflow

### Running the Server

```powershell
python manage.py runserver
```

### Making Migrations (when models are added)

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Static Files

No `collectstatic` needed for development (DEBUG=True). Static files served directly from `STATICFILES_DIRS`.

## Design Patterns

### Navigation Structure

- Main nav items: Home, About, Menu, Contact
- Dropdown menu: Pages → Gallery
- Offcanvas side menu duplicates main nav
- Two logo classes: `.logo-1` and `.logo-2` (for different themes/states)

### Template Organization

- Header/navigation duplicated across templates (no template inheritance currently)
- Bootstrap 4-based layout
- Heavy use of vendor libraries: owl-carousel, lightgallery, nice-select, swiper, etc.

## Important Notes

- **No database models yet** - `main/models.py` is empty
- **Contact form** submits to `/contact_process/` but doesn't persist data or send emails
- **Security**: `SECRET_KEY` exposed in settings.py (change for production)
- **DEBUG mode**: Currently `True` (disable for production)
- **Image naming**: Logo file has typo "lomgdon" instead of "longdon"

## When Adding Features

### New Pages

1. Add view function in `main/views.py`
2. Create template in `templates/`
3. Register route in `main/urls.py`
4. Update navigation in all template files (or refactor to template inheritance)

### Static Assets

- Images: `static/img/`
- CSS: `static/css/`
- JS: `static/js/`
- Vendors: `static/vendors/{library-name}/`

### Forms/Models

Currently no form handling beyond basic POST. To add:

- Define model in `main/models.py`
- Create/run migrations
- Update views to handle form validation
- Consider using Django's form classes
