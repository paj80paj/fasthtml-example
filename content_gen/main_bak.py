from fasthtml.common import *
from claudette import *
import os
from starlette.staticfiles import StaticFiles

# Set up the app
hdrs = (
    Script(src="https://cdn.tailwindcss.com?plugins=forms,container-queries"),
    Link(rel='preconnect', href='https://fonts.gstatic.com/', crossorigin=''),
    Link(rel='stylesheet', as_='style', onload="this.rel='stylesheet'", href='https://fonts.googleapis.com/css2?display=swap&family=Noto+Sans%3Awght%40400%3B500%3B700%3B900&family=Work+Sans%3Awght%40400%3B500%3B700%3B900'),
    Link(rel='icon', type='image/x-icon', href='data:image/x-icon;base64,')
)
app = FastHTML(hdrs=hdrs, ws_hdr=True)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up a chat model (keeping this for potential future use)
cli = Client(models[-1])
sp = "You are a helpful and concise financial advisor assistant."
messages = []

def header():
    return Header(
        Div(
            Div(
                Svg(
                    Path(d='M39.5563 34.1455V13.8546C39.5563 15.708 36.8773 17.3437 32.7927 18.3189C30.2914 18.916 27.263 19.2655 24 19.2655C20.737 19.2655 17.7086 18.916 15.2073 18.3189C11.1227 17.3437 8.44365 15.708 8.44365 13.8546V34.1455C8.44365 35.9988 11.1227 37.6346 15.2073 38.6098C17.7086 39.2069 20.737 39.5564 24 39.5564C27.263 39.5564 30.2914 39.2069 32.7927 38.6098C36.8773 37.6346 39.5563 35.9988 39.5563 34.1455Z', fill='currentColor'),
                    Path(fill_rule='evenodd', clip_rule='evenodd', d='M10.4485 13.8519C10.4749 13.9271 10.6203 14.246 11.379 14.7361C12.298 15.3298 13.7492 15.9145 15.6717 16.3735C18.0007 16.9296 20.8712 17.2655 24 17.2655C27.1288 17.2655 29.9993 16.9296 32.3283 16.3735C34.2508 15.9145 35.702 15.3298 36.621 14.7361C37.3796 14.246 37.5251 13.9271 37.5515 13.8519C37.5287 13.7876 37.4333 13.5973 37.0635 13.2931C36.5266 12.8516 35.6288 12.3647 34.343 11.9175C31.79 11.0295 28.1333 10.4437 24 10.4437C19.8667 10.4437 16.2099 11.0295 13.657 11.9175C12.3712 12.3647 11.4734 12.8516 10.9365 13.2931C10.5667 13.5973 10.4713 13.7876 10.4485 13.8519ZM37.5563 18.7877C36.3176 19.3925 34.8502 19.8839 33.2571 20.2642C30.5836 20.9025 27.3973 21.2655 24 21.2655C20.6027 21.2655 17.4164 20.9025 14.7429 20.2642C13.1498 19.8839 11.6824 19.3925 10.4436 18.7877V34.1275C10.4515 34.1545 10.5427 34.4867 11.379 35.027C12.298 35.6207 13.7492 36.2054 15.6717 36.6644C18.0007 37.2205 20.8712 37.5564 24 37.5564C27.1288 37.5564 29.9993 37.2205 32.3283 36.6644C34.2508 36.2054 35.702 35.6207 36.621 35.027C37.4573 34.4867 37.5485 34.1546 37.5563 34.1275V18.7877ZM41.5563 13.8546V34.1455C41.5563 36.1078 40.158 37.5042 38.7915 38.3869C37.3498 39.3182 35.4192 40.0389 33.2571 40.5551C30.5836 41.1934 27.3973 41.5564 24 41.5564C20.6027 41.5564 17.4164 41.1934 14.7429 40.5551C12.5808 40.0389 10.6502 39.3182 9.20848 38.3869C7.84205 37.5042 6.44365 36.1078 6.44365 34.1455L6.44365 13.8546C6.44365 12.2684 7.37223 11.0454 8.39581 10.2036C9.43325 9.3505 10.8137 8.67141 12.343 8.13948C15.4203 7.06909 19.5418 6.44366 24 6.44366C28.4582 6.44366 32.5797 7.06909 35.657 8.13948C37.1863 8.67141 38.5667 9.3505 39.6042 10.2036C40.6278 11.0454 41.5563 12.2684 41.5563 13.8546Z', fill='currentColor'),
                    viewbox='0 0 48 48',
                    fill='none',
                    xmlns='http://www.w3.org/2000/svg'
                ),
                cls='size-4'
            ),
            H2('Gadget Labs', cls='text-[#0e161b] text-lg font-bold leading-tight tracking-[-0.015em]'),
            cls='flex items-center gap-4 text-[#0e161b]'
        ),
        Div(
            Div(
                A('Home', href='#', cls='text-[#0e161b] text-sm font-medium leading-normal'),
                A('Docs', href='#', cls='text-[#0e161b] text-sm font-medium leading-normal'),
                A('API Reference', href='#', cls='text-[#0e161b] text-sm font-medium leading-normal'),
                A('Examples', href='#', cls='text-[#0e161b] text-sm font-medium leading-normal'),
                cls='flex items-center gap-9'
            ),
            Button(
                Span('Contact Sales', cls='truncate'),
                cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-10 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-bold leading-normal tracking-[0.015em]'
            ),
            Div(style='background-image: url("https://cdn.usegalileo.ai/sdxl10/a6afe60b-67df-4176-b76e-9a9bbb4e0a00.png");', cls='bg-center bg-no-repeat aspect-square bg-cover rounded-full size-10'),
            cls='flex flex-1 justify-end gap-8'
        ),
        cls='flex items-center justify-between whitespace-nowrap border-b border-solid border-b-[#e8eef3] px-10 py-3'
    )

