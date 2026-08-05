---
title: "Core infrastructure documentation — pages 2721-2760"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2721-2760
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2721-2760
family: sccm
documentKind: "doc"
abstract: "Feedback Was this page helpful?  Yes  No Provide product feedback CMG client authentication Article • 11/16/2023 Applies to: Configuration Manager (current branch) Clients that connect to a cloud management gateway (CMG) are potentially on the untrusted public internet. Becaus"
---

# Core infrastructure documentation — pages 2721-2760

<!-- p.2721 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2722 -->

CMG client authentication
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

Clients that connect to a cloud management gateway (CMG) are potentially on the
untrusted public internet. Because of the client's origin, they have a higher
authentication requirement. There are three options for identity and authentication with
a CMG:

      Microsoft Entra ID
      PKI certificates
      Configuration Manager site-issued tokens

The following table summarizes the key factors for each method:

                                                                          ﾉ     Expand table

                             Microsoft Entra ID      PKI certificate    Site token

 ConfigMgr version           All supported           All supported      All supported

 Windows client version      Windows 10 or later     All supported      All supported

 Scenario support            User and device         Device-only        Device-only

 Management point            E-HTTP or HTTPS         E-HTTP or HTTPS    E-HTTP or HTTPS

Microsoft recommends joining devices to Microsoft Entra ID. Internet-based devices can
use Microsoft Entra modern authentication with Configuration Manager. It also enables
both device and user scenarios whether the device is on the internet or connected to
the internal network.

You can use one or more methods. All clients don't have to use the same method.

Which ever method you choose, you may also need to reconfigure one or more
management points. For more information, see Configure client authentication for CMG.

Microsoft Entra ID
If your internet-based devices are running Windows 10 or later, consider using Microsoft
Entra modern authentication with the CMG. This authentication method is the only one
that enables user-centric scenarios. For example, deploying apps to a user collection.

<!-- p.2723 -->

First, the devices need to be either cloud domain-joined or Microsoft Entra hybrid
joined, and the user also needs a Microsoft Entra identity. If your organization is already
using Microsoft Entra identities, then you should be set with this prerequisite. If not, talk
with your Azure administrator to plan for cloud-based identities. For more information,
see Microsoft Entra device identity. Until that process is complete, consider token-based
authentication for internet-based clients with your CMG.

There are a few other requirements, depending upon your environment:

     Enable user discovery methods for hybrid identities
     Enable ASP.NET 4.5 on the management point
     Configure client settings

For more information on these prerequisites, see Install clients using Microsoft Entra ID.

  ７ Note

  If your devices are in a Microsoft Entra tenant that's separate from the tenant with a
  subscription for the CMG compute resources, starting in version 2010 you can
  disable authentication for tenants not associated with users and devices. For more
  information, see Configure Azure services.

PKI certificate
If you have a public key infrastructure (PKI) that can issue client authentication
certificates to devices, then consider this authentication method for internet-based
devices with your CMG. It doesn't support user-centric scenarios, but supports devices
running any supported version of Windows.

   Tip

  Windows devices that are hybrid or cloud domain-joined don't require this
  certificate because they use Microsoft Entra ID to authenticate.

This certificate may also be required on the CMG connection point.

Site token
If you can't join devices to Microsoft Entra ID or use PKI client authentication certificates,
then use Configuration Manager token-based authentication. Site-issued client

<!-- p.2724 -->

authentication tokens work on all supported client OS versions, but only support device
scenarios.

If clients occasionally connect to your internal network, they're automatically issued a
token. They need to communicate directly with an on-premises management point to
register with the site and get this client token.

If you can't register clients on the internal network, you can create and deploy a bulk
registration token. The bulk registration token enables the client to initially install and
communicate with the site. This initial communication is long enough for the site to
issue the client its own, unique client authentication token. The client then uses its
authentication token for all communication with the site while it's on the internet.

Next steps
Next, design how to use a CMG in your hierarchy:

  CMG hierarchy design

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2725 -->

CMG hierarchy design
Article • 03/07/2025

Applies to: Configuration Manager (current branch)

Whether you have a central administration site (CAS), a standalone primary site, or a
small test lab, design the cloud management gateway (CMG) for that environment. This
article provides the information to help you decide how to position the CMG in your
environment.

Create the CMG at the top-tier site of your hierarchy. If that's a CAS, then create CMG
connection points at child primary sites. The cloud service manager component is on the
service connection point, which is also on the CAS. This design can share the service
across different primary sites if needed.

You can create multiple CMG services in Azure, and you can create multiple CMG
connection points. Multiple CMG connection points provide load balancing of client
traffic from the CMG to the on-premises roles.

Other factors, such as the number of clients to manage, also affect your CMG design.
For more information, see Performance and scale.

Design examples

Example 1: Standalone primary site
Contoso has a standalone primary site in an on-premises datacenter at their
headquarters in New York City.

      They create a CMG in the East US Azure region to reduce network latency.
      They create two CMG connection points, both linked to the single CMG service.

As clients roam onto the internet, they communicate with the CMG in the East US Azure
region. The CMG forwards this communication through both of the CMG connection
points.

Example 2: Hierarchy
Fourth Coffee has a CAS in an on-premises datacenter at their headquarters in Seattle.
One primary site is in the same datacenter, and the other primary site is in their main
European office in Paris.

<!-- p.2726 -->

     On the CAS, they create a CMG service in the West US Azure region. They scale the
     number of VMs for the expected load of roaming clients in the entire hierarchy.
     On the Seattle-based primary site, they create a CMG connection point linked to
     the single CMG.
     On the Paris-based primary site, they create a CMG connection point linked to the
     single CMG.

