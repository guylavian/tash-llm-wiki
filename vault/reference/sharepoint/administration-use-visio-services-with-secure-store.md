---
title: "Use Visio Services with Secure Store Service in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-use-visio-services-with-secure-store
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/use-visio-services-with-secure-store
family: administration
documentKind: "how-to"
abstract: "Secure Store can be used to store encrypted credentials for use in refreshing data-connected Visio diagrams in Visio Services."
---

# Use Visio Services with Secure Store Service in SharePoint Server - SharePoint Server

Note

Use Visio Services with Secure Store Service in SharePoint Server

# Use Visio Services with Secure Store Service in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Visio Services can be configured to use the Secure Store Service to provide user authentication for data-connected diagrams that use an external data source such as SQL Server.

Note

This article assumes that you have already deployed a Secure Store Service service application. If you have not deployed Secure Store, see Plan the Secure Store Service in SharePoint Server and Configure the Secure Store Service in SharePoint Server.

Secure Store provides a method of mapping users who do not have direct data access to an account that does have data access. Secure Store and Visio Services work together in the following basic sequence of events:

A user accesses a data-connected diagram on a SharePoint site.

Visio Services passes the user's identity to Secure Store.

Secure Store determines whether the user is authorized to access the data. If so, Secure Store returns the data access credentials to Visio Services.

Visio Services impersonates the data access credentials, accesses the data, and displays the data to the user.

Visio Services provides three methods of using Secure Store to provide data access:

**Unattended Service Account**: The unattended service account is an account that is used by Visio Services to provide broad database access to all users in the farm. Use the unattended service account for accessing data that is not considered sensitive or where you do not want to restrict access to a certain group of users. For information about how to configure this scenario, see Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account.

**External Data Connections**: You can specify a Secure Store target application in an Office Data Connection (ODC) file and then connect to that ODC file in Visio. When you publish the diagram to a SharePoint document library, it maintains its connection to the ODC file. The connection information in the ODC file is used when Visio Services refreshes the data in the workbook. Using an ODC file has the following advantages:

A single ODC file can be referenced by multiple diagrams. If the data source connection parameters change (for example, if you want to use a different Secure Store target application than the one originally specified) you need only update the ODC file and not the diagrams themselves.

Using ODC files allows administrators to create and maintain the data connections used by the organization. You can create data connections appropriate for users, place them in a trusted data connection library, and then notify the users of which ODC files to use for their queries.

For information about how to configure this scenario, see Configure Visio Services data refresh in SharePoint Server by using external data connections.

Visio, which is used to create the diagrams, does not use Secure Store for data authentication. You must configure direct data access for diagram authors. Once the diagram has been published to a SharePoint site, Visio Services can use Secure Store when it renders the diagram.

See also

## See also

Concepts

#### Concepts

Secure Store for Business Intelligence service applications

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
