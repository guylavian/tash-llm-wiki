---
title: "Verify that OAuth is configured correctly for the Machine Translation Service application proxy (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify that OAuth is configured correctly for the Machine Translation Service application proxy, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Verify that OAuth is configured correctly for the Machine Translation Service application proxy (SharePoint Server)

# Verify that OAuth is configured correctly for the Machine Translation Service application proxy (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Verify that OAuth is configured correctly for the Machine Translation Service application proxy.

**Summary:** The Machine Translation Service application proxy that is provisioned on the farm can function correctly only when OAuth is correctly configured.

**Cause:** OAuth is not configured correctly for the Machine Translation Service application proxy.

**Resolution: Ensure that every Web application with a Machine Translation Service application proxy has a connection to a User Profile service application and an App Management service application, and is in claims-based authentication mode.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Application Management**.

On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.

In the **Application Proxy Group** column, click the proxy group for the Web application or service application that you want to configure. Usually it is the **default** Application Proxy Group.

Select the **User Profile Service Application Proxy** check box and the **App Management Service Application Proxy** check box.

Go back to Central Administration and in the **Application Management** section, click **Manage web applications**.

Click the Web application you want to configure, and then click the **Authentication Providers** button on the ribbon.

Ensure that the Membership Provider Name for the **Default** zone is **Claims Based Authentication**. If not, you have to migrate the Web applications from classic mode to claims-based authentication. For more information, see Migrate from classic-mode to claims-based authentication in SharePoint Server.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
