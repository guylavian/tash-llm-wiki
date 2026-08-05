---
title: "UpdateFeatureExposureStatus method in class SMS_CM_UpdatePackageFeatures"
type: reference
domain: sccm
slug: develop-updatefeatureexposurestatus-method-in-class-sms-cm-updatepackagefeatures
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/sum/updatefeatureexposurestatus-method-in-class-sms_cm_updatepackagefeatures
family: develop
documentKind: "reference"
abstract: "The UpdateFeatureExposureStatus Windows Management Instrumentation class method, in Configuration Manager, updates the feature exposure status for an update package feature extension."
---

# UpdateFeatureExposureStatus method in class SMS_CM_UpdatePackageFeatures

# UpdateFeatureExposureStatus Method in Class SMS_CM_UpdatePackageFeatures
The `UpdateFeatureExposureStatus` Windows Management Instrumentation (WMI) class method, in Configuration Manager, updates the feature exposure status for an update package feature extension.  

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.  

## Syntax  

```  
 SInt32 UpdateFeatureExposureStatus(  
     UInt32 Status  
);  

```  

#### Parameters  
 `Status`  
 Data type: `uint32`  

 Qualifiers: [in]  

 The installation state.  

## Return Values  
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.  

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).  

## Requirements  

### Runtime Requirements  
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).  

### Development Requirements  
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).  

## See Also  
 [SMS_CM_UpdatePackageFeatures Server WMI Class](../../../develop/reference/sum/sms_cm_updatepackagefeatures-server-wmi-class.md)
