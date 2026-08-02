---
title: "Configure alternate access mappings for SharePoint Server - SharePoint Server"
description: "Learn how to configure alternate access mappings in SharePoint Server."
ms.topic: how-to
---
Note

Configure alternate access mappings for SharePoint Server

# Configure alternate access mappings for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Each web application can be associated with a collection of mappings between internal and public URLs. Both internal and public URLs consist of the protocol and domain portions of the full URL (for example, https://www.fabrikam.com). A public URL is what users type to access the SharePoint site, and that URL is what appears in the links on the pages. Internal URLs are in the URL requests that are sent to the SharePoint site. Many internal URLs can be associated with a single public URL in multi-server farms (for example, when a load balancer routes requests to specific IP addresses to various servers in the load-balancing cluster).

Each web application supports five collections of mappings per URL. The five collections correspond to five zones (default, intranet, extranet, Internet, and custom). When the web application receives a request for an internal URL in a particular zone, links on the pages returned to the user have the public URL for that zone. For more information, see Plan alternate access mappings for SharePoint 2013.

Manage alternate access mappings

## Manage alternate access mappings

On the SharePoint Central Administration website, click **System Settings**.

On the **System Settings** page, in the **Farm Management** section, click **Configure alternate access mappings**.

For information about how to perform this procedure using a Microsoft PowerShell cmdlet, see New-SPAlternateUrl.

Add an internal URL

## Add an internal URL

On the **Alternate Access Mappings** page, click **Add Internal URLs**.

If the mapping collection that you want to change is not specified, then choose one. In the **Alternate Access Mapping Collection** section, on the **Alternate Access Mapping Collection** menu, click **Change alternate access mapping collection**.

On the **Select an Alternate Access Mapping Collection** page, click a mapping collection.

In the **Add internal URL** section, in the **URL protocol, host and port** box, type the new internal URL (for example, https://www.fabrikam.com).

In the **Zone** list, click the zone for the internal URL.

Click **Save**.

Edit or delete an internal URL

## Edit or delete an internal URL

Note

You can't delete the last internal URL for the default zone.

On the **Alternate Access Mappings** page, click the internal URL that you want to edit or delete.

In the **Edit internal URL** section, change the URL in the **URL protocol, host and port** box.

In the **Zone** list, click the zone for the internal URL.

Do one of the following:

Click **Save** to save your changes.

Click **Cancel** to discard your changes and return to the **Alternate Access Mappings** page.

- Click **Delete** to delete the internal URL.

For information about how to perform this procedure using a Microsoft PowerShell cmdlet, see Remove-SPAlternateUrl.

Edit public URLs

## Edit public URLs

Note

There must always be a public URL for the default zone.

On the **Alternate Access Mappings** page, click **Edit Public URLs**.

If the mapping collection that you want to change is not specified, then choose one. In the **Alternate Access Mapping Collection** section, on the **Alternate Access Mapping Collection** menu, click **Change alternate access mapping collection**.

On the **Select an Alternate Access Mapping Collection** page, click a mapping collection.

In the **Public URLs** section, you can add new URLs or edit existing URLs in any of the following text boxes:

**Default**

**Intranet**

**Extranet**

**Internet**

**Custom**

- Click **Save**.

Map to an external resource

## Map to an external resource

You can also define mappings for resources outside intranet applications. To do so, you must supply a unique name, initial URL, and a zone for that URL. (The URL must be unique to the farm.)

On the **Alternate Access Mappings** page, click **Map to External Resource**.

On the **Create External Resource Mapping** page, in the **Resource Name** box, type a unique name.

In the **URL protocol, host and port** box, type the initial URL.

Click **Save**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
