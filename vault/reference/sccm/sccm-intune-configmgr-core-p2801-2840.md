---
title: "Core infrastructure documentation — pages 2801-2840"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2801-2840
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2801-2840
family: sccm
documentKind: "doc"
abstract: "registered in the Azure portal: Microsoft Entra tenant Name: The name of your Microsoft Entra tenant. Microsoft Entra tenant ID: The GUID of your Microsoft Entra tenant. Application Name: A friendly name for the app, the display name in the app registration. Client ID: The Appli"
---

# Core infrastructure documentation — pages 2801-2840

<!-- p.2801 -->

registered in the Azure portal:

     Microsoft Entra tenant Name: The name of your Microsoft Entra tenant.
     Microsoft Entra tenant ID: The GUID of your Microsoft Entra tenant.
     Application Name: A friendly name for the app, the display name in the app
     registration.
     Client ID: The Application (client) ID value of the app registration. The format is a
     standard GUID.
     Secret Key: Copy the secret key when you register the app in Microsoft Entra ID
     and create the secret key.
     Secret Key Expiry: Specify the same date as from the Azure portal.
     App ID URI: The value is the Application ID URI of the app registration entry in the
     Microsoft Entra admin center. The format is similar to https://ConfigMgrService .

After entering the information, select Verify. Then select OK to close the Import apps
window.

  ） Important

  When you use an imported Microsoft Entra app, you aren't notified of an upcoming
  expiration date from console notifications.

Import native (client) app
When you select Import from the Client app window, it opens the Import apps window.
Enter the following information about the Microsoft Entra native app that's already
registered in the Azure portal:

     The wizard autopopulates the Microsoft Entra tenant name and tenant ID based on
     the web (server) app that you already specified.
     Application Name: A friendly name for the app.
     Client ID: The Application (client) ID value of the app registration. The format is a
     standard GUID.

After entering the information, select Verify. Then select OK to close the Import apps
window.

Next steps
After you manually register the two apps in the Azure portal, use the process in the
following article to import the apps:

<!-- p.2802 -->

  Configure Microsoft Entra ID for CMG

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2803 -->

Security and privacy for the cloud
management gateway
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article includes security and privacy information for the Configuration Manager
cloud management gateway (CMG). For more information, see Overview of cloud
management gateway.

Security details
The CMG accepts and manages connections from CMG connection points. It uses
mutual authentication using certificates and connection IDs.

The CMG accepts and forwards client requests using the following methods:

      Pre-authenticates connections using mutual HTTPS with the PKI-based client
      authentication certificate or Microsoft Entra ID.

         IIS on the CMG VM instances verifies the certificate path based on the trusted
         root certificates that you upload to the CMG.

         If you enable certificate revocation, IIS on the VM instance also verifies client
         certificate revocation. For more information, see Publish the certificate
         revocation list.

      The certificate trust list (CTL) checks the root of the client authentication certificate.
      It also does the same validation as the management point for the client. For more
      information, see Review entries in the site's certificate trust list.

      Validates and filters client requests (URLs) to check if any CMG connection point
      can service the request.

      Checks content length for each publishing endpoint.

      Uses round-robin behavior to load-balance CMG connection points in the same
      site.

The CMG connection point uses the following methods:

      Builds consistent HTTPS/TCP connections to all VM instances of the CMG. It checks
      and maintains these connections every minute.

<!-- p.2804 -->

     Uses mutual authentication with the CMG using certificates.

     Forwards client requests based on URL mappings.

     Reports connection status to show service health status in the console.

     Reports traffic per endpoint every five minutes.

Configuration Manager rotates the storage account key for the CMG. This process
happens automatically every 180 days.

Security mechanisms and protections
The CMG resources in Azure are part of the Azure platform as a service (PaaS). They're
protected in the same manner and with the same default protections as all other
resources in Azure. It's not supported to change any of the configurations of the CMG
resources or architecture in Azure. These changes include the use of any sort of firewall
in front the CMG to intercept, filter, or otherwise process traffic before it reaches the
CMG. All traffic destined for a CMG is processed through an Azure load balancer. CMG
deployments as a virtual machine scale set are protected by Microsoft Defender for
Cloud.

Service principals and authentication

The service principals are authenticated by the server app registration in Microsoft Entra
ID. This app is also known as the web app. You create this app registration automatically
when you create the CMG, or manually by an Azure administrator in advance. For more
information, see Manually register Microsoft Entra apps for the CMG.

The secret keys for the Azure apps are encrypted and stored in the Configuration
Manager site database. As part of the setup process, the server app has Read Directory
Data permission to the Microsoft Graph API. It also has the contributor role on the
resource group that hosts the CMG. Each time the app needs to access resources like
Microsoft Graph, it gets an access token from Azure, which it uses to access the cloud
resource.

Microsoft Entra ID can automatically rotate the secret key for these apps, or you can do
it manually. When the secret key changes, you need to renew the secret key in
Configuration Manager.

For more information, see Purpose of app registrations.

Configuration Manager client-facing roles

<!-- p.2805 -->

The management point and software update point host endpoints in IIS to service client
requests. The CMG doesn't expose all internal endpoints. Every endpoint published to
the CMG has a URL mapping.

     The external URL is the one the client uses to communicate with the CMG.

     The internal URL is the CMG connection point used to forward requests to the
     internal server.

URL-mapping example
When you enable CMG traffic on a management point, Configuration Manager creates
an internal set of URL mappings for each management point server. For example:
ccm_system, ccm_incoming, and sms_mp. The external URL for the management point
ccm_system endpoint might look like:
https://<CMG service name>/CCM_Proxy_MutualAuth/<MP Role ID>/CCM_System

The URL is unique for each management point. The Configuration Manager client then
puts the CMG-enabled management point name into its internet management point list.
This name looks like:
<CMG service name>/CCM_Proxy_MutualAuth/<MP Role ID>

The site automatically uploads all published external URLs to the CMG. This behavior
allows the CMG to do URL filtering. All URL mappings replicate to the CMG connection
point. It then forwards the communication to internal servers according to the external
URL from the client request.

Security guidance

Publish the certificate revocation list
Publish your PKI's certificate revocation list (CRL) for internet-based clients to access.
When deploying a CMG using PKI, configure the service to Verify client certificate
revocation on the Settings tab. This setting configures the service to use a published
CRL. For more information, see Plan for PKI certificate revocation.

This CMG option verifies the client authentication certificate.

     If the client is using Microsoft Entra ID or Configuration Manager token-based
     authentication, the CRL doesn't matter.

     If you use PKI, and externally publish the CRL, then enable this option
     (recommended).

<!-- p.2806 -->

     If you use PKI, don't publish the CRL, then disable this option.

     If you misconfigure this option, it can cause more traffic from clients to the CMG.
     This traffic can increase the Azure egress data, which can increase your Azure costs.

