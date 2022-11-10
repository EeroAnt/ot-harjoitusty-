```mermaid
sequenceDiagram
  participant Main
  participant Machine
  participant FuelTank
  participant Engine
  Main->>Machine: call kone = Machine()
  Machine->>FuelTank: kone._tank = FuelTank()
  Machine->>FuelTank: kone._tank.fill(40)
  activate FuelTank
  FuelTank->>Machine: kone._tank.fuel_contents += 40  
  deactivate FuelTank
  Machine->>Engine: kone._engine = Engine(kone._tank)
  activate Engine
  Engine->>Machine: kone._engine._fuel_tank = kone._tank
  deactivate Engine
  Main->>Machine: call kone.drive
```
