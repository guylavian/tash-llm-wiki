---
title: "Core infrastructure documentation — pages 521-560"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0521-0560
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0521-0560
family: sccm
documentKind: "doc"
abstract: "Client --> Global catalog domain controller Configuration Manager console --> internet Management point --> Domain controller Site server --> Domain controller Site server <--> Issuing Certification Authority (CA) Software update point --> internet Software update point --> Upst"
---

# Core infrastructure documentation — pages 521-560

<!-- p.521 -->

     Client --> Global catalog domain controller

     Configuration Manager console --> internet

     Management point --> Domain controller

     Site server --> Domain controller

     Site server <--> Issuing Certification Authority (CA)

     Software update point --> internet

     Software update point --> Upstream WSUS Server

     Service connection point --> Azure

     Service connection point --> Azure Logic App

     CMG connection point --> CMG cloud service

Installation requirements for site systems that support
internet-based clients

  ７ Note

  This section only applies to internet-based client management (IBCM). It doesn't apply to
  the cloud management gateway. For more information, see Manage clients on the
  internet.

Internet-based management points, distribution points that support internet-based clients, the
software update point, and the fallback status point use the following ports for installation and
repair:

     Site server --> Site system: RPC endpoint mapper using UDP and TCP port 135

     Site server --> Site system: RPC dynamic TCP ports

     Site server <--> Site system: Server message blocks (SMB) using TCP port 445

Application and package installations on distribution points require the following RPC ports:

     Site server --> Distribution point: RPC endpoint mapper using UDP and TCP port 135

     Site server --> Distribution point: RPC dynamic TCP ports

<!-- p.522 -->

Use IPsec to help secure the traffic between the site server and site systems. If you must restrict
the dynamic ports that are used with RPC, you can use the Microsoft RPC configuration tool
(rpccfg.exe). Use the tool to configure a limited range of ports for these RPC packets. For more
information, see How to configure RPC to use certain ports and how to help secure those ports
by using IPsec .

  ） Important

  Before you install these site systems, make sure that the remote registry service is running
  on the site system server and that you have specified a site system installation account if
  the site system is in a different Active Directory forest without a trust relationship. For
  example, the remote registry service is used on servers running site systems such as
  distribution points (both pull and standard) and remote SQL Servers.

Ports used by Configuration Manager client installation
The ports that Configuration Manager uses during client installation depends on the
deployment method:

       For a list of ports for each client deployment method, see Ports used during Configuration
       Manager client deployment

       For more information about how to configure Windows Firewall on the client for client
       installation and post-installation communication, see Windows Firewall and port settings
       for clients

Ports used by migration
The site server that runs migration uses several ports to connect to applicable sites in the
source hierarchy. For more information, see Required configurations for migration.

Ports used by Windows Server
The following table lists some of the key ports used by Windows Server.

                                                                                   ﾉ   Expand table

 Description                                                  UDP                       TCP

 DNS                                                          53                        53

<!-- p.523 -->

 Description                                                UDP                     TCP

 DHCP                                                       67 and 68               --

 NetBIOS Name Resolution                                    137                     --

 NetBIOS Datagram Service                                   138                     --

 NetBIOS Session Service                                    --                      139

 Kerberos authentication                                    --                      88

For more information, see the following articles:

     Service overview and network port requirements for Windows

     How to configure a firewall for domains and trusts

Diagram
The following diagram shows the connections between the main components that are in a
typical Configuration Manager site. It currently doesn't include all connections.

Next steps

<!-- p.524 -->

Proxy server support

Internet access requirements

Last updated on 12/08/2025

<!-- p.525 -->

Proxy server support in Configuration
Manager
Applies to: Configuration Manager (current branch)

Some Configuration Manager components require connections to the internet. If your
environment requires internet traffic to use a proxy server, configure these systems to use the
proxy.

     A computer that hosts a site system server supports a single proxy server configuration. All
     site system roles on that computer share this same proxy configuration. If you need
     separate proxy servers for different roles or instances of a role, place those roles on
     separate site system servers.

     When you configure new proxy server settings for a site system server that already has a
     proxy server configuration, the original configuration is overwritten.

     By default, connections to the proxy use the System account of the computer that hosts the
     site system role.

     If the computer account can't authenticate, the site system server can store user credentials
     to connect to the proxy server. These credentials are the site system proxy server account.

     If you install the Configuration Manager console on administrative workstations, some
     connections will use the proxy configuration.

Site system roles that use a proxy
The following site system roles connect to the internet, and if necessary, can use a proxy server:

Asset Intelligence synchronization point

  ） Important

  Starting in November 2021, this feature of Configuration Manager is deprecated. For more
  information, see Asset intelligence deprecation.

<!-- p.526 -->

This site system role connects to Microsoft and uses a proxy server configuration on the
computer that hosts the Asset Intelligence synchronization point.

Cloud distribution point

  ７ Note

  The cloud-based distribution point (CDP) is deprecated. Starting in version 2107, you can't
  create new CDP instances. To provide content to internet-based devices, enable a cloud
  management gateway (CMG) to distribute content. For more information, see Deprecated
  features.

The cloud distribution point role runs in Microsoft Azure. You don't configure this site system role
to use a proxy. Set the proxy configuration on the primary site server that manages the cloud
distribution point.

For this configuration, the primary site server:

     Must be able to connect to Microsoft Azure to set up, monitor, and distribute content to the
     cloud distribution point.

     By default, uses the computer's System account to make the connection. It can also use the
     site system proxy server account, if necessary.

     Uses Windows web browser APIs.

