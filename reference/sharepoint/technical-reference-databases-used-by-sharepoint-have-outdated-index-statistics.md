---
title: "Databases used by SharePoint have outdated index statistics (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-databases-used-by-sharepoint-have-outdated-index-statistics
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/databases-used-by-sharepoint-have-outdated-index-statistics
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Databases used by SharePoint have outdated index statistics, for SharePoint Server."
---

# Databases used by SharePoint have outdated index statistics (SharePoint Server) - SharePoint Server

Note

Databases used by SharePoint have outdated index statistics (SharePoint Server)

# Databases used by SharePoint have outdated index statistics (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Databases used by SharePoint have outdated index statistics.

**Summary:** Outdated index statistics can decrease query performance and cause SharePoint Server 2016 and SharePoint 2013 to respond slowly.

**Cause:** Index statistics in SharePoint Server databases are out of date.

Note

This SharePoint Health Analyzer rule is enabled daily by default.

**Resolution: Edit the rule definition so that the configuration is automatically repaired.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the Central Administration Home page, click **Monitoring**.

On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.

On the Health Analyzer Rule Definitions - All Rules page, in the **Category: Performance** section, click the name of the rule.

In the **Health Analyzer Rule Definitions** dialog, click **Edit Item**.

Select the **Repair Automatically** check box, and then click **Save**.

See also

## See also

Other Resources

#### Other Resources

Index Statistics

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
