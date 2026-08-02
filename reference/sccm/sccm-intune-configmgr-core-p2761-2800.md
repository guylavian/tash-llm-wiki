---
title: "Core infrastructure documentation — pages 2761-2800"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2761-2800
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2761-2800
family: sccm
documentKind: "doc"
abstract: "Configure client authentication for cloud management gateway ﾃ Summarize this article for me Applies to: Configuration Manager (current branch) The next step in the setup of a cloud management gateway (CMG) is to configure how clients authenticate. Because these clients are pote"
---

# Core infrastructure documentation — pages 2761-2800

<!-- p.2761 -->

Configure client authentication for cloud
management gateway
ﾃ   Summarize this article for me

Applies to: Configuration Manager (current branch)

The next step in the setup of a cloud management gateway (CMG) is to configure how clients
authenticate. Because these clients are potentially connecting to the service from the untrusted
public internet, they have a higher authentication requirement. There are three options:

     Microsoft Entra ID
     PKI certificates
     Configuration Manager site-issued tokens

This article describes how to configure each of these options. For more foundational
information, see Plan for CMG client authentication methods.

Microsoft Entra ID
If your internet-based devices are running Windows 10 or later, use Microsoft Entra modern
authentication with the CMG. This authentication method is the only one that enables user-
centric scenarios.

This authentication method requires the following configurations:

     The devices need to be either cloud domain-joined or Microsoft Entra hybrid joined, and
     the user also needs a Microsoft Entra identity.

         Tip

        To check if a device is cloud-joined, run dsregcmd.exe /status in a command
        prompt. If the device is Microsoft Entra joined or hybrid-joined, the AzureAdjoined
        field in the results shows YES. For more information, see dsregcmd command -
        device state.

     One of the primary requirements for using Microsoft Entra authentication for internet-
     based clients with a CMG is to integrate the site with Microsoft Entra ID. You already
     completed that action in the prior step.

     There are a few other requirements, depending upon your environment:
        Enable user discovery methods for hybrid identities

<!-- p.2762 -->

         Enable ASP.NET 4.5 on the management point
         Configure client settings

For more information on these prerequisites, see Install clients using Microsoft Entra ID.

PKI certificate
Use these steps if you have a public key infrastructure (PKI) that can issue client authentication
certificates to devices.

This certificate may be required on the CMG connection point. For more information, see CMG
connection point.

Issue the certificate
Create and issue this certificate from your PKI, which is outside of the context of Configuration
Manager. For example, you can use Active Directory Certificate Services and group policy to
automatically issue client authentication certificates to domain-joined devices. For more
information, see Example deployment of PKI certificates: Deploy the client certificate.

The CMG client authentication certificate supports the following configurations:

      2048-bit or 4096-bit key length

      This certificate supports key storage providers for certificate private keys (v3). For more
      information, see CNG v3 certificates overview.

Export the client certificate's trusted root
The CMG has to trust the client authentication certificates to establish the HTTPS channel with
clients. To accomplish this trust, export the trusted root certificate chain. Then supply these
certificates when you create the CMG in the Configuration Manager console.

Make sure to export all certificates in the trust chain. For example, if the client authentication
certificate is issued by an intermediate CA, export both the intermediate and root CA
certificates.

  ７ Note

  When clients use either Microsoft Entra ID or tokens for authentication, this certificate isn't
  required. Export this certificate only when clients are not joined to Entra ID and instead
  use PKI certificates for authentication.

<!-- p.2763 -->

After you issue a client authentication certificate to a computer, use this process on that
computer to export the trusted root certificate.

   1. Open the Start menu. Type "run" to open the Run window. Open mmc .

   2. From the File menu, choose Add/Remove Snap-in....

   3. In the Add or Remove Snap-ins dialog box, select Certificates, then select Add.

      a. In the Certificates snap-in dialog box, select Computer account, then select Next.

     b. In the Select Computer dialog box, select Local computer, then select Finish.

      c. In the Add or Remove Snap-ins dialog box, select OK.

   4. Expand Certificates, expand Personal, and select Certificates.

   5. Select a certificate whose Intended Purpose is Client Authentication.

      a. From the Action menu, select Open.

     b. Go to the Certification Path tab.

      c. Select the next certificate up the chain, and select View Certificate.

   6. On this new Certificate dialog box, go to the Details tab. Select Copy to File....

   7. Complete the Certificate Export Wizard using the default certificate format, DER encoded
     binary X.509 (.CER). Make note of the name and location of the exported certificate.

   8. Export all of the certificates in the certification path of the original client authentication
     certificate. Make note of which exported certificates are intermediate CAs, and which ones
     are trusted root CAs.

CMG connection point
To securely forward client requests, the CMG connection point requires a secure connection
with the management point. If you're using PKI client authentication, and the internet-enabled
management point is HTTPS, issue a client authentication certificate to the site system server
with the CMG connection point role.

  ７ Note

  The CMG connection point doesn't require a client authentication certificate in the
  following scenarios:

<!-- p.2764 -->

        Clients use Microsoft Entra authentication.

     Clients use Configuration Manager token-based authentication.

       The Management Points enabled for CMG traffic are configured for Enhanced HTTP.

For more information, see Enable management point for HTTPS.

Authentication Options
Management Points enabled for CMG traffic can be either EHTTP or HTTPS. If you can't join
devices to Microsoft Entra ID or use PKI client authentication certificates, then use
Configuration Manager token-based authentication. For more information, or to create a bulk
registration token, see Token-based authentication for cloud management gateway.

Enable management point for HTTPS
When you enable Enhanced HTTP, the site server generates a self-signed certificate named
SMS Role SSL Certificate. This certificate is issued by the root SMS Issuing certificate. The
management point adds this certificate to the IIS Default Web site bound to port 443.

With this option, internal clients can continue to communicate with the management point
without any additional configuration. Internet-based clients using Microsoft Entra ID can
securely communicate through the CMG with any management point enabled for EHTTP.

For more information, see Enhanced HTTP.

