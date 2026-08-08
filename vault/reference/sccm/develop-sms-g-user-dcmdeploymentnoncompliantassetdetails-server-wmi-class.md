---
title: "SMS_G_USER_DCMDeploymentNonCompliantAssetDetails Class"
type: reference
domain: sccm
slug: develop-sms-g-user-dcmdeploymentnoncompliantassetdetails-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/apps/sms_g_user_dcmdeploymentnoncompliantassetdetails-server-wmi-class
family: develop
documentKind: "reference"
abstract: "The SMS_G_USER_DCMDeploymentNonCompliantAssetDetails WMI class represents non-compliant asset details for a deployment."
---

# SMS_G_USER_DCMDeploymentNonCompliantAssetDetails Class

# SMS_G_USER_DCMDeploymentNonCompliantAssetDetails Server WMI Class
The `SMS_G_USER_DCMDeploymentNonCompliantAssetDetails` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents non-compliant asset details for a deployment.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_G_USER_DCMDeploymentNonCompliantAssetDetails : SMS_G_User
{
    UInt32 AssignmentID;
    UInt32 BL_ID;
    UInt32 CI_ID;
    UInt32 ResourceID;
    UInt32 Rule_ID;
    UInt32 RuleSubState;
};
```

## Methods
 The `SMS_G_USER_DCMDeploymentNonCompliantAssetDetails` class doesn't define any methods.

## Properties
 `AssignmentID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 See [SMS_DCMDeploymentErrorAssetDetails Server WMI Class](../../../develop/reference/compliance/sms_dcmdeploymenterrorassetdetails-server-wmi-class.md).

 `BL_ID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 See [SMS_DCMDeploymentErrorAssetDetails Server WMI Class](../../../develop/reference/compliance/sms_dcmdeploymenterrorassetdetails-server-wmi-class.md).

 `CI_ID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 See [SMS_DCMDeploymentErrorAssetDetails Server WMI Class](../../../develop/reference/compliance/sms_dcmdeploymenterrorassetdetails-server-wmi-class.md).

 `ResourceID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [not_null, read]

 Unique ID, supplied by Configuration Manager, that identifies a client resource. This ID isn't unique across sites.

 `Rule_ID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 Rule ID.

 `RuleSubState`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 Rule sub-status type.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
