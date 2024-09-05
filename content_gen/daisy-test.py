from fasthtml.common import *

# Set up the app with Tailwind CSS and Daisy UI
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
)
app = FastHTML(hdrs=hdrs, live=True)

@app.get("/")
def get():
    content = Div(
        # Card component
        P("Card: A self-contained piece of information"),
        Div(
            Div(
                H2("Card title", cls="card-title"),
                P("If a dog chews shoes whose shoes does he choose?"),
                Div(
                    Button("Buy Now", cls="btn btn-primary"),
                    Button("More info", cls="btn btn-ghost"),
                    cls="card-actions justify-end"
                ),
                cls="card-body"
            ),
            cls="card w-96 bg-base-100 shadow-xl mb-4"
        ),
        
        # Alert component
        P("Alert: Displays important messages or notifications"),
        Div(
            Svg(viewBox="0 0 24 24", cls="stroke-info shrink-0 w-6 h-6", contents=[
                Path(stroke_linecap="round", stroke_linejoin="round", stroke_width="2", d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z")
            ]),
            Span("New software update available"),
            cls="alert alert-info mb-4"
        ),
        
        # Tabs component
        P("Tabs: Organize content into different sections"),
        Div(
            cls="tabs tabs-lifted mb-4",
            role="tablist",
            contents=[
                Input(type="radio", name="my_tabs_2", role="tab", cls="tab", checked=True, contents=[
                    Div("Tab 1", cls="tab-content p-10")
                ]),
                Input(type="radio", name="my_tabs_2", role="tab", cls="tab", contents=[
                    Div("Tab 2", cls="tab-content p-10")
                ]),
                Input(type="radio", name="my_tabs_2", role="tab", cls="tab", contents=[
                    Div("Tab 3", cls="tab-content p-10")
                ])
            ]
        ),
        
        # Dropdown menu
        P("Dropdown: Compact navigation or selection options"),
        Div(
            Label("Select", tabindex="0", cls="btn m-1"),
            Ul(
                Li(A("Item 1")),
                Li(A("Item 2")),
                tabindex="0",
                cls="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52"
            ),
            cls="dropdown mb-4"
        ),
        
        # Modal dialog
        P("Modal Dialog: Click to open a popup that requires user interaction"),
        Div(
            Button("open modal", cls="btn", onclick="my_modal.showModal()"),
            Dialog(
                Div(
                    H3("Hello!", cls="font-bold text-lg"),
                    P("Press ESC key or click outside to close"),
                    Div(
                        Form(
                            Button("Close", cls="btn"),
                            method="dialog"
                        ),
                        cls="modal-action"
                    ),
                    cls="modal-box"
                ),
                id="my_modal",
                cls="modal"
            ),
            cls="mb-4"
        ),
        
        # Toggle component
        P("Toggle: Switch between two states (on/off)"),
        Input(type="checkbox", cls="toggle", checked=True),
        
        # Rating component
        P("Rating: Select a star rating (1-5 stars)"),
        Div(
            Input(type="radio", name="rating-1", cls="mask mask-star"),
            Input(type="radio", name="rating-1", cls="mask mask-star", checked=True),
            Input(type="radio", name="rating-1", cls="mask mask-star"),
            Input(type="radio", name="rating-1", cls="mask mask-star"),
            Input(type="radio", name="rating-1", cls="mask mask-star"),
            cls="rating mb-4"
        ),
        
        # Progress bar
        P("Progress Bar: Visual indicator of task completion (70% complete)"),
        Progress(cls="progress progress-primary w-56", value="70", max="100"),
        
        # Carousel
        P("Carousel: Slideshow for cycling through images or content"),
        Div(
            Div(id="slide1", cls="carousel-item relative w-full", contents=[
                Img(src="https://daisyui.com/images/stock/photo-1625726411847-8cbb60cc71e6.jpg", cls="w-full"),
                Div(
                    A(href="#slide4", cls="btn btn-circle", contents="❮"),
                    A(href="#slide2", cls="btn btn-circle", contents="❯"),
                    cls="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2"
                )
            ]),
            cls="carousel w-full"
        ),
        
        cls="p-4 space-y-4"
    )
    return Titled("Daisy UI Test", Html(lang="en", contents=[
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title("Daisy UI Test")
        ),
        Body(
            Div(content, cls="min-h-screen"),
            data_theme="corporate"
        )
    ]))

serve()