Configure the management point for HTTPS
If Entra ID authentication is not available, configure a management point for HTTPS. First issue
it a web server certificate, then enable the role for HTTPS.

   1. Create and issue a web server certificate from your PKI or a third-party provider, which
     are outside of the context of Configuration Manager. For example, use Active Directory
     Certificate Services and group policy to issue a web server certificate to the site system
     server with the management point role. For more information, see the following articles:

           PKI certificate requirements
           Example deployment of PKI certificates: Deploy the web server certificate for site
           systems that run IIS

<!-- p.2765 -->

   2. On the properties of the management point role, set the client connections to HTTPS.

        Tip

       After you set up the CMG, you'll configure other settings for this management point.

If your environment has multiple management points, you don't have to enable them all for
CMG. Configure the CMG-enabled management points as Internet only. Then your on-
premises clients don't try to use them.

Management point client connection mode summary
These tables summarize whether the management point requires EHTTP or HTTPS, depending
upon the type of client. They use the following terms:

     Workgroup: The device isn't joined to a domain or Microsoft Entra ID, but has a client
     authentication certificate.
     AD domain-joined: You join the device to an on-premises Active Directory domain.
     Microsoft Entra joined: Also known as cloud domain-joined, you join the device to a
     Microsoft Entra tenant. For more information, see Microsoft Entra joined devices.
     Hybrid-joined: You join the device to your on-premises Active Directory and register it
     with your Microsoft Entra ID. For more information, see Microsoft Entra hybrid joined
     devices.
     HTTPS: On the management point properties, you set the client connections to HTTPS.
     E-HTTP: On the site properties, Communication Security tab, you set the site system
     settings to HTTPS or EHTTP, and you enable the option to Use Configuration Manager-
     generated certificates for HTTP site systems. You configure the management point for
     EHTTP, and the management point is ready for CMG communication.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP-only client
  communication are deprecated and the site must be configured for Enhanced HTTP. For
  more information, see Enable the site for HTTPS-only or enhanced HTTP.

For internet-based clients communicating with the CMG

Configure an on-premises management point to allow connections from the CMG with the
following client connection mode:

<!-- p.2766 -->

                                                                                ﾉ   Expand table

 Internet-based client                               Management point

 Workgroup Note 1                                    E-HTTP, HTTPS

 AD domain-joined Note 1                             E-HTTP, HTTPS

 Microsoft Entra joined                              E-HTTP, HTTPS

 Hybrid-joined                                       E-HTTP, HTTPS

  ７ Note

  Note 1: This configuration requires the client has a client authentication certificate, and
  only supports device-centric scenarios.

For on-premises clients communicating with the on-premises
management point

Configure an on-premises management point with the following client connection mode:

                                                                                ﾉ   Expand table

 On-premises client                                Management point

 Workgroup                                         EHTTP, HTTPS

 AD domain-joined                                  EHTTP, HTTPS

 Microsoft Entra joined                            EHTTP, HTTPS

 Hybrid-joined                                     EHTTP, HTTPS

  ７ Note

  On-premises AD domain-joined clients support both device- and user-centric scenarios
  communicating with an EHTTP or HTTPS management point.

Next steps
You're now ready to create the CMG in Configuration Manager:

<!-- p.2767 -->

 Set up CMG

Last updated on 02/11/2026

<!-- p.2768 -->

Set up CMG for Configuration Manager
Article • 10/09/2023

Applies to: Configuration Manager (current branch)

Once you have the prerequisites in place, you can start the process to set up a cloud
management gateway (CMG). Before you start this process, make sure you have the
necessary information and prerequisites to create a CMG. For more information, see Set
up checklist for CMG.

This step of the overall process includes the following actions:

      Use the Configuration Manager console to create the CMG service in Azure.
      Configure the primary site for client certificate authentication.
      Add the CMG connection point site system role.
      Configure the management point and software update point for CMG traffic.
      Configure boundary groups.

Set up a CMG

  ７ Note

  Deploying a CMG with a virtual machine scale set in Azure was first introduced in
  version 2010 as a pre-release feature. Beginning with version 2107, it's no longer a
  pre-release feature.

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

Do this procedure on the top-level site. That site is either a standalone primary site, or
the central administration site (CAS).

   1. In the Configuration Manager console, go to the Administration workspace,
      expand Cloud Services, and select Cloud Management Gateway.

   2. Select Create Cloud Management Gateway in the ribbon.

   3. On the General page of the wizard, first specify the Azure environment for this
      CMG:

            AzurePublicCloud: Create the service in the global Azure cloud.

<!-- p.2769 -->

       AzureUSGovernmentCloud: Create the service in the Azure US Government
       cloud.

4. Next choose how you want to deploy the CMG in Azure:

       Virtual machine scale set

          Starting in version 2203, virtual machine scale set is the only option.

          Starting in version 2107, this option is the recommended deployment
          method. Even if you have an existing CMG deployed with the cloud service
          (classic) method, deploy new CMG instances as a virtual machine scale set.

          In versions 2010 and 2103, you have to enable this pre-release feature to
          see it. In these releases, it's only intended for customers with a Cloud
          Solution Provider (CSP) subscription. If you already deployed a CMG with
          the cloud service (classic) method, this option is unavailable. For more
          information, see Plan for CMG: Virtual machine scale sets.

       Cloud service (classic)

          ） Important

          Starting in version 2203, the option to deploy a CMG as a cloud service
          (classic) is removed. All CMG deployments should use a virtual machine
          scale set. For more information, see Removed and deprecated features.

          In version 2107 and later, only use this option if you can't deploy with a
          virtual machine scale set because of one of the limitations.

          In versions 2010 and 2103, most customers should use this deployment
          method.

5. Starting in version 2309, select Microsoft Entra tenant name, Microsoft Entra app
  name automatically populates. Select Sign in. Authenticate with an Azure
  Subscription Owner account. If you own multiple subscriptions, select the
  Subscription ID of the subscription you want to use.

    ７ Note

    Starting in version 2309, We have deprecated the use of first party app for the
    creation of CMG. Now, CMG uses a third party server app to get bearer
    tokens.

<!-- p.2770 -->

6. In versions 2303 and below, Select Sign in. Authenticate with an Azure
  Subscription Owner account. The wizard automatically populates the remaining
  fields from the information stored during the Microsoft Entra integration
  prerequisite. If you own multiple subscriptions, select the Subscription ID of the
  subscription you want to use.

  Select Next, and wait as the site tests the connection to Azure.

