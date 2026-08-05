---
title: "Basic authentication is being deprecated (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-basic-auth-is-being-deprecated
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/basic-auth-is-being-deprecated
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to disable Basic authentication as it is being deprecated."
---

# Basic authentication is being deprecated (SharePoint Server) - SharePoint Server

Note

Basic authentication is being deprecated (SharePoint Server)

# Basic authentication is being deprecated (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Basic authentication is being deprecated

**Summary:** Basic authentication is currently enabled in one or more web applications within SharePoint Server. It's important to note that Basic authentication is being deprecated and will no longer be supported in SharePoint Server for all scenarios. For more information, see What's deprecated or removed from SharePoint Server Subscription Edition.

Basic authentication doesn't provide confidentiality protection for the transmitted credentials. To better protect your SharePoint Server, it's highly recommended that you migrate web applications to a modern authentication mechanism (for example, Trusted Identity providers) as soon as possible.

**Cause:** One or more web applications in your SharePoint Server are using Basic authentication, which is being deprecated.

**Resolution: Disable Basic authentication**

Ensure that Basic authentication is disabled in both SharePoint Server and IIS settings:

Follow these steps to disable Basic authentication in SharePoint Server:

- Verify that you're the farm admin.

- Navigate to **Central Administration,** select **Application Management,**  and then select **Manage web applications**.

- Select the web application you want to disable Basic authentication.

- Click on the **Authentication Providers** link in the ribbon.

- Choose the appropriate zone for the web application.

- Uncheck the option **Basic authentication (password is sent in clear text)**.

Follow these steps to disable Basic authentication in IIS:

- Verify that you're a member of the Administrators group on the server where you're configuring IIS.

- On the Start menu, point to All Programs, select **Administrative Tools,** and then select **Internet Information Services (IIS) Manager** to start the IIS Management Console.

- Expand Sites on the console tree, right-click the IIS web site that corresponds to the web application zone where you want to disable Basic authentication.

- In the middle pane, double-click the **Authentication** icon.

- In the Authentication pane, locate and select **Basic authentication**.

- In the Actions pane on the right-hand side, click **Disable** to disable Basic authentication.

Additional resources

## Additional resources

- Last updated on 
		2023-09-12
