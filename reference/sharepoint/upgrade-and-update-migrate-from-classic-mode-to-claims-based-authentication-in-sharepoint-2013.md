---
title: "Migrate from classic-mode to claims-based authentication in SharePoint 2013 - SharePoint Server"
type: reference
domain: sharepoint
slug: upgrade-and-update-migrate-from-classic-mode-to-claims-based-authentication-in-sharepoint-2013
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/upgrade-and-update/migrate-from-classic-mode-to-claims-based-authentication-in-sharepoint-2013
family: upgrade-and-update
documentKind: "upgrade-and-migration-article"
abstract: "Convert SharePoint 2010 Products or SharePoint 2013 classic-mode web applications to claims-based authentication or create new claims-based web applications in SharePoint 2013."
---

# Migrate from classic-mode to claims-based authentication in SharePoint 2013 - SharePoint Server

Note

Migrate from classic-mode to claims-based authentication in SharePoint 2013

# Migrate from classic-mode to claims-based authentication in SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Claims-based authentication is an essential component to enable the advanced functionality of SharePoint 2013. To move classic-mode web applications from SharePoint 2010 Products to SharePoint 2013, you can convert them to claims-based web applications within SharePoint 2010 Products, and then migrate them to SharePoint 2013. The procedures in this article illustrate various supported scenarios.

The PowerShell **Convert-SPWebApplication** cmdlet in SharePoint 2013 converts classic-mode web applications to claims-based web applications.

Caution

After you convert a web application to claims-based authentication, you cannot revert it to classic-mode authentication.

Convert SharePoint 2010 Products classic-mode web applications to claims-based authentication in SharePoint 2010 Products and then upgrade to SharePoint 2013

## Convert SharePoint 2010 Products classic-mode web applications to claims-based authentication in SharePoint 2010 Products and then upgrade to SharePoint 2013

In SharePoint 2010 Products, complete the following procedure to convert an existing web application to claims-based authentication. After you convert the web application to claims-based authentication, complete the additional step to migrate the web application to SharePoint 2013. To complete this procedure, you need the following information:

The URL of the web application that you are converting:  *http://yourWebAppUrl*

A user account to set as a site administrator:  *yourDomain\yourUser*

**To convert a SharePoint 2010 Products web application to claims-based authentication**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running PowerShell cmdlets.

