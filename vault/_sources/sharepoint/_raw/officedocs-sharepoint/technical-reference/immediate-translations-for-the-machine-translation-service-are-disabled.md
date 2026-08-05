---
title: "Immediate translations for the Machine Translation service are disabled (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule:Immediate translations for the Machine Translation service are disabled, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Immediate translations for the Machine Translation service are disabled (SharePoint Server)

# Immediate translations for the Machine Translation service are disabled (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Immediate translations for the Machine Translation service are disabled.

**Summary:** There are several features in SharePoint Server that rely on the Machine Translation Service synchronous translation mode. If immediate translations are disabled, these features don't function correctly.

**Cause:** Synchronous translations for the Machine Translation service are disabled.

**Resolution: Enable synchronous translations for the Machine Translation service.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.

In the **Maximum Synchronous Translation Requests** section, type a value that ranges from 1 to 1000 in the **Maximum number of synchronous translation requests (per server)** text box. A value of 0 indicates that synchronous translations are disabled.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