7. On the Settings page of the wizard, first Browse to the .PFX file for the CMG server
  authentication certificate (Certificate file). The common name from this certificate
  is used to populate the Service name and Deployment name fields.

  If you use a wildcard certificate, replace the asterisk ( * ) in the Service name field
  with the globally unique deployment name prefix for your CMG.

  a. Optionally specify a Description to further identify this CMG in the
     Configuration Manager console.

  b. Select an Azure Region for this CMG. The list of available regions may vary
     based on the selected subscription.

   c. Select a Resource Group option:

          If you choose Use existing, then select an existing resource group from
          the list. This resource group needs to already exist in the same region you
          selected for the CMG. If you select an existing resource group, and it's in a
          different region than the previously selected region, the CMG will fail to
          deploy.

          If you choose Create new, then enter the new resource group name.

  d. By default, the VM Size is Standard (A2_V2). Select another option as your
     design specifies. For example, Large (A4_v2) for increased client capacity per
     VM, or Lab (B2s) in a small test environment.

       ） Important

       The Lab (B2s) size VM is only intended for lab testing and small proof-of-
       concept environments. For example, with the Configuration Manager
       technical preview branch. The B2s VMs aren't intended for production use
       with the CMG. They are low cost and low performing.

  e. In the VM Instance field, enter the number of VMs for this service. The default is
     one, but you can scale up to 16 VMs per CMG.

<!-- p.2771 -->

       f. If you're using client authentication certificates, select Certificates to add
         trusted root certificates. Add all of the certificates in the trust chain.

            ７ Note

            A trusted root certificate isn't required when using Microsoft Entra ID or
            site-issued tokens for client authentication.

       g. By default, the wizard enables the option to Verify Client Certificate
         Revocation. A certificate revocation list (CRL) must be publicly published for this
         verification to work. For more information, see Publish the certificate revocation
         list.

       h. By default, the wizard enables the option to Enforce TLS 1.2. This setting
         requires the Azure VM to use the TLS 1.2 encryption protocol. It doesn't apply
         to any on-premises Configuration Manager site servers or clients. Starting in
         version 2107 with the update rollup, this setting also applies to the CMG
         storage account. For more information, see How to enable TLS 1.2.

       i. By default, the wizard enables the option to Allow CMG to function as a cloud
         distribution point and serve content from Azure storage. If you plan on
         targeting deployments with content to clients, you need to configure the CMG
         to serve content.

   8. Next is the Alerts page of the wizard. To monitor CMG traffic with a 14-day
     threshold, enable the threshold alert. Then specify the threshold, and the
     percentage at which to raise the different alert levels. You can also enable a
     storage alert threshold. Choose Next when you're done.

   9. Review the settings, and complete the wizard.

Configuration Manager starts to set up the service. The amount of time it takes to
completely provision the service in Azure is dependent upon the settings that you
specified. To determine when the service is ready, view the Status column for the new
CMG.

To troubleshoot CMG deployments, use CloudMgr.log and CMGSetup.log. For more
information, see Monitor CMG.

   Tip

  You can also use the PowerShell cmdlet New-CMCloudManagementGateway for
  this process. Optionally use this cmdlet to create the CMG service. For more

<!-- p.2772 -->

  information, see New-CMCloudManagementGateway.

Configure primary site for client certificate
authentication
If you're using client authentication certificates for clients to authenticate with the CMG,
follow this procedure to configure each primary site.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select Sites.

   2. Select the primary site to which your internet-based clients are assigned, and
     choose Properties.

   3. Switch to the Communication Security tab, and select Use PKI client certificate
     (client authentication) when available.

   4. If you don't publish a CRL, disable the following option: Clients check the
     certificate revocation list (CRL) for site systems.

Add the CMG connection point
The CMG connection point is the site system role that's required for communication
from your on-premises Configuration Manager deployment to the cloud-based CMG.
Before you start this process, you should have already developed a plan for the role, and
identified at least one existing site system server. For more information, see Plan for the
CMG.

To add the CMG connection point, the following steps summarize the instructions to
install site system roles:

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Servers and Site System Roles node.

   2. Select an existing site server to which you want to add this role. In the ribbon, on
     the Home tab, select Add Site System Roles.

   3. On the System Role Selection screen, choose Cloud management gateway
     connection point, and then select Next. Choose the Cloud management gateway
     name to which this server connects. The wizard will show the region for the
     selected CMG.

<!-- p.2773 -->

  ） Important

  If you're using client authentication certificates, the CMG connection point needs
  this certificate. For more information, see client authentication certificate.

To troubleshoot CMG service health, use CMGService.log and
SMS_Cloud_ProxyConnector.log. For more information, see Log files.

   Tip

  Optionally, you can also use the PowerShell cmdlet Add-
  CMCloudManagementGatewayConnectionPoint to add the CMG connection point
  role to a site system server.

  For more information, see Add-CMCloudManagementGatewayConnectionPoint.

Configure client-facing roles for CMG traffic
Configure the management point and software update point site systems to accept
CMG traffic. Do this procedure on the primary site, for all management points and
software update points that service internet-based clients.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Servers and Site System Roles node. On
     the Home tab of the ribbon, in the View group, select Servers with Role. Then
     select Management point from the list.

   2. Select the site system server you want to configure for CMG traffic. Select the
     Management point role in the details pane, and then in the Site Role group of the
     ribbon, select Properties.

   3. In the Management point properties sheet, under Client Connections select Allow
     Configuration Manager cloud management gateway traffic.

     Depending upon your CMG design and Configuration Manager version, you may
     need to enable the HTTPS option. For more information, see Enable management
     point for HTTPS.

   4. Select OK to close the management point properties window.

Repeat these steps for other management points as needed, and for any software
update points.

<!-- p.2774 -->

Configure boundary groups
You can associate a CMG with a boundary group. This configuration allows clients to use
the CMG for client communication according to boundary group relationships. This
configuration is beneficial for VPN or branch office clients where it might be better to
manage them via a CMG than over the VPN or WAN connection. If you enable the
option to Prefer cloud-based sources over on-premises sources then clients will prefer
the CMG for both policy and content.

