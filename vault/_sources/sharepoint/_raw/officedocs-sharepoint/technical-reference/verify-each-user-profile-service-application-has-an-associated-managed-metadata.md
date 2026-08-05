---
title: "Verify each User Profile Service Application has an associated Managed Metadata Service Connection (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify each User Profile Service Application has an associated Managed Metadata Service Connection, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Verify each User Profile Service Application has an associated Managed Metadata Service Connection (SharePoint Server)

# Verify each User Profile Service Application has an associated Managed Metadata Service Connection (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Verify each User Profile Service Application has an associated Managed Metadata Service Connection.

**Summary:** If the Managed Metadata service is not associated with the User Profile service application, features such as social tagging and properties backed by managed terms do not work.

**Cause:** The Managed Metadata service connection is not included in the group of connections that is associated with the User Profile service application.

**Resolution: Edit the connections for the User Profile service application.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the Central Administration home page, click **Application Management**.

On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.

On the Service Application Associations page, in the **View** list, click **Service Applications**.

In the **Web Application/Service Application** column, click the User Profile service application for which you want to edit the connection.

In the **Configure Service Application Associations** dialog, select the **Managed Metadata Service** check box, or select **Default** in the **Edit the following group of connections** list, and then click **OK**. By default, all connections are included.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
