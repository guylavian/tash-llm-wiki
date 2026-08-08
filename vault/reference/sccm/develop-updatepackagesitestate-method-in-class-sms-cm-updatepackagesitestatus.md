---
title: "UpdatePackageSiteState Method"
type: reference
domain: sccm
slug: develop-updatepackagesitestate-method-in-class-sms-cm-updatepackagesitestatus
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/sum/updatepackagesitestate-method-in-class-sms_cm_updatepackagesitestatus
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the UpdatePackageSiteState Windows Management Instrumentation class method updates the package installation state of the site."
---

# UpdatePackageSiteState Method

# UpdatePackageSiteState Method in Class SMS_CM_UpdatePackageSiteStatus
The `UpdatePackageSiteState` Windows Management Instrumentation (WMI) class method, in Configuration Manager, updates the package installation state of the site.  

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.  

## Syntax  

```  
SInt32 UpdatePackageSiteState(  
     UInt32 State  
);  

```  

#### Parameters  
 `State`  
 Data type: `UInt32`  

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
 [SMS_CM_UpdatePackageSiteStatus Server WMI Class](../../../develop/reference/sum/sms_cm_updatepackagesitestatus-server-wmi-class.md)
