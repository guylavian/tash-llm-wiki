---
title: "Data authentication for Excel Services in SharePoint Server 2013 - SharePoint Server"
description: "Summary Learn how Excel Services in SharePoint Server supports connections with SQL Server Analysis Services (SSAS), SQL Server databases, and OLE DB and ODBC data sources."
ms.topic: article
---
Note

Data authentication for Excel Services in SharePoint Server 2013

# Data authentication for Excel Services in SharePoint Server 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Retrieving data from a data source requires a user to be authenticated by the data source and then authorized to access the data that is contained therein. In the case of a workbook, Excel Services authenticates to the data source on behalf of the user who is viewing it in order to refresh the data to which the workbook is connected.

Which authentication method Excel Services can use to retrieve data depends on the type of the underlying data source, as outlined in the following table. For data sources that support more than one authentication method, data connections must specify which one to use.

**Data sources and authentication methods for Excel Services**

| **Data source** | **Authentication method** |
| --- | --- |
| Analysis Services | Windows authentication (integrated security)  
  using Constrained Kerberos Delegation  
  using Secure Store  
  using the Unattended Service Account  
  using the EffectiveUserName connection string property |
| SQL Server | One of:  
  Windows authentication (integrated security)  
  using Constrained Kerberos Delegation  
  using Secure Store  
  using the Unattended Service Account  
  SQL Server Authentication |
| Custom data providers | Varies per data source, typically a user-name and password pair stored in the connection string. |

Custom data providers can also be used.

The following data sources are supported in Excel but not in Excel Services:

Access databases

Web content

XML data

Microsoft Azure Marketplace

Text files

Connecting to external data with Excel Services

## Connecting to external data with Excel Services

Excel Services can connect to various external data sources, including SQL Server, Analysis Services, and custom OLE DB/ODBC data providers. To connect to the data source, Excel Services uses a specific data provider for each data source.

As a security measure, Excel Services must explicitly trust data providers before they can be used. Trusted data providers can be configured as part of the Excel Services service application settings in the SharePoint Central Administration website.

Connecting to a SQL Server data source can be done by using either:

Windows authentication

SQL Server Authentication

Connecting to an Analysis Services data source is done by using Windows authentication.

Other data sources use a connection string usually consisting of a user name and password.

Data connections for Excel Services workbooks

### Data connections for Excel Services workbooks

Excel Services workbooks use one of two kinds of connections:

Embedded connections

Linked connections

Embedded connections are stored as part of the Excel Services workbook. Linked connections are stored externally to a workbook in Office Data Connection (ODC) files. To use a linked connection, a workbook must reference an .odc file that is also stored in the same farm as the workbook, in a trusted data connection library. Each data connection consists of:

A connection string

A query string

An authentication method

Optionally, some metadata required to retrieve external data

Each kind of connection has its advantages and drawbacks discussed here. Choose the one that best suits your scenario.

**Comparison of data connections for Excel Services**

| **Connection type** | **Embedded connections** | **ODC files** |
| --- | --- | --- |
| Advantages | All connection information is stored in the workbook.  
  Embedded connections require little administrative overhead to support.  
  Embedded connections are easy to create. | Linked connections can be centrally stored, managed, audited, shared and access to them controlled by using a data connection library.  
  Workbook authors can use existing connections without having to create queries and connection strings.  
  If the data connection details for a data source change, an administrator only need update one ODC file. With that change, all workbooks that refer to the ODC file will use the updated connection information when the next refresh occurs. (An example of this scenario is when the database server is moved or the database name is changed.) |
| Drawbacks | If the data connection details for a data source change, all workbooks with embedded connections to that data source will have to be republished with updated connection info.  
  Embedded data connections are more difficult to audit by SharePoint admins. | Linked connections may require the help of a SharePoint admin to share, manage and secure.  
  Linked connections are saved in clear text and may contain database passwords. Extra care must be taken to help secure these files. |

Choose a linked data connection, by using an ODC file, for scenarios in which you must have a data connection to an enterprise-scale data source such as SQL Server or Analysis Services. Linked data connections are most useful in scenarios in which they will be shared across many users and in which administrator control of the connection is important.

Note

ODC files must first be created in Excel and exported to SharePoint Server 2013 before it can be used with Excel Services.