As clients roam onto the internet, they communicate with the CMG in the West US
Azure region. The CMG forwards this communication to the CMG connection point in
the client's assigned primary site.

   Tip

  When providing global client support, content downloads from a geographically
  distant Cloud Management Gateway's storage account can be affected by cloud
  service communication latency between countries or regions. Although the delay
  from one network location to another may not be significant, the necessity for
  communication to traverse different regions can increase latency. For applications
  with large content (either in terms of the number of files or file size), the download
  timing can vary between proximate and distant CMGs (storage accounts). For Client
  operational communication, the impact is lower, as the routing to Storage account
  is different than the routing to CMG VM Api Service.

Multiple environments
Many organizations have separate environments for production, test, development, or
quality assurance. When you plan your CMG deployment, consider the following
questions:

     How many Microsoft Entra tenants does your organization have?
        Is there a separate tenant for testing?
        Are user and device identities in the same tenant?

     How many subscriptions are in each tenant?
        Are there subscriptions that are specific for testing?

Configuration Manager's Azure service for Cloud management supports multiple
tenants. Multiple Configuration Manager sites can connect to the same tenant. A single
site can deploy multiple CMG services into different subscriptions. Multiple sites can
deploy CMG services into the same subscription. Configuration Manager provides
flexibility depending upon your environment and business requirements.

<!-- p.2727 -->

For more information, see the following FAQ: Do the user accounts have to be in the
same Microsoft Entra tenant as the tenant associated with the subscription that hosts
the CMG cloud service?

Boundary groups
You can associate a CMG with a boundary group. This configuration allows clients to
default or fall back to the CMG for client communication according to boundary group
relationships. This behavior is especially useful in branch office and VPN scenarios. You
can direct client traffic away from expensive and slow WAN links to instead use faster
services in Microsoft Azure.

Intranet clients can access a CMG-enabled software update point when it's assigned to a
boundary group. For more information, see Configure boundary groups.

Internet-based clients don't rely on boundary groups. They only use internet-facing or
cloud content sources. If you're only using content-enabled CMGs for these types of
clients, then you don't need to include them in boundary groups.

If you want clients on your internal network to get content from a CMG, then it needs to
be in the same boundary group as the clients. By default, clients prioritize cloud-based
sources last in their list of content sources. This behavior is because there's a cost
associated with downloading content from Azure. Cloud-based sources are typically
used as a fallback source for intranet-based clients. If you want a cloud-first design, then
design your boundary groups to meet this business requirement. For more information,
see Configure boundary groups. For more information on content location priority and
when intranet-based clients use a cloud-based content source, see Content source
priority.

Even though you install the CMG in a specific region of Azure, clients aren't aware of the
Azure regions. They randomly select an available CMG as a content source. If you have
CMGs in multiple regions, and a client receives more than one in the content location
list, it may not download content from the same Azure region.

Next steps
Next, review the features and configurations that the CMG supports:

  Supported configurations for CMG

<!-- p.2728 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2729 -->

Supported configurations for cloud
management gateway
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

Use this article as a reference for the features and configurations that are supported by
the Configuration Manager cloud management gateway (CMG).

Specifications
      All Windows versions listed in Supported operating systems for clients and devices
      are supported for CMG.

      CMG only supports the management point and software update point roles.

      CMG doesn't support clients that only communicate with IPv6 addresses.

      Software update points using a network load balancer don't work with CMG.

      Starting in version 2203, the option to deploy a CMG as a cloud service (classic) is
      removed. All CMG deployments should use a virtual machine scale set. For more
      information, see Removed and deprecated features.

      CMG names need to be between 3-24 alphanumeric characters. The name must
      begin with a letter, end with a letter or digit, and not contain consecutive hyphens.

Support for Configuration Manager features
The following table lists CMG support for Configuration Manager features:

                                                                          ﾉ   Expand table

 Feature                                                                          Support

 Software updates

 Endpoint protection
                                                                                  Note 1

 Hardware and software inventory

<!-- p.2730 -->

Feature                                                                           Support

Client status and notifications

Run scripts

CMPivot

Compliance settings

Automatic client upgrade

Client install
(with Microsoft Entra integration)

Client install
(with token authentication)

Software distribution (device-targeted)

Software distribution (user-targeted, required)
(with Microsoft Entra integration)

Software distribution (user-targeted, available)
(all requirements)

BitLocker Management

Pull distribution point source

Windows in-place upgrade task sequence Note 2

Task sequence without a boot image, deployed with the option to Download all
content locally before starting task sequence Note 2

Task sequence without a boot image, deployed with either download option Note 2

Task sequence with a boot image, started from Software Center Note 2

Task sequence with a boot image, started from bootable media Note 2

Any other task sequence scenario Note 2

Content for PXE or multicast-enabled deployments

Client push

Automatic site assignment

Software approval requests

<!-- p.2731 -->

 Feature                                                                              Support

 Configuration Manager console

 Remote tools
                                                                                      Note 3

 Reporting website

 Wake on LAN

 macOS clients

 Peer cache

 On-premises MDM

 Alternate content providers
                                                                                      Note 4

 Content for App-V streaming applications

 Content for Microsoft 365 Apps updates

 Prestage content

                                                                              ﾉ   Expand table

 Key

    = This feature is supported with CMG by all supported versions of Configuration Manager

    (YYMM) = This feature is supported with CMG starting with version YYMM of Configuration
 Manager

    = This feature isn't supported with CMG

Support notes

Note 1: Support for endpoint protection

Clients that communicate via a CMG can immediately apply endpoint protection policies
without an active connection to Active Directory.

Note 2: Support for task sequences

<!-- p.2732 -->

For more information about support for deploying a task sequence to a client via the
CMG, see Deploy a task sequence over the internet.

Note 3: Support for remote tools

As announced at Microsoft Ignite 2021, a public preview of the new remote assistance
solution is now available in the Microsoft Intune admin center. This cloud-based tool
can help you more securely support users of Windows devices.

