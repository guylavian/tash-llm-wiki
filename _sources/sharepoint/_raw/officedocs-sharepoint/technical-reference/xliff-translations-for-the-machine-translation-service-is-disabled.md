---
title: "XLIFF translations for the Machine Translation Service is disabled (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: XLIFF translation for the Machine Translation Service is disabled, for SharePoint Server."
ms.topic: troubleshooting
---
Note

XLIFF translations for the Machine Translation Service is disabled (SharePoint Server)

# XLIFF translations for the Machine Translation Service is disabled (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** XLIFF translation for the Machine Translation Service is disabled.

**Summary:** There are several features in SharePoint Server that rely on the Machine Translation Service processing the XLIFF file format. If the .xlf extension is disabled, these features don't function correctly.

**Cause:** The .xlf file name extension is disabled for the Machine Translation Service.

**Resolution: Enable the .xlf file name extension for the Machine Translation Service.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.

In the **Enabled File Extensions** section, select the check box for the .xlf file name extension under the **XLIFF Parser**.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
