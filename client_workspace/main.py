from fasthtml.common import *
from claudette import *
import os
from starlette.staticfiles import StaticFiles

print(os.getcwd())  # Prints the current working directory

# Set up the app
hdrs = (
    Link(rel="stylesheet", href="/static/styles.css"),  # Ensure styles.css contains necessary styles
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
)
app = FastHTML(hdrs=hdrs, ws_hdr=True)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up a chat model (https://claudette.answer.ai/)
cli = Client(models[-1])
sp = "You are a helpful and concise financial advisor assistant."
messages = []

def app_tile(title, description, action, href="#"):
    return Div(cls="grid-item")(
        H3(title),
        P(description),
        A(action, href=href, cls="button")
    )

def sidebar():
    return Div(cls="sidebar")(
        Div("[ * ]"),
        Div("[ # ]"),
        Div("[ @ ]"),
        Div("[ $ ]"),
        Div("[ % ]")
    )

# Chat message component (renders a chat bubble)
def ChatMessage(msg):
    bubble_class = "chat-bubble-primary" if msg['role'] == 'user' else 'chat-bubble-secondary'
    chat_class = "chat-end" if msg['role'] == 'user' else 'chat-start'
    return Div(Div(msg['role'], cls="chat-header"),
               Div(msg['content'], cls=f"chat-bubble {bubble_class}"),
               cls=f"chat {chat_class}")

# The input field for the user message
def ChatInput():
    return Input(type="text", name='msg', id='msg-input',
                 placeholder="Ask your AI Digital Assistant a question about any of your clients or prospects.",
                 cls="input input-bordered w-full", hx_swap_oob='true')

@app.get
def index():
    page = Div(cls="container", data_theme="corporate")(
        # Apply corporate theme
        sidebar(),
        Div(cls="main-content")(
            H1("WealthAI", cls="text-2xl font-bold"),
            H2("Client Workspace", cls="text-lg font-medium"),
            Div(cls="grid-container gap-4 sm:grid-cols-2 lg:grid-cols-3")(
                app_tile("ClientComm", "An AI-powered digital assistant, combining natural language processing with client interactions.", "Open", href="/clientcomm"),
                app_tile("Monitor", "Automated monitoring of all client portfolios to warn of portfolio in distress.", "Open"),
                app_tile("Commentary", "Using GPT to generate personalized investment commentary at scale.", "Add"),
                app_tile("Optimiser", "Quantitative risk to enhance risk-adjusted return.", "Add"),
                app_tile("Voice", "Supports meetings in person or over calls for meeting summaries and actionable document drafting.", "Open"),
                app_tile("E2C", "Enables a digital meeting proposition through an integrated video and CASS custody service.", "Add")
            )
        )
    )
    return Titled('Client Workspace', page)

@app.get("/clientcomm")
def clientcomm():
    page = Div(cls="container flex", data_theme="corporate")(
        # Apply corporate theme
        Div(cls="w-1/2")(
            H1("ClientComm", cls="text-2xl font-bold"),
            Div(cls="chat-container mt-4")(
                Div(cls="chat-input mb-4")(
                    Form(Group(ChatInput(), Button("Go!", cls="btn btn-primary")),
                        ws_send=True, hx_ext="ws", ws_connect="/wscon",
                        cls="flex justify-between items-center",
                    )
                ),
                Div(cls="chat-tabs mb-4")(
                    Div(cls="tab tab-active", id="recent-tab")("Recent Questions"),
                    Div(cls="tab", id="common-tab")("Ideas for Questions")
                ),
                Div(cls="chat-suggestions")(  # Changed according to feedback
                    P("Here are some ideas for questions:", cls="mb-2"),
                    Ul(cls="list-disc pl-5")(
                        Li("Are you still worried about the market volatility?"),
                        Li("Congratulations on the baby!"),
                        Li("How are you getting on with the tax discussion?")
                    )
                ),
                Div(id="chatlist", cls="chat-messages"),  # Add this line to create a container for chat messages
                Div(cls="chat-footer mt-4 flex items-center")(
                    Div(cls="user-icon mr-2")("👤")
                )
            )
        ),
        Div(cls="w-1/2 mb-8 relative")(
            A("Back to Client Workspace", href="/", cls="btn btn-secondary absolute right-0 mt-4 mr-4"),  # Link as a button
            H2("Upcoming Meeting", cls="text-2xl font-bold mb-4"),
            P("Heads up! You have a meeting with *John Doe* in an hour. Here are some things to note:", cls="mb-2"),
            Ul(cls="list-disc pl-5")(
                Li(B("Portfolio Alert:") + " *Tech Ventures* underperformed by 15% this quarter."),
                Li(B("Unresolved Issue:") + " *John Doe* has an open support ticket about tax implications."),
                Li(B("Client Concern:") + " Recent email from *Jane Smith* expressed worry about market volatility—interested in low-risk options."),
                Li(B("Product Risk:") + " *Alpha Fund* has been reclassified as higher risk."),
                Li(B("Compliance Reminder:") + " Your compliance training renewal is due in two weeks."),
                Li(B("Consumer Duty:") + " Ensure the client understands the value and pricing of their products per FCA guidelines."),
                Li(B("Life Event:") + " *Jane Smith* added a new dependent—might impact financial goals.")
            )
        )
    )
    return Titled('ClientComm', page)

@app.ws('/wscon')
async def ws(msg: str, send):
    if msg.strip():
        # Send the user message to the user (updates the UI right away)
        messages.append({"role": "user", "content": msg.rstrip()})
        await send(Div(ChatMessage(messages[-1]), hx_swap_oob='beforeend', id="chatlist"))

        # Send the clear input field command to the user
        await send(ChatInput())

        # Get and send the model response
        r = cli(messages, sp=sp)
        if contents(r).strip():
            messages.append({"role": "assistant", "content": contents(r)})
            await send(Div(ChatMessage(messages[-1]), hx_swap_oob='beforeend', id="chatlist"))

serve()