Cloud management gateway connection point
The cloud management gateway (CMG) connection point is an on-premises role that
communicates with the CMG service in Azure. For more information, see Overview of CMG.

Distribution point
If you enable a Configuration Manager distribution point for Microsoft Connected Cache, it can
communicate through an unauthenticated proxy server for internet access. For more information,
see Microsoft Connected Cache.

Exchange Server connector

<!-- p.527 -->

This site system role connects to an Exchange Server. It uses a proxy server configuration on the
computer that hosts the Exchange Server connector.

Management point
Starting in version 2603, the management point uses Microsoft Identity Service Essentials (MISE)
for Microsoft Entra token validation. In environments that support Microsoft Entra joined users
and devices, the management point server requires internet access to connect to Microsoft Entra
authentication endpoints.

  ） Important

  The proxy configured in the site system properties doesn't apply to MISE token validation.
  You must configure the proxy at the system level on the management point server.

To configure the proxy, run the following command at an elevated command prompt on the
management point server:

 Windows Command Prompt

 netsh winhttp set proxy <proxyservername>:<portnumber>

Replace <proxyservername> with the fully qualified domain name of the proxy server. Replace
<portnumber> with the port number for the proxy server. For example,

proxy.domain.example.com:80 .

To verify the current proxy configuration:

 Windows Command Prompt

 netsh winhttp show proxy

To remove the proxy configuration and configure direct access to the internet:

 Windows Command Prompt

 netsh winhttp reset proxy

For more information about this requirement and troubleshooting, see Management point
requires internet access for Microsoft Entra token validation.

<!-- p.528 -->

Service connection point
This site system role connects to the Configuration Manager cloud service to download version
updates for Configuration Manager. It uses a proxy server that's configured on the computer that
hosts the service connection point.

Software update point
This site system role uses the proxy when it connects to Microsoft Update to download patches
and synchronize information about updates. Like every other site system role, first configure the
site system proxy settings. Then configure the following options specific to the software update
point:

     Use a proxy server when synchronizing software updates

     Use a proxy server when downloading content by using automatic deployment rules

         ７ Note

         While available for use, this setting isn't used by software update points at secondary
         sites.

These settings are on the Proxy and Account Settings tab of the software update point
properties.

  ７ Note

  By default, when the automatic deployment rules run, the System account on the site server
  of the site on which an automatic deployment rule was created is used to connect to the
  internet and download software updates. Alternatively, configure and use the site system
  proxy server account.

  When this account cannot access the internet, software updates fail to download. The
  following entry is logged to ruleengine.log: Failed to download the update from internet.
  Error = 12007.

Other features that use the proxy

<!-- p.529 -->

The following features use the proxy of the site system that hosts the service connection point
role:

        Microsoft Entra user discovery
        Microsoft Entra user group discovery
        Synchronizing collection membership results to Microsoft Entra groups

Configure the proxy for a site system server
   1. In the Configuration Manager console, go to the Administration workspace. Expand Site
        Configuration, and then select the Servers and Site System Roles node.

   2. Select the site system server that you want to edit. In the details pane, right-click the Site
        system role, and select Properties.

   3. In Site system Properties, switch to the Proxy tab. Configure the following proxy settings:

             Use a proxy server when synchronizing information from the internet: Select this
             option to enable the site system server to use a proxy server.

             Proxy server name: Specify the hostname or FQDN of the proxy server in your
             environment.

             Port: Specify the network port on which to communicate with the proxy server. By
             default, it uses port 80.

             Use credentials to connect to the proxy server: Many proxy servers require a user to
             authenticate. By default, the site system server uses its computer account to connect
             to the proxy server. If necessary, enable this option, click Set, and then choose an
             Existing Account or specify a New Account. These credentials are the site system
             proxy server account. For more information, see Accounts used in Configuration
             Manager.

   4. Choose OK to save the new proxy server configuration.

Configuration Manager console
If you install the Configuration Manager console on an administrative workstation, some
connections will use the proxy configuration. The console may fail to connect to the site because
of a proxy configuration. To help troubleshoot, you can modify the console configuration file,
Microsoft.ConfigurationManagement.exe.config . By default, this file is located in C:\Program Files

<!-- p.530 -->

(x86)\Microsoft Endpoint Manager\AdminConsole\bin . Open it in Windows Notepad or another

XML editor.

Change this original setting:

  XML

    <system.net>
      <defaultProxy useDefaultCredentials="true" />
    </system.net>

Add the following element with the defaultProxy element: <proxy usesystemdefault="False"/>
</defaultProxy>

For example:

  XML

    <system.net>
      <defaultProxy useDefaultCredentials="true"><proxy usesystemdefault="False"/>
  </defaultProxy>
    </system.net>

Next steps
If your organization restricts network communication with the internet using a firewall or proxy
device, you need to allow access to internet endpoints. For more information, see internet access
requirements.

 Last updated on 06/12/2026

<!-- p.531 -->

Internet access requirements
Some Configuration Manager features rely on internet connectivity for full functionality. If your
organization restricts network communication with the internet using a firewall or proxy device,
make sure to allow these endpoints.

Configuration Manager uses the following Microsoft URL forwarding services throughout the
product:

      https://aka.ms

      https://go.microsoft.com

Even if they're not explicitly listed in the following sections, you should always allow these
endpoints.

Service connection point
For more information, see About the service connection point.

These configurations apply to the server that hosts the service connection point and any firewalls
between that server and the internet. Allow communication through outgoing HTTPS port TCP
443 to the internet locations.

The service connection point supports using a web proxy with or without authentication to use
these locations. For more information, see Proxy server support.

