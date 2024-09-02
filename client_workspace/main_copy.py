# Importing necessary modules from FastHTML and other libraries
from fasthtml.common import *
from claudette import *  # Custom module, possibly for AI or language model usage
import os  # Standard library for operating system interactions
from starlette.staticfiles import StaticFiles  # For serving static files

# Setting up HTTP headers for styling with Tailwind CSS and DaisyUI
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),  # Link to Tailwind CSS via CDN
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css") # Link to DaisyUI styles 
)

# Initializing the FastHTML application with headers and enabling websocket headers
app = FastHTML(hdrs=hdrs, ws_hdr=True)

# Mounting a directory named "static" to serve static files like images, stylesheets, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setting up a chat model client using the last available model
cli = Client(models[-1])  # Assumes a list of models is defined elsewhere
sp = "You are a helpful and concise financial advisor assistant."  # System prompt for AI assistant
messages = []  # List to store chat messages

def app_tile(title, description, action, href="#", icon_path=""):
    # Creates a tile UI component to display app details and actions
    return Div(cls="grid-item bg-white p-4 rounded-lg shadow-md m-4 flex")(
        Img(src=icon_path, cls="mr-4 w-12 h-12 self-start"),  # Display app icon
        Div(
            H3(title, cls="text-xl font-bold mb-2 text-left"),  # App title
            P(description, cls="mb-2 text-left"),  # Short description of the app
            Div(cls="flex justify-between")(
                A("Learn more", href=href, cls="text-blue-500 underline text-sm"),  # Link to learn more
                A(action, href=href, cls="btn bg-green-500 text-white")  # Button for primary action (e.g., Open)
            )
        )
    )

def sidebar():
    # Creates a sidebar of navigation icons for different app functionalities
    return Div(cls="sidebar bg-dark-navy p-4 min-h-screen flex flex-col items-center text-white")(
        Img(src="/static/Alpha Enhancer2.png", cls="mb-4 w-8 h-8"),  # Navigation icon
        Img(src="/static/commentary2.png", cls="mb-4 w-8 h-8"),
        Img(src="/static/Compliance2.png", cls="mb-4 w-8 h-8"),
        Img(src="/static/OCIO2.png", cls="mb-4 w-8 h-8"),
        Img(src="/static/Voice2.png", cls="mb-4 w-8 h-8")
    )

def ChatMessage(msg):
    # Creates a chat message bubble
    bubble_class = "chat-bubble-primary" if msg['role'] == 'user' else 'chat-bubble-secondary'
    chat_class = "chat-end" if msg['role'] == 'user' else 'chat-start'
    return Div(Div(msg['role'], cls="chat-header"),
               Div(msg['content'], cls=f"chat-bubble {bubble_class}"),
               cls=f"chat {chat_class}")

def ChatInput():
    # Creates an input field for sending chat messages
    return Input(type="text", name='msg', id='msg-input',
                 placeholder="Ask Algernon anything",
                 cls="input input-bordered w-full", hx_swap_oob='true')

@app.get
def index():
    # Main page displaying client workspace with various applications
    page = Div(cls="flex bg-white min-h-screen")(
        sidebar(),  # Include sidebar component
        Div(cls="container mx-auto p-6 bg-gray-100")(
            Div(cls="flex justify-between items-center mb-4")(
                H1("Client Workspace", cls="text-4xl font-bold text-center text-dark-navy")
            ),
            Div(cls="main-content grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8")(
                app_tile("ClientComm", "An AI powered digital assistant, combining natural language processing with advanced machine learning.", "Open", href="/clientcomm", icon_path="/static/Client Comm1.png"),
                app_tile("Monitor", "Automated monitoring of all client portfolios to warn of portfolio in distress or approaching distress.", "Open", icon_path="/static/Monitor1.png"),
                app_tile("Commentary", "Using Generative AI to create personalized investment commentary at scale.", "Add", icon_path="/static/commentary1.png"),
                app_tile("Optimiser", "Combines AI and quantitative risk to enhance the investment decision-making process.", "Add", icon_path="/static/Optimiser1.png"),
                app_tile("Voice", "Supports meetings in person or over video call creating summaries and actionable document drafting.", "Open", icon_path="/static/Voice1.png"),
                app_tile("E2C", "Enables a digital investing proposition through an FCA-regulated administration and CASS custody service.", "Add", icon_path="/static/OCIO1.png"),
                app_tile("Pension Pot", "Manage pension planning for your clients pension plan", "Add", icon_path="/static/Pension Pot1.png"),
                app_tile("Compliance (UK)", "Monitor client status and suitability (risk), sales (appropriate), product, consumer duty status", "Add", icon_path="/static/Compliance1.png")
            )
        )
    )
    return Titled('WealthAI', page)