For more information, see the following resources:

     Remote Help: a new remote assistance tool from Microsoft (blog post)

     Enable remote help scenarios with Microsoft Intune (demo video)

     Use Remote Help with Intune and Configuration Manager

Note 4: Support for alternate content providers
Alternate content providers aren't supported to get content from a content-enabled
CMG. You can still use them on a client that communicates with a CMG and gets content
from other supported content locations.

   Tip

  Starting in version 2203, you can also configure the task sequence to allow token
  authentication with alternate content providers. For more information, see Task
  sequence variables: SMSTSAllowTokenAuthURLForACP.

Next steps
Next, plan how the design the CMG for the best performance at the appropriate scale:

  CMG performance and scale

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2733 -->

CMG performance and scale
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The supported scale and performance of the cloud management gateway (CMG) is
based on the number of devices that you expect to simultaneously connect to the
service. Use the information in this article to determine how many of the following
components you need in your environment for the best performance at the appropriate
scale:

         CMG cloud service
         Virtual machine instances for each CMG
         CMG connection point site system on your internal network

  ７ Note

  Sizing guidance for management points and software update points doesn't
  change whether they service on-premises or internet-based clients. For more
  information, see Size and scale numbers.

Size and scale for CMG
Unless otherwise noted, this guidance is the same for all deployment models and VM
sizes.

         You can install multiple instances of the cloud management gateway (CMG) at
         primary sites, or the central administration site (CAS).

            Tip

           In a hierarchy, create the CMG at the CAS.

         One CMG supports up to 16 virtual machine (VM) instances in the Azure cloud
         service.

         Simultaneous client connections per each CMG VM instance depend upon the
         deployment model and VM size. When the CMG is under high load with more than
         the supported number of clients, it still handles requests but there may be delay.

<!-- p.2734 -->

       Virtual machine scale-set (version 2107 and later)
           Lab (B2s): 10
           Standard (A2_v2): 6,000
           Large (A4_v2): 10,000

           ） Important

           The Lab (B2s) size VM is only intended for lab testing and small proof-of-
           concept environments. They aren't intended for production use with the
           CMG. The B2s VMs are low cost and low performing. The Configuration
           Manager technical preview branch only supports 10 clients, which is why
           this size supports that number of clients.

       Virtual machine scale set (version 2010 and 2103 for Cloud Service Provider
       (CSP) subscriptions): 2,000

       Cloud service (classic) (version 2111 and earlier): 6,000

           ） Important

           Starting in version 2203, the option to deploy a CMG as a cloud service
           (classic) is removed. All CMG deployments should use a virtual machine
           scale set. For more information, see Removed and deprecated features.

Size and scale for CMG connection point
This guidance is the same for all deployment models and VM sizes.

     You can install multiple instances of the CMG connection point at primary sites.

     One CMG connection point can support a CMG with up to four VM instances. If the
     CMG has more than four VM instances, add a second CMG connection point for
     load balancing. A CMG with 16 VM instances should be linked with four CMG
     connection points.

  ７ Note

  When considering hardware requirements for the CMG connection point, see
  Recommended hardware for remote site system servers.

<!-- p.2735 -->

Improve performance
The following recommendations can help you improve CMG performance:

     The connection between the Configuration Manager client and the CMG isn't
     region-aware. Client communication is largely unaffected by latency and
     geographic separation. It's generally not necessary to deploy multiple CMG for the
     purposes of geo-proximity. Deploy the CMG at the top-level site in your hierarchy.
     To increase scale, add VM instances.

     For high availability of the service, create a CMG with at least two VM instances
     and two CMG connection points per site.

     Scale the CMG to support more clients by adding more VM instances. The Azure
     load balancer controls client connections to the service.

     Create more CMG connection points to distribute the load among them. The CMG
     distributes the traffic to its connecting CMG connection points in a round-robin
     fashion.

  ７ Note

  The CMG connection point creates a TCP connection to the management point for
  each client. While Configuration Manager has no hard limit on the number of
  clients for a CMG connection point, Windows Server has a default maximum TCP
  dynamic port range of 16,384. If a Configuration Manager site manages more than
  16,384 clients with a single CMG connection point, add another site system or
  increase the Windows Server limit. All clients maintain a channel for client
  notifications, which holds a port open on the CMG connection point. For more
  information on how to increase this limit, see Microsoft Support article 929851      .

Content performance
As with any distribution point design, consider the following factors for a content-
enabled CMG:

     Number of concurrent client connections
     The size of the content that clients download
     The length of time allowed to meet your business requirements

Depending upon your design, if clients have the option of more than one CMG for any
given content, then they naturally randomize across those cloud sources. If you only

<!-- p.2736 -->

distribute a certain piece of content to a single CMG, and a large number of clients try
to download this content at the same time, it puts higher load on that single CMG.
Adding another CMG includes a separate Azure storage service. For more information
on how the client communicates with the CMG components and downloads content,
see Data flow.

  ７ Note

  The Azure storage service supports 500 requests per second for a single file.
  Performance testing of a single cloud-based content source supported distribution
  of a single 100-MB file to 50,000 clients in 24 hours.

Next steps
Next, understand the costs associated with operating an Azure service for the CMG:

  Cost of CMG

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2737 -->

Cost of CMG
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The cloud management gateway (CMG) in Configuration Manager uses several
components in Microsoft Azure. These components incur charges to the Azure
subscription account. Some costs are fixed, but some vary depending upon usage.

  ） Important

  The following cost information is for estimating purposes only. Your environment
  may have other variables that affect the overall cost of using CMG.

To help determine potential costs, use the following Azure resources:

      Azure pricing calculator

        ７ Note

        Virtual machine costs vary by region.

      Azure bandwidth pricing details

        ７ Note

        Pricing for data transfer is tiered. The more you use, the less you pay per
        gigabyte.

