---
title: "SMS_ClientDeploymentCollectionBucket Class"
type: reference
domain: sccm
slug: develop-sms-clientdeploymentcollectionbucket-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/deploy/sms_clientdeploymentcollectionbucket-server-wmi-class
family: develop
documentKind: "reference"
abstract: "The SMS_ClientDeploymentCollectionBucket Windows Management Instrumentation class is an SMS Provider server class, in Configuration Manager, that represents a client deployment collection bucket."
---

# SMS_ClientDeploymentCollectionBucket Class

# SMS_ClientDeploymentCollectionBucket Server WMI Class
The  `SMS_ClientDeploymentCollectionBucket` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents a client deployment collection bucket that is used to display the localized name in the client deployment detail view.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_ClientDeploymentCollectionBucket: SMS_BaseClass
{
    UInt32 BaselineType;
    String Bucket;
    String CollectionID;
    String CollectionName;
    UInt32 FeatureType;
};

```

## Methods
 The  `SMS_ClientDeploymentCollectionBucket`  class does not define any methods.

## Properties
 `BaselineType`
 Data type: `UInt32`

 Access type: Read

 Qualifiers: [key]

 The baseline type. Possible values are:

|Value|Baseline type|
|-|-|
|1|Product Baseline|
|2|Staging Baseline|

 `Bucket`
 Data type: `String`

 Access type: Read

 Qualifiers: [key]

 The client deployment status bucket. Possible values are:

|Value|
|-|
|CDUnknown|
|CDFullCompliant|
|CDInProgress|
|CDNotCompliant|
|CDCriticalError|

 `CollectionID`
 Data type: `String`

 Access type: Read

 Qualifiers: [key]

 The ID of the collection.

 `CollectionName`
 Data type: `String`

 Access type: Read

 Qualifiers: none

 The name of the collection.

 `FeatureType`
 Data type: `UInt32`

 Access type: Read

 Qualifiers: [key]

 The feature type. Possible values are:

|Value|Feature type|
|-|-|
|3|Client Deployment|

## Remarks
 Class qualifiers for this class include:

- Dynamic

- Read (read-only)

  For more information about both the class qualifiers and the property qualifiers included in the Properties section, see [Configuration Manager Class and Property Qualifiers](../../../../../develop/reference/misc/class-and-property-qualifiers.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).