If the Configuration Manager site fails to connect to required endpoints for a cloud service, it
raises a critical status message ID 11488. When it can't connect to the service, the
SMS_SERVICE_CONNECTOR component status changes to critical. View detailed status in the
Component Status node of the Configuration Manager console.

Starting in version 2010, the service connection point validates important internet endpoints for
tenant attach. These checks help make sure that the cloud-connected services are available. It
also helps you troubleshoot issues by quickly determining if network connectivity is a problem.
For more information, see Validate internet access.

The specific URLs required by the service connection point vary by Configuration Manager
feature:

     Updates and servicing

<!-- p.532 -->

     Windows servicing
     Azure services
     Microsoft Store for Business
     Cloud services
     Configuration Manager console
     Tenant attach
     External notifications

   Tip

  The service connection point uses the Microsoft Intune service when it connects to
  go.microsoft.com or manage.microsoft.com . There's a known issue in which the Intune

  connector experiences connectivity issues if the Baltimore CyberTrust Root Certificate isn't
  installed, is expired, or is corrupted on the service connection point. For more information,
  see Service connection point doesn't download updates.

Updates and servicing
For more information, see Updates and servicing.

   Tip

  Enable these endpoints for the management insight rule, Connect the site to the Microsoft
  cloud for Configuration Manager updates.

     *.akamaiedge.net

     *.akamaitechnologies.com

     *.manage.microsoft.com

     go.microsoft.com

     download.microsoft.com

     download.windowsupdate.com

     download.visualstudio.microsoft.com

     definitionupdates.microsoft.com

<!-- p.533 -->

  ７ Note

  Starting March 2025, the configmgrbits.azureedge.net domain migrates to
  configmgrbits.cdn.manage.microsoft.com. No action is required if *.manage.microsoft.com
  traffic is already allowed.

     configmgrbits.azureedge.net

     configmgrbits.cdn.manage.microsoft.com

       ） Important

       This Azure endpoint only supports TLS 1.2 with specific cipher suites. Make sure your
       environment supports these Azure configurations. For more information, see Azure
       Front Door: TLS configuration FAQ.

     cmbitsstore.blob.core.windows.net

     ceuswatcab01.blob.core.windows.net

     ceuswatcab02.blob.core.windows.net

     eaus2watcab01.blob.core.windows.net

     eaus2watcab02.blob.core.windows.net

     weus2watcab01.blob.core.windows.net

     weus2watcab02.blob.core.windows.net

     cmbitsstore.blob.core.windows.net

     umwatsonc.events.data.microsoft.com

     *-umwatsonc.events.data.microsoft.com

Windows servicing
For more information, see Manage Windows as a service.

     download.microsoft.com

<!-- p.534 -->

     https://go.microsoft.com/fwlink/?LinkID=619849

     dl.delivery.mp.microsoft.com

Azure services
For more information, see Configure Azure services for use with Configuration Manager.

     management.azure.com (Azure public cloud)

     management.usgovcloudapi.net (Azure US Government cloud)

Co-management
If you enroll Windows devices to Microsoft Intune for co-management, make sure those devices
can access the endpoints required by Intune. For more information, see Network endpoints for
Microsoft Intune.

Microsoft Store for Business
If you integrate Configuration Manager with the Microsoft Store for Business, make sure the
service connection point and targeted devices can access the cloud service. For more information,
see Microsoft Store for Business proxy configuration.

Delivery optimization
If you use delivery optimization, clients need to communicate with its cloud service:
*.do.dsp.mp.microsoft.com

Distribution points that support Microsoft Connected Cache also require these endpoints.

For more information, see the following articles:

     Delivery optimization FAQ
     Fundamental concepts for content management in Configuration Manager
     Microsoft Connected Cache with Configuration Manager

Cloud services
For more information on the cloud management gateway (CMG), see Plan for CMG.

This section covers the following features:

<!-- p.535 -->

     Cloud management gateway (CMG)

     Microsoft Entra integration

     Microsoft Entra ID-based discovery

     Cloud distribution point (CDP)

       ７ Note

       The cloud-based distribution point (CDP) is deprecated. Starting in version 2107, you
       can't create new CDP instances. To provide content to internet-based devices, enable
       the CMG to distribute content.

The following sections list the endpoints by role. Some endpoints refer to a service by <prefix> ,
which is the prefix name of the CMG. For example, if your CMG is
GraniteFalls.WestUS.CloudApp.Azure.Com , then the actual storage endpoint is

GraniteFalls.blob.core.windows.net .

   Tip

  To clarify some terminology:

       CMG service name: The common name (CN) of the CMG server authentication
       certificate. Clients and the CMG connection point site system role communicate with
       this service name. For example, GraniteFalls.contoso.com or
        GraniteFalls.WestUS.CloudApp.Azure.Com .

       CMG deployment name: The first part of the service name plus the Azure location for
       the cloud service deployment. The cloud service manager component of the service
       connection point uses this name when it deploys the CMG in Azure. The deployment
       name is always in an Azure domain. The Azure location depends upon the deployment
       method, for example:
          Virtual machine scale set: GraniteFalls.WestUS.CloudApp.Azure.Com
          Classic deployment: GraniteFalls.CloudApp.Net

  This article uses examples with a virtual machine scale set as the recommended deployment
  method in version 2107 and later. If you use a classic deployment, note the difference as you
  read this article and configure internet access.

<!-- p.536 -->

Service connection point for cloud services
For Configuration Manager to deploy the CMG service in Azure, the service connection point
needs access to:

     Specific Azure endpoints, which are different per environment depending upon the
     configuration. Configuration Manager stores these endpoints in the site database. Query
     the AzureEnvironments table in SQL Server for the list of Azure endpoints.

     Azure services:
         management.azure.com (Azure public cloud)

         management.usgovcloudapi.net (Azure US Government cloud)

     For Microsoft Entra user discovery: Microsoft Graph endpoint https://graph.microsoft.com/

