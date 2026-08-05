---
title: "Claims authentication doesn't validate user in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-claims-authentication-does-not-validate-user
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/claims-authentication-does-not-validate-user
family: administration
documentKind: "article"
abstract: "Because SharePoint Server recommends claims-based authentication for user access to web applications, this article describes the tools and techniques that you can use to troubleshoot failed claims-based user authentication attempts."
---

# Claims authentication doesn't validate user in SharePoint Server - SharePoint Server

Note

Claims authentication doesn't validate user in SharePoint Server

# Claims authentication doesn't validate user in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When users try to connect to a web application, logs record failed authentication events. If you use tools that Microsoft provides and use a systematic approach to examine failures, you can learn about common issues that relate to claims-based authentication and resolve them.

Successful access to a SharePoint resource requires both authentication and authorization. When you're using claims, authentication verifies that the security token is valid. Authorization verifies that access to the resource is allowed, based on the set of claims in the security token and the configured permissions for the resource.

To determine whether authentication or authorization causes an access issue, look closely at the error message in the browser window.

If the error message indicates that the user doesn't have access to the site, then the authentication was successful and the authorization failed. To troubleshoot authorization, try the following solutions:

The most common reason for failed authorization when you're using Security Assertion Markup Language (SAML) claims-based authentication is that the permissions were assigned to a user's Windows-based account (domain\user) instead of the user's SAML identity claim.

Verify that the user or a group to which the user belongs has been configured to use the appropriate permissions. For more information, see User permissions and permission levels in SharePoint Server.

Use the tools and techniques in this article to determine the set of claims in the user's security token so that you can compare it with the configured permissions.

If the message indicates that authentication failed, you have an authentication problem. If the resource is contained within a SharePoint web application that uses claims-based authentication, use the information in this article to start troubleshooting.

Troubleshooting tools

## Troubleshooting tools

The following are the primary troubleshooting tools that Microsoft provides to collect information about claims authentication in SharePoint Server:

Use **Unified Logging System (ULS) logs** to obtain the details of authentication transactions.

Use **Central Administration** to verify the details of user authentication settings for SharePoint web applications and zones and configure levels of ULS logging.

If you're using Active Directory Federation Services 2.0 (AD FS) as your federation provider for Security Assertion Markup Language (SAML)-based claims authentication, you can use **AD FS logging** to determine the claims that are in security tokens that AD FS issues to web client computers.

Use **Network Monitor 3.4** to capture and examine the details of user authentication network traffic.

Setting the level of ULS logging for user authentication

### Setting the level of ULS logging for user authentication

The following procedure configures SharePoint Server to log the maximum amount of information for claims authentication attempts.

**To configure SharePoint Server for the maximum amount of user authentication logging**

From Central Administration, select **Monitoring** on the Quick Launch, and then select **Configure diagnostic logging**.

In the list of categories, expand **SharePoint Foundation**, and then select **Authentication Authorization** and **Claims Authentication**.

In **Least critical event to report to the event log**, select **Verbose**.

In **Least critical event to report to the trace log**, select **Verbose**.

Select **OK**.

To optimize performance when you aren't performing claims authentication troubleshooting, follow these steps to set user authentication logging to its default values.

**To configure SharePoint Server for the default amount of user authentication logging**

From Central Administration, select **Monitoring** on the Quick Launch, and then select **Configure diagnostic logging**.

In the list of categories, expand **SharePoint Foundation**, and then select **Authentication Authorization** and **Claims Authentication**.

In **Least critical event to report to the event log**, select **Information**.

In **Least critical event to report to the trace log**, select **Medium**.

Select **OK**.

Configuring AD FS logging

### Configuring AD FS logging

Even after you enable the maximum level of ULS logging, SharePoint Server doesn't record the set of claims in a security token that it receives. If you use AD FS for SAML-based claims authentication, you can enable AD FS logging and use Event Viewer to examine the claims for security tokens that SharePoint Server issues.

**To enable AD FS logging**

On the AD FS server, from Event Viewer, select **View**, and then select **Show Analytic and Debug Logs**.

In the Event Viewer console tree, expand **Applications and Services Logs/AD FS 2.0 Tracing**.

Right-click **Debug**, and then select **Enable Log**.

Open the %ProgramFiles% **\Active Directory Federation Services 2.0** folder.

Use Notepad to open the **Microsoft.IdentityServer.ServiceHost.Exe.Config** file.

Select **Edit**, select **Find**, type **<source name="Microsoft.IdentityModel" switchValue="Off">**, and then select **OK**.

Change **switchValue="Off"** to **switchValue="Verbose"**.

Select **File**, select **Save**, and then exit Notepad.

From the Services snap-in, right-click the ** AD FS 2.0 service **, and then select **Restart**.

You can now use Event Viewer on the AD FS server to examine details about claims from the Applications and Services Logs/AD FS 2.0 Tracing/Debug node. Look for events with Event ID 1001.

You can also enumerate claims with an HttpModule or web part or through OperationContext. For more information, see How to Get All User Claims at Claims Augmentation Time in SharePoint 2010. This information about SharePoint 2010 applies also to SharePoint 2013.

