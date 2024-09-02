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
            Div(cls="absolute right-0 top-0 mt-4 mr-4 ")(
                A("Back", href="/", cls="btn bg-blue-800 text-white")
            ),
            Div(cls="flex flex-1 py-5 px-6 gap-6")(
                # Left side - Client info, Chat button, and Chat container
                Div(cls="layout-content-container flex flex-col w-80")(
                    # Client info at the top left
                    Div(cls="flex items-center mb-4")(
                        Div(style='background-image: url("https://cdn.usegalileo.ai/stability/4d0f19f3-b727-4b34-986f-6da507480b2d.png");', 
                            cls='bg-center bg-no-repeat aspect-square bg-cover rounded-xl min-h-32 w-32 mr-4'),
                        Div(cls="flex flex-col")(
                            P("John Doe", cls="text-[#111517] text-[22px] font-bold leading-tight tracking-[-0.015em]"),
                            P("Age 50, Male", cls="text-[#647987] text-base font-normal leading-normal"),
                            P("Primary client", cls="text-[#647987] text-base font-normal leading-normal")
                        )
                    ),
                    # Chat container
                    Div(cls="flex-grow overflow-y-auto mb-4 border rounded p-2", style="height: 300px;")(
                        Div(id="chat-messages")
                    ),
                    # Chat input
                    Form(cls="flex", hx_post="/chat", hx_target="#chat-messages", hx_swap="beforeend")(
                        Input(type="text", name="message", placeholder="Ask Algernon anything", cls="flex-grow p-2 border rounded-l"),
                        Button("Send", type="submit", cls="bg-blue-500 text-white p-2 rounded-r")
                    )
                ),
                # Right side - Meeting preparation
                Div(cls="layout-content-container flex flex-col max-w-[960px] flex-1")(
                    H1("Prepare for client meeting", cls="text-4xl font-bold text-center text-dark-navy mb-4"),
                    P("Next meeting: May 14, 2023", cls="text-center mb-6"),
                    # Meeting items
                    H2("Meeting items", cls="text-2xl font-bold mb-4"),
                    Div(cls="space-y-4")(
                        meeting_item("Client Actions", "Sign and return the investment agreement."),
                        meeting_item("Financial Events", "Tax filing deadline on April 15th."),
                        meeting_item("Market Events", "Stock market drop affecting portfolio value."),
                        meeting_item("Regulatory Events", "New pension regulations effective next month."),
                        meeting_item("Insurance Updates", "Life insurance policy review due."),
                        meeting_item("Compliance Alerts", "Portfolio needs adjustment for compliance.")
                    ),
                    # Next steps
                    H2("Next steps", cls="text-2xl font-bold mt-8 mb-4"),
                    Div(cls="space-y-4")(
                        next_step("Client Actions", "Review and sign the investment agreement"),
                        next_step("Our Actions", "Prepare the quarterly performance report")
                    ),
                    # Record Meeting button
                    Div(cls="mt-8")(
                        Button("Record Meeting", cls="w-full bg-blue-500 text-white py-2 rounded")
                    )
                )
            )
        )
    )
    return Titled('WealthAI - Client Comms', page)

def meeting_item(title, description):
    return Div(cls="flex items-center gap-4 bg-white px-4 min-h-[72px] py-2 justify-between")(
        Div(cls="flex flex-col justify-center")(
            P(title, cls="text-[#111517] text-base font-medium leading-normal line-clamp-1"),
            P(description, cls="text-[#647987] text-sm font-normal leading-normal line-clamp-2")
        ),
        Div(cls="shrink-0")(
            Button("Review", cls="flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#f0f3f4] text-[#111517] text-sm font-medium leading-normal w-fit")
        )
    )

def next_step(title, description):
    return Div(cls="flex items-center gap-4 bg-white px-4 min-h-[72px] py-2 justify-between")(
        Div(cls="flex flex-col justify-center")(
            P(title, cls="text-[#111517] text-base font-medium leading-normal line-clamp-1"),
            P(description, cls="text-[#647987] text-sm font-normal leading-normal line-clamp-2")
        ),
        Div(cls="shrink-0")(
            Div(cls="text-[#111517] flex size-7 items-center justify-center")(
                Svg(xmlns="http://www.w3.org/2000/svg", width="24px", height="24px", fill="currentColor", viewbox="0 0 256 256")(
                    Path(d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z")
                )
            )
        )
    )

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

@app.post("/chat")
def chat(message: str):
    messages.append({"role": "user", "content": message})
    r = cli(messages, sp=sp)
    ai_response = contents(r)
    messages.append({"role": "assistant", "content": ai_response})
    return Div(
        ChatMessage(messages[-2]),  # User message
        ChatMessage(messages[-1])   # AI response
    )

serve()