CMG connection point for cloud services
The CMG connection point needs access to the following endpoints:

                                                                                     ﾉ      Expand table

 Type                  Azure public cloud                      Azure US Government cloud

 Service name          <prefix>.<region>.cloudapp.azure.com    <prefix>.usgovcloudapp.net

 Storage endpoint 1    <prefix>.blob.core.windows.net          <prefix>.blob.core.usgovcloudapi.net

 Storage endpoint 2    <prefix>.table.core.windows.net         <prefix>.table.core.usgovcloudapi.net

 Key vault             <prefix>.vault.azure.net                <prefix>.vault.usgovcloudapi.net

The CMG connection point site system supports using a web proxy. For more information on
configuring this role for a proxy, see Proxy server support.

The CMG connection point only needs to connect to the CMG service endpoints. It doesn't need
access to other Azure endpoints.

Configuration Manager client for cloud services
Any Configuration Manager client that needs to communicate with a CMG needs access to the
following endpoints:

                                                                                     ﾉ      Expand table

<!-- p.537 -->

 Type                        Azure public cloud                     Azure US Government cloud

 Deployment name             <prefix>.<region>.cloudapp.azure.com   <prefix>.usgovcloudapp.net

 Storage endpoint            <prefix>.blob.core.windows.net         <prefix>.blob.core.usgovcloudapi.net

 Microsoft Entra endpoint    login.microsoftonline.com              login.microsoftonline.us

Configuration Manager console for cloud services
Any device with the Configuration Manager console needs access to the following endpoints:

                                                                                       ﾉ   Expand table

 Type                              Azure public cloud                Azure US Government cloud

 Microsoft Entra endpoints         login.microsoftonline.com         login.microsoftonline.us
                                   aadcdn.msauth.net
                                   aadcdn.msftauth.net

Management point
Starting in version 2603, the management point requires internet access to validate Microsoft
Entra tokens using Microsoft Identity Service Essentials (MISE). This requirement applies to
environments that support Microsoft Entra joined users and devices, especially when using a
cloud management gateway (CMG).

Allow the management point server to access the following endpoints:

Azure public cloud:

        https://login.microsoftonline.com

        https://sts.windows.net

Azure US Government cloud:

        https://login.microsoftonline.us

        https://sts.windows.net

For more information, see Management point requires internet access for Microsoft Entra token
validation.

Software updates

<!-- p.538 -->

Allow the active software update point to access the following endpoints so that WSUS and
Automatic Updates can communicate with the Microsoft Update cloud service:

     http://windowsupdate.microsoft.com

     http://*.windowsupdate.microsoft.com

     https://*.windowsupdate.microsoft.com

     http://*.update.microsoft.com

     https://*.update.microsoft.com

     http://*.windowsupdate.com

     http://download.windowsupdate.com

     http://download.microsoft.com

     http://*.download.windowsupdate.com

     http://ntservicepack.microsoft.com

For more information on software updates, see Plan for software updates.

Intranet firewall
You might need to add endpoints to a firewall that's between two site systems in the following
cases:

     If child sites have a software update point
     If there's a remote active internet-based software update point at a site

Software update point on the child site

     http://<FQDN for software update point on child site>

     https://<FQDN for software update point on child site>

     http://<FQDN for software update point on parent site>

     https://<FQDN for software update point on parent site>

Manage Microsoft 365 Apps

<!-- p.539 -->

  ７ Note

  On April 21, 2020, Office 365 ProPlus was renamed to Microsoft 365 Apps for enterprise.
  For more information, see Name change for Office 365 ProPlus. You might still see
  references to the old name in the Configuration Manager console and supporting
  documentation while the console is being updated.

If you use Configuration Manager to deploy and update Microsoft 365 Apps for enterprise, allow
the following endpoints:

      officecdn.microsoft.com to synchronize the software update point for Microsoft 365 Apps

     for enterprise client updates

      config.office.com to create custom configurations for Microsoft 365 Apps for enterprise

     deployments

      https://clients.config.office.net and https://go.microsoft.com/fwlink/?linkid=2190568

     to support deploying updates for Microsoft 365 Apps for enterprise

      contentstorage.osi.office.net to support the evaluation of Office add-in readiness

      clients.config.office.net to retrieve the names of the files needed for a particular

     Microsoft 365 Apps update. For more information, see Using the Microsoft 365 Apps file list
     API.

Your top-level site server needs access to the following endpoint to download the Microsoft Apps
365 readiness file:

     Starting March 2, 2021:
      https://omex.cdn.office.net/mirrored/sccmreadiness/SOT_SCCM_AddinReadiness.CAB

        Location before March 2, 2021:
         https://contentstorage.osi.office.net/sccmreadinessppe/sot_sccm_addinreadiness.cab

  ７ Note

  The location of this file is changing March 2, 2021. For more information, see Download
  location change for Microsoft 365 Apps readiness file .

Configuration Manager console

<!-- p.540 -->

Computers with the Configuration Manager console require access to the following internet
endpoints for specific features:

  ７ Note

  For push notifications from Microsoft to show in the console, the service connection point
  needs access to Configmgrbits.cdn.manage.microsoft.com . It also needs access to this
  endpoint for updates and servicing.

