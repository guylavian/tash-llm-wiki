---
title: "Verify that OAuth is configured correctly for the Machine Translation Service application (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify that OAuth is configured correctly for the Machine Translation Service application, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Verify that OAuth is configured correctly for the Machine Translation Service application (SharePoint Server)

# Verify that OAuth is configured correctly for the Machine Translation Service application (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Verify that OAuth is configured correctly for the Machine Translation Service application.

**Summary:** The Machine Translation Service application that is provisioned on the farm can function correctly only when OAuth is correctly configured.

**Cause:** OAuth isn't configured correctly for the Machine Translation Service application.

**Resolution: Ensure that a default User Profile Service Application proxy exists in the default farm service application proxy group.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Application Management**.

On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.

In the **Application Proxy Group** column, click the proxy group for the Web application or service application that you want to configure. Usually it is the **default** Application Proxy Group.

Select the **User Profile Service Application Proxy** check box.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