def working_titles_table():
    return Table(
        Thead(
            Tr(
                Th('Working Title', cls='px-4 py-3 text-left text-[#0e161b] w-[300px] text-sm font-medium leading-normal'),
                Th('Subtitle', cls='px-4 py-3 text-left text-[#0e161b] w-[200px] text-sm font-medium leading-normal'),
                Th('Theme', cls='px-4 py-3 text-left text-[#0e161b] w-60 text-sm font-medium leading-normal'),
                Th('Status', cls='px-4 py-3 text-left text-[#0e161b] w-60 text-sm font-medium leading-normal'),
                Th('Actions', cls='px-4 py-3 text-left text-[#0e161b] w-60 text-[#507a95] text-sm font-medium leading-normal'),
                cls='bg-[#f8fafb]'
            )
        ),
        Tbody(
            Tr(
                Td('AI-Powered Marketing Strategy', cls='h-[72px] px-4 py-2 w-[300px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td('Revolutionizing Digital Campaigns', cls='h-[72px] px-4 py-2 w-[200px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td(
                    Button(
                        Span('AI Marketing', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td(
                    Button(
                        Span('New', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td('Edit/Select', cls='h-[72px] px-4 py-2 w-60 text-[#507a95] text-sm font-bold leading-normal tracking-[0.015em]'),
                cls='border-t border-t-[#d1dde6]'
            ),
            Tr(
                Td('Cyber Risk Management in AI', cls='h-[72px] px-4 py-2 w-[300px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td('Securing AI Systems from Threats', cls='h-[72px] px-4 py-2 w-[200px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td(
                    Button(
                        Span('Cybersecurity, AI', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td(
                    Button(
                        Span('Outlined', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td('Edit/Select', cls='h-[72px] px-4 py-2 w-60 text-[#507a95] text-sm font-bold leading-normal tracking-[0.015em]'),
                cls='border-t border-t-[#d1dde6]'
            ),
            Tr(
                Td('Regulatory Compliance in AI', cls='h-[72px] px-4 py-2 w-[300px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td('Navigating AI Regulations', cls='h-[72px] px-4 py-2 w-[200px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td(
                    Button(
                        Span('AI, Regulations', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td(
                    Button(
                        Span('Drafted', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td('Edit/Select', cls='h-[72px] px-4 py-2 w-60 text-[#507a95] text-sm font-bold leading-normal tracking-[0.015em]'),
                cls='border-t border-t-[#d1dde6]'
            ),
            Tr(
                Td('Ethical AI: Principles and Practices', cls='h-[72px] px-4 py-2 w-[300px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td('Building Trustworthy AI Systems', cls='h-[72px] px-4 py-2 w-[200px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td(
                    Button(
                        Span('AI Ethics', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td(
                    Button(
                        Span('Final', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td('Edit/Select', cls='h-[72px] px-4 py-2 w-60 text-[#507a95] text-sm font-bold leading-normal tracking-[0.015em]'),
                cls='border-t border-t-[#d1dde6]'
            ),
            Tr(
                Td('AI for Financial Services', cls='h-[72px] px-4 py-2 w-[300px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td('Transforming Finance with AI', cls='h-[72px] px-4 py-2 w-[200px] text-[#0e161b] text-sm font-normal leading-normal'),
                Td(
                    Button(
                        Span('AI, Finance', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td(
                    Button(
                        Span('Published', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-8 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-medium leading-normal w-full'
                    ),
                    cls='h-[72px] px-4 py-2 w-60 text-sm font-normal leading-normal'
                ),
                Td('Edit/Select', cls='h-[72px] px-4 py-2 w-60 text-[#507a95] text-sm font-bold leading-normal tracking-[0.015em]'),
                cls='border-t border-t-[#d1dde6]'
            )
        ),
        cls='flex-1'
    )

def main_content():
    return Div(
        Div(
            Div(
                A('AI Marketing', href='#', cls='text-[#507a95] text-base font-medium leading-normal'),
                Span('/', cls='text-[#507a95] text-base font-medium leading-normal'),
                Span('Create Content', cls='text-[#0e161b] text-base font-medium leading-normal'),
                cls='flex flex-wrap gap-2 p-4'
            ),
            Div(
                Div(
                    P('Working Titles', cls='text-[#0e161b] tracking-light text-[32px] font-bold leading-tight'),
                    P('Step 1 of 5: Select or Edit a Working Title', cls='text-[#507a95] text-sm font-normal leading-normal'),
                    cls='flex min-w-72 flex-col gap-3'
                ),
                cls='flex flex-wrap justify-between gap-3 p-4'
            ),
            Div(
                Label(
                    Input(placeholder='Search for a working title', value='', cls='form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-[#0e161b] focus:outline-0 focus:ring-0 border-none bg-[#e8eef3] focus:border-none h-14 placeholder:text-[#507a95] p-4 text-base font-normal leading-normal'),
                    cls='flex flex-col min-w-40 flex-1'
                ),
                cls='flex max-w-[480px] flex-wrap items-end gap-4 px-4 py-3'
            ),
            Div(
                Div(
                    working_titles_table(),
                    cls='flex overflow-hidden rounded-xl border border-[#d1dde6] bg-[#f8fafb]'
                ),
                cls='px-4 py-3 @container'
            ),
            Div(
                Div(
                    Button(
                        Span('Generate Titles', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-10 px-4 bg-[#1f93e0] text-[#f8fafb] text-sm font-bold leading-normal tracking-[0.015em] grow'
                    ),
                    Button(
                        Span('View prompts', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-10 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-bold leading-normal tracking-[0.015em] grow'
                    ),
                    Button(
                        Span('Enter Title', cls='truncate'),
                        cls='flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-10 px-4 bg-[#e8eef3] text-[#0e161b] text-sm font-bold leading-normal tracking-[0.015em] grow'
                    ),
                    cls='flex flex-1 gap-3 flex-wrap px-4 py-3 max-w-[480px] justify-center'
                ),
                cls='flex justify-center'
            ),
            Div(
                Div(
                    P('Step 1 of 5', cls='text-[#0e161b] text-base font-medium leading-normal'),
                    cls='flex gap-6 justify-between'
                ),
                Div(
                    Div(style='width: 20%;', cls='h-2 rounded bg-[#1f93e0]'),
                    cls='rounded bg-[#d1dde6]'
                ),
                P('Select or Edit a Working Title', cls='text-[#507a95] text-sm font-normal leading-normal'),
                cls='flex flex-col gap-3 p-4'
            ),
            cls='layout-content-container flex flex-col max-w-[960px] flex-1'
        ),
        cls='px-40 flex flex-1 justify-center py-5'
    )

@app.get
def index():
    page = Div(
        header(),
        main_content(),
        style='font-family: "Work Sans", "Noto Sans", sans-serif;',
        cls='relative flex size-full min-h-screen flex-col bg-[#f8fafb] group/design-root overflow-x-hidden'
    )
    return Titled('Content Generation App', page)

# Add new routes for other pages
@app.get("/outline")
def outline():
    # Implement the outline page
    pass

@app.get("/full-text")
def full_text():
    # Implement the full text page
    pass

@app.get("/prompts")
def prompts():
    # Implement the prompts page
    pass

# Add API routes for CRUD operations
@app.post("/api/working-titles")
def create_working_title(title: str, subtitle: str, theme: str):
    # Implement creating a new working title
    pass

@app.put("/api/working-titles/{title_id}")
def update_working_title(title_id: int, title: str, subtitle: str, theme: str, status: str):
    # Implement updating an existing working title
    pass

@app.delete("/api/working-titles/{title_id}")
def delete_working_title(title_id: int):
    # Implement deleting a working title
    pass

@app.post("/api/generate-titles")
def generate_titles():
    # Implement AI-powered title generation
    pass

# Keep the existing routes for now, but they can be updated or removed as needed
@app.get("/clientcomm")
def clientcomm():
    # This route can be updated or removed based on the new design requirements
    pass

@app.ws('/wscon')
async def ws(msg: str, send):
    # This websocket route can be updated or removed based on the new design requirements
    pass

@app.post("/chat")
def chat(message: str):
    # This chat route can be updated or removed based on the new design requirements
    pass

serve()

