---
title: "Use Visio Services with SharePoint lists - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-use-visio-services-with-sharepoint-lists
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/use-visio-services-with-sharepoint-lists
family: administration
documentKind: "how-to"
abstract: "You can connect a Visio diagram to the data in a SharePoint list and maintain that connection when you publish the diagram to SharePoint Server."
---

# Use Visio Services with SharePoint lists - SharePoint Server

Note

Use Visio Services with SharePoint lists

# Use Visio Services with SharePoint lists

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can connect a Visio diagram to the data in a SharePoint list and maintain that connection when you publish the diagram to SharePoint Server 2013 or SharePoint Server 2016.

To connect to the SharePoint list from Visio, you must have at least Read access to the SharePoint list. Likewise, once the diagram has been published to a SharePoint document library, viewers must have Read access to the list in order to refresh the data from the list.

Note

This scenario requires you to have Visio Services deployed. For information about how to deploy Visio Services, see Plan for Visio Services in SharePoint Server.

Publishing a diagram connected to a SharePoint list

## Publishing a diagram connected to a SharePoint list

Publishing a data-connected diagram that is connected to a SharePoint list consists of two steps:

Create the diagram in Visio and connect shapes in the diagram to the data in the SharePoint list

Publish the diagram to a SharePoint document library

**To connect a Visio diagram to a SharePoint list**

In Visio, open the diagram that you want to connect to the SharePoint list, or create a new diagram.

On the **Data** tab, click **Link Data to Shapes**.

On the Data selector page, select the **Microsoft SharePoint Foundation list** option, and then click **Next**.

On the Select a site page, in the **Site** box, type the URL for the SharePoint site where the SharePoint list is located, and then click **Next**.

On the Select a list page, in the **Lists** list, select the list to which you want to connect, and then click **Next**.

Click **Finish**.

Once you have connected to the SharePoint list, you can drag the data rows onto the page to link data to your existing shapes, or add new shapes. When you have completed the diagram, you can save it to a SharePoint document library and render it with Visio Services.

**To publish a diagram to a SharePoint document library**

In Visio, click **File**.

Click **Save**, and then browse to a SharePoint document library.

Type a file name, and then click **Save**.

Once the diagram has been saved to the SharePoint document library, you can view the diagram by clicking it directly or by configuring it to appear in a Visio Web Access Web Part. The diagram remains connected to the data in the SharePoint list, and the data refreshes based on the refresh settings that you have configured for Visio Services and for the Visio Web Access Web Part, if applicable.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
