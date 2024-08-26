# FastHTML Variations Summary

This document details different FastHTML usages across the repository projects.

## 1. Chatbot with DaisyUI
- **Features**: Multiple chat implementations (basic, polling, websockets).
- **Styling**: Uses Tailwind CSS and DaisyUI for chat bubble styling.
- **Code Sample**:
  ```python
  def ChatMessage(msg):
      bubble_class = "chat-bubble-primary" if msg['role']=='user' else 'chat-bubble-secondary'
      chat_class = "chat-end" if msg['role']=='user' else 'chat-start'
      return Div(Div(msg['role'], cls="chat-header"),
                 Div(msg['content'], cls=f"chat-bubble {bubble_class}"),
                 cls=f"chat {chat_class}")
  ```

## 2. Game of Life
- **Features**: Real-time updates, multi-client sync using WebSockets.
- **FastHTML Components**: Interface for grid interactions using HTMX.
- **Implementation**:
  ```python
  def Grid():
      cells = []
      for y, row in enumerate(game_state['grid']):
          for x, cell in enumerate(row):
              cell_class = 'alive' if cell else 'dead'
              cell = Div(cls=f'cell {cell_class}', hx_put='/update', hx_vals={'x': x, 'y': y}, hx_swap='none', hx_target='#gol', hx_trigger='click')
              cells.append(cell)
      return Div(*cells, id='grid')
  ```

## 3. Todo App
- **Features**: Real-time item updates, SQLite database integration.
- **FastHTML with HTMX**: For dynamic list handling and database operations.
- **Form Handling**:
  ```python
  @rt("/")
  async def get():
      add = Form(Group(mk_input(), Button("Add")),
                 hx_post="/", target_id='todo-list', hx_swap="beforeend")
      card = Card(Ul(*todos(), id='todo-list'),
                  header=add, footer=Div(id=id_curr)),
      return Title('Todo list'), Main(H1('Todo list'), card, cls='container')
  ```

## 4. Chess App
- **Features**: Multiplayer game with websockets for real-time sync.
- **Setup**:
  ```bash
  pip install -r requirements.txt
  python chess_app.py
  ```

## 5. Doodle Demo
- **Features**: Non-functional form rendered using Doodle CSS.
- **Note**: Not functional, aesthetic demonstration only.

## 6. HTMX Form Demo
- **Features**: Uses HTMX for dynamic form submissions.
- **Example**:
  ```python
  @rt('/')
  def get():
      return Titled('HTMX Form Demo', Grid(
          Form(hx_post="/submit", hx_target="#result", hx_trigger="input delay:200ms")(
              Select(Option("One"), Option("Two"), id="select"),
              Input(value='j', type="text", id="name", placeholder="Name"),
              Input(value='h', type="text", id="email", placeholder="Email")),
          Div(id="result")
      ))
  ```

This summary outlines the diverse uses of FastHTML, displaying its versatility in various app contexts.