For more information on boundary groups, see Configure boundary groups.

When you create or configure a boundary group, on the References tab, add a cloud
management gateway. This action associates the CMG with this boundary group.

BranchCache
To enable a content-enabled CMG to use Windows BranchCache, install the
BranchCache feature on the site server.

     If the site server has an on-premises distribution point site system role, configure
     the option in that role's properties to Enable and configure BranchCache. For
     more information, see Configure a distribution point.

     If the site server doesn't have a distribution point role, install the BranchCache
     feature in Windows. For more information, see Install the BranchCache feature.

If you've already distributed content to a CMG, and then decide to enable BranchCache,
first install the feature. Then redistribute the content to the CMG.

Distribute and manage content
Distribute content to the content-enabled CMG the same as any other distribution
point. The management point doesn't include the CMG in the list of content locations
unless it has the content that clients request. For more information, see Distribute and
manage content.

Manage content on a CMG the same as any other distribution point. These actions
include assigning it to a distribution point group and managing content packages. For
more information, see Install and configure distribution points.

Next steps

<!-- p.2775 -->

Continue your CMG setup by configuring clients for CMG:

  Configure clients for CMG

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2776 -->

Configure clients for cloud management
gateway
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

Once the cloud management gateway (CMG) and the supporting site system roles are
operational, you may need to make configuration changes on Configuration Manager
clients.

Clients that can communicate with the management point automatically get the location
of the CMG service on the next location request. The polling cycle for location requests
is every 24 hours. If you don't want to wait for the normally scheduled location request,
you can force the request. To force the request, restart the SMS Agent Host service
(ccmexec.exe) on the computer.

For devices that aren't connected to the internal network, there are several options to
configure them with a CMG location. For more information, see Install off-premises
clients using a CMG.

  ７ Note

  By default all clients receive CMG policy. Control this behavior with the client
  setting, Enable clients to use a cloud management gateway. For more information,
  see About client settings.

Client location
The Configuration Manager client automatically determines whether it's on the intranet
or the internet. If the client can contact a domain controller or an on-premises
management point, it sets its connection type to Currently intranet. Otherwise, it
switches to Currently Internet, and uses the location of the CMG service to
communicate with the site.

  ７ Note

  You can force the client to always use the CMG regardless of whether it's on the
  intranet or internet. This configuration is useful for testing purposes, or for clients

<!-- p.2777 -->

  that you want to force to always use the CMG. Set the following registry key on the
  client:

  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CCM\Security, ClientAlwaysOnInternet = 1

  You can also specify this setting during client installation using the
  CCMALWAYSINF property.

  This setting will always apply, even if the client roams into a location where
  boundary group configurations would otherwise leverage local resources.

To verify that clients have the policy specifying the CMG, open a Windows PowerShell
command prompt as an administrator on the client computer, and run the following
command:

  PowerShell

  Get-WmiObject -Namespace Root\Ccm\LocationServices -Class
  SMS_ActiveMPCandidate | Where-Object {$_.Type -eq "Internet"}

This command displays any internet-based management points the client knows about.
While the CMG isn't technically an internet-based management point, clients view it as
one.

  ７ Note

  To troubleshoot CMG client traffic, use CMGService.log and
  SMS_Cloud_ProxyConnector.log. For more information, see Log files.

Install off-premises clients using a CMG
There are two methods to install the Configuration Manager client on devices that aren't
currently connected to your intranet. Both require a local administrator account on the
target system.

       The first method is to use a bulk registration token to install the client on a device.
       For more information on this method, see Create a bulk registration token.

       For the second method, when you run ccmsetup.exe, use the /mp parameter to
       specify the CMG's URL. For more information, see About client installation
       parameters and properties. This method requires one of the following conditions:

<!-- p.2778 -->

        The Configuration Manager site is properly configured to use PKI certificates for
        client authentication. Additionally, the client systems each have a valid, unique,
        and trusted client authentication certificate previously issued to them.

        The systems are Microsoft Entra domain-joined or hybrid Microsoft Entra
        domain-joined.

Configure off-premises clients for CMG
You can connect devices to a recently configured CMG where the following conditions
are true:

     They already have the Configuration Manager client installed.

     They aren't connected and can't be connected to your intranet.

     They meet one of the following conditions:

        A valid, unique, and trusted client authentication certificate previously issued to
        it.

        Microsoft Entra domain-joined

        Hybrid Microsoft Entra domain-joined

     You don't want to or can't completely reinstall the existing client.

     You have a method to change a machine registry value and restart the SMS Agent
     Host service using a local administrator account.

To force the connection on these devices, create the REG_SZ registry entry CMGFQDNs in
the key HKLM\Software\Microsoft\CCM . Set its value to the URL of the CMG, for example,
https://GraniteFalls.contoso.com . Then restart the SMS Agent Host Windows service

on the device.

If the Configuration Manager client doesn't have a current CMG or internet-facing
management point set in the registry, it automatically checks the CMGFQDNs registry
value. This check occurs every 25 hours, when the SMS Agent Host service starts, or
when it detects a network change. When the client connects to the site and learns of a
CMG, it automatically updates this value.

Next steps

<!-- p.2779 -->

Your CMG is now set up and functional with clients communicating to the site. Next,
understand how to monitor the CMG service and clients:

  Monitor CMG

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2780 -->

Monitor the CMG
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After the cloud management gateway (CMG) is running and clients are connecting
through it, you can monitor clients and network traffic. Monitor the service to make sure
its performance is optimal.

Monitor clients
Clients connected through the CMG appear in the Configuration Manager console the
same way on-premises clients do. For more information, see how to monitor clients.

Monitor traffic in the console
Monitor traffic on the CMG using the Configuration Manager console:

   1. Go to the Administration workspace, expand Cloud Services, and select the Cloud
      Management Gateway node.

   2. Select the CMG in the list pane.

   3. View the traffic information in the details pane for the CMG connection point and
      the site system roles it connects to. These statistics show the client requests
      coming into these roles. The requests include policy, location, registration, content,
      inventory, and client notifications.