In-console feedback
On the computer where you run the console, allow it to access the following internet endpoints
to send diagnostic data to Microsoft:

      petrol.office.microsoft.com

      ceuswatcab01.blob.core.windows.net

      ceuswatcab02.blob.core.windows.net

      eaus2watcab01.blob.core.windows.net

      eaus2watcab02.blob.core.windows.net

      weus2watcab01.blob.core.windows.net

      weus2watcab02.blob.core.windows.net

      umwatsonc.events.data.microsoft.com

      *-umwatsonc.events.data.microsoft.com

For more information on this feature, see Product feedback.

Community workspace
Documentation node

For more information on this console node, see Using the Configuration Manager console.

      https://aka.ms

      https://raw.githubusercontent.com

<!-- p.541 -->

Community hub

For more information on this feature, see Community hub.

      https://github.com

      https://communityhub.microsoft.com

Tenant attach
For more information, see Enable tenant attach.

      https://aka.ms/configmgrgateway

      https://*.manage.microsoft.com for Azure public cloud customers

      https://*.manage.microsoft.us for US Government cloud customers on version 2107 or later

      https://dc.services.visualstudio.com

The service connection point makes a long standing outgoing connection to the notification
service hosted on https://*.manage.microsoft.com . Verify the proxy used for the service
connection point doesn't time out outgoing connections too quickly. We recommend 3 minutes
for outgoing connections to this internet endpoint.

If your environment has proxy rules to allow only specific certificate revocation lists (CRLs) or
online certificate status protocol (OCSP) verification locations, also allow the following CRL and
OCSP URLs:

      http://crl3.digicert.com

      http://crl4.digicert.com

      http://ocsp.digicert.com

      http://www.d-trust.net

      http://root-c3-ca2-2009.ocsp.d-trust.net

      http://crl.microsoft.com

      http://oneocsp.microsoft.com

      http://ocsp.msocsp.com

      http://www.microsoft.com/pkiops

Endpoint analytics
For more information, see Endpoint analytics proxy configuration.

<!-- p.542 -->

Endpoints required for Configuration Manager-
managed devices
Configuration Manager-managed devices send data to Intune via the connector on the
Configuration Manager role and they don't need directly access to the Microsoft public cloud.

                                                                                          ﾉ   Expand table

 Endpoint                         Function

 https://graph.windows.net        Used to automatically retrieve settings when attaching your hierarchy to
                                  Endpoint analytics on Configuration Manager server role. For more
                                  information, see Configure the proxy for a site system server.

 https://*.manage.microsoft.com   Used to synch device collection and devices with Endpoint analytics on
                                  Configuration Manager server role only. For more information, see
                                  Configure the proxy for a site system server.

Endpoints required for Intune-managed devices
To enroll devices to Endpoint analytics, they need to send required functional data to Microsoft
public cloud. Endpoint Analytics uses the Windows client and Windows Server Connected User
Experiences and Telemetry component (DiagTrack) to collect the data from Intune-managed
devices. Make sure that the Connected User Experiences and Telemetry service on the device is
running.

                                                                                          ﾉ   Expand table

 Endpoint                              Function

 https://*.events.data.microsoft.com   Used by Intune-managed devices to send required functional data
                                       to the Intune data collection endpoint.

Asset intelligence
If you use asset intelligence, allow the following endpoints for the service to synchronize:

     https://sc.microsoft.com

     https://ssu2.manage.microsoft.com

Deploy Microsoft Edge

<!-- p.543 -->

The device running the Configuration Manager console needs access to the following endpoints
for deploying Microsoft Edge:

                                                                                     ﾉ   Expand table

 Location                                                     Use

 https://aka.ms/cmedgeapi                                     Information about releases of Microsoft
                                                              Edge

 https://edgeupdates.microsoft.com/api/products?              Information about releases of Microsoft
 view=enterprise                                              Edge

 http://dl.delivery.mp.microsoft.com                          Content for Microsoft Edge releases

External notifications
For more information, see External notifications.

The service connection point needs to communicate with the notification service, for example
Azure Logic Apps. The access endpoint for the logic app typically has the following format:
https://*.<RegionName>.logic.azure.com:443 . For example:

https://prod1.westus2.logic.azure.com:443

To get the access endpoint for the logic app, and the associated IP addresses, use the following
process:

   1. In the Azure portal, under Logic Apps, select the logic app for your notification. For more
     information, see Manage logic apps in the Azure portal.
   2. In the app's menu, in the Settings section, select Properties.
   3. View or copy the values for the Access endpoint and the Access endpoint IP addresses.

Microsoft public IP addresses
For more information on the Microsoft IP address ranges, see Microsoft Public IP Space        . These
addresses update regularly. There's no granularity by service; Any IP address in these ranges
could be used.

Next steps
     Ports used in Configuration Manager

<!-- p.544 -->

     Proxy server support in Configuration Manager

Last updated on 06/08/2026

<!-- p.545 -->

About schema extensions for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can extend the Active Directory schema to support Configuration Manager. This
action edits a forest's Active Directory schema to add a new container and several
attributes. Configuration Manager sites use these extensions to publish key information
in Active Directory where clients can securely access it. This information can simplify the
deployment and configuration of clients. It also helps clients locate site resources like
servers with deployed content or that provide different services to clients.

Microsoft recommends that you extend your Active Directory schema for Configuration
Manager, but it's not required.

Before you extend the Active Directory schema, you should be familiar with Active
Directory Domain Services and comfortable with modifying the Active Directory schema.