Review entries in the site's certificate trust list
Each Configuration Manager site includes a list of trusted root certification authorities,
the certificate trust list (CTL). View and modify the list by going to the Administration
workspace, expand Site Configuration, and select Sites. Select a site, and then select
Properties in the ribbon. Switch to the Communication Security tab, and then select Set
under Trusted Root Certification Authorities.

Use a more restrictive CTL for a site with a CMG using PKI client authentication.
Otherwise, clients with client authentication certificates issued by any trusted root that
already exists on the management point are automatically accepted for client
registration.

This subset provides administrators with more control over security. The CTL restricts the
server to only accept client certificates that are issued from the certification authorities
in the CTL. For example, Windows ships with certificates for many public and globally
trusted certificate providers. By default, the computer running IIS trusts certificates that
chain to these well-known certificate authorities (CA). Without configuring IIS with a CTL,
any computer that has a client certificate issued from these CAs are accepted as a valid
Configuration Manager client. If you configure IIS with a CTL that didn't include these
CAs, client connections are refused if the certificate chained to these CAs.

Enforce TLS 1.2
Use the CMG setting to Enforce TLS 1.2. It only applies to the Azure cloud service VM. It
doesn't apply to any on-premises Configuration Manager site servers or clients.

Starting in version 2107 with the update rollup, this setting also applies to the CMG
storage account.

For more information on TLS 1.2, see How to enable TLS 1.2.

Use token-based authentication
If you have devices that have one or more of the following conditions, consider using
Configuration Manager token-based authentication:

     An internet-based device that doesn't often connect to the internal network

<!-- p.2807 -->

     The device isn't able to join Microsoft Entra ID
     You don't have a method to install a PKI-issued certificate

With token-based authentication, the site automatically issues tokens for devices that
register on the internal network. You can create a bulk registration token for internet-
based devices. For more information, see Token-based authentication for CMG.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2808 -->

Frequently asked questions about the CMG
Applies to: Configuration Manager (current branch)

This article answers your frequently asked questions about the cloud management gateway
(CMG). For more information, see Overview of CMG.

Do I need any certificates?
Yes, at least one, and possibly others depending upon your design.

     Server authentication certificate: The CMG creates an HTTPS service to which internet-
     based clients connect. The service requires a server authentication certificate to build the
     secure channel. You can acquire a certificate for this purpose from a public provider, or issue
     it from your public key infrastructure (PKI). For more information, see CMG server
     authentication certificate.

     Client authentication certificate: Depending upon your environment and CMG design, you
     can use PKI certificates for client authentication. This authentication method doesn't
     support user-centric scenarios, but supports devices running any supported version of
     Windows. For more information, see Configure client authentication for CMG: PKI certificate.

     When you use this client authentication method, you also need to export the client
     certificate's trusted root chain. You then use this chain of certificates when you create the
     CMG and on the CMG connection point.

     HTTPS-enabled the management point: Depending upon how you configure the site, and
     which client authentication method you choose, you may need to configure your internet-
     enabled management points to support HTTPS. For more information, see Configure client
     authentication for CMG: Enable management point for HTTPS.

Do I need Azure ExpressRoute?
No. Azure ExpressRoute lets you extend your on-premises network into the Microsoft cloud.
ExpressRoute, or other such virtual network connections aren't required for the CMG. The design
of the CMG allows internet-based clients to communicate through the Azure service to on-
premises site systems with no additional network configuration. For more information, see
Overview of CMG.

<!-- p.2809 -->

Do I need to maintain or secure the Azure
virtual machines?
No. The CMG is a software as a service (SaaS) solution that extends your Configuration Manager
environment into the cloud. The design of the CMG uses Azure platform as a service (PaaS). Using
the subscription you provide, Configuration Manager creates the necessary virtual machines
(VMs), storage, and networking. Azure PaaS secures and updates the VMs. For more security
specific information on the underlying PaaS solution that the CMG is built on, see Securing PaaS
deployments.

  ） Important

  The CMG runs on Microsoft-managed Azure platform services. Some security or vulnerability
  scans that target CMG virtual machine instances can return findings that aren’t applicable or
  actionable, as they reflect generic checks for customer-managed infrastructure rather than
  Azure-managed platform services.

Since the CMG acts as a proxy for client communication, it doesn't process, keep, or store any
client data. The communication path over the internet always uses HTTPS. For greater security,
configure the management point for HTTPS. Also configure the site option for clients to encrypt
inventory and status messages. For more information, see Plan for security: Signing and
encryption.

Do I need to update the Virtual machine if the
image is deprecated?
No. The CMG VMs are deployed using template and IIS are configured, this will be broken if you
manually update the VMs. Product group will fix the issue through update or the current branch
releases.

How can I ensure service continuity during
service updates?
By scaling CMG to include two or more instances, you automatically benefit from Update
Domains in Azure. See How to update a cloud service.

<!-- p.2810 -->

I'm already using IBCM. If I add CMG, how do
clients behave?
If you already deployed internet-based client management (IBCM), you can also deploy the CMG.
Clients receive policy for both services. As they roam onto the internet, they randomly select and
use one of these internet-based services.

Do the user accounts have to be in the same
Microsoft Entra tenant as the tenant associated
with the subscription that hosts the CMG
cloud service?
No, you can deploy CMG into any subscription that can host Azure cloud services.

To clarify terms:

     The Microsoft Entra tenant is the directory of user accounts and app registrations. One
     tenant can have multiple subscriptions.
     An Azure subscription separates billing, resources, and services. It's associated with a single
     tenant.

   Tip

  For more information, see Subscriptions, licenses, accounts, and tenants for Microsoft's
  cloud offerings.

This question is common in the following scenarios:

     When you have distinct test and production Active Directory and Microsoft Entra
     environments, but one single, centralized Azure hosting subscription.

     Your use of Azure has grown organically across different teams.

When you're using a Resource Manager deployment, onboard the Microsoft Entra tenant
associated with the subscription. This connection allows Configuration Manager to authenticate
to Azure to create, deploy, and manage the CMG.

<!-- p.2811 -->

If you're using Microsoft Entra authentication for the users and devices managed over the CMG,
onboard that Microsoft Entra tenant. For more information on Azure services for cloud
management, see Configure Azure services. When you onboard each Microsoft Entra tenant, a
single CMG can provide Microsoft Entra authentication for multiple tenants, regardless of the
hosting location.

Example 1: One tenant with multiple subscriptions
The user identities, device registrations, and app registrations are all in the same tenant. You can
choose which subscription the CMG uses. You can deploy multiple CMG services from one site
into separate subscriptions. The site has a one-to-one relationship with the tenant. You decide
which subscriptions to use for various reasons such as billing or logical separation.

Example 2: Multiple tenants
In other words, your environment has more than one Microsoft Entra ID. If you need to support
user and device identities in both tenants, you need to attach the site to each tenant. This process
requires an administrative account from each tenant to create the app registrations in that
tenant. One site can then host CMG services in multiple tenants. You can create a CMG in any
available subscription in either tenant. Devices that are joined or hybrid joined to either Microsoft
Entra ID could use a CMG.

