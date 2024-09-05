from fasthtml.common import *
from collections import defaultdict, Counter
from fasthtml.common import Div, Textarea  # Make sure Textarea is imported
from prompts import (
    OUR_STRATEGY_PROMPT,
    WORKING_TITLES_PROMPT,
    OUTLINE_PROMPT,
    FULL_TEXT_PROMPT,
    REUSE_PROMPT,
    TITLE_GENERATION_PROMPT,
    CONTENT_EDITING_PROMPT,
)

# Global variables for screen names
DASHBOARD = "Dashboard"
OUR_STRATEGY = "Our Strategy"  # Changed from COMPANY_STRATEGY
WORKING_TITLES = "Working Titles"
OUTLINE = "Outline"  
FULL_TEXT = "Full Text"  
REUSE = "Reuse"
PROMPTS = "Prompts"

# List of main steps
MAIN_STEPS = [OUR_STRATEGY, WORKING_TITLES, OUTLINE, FULL_TEXT, REUSE]

# Set up the app
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css"),
)
app = FastHTML(hdrs=hdrs, ws_hdr=True)

# Mock data for demonstration purposes
working_titles = [
    {"id": 1, "title": "AI-Powered Marketing Strategy", "subtitle": "Leveraging AI for Better Marketing Results", "theme": "AI Marketing", "status": "new", "inspiration": "Twitter trend on AI marketing"},
    {"id": 2, "title": "Cyber Risk Management in AI", "subtitle": "Protecting AI Systems from Cyber Threats", "theme": "Cybersecurity, AI", "status": "outlined", "inspiration": "Recent cybersecurity conference"},
    {"id": 3, "title": "Regulatory Compliance in AI", "subtitle": "Navigating the Complex Landscape of AI Regulations", "theme": "AI, Regulations", "status": "draft", "inspiration": "New EU AI Act"},
    {"id": 4, "title": "Ethical AI: Principles and Practices", "subtitle": "Building Responsible AI Systems", "theme": "AI Ethics", "status": "final", "inspiration": "AI ethics guidelines by IEEE"},
    {"id": 5, "title": "AI for Financial Services", "subtitle": "Transforming Finance with Artificial Intelligence", "theme": "AI, Finance", "status": "published", "inspiration": "FinTech industry report"},
]

def create_layout(content):
    sidebar = Div(
        A(DASHBOARD, href="/", cls="btn btn-ghost btn-block"),
        A(OUR_STRATEGY, href="/our-strategy", cls="btn btn-ghost btn-block"),
        A(WORKING_TITLES, href="/working-titles", cls="btn btn-ghost btn-block"),
        A(OUTLINE, href="/outline", cls="btn btn-ghost btn-block"),
        A(FULL_TEXT, href="/full-text", cls="btn btn-ghost btn-block"),
        A(REUSE, href="/reuse", cls="btn btn-ghost btn-block"),
        A(PROMPTS, href="/prompts", cls="btn btn-ghost btn-block"),
        cls="menu bg-base-200 w-56 p-4"
    )
    theme_selector = Div(
        Select(
            Option("Corporate", value="corporate"),
            Option("Light", value="light"),
            Option("Dark", value="dark"),
            Option("Cupcake", value="cupcake"),
            Option("Bumblebee", value="bumblebee"),
            Option("Emerald", value="emerald"),
            Option("Synthwave", value="synthwave"),
            cls="select select-bordered w-full max-w-xs",
            hx_post="/change-theme",
            hx_target="#theme-wrapper",
            hx_swap="attributes"
        ),
        cls="fixed bottom-4 right-4"
    )
    return Div(
        sidebar, 
        Div(content, cls="flex-1 p-8"), 
        theme_selector,
        cls="flex min-h-screen bg-base-100", 
        data_theme="corporate",
        id="theme-wrapper"
    )

