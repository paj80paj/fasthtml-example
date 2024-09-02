from fasthtml.common import *

# Set up the app with Tailwind CSS and DaisyUI
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css")
)
app, rt = fast_app(hdrs=hdrs, live=True)

@rt("/")
def get():
    themes = [
        'light', 'dark', 'cupcake', 'bumblebee', 'emerald', 'corporate', 'synthwave', 'retro', 'cyberpunk', 'valentine',
        'halloween', 'garden', 'forest', 'aqua', 'lofi', 'pastel', 'fantasy', 'wireframe', 'black', 'luxury', 'dracula',
        'cmyk', 'autumn', 'business', 'acid', 'lemonade', 'night', 'coffee', 'winter', 'dim', 'nord', 'sunset'
    ]
    
    def create_div(theme):  # Function to create a div element for each theme
        return Div(
            Div(
                Div(
                    Div('top4',cls='bg-base-200 col-start-1 row-span-2 row-start-1'),  # Background div for theme preview with base-200 color, positioned at the start of the first column and spanning 2 rows
                    Div(cls='bg-base-300 col-start-1 row-start-3'),  # Another background div for theme preview with base-300 color
                    Div(
                        Div(theme, cls='font-bold'),  # Display the theme name in bold
                        Div(
                            Div(
                                Div('A', cls='text-primary-content text-sm font-bold'),  # Primary color preview with text-primary-content class for text color
                                cls='bg-primary flex aspect-square w-5 items-center justify-center rounded lg:w-6'  # Background primary color with flexbox, square aspect ratio, width, and rounded corners
                            ),
                            Div(
                                Div('A', cls='text-secondary-content text-sm font-bold'),  # Secondary color preview with text-secondary-content class for text color
                                cls='bg-secondary flex aspect-square w-5 items-center justify-center rounded lg:w-6'  # Background secondary color with flexbox, square aspect ratio, width, and rounded corners
                            ),
                            Div(
                                Div('A', cls='text-accent-content text-sm font-bold'),  # Accent color preview with text-accent-content class for text color
                                cls='bg-accent flex aspect-square w-5 items-center justify-center rounded lg:w-6'  # Background accent color with flexbox, square aspect ratio, width, and rounded corners
                            ),
                            Div(
                                Div('A', cls='text-neutral-content text-sm font-bold'),  # Neutral color preview with text-neutral-content class for text color
                                cls='bg-neutral flex aspect-square w-5 items-center justify-center rounded lg:w-6'  # Background neutral color with flexbox, square aspect ratio, width, and rounded corners
                            ),
                            cls='flex flex-wrap gap-1'  # Container for color previews with flexbox and gap between items
                        ),
                        cls='bg-base-100 col-span-4 col-start-2 row-span-3 row-start-1 flex flex-col gap-1 p-2'  # Main container for theme preview with base-100 background, grid positioning, flexbox, gap, and padding
                    ),
                    cls='grid grid-cols-5 grid-rows-3'  # Grid layout for theme preview with 5 columns and 3 rows
                ),
                data_theme=theme,  # Set the theme for the div
                cls='bg-base-100 text-base-content w-full cursor-pointer font-sans'  # Styling for the theme div with base-100 background, base-content text color, full width, pointer cursor, and sans-serif font
            ),
            data_act_class='!outline-base-content',  # Active class for the theme div with base-content outline
            data_set_theme=theme,  # Set the theme on click
            cls='border-base-content/20 hover:border-base-content/40 overflow-hidden rounded-lg border outline outline-2 outline-offset-2 outline-transparent'  # Styling for the outer div with border, hover effect, overflow hidden, rounded corners, and outline
        )
    
    return Div(
        *[create_div(theme) for theme in themes],  # Create a div for each theme
        cls='rounded-box grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5'  # Grid layout for all theme divs with responsive columns and gap between items
    )

serve()  # Start the FastHTML app
