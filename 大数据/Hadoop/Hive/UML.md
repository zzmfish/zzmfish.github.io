```uml
@startuml
class Operator {
    # initializeOp(hconf)
    # processOp(row, tag)
    # forward(row, rowInspector)
    
}

class ScriptOperator {
  - outThread
  - errThread
  - scriptPid
}

class GroupByOperator {
    - currentKeys
    - newKeys
    - forwardCache
    - processAggr(row, rowInspector, newKeys)
    - processHashAggr(row, rowInspector, newKeys)
}

Operator <|-- ScriptOperator
Operator <|-- GroupByOperator
Operator o-- "N" Operator: childOperatorsArray
@enduml
```