Compute costs
CMG uses Azure platform as a service (PaaS), which uses virtual machines (VMs). These
VMs incur compute costs. The specific type to use when estimating costs depends upon
which deployment method you use.

  ７ Note

  Although CMG is built on Azure PaaS, CMG is a software as a serice (SaaS) solution
  provided and maintained by Microsoft. CMG resources are added to customer

<!-- p.2738 -->

  Azure subscriptions so that consumption costs can be directly monitored and
  accounted for by the customer.

Virtual machine scale set
When you deploy the CMG as a virtual machine scale set, the following factors affect the
cost of the service:

     In version 2107 and later, you can configure the VM size:
        Lab (B2s)
        Standard (A2_v2)
        Large (A4_v2)

        ） Important

        The Lab (B2s) size VM is only intended for lab testing and small proof-of-
        concept environments. It isn't intended for production use with the CMG. The
        B2s VMs are low cost and low performing.

     You can change the VM size after you deploy the CMG. This action updates the
     Azure service to use a new VM.

     In version 2103 and earlier, the CMG uses a Standard A2_v2 VM. The VM size isn't
     configurable. To change the VM size, you need to Redeploy the service.

     You select how many VM instances support the CMG. One is the default, and 16 is
     the maximum. This number is set when you create the CMG, but you can change it
     afterwards to scale the service as needed.

     For more information on how many VMs you need to support your clients, see
     CMG performance and scale.

Virtual machine

  ） Important

  Starting in version 2203, the option to deploy a CMG as a cloud service (classic) is
  removed. All CMG deployments should use a virtual machine scale set. For more
  information, see Removed and deprecated features.

<!-- p.2739 -->

If you deployed the CMG as a classic cloud service, when estimating cost, this
deployment method replaces the virtual machine scale set. The specific details are
otherwise the same. With this deployment method, it uses a Standard A2_v2 VM. The
VM size isn't configurable. The cost difference between a virtual machine and a virtual
machine scale set should be negligible, but may vary by Azure region.

Outbound data transfer
     Charges are based on data flowing out of Azure, otherwise referred to as egress or
     download.

     CMG data flows out of Azure include policy to the client, client notifications, and
     client responses that the CMG forwards to the site. These responses include
     inventory reports, status messages, and compliance status.

     Even without any clients communicating with a CMG, some background
     communication causes network traffic between the CMG and the on-premises site.

     View the Outbound data transfer (GB) in the Configuration Manager console. For
     more information, see Monitor clients on CMG.

     For estimating purposes only, expect approximately 100-300 MB per client per
     month for internet-based clients. The lower estimate is for a default client
     configuration. The upper estimate is for a more aggressive client configuration.
     Your actual usage may vary depending upon how you configure client settings.

       ７ Note

       Other administrative actions can increase the amount of outbound data
       transfer from Azure. For example, deployments for software updates or
       applications.

     Internet-based clients get Microsoft software update content from Windows
     Update at no charge. Don't distribute update packages with Microsoft update
     content to a content-enabled CMG. If you do distribute software update packages
     to your cloud content sources, you may incur storage and data egress costs.

     Misconfiguration of the CMG option to Verify client certificate revocation can
     cause more traffic from clients to the CMG. This other traffic can increase the Azure
     egress data, which can increase your Azure costs. For more information, see
     Publish the certificate revocation list.

<!-- p.2740 -->

   Tip

  Any data flows into Azure are free. These flows are otherwise referred to as ingress
  or upload. When you distribute content from the site to the content-enabled CMG,
  you're uploading the content to Azure.

Content storage
     Internet-based clients get Microsoft software update content from Windows
     Update at no charge. Don't distribute update packages with Microsoft update
     content to a content-enabled CMG. If you do distribute software update packages
     to your cloud content sources, you may incur storage and data egress costs.

  ７ Note

  The cloud-based distribution point (CDP) is deprecated. Starting in version 2107,
  you can't create new CDP instances. To provide content to internet-based devices,
  enable the CMG to distribute content.

     CMG uses Azure locally redundant storage (LRS). For more information, see Locally
     redundant storage.

     For any other necessary content, distribute it to a content-enabled CMG. This other
     content includes applications or third-party software updates.

       ７ Note

       If you enable the client setting to Download delta content when available,
       the content for third-party updates won't download to clients.

Other costs
Each distinct CMG has one Basic (ARM) dynamic IP address. If you add other VMs to a
CMG, it doesn't increase the number of these IP addresses. For more information, see IP
addresses pricing   .

If you deploy the CMG as a virtual machine scale set, it uses Azure Key Vault. The CMG
usage of Key Vault is low, significantly less than 10,000 operations per month. For more
information, see Key Vault pricing   .

<!-- p.2741 -->

If you get a CMG server authentication certificate from a public provider, there's
generally a cost associated with this certificate. For more information, see CMG server
authentication certificate.

Control and monitor
Configuration Manager includes the following options to help control costs and monitor
data access:

     Control and monitor the amount of content that you store in a cloud service.

     Configure Configuration Manager to alert you when thresholds for client
     downloads meet or exceed monthly limits.

For more information, see Monitor CMG.

To help reduce the number of data transfers from cloud-based sources by clients, use
one of the following peer caching technologies:

     Configuration Manager peer cache

     Windows Delivery Optimization

     Windows BranchCache

        ７ Note

        To enable a content-enabled CMG to use Windows BranchCache, install the
        BranchCache feature on the site server. For more information, see Set up
        CMG: BranchCache

For more information, see Fundamental concepts for content management.

Next steps
Now that you have your CMG design, understand the supported configurations and
cost, you're ready to set up the CMG:

 Set up checklist for cloud management gateway

Feedback

<!-- p.2742 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2743 -->

Set up checklist for CMG
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

Before you deploy a cloud management gateway (CMG), use this article to understand
the setup process. Also make sure you have all of the prerequisites ready to get started.

First, develop your design and plan for implementing a CMG in your environment. For
more information, see Plan for cloud management gateway. Use that section of articles
to determine your CMG design.