def create_progress_bar(current_step):
    steps = ["Our Strategy", "Working Titles", "Outline", "Full Text", "Reuse"]
    progress_value = (steps.index(current_step) + 1) * 20  # Each step is worth 20%
    
    return Div(
        Ul(
            *(Li(
                cls=f"step {'step-primary' if steps.index(step) <= steps.index(current_step) else ''}"
            ) for step in steps),
            cls="steps w-full"
        ),
        Progress(cls="progress progress-primary w-full", value=str(progress_value), max="100"),
        cls="mb-8"
    )

@app.get("/")
def get():
    title = DASHBOARD
    
    status_count = defaultdict(int)
    theme_count = defaultdict(int)
    for title in working_titles:
        status_count[title['status']] += 1
        for theme in title['theme'].split(', '):
            theme_count[theme] += 1

    progress = Div(
        H2("Overall Progress", cls="text-xl font-bold mb-2"),
        Progress(cls="progress progress-primary w-56", value="40", max="100"),
        P("40% Complete", cls="mt-2"),
        cls="mb-6"
    )

    stage_summaries = Div(
        *(Div(
            cls="card bg-base-200",
            contents=[
                Div(
                    cls="card-body",
                    contents=[
                        H3(stage.title(), cls="card-title"),
                        P(f"{sum(1 for t in working_titles if t['status'] == stage.lower())} items"),
                        A(f"Go to {stage.title()}", href=f"/{stage.lower().replace(' ', '-')}", cls="btn btn-primary btn-sm mt-2 text-white")
                    ]
                )
            ]
        ) for stage in MAIN_STEPS),
        cls="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6"
    )

    current_projects = Div(
        H2("Current Projects", cls="text-xl font-bold mb-2"),
        *(Div(
            cls="card bg-base-200 mt-4",
            contents=[
                Div(
                    cls="card-body",
                    contents=[
                        H3(title['title'], cls="card-title"),
                        P(title['subtitle'], cls="text-sm text-base-content text-opacity-60"),
                        P(f"Status: {title['status'].capitalize()}", cls="mt-2"),
                        P(f"Theme: {title['theme']}", cls="mt-1"),
                        Div(
                            A("Edit", href=f"/{title['status'].lower().replace(' ', '-')}/{title['id']}", cls="btn btn-sm btn-outline mr-2"),
                            A("View History", href=f"/history/{title['id']}", cls="btn btn-sm btn-outline mr-2"),
                            A("Next Step", href=f"/next-step/{title['id']}", cls="btn btn-sm btn-primary text-white"),
                            cls="mt-4"
                        )
                    ]
                )
            ]
        ) for title in working_titles),
        cls="mb-6"
    )

    content = Div(
        H1(title, cls="text-4xl font-bold mb-8"),
        progress,
        stage_summaries,
        current_projects,
        cls="container mx-auto"
    )

    return Titled(title, create_layout(content))

