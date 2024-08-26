from fasthtml.common import *
from claudette import *

# Set up the app
hdrs = (picolink, Script(src="https://cdn.tailwindcss.com"))
app = FastHTML(hdrs=hdrs, cls="p-4 max-w-6xl mx-auto")

def app_tile(title, description, action):
    return Div(cls="border p-4 rounded-lg")(
        H3(title, cls="font-bold"),
        P(description),
        Button(action, cls="mt-2 bg-blue-500 text-white px-4 py-2 rounded")
    )

@app.get
def index():
    page = Div(
        H1("Client Workspace", cls="text-3xl font-bold mb-6"),
        Div(cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4")(
            app_tile("ClientComm", "An AI-powered digital assistant, combining natural language processing with client interactions.", "Open"),
            app_tile("Monitor", "Automated monitoring of all client portfolios to warn of portfolio in distress.", "Open"),
            app_tile("Commentary", "Using GPT to generate personalized investment commentary at scale.", "Add"),
            app_tile("Optimiser", "Quantitative risk to enhance risk-adjusted return.", "Add"),
            app_tile("Voice", "Supports meetings in person or over calls for meeting summaries and actionable document drafting.", "Open"),
            app_tile("E2C", "Enables a digital meeting proposition through an integrated video and CASS custody service.", "Add")
        )
    )
    return Titled('Client Workspace', page)

serve()