Monitor content
Monitor content that you distribute to a CMG the same as with any other distribution
point. For more information, see Monitor content.

When you view the list of CMGs in the console, you can add more columns to the list.
For example, the Storage egress (GB) column shows the amount of data that clients
downloaded from the service in the last 30 days.

Monitor logs

<!-- p.2781 -->

The following table lists the log files that contain information related to the cloud
management gateway.

                                                                                ﾉ     Expand table

 Log name                       Description                                  Computer with log
                                                                             file

 CloudMgr.log                   Records details about deploying the          The installdir folder
                                cloud management gateway service,            on the primary site
                                ongoing service status, and use data         server or CAS.
                                associated with the service. To configure
                                the logging level, edit the Logging level
                                value in the following registry key:
                                 HKLM\SOFTWARE\
                                Microsoft\SMS\COMPONENTS\ SMS_CLOUD_
                                SERVICES_MANAGER

 CMGSetup.log Note 1            Records details about the second phase       The
                                of the cloud management gateway              %approot%\logs on
                                deployment (local deployment in              your Azure server, or
                                Azure). To configure the logging level,      the SMS/Logs folder
                                use the setting Trace level (Information     on the site system
                                (Default), Verbose, Error) on the Azure      server
                                portal\Cloud services configuration
                                tab.

 CMGService.log Note 1          Records details about the cloud              The
                                management gateway service core              %approot%\logs on
                                component in Azure. To configure the         your Azure server, or
                                logging level, use the setting Trace level   the SMS/Logs folder
                                (Information (Default), Verbose, Error)      on the site system
                                on the Azure portal\Cloud services           server
                                configuration tab.

 SMS_Cloud_ProxyConnector.log   Records details about setting up             Site system server
                                connections between the cloud
                                management gateway service and the
                                cloud management gateway connection
                                point.

 CMGContentService.log Note 1   When you enable a CMG to also serve          The
                                content from Azure storage, this log         %approot%\logs on
                                records the details of that service.         your Azure server, or
                                                                             the SMS/Logs folder
                                                                             on the site system
                                                                             server

     For troubleshooting deployments, use CloudMgr.log and CMGSetup.log

<!-- p.2782 -->

     For troubleshooting service health, use CMGService.log and
     SMS_Cloud_ProxyConnector.log.
     For troubleshooting client traffic, use CMGService.log and
     SMS_Cloud_ProxyConnector.log.

Note 1: Logs synchronized from Azure

These are local Configuration Manager log files that cloud service manager syncs from
Azure storage every five minutes. The cloud management gateway pushes logs to Azure
storage every five minutes. So the maximum delay is 10 minutes. Verbose switches affect
both local and remote logs. The actual file names include the service name and role
instance identifier. For example, CMG-ServiceName-RoleInstanceID-CMGSetup.log.
These log files are synced, so you don't need to RDP to the cloud management gateway
to obtain them, and that option isn't supported.

Cloud management dashboard
The cloud management dashboard provides a centralized view for CMG usage. It also
displays data about cloud users and devices.

In the Configuration Manager console, go to the Monitoring workspace. Select the
Cloud Management node, and view the dashboard tiles.

The following screenshot shows the section of the cloud management dashboard
specific for the CMG:

<!-- p.2783 -->

                                                                                         

Connection analyzer
To aid troubleshooting, use the CMG connection analyzer for real-time verification. The
in-console utility checks the current status of the service, and the communication
channel through the CMG connection point to any management points that allow CMG
traffic.

   1. In the Configuration Manager console, go to the Administration workspace.
      Expand Cloud Services and select the Cloud management gateway node.

   2. Select the target CMG instance, and then select Connection analyzer in the ribbon.

   3. In the CMG connection analyzer window, select one of the following options to
      authenticate with the service:

       a. Microsoft Entra user: Use this option to simulate communication the same as a
           cloud-based user identity signed in to a Microsoft Entra joined Windows device.
           Select Sign In to securely enter the credentials for a Microsoft Entra user
           account.

       b. Client certificate: Use this option to simulate communication the same as a
           Configuration Manager client with a client authentication certificate.

<!-- p.2784 -->

   4. Select Start to start the analysis. The analyzer window displays the results. Select
     an entry to see more details in the Description field.

Set up outbound traffic alerts
Outbound traffic alerts help you know when network traffic approaches a 14-day
threshold level. When you create the CMG, you can set up traffic alerts. If you skipped
that part, you can still set up the alerts after the service is running. Adjust the alert
settings at any time.

You can also configure thresholds for the amount of data that you want to store on the
CMG and that clients download. Use alerts for these thresholds to help you decide when
to stop or delete the cloud service, adjust the content that you store on the CMG, or
modify which clients can use the service.

<!-- p.2785 -->

   1. Go to the Administration workspace, expand Cloud Services, and select the Cloud
     Management Gateway node.

   2. Select the CMG in the list pane, and then select Properties in the ribbon.

   3. Go to the Alerts tab to enable the threshold and alerts:

           Specify the 14-day data threshold for outbound data transfer in gigabytes
           (GB). This threshold helps you to monitor the amount of data that transfers
           from the CMG to clients every two weeks. By default, this threshold is
           approximately 10 TB. The default value is 10,000 GB. The site raises warning
           and critical alerts when transfers reach values that you define. By default,
           these alerts occur at 50% and 90% of the threshold.

           If the CMG is content-enabled, also specify a storage alert threshold. This
           threshold sets an upper limit on the amount of content to store on the CMG.
           By default, this threshold is approximately 2 TB. The default value is 2,000
           GB. Configuration Manager generates warning and critical alerts when the
           remaining free space reaches the levels that you specify. By default, these
           alerts occur at 50% and 90% of the threshold.

  ７ Note

  Alerts for the CMG depend on usage statistics from Azure, which can take up to 24
  hours to become available. For more information about Storage Analytics for Azure,
  see Storage Analytics.

  In an hourly cycle, the primary site that monitors the CMG downloads transaction
  data from Azure. It stores this transaction data in the CloudDP-<ServiceName>.log
  file on the site server. Configuration Manager then evaluates this information
  against the storage and transfer quotas for each CMG. When the transfer of data
  reaches or exceeds the specified volume for either warnings or critical alerts,
  Configuration Manager generates the appropriate alert.

  Because the site downloads information about data transfers from Azure every
  hour, the usage might exceed a warning or critical threshold before Configuration
  Manager can access the data and raise an alert.

