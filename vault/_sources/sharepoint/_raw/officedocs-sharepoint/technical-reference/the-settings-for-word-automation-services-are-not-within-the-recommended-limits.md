---
title: "The settings for Word Automation Services are not within the recommended limits (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer ruleThe settings for Word Automation Services are not within the recommended limits, in SharePoint Server."
ms.topic: troubleshooting
---
Note

The settings for Word Automation Services are not within the recommended limits (SharePoint Server)

# The settings for Word Automation Services are not within the recommended limits (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The settings for Word Automation Services are not within the recommended limits.

**Summary:** The throughput of Word Automation Services is limited by system resources on the application server. If the values for conversion processes and conversion throughput are set too high, the overall health of the application server can degrade, and other services on the computer can be affected. Additionally, Word Automation Services can experience decreased throughput and more conversion failures.

**Cause:** The settings for Word Automation Services are incorrect.

**Resolution: Change the settings for Word Automation Services.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, in the list of service applications, click **Word Automation Services**.

In the **Conversion Processes** section, type a value that ranges from 1 to 1000 in the **Conversion processes** text box. The default conversion processes is set at 1.

In the **Conversion Throughput** section, type a value that ranges from 1 to 59 in the **Frequency with which to start conversions (minutes)** text box, and a value that ranges from 1 to 1000 in the **Number of conversions to start (per conversion process)** text box, and then click **OK**. The default conversion throughput is set at 15.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