Considerations
      There are no new Active Directory schema extensions for Configuration Manager
      current branch. They haven't changed since Configuration Manager 2007. If you
      previously extended the schema an earlier version, you don't have to extend the
      schema again.

      Extending the schema is a forest-wide, one-time, irreversible action.

      Only a member of the Schema Admins group can extend the schema. It can also
      be a user with delegated permissions to change the schema.

      You can extend the schema before or after you install a Configuration Manager
      site. However, it's best to extend the schema before you start to configure your
      sites and hierarchy settings. This action can simplify many of the later
      configuration steps.

      After you extend the schema, the Active Directory global catalog replicates
      throughout the forest. Plan to extend the schema when the replication traffic won't
      adversely affect other network-dependent processes. Active Directory only
      replicates the newly added attributes.

<!-- p.546 -->

Devices and clients that don't use the Active Directory
schema
     Mobile devices that are managed by the Exchange Server connector

     The client for macOS computers

     Mobile devices that are enrolled by Configuration Manager on-premises MDM

     Windows clients that you configure for internet-only client management

     Windows clients that Configuration Manager detects to be on the internet

Features that benefit
The following Configuration Manager features benefit from extending the Active
Directory schema.

Client computer installation and site assignment
When you install a new client on a Windows computer, it searches Active Directory
Domain Services for installation properties.

If you don't extend the schema, use one of the following options to provide
configuration details:

     Use client push installation. This method uses the client installation properties that
     you configure in the Configuration Manager console.

     Use manual installation. Provide at least the following client installation properties
     on the command line:

        Specify a management point or source path from which the computer can
        download the installation files. Use the CCMSetup property /mp or /source .

        Specify a list of initial management points for the client to use. It uses this initial
        management point to assign to the site and download client policy and site
        settings. Use the CCMSetup Client.msi property SMSMP .

     For more information, see About client installation parameters and properties.

     Publish the management point in DNS. Configure clients to use this service
     location method.

<!-- p.547 -->

Port configuration for client-to-server communication
When a client installs, it uses the port information from Active Directory. If you later
change the client-to-server communication port for a site, clients get this new port
setting from Active Directory.

If you don't extend the schema, use one of the following options to provide new port
configurations to existing clients:

      Reinstall clients. Use options that configure the new port.

      Deploy a custom script to clients that updates the communication port. If clients
      can't communicate with a site because of a port change, you can't use
      Configuration Manager to deploy this script. For example, you could use group
      policy.

Content deployment scenarios
When you create content at one site, and then deploy that content to another site in the
hierarchy, the receiving site tries to verify the signature of the signed content data. This
behavior requires access to the public key of the source site where you create this
content. When you extend the Active Directory schema for Configuration Manager, a
site's public key is available to all sites in the hierarchy.

If you don't extend the schema, use the hierarchy maintenance tool, preinst.exe, to
exchange the secure key information between sites.

For example, you plan to create content at a primary site and then deploy that content
to a secondary site below a different primary site. If you extend the Active Directory
schema, the secondary site automatically gets the source primary site's public key.
Otherwise, use preinst.exe to share keys between the two sites directly.

Active Directory attributes and classes
When you extend the schema for Configuration Manager, the following classes and
attributes are added to the schema and available to all Configuration Manager sites in
that Active Directory forest.

                                                                           ﾉ   Expand table

<!-- p.548 -->

 Attributes                                    Classes

 cn=mS-SMS-Assignment-Site-Code                cn=MS-SMS-Management-Point
 cn=mS-SMS-Capabilities                        cn=MS-SMS-Roaming-Boundary-Range
 cn=MS-SMS-Default-MP                          cn=MS-SMS-Server-Locator-Point
 cn=mS-SMS-Device-Management-Point             cn=MS-SMS-Site
 cn=mS-SMS-Health-State
 cn=MS-SMS-MP-Address
 cn=MS-SMS-MP-Name
 cn=MS-SMS-Ranged-IP-High
 cn=MS-SMS-Ranged-IP-Low
 cn=MS-SMS-Roaming-Boundaries
 cn=MS-SMS-Site-Boundaries
 cn=MS-SMS-Site-Code
 cn=mS-SMS-Source-Forest
 cn=mS-SMS-Version

  ７ Note

  The schema extensions might include attributes and classes from previous versions
  of the product but not used by the latest version. For example:

        Attribute: cn=MS-SMS-Site-Boundaries
        Class: cn=MS-SMS-Server-Locator-Point

You can view these settings in the ConfigMgr_ad_schema.LDF file from the
\SMSSETUP\BIN\x64 folder of the Configuration Manager installation media.

Next steps
Prepare Active Directory for site publishing

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.549 -->

Prepare Active Directory for site
publishing
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you extend the Active Directory schema for Configuration Manager, you
introduce new structures to Active Directory. Configuration Manager sites use these new
structures to publish key information in a secure location where clients can easily access
it.

When you manage on-premises clients, you should extend the Active Directory schema
for Configuration Manager. An extended schema can simplify the process of deploying
and setting up clients. An extended schema also lets clients efficiently locate resources
like content servers. Extending the schema is a one-time action for any forest.

If you're not familiar with the benefits of an extended schema for Configuration
Manager, see Schema extensions for Configuration Manager.

When you don't use an extended schema, you can set up other methods like DNS to
locate services and site system servers. These methods of service location require other
configurations and aren't the preferred method for service location by clients. For more
information, see Understand how clients find site resources and services for
Configuration Manager.

If your Active Directory schema was extended for Configuration Manager 2007 or
System Center 2012 Configuration Manager, then you don't need to do more. The
schema extensions are unchanged and are already in place.

Step 1: Extend the schema
To extend the schema for Configuration Manager:

      Use an account that's a member of the Schema Admins security group.

      Sign in with that account to the schema master domain controller.

Then use one of the following options to add the new classes and attributes to the
Active Directory schema.

