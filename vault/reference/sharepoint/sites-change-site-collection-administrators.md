---
title: "Change site collection administrators in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: sites-change-site-collection-administrators
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/sites/change-site-collection-administrators
family: sites
documentKind: "how-to"
abstract: "How to change site collection administrators for SharePoint Server site collections by using the SharePoint Central Administration website or Microsoft PowerShell."
---

# Change site collection administrators in SharePoint Server - SharePoint Server

Note

Change site collection administrators in SharePoint Server

# Change site collection administrators in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

A site collection administrator in SharePoint Server can configure the appearance and behavior of the site, configure search settings and site directory settings, and allocate storage space. A site collection must have one primary site collection administrator and can have one secondary site collection administrator. The primary and secondary site collection administrators receive administrative email alerts for the site collection. The primary and secondary site collection administrators are automatically added to the SharePoint Site Collection Administrators group. You can add as many additional accounts as you want to the SharePoint Site Collection administrators group, but only the primary and secondary site collection administrators will receive administrative alerts for the site collection. All members of the SharePoint Site Collection Administrators group have full administrative permissions to the site collection.

Learn about Managing site admins for SharePoint in Microsoft 365.

Change the primary or secondary site collection administrator

## Change the primary or secondary site collection administrator

Use this procedure when you want to make a user a primary or secondary site collection administrator for a specific site collection.

Caution

A site collection can have only one primary site collection administrator and one secondary site collection administrator. The steps in this procedure describe how to change either of them. Any user who is removed as a site collection administrator is removed from the site collection administrators group for the site collection.

To change the primary or secondary site collection administrator by using Central Administration

### To change the primary or secondary site collection administrator by using Central Administration

Verify that you have the following administrative credentials:

- To add a site collection administrator, you must be a member of the Farm Administrators group on the computer that is running Central Administration.

In Central Administration, click **Application Management**. On the **Application Management** page, in the **Site Collections** section, click **Change site collection administrators**.

On the **Site Collection Administrators** page, click the arrow next to the site collection name, and then select **Change Site Collection** if the site collection you want is not already selected.

If the site collection to which you want to add an administrator is listed, select the URL of the site collection, and then click **OK**. If the site collection is not listed, click the arrow next to the web application name, click **Change Web Application**, select the name of the web application that contains the site collection, select the URL of the site collection, and then click **OK**.

In the **Primary site collection administrator** or **Secondary site collection administrator** area, either type the name of the user whom you want to add by using the format  *<domain>*\ *<username>* or select the user by using the address book.

Click **OK**.

To add a primary or secondary site collection administrator by using Microsoft PowerShell

### To add a primary or secondary site collection administrator by using Microsoft PowerShell

Verify that you meet the following minimum requirements: See Add-SPShellAdmin.

Open the SharePoint Management Shell.

At the PowerShell command prompt, type the following command to replace the secondary site collection administrator:

```
Set-SPSite -Identity "<SiteCollection>" -SecondaryOwnerAlias "<User>"
```

Where:

*<SiteCollection>* is the URL of the site collection to which you want to add a site collection administrator.

*<User>* is name of the user whom you want to add in the format  *<domain>*\ *<username>*.

The previous procedure shows a common way to use the **Set-SPSite** cmdlet to add a secondary site collection administrator. You can specify different parameters to configure different settings for a site collection. For more information, see Set-SPSite.

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Remove a site collection administrator

## Remove a site collection administrator

Use this procedure to specify the user to be removed from the site collection administrator list. This procedure does not remove the user from Active Directory Domain Services (AD DS).

To remove a site collection administrator by using Central Administration

### To remove a site collection administrator by using Central Administration

Verify that you have the following administrative credentials:

- To remove a site collection administrator, you must be a member of the Farm Administrators group on the computer that is running Central Administration.

In Central Administration, select **Application Management**. On the **Application Management** page, in the **Site Collections** section, click **Change site collection administrators**.

On the **Site Collection Administrators** page, click the arrow next to the site collection name, and then click **Change Site Collection**.

If the site collection from which you want to remove an administrator is listed, select the URL of the site collection, and then click **OK**. If the site collection is not listed, click the arrow next to the web application name, click **Change Web Application**, select the name of the web application that contains the site collection, select the URL of the site collection, and then click **OK**.

Every site collection must have a primary site collection administrator. If you want to remove the primary site collection administrator, you must replace it with a different primary site collection administrator. To do so, select the current administrator's name, press the Delete key, and then either type the name of the replacement site collection administrator by using the format  *<domain>*\ *<username>* or select a replacement site collection administrator by using the address book.

To remove the secondary site collection administrator, select the administrator's name, and then press the **Delete** key.

Click **OK**.

See also

## See also

Concepts

#### Concepts

Create a site collection in SharePoint Server

Other Resources

#### Other Resources

Manage administrators for a site collection

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
