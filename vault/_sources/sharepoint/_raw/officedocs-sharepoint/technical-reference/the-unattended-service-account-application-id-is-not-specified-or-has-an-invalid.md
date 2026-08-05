---
title: "The unattended Service Account Application ID is not specified or has an invalid value (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Unattended Service Account Application ID is not specified or has an invalid value, for SharePoint Server."
ms.topic: troubleshooting
---
Note

The unattended Service Account Application ID is not specified or has an invalid value (SharePoint Server)

# The unattended Service Account Application ID is not specified or has an invalid value (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule name:** The Unattended Service Account Application ID is not specified or has an invalid value.

**Summary:** The Unattended Service Account Application ID setting stores an application identifier (ID) in the registered Secure Store Service. The application ID is used to reference the Unattended Service Account credentials. The Unattended Service Account is a single, low-privileged account that Visio Graphics Service impersonates when it connects to data sources external to SharePoint Server, such as SQL Server. This account is required to connect to these external data sources. For more information about Visio Graphics Service, see Plan for Visio Services in SharePoint Server and Plan Visio Services security in SharePoint Server.

**Resolution: Specify a valid application ID value**

Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application and the Secure Store Service service application.

In Central Administration, on the Home page, in the **Application Management** section, click **Manage service applications**.

On the Service Applications page, click the Secure Store Service service application.

On the Secure Store Service page, record the application ID from the **Target Application ID** column.

For more information about the Secure Store Service service application, see Plan the Secure Store Service in SharePoint Server.

On the Service Applications page, click the Visio Graphics service application.

On the Manage the Visio Graphics Service page, click **Global Settings**.

On the Visio Graphics Service Settings page, in the **External Data** section, in the **Unattended Service Account** text box, type the application ID that you recorded in step 4 of this procedure.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