The overall CMG setup process is divided into the following five main parts:

   1. Get the CMG server authentication certificate: The CMG uses HTTPS for secure
      client communication over the public internet. You can get a certificate from a
      public provider, or issue one from your public key infrastructure (PKI).

   2. Configure Microsoft Entra ID: Configuration Manager requires app registrations in
      Microsoft Entra ID. You can let Configuration Manager create them, or an Azure
      administrator can pre-create the registrations.

   3. Configure client authentication: Because clients communicate across the internet,
      Configuration Manager requires more security for this channel. You can use
      Microsoft Entra ID, PKI certificates, or token-based authentication from the site
      server.

   4. Set up the CMG: This step also includes configuring the site, and adding the CMG
      connection point site system role.

   5. Configure clients to use the CMG.

The other articles in this section step through each part of the process.

Terminology
The following terms are used in the context of setting up a CMG. They're defined here
for clarity.

      Microsoft Entra ID tenant: The directory of user accounts and app registrations.
      One tenant can have multiple subscriptions.

<!-- p.2744 -->

     Azure subscription: A subscription separates billing, resources, and services. It's
     associated with a single tenant.

        Tip

       For more information, see Subscriptions, licenses, accounts, and tenants for
       Microsoft's cloud offerings.

     Azure resource group: A container that holds related resources for an Azure
     solution. The resource group includes those resources that you want to manage as
     a group. You decide which resources belong in a resource group based on what
     makes the most sense for your organization. For more information, see Resource
     groups.

     CMG service name: The common name (CN) of the CMG server authentication
     certificate. Clients and the CMG connection point site system role communicate
     with this service name. For example, GraniteFalls.Contoso.Com or
     GraniteFalls.WestUS.CloudApp.Azure.Com .

     CMG deployment name: The first part of the service name plus the Azure location
     for the cloud service deployment. The cloud service manager component of the
     service connection point uses this name when it deploys the CMG in Azure. The
     deployment name is always in an Azure domain. The Azure location depends upon
     the deployment method, for example:
        Virtual machine scale set: GraniteFalls.WestUS.CloudApp.Azure.Com
        Classic deployment: GraniteFalls.CloudApp.Net

Checklist
Use the following checklist to make sure you have the necessary information and
prerequisites to create a CMG:

     The Azure environment to use. For example, the Azure Public Cloud or the Azure
     US Government Cloud.

     The Azure region for this CMG deployment.

     How many VM instances you need for scale and redundancy.

     An Azure application developer, cloud application administrator, application
     administrator, or global administrator role to register apps in Microsoft Entra ID.

<!-- p.2745 -->

     An Azure subscription owner role for when you create the CMG in Azure.

     At least one existing site system server on which you plan to add the CMG
     connection point role.

     Review the internet access requirements to make sure each required services can
     be reached.

     Enable this optional feature.

You'll set up other prerequisite components during the next steps in the process.

Automate with PowerShell
Optionally, you can automate aspects of the CMG setup using PowerShell. While some
cmdlets were available in earlier versions, version 2010 includes new cmdlets and
significant improvements to existing cmdlets.

For example, an Azure administrator first creates the two required apps in Microsoft
Entra ID. Then you write a script that uses the following cmdlets to deploy a CMG:

   1. Import-CMAADServerApplication: Create the Microsoft Entra server app definition
     in Configuration Manager.
   2. Import-CMAADClientApplication: Create the Microsoft Entra client app definition
     in Configuration Manager.
   3. Use Get-CMAADApplication to get the app objects, and then pass to New-
     CMCloudManagementAzureService to create the Azure service connection in
     Configuration Manager.
   4. New-CMCloudManagementGateway: Create the CMG service in Azure.
   5. Add-CMCloudManagementGatewayConnectionPoint: Create the CMG
     connection point site system.

You can use these cmdlets to automate the creation, configuration, and management of
the CMG service and Microsoft Entra requirements.

Microsoft Entra app definitions in Configuration Manager:

     Get-CMAADApplication
     Import-CMAADClientApplication
     Import-CMAADServerApplication

The Cloud Management Azure service in Configuration Manager:

     New-CMCloudManagementAzureService

<!-- p.2746 -->

     Set-CMCloudManagementAzureService
     Get-CMAzureService
     Remove-CMAzureService

The cloud management gateway service in Configuration Manager:

     Get-CMCloudManagementGateway
     New-CMCloudManagementGateway
     Remove-CMCloudManagementGateway
     Set-CMCloudManagementGateway
     Start-CMCloudManagementGateway
     Stop-CMCloudManagementGateway

The CMG connection point site system role:

     Add-CMCloudManagementGatewayConnectionPoint
     Get-CMCloudManagementGatewayConnectionPoint
     Remove-CMCloudManagementGatewayConnectionPoint
     Set-CMCloudManagementGatewayConnectionPoint

Next steps
Get started with your CMG setup by getting a server authentication certificate:

  CMG server authentication certificate

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2747 -->

CMG server authentication certificate
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The first step when you set up a cloud management gateway (CMG) is to get the server
authentication certificate. The CMG creates an HTTPS service to which internet-based
clients connect. The server requires a server authentication certificate to build the secure
channel. You can acquire a certificate for this purpose from a public provider, or issue it
from your public key infrastructure (PKI).

When you create the CMG in the Configuration Manager console, you provide this
certificate. The common name (CN) of this certificate defines the service name of the
CMG.

  ７ Note

  You may need additional certificates for clients and management points. These
  certificates are covered in the third step of the CMG setup process, Configure client
  authentication.

