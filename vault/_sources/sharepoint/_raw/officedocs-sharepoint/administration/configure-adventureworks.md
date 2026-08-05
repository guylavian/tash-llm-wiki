---
title: "Configure AdventureWorks for Business Intelligence solutions - SharePoint Server"
description: "Configure the AdventureWorks sample data for use with Excel, Excel Services in SharePoint Server 2013, and PerformancePoint Services business intelligence scenarios."
ms.topic: how-to
---
Note

Configure AdventureWorks for Business Intelligence solutions

# Configure AdventureWorks for Business Intelligence solutions

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The AdventureWorks sample data set provides a sample database, data warehouse, and OLAP cube. The subsequent articles in this section make use of this sample data to demonstrate Business Intelligence capabilities in Excel, Excel Services in SharePoint Server 2013, and PerformancePoint Services. This article describes how to install and configure the AdventureWorks sample data set and configure a Business Intelligence Center on your SharePoint Server 2013 farm.

Important

This scenario applies only to SharePoint Server 2013 Enterprise.

Scenario overview

## Scenario overview

Installing the AdventureWorks sample data set consists of downloading the sample data, attaching the sample databases in SQL Server Management Studio, and deploying the sample OLAP cube using the SQL Server Data Tools.

Creating a Business Intelligence Center consists of creating a new site collection with the Business Intelligence Center template using the SharePoint Central Administration website.

The procedures for completing both of these tasks, plus procedures for configuring the required user access and permissions are included in this article.

Before you begin

## Before you begin

Before starting, read the following information about permissions and software requirements:

To deploy the AdventureWorks sample data, you must be a SQL Server and Analysis Services administrator.

To create a Business Intelligence Center, you must be a farm administrator on the SharePoint Server 2013 farm.

The subsequent articles make use of Excel Services and PerformancePoint Services. It is assumed that these are configured on your farm. For information about deploying Excel Services, see Overview of Excel Services in SharePoint Server 2013 and Configure Excel Services in SharePoint Server 2013.

When using Excel Services or PerformancePoint Services, user access can be provided using Windows Authentication with Kerberos delegation, the Secure Store Service, or, with OLAP data sources, the EffectiveUserName feature. It is assumed that one or more of these options are configured on your farm. For information about configuring Secure Store, see Plan the Secure Store Service in SharePoint Server and Configure the Secure Store Service in SharePoint Server. For information about configuring the EffectiveUserName feature for OLAP data sources, see Use Analysis Services EffectiveUserName in SharePoint Server.

Video demonstration

## Video demonstration

This video shows the steps involved in installing and configuring the AdventureWorks sample data set, as described in this article.

**Video: Configure AdventureWorks for Business Intelligence solutions**

Install the AdventureWorks sample data

## Install the AdventureWorks sample data

The AdventureWorks sample data consists of:

The AdventureWorks2012 database

The AdventureWorksDW2012 database

The AdventureWorksDW2012Multidimensional-EE OLAP cube

The following sections describe how to deploy each of these data sets.

Deploy the AdventureWorks sample databases

### Deploy the AdventureWorks sample databases

Each of the two AdventureWorks sample databases must be downloaded separately.

Use the following procedure to download and deploy the AdventureWorks2012 database.

**To deploy the AdventureWorks2012 database**

Download AdvetureWorks Database 2012.

Note

Because this file was downloaded from the Internet, it may be blocked by Windows. Right-click the file, and then click **Properties**. Click the **Unblock** button if it is present, and then click **OK**. (If the **Unblock** button is not present, then the file is not blocked.)

Copy AdventureWorks2012_Data.mdf to your default database directory (normally \Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA) or other location as designated by your database administrator.

Open SQL Server Management Studio.

Connect to the database engine.

Right-click **Databases**, and then click **Attach**.

On the **Attach Databases** dialog, click **Add**.

Navigate to the location where you copied AdventureWorks2012_Data.mdf, select the file, and then click **OK**.

Under **"AdventureWorks2012" database details**, select the row where **File Type** is **Log**.

Click **Remove**.

Click **OK**.

Use the following procedure to download and deploy the AdventureWorksDW2012 data warehouse database.

**To deploy the AdventureWorksDW2012 data warehouse**

Download AdvetureWorks Database 2012.

Note

Because this file was downloaded from the Internet, it may be blocked by Windows. Right-click the file, and then click **Properties**. Click the **Unblock** button if it is present, and then click **OK**. (If the **Unblock** button is not present, then the file is not blocked.)

Copy AdventureWorksDW2012_Data.mdf to your default database directory (normally \Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA) or other location as designated by your database administrator.

Open SQL Server Management Studio.

Connect to the database engine.

Right-click **Databases**, and then click **Attach**.

