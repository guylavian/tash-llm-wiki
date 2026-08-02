---
title: "Some content databases are growing too large (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Some content databases are growing too large, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Some content databases are growing too large (SharePoint Server)

# Some content databases are growing too large (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Some content databases are growing too large.

**Summary:** The content databases have grown larger than 100 gigabytes (GB). Large content databases can be difficult to back up and restore. They are also more likely to cause the application to stop responding when you perform operations that affect entire databases.

**Cause:** Content databases exceed 100 GB.

**Resolution: Edit the rule definition to prevent new sites from being added to these databases, and then move some site collections to other databases.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Monitoring**.

On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.

On the Health Analyzer Rule Definitions page, in the **Availability** category, click the name of the rule.

In the **Health Analyzer Rule Definitions** dialog, click **Edit Item**, and then select the **Repair Automatically** check box.

Click **Save**. You can no longer add new sites to databases that exceed 100 GB.

Move some site collections to smaller databases. For more information, see Move site collections between databases in SharePoint Server.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
