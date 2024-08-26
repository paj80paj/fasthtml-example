from fasthtml.common import *
from claudette import *
import os
from starlette.staticfiles import StaticFiles

print(os.getcwd())  # Prints the current working directory

# Set up the app
hdrs = (
    picolink,
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css"),
    Link(rel="stylesheet", href="/static/styles.css"),
)
app = FastHTML(hdrs=hdrs)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

def app_tile(title, description, action, href="#", icon=""):
    return Div(cls="grid-item")(
        Img(src=f"/static/{icon}", alt=title),
        H3(title),
        P(description),
        A(action, href=href, cls="button")
    )

def sidebar():
    return Div(cls="sidebar")(
        Img(src="/static/icon1.png", alt="Icon 1"),
        Img(src="/static/icon2.png", alt="Icon 2"),
        Img(src="/static/icon3.png", alt="Icon 3"),
        Img(src="/static/icon4.png", alt="Icon 4"),
        Img(src="/static/icon5.png", alt="Icon 5")
    )

@app.get
def index():
    page = Div(cls="container")(
        sidebar(),
        Div(cls="main-content")(
            Img(src="/static/logo.png", alt="WealthAI Logo", cls="logo"),
            H1("Client Workspace"),
            Div(cls="grid-container")(
                app_tile("ClientComm", "An AI-powered digital assistant, combining natural language processing with client interactions.", "Open", href="/clientcomm", icon="clientcomm-icon.png"),
                app_tile("Monitor", "Automated monitoring of all client portfolios to warn of portfolio in distress.", "Open", icon="monitor-icon.png"),
                app_tile("Commentary", "Using GPT to generate personalized investment commentary at scale.", "Add", icon="commentary-icon.png"),
                app_tile("Optimiser", "Quantitative risk to enhance risk-adjusted return.", "Add", icon="optimiser-icon.png"),
                app_tile("Voice", "Supports meetings in person or over calls for meeting summaries and actionable document drafting.", "Open", icon="voice-icon.png"),
                app_tile("E2C", "Enables a digital meeting proposition through an integrated video and CASS custody service.", "Add", icon="e2c-icon.png")
            )
        )
    )
    return Titled('Client Workspace', page)

@app.get("/clientcomm")
def clientcomm():
    page = Div(cls="container")(
        sidebar(),
        Div(cls="main-content")(
            A("Back to Client Workspace", href="/", cls="button secondary"),
            H1("ClientComm"),
            Div(cls="mb-8")(
                H2("Ask your AI Digital Assistant"),
                Div(cls="flex")(
                    Input(type="text", placeholder="Ask your question here", cls="flex-grow p-2 border rounded-l"),
                    Button("Go", cls="button")
                )
            ),
            Div(cls="mb-8")(
                H2("Upcoming Meeting"),
                P("Heads up! You have a meeting with [Client Name] in an hour. Here are some things to note:"),
                Ul(cls="list-disc pl-5")(
                    Li("Portfolio Alert: [Product Name] underperformed by 15% this quarter."),
                    Li("Unresolved Issue: Client has an open support ticket about tax implications."),
                    Li("Client Concern: Recent email expressed worry about market volatility—interested in low-risk options."),
                    Li("Product Risk: [Specific Product] has been reclassified as higher risk."),
                    Li("Compliance Reminder: Your compliance training renewal is due in two weeks."),
                    Li("Consumer Duty: Ensure the client understands the value and pricing of their products per FCA guidelines."),
                    Li("Life Event: Client added a new dependent—might impact financial goals.")
                )
            ),
            Div(
                H2("Recent Questions"),
                Div(cls="border-b pb-4 mb-4")(
                    P("Which clients hold US securities, but we don't hold a W-8 BEN form for them on file.", cls="font-bold"),
                    Div(cls="flex items-center mt-2")(
                        Img(src="/static/user-icon.png", alt="User Icon", cls="w-8 h-8 mr-2"),
                        P("Three clients hold your securities...")
                    )
                )
            )
        )
    )
    return Titled('ClientComm', page)

serve()