from fasthtml.common import *
from claudette import *
import os
from starlette.staticfiles import StaticFiles

print(os.getcwd())  # Prints the current working directory

# Set up the app
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
)
app = FastHTML(hdrs=hdrs, ws_hdr=True)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up a chat model
cli = Client(models[-1])
sp = "You are a helpful and concise financial advisor assistant."
messages = []

def app_tile(title, description, action, href="#", icon_path=""):
    return Div(cls="grid-item bg-white p-4 rounded-lg shadow-md m-4 flex")(
        Img(src=icon_path, cls="mr-4 w-12 h-12 self-start"),
        Div(
            H3(title, cls="text-xl font-bold mb-2 text-left"),
            P(description, cls="mb-2 text-left"),
            Div(cls="flex justify-between")(
                A("Learn more", href=href, cls="text-blue-500 underline text-sm"),
                A(action, href=href, cls="btn bg-green-500 text-white")
            )
        )
    )

def sidebar():
    return Div(cls="sidebar bg-dark-navy p-4 min-h-screen flex flex-col items-center text-white")(
        Img(src="/static/Alpha Enhancer2.png", cls="mb-4 w-8 h-8"),
        Img(src="/static/commentary2.png", cls="mb-4 w-8 h-8"),
        Img(src="/static/Compliance2.png", cls="mb-4 w-8 h-8"),
        Img(src="/static/OCIO2.png", cls="mb-4 w-8 h-8"),
        Img(src="/static/Voice2.png", cls="mb-4 w-8 h-8")
    )

def ChatMessage(msg):
    bubble_class = "chat-bubble-primary" if msg['role'] == 'user' else 'chat-bubble-secondary'
    chat_class = "chat-end" if msg['role'] == 'user' else 'chat-start'
    return Div(Div(msg['role'], cls="chat-header"),
               Div(msg['content'], cls=f"chat-bubble {bubble_class}"),
               cls=f"chat {chat_class}")

def ChatInput():
    return Input(type="text", name='msg', id='msg-input',
                 placeholder="Ask Algernon anything",
                 cls="input input-bordered w-full", hx_swap_oob='true')

@app.get
def index():
    page = Div(cls="flex bg-white min-h-screen")(
        sidebar(),
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
                        Div(id="chatlist", cls="chat-messages"),  # Container for chat messages
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