A reminder of some CMG terminology that's used in this article:

      Service name: The common name (CN) of the CMG server authentication
      certificate. Clients and the CMG connection point site system role communicate
      with this service name. For example, GraniteFalls.contoso.com or
       GraniteFalls.WestUS.CloudApp.Azure.Com .

      Deployment name: The first part of the service name plus the Azure location for
      the cloud service deployment. The cloud service manager component of the
      service connection point uses this name when it deploys the CMG in Azure. The
      deployment name is always in an Azure domain. The Azure location depends upon
      the deployment method, for example:
         Virtual machine scale set: GraniteFalls.WestUS.CloudApp.Azure.Com
         Classic deployment: GraniteFalls.CloudApp.Net

        ） Important

        This article uses examples with a virtual machine scale set as the
        recommended deployment method in version 2107 and later. If you use a

<!-- p.2748 -->

        classic deployment, note the difference as you read this article and prepare
        the server authentication certificate.

Choose the certificate type
First, decide where you want to get the certificate. There are several factors to consider.

Clients must trust the CMG server authentication certificate to establish the HTTPS
channel with the CMG service. There are two methods to accomplish this trust:

   1. Use a certificate from a public and globally trusted certificate provider.

              Windows clients include trusted root certificate authorities (CAs) from these
              providers. By using a certificate issued by one of these providers, your clients
              automatically trust it.

              There's a cost associated with this certificate, which is specific to the provider.

   2. Use a certificate issued by an enterprise CA from your public key infrastructure
     (PKI).

              Most enterprise PKI implementations add the trusted root CAs to Windows
              clients. For example, if you use Active Directory Certificate Services with
              group policy. If you issue the CMG server authentication certificate from a CA
              that your clients don't automatically trust, add the CA trusted root certificate
              to internet-based clients.

              If you plan to install the Configuration Manager client from Intune, you can
              also use Intune certificate profiles to provision certificates on clients. For
              more information, see Configure a certificate profile.

              Your organization may have an internal cost to issue certificates, but there are
              generally no external costs associated with this certificate.

  ） Important

  Before you get this certificate, make sure the service name is globally unique for
  the cloud service and storage account. Also make sure the name uses supported
  characters. For more information, see Globally unique name.

Summary comparison of certificate types

<!-- p.2749 -->

                                                                             ﾉ   Expand table

                Public provider            Enterprise PKI

 Client trust   Trusted in Windows by      Automatic with some implementations, otherwise
                default                    need to deploy

 Cost           Yes                        Not typical

 Service        GraniteFalls.contoso.com   GraniteFalls.contoso.com or
 name                                      GraniteFalls.WestUS.CloudApp.Azure.Com
 example

 DNS            Yes                        No for Azure domain service name
 CNAME                                     ( GraniteFalls.WestUS.CloudApp.Azure.Com )
 required

  ７ Note

  The CMG server authentication certificate supports wildcards. Some certificate
  authorities issue certificates using a wildcard character for the service name prefix.
  For example, *.contoso.com . Some organizations use wildcard certificates to
  simplify their PKI and reduce maintenance costs.

  For more information on how to use a wildcard certificate with a CMG, see Set up a
  CMG.

Globally unique name
This certificate requires a globally unique name to identify the service in Azure. Before
you request a certificate, confirm that the Azure deployment name you want is unique.
For example, GraniteFalls.WestUS.CloudApp.Azure.Com .

Virtual machine scale set
   1. Sign in to the Azure portal .

   2. From the Azure portal home page, select Create a resource under Azure services.

   3. Search for Virtual machine scale set. Select Create.

   4. Select the Subscription and Resource group that you'll use for the CMG.

<!-- p.2750 -->

   5. In the Virtual machine scale set name field, type the prefix that you want. For
     example, GraniteFalls .

   6. Select the Region that you'll use for the CMG. For example, (US) West US.

The interface reflects whether the domain name is available or already in use by another
service.

  ） Important

  Don't create the service in the portal, just use this process to check the name
  availability.

Repeat this process for the Key Vault resource. The virtual machine scale set deployment
creates a key vault with the same name, which also needs to be globally unique.

Content-enabled CMG storage account
If you also enable the CMG for content, confirm that it's also a unique Azure storage
account name. If the CMG deployment name is unique, but the storage account isn't,
Configuration Manager fails to provision the service in Azure. Repeat the above process
in the Azure portal with the following changes:

     Search for Storage account.

     Test your name in the Storage account name field.

  ） Important

  The DNS name prefix should be 3 to 24 characters long, and contain numbers and
  lowercase letters only. Don't use special characters, like a dash ( - ). For example:
   granitefalls .

Issue the certificate
The CMG server authentication certificate supports the following configurations:

     2048-bit or 4096-bit key length

     This certificate supports key storage providers for certificate private keys (v3). For
     more information, see CNG v3 certificates overview.

<!-- p.2751 -->

Use a public provider certificate
A third-party certificate provider can't create a certificate for an Azure domain like
cloudapp.azure.com , because Microsoft owns those domains. You can only get a

certificate issued for a domain you own. The main reason for acquiring a certificate from
a third-party provider is that your clients already trust that provider's root certificate.

The specific process to get this certificate varies by provider. For more information,
contact your third-party certificate provider.

For the web server certificate common name (CN):

     You've made sure the deployment name is globally unique in Azure for the cloud
     service and storage account. For example,
      GraniteFalls.WestUS.CloudApp.Azure.Com .

     To determine the service name, append the deployment name prefix ( GraniteFalls )
     to your organization's domain name ( contoso.com ).

     Use this service name for the certificate common name (CN). For example,
      GraniteFalls.contoso.com .

Next, you need to create a DNS CNAME alias.

Use an enterprise PKI certificate
Issuing a web server certificate from your organization's PKI varies by product. The
instructions for Deploying the service certificate for cloud-based distribution points are
for Active Directory Certificate Services. This process generally applies for the CMG
server authentication certificate.

