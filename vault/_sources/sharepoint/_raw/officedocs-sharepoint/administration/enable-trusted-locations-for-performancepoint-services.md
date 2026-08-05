---
title: "Enable trusted locations for PerformancePoint Services - SharePoint Server"
description: "Learn how to limit PerformancePoint Services features that use trusted locations by allowing only designated sites, lists or document libraries rather than the entire site collection."
ms.topic: how-to
---
Note

Enable trusted locations for PerformancePoint Services

# Enable trusted locations for PerformancePoint Services

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

After you enable a feature on a site collection in SharePoint Server, the content types or PerformancePoint Services objects are made available for others to use on any site within that site collection. An administrator may want to limit PerformancePoint Services features that use trusted locations by allowing one or more sites, lists, or document libraries rather than an entire site collection. In this way the administrator can limit use of PerformancePoint Services to specific locations in the farm to prevent unauthorized access to data sources. See To add a trusted data source location.

Note

PerformancePoint Services has been removed from SharePoint Server Subscription Edition. We recommend to explore Microsoft Power BI as an alternative to PerformancePoint Services.

Establish trusted locations for data sources and dashboard content

## Establish trusted locations for data sources and dashboard content

You can specify locations in SharePoint Server where dashboard content and data sources are secured. The default is to trust all locations, but administrators can specify other trusted locations.

**PerformancePoint Content List:** A PerformancePoint Content List stores the elements that are used to construct a dashboard. A PerformancePoint Services dashboard is a related group of interactive scorecards, filters, and report views organized into a set of Web pages.

**PerformancePoint Data Source Library:** A PerformancePoint Data Source Library contains data-source definitions that identify a source of business data. It may include cubes or perspectives based on online analytical processing (OLAP) cubes, relational databases, CSV files, and Microsoft Excel Services worksheets.

**Trusted Data Sources and Trusted Content Locations:** When you navigate to either Trusted Data Sources or Trusted Content Locations pages from the Manage PerformancePoint Services page, there are two option buttons. When the **Only specific locations** option button is selected, the list of trusted locations is enabled. For data source or content locations, if there are no items in the list, only the toolbar button is enabled. When one or more items are listed, the **Edit** and **Delete** buttons are enabled.

The URL you type is checked for a valid site collection, site, document library, and list. Option buttons are enabled or disabled depending on the type of site. Validation depends on whether your URL is a valid site and/or already exists.

Caution

The default for a trusted data source and trusted content locations is to trust all.

**To add a trusted data source location**

On the SharePoint Central Administration website, select **Manage Service Applications**.

On the Manage Service Applications page, select the PerformancePoint Services service application you want to manage.

On the **Service Application** tab, click **Manage**. The Manage PerformancePoint Services page opens.

Click **Trusted Data Source Locations**. The Trusted Data Source Locations page opens.

Select one of the following options and click **Apply**.

**All SharePoint locations:** Specifies that data sources are trusted from all SharePoint Server locations.

**Only specific locations:** Specifies that data sources are only trusted when found in the locations listed.

If you select **Only specific locations** and click **Apply**, **Add Trusted Data Source Location** appears; otherwise **All SharePoint locations** is the current setting.

Click **Add Trusted Data Source Location** to specify the URL and location for this trusted location.

Enter the full Web address (it must be a site collection, site, or document library for this trusted location).

Select the location type, type a description (optional), and then click **OK**. The location type appears under **Location**.

**To add a trusted content location**

In Central Administration select **Manage Service Applications**.

In the Manage Service Applications page, select the PerformancePoint Services service application you want to manage.

On the **Service Application** tab, click **Manage**. The Manage PerformancePoint Services page opens.

Click **Trusted Content Locations**. The Trusted Content Locations page opens.

Select one of the following options, and then click **Apply**.

**All SharePoint locations:** Specifies that content is trusted from all SharePoint Server locations.

**Only specific locations:** Specifies that content is only trusted when found in the locations listed.

If you select **Only specific locations** and click **Apply**, **Add Trusted Content Location** appears; otherwise **All SharePoint locations** is the current setting.

Click **Add Trusted Content Location** to specify the URL and location for this trusted location.

Enter the full Web address (it must be a site collection, site, or list address for this trusted location.)

Select the location type, type a description (optional), and then click **OK**. The location type appears under **Location**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
