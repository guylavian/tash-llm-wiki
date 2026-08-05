---
title: "CCM_DTS_PRIORITY enumeration"
type: reference
domain: sccm
slug: develop-ccm-dts-priority-enumeration
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/ccm_dts_priority-enumeration
family: develop
documentKind: "reference"
abstract: "The CCM_DTS_PRIORITY enumeration indicates the priority of the download."
---

# CCM_DTS_PRIORITY enumeration

# CCM_DTS_PRIORITY enumeration

The **CCM_DTS_PRIORITY** enumeration indicates the priority of the download.

## Syntax

```
typedef enum
{
    CCM_DTS_PRIORITY_FOREGROUND,
    CCM_DTS_PRIORITY_HIGH,
    CCM_DTS_PRIORITY_NORMAL,
    CCM_DTS_PRIORITY_LOW,
}CCM_DTS_PRIORITY;

```

## Members

|Priority flag|Description|
|-|-|
|CCM_DTS_PRIORITY_FOREGROUND|The highest priority.|
|CCM_DTS_PRIORITY_HIGH|High priority.|
|CCM_DTS_PRIORITY_NORMAL|Normal priority.|
|CCM_DTS_PRIORITY_LOW|Low priority.|

## Remarks

The only strict requirement is that jobs at a lower priority do not block progress of jobs at a higher priority. Providers must respect this.

## Requirements

### Runtime requirements

For more information, see [Configuration Manager client runtime requirements](../../../../core/reqs/client-runtime-requirements.md).

### Development requirements

For more information, see [Configuration Manager client development requirements](../../../../core/reqs/client-development-requirements.md).
