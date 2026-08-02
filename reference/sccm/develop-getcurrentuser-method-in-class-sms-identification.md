---
title: "GetCurrentUser Method"
type: reference
domain: sccm
slug: develop-getcurrentuser-method-in-class-sms-identification
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/getcurrentuser-method-in-class-sms_identification
family: develop
documentKind: "reference"
abstract: "Learn how to use the GetCurrentUser method to get the domain\\user name that is used by the SMS Provider for authentication."
---

# GetCurrentUser Method

# GetCurrentUser Method in Class SMS_Identification
The `GetCurrentUser` Windows Management Instrumentation (WMI) class method, in Configuration Manager, gets the domain\user name that is used by the SMS Provider for authentication.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 GetCurrentUser(
     String UserName
);
```

#### Parameters
 `UserName`
 Data type: `String`

 Qualifiers: [out]

 Domain\user name being used by the SMS Provider. This name might differ from the domain\user name supplied by the application, depending on the domain trust model that is used.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Example Code
 The following example shows how to call this method to get the current user.

```
Dim Identification As SWbemObject
Dim UserName As String

Set Identification = GetObject("winmgmts:\root\sms\site_<sitecode>:SMS_Identification")
Identification.GetCurrentUser UserName

MsgBox "UserName = " & UserName
```

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Identification Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_identification-server-wmi-class.md)