On the **Attach Databases** dialog, click **Add**.

Navigate to the location where you copied AdventureWorksDW2012_Data.mdf, select the file, and then click **OK**.

Under **"AdventureWorksDW2012" database details**, select the row where **File Type** is **Log**.

Click **Remove**.

Click **OK**.

Deploy the AdventureWorks sample OLAP cube

### Deploy the AdventureWorks sample OLAP cube

The following requirements must be met before you can deploy the sample OLAP cube. Procedures are provided to accomplish each of these tasks if they have not already been completed in your environment.

The AdventureWorksDW2012 database must be deployed on the SQL Server database engine as covered in the section above.

The SQL Server Data Tools must be installed as part of your SQL Server and Analysis Services deployment.

Note

SQL Server Data Tools was known as Business Intelligence Developer Studio (BIDS) in previous versions of SQL Server.

The account running the Analysis Services service must have a login on the SQL Server database engine.

If you have not deployed the AdventureWorksDW2012 database, do so now before proceeding with the procedures in this section.

If you have not deployed the SQL Server Data Tools, use the following procedure to deploy them.

Note

You can determine if the SQL Server Data Tools are installed by clicking **Start**, **All Programs**, and then **Microsoft SQL Server 2012** on the computer running SQL Server. If the SQL Server Data Tools are installed, it will appear in the menu under **Microsoft SQL Server 2012**.

**To install the SQL Server Data Tools**

On the SQL Server 2012 DVD, run setup.exe.

In the SQL Server Installation Center, on the left pane, click **Installation**.

In the right pane, click **New SQL Server stand-alone installation or add features to an existing installation**.

On the Setup Support Rules page, click **OK**.

On the Product Updates page click **Next**.

On the Setup Support Rules page, click **Next**.

On the Installation Type page, select the **Add features to an existing instance of SQL Server 2012** option, and select the instance where you want to install the SQL Server Data Tools.

Click **Next**.

On the Feature Selection page, select the **SQL Server Data Tools** check box, and then click **Next**.

On the Installation Rules page, click **Next**.

On the Disk Space Requirements page, click **Next**.

On the Error Reporting page, click **Next**.

On the Installation Configuration Rules page, click **Next**.

On the Ready to Install page, click **Install**.

When the installation completes, click **Close**.

Once the SQL Server Data Tools have been installed, the next step is to create a login for the account running Analysis Services if one does not already exist.

If you do not know what account is running Analysis Services, use the following procedure to determine the account.

**To determine the Analysis Services service account**

On the computer running Analysis Services, click **Start**, click **All Programs**, click **Microsoft SQL Server 2012**, click **Configuration Tools**, and then click **SQL Server Configuration Manager**.

In the left pane, click **SQL Server Services**.

In the right pane, find the instance of Analysis Services that you will be using, and note the account listed in the **Log On As** column. This is the account for which you must add a logon in SQL Server.

If you do not already have a SQL Server login for the account running Analysis Services, use the following procedure to create one.

**To add a login for the Analysis Services service account**

Open SQL Server Management Studio.

Connect to the database engine.

Expand **Security**.

Right-click **Logins** and click **New Login**.

In the **Login name** text box, type the name of the account running the Analysis Services service.

Click **OK**.

Note

This login does not require any Server Roles other than the default role of Public. No User Mapping is necessary.

Once you have configured the login for the Analysis Services service account, the next step is to download and deploy the AdventureWorks OLAP cube. Use the following procedure to download and deploy the cube.

**To configure the AdventureWorks OLAP cube**

Download AdventureWorks Multidimensional Models SQL Server 2012

Note

Because this file was downloaded from the Internet, it may be blocked by Windows. Right-click the file, and then click **Properties**. Click the **Unblock** button if it is present, and then click **OK**. (If the **Unblock** button is not present, then the file is not blocked.)

Unzip the file to a location on the computer running Analysis Services.

In the **Enterprise** folder, double-click AdventureWorksDW2012Multidimensional-EE.sln.

If the **Choose Default Environment Settings** dialog appears, choose the **Business Intelligence Settings** option, and then click **Start Visual Studio**.

In Visual Studio, at the top of the **Solution Explorer** window, right click **AdventureWorksDW2012Multidimensional-EE** and click **Deploy**.

Close Visual Studio without saving changes.

Configure AdventureWorks user access

### Configure AdventureWorks user access

Once the databases and the cube have been deployed, you must grant your users access to them. The following access is required:

Users who will be creating reports or dashboards in the subsequent articles in this section must have **db_datareader** access to the AdventureWorks databases and **Read** access to the AdventureWorks cube.

If you are using the unattended service account with Excel Services or PerformancePoint Services, that account must have **db_datareader** access to the AdventureWorks databases and **Read** access to the AdventureWorks cube.