If the user and device identities are in one tenant, but the CMG's subscription is in another
tenant, you need to attach the site to both tenants. Technically, the client app isn't needed for the
second tenant that only has the CMG service. The client app only provides user and device
authentication for clients that use the CMG service.

How does CMG affect my clients connected
via VPN?
Roaming clients that connect to your environment via a VPN are commonly detected as intranet-
facing. They attempt to connect to your on-premises infrastructure such as management points
and distribution points. Some customers prefer to have these roaming clients managed by cloud
services even when connected via VPN.

You can also associate the CMG with a boundary group. This action forces these clients to not use
the on-premises site systems. For more information, see Configure boundary groups.

<!-- p.2812 -->

How does the configuration of the
management point affect internal clients?
To secure sensitive traffic sent over a CMG, you need to configure at least one management point
to use HTTPS or configure the site for Enhanced HTTP.

Then when you deploy a CMG, if you use PKI certificates for HTTPS communication on the CMG-
enabled management point, select the option to Allow internet-only clients on the management
point properties. This setting makes sure that internal clients continue to use HTTP management
points in your environment.

If you use Enhanced HTTP, you don't need to configure this setting. Clients continue to use HTTP
when communicating directly to the CMG-enabled management point. For more information, see
Enhanced HTTP.

What are the differences with client
authentication between Microsoft Entra ID
and certificates?
You can use Microsoft Entra ID or a client authentication certificate for devices to authenticate to
the CMG service. You can also use Configuration Manager site-issued tokens for authentication.

If you manage traditional Windows clients with Active Directory domain-joined identity, they
need PKI certificates to secure the communication channel. These clients can include any
supported version of Windows. You can use all CMG-supported features, but software
distribution is limited to devices only. Install the Configuration Manager client before the device
roams onto the internet, or use token authentication.

You can also manage Windows 10 or later clients with modern identity, either hybrid or pure
cloud domain-joined with Microsoft Entra ID. Clients use Microsoft Entra ID to authenticate rather
than PKI certificates. Using Microsoft Entra ID is simpler to set up, configure and maintain than
more complex PKI systems. You can do all of the same management activities plus software
distribution to the user. It also enables additional methods to install the client on a remote
device.

Microsoft recommends joining devices to Microsoft Entra ID. Internet-based devices can use
Microsoft Entra ID to authenticate with Configuration Manager. It also enables both device and
user scenarios whether the device is on the internet or connected to the internal network.

<!-- p.2813 -->

For more information, see Configure client authentication.

Should I use a virtual machine scale
set deployment?
Yes, if your site is version 2107 or later. It's no longer a pre-release feature, and recommended for
all customers. If you have an existing classic CMG deployment, you can convert it to a virtual
machine scale set.

If your site is version 2010 or 2103, the virtual machine scale set deployment method is a pre-
release feature. It's only intended for customers with a Cloud Solution Provider (CSP)
subscription.

  ） Important

  Starting in version 2203, the option to deploy a CMG as a cloud service (classic) is removed.
  All CMG deployments should use a virtual machine scale set. For more information, see
  Removed and deprecated features.

For more information about deploying a CMG as a virtual machine scale set, see Plan for CMG.

Does a content-enabled CMG use Azure CDN?
No. It doesn't currently support the Azure content delivery network (CDN). The CDN is a global
solution for rapidly delivering high-bandwidth content by caching the content at strategically
placed physical nodes across the world. For more information, see What is Azure CDN?.

Do I need to do anything with the deprecation
of the Azure AD Graph API and Azure AD
Authentication Library (ADAL)?
No. You may have seen the following blog post and are wondering how it applies to
Configuration Manager: Update your applications to use Microsoft Authentication Library and
Microsoft Graph API    . This post is referring to any developed code that uses these
authentication libraries. Configuration Manager has been using the Microsoft Graph API and
Microsoft Authentication Library (MSAL) in some places for several years. All other components

<!-- p.2814 -->

are updated in Configuration Manager version 2107 with the update rollup. If you stay current
with Configuration Manager versions, there's nothing else you need to do.

Some people confuse the information in this blog post with the application registrations in
Microsoft Entra ID that Configuration Manager uses for various cloud-attached services. These
app registrations are cloud-based service principals that don't directly use these authentication
libraries. If a Microsoft Entra Global Administrator manually created the Configuration Manager
app registrations in Microsoft Entra ID, they can double-check that those registrations have
permissions for the Microsoft Graph API. They don't need permissions for the Azure AD Graph
API. For more information, see Manually register Microsoft Entra apps.

For more information: Migrate your apps from Azure AD Graph to Microsoft Graph.

 Last updated on 05/26/2026

<!-- p.2815 -->

Data flow for CMG
Applies to: Configuration Manager (current branch)

Use this article to understand how data flows between components of the cloud management
gateway (CMG). It requires specific network ports and internet endpoints to function. You don't
need to open any inbound ports to your on-premises network. The service connection point
and CMG connection point site system roles start all communication with Azure and the CMG.
These two roles need to create outbound connections to the Microsoft cloud. The service
connection point deploys and monitors the service in Azure, so needs to be online. The CMG
connection point connects to the CMG to manage communication between the CMG and on-
premises site system roles.

Data flow diagram
The following diagram is a basic, conceptual data flow for the CMG:

   1. The service connection point connects to Azure over HTTPS port 443. It authenticates
     using Microsoft Entra ID. The service connection point deploys the CMG in Azure. The
     CMG creates the HTTPS service using the server authentication certificate.

   2. The CMG connection point connects to the CMG in Azure. It holds the connection open,
     and builds the channel for future two-way communication.

          When you deploy the CMG as a virtual machine scale set, this flow is over HTTPS.

<!-- p.2816 -->

           If you deploy the CMG as a classic cloud service, it first tries TCP-TLS. If that
           connection fails, it switches to HTTPS.

     For more information, see Note 2: CMG connection point HTTPS ports for one VM.

   3. The client connects to the CMG over HTTPS port 443. It authenticates using Microsoft
     Entra ID, the client authentication certificate, or a site-issued token.

       ７ Note

       If you enable the CMG to serve content, the client connects directly to Azure blob
       storage over HTTPS port 443. For more information, see Content data flow.

   4. The CMG forwards the client communication over the existing connection to the on-
     premises CMG connection point. You don't need to open any inbound firewall ports.

   5. The CMG connection point forwards the client communication to the on-premises
     management point and software update point.

For more information when you integrate with Microsoft Entra ID, see Configure Azure services:
Cloud management data flow.