Option A: Use the extadsch.exe tool

<!-- p.550 -->

This tool is in the SMSSETUP\BIN\X64 folder on the Configuration Manager installation
media.

   1. Open a command line, and run extadsch.exe.

          Tip

         Run this tool from a command line to view feedback while it runs.

   2. To verify that the schema extension was successful, review extadsch.log in the root
     of the system drive.

Option B: Use the LDIF file
This file is in the SMSSETUP\BIN\X64 folder on the Configuration Manager installation
media.

   1. Make a copy of the ConfigMgr_ad_schema.ldf file. Edit it in Notepad, and define
     the Active Directory root domain that you want to extend. Replace all instances of
     the text DC=x in the file with the full name of the domain to extend. For example, if
     the full name of the domain to extend is named widgets.contoso.com, change all
     instances of DC=x in the file to DC=widgets, DC=contoso, DC=com .

   2. Use the LDIFDE command-line utility to import the contents of the
     ConfigMgr_ad_schema.ldf file to Active Directory Domain Services. For example,
     the following command-line imports the schema extensions, turns on verbose
     logging, and creates a log file in the temp directory:

     ldifde -i -f ConfigMgr_ad_schema.ldf -v -j "%temp%"

     For more information, see Command-line reference: Ldifde.

   3. To verify that the schema extension was successful, review the ldifde log file.

Step 2: The System Management container
After you extend the schema, create a container named System Management in Active
Directory Domain Services. Create this container once in each domain that has a
Configuration site that will publish data to Active Directory. For each container, you
need to grant permissions to the computer account of each site server that will publish
data to that domain.

<!-- p.551 -->

   1. Use an account that has the Create All Child Objects permission on the System
     container in Active Directory Domain Services.

   2. Run ADSI Edit (adsiedit.msc), and connect to the site server's domain.

   3. Create the container:

      a. Expand the fully qualified domain name, and expand the distinguished name.
        Right-click CN=System, choose New, and then select Object.

     b. In the Create Object window, select Container, and then select Next.

      c. In the Value box, enter System Management , and then select Next.

   4. Assign permissions:

       ７ Note

       If you prefer, you can use other tools like the Active Directory Users and
       Computers administrative tool (dsa.msc) to add permissions to the container.

      a. Right-click CN=System Management, and select Properties.

     b. Switch to the Security tab. Select Add, and then add the site server's computer
        account with the Full Control permission.

        Add the computer account for each Configuration Manager site server in this
        domain. If you use site server high availability, make sure to include the
        computer account of the site server in passive mode.

      c. Select Advanced, select the site server's computer account, and then select Edit.

     d. In the Apply onto list, select This object and all descendant objects.

     e. Select OK to save the configuration.

Next steps
After you create the container and grant permissions, configure the Configuration
Manager site to publish data to Active Directory.

Publish site data for Configuration Manager

<!-- p.552 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.553 -->

Prepare Windows Servers to support
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you can use a Windows computer as a site system server for Configuration
Manager, it must meet the prerequisites for its intended use. These prerequisites often
include one or more Windows features or roles. Because the method to enable Windows
features and roles differs among OS versions, refer to the documentation for your OS
version for detailed information.

The information in this article provides an overview of the types of Windows
configurations that are required to support Configuration Manager site systems. For
configuration details for specific site system roles, see Site and site system prerequisites.

Windows features and roles
When you set up Windows features and roles on a computer, you might be required to
reboot the computer to complete that configuration. So before you install a
Configuration Manager site or site system server, identify computers that will host
specific site system roles.

Features
The following Windows features are required on certain site system servers. Set them up
before you install a site system role on that computer.

      .NET Framework: Different site system roles require different versions of .NET
      Framework.

      Background Intelligent Transfer Services (BITS): Management points require BITS
      to support communication with managed devices. This feature includes all
      automatically selected options.

      BranchCache: Distribution points can be set up with BranchCache to support
      clients.

      Data Deduplication: Distribution points can be set up with and benefit from data
      deduplication.

<!-- p.554 -->

     Remote Differential Compression (RDC): Each computer that hosts a site server or
     a distribution point requires RDC. RDC is used to generate package signatures and
     compare digital signatures.

Roles
The following Windows roles are required to support specific functionality, like software
updates and OS deployments. IIS is required by the most common site system roles.

     Network Device Enrollment Service (under Active Directory Certificate Services):
     This Windows role is a prerequisite to use certificate profiles in Configuration
     Manager.

     Web server (IIS): The following site system roles use IIS:
        Distribution point
        Enrollment point
        Enrollment proxy point
        Fallback status point
        Management point
        Software update point
        State migration point

     The minimum version of IIS that's required is the version that's supplied with the
     OS of the site server.

     Windows Deployment Services: This role is used with OS deployment.

     Windows Server Update Services: This role is required for software updates.

IIS request filtering for distribution points
By default, IIS uses request filtering to block several file name extensions and folder
locations from access by HTTP or HTTPS communication. On a distribution point, this
configuration prevents clients from downloading packages that have blocked extensions
or folder locations.

When your package source files have extensions that are blocked in IIS by your request
filtering configuration, set up request filtering to allow them. Use the IIS Manager to edit
the request filtering feature on your distribution point computers.

Additionally, the following file name extensions are used by Configuration Manager for
packages and applications. Make sure that your request filtering configurations don't
block these file extensions:

<!-- p.555 -->

     .PCK
     .PKG
     .STA
     .TAR

