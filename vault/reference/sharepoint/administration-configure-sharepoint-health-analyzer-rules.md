---
title: "Configure SharePoint Health Analyzer rules in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-sharepoint-health-analyzer-rules
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-sharepoint-health-analyzer-rules
family: administration
documentKind: "how-to"
abstract: "Learn to configure SharePoint Server Health Analyzer rules by using Central Administration."
---

# Configure SharePoint Health Analyzer rules in SharePoint Server - SharePoint Server

Note

Configure SharePoint Health Analyzer rules in SharePoint Server

# Configure SharePoint Health Analyzer rules in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Before you begin

## Before you begin

Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources:

Plan browser support

Accessibility in SharePoint

Keyboard shortcuts

Touch

Configuring SharePoint Health Analyzer rules

## Configuring SharePoint Health Analyzer rules

You can accept the default settings for each health rule, or you can change settings for a health rule by using Central Administration.

**To configure health rules by using Central Administration**

Verify that the user account performing this procedure is a member of the Farm Administrators group.

In Central Administration, on the home page, click **Monitoring**.

On the **Monitoring** page, under **Health Analyzer**, click **Review rule definitions**.

On the **Health Analyzer Rule Definitions** page, click the rule that you want to configure.

In the **Health Analyzer Rule Definitions** dialog, click **Edit Item**.

Edit one or more rule fields, and then click **Save**.

To leave the rule unchanged, either dismiss the dialog or click **Cancel**.

Each health rule has configurable fields, which are described in the following table.

**Configurable fields for SharePoint Health Analyzer rules**

| **Configurable field** | **Description** |
| --- | --- |
| Title | The name of the health rule. You can rename a health rule to clarify its functionality. The title is the name of the rule as it appears in the **Health Rule Definitions** list in Central Administration.  
 Changing the title does not affect how the rule runs. |
| Scope | You can set a health rule to run against all servers or any server. If set to any server, the rule will run on the first available server that the system encounters. |
| Schedule | You can schedule a health rule to run hourly, daily, weekly, monthly, or on demand only. |
| Enabled | You can select or clear this check box to enable or disable a health rule. |
| Repair Automatically | You can specify whether a health rule automatically attempts to repair errors that it finds. If this option is selected, SharePoint Server will repair errors as soon as they are found, as defined by the rule.  
 > [!NOTE]> If no repair is specified by the rule, the system does not attempt to repair the problem. |
| Version | Version history enables you to track the changes performed on each rule. The version number is updated every time that the rule is saved. The version number does not affect how the rule works. |

Each health rule has read-only fields, which are described in the following table.

**Read-only fields for SharePoint Health Analyzer rules**

| **Read-only field** | **Description** |
| --- | --- |
| Version | The current version number of the rule. |
| Created at | The date and time that the rule was originally created and the user account that created the rule. |
| Last modified at | The date and time that the rule was last changed and the user account that created the rule. |

For more information about SharePoint Server monitoring configuration, see Configure monitoring in SharePoint Server 2016.

See also

## See also

Concepts

#### Concepts

SharePoint Health Analyzer rules reference for SharePoint Server 2016

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