Content data flow
When a client uses a CMG as a content location:

   1. The management point gives the client an access token along with the list of content
     sources. This token is valid for 24 hours, and gives the client access to the cloud-based
     content source.

   2. The management point responds to the client's location request with the service name of
     the CMG. This property is the same as the common name of the server authentication
     certificate.

     If you're using your domain name, for example, WallaceFalls.contoso.com , then the client
     first tries to resolve this FQDN. Clients use the CNAME alias in your domain's internet-
     facing DNS to resolve the Azure deployment name.

   3. The client next resolves the deployment name to a valid IP address. This response is
     handled by Azure's DNS.

   4. The client connects to the CMG. Azure load balances the connection to one of the VM
     instances. The client authenticates itself using the access token.

<!-- p.2817 -->

   5. The CMG authenticates the client's access token, and then gives the client the exact
      content location in Azure storage.

   6. If the client trusts the CMG's server authentication certificate, it connects to Azure storage
      to download the content.

When distributing content to CMG:

   1. SMS_DISTRIBUTION_MANAGER (Distmgr) Creates request to distribute content to CMG.

   2. SMS_PACKAGE_TRANSFER_MANAGER (PkgXfermgr) gets send request and starts upload
      process by copying the package to Temp share location.

   3. SMS_PACKAGE_TRANSFER_MANAGER (PkgXfermgr) acquires access token for CMG
      storage.

   4. SMS_PACKAGE_TRANSFER_MANAGER (PkgXfermgr) uploads content to CMG storage.

Required ports
This table lists the required network ports and protocols. The Client is the device that starts the
connection, requiring an outbound port. The Server is the device that accepts the connection,
requiring an inbound port.

                                                                                  ﾉ   Expand table

 Client                   Protocol   Port         Server           Description

 Service connection       HTTPS      443          Azure            CMG deployment
 point

 CMG connection           HTTPS      443          CMG service      Protocol to build CMG channel to
 point (virtual machine                                            only one VM instance Note 2
 scale set)

 CMG connection           HTTPS      10124-       CMG service      Protocol to build CMG channel to
 point (virtual machine              10139                         two or more VM instances Note 3
 scale set)

 CMG connection           TCP-TLS    10140-       CMG service      Preferred protocol to build CMG
 point (classic cloud                10155                         channel Note 1
 service)

 CMG connection           HTTPS      443          CMG service      Fall back protocol to build CMG
 point (classic cloud                                              channel to only one VM instance
 service)                                                          Note 2

<!-- p.2818 -->

 Client                 Protocol     Port          Server         Description

 CMG connection         HTTPS        10124-        CMG service    Fall back protocol to build CMG
 point (classic cloud                10139                        channel to two or more VM
 service)                                                         instances Note 3

 Client                 HTTPS        443           CMG            General client communication

 Client                 HTTPS        443           Blob storage   Download cloud-based content

 CMG connection         HTTPS or     443 or 80     Management     On-premises traffic, port depends
 point                  HTTP                       point          upon management point
                                                                  configuration

 CMG connection         HTTPS or     443 or 80 /   Software       On-premises traffic, port depends
 point                  HTTP         8530 or       update point   upon software update point
                                     8531                         configuration

 Site Server            HTTPS        443           Azure          CMG deployment

Notes on ports

Note 1: CMG connection point TCP-TLS ports
These ports only apply when you deploy the CMG as a cloud service (classic), which was the
only method available in version 2006 and earlier.

The CMG connection point first tries to establish a long-lived TCP-TLS connection with each
CMG VM instance. It connects to the first VM instance on port 10140. The second VM instance
uses port 10141, up to the 16th on port 10155. A TCP-TLS connection has the best
performance, but it doesn't support internet proxy. If the CMG connection point can't connect
via TCP-TLS, then it falls back to HTTPSNote 2.

Note 2: CMG connection point HTTPS ports for one VM
If you deploy the CMG in a virtual machine scale set, the CMG connection point only
communicates with the service in Azure over HTTPS. It doesn't require TCP-TLS ports to build
the CMG communication channel.

For a CMG deployed as a classic cloud service, it only uses this port if the TCP-TLS connection
fails. If the CMG connection point can't connect to the CMG via TCP-TLSNote 1, it connects to
the Azure network load balancer over HTTPS 443. This behavior is only for one VM instance.

Note 3: CMG connection point HTTPS ports for two or more VMs

<!-- p.2819 -->

If there are two or more VM instances, the CMG connection point uses HTTPS 10124 to the first
VM instance, not HTTPS 443. It connects to the second VM instance on HTTPS 10125, up to the
16th on HTTPS port 10139.

Internet access requirements
If your organization restricts network communication with the internet using a firewall or proxy
device, you need to allow the CMG connection point and service connection point to access
internet endpoints.

For more information, see Internet access requirements.

This section covers the following features:

     Cloud management gateway (CMG)

     Microsoft Entra integration

     Microsoft Entra ID-based discovery

     Cloud distribution point (CDP)

        ７ Note

        The cloud-based distribution point (CDP) is deprecated. Starting in version 2107, you
        can't create new CDP instances. To provide content to internet-based devices, enable
        the CMG to distribute content.

The following sections list the endpoints by role. Some endpoints refer to a service by
<prefix> , which is the prefix name of the CMG. For example, if your CMG is

GraniteFalls.WestUS.CloudApp.Azure.Com , then the actual storage endpoint is
GraniteFalls.blob.core.windows.net .

   Tip

  To clarify some terminology:

        CMG service name: The common name (CN) of the CMG server authentication
        certificate. Clients and the CMG connection point site system role communicate with
        this service name. For example, GraniteFalls.contoso.com or
        GraniteFalls.WestUS.CloudApp.Azure.Com .

<!-- p.2820 -->

         CMG deployment name: The first part of the service name plus the Azure location for
         the cloud service deployment. The cloud service manager component of the service
         connection point uses this name when it deploys the CMG in Azure. The deployment
         name is always in an Azure domain. The Azure location depends upon the
         deployment method, for example:
            Virtual machine scale set: GraniteFalls.WestUS.CloudApp.Azure.Com
            Classic deployment: GraniteFalls.CloudApp.Net

  This article uses examples with a virtual machine scale set as the recommended
  deployment method in version 2107 and later. If you use a classic deployment, note the
  difference as you read this article and configure internet access.

Service connection point for cloud services
For Configuration Manager to deploy the CMG service in Azure, the service connection point
needs access to:

     Specific Azure endpoints, which are different per environment depending upon the
     configuration. Configuration Manager stores these endpoints in the site database. Query
     the AzureEnvironments table in SQL Server for the list of Azure endpoints.

     Azure services:
          management.azure.com (Azure public cloud)

          management.usgovcloudapi.net (Azure US Government cloud)

     For Microsoft Entra user discovery: Microsoft Graph endpoint
        https://graph.microsoft.com/

