from fasthtml.common import *
from claudette import *

# Set up the app
hdrs = (picolink, Script(src="https://cdn.tailwindcss.com"))
app = FastHTML(hdrs=hdrs, cls="p-4 max-w-6xl mx-auto")

def app_tile(title, description, action, href="#"):
    return Div(cls="border p-4 rounded-lg")(
        H3(title, cls="font-bold"),
        P(description),
        A(Button(action, cls="mt-2 bg-blue-500 text-white px-4 py-2 rounded"), href=href)
    )

@app.get
def index():
    page = Div(
        H1("Client Workspace", cls="text-3xl font-bold mb-6"),
        Div(cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4")(
            app_tile("ClientComm", "An AI-powered digital assistant, combining natural language processing with client interactions.", "Open", href="/clientcomm"),
            app_tile("Monitor", "Automated monitoring of all client portfolios to warn of portfolio in distress.", "Open"),
            app_tile("Commentary", "Using GPT to generate personalized investment commentary at scale.", "Add"),
            app_tile("Optimiser", "Quantitative risk to enhance risk-adjusted return.", "Add"),
            app_tile("Voice", "Supports meetings in person or over calls for meeting summaries and actionable document drafting.", "Open"),
            app_tile("E2C", "Enables a digital meeting proposition through an integrated video and CASS custody service.", "Add")
        )
    )
    return Titled('Client Workspace', page)

@app.get("/clientcomm")
def clientcomm():
    page = Div(
        A("Back to Client Workspace", href="/", cls="text-blue-500 hover:underline mb-4 inline-block"),
        H1("ClientComm", cls="text-3xl font-bold mb-6"),
        Div(cls="mb-8")(
            H2("Ask your AI Digital Assistant", cls="text-2xl font-bold mb-4"),
            Div(cls="flex")(
                Input(type="text", placeholder="Ask your question here", cls="flex-grow p-2 border rounded-l"),
                Button("Go", cls="bg-blue-500 text-white px-4 py-2 rounded-r")
            )
        ),
        Div(cls="mb-8")(
            H2("Upcoming Meeting", cls="text-2xl font-bold mb-4"),
            P("Heads up! You have a meeting with [Client Name] in an hour. Here are some things to note:", cls="mb-2"),
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
            H2("Recent Questions", cls="text-2xl font-bold mb-4"),
            Div(cls="border-b pb-4 mb-4")(
                P("Which clients hold US securities, but we don't hold a W-8 BEN form for them on file.", cls="font-bold"),
                Div(cls="flex items-center mt-2")(
                    Img(src="user-icon.png", alt="User Icon", cls="w-8 h-8 mr-2"),
                    P("Three clients hold your securities...")
                )
            )
        )
    )
    return Titled('ClientComm', page)

serve()