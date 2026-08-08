---
title: "SMS_CertificateData Class"
type: reference
domain: sccm
slug: develop-sms-certificatedata-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/sms_certificatedata-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to represent certificate data managed by Configuration Manager using SMS_CertificateData class."
---

# SMS_CertificateData Class

# SMS_CertificateData Server WMI Class
The `SMS_CertificateData` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents certificate data managed by Configuration Manager.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_CertificateData : SMS_BaseClass
{
    String CertID;
    UInt32 CertType;
    String Description;
    String Name;
};
```

## Methods
 The following table lists the methods in the `SMS_CertificateData` class.

|Method|Description|
|------------|-----------------|
|[SubmitCertificate Method in Class SMS_CertificateData](../../../develop/reference/osd/submitcertificate-method-in-class-sms_certificatedata.md)|Submit certificate.|
|[DeleteCertificate Method in Class SMS_CertificateData](../../../develop/reference/osd/deletecertificate-method-in-class-sms_certificatedata.md)|Deletes the certificate from the database.|

## Properties
 `CertID`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [key, read]

 Certificate unique identifier.

 `CertType`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [enumeration, read]

 Certificate type. Possible values are:

| Value | Certificate type |
| ----- | ---------------- |
|1|Windows Intune Subscription|

 `Description`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Certificate description.

 `Name`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Certificate name.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).