If you are using Secure Store to refresh data in Excel Services or PerformancePoint Services, the target application credentials must have **db_datareader** access to the AdventureWorks databases and **Read** access to the AdventureWorks cube.

We recommend that you use an Active Directory group containing the users to whom you want to grant access.

Use the following procedure to grant access to the AdventureWorks databases. If you choose to grant access to each user individually instead of using an Active Directory group, you must create a separate login for each user.

**To grant access to the AdventureWorks databases**

In SQL Server Management Studio, connect to the database engine.

Expand **Security**.

Right-click **Logins**, and then click **New Login**.

Click **Search**.

If you are using an Active Directory group, click **Object Types**, select the **Groups** check box, and then click **OK**.

On the **Select User or Group** dialog, type the name of the Active Directory group or user to whom you want to grant database access, and then click **OK**.

Under **Select a page**, click **User Mapping**.

Select the **Map** check box for **AdventureWorks2012**, and then select the **db_datareader** database role membership check box.

Select the **Map** check box for **AdventureWorksDW2012**, and then select the **db_datareader** database role membership check box.

Click **OK**.

Use the following procedure to grant access to the AdventureWorks OLAP cube.

**To grant access to the AdventureWorks OLAP cube**

In SQL Server Management Studio, connect to Analysis Services.

Expand **Databases**, and then expand **AdventureWorksDW2012Multidimensional-EE**.

Note

If the AdventureWorksDW2012Multidimensional-EE database is not present, then right-click **Databases** and click **Refresh**.

Right-click **Roles** and then click **New Role**.

In the **Role name** text box, type a name for the role.

In the **Select a page** pane, click **Membership**.

Click **Add**.

Type the name of the users or Active Directory group to whom you want to grant cube access.

Note

If you will be using Secure Store or an unattended service account to access the cube, include those credentials here.

On the **Select Users or Groups** dialog, click **OK**.

In the **Select a page** pane, click **Cubes**.

In the right pane, in the **Access** column, click select **Read** from the dropdown list for **Adventure Works** and **Mined Customers**.

In the right pane, in the **Local Cube/Drillthrough Access** column, click select **Drillthrough** from the dropdown list for **Adventure Works** and **Mined Customers**.

Click **OK**.

Create a Business Intelligence Center

## Create a Business Intelligence Center

The subsequent articles in this section rely on a Business Intelligence Center site being present. If you have an existing Business Intelligence Center, you can use it. However, we recommend creating a new Business Intelligence Center that is not part of your production environment.

Use the following procedure to create a Business Intelligence Center.

**To create a Business Intelligence Center**

On the SharePoint Central Administration website, under **Application Management**, click **Create site collections**.

On the Create Site Collection page:

Type a title in the **Title** text box.

Type the URL that you want to use in the **URL** text box.

Under **Select a template**, choose the **Enterprise** tab, and then select **Business Intelligence Center**.

In the **Primary Site Collection Administrator** section, type a name for the primary site collection administrator in the **User name** text box.

Optionally, type a name for the secondary site collection administrator.

Optionally, select a quota template.

Click **OK**.

Configure BI Center access

### Configure BI Center access

The following table describes the permissions available in a Business Intelligence Center.

**Business Intelligence Center permissions**

| **Account** | **Permissions** |
| --- | --- |
| Visitors | Read  
 Read permissions enable users to view information in the Business Intelligence Center. |
| Members | Contribute  
 Contribute permissions enable users to view and create items, such as reports, and save them to this site. |
| Designers | Design  
 Design permissions enable users to view, create, and publish items that include dashboards. |
| Owners | Full Control  
 Full Control permissions enable users to view, create, and publish dashboard content, and to view or edit user permissions |

For the scenarios described in the subsequent articles in this section, users will need the following permissions.

Users publishing workbooks to the Business Intelligence Center from Excel require Contribute permissions and must be added to the Members group.

Users publishing dashboards from PerformancePoint Dashboard Designer require Design permissions and must be added to the Designers group.

Users who are only viewing reports or dashboards in the Business Intelligence Center but not publishing only require Read permission and can be added to the Visitors group.

Use the following procedure to configure permissions for the Business Intelligence Center.

**To set permissions in the Business Intelligence Center**

In the Business Intelligence Center, click **Share**.

Type the names of the users or groups to whom you want to grant access.

Click **Show Options**.

On the **Select a group or permission level** dropdown list, select the permission level that you want.

Click **Share**.

Scenarios that use this configuration

## Scenarios that use this configuration

The following scenarios use the AdventureWorks sample data and Business Intelligence Center as configured in this article:

Create an Excel Services dashboard using SQL Server Analysis Services data

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