CMG connection point for cloud services
The CMG connection point needs access to the following endpoints:

                                                                                   ﾉ   Expand table

 Type                  Azure public cloud                     Azure US Government cloud

 Service name          <prefix>.<region>.cloudapp.azure.com   <prefix>.usgovcloudapp.net

 Storage endpoint 1    <prefix>.blob.core.windows.net         <prefix>.blob.core.usgovcloudapi.net

 Storage endpoint 2    <prefix>.table.core.windows.net        <prefix>.table.core.usgovcloudapi.net

<!-- p.2821 -->

 Type                  Azure public cloud                       Azure US Government cloud

 Key vault             <prefix>.vault.azure.net                 <prefix>.vault.usgovcloudapi.net

The CMG connection point site system supports using a web proxy. For more information on
configuring this role for a proxy, see Proxy server support.

The CMG connection point only needs to connect to the CMG service endpoints. It doesn't
need access to other Azure endpoints.

Configuration Manager client for cloud services
Any Configuration Manager client that needs to communicate with a CMG needs access to the
following endpoints:

                                                                                     ﾉ   Expand table

 Type                        Azure public cloud                  Azure US Government cloud

 Deployment name             <prefix>.                            <prefix>.usgovcloudapp.net
                             <region>.cloudapp.azure.com

 Storage endpoint            <prefix>.blob.core.windows.net       <prefix>.blob.core.usgovcloudapi.net

 Microsoft Entra             login.microsoftonline.com            login.microsoftonline.us
 endpoint

Configuration Manager console for cloud services
Any device with the Configuration Manager console needs access to the following endpoints:

                                                                                     ﾉ   Expand table

 Type                               Azure public cloud              Azure US Government cloud

 Microsoft Entra endpoints          login.microsoftonline.com       login.microsoftonline.us
                                    aadcdn.msauth.net
                                    aadcdn.msftauth.net

HTTP headers and verbs
Any networking device that manages communication between the client, the CMG, and the on-
premises site systems has to allow the following HTTP headers and verbs. If these items are

<!-- p.2822 -->

blocked, it will affect client communication through the CMG.

HTTP headers
     Range:
     CCMClientID:
     CCMClientIDSignature:
     CCMClientTimestamp:
     CCMClientTimestampsSignature:

HTTP verbs
     HEAD
     CCM_POST
     BITS_POST
     GET
     PROPFIND

Last updated on 12/08/2025

<!-- p.2823 -->

Plan for internet-based client
management in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use internet-based client management (IBCM) to manage Configuration Manager
clients when they aren't connected to your internal network. Advantages of using IBCM:

      Full control of servers and roles providing the service
      No cloud service dependency
      May not require a virtual private network (VPN)
      All costs are associated with the on-premises service

Because of the higher security requirements of managing client computers on a public
network, IBCM requires the use of PKI certificates. This configuration makes sure that
connections are authenticated by an independent authority. When IBCM clients and site
servers send data, it's encrypted and secure.

Client communications
The following site system roles at primary sites support connections from clients that are
in untrusted locations:

  ７ Note

  While IBCM primarily focuses on the internet-based scenario, the same behaviors
  apply to clients in an untrusted Active Directory forest. Secondary sites don't
  support client connections from untrusted locations.

      Certificate registration point for the Configuration Manager policy module (NDES)

        ２ Warning

        Starting in version 2203, the certificate registration point is no longer
        supported. For more information, see Frequently asked questions about
        resource access deprecation.

      Distribution point

<!-- p.2824 -->

     Content-enabled cloud management gateway (CMG)

     Enrollment proxy point

     Fallback status point

     Management point

     Software update point

About internet facing site systems
There's no requirement to have a trust between a client's forest and that of the site
system server. However, when the forest that contains an internet-facing site system
trusts the forest that contains the user accounts, this configuration supports user-based
policies for devices on the internet when you enable the Client Policy client setting
Enable user policy requests from internet clients.

For example, the following configurations illustrate when IBCM supports user policies for
devices on the internet:

     The internet-based management point is in the perimeter network. That network
     also has a read-only domain controller to authenticate the user. A firewall between
     the perimeter and internal networks allows Active Directory packets.

     The user account is in the intranet-based forest. The internet-based management
     point is in the perimeter-based forest. The perimeter forest trusts the internal
     forest. A firewall between the perimeter and internal networks allows the
     authentication packets.

     The user account and the internet-based management point are both in the
     intranet-based forest. You publish the management point to the internet with a
     web proxy server.

Use a web proxy server
You can place internet-based site systems in the intranet when you publish them to the
internet with a web proxy server. Configure these site systems for client connections
from the internet only, or client connections from the internet and intranet. When you
use a web proxy server, you can configure it for Secure Sockets Layer (SSL) bridging to
SSL or SSL tunneling.

SSL bridging to SSL

<!-- p.2825 -->

SSL bridging to SSL is the recommended and more secure configuration, because it uses
SSL termination with authentication. It authenticates client computers with computer
authentication. Mobile devices that you enroll with Configuration Manager don't
support SSL bridging.

With SSL termination at the proxy, it inspects packets from the internet before it
forwards them to the internal network. The proxy authenticates the connection from the
client, terminates it, and then opens a new authenticated connection to the internet-
based site systems. When Configuration Manager clients use a proxy, the client securely
contains its identity (GUID) in the packet payload. The management point doesn't
consider the proxy to be the client. Configuration Manager doesn't support bridging
with HTTP to HTTPS, or from HTTPS to HTTP.

  ７ Note

  Configuration Manager doesn't support setting third-party SSL bridging
  configurations. For example, Citrix Netscaler or F5 BIG-IP. Please work with your
  device vendor to configure it for use with Configuration Manager.

Tunneling
If your proxy web server can't support the requirements for SSL bridging, Configuration
Manager also supports SSL tunneling. You can also use SSL tunneling to support mobile
devices that you enroll with Configuration Manager. It's a less secure option because the
proxy forwards the SSL packets from the internet to the site systems without SSL
termination. The proxy doesn't inspect the packets for malicious content. When you use
SSL tunneling, there are no certificate requirements for the proxy web server.

Plan for internet-based clients
Decide whether to configure your internet-based clients for management on both the
intranet and the internet, or for internet-only client management. You can only
configure this management option during client installation. To change it later, reinstall
the client.

  ７ Note

  If you configure a management point to support internet-based clients, clients that
  connect to this management point will become internet-capable when they next
  refresh their list of available management points.

<!-- p.2826 -->

  You don't have to restrict the configuration of internet-only client management to
  the internet. You can also use it on the intranet.

Clients that you configure for internet-only management only communicate with the
site systems that you configure for client connections from the internet. Use this
configuration in the following scenarios:

     For computers that you know will never connect to your intranet. For example,
     point of sale computers in remote locations.
     To restrict client communication to HTTPS only. For example, to support firewall
     and restricted security policies.
     When you install internet-based site systems in a perimeter network, and you want
     to manage these servers as Configuration Manager clients.

  ７ Note

  When you want to manage workgroup clients on the internet, install them as
  internet-only.

  When you configure a mobile device to use an internet-based management point,
  it automatically configures as internet-only.