Stop CMG when it exceeds threshold
Configuration Manager can stop a CMG service when the total data transfer goes over
your limit. Use alerts to trigger notifications when the usage reaches warning or critical

<!-- p.2786 -->

levels. To help reduce any unexpected Azure costs because of a spike in usage, this
option turns off the cloud service.

  ） Important

  Even if the service isn't running, there are still costs associated with the cloud
  service. Stopping the service doesn't eliminate all associated Azure costs. To
  remove all cost for the cloud service, delete the CMG.

  When you stop the CMG service, internet-based clients can't communicate with
  Configuration Manager.

The total data transfer (egress) includes data from the cloud service and storage
account. This data comes from the following flows:

     CMG to client
     CMG to site, including CMG log files
     If you enable CMG for content, storage account to client

For more information on these data flows, see CMG ports and data flow.

The storage alert threshold is separate. That alert monitors the capacity of your Azure
storage instance.

When you select the CMG instance in the Cloud Management Gateway node in the
console, you can see the total data transfer in the details pane.

Configuration Manager checks the threshold value every six minutes. If there's a sudden
spike in usage, Configuration Manager can take up to six minutes to detect that it
exceeded the threshold and then stop the service.

Process to stop the cloud service when it exceeds
threshold
   1. Set up outbound traffic alerts.

   2. On the Alerts tab of the CMG properties window, enable the option to Stop this
     service when the critical threshold is exceeded.

To test this feature, temporarily reduce one of the following values:

     14-day threshold for outbound data transfer (GB). The default value is 10000 .

     Percentage of threshold for raising Critical alert. The default value is 90 .

<!-- p.2787 -->

Next steps
If you need to change the configuration, you can modify the CMG:

  Modify a CMG

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2788 -->

Modify a CMG
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If you need to change the configuration, you can modify the cloud management
gateway (CMG).

Configure properties
After you create a CMG, you can modify some of its settings. Select the CMG in the
Configuration Manager console and select Properties. Configure settings on the
following tabs:

Settings tab
      Certificate file: Change the server authentication certificate for the CMG. This
      option is useful when you renew the certificate before it expires. When you get a
      new certificate, make sure its common name is the same.

        ７ Note

        When you renew the server authentication certificate for the CMG, the FQDN
        that you specify for the certificate's common name (CN) is case-sensitive. For
        example, if the CN of the current certificate is granitefalls.contoso.com ,
        create the new certificate with the same lowercase CN. The wizard won't
        accept a certificate with the CN GRANITEFALLS.CONTOSO.COM .

        If you make significant changes to the certificate, you may need to Redeploy
        the service. For example, changing the organization name on the certificate.

      Description: Specify an optional description to further identify this CMG in the
      Configuration Manager console.

      VM Instance: Change the number of virtual machines that the service uses in
      Azure. This setting allows you to dynamically scale the service up or down based
      on usage or cost considerations.

      Certificates: Add or remove trusted root or intermediate CA certificates. This
      option is useful when adding new CAs, or retiring expired certificates.

<!-- p.2789 -->

     Verify Client Certificate Revocation: If you didn't originally enable this setting
     when you created the CMG, you can enable it afterwards after you publish the CRL.
     For more information, see Publish the certificate revocation list.

     Enforce TLS 1.2: The CMG enables this option by default. Require it to use the TLS
     1.2 encryption protocol. Starting in version 2107 with the update rollup, this setting
     also applies to the CMG storage account. For more information, see How to enable
     TLS 1.2.

     Allow CMG to function as a cloud distribution point and serve content from
     Azure storage: The CMG enables this option by default. If you plan on targeting
     deployments with content to clients, you need to configure the CMG to serve
     content.

Alerts tab
Reconfigure the alerts at any time after you create the CMG. For more information, see
Monitor the CMG: Set up outbound traffic alerts.

Content tab
View the packages that are assigned to the cloud storage account for this CMG. See
how much space each package uses in the storage account. When you select a package,
you can redistribute or remove the content files.

To verify that the content files for a package are available on the content-enabled CMG,
go to the Content Status node in the Monitoring workspace. For more information, see
Monitor content you distribute.

Convert

  ７ Note

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

Starting in version 2107, if you have a CMG that uses the classic cloud service, convert it
to use a virtual machine scale set.

<!-- p.2790 -->

   Tip

  This process reuses the underlying storage account.

When you convert a CMG, you can't change all settings:

                                                                         ﾉ   Expand table

 Setting                                                      Convert

 VM size

 VM instances

 Verify CRL

 Require TLS

 Serve content

 Azure environment

 Subscription

 Microsoft Entra app

 Region

 Resource group

To make changes that the conversion process doesn't support, you need to Redeploy
the service.

  ） Important

  If your CMG's service name is in the cloudapp.net domain, you can't convert it to a
  virtual machine scale set. For example, you issued a server authentication certificate
  from your internal PKI with a common name of GraniteFalls.cloudapp.net . Since
  Microsoft owns the cloudapp.net domain, you can't create a DNS CNAME to map
  this service name to the new deployment name in the cloudapp.azure.com domain.

     1. Issue a new server authentication certificate from your internal PKI with a new
          service name. Consider using your domain name instead of a Microsoft
          domain. For more information, see Use an enterprise PKI certificate.

<!-- p.2791 -->

     2. Deploy a new CMG as a virtual machine scale set with the new certificate.
     3. Once clients refresh policy to get this new CMG, delete the old CMG.

  For more information, see Replace a CMG with a new service name.

Process to convert a CMG to a virtual machine scale set

  ） Important

  First review the prerequisites for virtual machine scale sets. For example, make sure
  that you register the necessary Azure resource providers in the subscription. You
  also need both Subscription Owner permission to the associated subscription and
  Global Administrator permissions for the associated tenant.

  1. In the Configuration Manager console, go to the Administration workspace,
     expand Cloud Services, and select the Cloud Management Gateway node.

  2. Select a CMG instance whose Status is Ready. In the ribbon, select Convert. This
     action opens the Convert CMG wizard.

  3. On the General page, select Next. You can't change any of these settings.

  4. On the Settings page, note the new Deployment name with the suffix for the virtual
     machine scale set.

  5. Make other configuration changes as needed. Then select Next and complete the
     wizard.