For example, source files for a software deployment might include a folder named bin or
have a file that has the .mdb file name extension.

     By default, IIS request filtering blocks access to these elements. Bin is blocked as a
     Hidden Segment and .mdb is blocked as a file name extension.

     When you use the default IIS configuration on a distribution point, clients that use
     BITS fail to download this software deployment from the distribution point and
     indicate that they're waiting for content.

     To let the clients download this content, on each applicable distribution point, edit
     Request Filtering in IIS Manager. Allow access to the file extensions and folders
     that are in the packages and applications that you deploy.

  ） Important

  Edits to the request filter can increase the attack surface of the computer.

        Edits that you make at the server level apply to all websites on the server.
        Edits that you make to individual websites apply to only that website.

  For best security, run Configuration Manager on a dedicated web server. If you
  need to run other applications on the web server, use a custom website for
  Configuration Manager. For information, see Websites for site system servers.

HTTP verbs
For more information, see Configure request filtering in IIS.

Management points
To make sure that clients can successfully communicate with a management point, on
the management point server make sure IIS allows the following HTTP verbs:

     GET
     POST
     CCM_POST

<!-- p.556 -->

     HEAD
     PROPFIND

Distribution points
Distribution points require that IIS allows the following HTTP verbs:

     GET
     HEAD
     PROPFIND

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.557 -->

Websites for site system servers in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Several Configuration Manager site system roles require the use of Internet Information
Services (IIS). By default, they use the default IIS website to host site system services.
When you run other web applications on the same server, and settings aren't
compatible with Configuration Manager, consider using a custom website for
Configuration Manager.

   Tip

  For improved security, dedicate a server for the Configuration Manager site
  systems that require IIS. When you run other applications on a Configuration
  Manager site system, you increase the attack surface of that computer.

Choosing to use custom websites
By default, site system roles use the Default Web Site in IIS. This configuration is set up
automatically when the site system role installs. However, at primary sites, you can
choose to use custom websites instead.

When you use custom websites:

      They're enabled for the entire site instead of for individual site system servers or
      roles.

      At primary sites, for each computer that will host an applicable site system role,
      configure it with a custom website named SMSWEB. Until you create this website,
      and set up site system roles on that computer to use the custom website, clients
      can't communicate with site system roles on that computer.

      Secondary sites are automatically set up to use a custom website when their
      primary parent site uses it. Create custom websites in IIS on each secondary site
      system server that requires IIS.

Prerequisites for using custom websites

<!-- p.558 -->

Before you enable the option to use custom websites at a site:

     Create a custom website named SMSWEB in IIS on each site system server that
     requires IIS. Set this configuration at the primary site and at any child secondary
     sites.

     Set up the custom website to respond to the same port that you set up for
     Configuration Manager client communication. This port is known as the client
     request port.

     For each custom or default website that uses a custom folder, place a copy of the
     default document type that you use in the root folder that hosts the website. For
     example, with the typical default configuration, iisstart.htm is one of several
     default document types that are available. You can find this file in the root of the
     default website. Place a copy of this file or other default document in the root
     folder that hosts the SMSWEB custom website. For more information about default
     document types, see Default Document for IIS.

About IIS requirements
The following site system roles require IIS and a website to host the site system services:

     Distribution point

     Enrollment point

     Enrollment proxy point

     Fallback status point

     Management point

     Software update point

     State migration point

Other considerations:

     When a primary site has custom websites enabled, clients that are assigned to that
     site are directed to communicate with the custom websites instead of the default
     websites.

     If you use custom websites for one primary site, consider custom websites for all
     primary sites in your hierarchy. This configuration makes sure that clients can
     successfully roam within the hierarchy. Roaming is when a client computer moves

<!-- p.559 -->

     to a new network segment that is managed by a different site. Roaming can affect
     resources that a client can access locally instead of across a WAN link.

     Site system roles that use IIS but don't accept client connections also use the
     SMSWEB website instead of the default website. For example, the reporting
     services point.

     Custom websites require you to assign port numbers that differ from the
     computer's default website. A default website and custom website can't run at the
     same time if both websites try to use the same TCP/IP ports.

     The TCP/IP ports that you set up in IIS for the custom website must match the
     client request ports for the site.

Switch between default and custom websites
Although you can check or uncheck the box for using custom websites at a primary site
at any time, plan carefully before you make this change. When this configuration
changes, all applicable site system roles at the primary site and child secondary sites
uninstall and then reinstall.

The following roles reinstall automatically:

     Management point

     Distribution point

     Software update point

     Fallback status point

     State migration point

You need to manually reinstall the following roles:

     Enrollment point

     Enrollment proxy point

When you change from the default website to use a custom website, Configuration
Manager doesn't remove the old virtual directories. If you want to remove the files that
Configuration Manager used, manually delete the virtual directories that were created
under the default website.

<!-- p.560 -->

If you change the site to use custom websites, clients that are already assigned to the
site need to be reconfigured to use the new client request ports for the custom
websites. For more information, see How to configure client communication ports.

Set up custom websites
The steps to create a custom website vary for different OS versions. For exact steps, refer
to the documentation for your OS version.

Use the following general information when applicable:

     The website name is SMSWEB.

     When you set up HTTPS, specify a PKI certificate before you can save the
     configuration.

     After you create the custom website, remove the custom website ports that you
     use from other websites in IIS:

         1. Edit the Bindings of the other websites to remove ports that match the ports
           that are assigned to the SMSWEB website.

         2. Start the SMSWEB website.

         3. Restart the SMS_SITE_COMPONENT_MANAGER service on the site server of
           the site.

Next steps
To configure the site to use a custom web site, enable the setting Use custom web site
on the Ports tab of the site properties. For more information, see Configure client
communication ports.

Feedback
Was this page helpful?      Yes    No

Provide product feedback
