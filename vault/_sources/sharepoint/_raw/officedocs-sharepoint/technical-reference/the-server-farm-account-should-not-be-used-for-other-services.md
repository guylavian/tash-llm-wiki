---
title: "The server farm account should not be used for other services (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: The server farm account should not be used for the other services, for SharePoint Server."
ms.topic: troubleshooting
---
Note

The server farm account should not be used for other services (SharePoint Server)

# The server farm account should not be used for other services (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The server farm account should not be used for the other services.

**Summary:** The account that is used to run the SharePoint Server Timer service and other system services in the SharePoint farm should not be used for other services in the farm.

**Cause:** The farm account, which is used for the SharePoint Server Timer service and the SharePoint Central Administration website, is highly privileged and should not be used for other services on any computers in the server farm. Services in the farm were found to use this account.

Note

You can ignore this event if using the User Profile Synchronization service. The User Profile Synchronization service must run as the farm account in SharePoint Server.

**Resolution: Change the account that is used for other services.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

In Central Administration , in the **Security** section, click **Configure service accounts**.

On the Service Accounts page, in the **Credential Management** section, in the drop-down list, click the service that you want to update credentials.

In the **Select an account for this component** list, click the domain account that you want to associate with this service.

If you want to register the account that you selected on the SharePoint Server farm, click **Register new managed account**.

Click **OK**.

For more information, see Account permissions and security settings in SharePoint Server 2016 and Account permissions and security settings in SharePoint 2013.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