@app.get("/our-strategy")
def get():
    title = OUR_STRATEGY
    content = Div(
        Div(
            H1(title, cls="text-4xl font-bold"),
            A("Next", href="/working-titles", cls="btn btn-secondary text-white", id="nextButton", hx_get="/activate-next", hx_trigger="titleSelected from:body", hx_swap="outerHTML"),
            cls="flex justify-between items-center mb-8"
        ),
        create_progress_bar(OUR_STRATEGY),
        Div(
            Div(
                H2("Value Proposition", cls="text-xl font-semibold mb-2"),
                Textarea(placeholder="Enter your company's value proposition", cls="textarea textarea-bordered w-full h-24"),
                cls="mb-6"
            ),
            Div(
                H2("Key Differentiators", cls="text-xl font-semibold mb-2"),
                Ul(
                    Li(Input(type="text", placeholder="Enter a key differentiator", cls="input input-bordered w-full mb-2")),
                    Li(Input(type="text", placeholder="Enter a key differentiator", cls="input input-bordered w-full mb-2")),
                    Li(Input(type="text", placeholder="Enter a key differentiator", cls="input input-bordered w-full mb-2")),
                    cls="list-none p-0"
                ),
                Button("+ Add Differentiator", cls="btn btn-outline btn-sm mt-2"),
                cls="mb-6"
            ),
            Div(
                H2("Competitors", cls="text-xl font-semibold mb-2"),
                Ul(
                    Li(Div("Amazon", Button("x", cls="btn btn-ghost btn-xs ml-2"), cls="flex items-center")),
                    Li(Div("Microsoft", Button("x", cls="btn btn-ghost btn-xs ml-2"), cls="flex items-center")),
                    cls="list-disc list-inside mb-2"
                ),
                Div(
                    Input(type="text", placeholder="Add a competitor", cls="input input-bordered w-full mr-2"),
                    Button("Add", cls="btn btn-primary btn-sm"),
                    cls="flex mt-2"
                ),
                cls="mb-6"
            ),
            Div(
                H2("Social Media Profiles", cls="text-xl font-semibold mb-2"),
                Input(type="text", placeholder="Twitter profile URL", cls="input input-bordered w-full mb-2"),
                Input(type="text", placeholder="LinkedIn profile URL", cls="input input-bordered w-full mb-2"),
                Button("+ Add Profile", cls="btn btn-outline btn-sm mt-2"),
                cls="mb-6"
            ),
            cls="grid grid-cols-1 md:grid-cols-2 gap-6"
        ),
        Div(
            Button("Save Strategy", cls="btn btn-primary text-white"),
            A("View Prompts", href="/prompts", cls="btn btn-link ml-4"),
            A("Next", href="/working-titles", cls="btn btn-secondary text-white"),
            cls="mt-8 flex justify-between items-center"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/working-titles")
def get():
    title = WORKING_TITLES
    
    theme_mapping = {
        "AI Marketing": "AI Mktg",
        "Cybersecurity": "Cyber",
        "AI": "AI",
        "Regulations": "Regs",
        "AI Ethics": "Ethics",
        "Finance": "Finance"
    }
    theme_counts = Counter()
    for title in working_titles:
        for theme in title['theme'].split(', '):
            short_theme = theme_mapping.get(theme, theme[:6])
            theme_counts[short_theme] += 1
    
    # Using DaisyUI theme colors
    badge_colors = ['badge-primary text-white', 'badge-secondary text-white', 'badge-accent text-white', 
                    'badge-info text-white', 'badge-success text-white', 'badge-warning text-white']
    
    # Define status badge colors with different darkness levels of blue
    status_badge_colors = {
        "new": "bg-blue-200 text-blue-800",
        "outlined": "bg-blue-300 text-blue-800",
        "draft": "bg-blue-400 text-blue-800",
        "final": "bg-blue-500 text-blue-800",
        "published": "bg-blue-600 text-blue-800"
    }
    
    content = Div(
        Div(
            H1("Working Titles", cls="text-4xl font-bold"),
            A("Next", href="/outline", cls="btn btn-secondary text-white opacity-50", id="nextButton", hx_get="/activate-next", hx_trigger="titleSelected from:body", hx_swap="outerHTML"),
            cls="flex justify-between items-center mb-8"
        ),
        create_progress_bar(WORKING_TITLES),
        Div(
            Div(
                Input(type="text", placeholder="Search for a working title", cls="input input-bordered w-full max-w-xs text-lg py-3 mr-4"),
                cls="flex items-center"
            ),
            Div(
                *(Div(
                    Div(str(count), cls="absolute -top-2 -right-2 bg-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center border border-base-300 shadow text-black"),
                    short_theme,
                    cls=f"badge {badge_colors[i % len(badge_colors)]} badge-md px-3 py-1 text-xs font-semibold mr-3 mb-3 cursor-pointer relative",
                    onclick=f"filterTheme('{short_theme}')"
                ) for i, (short_theme, count) in enumerate(theme_counts.items())),
                cls="flex flex-wrap"
            ),
            cls="flex items-center justify-between mb-8"
        ),
        Table(
            Thead(
                Tr(
                    Th("Title", cls="text-left font-bold text-lg py-3 text-gray-600"),
                    Th("Subtitle", cls="text-left font-bold text-lg py-3 text-gray-600"),
                    Th("Themes", cls="text-left font-bold text-lg py-3 text-gray-600"),
                    Th("Current Status", cls="text-left font-bold text-lg py-3 text-gray-600"),
                    Th("Inspiration Source", cls="text-left font-bold text-lg py-3 text-gray-600"),
                    Th("Actions", cls="text-left font-bold text-lg py-3 text-gray-600")
                )
            ),
            Tbody(
                *(Tr(
                    Td(title['title'], cls="py-3 border-b border-base-300"),
                    Td(title['subtitle'], cls="py-3 border-b border-base-300"),
                    Td(Div(
                        *(Div(
                            theme_mapping.get(theme.strip(), theme.strip()[:6]),
                            cls=f"badge {badge_colors[list(theme_mapping.keys()).index(theme.strip()) % len(badge_colors)]} badge-sm px-2 py-1 text-xs font-semibold mr-1 mb-1"
                        ) for theme in title['theme'].split(', ')),
                        cls="flex flex-wrap"
                    ), cls="py-3 border-b border-base-300"),
                    Td(Div(title['status'].capitalize(), cls=f"badge {status_badge_colors[title['status'].lower()]} badge-sm text-sm"), cls="py-3 border-b border-base-300"),
                    Td(title['inspiration'], cls="py-3 border-b border-base-300"),
                    Td(
                        Div(
                            A("Edit", href=f"/edit-title/{title['id']}", cls="btn btn-sm btn-outline mr-2"),
                            Button("Select", cls="btn btn-sm btn-primary text-white", hx_post=f"/select-title/{title['id']}", hx_target="closest tr", hx_swap="outerHTML"),
                            cls="flex"
                        ),
                        cls="py-3 border-b border-base-300"
                    ),
                    id=f"title-row-{title['id']}"
                ) for title in working_titles),
                cls="table w-full mb-8"
            ),
        ),
        Div(
            Div(
                Input(type="text", placeholder="Enter a new working title", cls="input input-bordered w-full max-w-md text-lg py-3"),
                Button("+ Add Title", cls="btn btn-primary btn-md ml-3 text-white"),
                cls="flex items-center"
            ),
            Button("Generate Titles", cls="btn btn-secondary btn-md ml-4 text-white"),
            A("View Prompts", href="/prompts", cls="btn btn-link btn-md ml-4"),
            A("Next", href="/outline", cls="btn btn-secondary text-white"),
            cls="mt-8 flex justify-between items-center"
        ),
        Div(
            id="theme-filter",
            hx_get="/filter-theme",
            hx_trigger="click",
            hx_target="#working-titles-table",
            hx_include="[name='theme']"
        ),
        Input(type="hidden", name="theme", id="selected-theme"),
        
        cls="container mx-auto px-4"
    )
    return Titled(title, create_layout(content))

@app.post("/select-title/{title_id}")
def select_title(title_id: int):
    # Find the selected title
    selected_title = next((t for t in working_titles if t['id'] == title_id), None)
    if not selected_title:
        return "Title not found", 404

    # Create the updated row with a different background color
    return Tr(
        Td(selected_title['title'], cls="py-3 border-b border-base-300"),
        Td(selected_title['subtitle'], cls="py-3 border-b border-base-300"),
        Td(Div(
            *(Div(
                theme_mapping.get(theme.strip(), theme.strip()[:6]),
                cls=f"badge {badge_colors[list(theme_mapping.keys()).index(theme.strip()) % len(badge_colors)]} badge-sm px-2 py-1 text-xs font-semibold mr-1 mb-1"
            ) for theme in selected_title['theme'].split(', ')),
            cls="flex flex-wrap"
        ), cls="py-3 border-b border-base-300"),
        Td(Div(selected_title['status'].capitalize(), cls=f"badge {status_badge_colors[selected_title['status'].lower()]} badge-sm text-sm"), cls="py-3 border-b border-base-300"),
        Td(selected_title['inspiration'], cls="py-3 border-b border-base-300"),
        Td(
            Div(
                A("Edit", href=f"/edit-title/{selected_title['id']}", cls="btn btn-sm btn-outline mr-2"),
                Button("Selected", cls="btn btn-sm btn-success text-white"),
                cls="flex"
            ),
            cls="py-3 border-b border-base-300"
        ),
        id=f"title-row-{selected_title['id']}",
        cls="bg-base-200",  # Use DaisyUI theme color for selected row
        hx_trigger="load"
    )

@app.get("/activate-next")
def activate_next():
    return A("Next", href="/outline", cls="btn btn-secondary text-white", id="nextButton", hx_get="/activate-next", hx_trigger="titleSelected from:body", hx_swap="outerHTML")

@app.get("/outline")
def get():
    title = OUTLINE
    content = Div(
        Div(
            H1(title, cls="text-4xl font-bold"),
            A("Next", href="/full-text", cls="btn btn-secondary text-white", id="nextButton", hx_get="/activate-next", hx_trigger="titleSelected from:body", hx_swap="outerHTML"),
            cls="flex justify-between items-center mb-8"
        ),
        create_progress_bar(OUTLINE),
        Div(
            Select(
                Option("Choose a working title", value=""),
                *(Option(title['title'], value=str(title['id'])) for title in working_titles),
                cls="select select-bordered w-full max-w-xs"
            ),
            cls="mb-4"
        ),
        Textarea(placeholder="Enter or generate an outline here", cls="textarea textarea-bordered w-full h-64"),
        Div(
            Button("Generate Outline", cls="btn btn-primary text-white"),
            Button("Edit Outline", cls="btn btn-secondary text-white ml-2"),
            cls="mt-4"
        ),
        A("View Prompts", href="/prompts", cls="btn btn-link mt-4"),
        Div(
            H3("Chat with AI", cls="text-xl font-bold mb-2"),
            Div("How can I help you with your outline?", cls="chat-bubble", cls_="chat chat-start"),
            Div("Can you suggest a structure for my AI marketing strategy article?", cls="chat-bubble", cls_="chat chat-end"),
            Div(
                Input(type="text", placeholder="Type your message here", cls="input input-bordered w-full"),
                Button("Send", cls="btn btn-primary ml-2"),
                cls="flex mt-2"
            ),
            cls="mt-8 p-4 bg-base-200 rounded-box"
        ),
        Div(
            A("View Prompts", href="/prompts", cls="btn btn-link"),
            A("Next", href="/full-text", cls="btn btn-secondary text-white"),
            cls="mt-8 flex justify-between items-center"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/full-text")
def get():
    title = FULL_TEXT
    content = Div(
        Div(
            H1(title, cls="text-4xl font-bold"),
            A("Next", href="/reuse", cls="btn btn-secondary text-white", id="nextButton", hx_get="/activate-next", hx_trigger="titleSelected from:body", hx_swap="outerHTML"),
            cls="flex justify-between items-center mb-8"
        ),
        create_progress_bar(FULL_TEXT),
        Select(
            Option("Choose an outline", value=""),
            Option("AI-Powered Marketing Strategy Outline", value="1"),
            Option("Cyber Risk Management in AI Outline", value="2"),
            cls="select select-bordered w-full max-w-xs mb-4"
        ),
        Textarea(placeholder="Generated full text will appear here", cls="textarea textarea-bordered w-full h-64"),
        Div(
            Button("Generate Full Text", cls="btn btn-primary text-white"),
            Button("Edit Text", cls="btn btn-secondary text-white ml-2"),
            Button("View Diff", cls="btn btn-outline ml-2"),
            cls="mt-4"
        ),
        Div(
            A("View Prompts", href="/prompts", cls="btn btn-link"),
            A("Next", href="/reuse", cls="btn btn-secondary text-white"),
            cls="mt-8 flex justify-between items-center"
        ),
        Div(
            H3("Chat with AI", cls="text-xl font-bold mb-2"),
            Div("How can I assist you with the full text generation?", cls="chat-bubble", cls_="chat chat-start"),
            Div("Can you expand on the second point in the outline?", cls="chat-bubble", cls_="chat chat-end"),
            Div(
                Input(type="text", placeholder="Type your message here", cls="input input-bordered w-full"),
                Button("Send", cls="btn btn-primary ml-2"),
                cls="flex mt-2"
            ),
            cls="mt-8 p-4 bg-base-200 rounded-box"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/reuse")
def get():
    title = REUSE
    content = Div(
        Div(
            H1(title, cls="text-4xl font-bold"),
            Button("Publish", cls="btn btn-success text-white", id="nextButton", hx_get="/activate-next", hx_trigger="titleSelected from:body", hx_swap="outerHTML"),
            cls="flex justify-between items-center mb-8"
        ),
        create_progress_bar(REUSE),
        Select(
            Option("Choose a full-text article", value=""),
            Option("AI-Powered Marketing Strategy", value="1"),
            Option("Cyber Risk Management in AI", value="2"),
            cls="select select-bordered w-full max-w-xs mb-4"
        ),
        Textarea(placeholder="Generated shorter content will appear here", cls="textarea textarea-bordered w-full h-32"),
        Div(
            Button("Generate Short Content", cls="btn btn-primary text-white"),
            Button("Edit Content", cls="btn btn-secondary text-white ml-2"),
            cls="mt-4"
        ),
        Div(
            A("View Prompts", href="/prompts", cls="btn btn-link"),
            Button("Publish", cls="btn btn-success text-white"),
            cls="mt-8 flex justify-between items-center"
        ),
        Div(
            H3("Chat with AI", cls="text-xl font-bold mb-2"),
            Div("How would you like to repurpose this content?", cls="chat-bubble", cls_="chat chat-start"),
            Div("Can you create a tweet thread from the main points?", cls="chat-bubble", cls_="chat chat-end"),
            Div(
                Input(type="text", placeholder="Type your message here", cls="input input-bordered w-full"),
                Button("Send", cls="btn btn-primary ml-2"),
                cls="flex mt-2"
            ),
            cls="mt-8 p-4 bg-base-200 rounded-box"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/prompts")
def get():
    title = PROMPTS
    content = Div(
        H1(title, cls="text-4xl font-bold mb-8"),
        Div(
            H2("Our Strategy Prompt", cls="text-xl font-semibold mb-2"),
            Textarea(OUR_STRATEGY_PROMPT, cls="textarea textarea-bordered w-full h-24 mb-4"),
            H2("Working Titles Prompt", cls="text-xl font-semibold mb-2"),
            Textarea(WORKING_TITLES_PROMPT, cls="textarea textarea-bordered w-full h-24 mb-4"),
            H2("Outline Prompt", cls="text-xl font-semibold mb-2"),
            Textarea(OUTLINE_PROMPT, cls="textarea textarea-bordered w-full h-24 mb-4"),
            H2("Full Text Prompt", cls="text-xl font-semibold mb-2"),
            Textarea(FULL_TEXT_PROMPT, cls="textarea textarea-bordered w-full h-24 mb-4"),
            H2("Reuse Prompt", cls="text-xl font-semibold mb-2"),
            Textarea(REUSE_PROMPT, cls="textarea textarea-bordered w-full h-24 mb-4"),
            H2("Title Generation Prompt", cls="text-xl font-semibold mb-2"),
            Textarea(TITLE_GENERATION_PROMPT, cls="textarea textarea-bordered w-full h-24 mb-4"),
            H2("Content Editing Prompt", cls="text-xl font-semibold mb-2"),
            Textarea(CONTENT_EDITING_PROMPT, cls="textarea textarea-bordered w-full h-24 mb-4"),
            cls="space-y-4"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.post("/change-theme")
def change_theme():
    theme = request.form.get("theme")
    return {"data-theme": theme}

serve()