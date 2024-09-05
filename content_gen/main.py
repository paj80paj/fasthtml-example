from fasthtml.common import *
from claudette import *
import os
from starlette.staticfiles import StaticFiles
from collections import defaultdict

app, rt = fast_app()

# Mock data for demonstration purposes
working_titles = [
    {"id": 1, "title": "AI-Powered Marketing Strategy", "theme": "AI Marketing", "status": "new"},
    {"id": 2, "title": "Cyber Risk Management in AI", "theme": "Cybersecurity, AI", "status": "outlined"},
    {"id": 3, "title": "Regulatory Compliance in AI", "theme": "AI, Regulations", "status": "draft"},
    {"id": 4, "title": "Ethical AI: Principles and Practices", "theme": "AI Ethics", "status": "final"},
    {"id": 5, "title": "AI for Financial Services", "theme": "AI, Finance", "status": "published"},
]

@rt("/")
def get():
    title = "Content Generation Dashboard"
    description = "Overview of Working Titles"

    # Count titles by status and theme
    status_count = defaultdict(int)
    theme_count = defaultdict(int)
    for title in working_titles:
        status_count[title['status']] += 1
        for theme in title['theme'].split(', '):
            theme_count[theme] += 1

    # Create status breakdown
    status_breakdown = Div(
        H2("Status Breakdown", cls="text-xl font-bold mb-2"),
        *[P(f"{status.capitalize()}: {count}", cls="mb-1") for status, count in status_count.items()],
        cls="mb-6"
    )

    # Create theme breakdown
    theme_breakdown = Div(
        H2("Theme Breakdown", cls="text-xl font-bold mb-2"),
        *[P(f"{theme}: {count}", cls="mb-1") for theme, count in theme_count.items()],
        cls="mb-6"
    )

    # Create working titles list
    titles_list = Div(
        H2("Working Titles", cls="text-xl font-bold mb-2"),
        *[A(f"{title['title']} ({title['status'].capitalize()})", 
            href=f"/{title['status']}/{title['id']}", 
            cls="block mb-2 text-blue-500 hover:underline") 
          for title in working_titles],
        cls="mb-6"
    )

    content = Div(
        H1(title, cls="text-3xl font-bold mb-4"),
        P(description, cls="text-gray-600 mb-6"),
        Div(
            Div(status_breakdown, cls="w-1/2 pr-4"),
            Div(theme_breakdown, cls="w-1/2 pl-4"),
            cls="flex mb-6"
        ),
        titles_list,
        cls="container mx-auto px-4 py-8"
    )

    return Titled(title, content)

# Add placeholder routes for different statuses
@rt("/{status}/{title_id}")
def get(status: str, title_id: int):
    title = next((t for t in working_titles if t['id'] == title_id), None)
    if not title:
        return Titled("Not Found", H1("Title not found"))
    
    content = Div(
        H1(f"{title['title']} ({status.capitalize()})", cls="text-3xl font-bold mb-4"),
        P(f"Theme: {title['theme']}", cls="text-gray-600 mb-4"),
        P("This is a placeholder page for the working title. Implement the appropriate content based on the status.", cls="mb-4"),
        A("Back to Dashboard", href="/", cls="text-blue-500 hover:underline"),
        cls="container mx-auto px-4 py-8"
    )
    
    return Titled(f"{title['title']} - {status.capitalize()}", content)

serve()
