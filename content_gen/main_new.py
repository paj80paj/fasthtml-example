from fasthtml.common import *
from collections import defaultdict

# Set up the app
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
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
        A("Dashboard", href="/", cls="btn btn-ghost btn-block"),
        A("Company Strategy", href="/company-strategy", cls="btn btn-ghost btn-block"),
        A("Working Titles", href="/working-titles", cls="btn btn-ghost btn-block"),
        A("Outlining", href="/outlining", cls="btn btn-ghost btn-block"),
        A("Full Text Generation", href="/full-text", cls="btn btn-ghost btn-block"),
        A("Content Reuse", href="/content-reuse", cls="btn btn-ghost btn-block"),
        A("Prompts", href="/prompts", cls="btn btn-ghost btn-block"),
        cls="menu bg-base-200 w-56 p-4"
    )
    return Div(sidebar, Div(content, cls="flex-1 p-8"), cls="flex min-h-screen bg-base-100")

@app.get("/")
def get():
    title = "Content Generation Dashboard"
    
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
                        A(f"Go to {stage.title()}", href=f"/{stage.lower().replace(' ', '-')}", cls="btn btn-primary btn-sm mt-2")
                    ]
                )
            ]
        ) for stage in ["Company Strategy", "Working Titles", "Outlining", "Full Text", "Content Reuse"]),
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
                            A("Next Step", href=f"/next-step/{title['id']}", cls="btn btn-sm btn-primary"),
                            cls="mt-4"
                        )
                    ]
                )
            ]
        ) for title in working_titles),
        cls="mb-6"
    )

    content = Div(
        H1(title, cls="text-3xl font-bold mb-4"),
        progress,
        stage_summaries,
        current_projects,
        cls="container mx-auto"
    )

    return Titled(title, create_layout(content))

