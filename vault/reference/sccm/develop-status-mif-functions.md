---
title: "Status MIF Functions"
type: reference
domain: sccm
slug: develop-status-mif-functions
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/manage/status-mif-functions
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, status MIF functions are provided in separate libraries to create a status Management Information Format file."
---

# Status MIF Functions

# Status MIF Functions
In Configuration Manager, status MIF functions are provided in separate libraries to create a status Management Information Format (MIF) file. For more information about how the install status MIF file is used by Configuration Manager, see [SMS_Package Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_package-server-wmi-class.md).

 Success or failure of an advertisement is determined by using either an install status MIF file or the exit code of the advertised program. Relying on the exit code limits the visibility of events during the installation process and requires interpretation of the various exit codes. However, using the install status MIF file provides an enhanced status indicating whether the installation succeeded or failed, and it includes an appropriate description.

## Status MIF Functions

-   [Create Function](../../../../../develop/reference/core/servers/manage/create-function.md)

-   [InstallStatusMIF Function](../../../../../develop/reference/core/servers/manage/installstatusmif-function.md)

-   [InstallStatusMIFEx Function](../../../../../develop/reference/core/servers/manage/installstatusmifex-function.md)
