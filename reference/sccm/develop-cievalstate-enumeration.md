---
title: "CIEvalState Enumeration"
type: reference
domain: sccm
slug: develop-cievalstate-enumeration
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/cievalstate-enumeration
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the CIEvalState enumeration is used by the ICIINFO Interface."
---

# CIEvalState Enumeration

# CIEvalState Enumeration
In Configuration Manager, the `CIEvalState` enumeration defines configuration item evaluation states. This enumeration is used by the [ICIINFO Interface](../../../../../develop/reference/core/clients/client-classes/iciinfo-interface.md).

## Syntax

```
typedef enum tagCIEvalState
{
  ciIdle = 0,
  ciEvaluating
} CIEvalState;
```

## Elements
 ciIdle
 Configuration item is idle.

 ciEvaluating
 Configuration item is being evaluated.

## See Also
 [ICIINFO Interface](../../../../../develop/reference/core/clients/client-classes/iciinfo-interface.md)
