---
title: "Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and haven't been mistakenly deleted, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted (SharePoint Server)

# Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and haven't been mistakenly deleted.

**Summary:** User Profile Service Application or User Profile service proxy timer jobs aren't available and might have been deleted.

**Cause:** A required timer job for the User Profile service or the User Profile service proxy is missing.

**Resolution: Edit the rule definition so that the configuration is automatically repaired.**

On the SharePoint Central Administration website, select **Monitoring**.

On the Monitoring page, in the **Health Analyzer** section, select **Review rule definitions**.

On the Health Analyzer Rule Definitions - All Rules page, in the **Category: Configuration** section, select the name of the rule.

In the **Health Analyzer Rule Definitions** dialog, select **Edit Item**.

Select the **Repair Automatically** check box, and then select **Save**.

The system automatically creates the missing timer jobs.

For more information, see Default timer jobs in SharePoint Server 2019, Default timer jobs in SharePoint Server 2016, or Default timer jobs in SharePoint 2013.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
