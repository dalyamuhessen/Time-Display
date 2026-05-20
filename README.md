# Time Display — Django Project
A beginner Django project that displays the current date and time on a styled web page.
---

## Objectives

- Practice setting up a Django project
- Familiarity with passing data to a template
- Practice connecting to static files
---
## Project Structure
```
Date/
├── Date/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── time_display/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
└── manage.py
```

---
## Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `index` | Displays current date and time |
| `/time_display/` | `index` | Displays current date and time |

---

## Views

**`time_display/views.py`:**
```python
from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)
```

### Ninja Bonus — Alternative using `datetime`:
```python
from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        "time": datetime.now().strftime("%B %d, %Y — %I:%M %p")
    }
    return render(request, 'index.html', context)
```

---

Static files are loaded using:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

## Key Concepts

- **`render()`** — renders an HTML template and passes context data to it
- **`context`** — a dictionary passed from the view to the template
- **`strftime`** — formats a time object into a readable string
- **`{% load static %}`** — Django template tag to enable static file references
- **`{% static '...' %}`** — generates the correct URL for a static file

---