Choose an embedded connection for scenarios where you need a data connection that will not be widely used.

ODC files must be stored in a trusted data connection library. Centralizing data connections in such a document library has several advantages:

Administrators can restrict write access to a data connection library to trusted data connection authors to ensure that only well tested and secure data connections are used by workbook authors.

Administrators have a single location to manage data connections for a large group of users.

Administrators can easily approve, audit, revert and manage data connection files by using document library versioning and workflow features.

Data connection libraries can be reused across other Office applications such as Visio, Visio Services, InfoPath 2016, InfoPath Forms Services, and Word.

Workbook authors only have a single location to find workbook data connections, reducing confusion and user training.

For information about how to create data connection libraries, see How to: Create and Use a Data Connection Library (https://go.microsoft.com/fwlink/p/?LinkID=188117). For information about how to create ODC files, see Create, edit, and manage connections to external data (https://go.microsoft.com/fwlink/p/?LinkID=196894).

Windows authentication

### Windows authentication

Windows authentication requires that Excel Services present to the data source a set of Windows credentials. This kind of credential is common on Windows networks and is the same credential used to log on to computers on a Windows domain or to connect to a computer that is running Exchange. Windows credentials are considered the most secure and manageable means of controlling access to SQL Server databases. However, one obstacle to using Windows authentication with Excel Services is the Windows double hop security measure, wherein a user's credentials cannot be passed across more than one computer in a Windows network. Given that Excel Services is a multi-tiered system, special authentication methods are required for Excel Services to retrieve data on behalf of the end-user.

The authentication method to choose depends on various factors as outlined in the following table. Choose the one that best suits your scenario.

**Comparison of authentication methods**

| Authentication method | Kerberos delegation | Secure Store | Unattended Service Account | Effective User Name |
| --- | --- | --- | --- | --- |
| **Description** | Using constrained Kerberos delegation, the workbook viewer's Windows credentials are sent to the data source directly. | Using the Secure Store Service, the viewer's Windows credentials are mapped to another set of credentials specified in a Secure Store target application. | Using the Secure Store Service, all viewers are mapped to a unique set of credentials called the Unattended Service Account that is stored in a specific Secure Store target application specified in Excel Services Global Settings. | Using the EffectiveUserName Global Setting, the user's domain user name is passed to Analysis Services data sources. |
| **Data connection credentials** | The Windows credentials of the workbook viewer. | The credentials specified in the Secure Store target application. | The credentials of the Unattended Service Account. | The credentials of the Excel Services process identity. |
| **Advantages** | The Kerberos protocol is an industry standard in credentials management.  
  Kerberos ties into the existing Active Directory infrastructure.  
  Kerberos delegation permits auditing of individual accesses to a data source.  
  Given that the workbook viewer's identity is known, workbook creators can embed personalized database queries into workbooks. | The Secure Store Service is part of SharePoint Server and is easier to configure than Kerberos.  
  Mappings are flexible: a user can be mapped either 1-to-1 or many-to-1.  
  Non-Windows credentials can be used to connect to data sources that do not accept Windows credentials. (Requires the Unattended Service Account to be configured also.)  
  Mappings created for Excel Services can be re-used by other business intelligence applications such as Visio Services. | The Unattended Service Account is easy to deploy and setup.  
  The Unattended Service Account does not require much administrative overhead. | Per-user data security without the need to configure Kerberos delegation.  
  Minimal configuration and administrative overhead. |
| **Drawbacks** | Additional administrative effort required to configure SharePoint Server 2013 and Excel Services. | Establishing and managing mapping tables requires some administrative overhead.  
  Secure Store permits limited auditing. In the many-to-1 scenario, individual incoming users are mapped into the same credentials through a target application, effectively blending them into one user. | Given that everyone is mapped to the same credentials, an administrator cannot distinguish who accessed a data source. | Only works with Analysis Services data sources. |
| **For the authentication operation to succeed ...** | Kerberos delegation must be set up on the SharePoint Server 2013. | The Secure Store Service must be provisioned and configured on the farm. It must also contain appropriate mapping information for a particular incoming user. Additionally the mapping information may need to be updated periodically to reflect password changes on the mapped account. | The Secure Store Service must be provisioned and configured on the farm. It must also contain the credentials for the Unattended Service Account. Additionally the mapping information may need to be updated periodically to reflect password changes on the mapped account.  
  Excel Services Global Settings must be configured to use the Unattended Service Account. | The **EffectiveUserName** option must be enabled in Excel Services Global Settings.  
  The user must be a member of the appropriate Analysis Services role. |

Kerberos delegation

#### Kerberos delegation

Choose Kerberos delegation for secure and fast authentication to enterprise-scale relational data sources that support Windows authentication. For information about configuring Kerberos delegation, see:

Configuring Kerberos Authentication for Microsoft SharePoint 2010 Products (https://go.microsoft.com/fwlink/p/?LinkId=196600)

Configure Kerberos authentication (SharePoint Server 2010)

Secure Store

#### Secure Store

Choose Secure Store for authentication to enterprise-scale relational data sources that may or may not support Windows Authentication. Secure Store is also useful in scenarios in which you want to control user credential mappings.

For information about using Secure Store with Excel Services, see Use Excel Services with Secure Store Service in SharePoint Server 2016.

Unattended service account

#### Unattended service account

For ease of configuration Excel Services provides a special configuration where an administrator can create a unique mapping where all users are mapped into to a single set of credentials.

This account, known as the unattended service account, must be a low-privilege Windows domain account. Excel Services impersonates this account when it connects to a data source on behalf of a workbook viewer.

It is a best practice to give this account as few network permissions as possible, typically only access to log into the network and access to the data source you want to have users connect to. For best security, be sure that the unattended service account does not have access to the SharePoint Configuration and Content databases.

The unattended service account is used by Excel Services in these scenarios:

When an ODC file specifies the use of the Unattended Service

When an embedded data connection specifies the Unattended Service Account

When using SQL credentials that are stored in a Secure Store target application

Note

The unattended service account can be a local computer account of type Windows. If the unattended service account is configured as a local computer account, ensure that the configuration is identical on every application server running Excel Services. For manageability reasons, the best practice is to use a domain account

Choose the unattended service account when you are connecting to small ad-hoc deployments in which security is less important or for which speed of deployment is essential.

For information about using the unattended service account with Excel Services, see Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2016.

SQL Server Authentication

### SQL Server Authentication

SQL Server Authentication requires that Excel Services present a SQL Server user name and password to a SQL Server data source to authenticate. Excel Services passes the connection string to the data source. The connection string must contain the user name and password.

If the user name and password are stored in a Secure Store target application (recommended for best security), then Excel Services will impersonate the unattended service account and when the connection is made, the SQL credentials are set as properties of the connection.

Authentication against OLEDB/ODBC data sources

### Authentication against OLEDB/ODBC data sources

Authentication to third party data sources typically requires that Excel Services present a user name and password to a data source.

If the user name and password are stored in the workbook or in the ODC file, then Excel Services impersonates a Windows identity dependent on which option has been selected for **Excel Services authentication settings**, either in the workbook or in the ODC file.

If the user name and password are stored in a Secure Store target application (recommended for best security), then Excel Services impersonates the unattended service account and when the connection is made, the SQL credentials are set as properties of the connection.

Data refresh

## Data refresh

Excel Services supports refreshing workbooks connected to one or more of the following data sources:

SQL Server

SQL Server Analysis Services (SSAS)

Note

If the data source that you plan to connect to is not in the list above, you can add support for it by creating a Custom Data Provider. This technology enables you to wrap your existing data sources into one that Excel Services can consume.

External data refresh is the result of the following set of steps through Excel Services.

**Creating a workbook:** A workbook author uploads a data-connected workbook to SharePoint Server 2013.

**Triggering Refresh:** The workbook viewer triggers refresh on a data-connected workbook.

**Data Connections:** Excel Services retrieves data connection information for each external data source in the workbook.

**Trusted Data Providers:** Excel Services checks to see if there is a trusted data provider it can use to retrieve data.

**Authentication:** Excel Services authenticates into the data source and retrieves the requested data on behalf of the workbook viewer.

**Workbook Refresh:** Excel Services updates the workbook based on the data source data and returns it to the viewer.

Refresh can be triggered in one of following ways from within the browser:

The end-user opens the workbook (if the workbook is configured to refresh on open).

The end-user clicks on the refresh button on an already open workbook.

If there are no previously cached versions of this workbook, any of these actions will trigger a refresh and update the workbook.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