You can configure other clients for both internet and intranet client management. When
they detect a change of network, they automatically switch between IBCM and intranet
client management. If these clients can find and connect to a management point that
supports client connections on the intranet, these clients are managed as intranet
clients. Intranet clients have full Configuration Manager functionality. If the clients can't
find or connect to a management point that supports client connections on the intranet,
they attempt to connect to an internet-based management point. If this action
succeeds, these clients are then managed by the internet-based site systems in their
assigned site.

The benefit in automatic switching is that clients can use all features when they connect
to the intranet, and receive essential management when they're on the internet. Content
download that begins on the internet can seamlessly resume on the intranet, and the
other way around.

Prerequisites
IBCM in Configuration Manager has the following dependencies:

<!-- p.2827 -->

     Clients require an internet connection. Configuration Manager uses the device's
     existing internet connection. Mobile devices must have a direct internet
     connection. Full client computers can have either a direct internet connection or
     connect by using a proxy web server.

     Site systems that support IBCM require an internet connection, and must be in an
     Active Directory domain. The internet-based site systems don't require a trust
     relationship with the Active Directory forest of the site server. However, when the
     internet-based management point can authenticate the user by using Windows
     authentication, it supports user policies. If Windows authentication fails, it only
     supports device policies.

        ７ Note

        To support user policies, also enable the following client settings in the Client
        Policy group:
          Enable user policy polling on clients
          Enable user policy requests from Internet clients

     A public key infrastructure (PKI) to deploy and manage the required certificates for
     internet-based clients and site system servers. For more information, see PKI
     certificate requirements.

     Register public DNS host entries for the internet fully qualified domain names
     (FQDN) of site systems that support IBCM.

     Enable the option to Use PKI client certificate (client authentication capability)
     when available on the Communication Security tab of the site properties. This
     option is required.

Client communication requirements
Intervening firewalls or proxy servers must allow the client communication for internet-
based site systems:

     Support HTTP 1.1

     Allow HTTP content type of multipart MIME attachment (multipart/mixed and
     application/octet-stream)

Verbs

<!-- p.2828 -->

Allow the following verbs for the internet-based site system server roles:

                                                                         ﾉ   Expand table

 Role                                                   Verbs

 Management point                                       - HEAD
                                                        - CCM_POST
                                                        - BITS_POST
                                                        - GET
                                                        - PROPFIND

 Distribution point                                     - HEAD
                                                        - GET
                                                        - PROPFIND

 Fallback status point                                  POST

HTTP headers

Allow the following HTTP headers for the internet-based site system server roles:

                                                                         ﾉ   Expand table

 Role                              HTTP headers

 Management point                  - Range:
                                   - CCMClientID:
                                   - CCMClientIDSignature:
                                   - CCMClientTimestamp:
                                   - CCMClientTimestampsSignature:

 Distribution point                Range:

For similar communication requirements when you use the software update point for
client connections from the internet, see the documentation for Windows Server Update
Services (WSUS).

Unsupported features
Not all client management functionality is appropriate for the internet. Configuration
Manager doesn't support some features for clients on the internet. These unsupported
features typically rely on Active Directory Domain Services or aren't appropriate for a
public network.

<!-- p.2829 -->

The following features aren't supported when you manage clients on the internet with
IBCM:

     Client deployment over the internet, such as client push and software update-
     based client deployment. Use manual client installation.

     Automatic site assignment

     Wake-on-LAN

     OS deployment. However, you can deploy task sequences that don't deploy an OS.

     Remote control

     Software deployment to users. This feature relied upon the application catalog,
     which is no longer supported.

     Client roaming. Roaming enables clients to always find the closest distribution
     points to download content. Clients non-deterministically select one of the
     internet-based site systems, whatever the bandwidth or physical location.

When you configure a software update point to accept connections from the internet,
internet-based clients always scan against this software update point to determine
which software updates are required. When these clients are on the internet, they first
try to download the software updates from Microsoft Update, rather than from an
internet-based distribution point. If this behavior fails, they then try to download the
required software updates from an internet-based distribution point.

   Tip

  The Configuration Manager client automatically determines whether it's on the
  intranet or the internet. If the client can contact a domain controller or an on-
  premises management point, it sets its connection type to "Currently intranet".
  Otherwise, it switches to "Currently internet", and communicates with the site
  systems assigned to its site.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2830 -->

Install and assign Configuration Manager
clients using Microsoft Entra ID for
authentication
To install the Configuration Manager client on Windows devices using Microsoft Entra
authentication, integrate Configuration Manager with Microsoft Entra ID. Clients can be on the
intranet communicating directly with an HTTPS-enabled management point or any
management point in a site enabled for Enhanced HTTP. They can also be internet-based
communicating through the CMG or with an Internet-based management point. This process
uses Microsoft Entra ID to authenticate clients to the Configuration Manager site. Microsoft
Entra ID replaces the need to configure and use client authentication certificates.

Setting up Microsoft Entra ID may be easier for some customers than setting up a public key
infrastructure for certificate-based authentication. There are features that require you onboard
the site to Microsoft Entra ID, but don't necessarily require the clients to be Microsoft Entra
joined. For more information, see the following articles:

     Plan for Microsoft Entra ID
     Use Microsoft Entra ID for co-management

Before you begin
     A Microsoft Entra tenant is a prerequisite

     Device requirements:

        A supported version of Windows 10 or later

        Joined to Microsoft Entra ID, either pure cloud domain-joined, or Microsoft Entra
        hybrid joined

     User requirements:

        The signed in user must be a Microsoft Entra identity.

        If the user is a federated or synchronized identity, configure both Configuration
        Manager Active Directory user discovery and Microsoft Entra user discovery. For more
        information about hybrid identities, see Define a hybrid identity adoption strategy.

     In addition to the existing prerequisites for the management point site system role, also
     enable ASP.NET 4.5 on this server. Include any other options that are automatically
     selected when enabling ASP.NET 4.5.

<!-- p.2831 -->

     Determine whether your management point needs HTTPS. For more information, see
     Enable management point for HTTPS.

     Optionally set up a cloud management gateway (CMG) to deploy internet-based clients.
     For on-premises clients that authenticate with Microsoft Entra ID, you don't need a CMG.

  ） Important

  Use of the NLM AllowedTlsAuthenticationEndpoints Intune Policy can cause Entra-only
  joined devices to fail to register when on a local network with connectivity to the
  endpoints specified in the policy.

   Tip

  Configuration Manager extends its support for internet-based devices that don't often
  connect to the internal network, aren't able to join Microsoft Entra ID, and don't have a
  method to install a PKI-issued certificate. For more information, see Token-based
  authentication for CMG.

Configure Azure Services for Cloud Management
Connect your Configuration Manager site to Microsoft Entra ID as the first step. For details of
this process, see Configure Azure services. Create a connection to the Cloud Management
service.