For the web server certificate common name (CN):

     You've made sure the deployment name is globally unique in Azure for the cloud
     service and storage account. For example,
      GraniteFalls.WestUS.CloudApp.Azure.Com .

     To determine the service name, you have two options:

        Use your domain name (recommended). Append the deployment name prefix
        ( GraniteFalls ) to your organization's domain name ( contoso.com ). For example,
         GraniteFalls.contoso.com . For this option, you also need to create a DNS

        CNAME alias.

<!-- p.2752 -->

        Use the Azure deployment name. This option doesn't require a DNS CNAME
        alias. For example:

           For the Azure public cloud: GraniteFalls.WestUS.CloudApp.Azure.Com .

           For the Azure US Government cloud: GraniteFalls.usgovcloudapp.net .

          ７ Note

          If the Azure deployment name changes, you'll need to redeploy the service
          to change this service name. For example, if your service name is in the
           cloudapp.net domain, you can't convert the classic cloud service CMG to a

          virtual machine scale set. If you use your domain name for the CMG service
          name, then you can update the DNS CNAME for the new deployment
          name.

     Use this service name for the certificate common name (CN).

Create a DNS CNAME alias
If the CMG service name uses your organization's domain name
( GraniteFalls.contoso.com ), you need to create a DNS canonical name record (CNAME).
This alias maps the service name to the deployment name.

Create a CNAME record in your organization's public DNS. The CMG service in Azure
and all clients that use it need to resolve the service name. For example:

     Contoso names their CMG GraniteFalls.

     The deployment name in Azure is GraniteFalls.WestUS.CloudApp.Azure.Com .

     In Contoso's public DNS contoso.com namespace, the DNS administrator creates a
     new CNAME record for the service name GraniteFalls.contoso.com to the Azure
     deployment name, GraniteFalls.WestUS.CloudApp.Azure.Com .

When you create the CMG, while the certificate has GraniteFalls.contoso.com as the
CN, Configuration Manager only extracts the service name prefix, for example:
GraniteFalls. It appends this prefix to the Azure service domain ( cloudapp.azure.com )
with the region ( westus ) to create the deployment name. For example,
GraniteFalls.WestUS.CloudApp.Azure.Com . The CNAME alias in the DNS namespace for

your domain ( contoso.com ) maps together these two FQDNs.

<!-- p.2753 -->

The Configuration Manager client policy includes the CMG service name,
GraniteFalls.contoso.com . The client resolves the service name via the CNAME alias to

the deployment name, GraniteFalls.WestUS.CloudApp.Azure.Com . It then can resolve the
IP address of the deployment name to communicate with the service in Azure.

Next steps
Continue your CMG setup by configuring Microsoft Entra ID:

  Configure Microsoft Entra ID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2754 -->

Configure Microsoft Entra ID for CMG
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

The second primary step to set up a cloud management gateway (CMG) is to integrate
the Configuration Manager site with your Microsoft Entra tenant. This integration allows
the site to authenticate with Microsoft Entra ID, which it uses to deploy and monitor the
CMG service. If you choose the Microsoft Entra authentication method for clients in the
next step, then this integration is a prerequisite for that authentication method.

   Tip

  This article provides prescriptive guidance to integrate the site specifically for the
  cloud management gateway. For more information on this process and other uses
  of the Azure Services node in the Configuration Manager console, see Configure
  Azure services.

When you integrate the site, you create app registrations in Microsoft Entra ID. The CMG
requires two app registrations:

      Web app (also referred to as a server app in Configuration Manager)
      Native app (also referred to as a client app in Configuration Manager)

There are two methods to create these apps, both of which require a global
administrator role in Microsoft Entra ID:

      Use Configuration Manager to automate the creation of the apps when you
      integrate the site.
      Manually create the apps in advance, and then import them when you integrate
      the site.

This article primarily follows the first method. For more information on the other
method, see Manually register Microsoft Entra apps for CMG.

Before you start, make sure you have a Microsoft Entra ID global administrator
available.

  ７ Note

  If you plan to import precreated app registrations, you first need to create them in
  Microsoft Entra ID. Start with the article to Manually register Microsoft Entra apps

<!-- p.2755 -->

  for CMG. Then return to this article to run the Azure Services wizard and import the
  apps to Configuration Manager.

Purpose of app registrations
These two Microsoft Entra app registrations represent the server and client side of the
CMG.

     The client app represents managed clients and users that connect to the CMG. It
     defines what resources they have access to within Azure, including the CMG itself.

     The server app represents the CMG components that are hosted in Azure. It defines
     what resources they have access to within Azure. The server app is used to
     facilitate authentication and authorization from managed clients, users, and the
     CMG connection point to the Azure-based CMG components. This communication
     includes traffic to on-premises management points and software update points,
     initial CMG provisioning in Azure, and Microsoft Entra discovery.

If clients use PKI-issued client authentication certificates, then the two client apps aren't
used for device-centric activity. For example, software distribution targeted to a device
collection. User-centric activity always uses these two app registrations for
authentication and authorization purposes.

Start the Azure Services wizard
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Cloud Services, and select the Azure Services node.

   2. On the Home tab of the ribbon, in the Azure Services* group, select Configure
     Azure Services.

   3. On the Azure Services page of the Azure Services Wizard:

       a. Specify a Name for the object in Configuration Manager. This name is only to
         identify the connection in Configuration Manager.

       b. Specify an optional Description to further identify this service connection.

       c. Select the Cloud Management service.

   4. On the App page of the Azure Services Wizard, select the Azure environment for
     your tenant:

<!-- p.2756 -->

        AzurePublicCloud: Your tenant is in the global Azure cloud.
        AzureUSGovernmentCloud: Your tenant is in the Azure US Government
        cloud.

