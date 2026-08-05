---
title: "Configure server-to-server authentication between publishing and consuming farms - SharePoint Server"
description: "Learn how to configure server-to-server authentication when you share User Profile service application across SharePoint Server publishing and consuming farms."
ms.topic: how-to
---
Note

Configure Server-to-Server authentication between publishing and consuming farms

# Configure Server-to-Server authentication between publishing and consuming farms

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When a farm consumes the User Profile service application of a publishing farm, SharePoint issues requests using Server-to-Server authentication on behalf of the user for some features:

Follow a document on a content web application when a user's personal site is located on a web application in an external farm. The content web application makes a OAuth request to the My Sites web application on behalf of the user.

Create or reply to a site feed post for a site that is located on a content web application but performed through the user's My Site Newsfeed on the My Sites web application. The My Sites web application will make a request of the content web application on behalf of the user to write the post or the reply.

A User Profile service application task to repopulate the feed cache has to read from the personal site or content site. If the User Profile Service application is running in a different farm, it sends a OAuth request to the My Sites web application or content web application to read the user or site feed data into the cache.

Before you begin

## Before you begin

The procedure in this article requires that you already configured the following:

- Shared the User Profile service application between a consuming and a publishing farm as documented in Share service applications across farms in SharePoint Server.

- Configured the Subscription Settings and App Management service applications on both publishing and consuming farms as documented in section "Configure the Subscription Settings and App Management service applications" of this article

Verify that you have the following memberships:

- **Securityadmin** fixed server role on the SQL Server instance.

- **db_owner** fixed database role on all databases that are to be updated.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Configure server-to-server authentication between publishing and consuming farms

## Configure server-to-server authentication between publishing and consuming farms

The following procedure describes how to configure server-to-server authentication between publishing and consuming farms, and grant just the necessary permissions to allow social features to work. Each farm keeps its own, unique authentication realm.

Authorize consuming farm to send OAuth requests to the farm hosting the MySites web application

### Authorize consuming farm to send OAuth requests to the farm hosting the MySites web application

In a SharePoint server in the **farm running the MySites web application** (which might not be the publishing farm), start the SharePoint Management Shell and run this PowerShell script to register the consuming farm as a trusted issuer, get its app principal and grant it the required authorizations:

```
# Register the consuming farm as a trusted issuer using information in its metadata file
$trustedIssuer = New-SPTrustedSecurityTokenIssuer -MetadataEndpoint "https://<ConsumingFarmWinClaimsWebApp>/_layouts/15/metadata/json/1" -Name "<ConsumingFarmFriendlyName>"

# Get the app principal and set required authorizations
$mySiteHost = Get-SPWeb "http://<MySiteHostUrl/"
$appPrincipal = Get-SPAppPrincipal -Site $mySiteHost -NameIdentifier $trustedIssuer.NameId

# Grant permissions AppOnly and Write on the MySite host
Set-SPAppPrincipalPermission -EnableAppOnlyPolicy -Site $mySiteHost -AppPrincipal $appPrincipal -Scope SiteSubscription -Right Write

# Grant permissions Manage on the PrivateAPI and Read on the SocialPermissionProvider
$privateAPITypeId = New-Object -TypeName System.Guid ("a2ccc2e2-1703-4bd9-955f-77b2550d6f0d")
$socialPermissionProviderId = New-Object -TypeName System.Guid ("fcaec196-a98c-4f8f-b60f-e1a82272a6d2")
$mgr = New-Object -TypeName Microsoft.SharePoint.SPAppPrincipalPermissionsManager ($mySiteHost)
$mgr.AddSiteSubscriptionPermission($appPrincipal, $privateAPITypeId, [Microsoft.SharePoint.SPAppPrincipalPermissionKind]::Manage)
$mgr.AddSiteSubscriptionPermission($appPrincipal, $socialPermissionProviderId, [Microsoft.SharePoint.SPAppPrincipalPermissionKind]::Read)
```

Authorize publishing farm to send OAuth requests to the consuming farm

### Authorize publishing farm to send OAuth requests to the consuming farm

In a SharePoint server in the **consuming farm**, start the SharePoint Management Shell and run this PowerShell script to register the publishing farm as a trusted issuer, get its app principal and grant it the required authorizations:

```
# Register the publishing farm as a trusted issuer using information in its metadata file
$trustedIssuer = New-SPTrustedSecurityTokenIssuer -MetadataEndpoint "https://<PublishingFarmWinClaimsWebApp>/_layouts/15/metadata/json/1" -Name "<PublishingFarmFriendlyName>"

# Get the app principal
$centralAdminWeb = Get-SPWeb "http://<ConsumingFarmCentralAdminURL/"
$appPrincipal = Get-SPAppPrincipal -Site $centralAdminWeb -NameIdentifier $trustedIssuer.NameId

# Grant app only permission and Read on the SiteSubscription
Set-SPAppPrincipalPermission -EnableAppOnlyPolicy -AppPrincipal $appPrincipal -Site $centralAdminWeb -Scope SiteSubscription -Right Read

# Grant permissions Manage on the PrivateAPI
$privateAPITypeId = New-Object -TypeName System.Guid ("a2ccc2e2-1703-4bd9-955f-77b2550d6f0d")
$mgr = New-Object -TypeName Microsoft.SharePoint.SPAppPrincipalPermissionsManager ($centralAdminWeb)
$mgr.AddSiteSubscriptionPermission($appPrincipal, $privateAPITypeId, [Microsoft.SharePoint.SPAppPrincipalPermissionKind]::Manage)
```

See also

## See also

Concepts

### Concepts

Share service applications across farms in SharePoint Server

Authentication overview for SharePoint Server

Plan for server-to-server authentication in SharePoint Server

Other Resources

### Other Resources

New-SPTrustedSecurityTokenIssuer

Set-SPAppPrincipalPermission

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
