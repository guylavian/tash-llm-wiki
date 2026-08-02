---
title: "Create web applications that use classic mode authentication in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: security-for-sharepoint-server-create-web-applications-that-use-classic-mode-authentication
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/create-web-applications-that-use-classic-mode-authentication
family: security-for-sharepoint-server
documentKind: "how-to"
abstract: "Learn how to create a web application that uses classic mode (Windows-classic) authentication in SharePoint Server."
---

# Create web applications that use classic mode authentication in SharePoint Server - SharePoint Server

Note

Create web applications that use classic mode authentication in SharePoint Server

# Create web applications that use classic mode authentication in SharePoint Server

**APPLIES TO:** 2013 2016 2019 SharePoint in Microsoft 365

In SharePoint Server, claims-based authentication is the default and preferred method of user authentication and is required to take advantage of server-to-server authentication and app authentication. In Central Administration, you can only configure claims-based authentication when you manage web applications. You can also use Microsoft PowerShell cmdlets. The use of classic mode authentication, also known as Windows classic authentication, is discouraged in SharePoint Server and you can only create or configure web applications for classic mode authentication with Microsoft PowerShell cmdlets.

Important

Office Online can be used only by SharePoint Server web applications that use claims-based authentication. Office Online rendering and editing will not work on SharePoint Server web applications that use classic mode authentication. If you migrate SharePoint 2010 web applications that use classic mode authentication to SharePoint Server 2016, you must migrate them to claims-based authentication to allow them to work with Office Online. For more information, see Use Office Web Apps with SharePoint 2013.

To use Windows claims-based authentication instead (recommended), see Create a web application that uses Windows-claims authentication. To convert a web application that uses classic mode to use claims-based authentication, see Migrate from classic-mode to claims-based authentication in SharePoint Server.

Important

The steps in this article apply to both SharePoint Foundation 2013 and SharePoint Server.

Before you begin

## Before you begin

Before you perform this procedure, confirm the following:

You have determined the design of your logical architecture.

For additional information, see Logical architecture components.

You have planned authentication for your web application.

For additional information, see Plan for user authentication methods in SharePoint Server.

If you use Secure Sockets Layer (SSL), you must associate the SSL certificate with the web application's IIS website after the IIS website is created. SSL is required by default for web applications that are used in server-to-server authentication and app authentication scenarios.

You understand host-named site collections.

Create a web application that uses classic mode authentication with PowerShell

## Create a web application that uses classic mode authentication with PowerShell

Perform the following procedure to use PowerShell to create a web application that uses classic mode authentication.

**To create a web application that uses classic mode authentication with PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
New-SPWebApplication -Name <Name> -ApplicationPool <ApplicationPool> -AuthenticationMethod <WindowsAuthType> -ApplicationPoolAccount <ApplicationPoolAccount> -Port <Port> -URL <URL>
```

Where:

*<Name>* is the name of the new web application.

*<ApplicationPool>* is the name of the application pool.

*< WindowsAuthType >* is either "NTLM" or "Kerberos". Kerberos is recommended.

*<ApplicationPoolAccount>* is the user account that this application pool will run as.

*<Port>* is the port on which the web application will be created in IIS.

*<URL>* is the public URL for the web application.

**Example**

```
New-SPWebApplication -Name "Contoso Internet Site" -ApplicationPool "ContosoAppPool" -AuthenticationMethod "Kerberos" -ApplicationPoolAccount (Get-SPManagedAccount "CONTOSO\jdoe") -Port 80 -URL "https://www.contoso.com"
```

For more information, see New-SPWebApplication.PShell_stsadm_deprecated

After this procedure is complete, you can create one or more site collections for this web application. For more information, see Create a site collection in SharePoint Server.

After you successfully create the web application, when you open the Central Administration page, you see a health rule warning that indicates that one or more web applications is enabled with classic authentication mode. This is a reflection of our recommendation to use claims-based authentication instead of classic mode authentication.

See also

## See also

Concepts

#### Concepts

Create a Web application that uses Windows-claims authentication)

Other Resources

#### Other Resources

Plan for user authentication methods in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
