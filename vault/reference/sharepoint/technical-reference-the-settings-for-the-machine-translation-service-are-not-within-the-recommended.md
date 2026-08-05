---
title: "The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-the-settings-for-the-machine-translation-service-are-not-within-the-recommended
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/the-settings-for-the-machine-translation-service-are-not-within-the-recommended
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: The settings for the Machine Translation Service are not within the recommended limits, for SharePoint Server."
---

# The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server) - SharePoint Server

Note

The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server)

# The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The settings for the Machine Translation Service are not within the recommended limits.

**Summary:** The throughput of the Machine Translation Service is limited by system resources on the application server. If the values for translation processes and translation throughput are set too high, the overall health of the application server can decrease, and other services on the computer can be affected. Additionally, the Machine Translation Service can experience decreased throughput and more translation failures.

**Cause:** The settings for the Machine Translation Service are incorrect.

**Resolution: Change the settings for the Machine Translation Service.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.

In the **Translation Processes** section, type a value that ranges from 1 to 1000 in the **Translation processes** box. The default value for Translation processes is set at 1.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