Enable Microsoft Entra user Discovery as part of onboarding to Cloud Management.

After you complete these actions, your Configuration Manager site is connected to Microsoft
Entra ID.

  ７ Note

  If your devices are in a Microsoft Entra tenant that's separate from the tenant with a
  subscription for the CMG compute resources, starting in version 2010 you can disable
  authentication for tenants not associated with users and devices. For more information,
  see Configure Azure services.

Configure client settings

<!-- p.2832 -->

These client settings help configure Windows devices to be hybrid-joined. They also enable
internet-based clients to use the CMG.

   1. Configure the following client settings in the Cloud Services group. For more information,
     see How to configure client settings.

           Allow access to cloud distribution point: Enable this setting to help internet-based
           devices get the required content to install the Configuration Manager client. Devices
           can get the content from the CMG.

           Automatically register new Windows 10 or later domain joined devices with
           Microsoft Entra ID: Set to Yes or No. The default setting is Yes. This behavior is also
           the default in Windows.

              Tip

             Hybrid-joined devices are joined to an on-premises Active Directory domain
             and registered with Microsoft Entra ID. For more information, see Microsoft
             Entra hybrid joined devices.

           Enable clients to use a cloud management gateway: Set to Yes (default), or No.

   2. Deploy the client settings to the required collection of devices. Don't deploy these
     settings to user collections.

To confirm the device is hybrid-joined, run dsregcmd.exe /status in a command prompt. If the
device is Microsoft Entra joined or hybrid-joined, the AzureAdjoined field in the results shows
YES. For more information, see dsregcmd command - device state.

Install and register the client using Microsoft Entra
identity
To manually install the client using Microsoft Entra identity, first review the general process on
How to install clients manually.

  ７ Note

  The device needs access to the internet to contact Microsoft Entra ID, but doesn't need to
  be internet-based.

<!-- p.2833 -->

The following example shows the general structure of the command line: ccmsetup.exe /mp:
<source management point> CCMHOSTNAME=<internet-based management point> SMSSITECODE=<site

code> SMSMP=<initial management point> AADTENANTID=<Azure AD tenant identifier>
AADCLIENTAPPID=<Azure AD client app identifier> AADRESOURCEURI=<Azure AD server app

identifier>

For more information, see Client installation properties.

The /mp parameter and CCMHOSTNAME property specify one of the following, depending upon
the scenario:

      On-premises management point. Only specify the /mp parameter. The CCMHOSTNAME
      property isn't required.
      Cloud management gateway
      Internet-based management point

This example uses a cloud management gateway. It replaces sample values: ccmsetup.exe
/mp:https://CONTOSO.EASTUS.CLOUDAPP.AZURE.COM/CCM_Proxy_MutualAuth/72186325152220500

CCMHOSTNAME=CONTOSO.EASTUS.CLOUDAPP.AZURE.COM/CCM_Proxy_MutualAuth/72186325152220500

SMSSITECODE=ABC

The site publishes additional Microsoft Entra information to the cloud management gateway
(CMG). A Microsoft Entra joined client gets this information from the CMG during the ccmsetup
process, using the same tenant to which it's joined. This behavior further simplifies installing
the client in an environment with more than one Microsoft Entra tenant. The only two required
ccmsetup properties are CCMHOSTNAME and SMSSITECODE .

To automate the client install using Microsoft Entra identity via Microsoft Intune, see How to
prepare internet-based devices for co-management.

Next steps
Once complete, you can continue to monitor and manage clients.

 Last updated on 12/08/2025

<!-- p.2834 -->

Token-based authentication for cloud
management gateway
Applies to: Configuration Manager (current branch)

The cloud management gateway (CMG) supports many types of clients, but even with
Enhanced HTTP, these clients require a client authentication certificate. This certificate
requirement can be challenging to provision on internet-based clients that don't often connect
to the internal network, aren't able to join Microsoft Entra ID, and don't have a method to
install a PKI-issued certificate.

To overcome these challenges, Configuration Manager extends its device support by issuing its
own authentication tokens to devices. To take full advantage of this feature, after you update
the site, also update clients to the latest version. The complete scenario isn't functional until
the client version is also the latest. If necessary, make sure you promote the new client version
to production.

Clients initially register for these tokens using one of the following two methods:

      Internal network

      Bulk registration

The Configuration Manager client together with the management point manage this token, so
there's no OS version dependency at client level. This feature is available for any supported
client OS version.

  ７ Note

  These methods only support device-centric management scenarios.

  Microsoft recommends joining devices to Microsoft Entra ID. Internet-based devices can
  use Microsoft Entra ID to authenticate with Configuration Manager. It also enables both
  device and user scenarios whether the device is on the internet or connected to the
  internal network. For more information, see Install and register the client using Microsoft
  Entra identity.

Make sure to Enable clients to use a cloud management gateway in the Cloud services group
of client settings. Even with a site token, clients can't communicate with a CMG if client settings
don't allow it. For more information, see About client settings: Cloud services.

Internal network registration

<!-- p.2835 -->

This method requires the client to first register with the management point on the internal
network. Client registration typically happens right after installation. The management point
gives the client a unique token that shows it's using a self-signed certificate. When the client
roams onto the internet, to communicate with the CMG it pairs its self-signed certificate with
the management point-issued token.

This behavior is enabled by default on the Hierarchy.

  ７ Note

  With an HTTPS management point, the client needs to first register regardless of
  internet/intranet management point. The client needs to present a valid PKI-issued
  certificate, a Microsoft Entra token, or a bulk registration token.

Bulk registration token
If you can't install and register clients on the internal network, create a bulk registration token.
Use this token when the client installs on an internet-based device, and registers through the
CMG. The bulk registration token has a short-validity period, and isn't stored on the client or
the site. It allows the client to generate a unique token, which paired with its self-signed
certificate, lets it authenticate with the CMG.

  ７ Note

  Don't confuse bulk registration tokens with those that Configuration Manager issues to
  individual clients. The bulk registration token enables the client to initially install and
  communicate with the site. This initial communication is long enough for the site to issue
  the client its own, unique client authentication token. The client then uses its
  authentication token for all communication with the site while it's on the internet. Beyond
  the initial registration, the client doesn't use or store the bulk registration token.

To create a bulk registration token for use during client installation on internet-based devices,
complete the following actions:

   1. Sign in to the top-level site server in the hierarchy with an account that is a Full
     Administrator in Configuration Manager and a member of the local Administrators group
     on the server.

   2. Open a command prompt as an administrator.

