---
title: "SMS_SUMDeploymentStatistics Class"
type: reference
domain: sccm
slug: develop-sms-sumdeploymentstatistics-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/sum/sms_sumdeploymentstatistics-server-wmi-class
family: develop
documentKind: "reference"
abstract: "An SMS Provider server class that represents a per-deployment summary for SUM deployments in-console monitoring."
---

# SMS_SUMDeploymentStatistics Class

# SMS_SUMDeploymentStatistics Server WMI Class
The `SMS_SUMDeploymentStatistics` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents a per-deployment summary for SUM deployments in-console monitoring.  

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.  

## Syntax  

```  
Class SMS_SUMDeploymentStatistics : SMS_BaseClass  
{  
    UInt32 AssignmentID;  
    String AssignmentUniqueID;  
    UInt32 NumError;  
    UInt32 NumInProgress;  
    UInt32 NumReqsNotMet;  
    UInt32 NumSuccess;  
    UInt32 NumUnknown;  
    DateTime SummarizationTime;  
};  
```  

## Methods  
 The `SMS_SUMDeploymentStatistics` class does not define any methods.  

## Properties  
 `AssignmentID`  
 Data type: `UInt32`  

 Access type: Read-only  

 Qualifiers: [key, not_null, read]  

 The ID of the configuration item assignment. This ID is unique only for the site.  

 `AssignmentUniqueID`  
 Data type: `String`  

 Access type: Read-only  

 Qualifiers: [not_null, read]  

 The unique ID of the configuration item assignment. This ID is unique across sites.  

 `NumError`  
 Data type: `UInt32`  

 Access type: Read-only  

 Qualifiers: [read]  

 Count of the number of errors.  

 `NumInProgress`  
 Data type: `UInt32`  

 Access type: Read-only  

 Qualifiers: [read]  

 Count of the number in progress.  

 `NumReqsNotMet`  
 Data type: `UInt32`  

 Access type: Read-only  

 Qualifiers: [read]  

 Count of the number where requirements are not met.  

 `NumSuccess`  
 Data type: `UInt32`  

 Access type: Read-only  

 Qualifiers: [read]  

 Count of the number of successes.  

 `NumUnknown`  
 Data type: `UInt32`  

 Access type: Read-only  

 Qualifiers: [read]  

 Count of the number unknown.  

 `SummarizationTime`  
 Data type: `DateTime`  

 Access type: Read-only  

 Qualifiers: [read]  

 Summarization time.   

## Remarks  

## Requirements  

### Runtime Requirements  
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).  

### Development Requirements  
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).  

## See Also  
 [About software update deployments](../../sum/about-software-updates-deployments.md)
