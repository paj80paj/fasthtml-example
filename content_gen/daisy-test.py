from fasthtml.common import *

# Set up the app with Tailwind CSS and Daisy UI
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
)
app, rt = fast_app(hdrs=hdrs, live=True)

@rt("/")
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
        
        # New components from DaisyUI

        # Accordion component
        P("Accordion: Collapsible content panels"),
        Div(
            Div(
                Input(type="radio", name="my-accordion-1", checked=True),
                Div("Click to open this one and close others", cls="collapse-title text-xl font-medium"),
                Div("Hello, I'm the content inside the accordion", cls="collapse-content"),
                cls="collapse collapse-arrow bg-base-200"
            ),
            cls="mb-4"
        ),

        # Avatar component
        P("Avatar: Display user profile images"),
        Div(
            Div(
                Img(src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg"),
                cls="w-24 rounded-full"
            ),
            cls="avatar mb-4"
        ),

        # Badge component
        P("Badge: Small status descriptors"),
        Div(
            Div("Badge", cls="badge"),
            Div("Badge", cls="badge badge-neutral"),
            Div("Badge", cls="badge badge-primary"),
            cls="mb-4"
        ),

        # Bottom navigation component
        P("Bottom navigation: Mobile-friendly navigation bar"),
        Div(
            A("Home", cls="active"),
            A("Search"),
            A("Profile"),
            cls="btm-nav mb-4"
        ),

        # Breadcrumbs component
        P("Breadcrumbs: Show navigation hierarchy"),
        Div(
            Ul(
                Li(A("Home")),
                Li(A("Documents")),
                Li("Add Document"),
                cls="breadcrumbs text-sm"
            ),
            cls="mb-4"
        ),

        # Button group component
        P("Button group: Group related actions"),
        Div(
            Div(
                Input(type="radio", name="options", data_title="Left", cls="btn"),
                Input(type="radio", name="options", data_title="Center", cls="btn", checked=True),
                Input(type="radio", name="options", data_title="Right", cls="btn"),
                cls="join"
            ),
            cls="mb-4"
        ),

        # Chat bubble component
        P("Chat bubble: Display conversation messages"),
        Div(
            Div(
                Div("How are you?", cls="chat-bubble"),
                cls="chat-start"
            ),
            Div(
                Div("I'm doing great, thanks for asking!", cls="chat-bubble"),
                cls="chat-end"
            ),
            cls="chat chat-start mb-4"
        ),

        # Collapse component
        P("Collapse: Toggle visibility of content"),
        Div(
            Input(type="checkbox"),
            Div("Click me to show/hide content", cls="collapse-title text-xl font-medium"),
            Div("Hello, I'm the collapsible content", cls="collapse-content"),
            cls="collapse bg-base-200 mb-4"
        ),

        # Divider component
        P("Divider: Separate content sections"),
        Div(
            "Above content",
            Div("OR", cls="divider"),
            "Below content",
            cls="mb-4"
        ),

        # Footer component
        P("Footer: Page footer with multiple columns"),
        Footer(
            Div(
                Div(
                    Span("Footer", cls="footer-title"),
                    A("Link 1"),
                    A("Link 2"),
                    A("Link 3"),
                ),
                Div(
                    Span("Social", cls="footer-title"),
                    A("Twitter"),
                    A("Instagram"),
                    A("Facebook"),
                ),
            ),
            cls="footer p-10 bg-neutral text-neutral-content mb-4"
        ),

        # Indicator component
        P("Indicator: Show a badge on another element"),
        Div(
            Div(
                Span("99+", cls="indicator-item badge badge-secondary"),
                Button("Inbox", cls="btn"),
            ),
            cls="indicator mb-4"
        ),

        # Kbd (Keyboard) component
        P("Kbd: Display keyboard key or shortcut"),
        Div(
            Kbd("ctrl"),
            "+",
            Kbd("shift"),
            "+",
            Kbd("del"),
            cls="mb-4"
        ),

        # Link component
        P("Link: Styled anchor tag"),
        Div(
            A("Simple link", cls="link"),
            A("Colored link", cls="link link-primary"),
            A("Link with hover", cls="link link-hover"),
            cls="mb-4"
        ),

        # Loading component
        P("Loading: Indicate content is being loaded"),
        Div(
            Span("Loading...", cls="loading loading-dots loading-lg"),
            cls="mb-4"
        ),

        # Menu component
        P("Menu: Vertical menu for navigation"),
        Ul(
            Li(A("Item 1")),
            Li(A("Item 2")),
            Li(A("Item 3")),
            cls="menu bg-base-200 w-56 rounded-box mb-4"
        ),

        # Navbar component
        P("Navbar: Responsive navigation header"),
        Div(
            Div(
                A("daisyUI", cls="btn btn-ghost normal-case text-xl"),
                cls="flex-1"
            ),
            Div(
                Ul(
                    Li(A("Home")),
                    Li(A("About")),
                    Li(A("Contact")),
                    cls="menu menu-horizontal px-1"
                ),
                cls="flex-none"
            ),
            cls="navbar bg-base-100 mb-4"
        ),

        # Pagination component
        P("Pagination: Navigate through pages"),
        Div(
            Button("«", cls="join-item btn btn-outline"),
            Button("Page 22", cls="join-item btn btn-outline"),
            Button("»", cls="join-item btn btn-outline"),
            cls="join mb-4"
        ),

        # Radial progress component
        P("Radial progress: Circular progress indicator"),
        Div(
            Div("70%", cls="radial-progress", style="--value:70;"),
            cls="mb-4"
        ),

        # Select component
        P("Select: Dropdown for selecting options"),
        Div(
            Select(
                Option("Pick your favorite Simpson"),
                Option("Homer"),
                Option("Marge"),
                Option("Bart"),
                Option("Lisa"),
                Option("Maggie"),
                cls="select select-bordered w-full max-w-xs"
            ),
            cls="mb-4"
        ),

        # Stat component
        P("Stat: Display statistics"),
        Div(
            Div(
                Div(
                    Div("Total Page Views", cls="stat-title"),
                    Div("89,400", cls="stat-value"),
                    Div("21% more than last month", cls="stat-desc"),
                ),
                cls="stat"
            ),
            cls="stats shadow mb-4"
        ),

        # Steps component
        P("Steps: Show progress through a series of steps"),
        Ul(
            Li("Step 1", cls="step step-primary"),
            Li("Step 2", cls="step step-primary"),
            Li("Step 3", cls="step"),
            Li("Step 4", cls="step"),
            cls="steps mb-4"
        ),

        # Timeline component
        P("Timeline: Display a series of events"),
        Ul(
            Li(
                Div(
                    Div("First event", cls="timeline-start"),
                    Div(cls="timeline-middle"),
                    Div("Event details", cls="timeline-end timeline-box"),
                    Hr(),
                ),
            ),
            Li(
                Div(
                    Div("Second event", cls="timeline-start"),
                    Div(cls="timeline-middle"),
                    Div("More details", cls="timeline-end timeline-box"),
                    Hr(),
                ),
            ),
            cls="timeline mb-4"
        ),

        cls="p-4 space-y-4"
    )

    # Explanation for one component (Accordion)
    explanation = Div(
        H2("Accordion Component Explanation", cls="text-xl font-bold mb-2"),
        P("The Accordion component is used to create collapsible content panels. It's particularly useful when you want to present a large amount of information in a compact space, allowing users to expand only the sections they're interested in."),
        P("Use cases for the Accordion component include:"),
        Ul(
            Li("FAQ sections where questions can be expanded to reveal answers"),
            Li("Product details pages where different aspects of the product can be collapsed"),
            Li("Settings menus where options are grouped and can be expanded for more details"),
            Li("Navigation menus with sub-categories that can be expanded"),
            cls="list-disc list-inside mb-2"
        ),
        P("The Accordion helps improve user experience by reducing clutter and allowing users to focus on specific content as needed."),
        cls="bg-base-200 p-4 rounded-lg mb-4"
    )
 
    return Titled("Daisy UI Test",
        Body(
            Div(content, explanation, cls="min-h-screen"),
            data_theme="corporate"
        )
    )

serve()