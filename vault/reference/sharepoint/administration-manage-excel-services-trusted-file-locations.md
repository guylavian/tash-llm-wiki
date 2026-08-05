---
title: "Manage Excel Services trusted file locations (SharePoint Server 2013) - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-manage-excel-services-trusted-file-locations
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/manage-excel-services-trusted-file-locations
family: administration
documentKind: "how-to"
abstract: "Add, configure, or delete an Excel Services trusted file location in SharePoint Server 2013."
---

# Manage Excel Services trusted file locations (SharePoint Server 2013) - SharePoint Server

Note

Manage Excel Services trusted file locations (SharePoint Server 2013)

# Manage Excel Services trusted file locations (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365.

A trusted file location is a SharePoint Server 2013 location, network file share, or Web folder address that the administrator has explicitly enabled workbooks to be loaded from. Excel Services only loads workbooks from trusted file locations.

Use the procedures in this article to configure trusted file locations for Excel Services.

To perform these procedures, you must be member of the Farm Administrators group or an Administrator for the Excel Services service application that you are configuring.

Important

The steps in this article apply to SharePoint Server 2013 Enterprise.

Add a trusted file location

## Add a trusted file location

Use the following procedure to add a trusted file location in Excel Services.

**To add a trusted file location**

On the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.

On the Manage service applications page, click the Excel Services service application that you want to configure.

On the Manage Excel Services Application page, click **Trusted File Locations**.

On the Excel Services Application Trusted File Locations page, click **Add Trusted File Location**.

Configure the settings for the trusted file location as described in Configure a trusted file location, below.

Configure a trusted file location

## Configure a trusted file location

Use the following procedure to configure a trusted file location.

**To configure a trusted file location**

On the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.

On the Manage service applications page, click the Excel Services service application that you want to configure.

On the Manage Excel Services Application page, click **Trusted File Locations**.

In the **Address** column, click the trusted file location that you want to configure.

Configure the settings as described in the following table:

| **Option** | **Description** |
| --- | --- |
| Address | The location of the Excel documents that you want Excel Services to trust. |
| Location Type | If the document library is stored in the SharePoint Server 2013 content database, select **Microsoft SharePoint Foundation**. If the document library is stored in a network file share, select **UNC**. If the document library is stored in a Web folder address, select **HTTP**. |
| Trust Children | Select **Children trusted** if you want to trust all child libraries or directories. |
| Description | Text description of the file location you specified. |
| Session Timeout | Value in seconds that an Excel Calculation Services session can stay open and inactive before it is shut down, as measured from the end of each open request. The default is 450 seconds. |
| Short Session Timeout | Value in seconds that an Excel Services session stays open and inactive, before any user interaction, before it is shut down. This is measured from the end of the original open request. The default is 450 seconds. |
| New Workbook Session Timeout | Value in seconds that an Excel Calculation Services session for a new workbook stays open and inactive before it is shut down, as measured from the end of each request. The default value is 1,800 seconds (30 minutes). |
| Maximum Request Duration | Value in seconds for the maximum duration of a single request in a session. The default is 300 seconds. |
| Maximum Chart Render Duration | Value in seconds for the maximum time that is spent rendering any single chart. The default is 3 seconds. |
| Maximum Workbook Size | Value in megabytes (MB) for the maximum size of workbooks that Excel Calculation Services can open. The default size is 10 megabytes. |
| Maximum Chart or Image Size | Value in megabytes (MB) for the maximum size of charts or images that Excel Calculation Services can open. The default size is 1 megabyte. |
| Volatile Function Cache Lifetime | Value in seconds that a computed value for a volatile function is cached for automatic recalculations. The default is 300 seconds. |
| Workbook Calculation Mode | Select **File** to perform calculations as specified in the file.  
 Select **Manual** if you want recalculation to occur only when a Calculate request is received.  
 Select **Automatic** if you want any change to a value to cause the recalculation of all other values that depend on that value. Also, volatile functions are called if their time-out has expired.  
 Select **Automatic except data tables** if you want any change to a value to cause the recalculations of all other values dependent on that value (the values cannot be in a data table.) Also, volatile functions are called if their time-out has expired. |
| Allow External Data | Select **None** to disable all external data connections for the trusted file location.  
 Select **Trusted data connection libraries only** to only enable using connections to data sources that are stored in a trusted data connection library. The server will ignore settings embedded in the worksheet.  
 Select **Trusted data connection libraries and embedded** to enable connections that are embedded in the workbook file or connections that are stored in a trusted data connection library. If you do not have to have tight control or restrictions on the data connections that are used by workbooks on the server, consider selecting this option. |
| Warn on Refresh | Select the **Refresh warning enabled** check box to display a warning before refreshing external data for files in this location. When you select this option, you make sure that external data is not automatically refreshed without user interaction. |
| Display Granular External Data Errors | Select the **Granular External Data Errors** check box to display specific error messages when external data failures occur for files in this location. Displaying specific error messages can help troubleshoot data connectivity issues if they occur. |
| Stop When Refresh on Open Fails | Select the **Stopping open enabled** check box to prevent users from viewing files that are configured to refresh on open, if the refresh fails. This prevents users from seeing cached information in the workbook. This option is only effective if the user does not have Open Item permissions on the workbook. (A user with Open Item permissions on the workbook can open the workbook in Excel and thus has access to any cached information.) |
| External Cache Lifetime (Automatic Refresh) | In the **Automatic refresh (periodic / on-open)** box, type a value in seconds for the maximum time that the system can use external data query results for automatically refreshed external query results. The default is 300 seconds. |
| External Cache Lifetime (Manual Refresh) | In the **Manual refresh** box, type a value in seconds for the maximum time that the system can use external data query results for manually refreshed external query results. To prevent data refresh after the first query, type -1. The default is 300 seconds. |
| Maximum Concurrent Queries Per Session | Type a value for the maximum number of queries that can run at the same time during a single session. The default is 5 queries. |
| Allow External Data Using REST | Select the **Data refresh from REST enabled** check box to all requests from the REST API to refresh external data connections. Note that this setting has no effect if Allow External Data is set to **None**. Note too, that this setting has no effect if Warn on Refresh is enabled. |
| Allow User-Defined Functions | Select **User-defined functions allowed** if you want to allow user-defined functions in Excel Calculation Services for workbooks from this location. |

- Click **OK**.

Delete a trusted file location

## Delete a trusted file location

Use the following procedure to delete a trusted file location.

Note

Deleting a trusted file location does not affect the file location itself or its contents. It only removes the location from the Excel Services trusted location list, and Excel Services no longer loads workbooks from that location.

**To delete a trusted file location**

On the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.

On the Manage service applications page, click the Excel Services service application that you want to configure.

On the Manage Excel Services Application page, click **Trusted File Locations**.

On the Excel Services Application Trusted File Locations page, point to the trusted file location that you want to delete, click the arrow that appears, and then click **Delete**.

Click **OK** in the message box that asks whether you want to continue with the deletion.

See also

## See also

Other Resources

#### Other Resources

Configure Excel Services in SharePoint

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
