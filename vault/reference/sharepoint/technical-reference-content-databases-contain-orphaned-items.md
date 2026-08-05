---
title: "Content databases contain orphaned items (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-content-databases-contain-orphaned-items
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/content-databases-contain-orphaned-items
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Content databases contain orphaned items, for SharePoint Server."
---

# Content databases contain orphaned items (SharePoint Server) - SharePoint Server

Note

Content databases contain orphaned items (SharePoint Server)

# Content databases contain orphaned items (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Content databases contain orphaned items.

**Summary:** The SharePoint Health Analyzer has detected some sites in a content databases that are not referenced in the configuration database. These sites may not be accessible.

**Cause:** A restore operation that was not completed can result in sites in a content database that are not referenced in the SharePoint configuration database.

**Resolution: Decrease the number of days to store log files**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Monitoring**, in the **Health Analyzer** section, click **Review problems and solutions**.

On the Review problems and solutions page, click the alert for the failing rule, and then click **Fix Now**. Keep the dialog open so you can run the rule again to confirm the resolution.

Note

The Fix Now feature removes all orphans from the content database.

After following the steps in the **Remedy** section, in the **Review problems and solutions** dialog for the alert, click **Re-analyze Now** to confirm the resolution. If the problem is resolved, the rule is not flagged as a failing rule on the Review problems and solutions page.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
