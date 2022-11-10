```mermaid
sequenceDiagram
  participant Main
  participant Machine
  participant FuelTank
  participant Engine
  Main->>Machine: call kone = Machine()
  Machine->>FuelTank: kone._tank = FuelTank()
  activate FuelTank
  Machine->>FuelTank: kone._tank.fill(40)
  deactivate FuelTank
  FuelTank->>FuelTank: kone._tank.fuel_contents += 40  
  TodoService->>TodoRepository: create(todo)
  TodoRepository-->>TodoService: todo
  TodoService-->>UI: todo 
  UI->>UI: initialize_todo_list()
```