Troubleshooting methodology for claims user authentication

## Troubleshooting methodology for claims user authentication

The following steps can help you determine the cause of failed claims authentication attempts.

Step 1: Determine the details of the failed authentication attempt

### Step 1: Determine the details of the failed authentication attempt

To obtain detailed and definitive information about a failed authentication attempt, you have to find it in the SharePoint ULS logs. These log files are stored in the %CommonProgramFiles%\Microsoft Shared\Web Server Extensions\15\LOGS folder.

You can find the failed authentication attempt in the ULS log files either manually or you can use the ULS Log Viewer.

**To find the failed authentication attempt manually**

Obtain the user account name that produces the failed authentication attempt from the user.

On the server that is running SharePoint Server or SharePoint Foundation, find the %CommonProgramFiles% **\Microsoft Shared\Web Server Extensions\16\LOGS** or %CommonProgramFiles% **\Microsoft Shared\Web Server Extensions\15\LOGS** folder.

In the **LOGS** folder, select **Date modified** to sort the folder by date, with the most recent at the top.

Try the authentication task again.

In the **LOGS** folder window, double-click the log file at the top of the list to open the file in Notepad.

In **Notepad**, select **Edit,** select **Find**, type **Authentication Authorization** or **Claims Authentication**, and then select **Find Next**.

Select **Cancel**, and then read the contents of the **Message** column.

To use the ULS Viewer, download it from ULS Viewer and save it to a folder on the server that is running SharePoint Server or SharePoint Foundation. After it's installed, follow these steps to locate the failed authentication attempt.

**To find the failed authentication attempt with the ULS Viewer**

On the server that is running SharePoint Server or SharePoint Foundation, double-click **Ulsviewer** from the folder in which it's stored.

In the **ULS Viewer**, select **File**, point to **Open From**, and then select **ULS**.

In the **Setup the ULS Runtime feed** dialog, verify that %CommonProgramFiles% **\Common Files\Microsoft Shared\Web Server Extensions\16\LOGS folder** or **\Common Files\Microsoft Shared\Web Server Extensions\15\LOGS folder** is specified in **Use ULS feed from default log-file directory**. If not, select **Use directory location for real-time feeds** and specify the %CommonProgramFiles% **\Microsoft Shared\Web Server Extensions\16\LOGS folder** or **\Microsoft Shared\Web Server Extensions\15\LOGS folder** in **Log file location**.

For %CommonProgramFiles%, substitute the value from the CommonProgramFiles environment variable of the server that is running SharePoint Server or SharePoint Foundation. For example, if the location is the C drive, %CommonProgramFiles% is set to C:\Program Files\Common Files.

Select **OK**.

Select **Edit**, and then select **Modify Filter**.

In the **Filter by** dialog, in **Field**, select **Category**.

In **Value**, type **Authentication Authorization** or **Claims Authentication**, and then select **OK**.

Repeat the authentication attempt.

From the **ULS Viewer** window, double-click the displayed lines to view the **Message** portion.