<!-- p.2836 -->

   3. Run the tool from the \bin\X64 folder of the Configuration Manager installation directory
     on the site server: BulkRegistrationTokenTool.exe . Create a new token with the /new
     parameter. For example, BulkRegistrationTokenTool.exe /new . For more information, see
     Bulk registration token tool usage.

   4. Copy the token and save it in a secure location.

   5. Install the Configuration Manager client on an internet-based device. Include the client
     installation parameter: /regtoken. The following example command line includes the
     other required setup parameters and properties:

      ccmsetup.exe /mp:https://CONTOSO.CLOUDAPP.NET/CCM_Proxy_MutualAuth/72186325152220500

     CCMHOSTNAME=CONTOSO.CLOUDAPP.NET/CCM_Proxy_MutualAuth/72186325152220500

     SMSSiteCode=ABC
     /regtoken:eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik9Tbzh2Tmd5VldRUjlDYVh5T2lacH

     FlMDlXNCJ9.eyJTQ0NNVG9rZW5DYXRlZ29yeSI6IlN7Q01QcmVBdXRoVG9rZW4iLCJBdXRob3JpdHkiOiJTQ
     0NNIiwiTGljZW5zZSI6IlNDQ00iLCJUeXBlIjoiQnVsa1JlZ2lzdHJhdGlvbiIsIlRlbmFudElkIjoiQ0RDQ

     zVFOTEtMEFERi00QTI0LTgyRDAtMTk2NjY3RjFDMDgxIiwiVW5pcXVlSWQiOiJkYjU5MWUzMy1wNmZkLTRjN

     WItODJmMy1iZjY3M2U1YmQwYTIiLCJpc3MiOiJ1cm46c2NjbTpvYXV0aDI6Y2RjYzVlOTEtMGFkZi00YTI0L
     TgyZDAtMTk2NjY3ZjFjMDgxIiwiYXVkIjoidXJuOnNjY206c2VydmljZSIsImV4cCI6MTU4MDQxNbUwNSwib

     mJmIjoxNTgwMTU2MzA1fQ.ZUJkxCX6lxHUZhMH_WhYXFm_tbXenEdpgnbIqI1h8hYIJw7xDk3wv625SCfNfs
     qxhAwRwJByfkXdVGgIpAcFshzArXUVPPvmiUGaxlbB83etUTQjrLIk-

     gvQQZiE5NSgJ63LCp5KtqFCZe8vlZxnOloErFIrebjFikxqAgwOO4i5ukJdl3KQ07YPRhwpuXmwxRf1vsiaw

     XBvTMhy40SOeZ3mAyCRypQpQNa7NM3adCBwUtYKwHqiX3r1jQU0y57LvU_brBfLUL6JUpk3ri-
     LSpwPFarRXzZPJUu4-mQFIgrMmKCYbFk3AaEvvrJienfWSvFYLpIYA7lg-6EVYRcCAA

         Tip

        For more information on this command line, see Install and register the client using
        Microsoft Entra identity. This process is similar, just doesn't use the Microsoft Entra
        properties.

To verify, review the following log file for a similar entry:

 ClientLocation.log
 Rotating internet management point, new management point [1] is:
 https://CONTOSO.CLOUDAPP.NET/CCM_Proxy_MutualAuth/72186325152220500 (0) with
 capabilities: <Capabilities SchemaVersion ="1.0"><Property Name="SSL" Version="1" />
 </Capabilities>

<!-- p.2837 -->

To troubleshoot installation, review %WinDir%\ccmsetup\logs\ccmsetup.log on the client. After
installation, review %WinDir%\ccm\logs\ClientIDManagerStartup.log .

On the server, review the following logs:

     CMG logs
     Management point
           CCM_STS.log
           MP_RegistrationManager.log
           ClientAuth.log

Bulk registration token tool usage
The BulkRegistrationTokenTool.exe tool is in the \bin\X64 folder of the Configuration
Manager installation directory on the site server. Sign in to the site server, and run it as an
administrator. It supports the following command-line parameters:

      /?

      /new
      /lifetime

/?

Display this usage information.

Example: BulkRegistrationTokenTool.exe /?

/new

Create a new bulk registration token.

Example: BulkRegistrationTokenTool.exe /new

The tool displays the following information:

     A GUID that the site uses to track issued tokens
     The token validity period, which is three days by default.
     The bulk registration token.

The token isn't stored on the client or the site. Make sure to copy the token from the command
prompt, and store in a secure location.

<!-- p.2838 -->

/lifetime

Use with /new parameter to specify the token validity period of the token. Specify an integer
value in minutes. The default value is 4,320 (three days). The maximum value is 10,080 (seven
days).

Example: BulkRegistrationTokenTool.exe /lifetime 4320

Bulk registration token management
You can see previously created bulk registration tokens and their lifetimes in the Configuration
Manager console and block their usage if necessary. The site database doesn't, however, store
bulk registration tokens.

Review a bulk registration token
   1. In the Configuration Manager console, go to the Administration workspace.

   2. Expand Security, and select the Certificates node. The console lists all site-related
     certificates and bulk registration tokens in the details pane.

   3. Select the bulk registration token to review.

You can filter or sort on the Type column. Identify specific bulk registration tokens based on
their GUID. When you create a bulk registration token, the tool displays the GUID.

Block a bulk registration token
   1. In the Configuration Manager console, go to the Administration workspace.

   2. Expand Security, select the Certificates node, and select the bulk registration token to
     block.

   3. On the Home tab of the ribbon bar or the right-click context menu, select Block. To
     unblock previously blocked bulk registration tokens, select the Unblock action.

Token Signing
The token the client gets the from the Management Point (when registered internally) or when
installed using the Bulk token is signed by the SMS Token Signing Certificate. This is a self-
signed certificate created by the Certificate Manager component using the SMS Issuing root
certificate. The Configuration Manager-issued token includes the reference of the SMS Token

<!-- p.2839 -->

Signing Certificate, apart from other auth headers when sending a request to the Management
Point via the CMG.

While it's not typical that the SMS Issuing or the SMS Token Signing Certificate needs to be
renewed, there are some uncertain scenarios that can require the certificate be renewed:

     Certificate is corrupted
     SMS issuing certificate is renewed
     Site operating system upgrade, where a SHA-1 hash algorithm was used to sign the
     certificate.

  ７ Note

  If the SMS Token Signing Certificate is renewed, clients using the Configuration Manager-
  issued token won't be able to authenticate until the new token, signed with the newer
  certificate, is provided.

Token renewal
The client renews its unique, Configuration Manager-issued token once a month, and it's valid
for 90 days. A client doesn't need to connect to the internal network to renew its token. As
long as the token is still valid, connecting to the site using a CMG is sufficient. If the token isn't
renewed within 90 days, the client must directly connect to a management point on an internal
network to receive a new token.

  ７ Note

  The token will only renew during the startup of the Configuration Manager Client.
  Therefore, the SMS Agent Host (CCMExec) Service or the client machine must restart at
  least every 90 days.

You can't renew a bulk registration token. Once a bulk registration token expires, generate a
new one for internet-based device registration using a CMG.

See also
     Overview of cloud management gateway

     Install and assign Configuration Manager clients using Microsoft Entra ID for
     authentication

<!-- p.2840 -->

Last updated on 12/08/2025
