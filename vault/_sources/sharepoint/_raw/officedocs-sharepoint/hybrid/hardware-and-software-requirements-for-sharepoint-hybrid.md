---
title: "Hardware and software requirements for SharePoint hybrid - SharePoint Server"
description: "Learn what prerequisites you need to configure hybrid for SharePoint Server."
ms.topic: article
---
Note

Hardware and software requirements for SharePoint hybrid

# Hardware and software requirements for SharePoint hybrid

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article describes the prerequisites that are required to deploy a SharePoint hybrid solution between SharePoint Server and SharePoint in Microsoft 365 for enterprises.

Hardware and software requirements

## Hardware and software requirements

An operational, on-premises Active Directory Directory Services (AD DS) domain.

An operational SharePoint Server farm. Services must be running on the local farm - farms with federated services aren't supported. For more information about setting up a farm, see Install SharePoint Server.

A properly configured Microsoft 365 organization that is provisioned with SharePoint in Microsoft 365 with one of the following subscription plans: E1 supports Display hybrid federated search results in SharePoint Server only, E3, or E4.

Certificate requirements

## Certificate requirements

The default STS certificate in the SharePoint farm is used by the Hybrid Configuration Wizard to establish the token signing trust when configuring hybrid workloads. Using the inbuilt STS certificate is the recommended approach when configuring hybrid workloads. If however, you intend to use a publicly signed certificate instead of the inbuilt STS one then you must replace the inbuilt certificate with your own following the provided guidance.

For more information, see Replace the STS certificate.

Inbound connectivity requirements

## Inbound connectivity requirements

The following hybrid solutions require inbound connectivity from Microsoft 365 to SharePoint Server:

Inbound hybrid search (displaying search results from SharePoint Server in Microsoft 365)

Hybrid Business Connectivity Services

Hybrid Duet Enterprise Online for Microsoft SharePoint in Microsoft 365 and SAP

For each of these hybrid solutions, the requirements in the following sections apply.

Additional hardware requirements

### Additional hardware requirements

Inbound connectivity requires the following:

A reverse proxy device. The reverse proxy device provides a secure endpoint for inbound traffic using SSL encryption and client certificate authentication.

An Internet domain (such as https://adventureworks.com) and the permission to create or edit DNS records for that domain.

Note

This public domain must be registered by using a domain registrar, such as GoDaddy.com, and must be the same domain that the URL of the external endpoint of the reverse proxy device is associated with.

Certificate requirements

### Certificate requirements

This section describes the certificates you need to configure an inbound connectivity from Microsoft 365 to SharePoint Server.

About the Secure Channel SSL certificate

#### About the Secure Channel SSL certificate

This certificate provides authentication and encryption between the reverse proxy device and Microsoft 365. It must be either a wildcard or a SAN certificate and be issued by a public root certification authority. For more info, see About Secure Channel SSL certificates and Get a Secure Channel SSL certificate.

About the on-premises SharePoint SSL certificate

#### About the on-premises SharePoint SSL certificate

If you configure your primary web application to use SSL (which is the web application on the on-premises SharePoint farm that's configured for hybrid), you have to bind an SSL certificate to the primary web application.

If this web application already exists and is configured for SSL, you're ready to go. Otherwise you have to either obtain or create one for this purpose. For production environments, this certificate should be issued by a public certification authority (CA). For test and development environments, it can be a self-signed certificate.

For more info, see Plan SSL certificates.

Supported reverse proxy devices

#### Supported reverse proxy devices

The following table lists the currently supported reverse proxy devices for SharePoint Server hybrid deployments. This list will be updated as new devices are tested for supportability.

| **Supported reverse proxy devices** | **Configuration article** | **More information** |
| --- | --- | --- |
| Windows Server 2012 R2 with Web Application Proxy (WA-P) | Configure Web Application Proxy for a hybrid environment | Web Application Proxy (WA-P) is a Remote Access service in Windows Server 2012 R2 that publishes web applications that users can interact with from many devices.  
 > [!IMPORTANT]> To use Web Application Proxy as a reverse proxy device in a hybrid SharePoint Server environment, you must also deploy AD FS in Windows Server 2012 R2. Earlier versions of Windows don't support Web Application Proxy |
| Forefront Threat Management Gateway (TMG) 2010 | Configure Forefront TMG for a hybrid environment | Forefront TMG 2010 is a comprehensive, secure, web gateway solution that provides secure reverse proxy functionality.  
 Forefront TMG 2010 is no longer sold by Microsoft but will be supported through 4/14/2020. For more information, see Microsoft Support Lifecycle information for Forefront TMG 2010. |
| F5 BIG-IP | Enabling SharePoint 2013 Hybrid Search with the BIG-IP | This is external content that's managed by F5 Networks. |

General reverse proxy requirements

#### General reverse proxy requirements

In a hybrid SharePoint Server scenario, the reverse proxy must be able to:

Support client certificate authentication with a wildcard or SAN SSL certificate.

Support pass-through authentication for OAuth 2.0, including unlimited OAuth bearer token transactions.

Accept unsolicited inbound traffic on **TCP port 443** (HTTPS).

Tip

No ports other than TCP 443 have to be opened on the external reverse proxy endpoint to support hybrid connectivity.

Bind a wildcard or SAN SSL certificate to a published endpoint.

Relay traffic to an on-premises SharePoint Server farm or load balancer without rewriting any packet headers.

For an overview of reverse proxy devices in a SharePoint hybrid topology, see Configure a reverse proxy device for SharePoint Server hybrid.

Additional resources

## Additional resources

- Last updated on 
		2024-12-02
