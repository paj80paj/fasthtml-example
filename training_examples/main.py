import fasthtml.common as fh

# Set up the app with Tailwind CSS and DaisyUI
hdrs = (
    fh.Script(src="https://cdn.tailwindcss.com"),
    fh.Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
)
app, rt = fh.fast_app(hdrs=hdrs, live=True)

@rt("/")
def get():
    return fh.Div(
        fh.Header(
            fh.Nav(
                fh.A("Home", href="/", class_="btn btn-ghost normal-case text-xl"),
                fh.A("About", href="/about", class_="btn btn-ghost normal-case text-xl"),
                fh.A("Services", href="/services", class_="btn btn-ghost normal-case text-xl"),
                fh.A("Contact", href="/contact", class_="btn btn-ghost normal-case text-xl"),
                class_="navbar bg-gradient-to-r from-purple-500 to-pink-500 text-white"
            ),
            class_="header"
        ),
        fh.Main(
            fh.Div(
                fh.H1("Welcome to Our Company", class_="text-6xl font-extrabold text-center mt-10"),
                fh.P("We provide the best services to help your business grow.", class_="py-6 text-center text-lg"),
                fh.Img(src="https://picsum.photos/800/400", alt="Hero Image", class_="rounded-lg shadow-2xl mx-auto"),
                fh.Button("Learn More", class_="btn btn-primary mt-6 mx-auto block"),
                class_="hero min-h-screen bg-gradient-to-r from-blue-500 to-green-500 flex-col text-white"
            ),
            class_="main-content"
        ),
        fh.Div(
            fh.Div(
                fh.Figure(
                    fh.Img(src="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg", alt="Shoes")
                ),
                fh.Div(
                    fh.H2("Shoes!", class_="card-title"),
                    fh.P("If a dog chews shoes whose shoes does he choose?"),
                    fh.Div(
                        fh.Button("Buy Now", class_="btn btn-primary"),
                        class_="card-actions justify-end"
                    ),
                    class_="card-body"
                ),
                class_="card w-96 bg-base-100 shadow-xl mx-auto mt-10"
            ),
            class_="flex justify-center"
        ),
        fh.Div(
            fh.H2("Try them:", class_="text-2xl font-bold text-center mt-10"),
            fh.Div(
                *[
                    fh.Div(
                        fh.Div(
                            fh.H3(theme.capitalize(), class_="text-lg font-bold"),
                            fh.Div(
                                fh.Span("A", class_="text-primary"),
                                fh.Span("A", class_="text-secondary"),
                                fh.Span("A", class_="text-accent"),
                                fh.Span("A", class_="text-neutral"),
                                class_="flex space-x-2"
                            ),
                            class_="p-4"
                        ),
                        class_="w-40 h-24 bg-base-100 shadow-lg rounded-lg m-2",
                        data_theme=theme
                    ) for theme in [
                        "light", "dark", "cupcake", "bumblebee", "emerald", "corporate", "synthwave", "retro",
                        "cyberpunk", "valentine", "halloween", "garden", "forest", "aqua", "lofi", "pastel",
                        "fantasy", "wireframe", "black", "luxury", "dracula", "cmyk", "autumn", "business",
                        "acid", "lemonade", "night", "coffee", "winter", "dim", "nord", "sunset"
                    ]
                ],
                class_="flex flex-wrap justify-center"
            ),
            class_="theme-showcase"
        ),
        fh.Footer(
            fh.P("© 2023 Our Company. All rights reserved.", class_="text-center"),
            class_="footer p-4 bg-gray-800 text-white"
        ),
        class_="container mx-auto",
        data_theme="corporate"  # Set the data-theme attribute to 'corporate'
    )

fh.serve()
