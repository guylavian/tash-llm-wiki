---
title: "View all site collections in SharePoint Server - SharePoint Server"
description: "How to see the list of site collections in SharePoint Server."
ms.topic: how-to
---
Note

View all site collections in SharePoint Server

# View all site collections in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

A site collection is a group of websites that have the same owner and share administrative settings, for example, permissions, and quotas. Site collections are created within a web application. When you create a site collection, a top-level site is automatically created in the site collection. You can then create one or more subsites below the top-level site. The entire structure of the top-level site and all its subsites is called a site collection.

Learn about Managing sites in the new SharePoint admin center in Microsoft 365.

View the site collections in a web application

## View the site collections in a web application

Use the following procedures to view all the site collections in a web application.

To view all site collections by using Central Administration

### To view all site collections by using Central Administration

Refer to the following table in step 3.

| Item | Description |
| --- | --- |
| URL | The URL of the site collection. |
| Title | The current title for site collection. |
| Description | The current description for the site collection. |
| Primary administrator | The primary administrator for the site collection. |
| Email address | The email address for the primary administrator. |
| Database name | The content database that is used by the site collection. |

Verify that you have the following administrative credentials:

To view all site collections, you must be a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.

Open Central Administration. On the **Application Management** page, in the **Site Collections** section, click **View all site collections**.

The **Site Collection List** page lists all the site collections in the web application.

To display more information about a site collection, in the **URL** column, click the site collection.

The table just before this procedure appears on the right side of the page.

If you want to change the selected web application, click the **Web Application** box, and then click **Change Web Application**. Use the **Select Web Application** page to select another web application.

To view all site collections by using Microsoft PowerShell

### To view all site collections by using Microsoft PowerShell

Verify that you meet the following minimum requirements: See Add-SPShellAdmin.

Open **SharePoint Management Shell**.

At the PowerShell command prompt, type the following command, and then press ENTER:

```
Get-SPWebApplication | Get-SPSite -Limit All | Format-Table -Property URL,ContentDatabase
```

Note

This command displays the URLs of all the web applications in a server farm and the site collections in each web application.

For more information, see Get-SPWebApplication and Get-SPSite.

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Other Resources

#### Other Resources

SharePoint planning guide

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
