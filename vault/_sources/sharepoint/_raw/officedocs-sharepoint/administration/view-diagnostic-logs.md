---
title: "View diagnostic logs in SharePoint Server - SharePoint Server"
description: "Learn to view and filter log events by using Microsoft PowerShell, and view and export diagnostic logs by using the Out-GridView cmdlet."
ms.topic: how-to
---
Note

View diagnostic logs in SharePoint Server

# View diagnostic logs in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can troubleshoot problems in the farm by using data from the Unified Logging Service (ULS) logs in SharePoint Server . The ULS logs can collect data at varying levels depending on the logging settings. Use PowerShell to filter the data, display it in various ways, and output the data to a data grid with which you can filter, sort, group, and export data to Excel 2016.

View and filter log events by using PowerShell

## View and filter log events by using PowerShell

You can use PowerShell to view and filter log events. You cannot view or filter log events by using the SharePoint Central Administration website.

**To view and filter log events by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Go to the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

- **All trace events**:

```
Get-SPLogEvent
```

- **By level**:

```
Get-SPLogEvent | Where-Object {$_.Level -eq "Information" }
```

- **By area**:

```
Get-SPLogEvent | Where-Object {$_.Area -eq <Area>}
```

Where  *<Area>* is the value of the **Area** property.

- **By category**:

```
Get-SPLogEvent | Where-Object {$_.Category -eq <Category>
```

Where  *<Category>* is the value of the **Category** property.

- **By event ID**:

```
Get-SPLogEvent | Where-Object {$_.EventID -eq <EventID>}
```

Where  *<EventID>* is the value of the **EventID** property.

- **By message text**:

```
Get-SPLogEvent | Where-Object {$_.Message -like "<string>"}
```

Where  *<string>* is the string found in the event message.

- **By process**:

```
Get-SPLogEvent | Where-Object {$_.Process -like "<Process>"}
```

Where  *<Process>* is the value of the **Process** property.

By default, the command retrieves data from the default ULS log folder. To view and filter trace events that are on shared folder on a network, use the **Directory** parameter of the **Get-SPLogEvent** cmdlet.

To view more details about each trace event, use the **Format-List** cmdlet at the end of the command. For example,

```
Get-SPLogEvent | Where-Object {$_.Area -eq "SharePoint Foundation"} | Format-List
```

For more information, see Get-SPLogEvent.

View and export diagnostic logs by using the PowerShell Out-GridView cmdlet

## View and export diagnostic logs by using the PowerShell Out-GridView cmdlet

PowerShell provides a powerful and easy-to-use feature that displays tabular data resulting from PowerShell commands in a filterable, searchable data grid in a separate window. You can use this grid to view log events and to perform the following operations on the data:

Sort the data by any column.

View the data in groups.

Filter the data by Level, Area, Category, Message, Event ID, or Timestamp.

Search the data for any string.

Export raw or sorted or filtered data to a spreadsheet.

Note

The **Out-GridView** cmdlet cannot be used with cmdlets that use the **Format** verb. The **Out-GridView** cmdlet receives objects whereas the cmdlets that use the **Format** verb return only formatted text. > You can view a subset of the data by using the **Where-Object** cmdlet that filters and passes the results to the **Out-GridView** cmdlet. For example,  `Get-SPLogEvent | Where-Object {$_.Area -eq "SharePoint Foundation"} | Out-GridView`. > If the grid is displaying more than several hundred rows, it might run slowly, especially if performing complex filtering operations. For faster performance, export the data to Excel 2016.

**To view and filter diagnostic logs by using Windows PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Go to the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Get-SPLogEvent | Out-GridView
```

To sort columns, click the column header.

To search for a specific string, type the string in the **Filter** box. Search is performed over all columns and rows. To clear the search, click **X**.

To filter data on only one criterion, type the following in the **Search** box: <property name>:<value>. For example, to search for all log entries raised by SharePoint Foundation 2013, type the following: Area:SharePoint Foundation. To clear the filter, click **X**.

To filter data by using more than one criterion or by using criteria with "contains, begins with, ends with" or other methods:

Click **Add criteria** button.

Click the check box for the properties that you want to filter on, and then click **Add**.

Click **contains** to change to a different filter method. The methods that are available are **contains**, **does not contain**, **starts with**, **equals**, **does not equal**, **ends with**, **is empty**, and **is not empty**.

Type a value in the text box.

Repeat steps "c" and "d" for each property that you selected in step "b".

When all the filtering criteria are specified, the data that satisfies the criteria will appear.

To clear a specific filter, click the **X** button.

To clear all the filters, collapse the query view and then click the **Clear All** button.

**To export grid data to a spreadsheet**

Select the rows that you want to export. You can select multiple rows by using SHIFT+DRAG to select a block of rows, CTRL+CLICK to select specific rows, or CTRL+A to select all rows.

You can also filter and sort the results before you copy the data into a spreadsheet. When you sort or filter data, only the resulting viewable data is copied over.

Copy the selected rows by using CTRL+C.

Open the spreadsheet workbook page, and then paste the copied rows into it by using CTRL+V.

For more information, see Out-GridView and Out-GridView Revisited.

Additional resources

## Additional resources

- Last updated on 
		2023-10-18