From the claims encoding part of the Message portion for non-OAuth requests, you can determine the authentication method and encoded user identity from the claims-encoded string (example: i:0#.w|contoso\chris).

Step 2: Check configuration requirements

### Step 2: Check configuration requirements

To determine how a web application or zone is configured to support one or more claims authentication methods, use the SharePoint Central Administration website.

**To verify the authentication configuration for a web application or zone**

From Central Administration, select **Application Management** on the Quick Launch, and then select **Manage web applications**.

Select the name of the web application that the user is trying to access, and in the **Security** group of the ribbon, select **Authentication Providers**.

In the list of authentication providers, select the appropriate zone (such as **Default**).

In the **Edit Authentication** dialog, in the **Claims Authentication Types** section, verify the settings for claims authentication.

For Windows claims authentication, verify that **Enable Windows Authentication** and **Integrated Windows authentication** are selected, and that either **NTLM** or **Negotiate (Kerberos)** is selected as needed. Select **Basic authentication** if it's needed.

For forms-based authentication, verify that **Enable Forms Based Authentication (FBA)** is selected. Verify the values in **ASP.NET Membership provider name** and **ASP.NET Role manager name**. These values must match the membership provider and role values that you configured in your web.config files for the SharePoint Central Administration website, web application, and SharePoint Web Services\SecurityTokenServiceApplication. For more information, see Configure forms-based authentication for a claims-based web application in SharePoint Server.

For SAML-based claims authentication, verify that **Trusted identity provider** and the correct trusted provider name are selected. For more information, see Configure SAML-based claims authentication with AD FS in SharePoint Server.

In the **Sign In Page URL** section, verify the option for the sign-in page. For a default sign-in page, **Default Sign In Page** should be selected. For a custom sign-in-page, verify the specified URL of the custom sign-in page. To verify it, copy the URL, and then attempt to access it using a web browser.

Select **Save** to save the changes to the authentication settings.

Repeat the authentication attempt. For forms-based or SAML-based authentication, does the expected sign-in page appear with the correct sign-in options?

If authentication still fails, check the ULS logs to determine whether there's any difference between the authentication attempt before the authentication configuration change and after it.

Step 3: More items to check

### Step 3: More items to check

After you check the log files and web application configuration, verify the following:

The web browser on the web client computer supports claims. For more information, see Plan browser support in SharePoint Server 2016.

For Windows claims authentication, verify that the following:

The computer from which the user issues the authentication attempt is a member of the same domain as the server that hosts the SharePoint web application or a member of a domain that the hosting server trusts.

The computer from which the user issues the authentication attempt is logged on to its Active Directory Domain Services (AD DS) domain. Type **nltest /dsgetdc: /force** at a Command Prompt or the SharePoint Management Shell on the web client computer to make sure that it can access a domain controller. If no domain controllers are listed, troubleshoot the lack of discoverability and connectivity between the web client computer and an AD DS domain controller.

The server that is running SharePoint Server or SharePoint Foundation is logged on to its AD DS domain. Type **nltest /dsgetdc: /force** at a Command Prompt or the SharePoint Management Shell on the server that is running SharePoint Server or SharePoint Foundation to make sure that it can access a domain controller. If no domain controllers are listed, troubleshoot the lack of discoverability and connectivity between the server that is running SharePoint Server or SharePoint Foundation and an AD DS domain controller.

For forms-based authentication, verify that the following:

The user credentials for the configured ASP.NET membership and role provider are correct.

The systems that host the ASP.NET membership and role provider are available on the network.

Custom sign-in pages correctly collect and convey the user's credentials. To test this, configure the web application to temporarily use the default sign-in page and verify that it works.

For SAML-based claims authentication, verify that the following:

The user credentials for the configured identity provider are correct.

Systems that act as the federation provider (such as AD FS) and the identity provider (such as AD DS or a third-party identity provider) are available on the network.

Custom sign-in pages correctly collect and convey the user's credentials. To test this, configure the web application to temporarily use the default sign-in page and verify that it works.

Step 4: Use a web debug tool to monitor and analyze web traffic

### Step 4: Use a web debug tool to monitor and analyze web traffic

Use a tool such as HttpWatch or Fiddler to analyze the following types of HTTP traffic:

Between the web client computer and the server that is running SharePoint Server or SharePoint Foundation

For example, you can monitor the HTTP Redirect messages that the server that is running SharePoint Server or SharePoint Foundation sends to inform the web client computer of the location of a federation server (such as AD FS).

Between the web client computer and the federation server (such as AD FS)

For example, you can monitor the HTTP messages that the web client computer sends and the responses of the federation server, which could include security tokens and their claims.

Note

If you use Fiddler, the authentication attempt can fail after requiring three authentication prompts. To prevent this behavior, see Using Fiddler With SAML and SharePoint to Get Past the Three Authentication Prompts.

Step 5: Capture and analyze authentication network traffic

### Step 5: Capture and analyze authentication network traffic

Use a network traffic tool, such as Network Monitor 3.4, to capture and analyze traffic between the web client computer, the server that is running SharePoint Server or SharePoint Foundation, and the systems on which SharePoint Server or SharePoint Foundation relies for claims authentication.

Note

In many cases, claims authentication uses Hypertext Transfer Protocol Secure (HTTPS)-based connections, which encrypt the messages sent between computers. You cannot see the contents of encrypted messages with a network traffic tool without the aid of an add-in or extension. For example, for Network Monitor, you must install and configure the Expert to Network Monitor. As an easier alternative to attempting to decrypt HTTPS messages, use a tool such as Fiddler on the server that hosts SharePoint Server or SharePoint Foundation, which can report on the unencrypted HTTP messages.

An analysis of the network traffic can reveal the following:

The exact set of protocols and messages that are being sent between the computers involved in the claims authentication process. Reply messages can contain error condition information, which you can use to determine more troubleshooting steps.

Whether request messages have corresponding replies. Multiple sent request messages that don't receive a reply can indicate that the network traffic isn't reaching its intended destination. In that case, check for packet routing issues, packet filtering devices in the path (such as a firewall), or packet filtering on the destination (such as a local firewall).

Whether multiple claims methods are being tried, and which are failing.

For Windows claims authentication, you can capture and analyze the traffic between the following computers:

The web client computer and the server that is running SharePoint Server or SharePoint Foundation

The server that is running SharePoint Server or SharePoint Foundation and its domain controller

For forms-based authentication, you can capture and analyze the traffic between the following computers:

The web client computer and the server that is running SharePoint Server or SharePoint Foundation

The server that is running SharePoint Server or SharePoint Foundation and the ASP.NET membership and role provider

For SAML-based claims authentication, you can capture and analyze the traffic between the following computers:

The web client computer and the server that is running SharePoint Server or SharePoint Foundation

The web client computer and its identity provider (such as an AD DS domain controller)

The web client computer and the federation provider (such as AD FS)

See also

## See also

Other Resources

#### Other Resources

Configure forms-based authentication for a claims-based web application in SharePoint Server

Configure SAML-based claims authentication with AD FS in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2024-12-03
