---
title: "ActivateHierarchy method"
type: reference
domain: sccm
slug: develop-activatehierarchy-method-in-class-sms-migrationsitemapping
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/migration/activatehierarchy-method-in-class-sms_migrationsitemapping
family: develop
documentKind: "reference"
abstract: "The technical details of the ActivateHierarchy method in the SMS_MigrationSiteMapping WMI class."
---

# ActivateHierarchy method

# ActivateHierarchy Method in Class SMS_MigrationSiteMapping

The `ActivateHierarchy` WMI class method in Configuration Manager activates the hierarchy.  

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.  

## Syntax  

```  
SInt32 ActivateHierarchy (  
     String sourceSite,  
     String wmiAccount,  
     String sqlAccount,  
     String destinationSiteCode,  
     String scheduleToken  
);  
```  

#### Parameters  
 `sourceSite`  
 Data type: `String` Array  

 Qualifiers: [in]  

 The source site FQDN, netBIOS name or IP address.  

 `wmiAccount`  
 Data type: `String` Array  

 Qualifiers: `[in]`  

 The account name to access the WMI provider on the source site.  

 `sqlAccount`  
 Data type: `String` Array  

 Qualifiers: [in]  

 The account name to access SQL Server on the source site.  

 `destinationSiteCode`  
 Data type: `String` Array  

 Qualifiers: `[in]`  

 The destination site's site code. This should be the top site.  

 `scheduleToken`  
 Data type: `String` Array  

 Qualifiers: [in]  

 The schedule for the data gathering job.  

## Return Values  
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.  

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../develop/core/understand/about-configuration-manager-errors.md).  

## Requirements  

### Runtime Requirements  
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../develop/core/reqs/server-runtime-requirements.md).  

### Development Requirements  
 For more information, see [Configuration Manager Server Development Requirements](../../../../develop/core/reqs/server-development-requirements.md).  

## See also

[SMS_MigrationEntity Server WMI Class](../../../../develop/reference/core/migration/sms_migrationentity-server-wmi-class.md)
