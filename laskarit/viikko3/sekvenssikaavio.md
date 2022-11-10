```mermaid
sequenceDiagram
  actor User
  participant UI
  participant TodoService
  participant TodoRepository
  participant todo
  User->>UI: click "Create"
  UI->>TodoService: create_todo("vie roskat")
  TodoService->>todo: Todo("vie roskat", kalle)
  TodoService->>TodoRepository: create(todo)
  TodoRepository-->>TodoService: todo
  TodoService-->>UI: todo 
  UI->>UI: initialize_todo_list()
```
