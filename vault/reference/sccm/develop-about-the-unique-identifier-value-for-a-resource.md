---
title: "Unique Identifier Value for a Resource"
type: reference
domain: sccm
slug: develop-about-the-unique-identifier-value-for-a-resource
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/servers/configure/about-the-unique-identifier-value-for-a-resource
family: develop
documentKind: "concept-article"
abstract: "An optional property that reports inventory data for a resource."
---

# Unique Identifier Value for a Resource

# About the Unique Identifier Value for a Resource
In Configuration Manager, the Configuration Manager unique identifier property for a new resource class is optional. If you report inventory data for the resource, you must include this property. The Configuration Manager unique identifier value must be unique — it relates your resource discovery data to your inventory data (SMS_G_xxx). Typically, hardware resources use a GUID to uniquely identify individual resources.

 The format of the Configuration Manager unique identifier value is as follows.

```
<ID Type>:<ID Value>
```

 For example, Configuration Manager uses a GUID to identify Configuration Manager clients.

```
GUID:4976DCD4-CAAE-11D2-8E00-00104BCC3648
```

 You can use any \<ID Type> and \<ID Value> values to identify a new resource. However, when discovering data for an existing resource type, you should follow the convention that is used by that resource type.

## See Also
 [How to Get the Unique Identifier Value for a Client](../../../../develop/core/servers/configure/how-to-get-the-unique-identifier-value-for-a-client.md)