Monitor the conversion process the same as a new deployment. For example, view the
state in the console, and review cloudmgr.log. For more information, see Monitor CMG.

Update or create a DNS CNAME
Since the deployment name changed, you need to update or create a DNS canonical
name record (CNAME). This alias maps the service name to the deployment name. For
more information, see Create a DNS CNAME alias.

For example:

     The CMG's service name is GraniteFalls.contoso.com .

     For the deployment name:

<!-- p.2792 -->

        Classic: GraniteFalls.cloudapp.net

        Virtual machine scale set: GraniteFalls.EastUS.CloudApp.Azure.Com

Redeploy the service
More significant changes, such as the following configurations, require that you
redeploy the service:

     Subscription
     Service name
     Region
     Resource group
     Significant changes to the server authentication certificate

Always keep at least one active CMG for internet-based clients to receive updated
policy. Internet-based clients can't communicate with a removed CMG. Clients don't
know about a new one until they refresh policy. When you create a second CMG
instance to delete the first, also create another CMG connection point.

Clients refresh policy by default every 24 hours. Before you delete the old CMG, wait at
least one day after you create a new one. If clients are turned off or without an internet
connection, you may need to wait longer.

If you have an existing CMG from version 1810 or earlier, it uses the Azure Service
Manager deployment method. This method used an Azure management certificate. This
method is deprecated, and support will be removed in a later version of Configuration
Manager. Redeploy a new CMG to use the Azure Resource Manager deployment
method.

The process to redeploy the service depends upon your service name and whether you
want to reuse it.

  ７ Note

  In version 2107 and later, you can have multiple CMGs that use different
  deployment methods. You can also convert a cloud service (classic) CMG to a
  virtual machine scale set. For more information, see Convert.

  In versions 2010 and 2103, if you already deployed a CMG with the cloud service
  (classic) method, you can't deploy another CMG as a virtual machine scale set, and
  vice versa. First delete the existing CMG, and then create a new one with the other
  deployment method. All CMG instances for the site need to use the same

<!-- p.2793 -->

  deployment method. For more information, see Plan for CMG: Virtual machine
  scale sets.

Replace a CMG and reuse the same service name

  ） Important

  This process assumes that you already have at least two CMG services, and are
  replacing one of them at a time. You need to have at least one active CMG for
  internet-based clients.

   1. Delete the old CMG.

   2. Create a new CMG with the same server authentication certificate.

   3. Reconfigure the CMG connection point to use the new CMG.

Replace a CMG with a new service name
   1. Get a new server authentication certificate.

   2. Create a new CMG.

   3. Create a new CMG connection point and link it with the new CMG.

   4. Wait at least one day for internet-based clients to receive policy about the new
     CMG. If clients are turned off or without an internet connection, you may need to
     wait longer.

   5. Delete the old CMG and associated CMG connection point.

Stop and start the service
Use the Configuration Manager console to stop and start the service if you need to.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Cloud Services, and select the Cloud Management Gateway node.

   2. Select the CMG instance.

   3. In the ribbon, select one of the following actions:

           To stop a running CMG, select Stop service.

<!-- p.2794 -->

          To start a stopped CMG, select Start service.

Configuration Manager can stop a CMG service when the total data transfer goes over
your limit. For more information, see Stop CMG when it exceeds threshold

  ） Important

  Even if the service isn't running, there are still costs associated with the cloud
  service. Stopping the service doesn't eliminate all associated Azure costs. To
  remove all cost for the cloud service, delete the CMG.

  When you stop the CMG service, internet-based clients can't communicate with
  Configuration Manager.

You can also use PowerShell to stop and start a CMG:

     Start-CMCloudManagementGateway
     Stop-CMCloudManagementGateway

Determine deployment model
To determine the current deployment model of a CMG:

  1. In the Configuration Manager console, go to the Administration workspace,
     expand Cloud Services, and select the Cloud Management Gateway node.

  2. Select the CMG instance.

  3. In the Details pane at the bottom of the window, look for the Deployment Model
     attribute.

     Starting in version 2010, you'll see either Cloud service (classic) or Virtual machine
     scale set.

     In version 2006 and earlier, for a Resource Manager deployment, this attribute is
     Azure Resource Manager. The legacy deployment model with the Azure
     management certificate displays as Azure Service Manager.

       ） Important

<!-- p.2795 -->

        CMG deployments using Azure Service Manager are deprecated. Support will
        be removed in a later version of Configuration Manager. Redeploy a new
        CMG to use the Azure Resource Manager deployment method.

You can also add the Deployment Model attribute as a column to the list view.

Modifications in the Azure portal
Only modify the CMG from the Configuration Manager console. Making modifications
to the service or underlying VMs directly in Azure isn't supported. Any changes may be
lost without notice. As with any platform as a service (PaaS), the service can rebuild the
VMs at any time. These rebuilds can happen for backend hardware maintenance, or to
apply updates to the VM OS.

Renew Azure service secret key
When you first configure Microsoft Entra ID for the CMG to create the Cloud
Management Azure service, you specify a secret key validity period on the web (server)
app registration. By default, the secret key is valid for one year, or you can specify two
years. Before the secret key expires, make sure to renew it. For more information, see
Renew secret key.

Delete the service
If you need to delete the CMG, only do it from the Configuration Manager console.
Manually removing any components in Azure causes the system to be inconsistent. This
state leaves orphaned information, and unexpected behaviors may occur.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2796 -->

Manually register Microsoft Entra apps
for the CMG
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

The second primary step to set up a cloud management gateway (CMG) is to integrate
the Configuration Manager site with your Microsoft Entra tenant. This integration allows
the site to authenticate with Microsoft Entra ID, which it uses to deploy and monitor the
CMG service. If you can't use Configuration Manager to automate the creation of the
apps during the Azure Service Wizard, you can use the wizard to import a previously
created app. For example, if your Azure administrators require that they manually create
all Microsoft Entra app registrations, then use this process.

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

