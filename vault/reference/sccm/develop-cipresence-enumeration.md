---
title: "CIPresence Enumeration"
type: reference
domain: sccm
slug: develop-cipresence-enumeration
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/cipresence-enumeration
family: develop
documentKind: "reference"
abstract: "Learn how to define configuration item presence types used in the discovery process with CIPresence enumeration."
---

# CIPresence Enumeration

# CIPresence Enumeration
In Configuration Manager, the `CIPresence` enumeration defines configuration item presence types used in the discovery process.

## Syntax

```
typedef enum tagCIPresence
{
  ciNotPresent = 0,ciNonCompliant = 0,
  ciPresent = 1,ciCompliant = 1,
  ciNotApplicable = 2,
  ciPresenceUnknown = 3,ciComplianceUnknown = 3,
  ciEvaluationError = 4,
  ciNotEvaluated = 5
} CIPresence;
```

## Elements
 `ciNotPresent, ciNonCompliant`
 Configuration item not present or not compliant.

 `ciPresent, ciCompliant`
 Configuration item present or compliant.

 `ciNotApplicable`
 Configuration item not applicable.

 `ciPresenceUnknown, ciComplianceUnknown`
 Configuration item presence or compliance unknown.

 `ciEvaluationError`
 Configuration item evaluation error.

 `ciNotEvaluated`
 Configuration item not evaluated.

## Remarks
 This enumeration is used by the [ICIINFO Interface](../../../../../develop/reference/core/clients/client-classes/iciinfo-interface.md).

## See Also
 [ICIINFO Interface](../../../../../develop/reference/core/clients/client-classes/iciinfo-interface.md)