Create the web (server) app registration
 1. On the App page of the Azure Services Wizard window, for the Web app, select
   Browse.

 2. In the Server App window, select Create to use Configuration Manager to automate
   the creation of the app.

 3. In the Create Server Application window, specify the following information:

        Application name: A friendly name for the app.

        HomePage URL: This value isn't used by Configuration Manager, but required
        by Microsoft Entra ID. By default this value is https://ConfigMgrService .

        App ID URI: This value needs to be unique in your Microsoft Entra tenant. It's
        in the access token used by the Configuration Manager client to request
        access to the service. By default this value is https://ConfigMgrService .
        Change the default to one of the following recommended formats:
             api://{tenantId}/{string} , for example, api://5e97358c-d99c-4558-af0c-

             de7774091dda/ConfigMgrService
             https://{verifiedCustomerDomain}/{string} , for example,

             https://contoso.onmicrosoft.com/ConfigMgrService

        Secret key validity period: choose either 1 year or 2 years from the drop-
        down list. One year is the default value.

        Microsoft Entra admin account: Select Sign in to authenticate to Microsoft
        Entra ID as a global administrator. Configuration Manager doesn't save these
        credentials. This persona doesn't require permissions in Configuration
        Manager, and doesn't need to be the same account that runs the Azure
        Services Wizard. After successfully authenticating to Azure, the page shows
        the Microsoft Entra tenant name for reference.

 4. Select OK to create the web app in Microsoft Entra ID and close the Create Server
   Application window.

 5. In the Server App window, make sure your new app is selected, then select OK to
   save and close the window.

<!-- p.2757 -->

 ７ Note

 Starting in Configuration Manager current branch version 2309, We have enhanced
 security of web (server) app for the creation of CMG. For new CMG creation, users
 can select tenant and the app name using the Microsoft Entra tenant name. After
 selecting tenant and app name the sign-in button appears, follow rest of the
 process as per the setup CMG.

 Pre-existing CMG customers must update their web server app by navigating to
 Microsoft Entra tenants node --> select the tenant --> select the server app -->
 click on "update application settings".

Create the native (client) app registration
 1. On the App page of the Azure Services Wizard window, for the Native Client app,
    select Browse.

 2. In the Client App window, select Create to use Configuration Manager to automate
    the creation of the app.

 3. In the Create Client Application window, specify the following information:

          Application name: A friendly name for the app.

          Microsoft Entra admin account: Select Sign in to authenticate to Microsoft
          Entra ID as a global administrator. Configuration Manager doesn't save these
          credentials. This persona doesn't require permissions in Configuration
          Manager, and doesn't need to be the same account that runs the Azure
          Services Wizard. After successfully authenticating to Azure, the page shows
          the Microsoft Entra tenant name for reference.

 4. Select OK to create the native app in Microsoft Entra ID and close the Create Client
    Application window.

 5. In the Client App window, make sure your new app is selected, then select OK to
    save and close the window.

Complete the Azure Services wizard
 1. In the Azure Services Wizard, confirm both the Web app and Native Client app
    values are complete. Select Next to continue.

<!-- p.2758 -->

   2. The Discovery page of the wizard is only necessary in some scenarios. It's optional
     when you onboard the site to Microsoft Entra ID, and not required to create the
     CMG. If you need it to support specific functionality in your environment, you can
     enable it later.

     For more information on the CMG scenarios that may require Microsoft Entra user
     discovery, see Configure client authentication: Microsoft Entra ID and Install clients
     using Microsoft Entra ID.

     For more information on this discovery method, see Configure Microsoft Entra user
     discovery.

   3. Review the settings and complete the wizard.

When the wizard closes, you'll see the new connection in the Azure Services node. You
can also view the tenant and app registrations in the Microsoft Entra tenants node of
the Configuration Manager console.

Disable Microsoft Entra authentication for non-device or
user tenants
If your devices are in a Microsoft Entra tenant that's separate from the tenant with a
subscription for the CMG compute resources, you can disable authentication for tenants
not associated with users and devices.

   1. Open the properties of the Cloud Management service.

   2. Switch to the Applications tab.

   3. Select the option to Disable Microsoft Entra authentication for this tenant.

For more information, see Configure Azure services.

Configure Azure resource providers
The CMG service requires that you register specific resource providers in your Azure
subscription. When you deploy the CMG to a virtual machine scale set, register the
following resource providers:

     Microsoft.KeyVault
     Microsoft.Storage
     Microsoft.Network
     Microsoft.Compute

<!-- p.2759 -->

  ７ Note

  If you previously deployed the CMG using a classic cloud service, your Azure
  subscription requires the following two resource providers:

       Microsoft.ClassicCompute
       Microsoft.Storage

  Starting in version 2203, the option to deploy a CMG as a cloud service (classic) is
  removed. All CMG deployments should use a virtual machine scale set. For more
  information, see Removed and deprecated features.

Your Microsoft Entra account needs permission to do the /register/action operation
for the resource provider. By default, the Contributor and Owner roles include this
permission.

The following steps summarize the process to register a resource provider. For more
information, see Azure resource providers and types.

   1. Sign in to the Azure portal .

   2. On the Azure portal menu, search for Subscriptions. Select it from the available
     options.

   3. Select the subscription you want to view.

   4. On the left menu, under Settings, select Resource providers.

   5. Find the resource provider you want to register, and select Register. To maintain
     least privileges in your subscription, only register those resource providers that
     you're ready to use.

Automate with PowerShell
You can optionally automate aspects of these configurations using PowerShell.

   1. Use the Import-CMAADServerApplication cmdlet to define the Microsoft Entra
     web/server app in Configuration Manager.

   2. Use the Import-CMAADClientApplication cmdlet to define the Microsoft Entra
     native/client app in Configuration Manager.

   3. Use the Get-CMAADApplication cmdlet to get the imported app objects.

<!-- p.2760 -->

   4. Then pass the app objects to the New-CMCloudManagementAzureService cmdlet
     to create the Azure service for Cloud Management in Configuration Manager.

Next steps
Continue your CMG setup by deciding which type of client authentication to use:

  Configure client authentication

Feedback
Was this page helpful?      Yes    No

Provide product feedback