@app.get("/company-strategy")
def get():
    title = "Company Strategy"
    content = Div(
        H1(title, cls="text-3xl font-bold mb-4"),
        Form(
            Div(
                Label("Value Proposition", cls="label"),
                Textarea(placeholder="Enter your company's value proposition", cls="textarea textarea-bordered w-full"),
                cls="mb-4"
            ),
            Div(
                Label("Key Differentiators", cls="label"),
                Input(type="text", placeholder="Enter a key differentiator", cls="input input-bordered w-full mb-2"),
                Input(type="text", placeholder="Enter a key differentiator", cls="input input-bordered w-full mb-2"),
                Input(type="text", placeholder="Enter a key differentiator", cls="input input-bordered w-full mb-2"),
                cls="mb-4"
            ),
            Div(
                Label("Competitors", cls="label"),
                Ul(
                    Li("Amazon", cls="mb-2"),
                    Li("Microsoft", cls="mb-2"),
                    cls="list-disc list-inside mb-2"
                ),
                Input(type="text", placeholder="Add a competitor", cls="input input-bordered w-full"),
                cls="mb-4"
            ),
            Div(
                Label("Social Media Profiles", cls="label"),
                Input(type="text", placeholder="Twitter profile URL", cls="input input-bordered w-full mb-2"),
                Input(type="text", placeholder="LinkedIn profile URL", cls="input input-bordered w-full mb-2"),
                cls="mb-4"
            ),
            Button("Save Strategy", cls="btn btn-primary"),
            cls="space-y-4"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/working-titles")
def get():
    title = "Working Titles"
    content = Div(
        H1(title, cls="text-3xl font-bold mb-4"),
        Div(
            Input(type="text", placeholder="Search titles", cls="input input-bordered w-full max-w-xs mr-2"),
            Select(
                Option("All Themes", value=""),
                *(Option(theme) for theme in set(title['theme'] for title in working_titles)),
                cls="select select-bordered"
            ),
            cls="mb-4"
        ),
        Table(
            Thead(
                Tr(
                    Th("Title"),
                    Th("Subtitle"),
                    Th("Theme"),
                    Th("Status"),
                    Th("Inspiration"),
                    Th("Actions")
                )
            ),
            Tbody(
                *(Tr(
                    Td(title['title']),
                    Td(title['subtitle']),
                    Td(title['theme']),
                    Td(Badge(title['status'].capitalize(), cls=f"badge badge-{title['status'].lower()}")),
                    Td(title['inspiration']),
                    Td(
                        Div(
                            A("Edit", href=f"/edit-title/{title['id']}", cls="btn btn-xs btn-outline"),
                            A("Select", href=f"/select-title/{title['id']}", cls="btn btn-xs btn-primary"),
                            cls="btn-group"
                        )
                    )
                ) for title in working_titles)
            ),
            cls="table table-zebra w-full"
        ),
        Div(
            Input(type="text", placeholder="Enter a new working title", cls="input input-bordered w-full max-w-xs mr-2"),
            Button("Add Title", cls="btn btn-primary"),
            Button("Generate Titles", cls="btn btn-secondary ml-2"),
            cls="mt-4"
        ),
        A("View Prompts", href="/prompts", cls="btn btn-link mt-4"),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/outlining")
def get():
    title = "Outlining"
    content = Div(
        H1(title, cls="text-3xl font-bold mb-4"),
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
            Button("Generate Outline", cls="btn btn-primary"),
            Button("Edit Outline", cls="btn btn-secondary ml-2"),
            cls="mt-4"
        ),
        A("View Prompts", href="/prompts", cls="btn btn-link mt-4"),
        Div(
            H3("Chat with AI", cls="text-xl font-bold mb-2"),
            Div("How can I help you with your outline?", cls="chat-bubble", cls_="chat chat-start"),
            Div("Can you suggest a structure for my AI marketing strategy article?", cls="chat-bubble", cls_="chat chat-end"),
            Input(type="text", placeholder="Type your message here", cls="input input-bordered w-full mt-2"),
            cls="mt-8 p-4 bg-base-200 rounded-box"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/full-text")
def get():
    title = "Full Text Generation"
    content = Div(
        H1(title, cls="text-3xl font-bold mb-4"),
        Select(
            Option("Choose an outline", value=""),
            Option("AI-Powered Marketing Strategy Outline", value="1"),
            Option("Cyber Risk Management in AI Outline", value="2"),
            cls="select select-bordered w-full max-w-xs mb-4"
        ),
        Textarea(placeholder="Generated full text will appear here", cls="textarea textarea-bordered w-full h-64"),
        Div(
            Button("Generate Full Text", cls="btn btn-primary"),
            Button("Edit Text", cls="btn btn-secondary ml-2"),
            Button("View Diff", cls="btn btn-outline ml-2"),
            cls="mt-4"
        ),
        A("View Prompts", href="/prompts", cls="btn btn-link mt-4"),
        Div(
            H3("Chat with AI", cls="text-xl font-bold mb-2"),
            Div("How can I assist you with the full text generation?", cls="chat-bubble", cls_="chat chat-start"),
            Div("Can you expand on the second point in the outline?", cls="chat-bubble", cls_="chat chat-end"),
            Input(type="text", placeholder="Type your message here", cls="input input-bordered w-full mt-2"),
            cls="mt-8 p-4 bg-base-200 rounded-box"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/content-reuse")
def get():
    title = "Content Reuse"
    content = Div(
        H1(title, cls="text-3xl font-bold mb-4"),
        Select(
            Option("Choose a full-text article", value=""),
            Option("AI-Powered Marketing Strategy", value="1"),
            Option("Cyber Risk Management in AI", value="2"),
            cls="select select-bordered w-full max-w-xs mb-4"
        ),
        Textarea(placeholder="Generated shorter content will appear here", cls="textarea textarea-bordered w-full h-32"),
        Div(
            Button("Generate Short Content", cls="btn btn-primary"),
            Button("Edit Content", cls="btn btn-secondary ml-2"),
            cls="mt-4"
        ),
        A("View Prompts", href="/prompts", cls="btn btn-link mt-4"),
        Div(
            H3("Chat with AI", cls="text-xl font-bold mb-2"),
            Div("How would you like to repurpose this content?", cls="chat-bubble", cls_="chat chat-start"),
            Div("Can you create a tweet thread from the main points?", cls="chat-bubble", cls_="chat chat-end"),
            Input(type="text", placeholder="Type your message here", cls="input input-bordered w-full mt-2"),
            cls="mt-8 p-4 bg-base-200 rounded-box"
        ),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

@app.get("/prompts")
def get():
    title = "Prompts"
    content = Div(
        H1(title, cls="text-3xl font-bold mb-4"),
        *(Div(
            H2(f"{stage} Prompts", cls="text-2xl font-bold mb-2"),
            Textarea(placeholder=f"Enter prompts for {stage}", cls="textarea textarea-bordered w-full h-32"),
            Div(
                Button("Regenerate Prompt", cls="btn btn-primary"),
                Button("View Diff", cls="btn btn-outline ml-2"),
                cls="mt-2"
            ),
            cls="mb-8"
        ) for stage in ["Company Strategy", "Working Titles", "Outlining", "Full Text Generation", "Content Reuse"]),
        Button("Save All Prompts", cls="btn btn-primary mt-4"),
        cls="container mx-auto"
    )
    return Titled(title, create_layout(content))

serve()