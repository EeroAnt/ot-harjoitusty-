```mermaid
sequenceDiagram
  actor User
  participant Machine
  participant FuelTank
  participant Engine
  User->>Machine call kone = Machine()
  UI->>TodoService: create_todo("vie roskat")
  TodoService->>todo: Todo("vie roskat", kalle)
  TodoService->>TodoRepository: create(todo)
  TodoRepository-->>TodoService: todo
  TodoService-->>UI: todo 
  UI->>UI: initialize_todo_list()
```