You must read about_Execution_Policies (https://go.microsoft.com/fwlink/p/?LinkId=193050).

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

- From the PowerShell command prompt, type the following to set the specified user account as an administrator for the site:

```
$WebAppName = "http://<yourWebAppUrl>"
$wa = get-SPWebApplication $WebAppName
$wa.UseClaimsAuthentication = $true
$wa.Update()
```

Where:

- *<yourWebAppUrl>* is the URL of the web application.

- From the PowerShell command prompt, type the following to configure the policy to enable the user to have full access:

```
$account = "yourDomain\yourUser"
$account = (New-SPClaimsPrincipal -identity $account -identitytype 1).ToEncodedString()
$wa = get-SPWebApplication $WebAppName
$zp = $wa.ZonePolicies("Default")
$p = $zp.Add($account,"PSPolicy")
$fc=$wa.PolicyRoles.GetSpecialRole("FullControl")
$p.PolicyRoleBindings.Add($fc)
$wa.Update()
```

For more information, see Get-SPWebApplication.

- From the PowerShell command prompt, type the following to perform user migration:

```
$wa.MigrateUsers($true)
```

- After user migration completes, type the following from the PowerShell command prompt to perform provisioning:

```
$wa.ProvisionGlobally()
```

For more information, see New-SPClaimsPrincipal.

After you complete the previous procedures, you might experience one or more of the following issues:Users who submit valid credentials when accessing the migrated web application might be notified that they do not have permissions. If this occurs, the portalsuperuseraccount property and the portalsuperreaderaccount property of the web application were probably configured prior to migration. If this is the case, update the portalsuperuseraccount property and the portalsuperreaderaccount property to use the new claims-based account name. After migration, you can find the new claims-based account name in the web application policy for the migrated web application.If existing alerts are not invoked after migration, you might have to delete and recreate the alerts.If Search crawl does not function on the web application after migration, make sure that the Search crawl account lists the new converted account name. If the new converted account name is not listed, you must manually create a new policy for the crawl account.

**To migrate a claims-based SharePoint 2010 Products web application to SharePoint 2013**

In SharePoint 2013, create a claims-based web application. For more information, see Create claims-based web applications in SharePoint Server.

Attach the two existing SharePoint 2010 Products content databases to the newly created SharePoint 2013 claims-based web application. For more information, see Attach or detach content databases in SharePoint Server.

Note

When you attach the SharePoint 2010 Products content databases to the SharePoint 2013 claims-based web application, the databases will be upgraded to the SharePoint 2013 database format but will not be claims-enabled.

Convert SharePoint 2010 Products classic-mode web applications to SharePoint 2013 claims-based web applications

## Convert SharePoint 2010 Products classic-mode web applications to SharePoint 2013 claims-based web applications

In SharePoint 2013, complete the following procedure to convert an existing SharePoint 2010 Products classic-mode web application to a SharePoint 2013 web application that uses claims-based authentication.

**To convert a SharePoint 2010 Products classic-mode web application to a SharePoint 2013 claims-based authentication**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running PowerShell cmdlets.

You must read about_Execution_Policies (https://go.microsoft.com/fwlink/p/?LinkId=193050).

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

In the SharePoint 2013 environment, on the **Start** menu, click **All Programs**.

Click **SharePoint 2013**.

Click **SharePoint 2013 Management Shell**.

Change to the directory where you saved the file.

At the PowerShell command prompt, type the following command:

```
$ap = New-SPAuthenticationProvider -UseWindowsIntegratedAuthentication -DisableKerberos
New-SPWebApplication -name "ClaimsWebApp" -Port 80 -ApplicationPool "ClaimsAuthAppPool" -ApplicationPoolAccount (Get-SPManagedAccount "<domainname>\<user>") -AuthenticationMethod NTLM -AuthenticationProvider $ap
```

Where:

- *<domainname>*\ *<user>* is the domain to which the server belongs and the name of the user account.

Attach the two existing SharePoint 2010 Products content databases to the new SharePoint 2013 claims-mode web application. For more information, see Attach or detach content databases in SharePoint Server.

Note

When you attach the SharePoint 2010 Products content databases to the SharePoint 2013 claims-mode web application, the databases are upgraded to the SharePoint 2013 database format. You have to verify that the content databases work correctly after you have attached them.

From the PowerShell command prompt, type the following:

```
Convert-SPWebApplication -Identity <yourWebAppUrl> -From Legacy -To Claims -RetainPermissions [-Force]
```

Where:

- *<yourWebAppUrl>* is the URL of the web application.

Note

**Convert-SPWebApplication** converts the content databases to claims-based authentication. You have to verify that the users can access the web application after you have converted the content databases.

If necessary, attach a third SharePoint 2010 Products content database to the new SharePoint 2013 claims-mode web application, and verify that the content database working correctly after you have attached it.

From the PowerShell command prompt, type the following:

```
Convert-SPWebApplication -Identity <yourWebAppUrl> -From Legacy -To Claims -RetainPermissions [-Force]
```

Verify that users can access the web application after you have converted the content databases to claims-based authentication. For more information, see New-SPWebApplication, Get-SPManagedAccount, and Convert-SPWebApplication.

Convert SharePoint 2013 classic-mode web applications to claims-based web applications

## Convert SharePoint 2013 classic-mode web applications to claims-based web applications

In SharePoint 2013, complete the following procedures to first create a classic-mode Web application, and then convert it to claims-based authentication.

**To create a classic-mode Web application in SharePoint 2013**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running PowerShell cmdlets.

You must read about_Execution_Policies (https://go.microsoft.com/fwlink/p/?LinkId=193050).

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

From the PowerShell command prompt, type the following:

```
New-SPWebApplication -Name <Name> -ApplicationPool <ApplicationPool> -AuthenticationMethod <WindowsAuthType> -ApplicationPoolAccount <ApplicationPoolAccount> -Port <Port> -URL <URL>
```

Where:

*<Name>* is the name of the new web application that uses classic-mode authentication.

*<ApplicationPool>* is the name of the application pool.

*<WindowsAuthType>* is either "NTLM" or "Kerberos". Kerberos is recommended.

*<ApplicationPoolAccount>* is the user account that this application pool will run as.

*<Port>* is the port on which the web application will be created in IIS.

*<URL>* is the public URL for the web application.

Note

For more information, see New-SPWebApplication.

Note

After you successfully create the web application, when you open the Central Administration page, you see a health rule warning that indicates that one or more web applications is enabled with classic authentication mode. This is a reflection of our recommendation to use claims-based authentication instead of classic mode authentication.

**To convert a SharePoint 2013 classic-mode web application to claims-based authentication**

From the PowerShell command prompt, type the following:

```
Convert-SPWebApplication -Identity "http:// <servername>:port" -From Legacy -To Claims -RetainPermissions [-Force]
```

Where:

- *<servername>* is the name of the server.

Verify that users can access the web application after you have converted it to claims-based authentication.For more information, see New-SPWebApplication, Get-SPManagedAccount, and Convert-SPWebApplication.

Migrate SharePoint 2010 Products classic-mode web applications to SharePoint 2013 classic-mode web applications

## Migrate SharePoint 2010 Products classic-mode web applications to SharePoint 2013 classic-mode web applications

In SharePoint 2013, complete the following procedure to create a classic-mode web application, and then migrate an existing SharePoint 2010 Products classic-mode Web application to SharePoint 2013.

**To migrate a SharePoint 2010 Products classic-mode web application to SharePoint 2013**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running PowerShell cmdlets.

You must read about_Execution_Policies (https://go.microsoft.com/fwlink/p/?LinkId=193050).

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

- From the PowerShell command prompt, type the following:

```
New-SPWebApplication -name "ClassicAuthApp" -Port 100 -ApplicationPool "ClassicAuthAppPool" -ApplicationPoolAccount (Get-SPManagedAccount "<domainname>\<user>")
```

Where:

- *<domainname>*\ *<user>* is the domain to which the server belongs and the name of the user account.

- Attach the two existing SharePoint 2010 Products content databases to the new SharePoint 2013 classic-mode web application. Verify that the content databases work correctly after you have attached them. For more information, see Attach or detach content databases in SharePoint Server.

For more information, see New-SPWebApplication and Get-SPManagedAccount.

See also

## See also

Other Resources

#### Other Resources

Create claims-based web applications in SharePoint Server

Create claims-based web applications in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-26