This article provides the specific details for the second method. Pair these instructions
with the procedures in the Configure Microsoft Entra ID for CMG article to complete the
process.

Get tenant details

<!-- p.2797 -->

   Tip

  During this process, you'll need to note several values to use later. Open an app like
  Windows Notepad to paste in the values that you'll copy from the Azure Portal.

First, you need to make note of the Microsoft Entra tenant name and tenant ID. These
values are the first two pieces of information that you need to import the app
registrations in Configuration Manager.

   1. In the Azure portal   , select Microsoft Entra ID.

   2. In the Microsoft Entra ID menu, select Custom domain names.

   3. Note the tenant name. For example, contoso.onmicrosoft.com .

   4. In the Microsoft Entra ID menu, select Properties.

   5. Copy the Tenant ID GUID value.

Register the web (server) app
   1. In the Microsoft Entra ID menu, select App registrations. Select New registration
     to create a new app.

   2. In the Register an application pane, specify the following information:

           Name: A friendly name for the app. For example, CMG-ServerApp .
           Supported account types: Leave this setting as the default option, Accounts
           in this organizational directory only.
           Redirect URI: Select: Public client/native (mobile &desktop) and type
           http://localhost as URI

   3. Select Register to create the app.

   4. In the properties of the new app, copy the following values:

           Display name: This value is the friendly name for this app registration that
           you'll use later as the application name.
           Application (client) ID: You'll use this GUID value later as the client ID.

   5. In the menu of the app properties, select Certificates & secrets, then select New
     client secret.

           Description: You can use any name for the secret or leave it blank.

<!-- p.2798 -->

       Expires: Select either 12 months or 24 months.

  Select Add. Immediately copy the client secret string Value and Expires. If you
  leave this pane, you can't retrieve the same secret again. You'll use these values
  later as the secret key and secret key expiry values.

6. If you're going to use Microsoft Entra user Discovery in Configuration Manager,
  you need to adjust the permissions on this app. In the menu of the app properties,
  select API permissions. By default it should have the User.Read permission for the
  Microsoft Graph API, which needs to change.

  a. Select Microsoft Graph to enumerate the list of available API permissions, then
     select Application permissions.

  b. Expand Directory, and then select Directory.Read.All.

   c. Switch to Delegated permissions.

  d. Expand User, and remove the User.Read permission.

  e. Select Update permissions.

   f. On the API permissions pane, select Grant admin consent for..., then select Yes.

7. In the menu of the app properties, select Expose an API.

  a. For the Application ID URI, select Add. Specify a URI that's unique for the
     tenant. You'll use this value later as the App ID URI. Use one of the following
     recommended formats:

           api://{tenantId}/{string} , for example, api://5e97358c-d99c-4558-af0c-

          de7774091dda/ConfigMgrService
           https://{verifiedCustomerDomain}/{string} , for example,

           https://contoso.onmicrosoft.com/ConfigMgrService

     Select Save.

  b. Select Add a scope, and specify the following required information:

          Scope name: user_impersonation
          Who can consent: Select Admins and users
          Admin consent display name: Specify a meaningful name. For example,
           Access CMG-ServerApp

          Admin consent description: Specify a meaningful description. For
          example, Allow the application to access CMG-ServerApp on behalf of

<!-- p.2799 -->

              the signed-in user.

      c. Select Add scope to save.

   8. In the menu of the app properties, select Manifest. Set the
     oauth2AllowIdTokenImplicitFlow entry to true. For example:

       JSON

        "oauth2AllowIdTokenImplicitFlow": true,

     Select Save.

The web (server) app for CMG is now registered in Microsoft Entra ID.

Register the native (client) app
   1. In the Microsoft Entra ID menu, select App registrations. Select New registration
     to create a new app.

   2. In the Register an application pane, specify the following information:

           Name: A friendly name for the app. For example, CMG-ClientApp .
           Supported account types: Leave this setting as the default option, Accounts
           in this organizational directory only.
           Redirect URI: Leave this optional value blank.

   3. Select Register to create the app.

   4. In the properties of the new app, copy the following values:

           Display name: This value is the friendly name for this app registration that
           you'll use later as the application name.
           Application (client) ID: You'll use this GUID value later as the client ID.

   5. In the menu of the app properties, select Authentication.

      a. Under Platform configurations, select Add a platform.

         i. In the Configure platforms pane, select Mobile and desktop applications.

         ii. In the Configure Desktop + devices pane, under Custom redirect URIs,
           specify ms-appx-web://Microsoft.AAD.BrokerPlugin/<ClientID> . Use the app's
           client ID GUID, for example: ms-appx-
           web://Microsoft.AAD.BrokerPlugin/2afe572e-d268-4c77-a22d-fdca617e2255 .

<!-- p.2800 -->

          iii. Select Configure.

        b. Under Advanced settings, set Allow public client flows to Yes. Select Save.

   6. Adjust the permissions on this app. In the menu of the app properties, select API
     permissions. By default it should have the User.Read delegated permission for the
     Microsoft Graph API.

        a. On the API permissions pane, select Add a permission.

        b. Switch to the My APIs tab, and select your web (server) app. For example, CMG-
          ServerApp. Select the user_impersonation permission, and then select Add
          permissions to save.

        c. On the API permissions pane, select Grant admin consent for..., and then select
          Yes.

   7. In the menu of the app properties, select Manifest. Set the
     oauth2AllowIdTokenImplicitFlow entry to true. For example:

          JSON

          "oauth2AllowIdTokenImplicitFlow": true,

     Select Save.

The native (client) app for CMG is now registered in Microsoft Entra ID. This step also
concludes the process in the Azure portal. The role of the Azure global administrator is
done.

Import the apps to Configuration Manager
After you manually register the two apps in the Azure portal, use the process in the
article to Configure Microsoft Entra ID for CMG, but select the option to Import each of
the apps.

These processes import metadata about the Microsoft Entra apps into Configuration
Manager. You don't require any Microsoft Entra permissions to import these apps.

Import web (server) app
When you select Import from the Server app window, it opens the Import apps window.
Enter the following information about the Microsoft Entra web app that's already
