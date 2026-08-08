---
title: "Configure a reverse proxy device for SharePoint Server hybrid - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-configure-a-reverse-proxy-device-for-sharepoint-server-hybrid
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/configure-a-reverse-proxy-device-for-sharepoint-server-hybrid
family: hybrid
documentKind: "how-to"
abstract: "Learn about supported reverse proxy devices for SharePoint Server hybrid deployments."
---

# Configure a reverse proxy device for SharePoint Server hybrid - SharePoint Server

Note

Configure a reverse proxy device for SharePoint Server hybrid

# Configure a reverse proxy device for SharePoint Server hybrid

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

This article is part of a **roadmap** of procedures for configuring SharePoint hybrid solutions. Be sure you're following a roadmap when you do the procedures in this article.

This topic provides an overview of the role of reverse proxy devices in a SharePoint Server hybrid deployment and links to device-specific configuration guidance.

The role of a reverse proxy in a SharePoint Server hybrid deployment

## The role of a reverse proxy in a SharePoint Server hybrid deployment

SharePoint Server and SharePoint in Microsoft 365 can be configured in a hybrid configuration to securely combine search results and external data from Microsoft Business Connectivity Services. Reverse proxy devices play a role in the secure configuration of a hybrid SharePoint Server deployment when inbound traffic from SharePoint in Microsoft 365 needs to be relayed to your on-premises SharePoint Server farm. For example, if a federated user uses a SharePoint in Microsoft 365 search portal that is configured to return hybrid search results, a reverse proxy device intercepts and pre-authenticates the request for on-premises SharePoint Server content and then relays it to SharePoint Server. The reverse proxy device in a hybrid topology provides a secure endpoint for inbound traffic using SSL encryption and client certificate authentication.

How inbound connectivity works

### How inbound connectivity works

The following diagrams show how a reverse proxy device is used for inbound connectivity.

With an inbound search solution, only the SharePoint in Microsoft 365 site has search results from both locations.

**Inbound connectivity**

In the example below, a federated user on the Internet uses the SharePoint in Microsoft 365 search portal to search for content in both SharePoint in Microsoft 365 and her company's on-premises SharePoint server.

**A federated user on the Internet searches for content that's located on her company's on-premises server.**

The following list describes the steps shown in the preceding picture.

From the Internet, a federated user browses to her SharePoint in Microsoft 365 site.

SharePoint in Microsoft 365 queries the search index in SharePoint in Microsoft 365, and also sends the search query to the external URL of the on-premises SharePoint farm which resolves to the external endpoint of the reverse proxy device.

The reverse proxy device pre-authenticates the request using the Secure Channel SSL certificate and relays the request to the URL of the primary web application.

The SharePoint farm service account queries the on-premises search index and security trims the search results in the context of the user who sent the search request.

Security trimmed search results are returned to SharePoint in Microsoft 365 and appear on the search results page. This result set includes search results from the SharePoint in Microsoft 365 search index and search results from the search index of the SharePoint Server farm.

Note

Inbound connectivity enables access to content and resources in your on-premises SharePoint Server farm **from the internet** only if the user has an active, secure connection to the intranet network over VPN or DirectAccess or if the SharePoint Server farm is configured in an extranet topology.

For a more detailed description of this process, that shows how certificates are used and authentication and authorization work in this topology, see Poster: SharePoint 2013 Hybrid Topology: Certificate, Authentication, and Authorization flow.

General reverse proxy requirements

## General reverse proxy requirements

In a hybrid SharePoint Server scenario, the reverse proxy must be able to:

Support client certificate authentication with a wildcard or SAN SSL certificate.

Support pass-through authentication for OAuth 2.0, including unlimited OAuth bearer token transactions.

Accept unsolicited inbound traffic on **TCP port 443** (HTTPS).

Tip

No ports other than TCP 443 need to be opened on the external reverse proxy endpoint to support hybrid connectivity.

Bind a wildcard or SAN SSL certificate to a published endpoint.

Relay traffic to an on-premises SharePoint Server farm or load balancer without rewriting any packet headers.

Supported reverse proxy devices

## Supported reverse proxy devices

The table below lists the currently supported reverse proxy devices for SharePoint Server hybrid deployments. This list will be updated as new devices are tested for supportability. Follow the steps in the configuration article for the reverse proxy device that you want to use. When you've completed configuring the reverse proxy device, return to your roadmap.

| **Supported reverse proxy devices** | **Configuration article** | **Additional information** |
| --- | --- | --- |
| Azure Application Proxy | Enable remote access to SharePoint in Microsoft 365 with Microsoft Entra application proxy | Azure Application Proxy is an Azure service that allows remote access to services within your network without opening firewall ports from the Internet to your service. |
| Windows Server 2012 R2 with Web Application Proxy (WA-P) | Configure Web Application Proxy for a hybrid environment | Web Application Proxy (WA-P) is a Remote Access service in Windows Server 2012 R2 that publishes web applications that users can interact with from many devices.  
 > [!IMPORTANT]> To use Web Application Proxy as a reverse proxy device in a hybrid SharePoint Server environment, you must also deploy AD FS in Windows Server 2012 R2. |
| Forefront Threat Management Gateway (TMG) 2010 | Configure Forefront TMG for a hybrid environment | Forefront TMG 2010 is a comprehensive, secure, web gateway solution that provides secure reverse proxy functionality.  
 > [!NOTE]> Forefront TMG 2010 is no longer sold by Microsoft but was supported through 4/14/2020. For more information, see Microsoft Support Lifecycle information for TMG 2010. |
| F5 BIG-IP | Enabling SharePoint 2013 Hybrid Search with the BIG-IP | External content managed by F5 Networks. |
| Citrix NetScaler | Citrix NetScaler and Microsoft SharePoint 2013 Hybrid Deployment Guide | External content managed by Citrix. |

See also

## See also

Concepts

#### Concepts

Hybrid for SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-31
