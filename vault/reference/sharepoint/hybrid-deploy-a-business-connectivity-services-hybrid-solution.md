---
title: "Deploy a Business Connectivity Services hybrid solution in SharePoint - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-deploy-a-business-connectivity-services-hybrid-solution
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/deploy-a-business-connectivity-services-hybrid-solution
family: hybrid
documentKind: "install-set-up-deploy"
abstract: "Learn how to configure the Business Connectivity Services (BCS) hybrid scenario to access on-premises data through SharePoint in Microsoft 365."
---

# Deploy a Business Connectivity Services hybrid solution in SharePoint - SharePoint Server

Note

Deploy a Business Connectivity Services hybrid solution in SharePoint in Microsoft 365

# Deploy a Business Connectivity Services hybrid solution in SharePoint in Microsoft 365

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Note

Business Connectivity Services (BCS) has retired in Microsoft 365. Its features are no longer available and can't be enabled. This applies to all environments including Government Clouds and Department of Defense. For more information, see BCS retirement in Microsoft 365.

**This article is part of a roadmap of procedures for configuring SharePoint hybrid solutions. Be sure you're following a roadmap when you do the procedures in this article. **

The Microsoft Business Connectivity Services (BCS) hybrid deployment scenario allows you to securely publish on-premises data to an external list or app for SharePoint in Microsoft 365. From there, users can view and edit the data, depending on the permissions that they have.

In this scenario, you will learn how to:

Configure your on-premises environment so that you can securely publish confidential business data to your SharePoint in Microsoft 365 tenancy.

Create and configure an OData service endpoint and an external content type with Visual Studio 2012.

Prepare your SharePoint in Microsoft 365 tenancy to host an app for SharePoint in Microsoft 365 or an external list, which makes the external data available to your extranet users.

Create a connection settings object that tells Business Connectivity Services in SharePoint in Microsoft 365 how to connect to the on-premises OData service endpoint.

Deploy an app for SharePoint in Microsoft 365 or external list to SharePoint in Microsoft 365.

Validate and troubleshoot the BCS hybrid scenario.

What these procedures help you deploy

## What these procedures help you deploy

BCS is a centralized infrastructure in SharePoint Server, Office 2016, and SharePoint in Microsoft 365 that enables you to integrate data that is not in SharePoint in Microsoft 365 products or Office 2016 into SharePoint Server. BCS implementations take many forms. This includes this hybrid form that uses SharePoint in Microsoft 365 and SharePoint Server on-premises. These procedures show how to install and configure BCS to integrate data from an on-premises OData service endpoint into SharePoint in Microsoft 365. For this scenario, we use the AdventureWorks sample SQL database and create an OData service head for the database. The solution looks as shown in the following diagram.

**Figure: Hybrid BCS solution**

An information worker signs in to SharePoint in Microsoft 365 by using their federated account and opens an app for SharePoint in Microsoft 365 or external list that needs data from an on-premises OData data source.

The external list creates a request for the data and sends it to Business Connectivity Services. Business Connectivity Services looks at the connection settings object to see how to connect to the data source and which credentials to use.

Business Connectivity Services retrieves two sets of credentials:

The Secure Channel certificate from Secure Store in SharePoint in Microsoft 365. This is used for SharePoint in Microsoft 365 authentication to the reverse proxy.

An OAuth token from the Microsoft Entra service. This is used for user authentication to the SharePoint Server farm. You gain access to the Microsoft Entra service with your SharePoint in Microsoft 365 subscription. It is a security token service that manages security tokens for users of SharePoint in Microsoft 365.

Business Connectivity Services sends an HTTPS request to the published endpoint for the data source. The request includes the client certificate from Secure Store, the OAuth token, and a request for the data. The reverse proxy authenticates the request by using the client certificate and forwards it to the on-premises SharePoint Server farm. For more info about publishing SharePoint in Microsoft 365 to the internet, see SharePoint in Microsoft 365 publishing solution guide in the Forefront Technical Library.

The on-premises farm retrieves the user's cloud identity from the OAuth token (for example, user123@contoso.com), and through the Client Side Object Model (CSOM) code, maps it to the on-premises identity (for example, contoso\user123). The on-premises credentials are mapped to credentials that have access to the external data via a Secure Store target application.

The on-premises Business Connectivity Services forwards the request to the OData Service endpoint. The OData Service authenticates the request (via IIS) and returns the data, which is passed back through the chain to the external list for the user to work with.

**Video: Watch a demonstration of the BCS hybrid scenario**

How to use these procedures

## How to use these procedures

The steps to completely deploy this scenario are presented in smaller procedures. Each procedure is numbered indicating its position in the overall sequence. At the beginning and end of each procedure, links direct you to the previous and following steps. The following list contains links to all of the procedures, in the required order, for your reference. Be aware that this list includes the steps to deploy an external list and an app for SharePoint in Microsoft 365. You can deploy one or the other or both, depending on your needs. You should skip the steps for whichever configuration you don't want to deploy. You must follow them in sequence to build out the scenario. You can also use these procedures individually for your own unique scenarios. When you assemble individual procedures to build out your own scenarios, it is important that you test the complete set of procedures, in order, in a lab setting before you try them in production.

Roadmap of the procedures

## Roadmap of the procedures

To configure the BCS hybrid solution:

To configure the underlying settings and services needed, follow the procedures in Prepare your environment for the Business Connectivity Services hybrid scenario.

If you want to use an external list, follow the procedures in Deploy the Business Connectivity Services hybrid scenario as an external list.

To validate your setup, follow the procedures in Validate the Business Connectivity Services hybrid scenario.

See also

## See also

Concepts

#### Concepts

Hybrid for SharePoint Server

Plan SharePoint Server hybrid

Install and configure SharePoint Server hybrid

Other Resources

#### Other Resources

Introducing OData: Data Access for the Web, the cloud, mobile devices, and more

Additional resources

## Additional resources

- Last updated on 
		2025-02-24
