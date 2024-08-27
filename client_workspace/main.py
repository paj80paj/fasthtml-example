from fasthtml.common import *
from claudette import *
import os
from starlette.staticfiles import StaticFiles

print(os.getcwd())  # Prints the current working directory

# Set up the app
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css"),
    # Link(rel="stylesheet", href="/static/styles.css")
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
    page = Div(cls="container")(
        sidebar(),
        Div(cls="main-content")(
            H1("WealthAI"),
            H2("Client Workspace"),
            Div(cls="grid-container")(
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
    page = Div(cls="container")(
        H1("ClientComm"),
        Div(cls="chat-container")(
            Div(cls="chat-input")(
                Form(Group(ChatInput(), Button("Go!", cls="button")),
                    ws_send=True, hx_ext="ws", ws_connect="/wscon",
                    cls="flex space-x-2",
                )
            ),
            Div(cls="chat-tabs")(
                Div(cls="tab active", id="recent-tab")("Recent Questions"),
                Div(cls="tab", id="common-tab")("Common Questions")
            ),
            Div(cls="chat-messages", id="chatlist")(
                *[ChatMessage(msg) for msg in messages]
            ),
            Div(cls="chat-footer")(
                Div(cls="user-icon")("👤"),
                Div(cls="message-count")("Three clients have asked your assistant 13 questions.")
            )
        )
    )
    return Titled('ClientComm', page)

@app.ws('/wscon')
async def ws(msg:str, send):
    # Send the user message to the user (updates the UI right away)
    messages.append({"role":"user", "content":msg.rstrip()})
    await send(Div(ChatMessage(messages[-1]), hx_swap_oob='beforeend', id="chatlist"))

    # Send the clear input field command to the user
    await send(ChatInput())

    # Get and send the model response
    r = cli(messages, sp=sp)
    messages.append({"role":"assistant", "content":contents(r)})
    await send(Div(ChatMessage(messages[-1]), hx_swap_oob='beforeend', id="chatlist"))

serve()