@app.get("/clientcomm")
def clientcomm():
    # Displays the Client Communication Application with chat and meeting information
    page = Div(cls="flex bg-white min-h-screen")(
        sidebar(),
        Div(cls="container", data_theme="corporate")(
            Div(cls="absolute right-0 top-0 mt-4 mr-4")(
                A("Back", href="/", cls="btn bg-blue-800 text-white")
            ),
            H2("Client Comms", cls="text-3xl font-bold mb-4"),
            Div(cls="flex bg-gray-100 p-6 m-4")(
                Div(cls="w-1/2")(
                    Div(cls="chat-container mt-4")(
                        Div(cls="chat-input mb-4")(
                            Form(
                                Div(cls="flex items-center")(
                                    ChatInput(),
                                    Button("Go!", cls="btn bg-blue-800 text-white ml-2")
                                ),
                                ws_send=True, hx_ext="ws", ws_connect="/wscon",
                                cls="flex justify-between items-center",
                            )
                        ),
                        Div(id="chatlist", cls="chat-messages"),  # Chat message container
                        Div(cls="chat-footer mt-4 flex items-center")(
                            Div(cls="user-icon mr-2")
                        )
                    )
                ),
                Div(cls="w-1/2 mb-8 relative")(
                    H2("Upcoming Meeting", cls="text-2xl font-bold mb-4"),
                    P("Heads up! You have a meeting with *John Doe* in an hour. Here are some things to note:", cls="mb-2"),
                    Ul(cls="list-disc pl-5 text-sm space-y-4")(
                        Li(Span("Portfolio Alert:", cls="font-bold") + Span(" *Tech Ventures* underperformed by 15% this quarter.")),
                        Li(Span("Unresolved Issue:", cls="font-bold") + Span(" *John Doe* has an open support ticket about tax implications.")),
                        Li(Span("Client Concern:", cls="font-bold") + Span(" Recent email from *Jane Smith* expressed worry about market volatility—interested in low-risk options.")),
                        Li(Span("Product Risk:", cls="font-bold") + Span(" *Alpha Fund* has been reclassified as higher risk.")),
                        Li(Span("Compliance Reminder:", cls="font-bold") + Span(" Your compliance training renewal is due in two weeks.")),
                        Li(Span("Consumer Duty:", cls="font-bold") + Span(" Ensure the client understands the value and pricing of their products per FCA guidelines.")),
                        Li(Span("Life Event:", cls="font-bold") + Span(" *Jane Smith* added a new dependent—might impact financial goals."))
                    ),
                    Div(cls="mt-4")(
                        P("Suggested client talking points:", cls="mb-2 font-bold"),
                        Ul(cls="list-disc pl-5 italic space-y-4")(
                            Li("Are you still worried about the market volatility?"),
                            Li("Congratulations on the baby!"),
                            Li("How are you getting on with the tax discussion?")
                        )
                    )
                )
            )
        )
    )
    return Titled('Wealth AI', page)

@app.ws('/wscon')
async def ws(msg: str, send):
    # WebSocket handler for chat functionality
    if msg.strip():  # Check if the message is not empty
        messages.append({"role": "user", "content": msg.rstrip()})
        await send(Div(ChatMessage(messages[-1]), hx_swap_oob='beforeend', id="chatlist"))

        # Clears the input field
        await send(ChatInput())

        # Generates and sends a response from the AI assistant
        r = cli(messages, sp=sp)
        if contents(r).strip():  # Check if the response content is not empty
            messages.append({"role": "assistant", "content": contents(r)})
            await send(Div(ChatMessage(messages[-1]), hx_swap_oob='beforeend', id="chatlist"))

# Run the FastHTML server
serve()
