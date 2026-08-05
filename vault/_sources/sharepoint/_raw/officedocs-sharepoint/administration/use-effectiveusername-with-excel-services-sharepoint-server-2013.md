---
title: "Use EffectiveUserName with Excel Services (SharePoint Server 2013) - SharePoint Server"
description: "Use the Analysis Services EffectiveUserName feature to refresh data-connected workbooks in Excel Services in SharePoint Server 2013 using the workbook viewer's Windows identity."
ms.topic: how-to
---
Note

Use EffectiveUserName with Excel Services (SharePoint Server 2013)

# Use EffectiveUserName with Excel Services (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

This scenario applies only to Excel Services with an Analysis Services data source on SharePoint Server 2013 Enterprise.

Scenario overview

## Scenario overview

Using the EffectiveUserName feature with Excel Services allows the identity of a user viewing a report to be passed to SQL Server Analysis Services. This allows you to specify the appropriate level of data access for a given user on the OLAP cube itself.

Using the EffectiveUserName option allows passing the user's identity to SQL Server Analysis Services without the need to configure Secure Store or Kerberos delegation.

Before you begin

## Before you begin

Before starting, read the following information about permissions and software requirements.

This scenario assumes that you have Excel Services configured on your farm and an Excel Services trusted file location where you can save your report. For information about configuring Excel Services, see Overview of Excel Services in SharePoint Server 2013 and Configure Excel Services in SharePoint Server 2013 Preview. For information about configuring a trusted file location, see Manage Excel Services trusted file locations (SharePoint Server 2013).

This scenario requires that you have Farm Administrator access to the SharePoint Server 2013 farm and administrator access to SQL Server Analysis Services.

Configure Excel Services Global Settings

## Configure Excel Services Global Settings

The first step in configuring the EffectiveUserName feature is to enable the feature in Excel Services global settings. Use the following procedure to enable the EffectiveUserName feature.

**To enable EffectiveUserName in Excel Services**

In Central Administration, under **Application Management**, click **Manage service applications**.

Click the Excel Services service application.

Click **Global Settings**.

On the Excel Services Application Settings page, in the **External Data** section, select the **Use the EffectiveUserName property** check box.

Click **OK**.

Configure Analysis Services access

## Configure Analysis Services access

Using the EffectiveUserName feature requires that the account that is running the Excel Services application pool be an Analysis Services administrator.

If you do not know what account is running the Excel Services application pool in your farm, use the following procedure to determine the account. If you know the account, skip this procedure.

**To determine the Excel Services application pool account**

On the SharePoint Central Administration Web site home page, click **Security**.

On the Security page, under **General Security**, click **Configure service accounts**.

On the Service Account page, in the **Credential Management** section, from the drop-down list, select the application pool that runs Excel Services Application.

When this option is selected, the name of the Excel Services service application appears in the box underneath the drop-down list. The account shown in the **Select an account for this component** dropdown list is the Windows identity that you need to add as an Analysis Services administrator.

Click **Cancel**.

You must add the Excel Services application pool account as an Analysis Services administrator. Use the following procedure to add this account as an administrator in Analysis Services.

**To add an Analysis Services administrator**

In SQL Server Management Studio, connect to Analysis Services.

Right click the Analysis Services top node, and then click **Properties**.

On the **Security** page, click **Add**.

Type the name of the account that runs the Excel Services application pool, and then click **OK**.

Click **OK**.

Configure OLAP cube access

## Configure OLAP cube access

You must grant access to the OLAP cube for the users who will be creating or viewing Excel Services reports. To do this, you must create a role in the OLAP cube. (You can use an existing role if you have created one previously.)

Within the role, you can grant access to users or Active Directory groups. We recommend using Active Directory groups for easier administration.

Analysis Services provides a variety of access options for a given role. You can create multiple roles if you have different groups of users who need different levels of access to the cube.

Use the following procedure to create a role and assign permissions to users.

Note

This procedure describes how to grant read access to a cube. You can adjust the permissions for the role as needed for your users.

**To create a role**

In SQL Server Management Studio, connect to Analysis Services.

Expand **Databases** and expand the database where you want to create the role.

Right-click **Roles** and click **New Role**.

On the General page, type a name for the role.

On the Membership page, add the users or Active Directory group containing the users to whom you want to grant cube access.

On the Cubes page, select **Read** from the **Access** dropdown list for the cubes that you want to grant access to.

Click **OK**.

Once granted read permissions to the OLAP cube, users will be able to connect to the cube in Excel to create reports and will also be able to refresh the data in Excel Services.

Note

Once granted access to an OLAP cube, users can also connect to the cube directly in SQL Server Management Studio. The access that they are granted to the cube determines what actions they can perform in Management Studio.

Create and publish a report

## Create and publish a report

Once a user has been granted access to the cube, they can connect to it in Excel. Use the following procedure to connect to the cube.

**To connect to an OLAP data source**

In Excel, on the **Data** tab, in the **Get External Data** section, click **From Other Sources**, and then click **From Analysis Services**.

In the **Server name** text box, type the name of the instance of Analysis Services that you want to connect to, and then click **Next**.

Select the cube that you want to connect to, and then click **Next**.

Click **Finish**.

In order for the EffectiveUserName feature to be used in a published report, the Excel Services authentication settings must be configured to use Windows authentication. Use the following procedure to configure the Excel Services authentication settings for your data source.

**To configure Excel Services authentication settings**

In Excel, on the **Data** tab, in the **Connections** section, click **Connections**.

Select the connection to your Analysis Services cube, and then click **Properties**.

On the **Definition** tab, click **Authentication Settings**.

On the **Excel Services Authentication Settings** dialog, select the **Use the authenticated user's account** (Excel 2016) or **Windows Authentication** (Excel 2010) option, and then click **OK**.

Click **OK** and then click **Close**.

When you have finished creating your report, the next step is to save it to a SharePoint Server 2013 document library that has been configured as a trusted file location in Excel Services. Use the following procedure to save your workbook.

Note

This procedure uses Excel 2016. In Excel 2010, use **File**, **Save & Send** to publish the workbook to SharePoint Server 2013.

**To publish the report to SharePoint Server**

In Excel, on the **File** tab, click **Save**.

Click **Computer**, and then click **Browse**.

Type the URL of the SharePoint document library where you want to save the file.

Type a file name, and then click **Save**.

Once the workbook has been saved to SharePoint Server 2013, you can render it using Excel Services and the data will refresh based on the refresh settings configured in the Excel Services trusted file location settings.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
