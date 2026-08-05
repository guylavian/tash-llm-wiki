---
title: "Update a web application URL and IIS bindings for SharePoint Server Subscription Edition - SharePoint Server"
description: "Learn how to change a web application binding for SharePoint Server."
ms.topic: article
---
Note

Update a web application URL and IIS bindings for SharePoint Server Subscription Edition

# Update a web application URL and IIS bindings for SharePoint Server Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In SharePoint Server Subscription Edition, you can now easily change the IIS bindings of a SharePoint web application through PowerShell or Central Administration.

Note

This functionality is available only to those users who are a member of the local Administrator's group on the server.

This article provides detailed guidance for changing the IIS bindings of a web application.

Editing the web application bindings through Central Administration

## Editing the web application bindings through Central Administration

To edit the web application and set the port, URL, SSL certificate host header, do the following:

Navigate to **SharePoint Central Administration** > **Application Management** > **Manage web applications**.

Select a web application and click **Edit**.

In the **Edit a Web Application Zone** dialog box, click the zone that contains the IIS binding you want to update.

In the **IIS Web site** section, you can change the **Port** and **Host Header** settings.

In the **Security Configuration** section, you can change the **Use Secure Sockets Layer (SSL)**, **Server Certificate**, **Use Server Name Indication**, and **Allow Legacy Encryption** settings.

In the **Public URL** section, you can change the public URL for this zone.

Click **Save** to save the changes.

Editing the web application bindings through PowerShell

## Editing the web application bindings through PowerShell

To change the IIS bindings of a web application through PowerShell, use the `Set-SPWebApplication` cmdlet. This functionality is supported in all web application zones.

For example, you can run the following PowerShell command to change a SharePoint web application on HTTP port 80 to instead use a host header binding on SSL port 443:

```
Set-SPWebApplication -Identity http://servername -Zone Default -Port 443 -SecureSocketsLayer -HostHeader sharepoint.contoso.com -Url https://sharepoint.contoso.com 
```

Additional resources

## Additional resources

- Last updated on 
		2023-04-27
