---
title: "Exchange Server — pages 361-400"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0361-0400
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0361-0400
family: exchange
documentKind: "doc"
abstract: "Windows Server prerequisites for Exchange 2016 The requirements to install Exchange 2016 on supported Operating Systems (OS) are described in the following sections. We recommend either of the following methods to install the Windows prerequisites for Exchange 2016: Use the /Ins"
---

# Exchange Server — pages 361-400

<!-- p.361 -->

Windows Server prerequisites for Exchange 2016
The requirements to install Exchange 2016 on supported Operating Systems (OS) are described
in the following sections. We recommend either of the following methods to install the
Windows prerequisites for Exchange 2016:

     Use the /InstallWindowsComponents switch in unattended Setup mode.
     Select the check box in the Exchange Setup Wizard to install Windows prerequisites.

When you use one of these options, you don't need to restart the computer after the Windows
components have been added.

Exchange 2016 preparing Active Directory
You can use any member of the Active Directory domain to prepare Active Directory for
Exchange 2016. To prepare Active Directory using the graphical user interface (GUI), you need
to install the Exchange Management Tools role.

   1. The computer which is used to prepare the Active Directory requires the following
     software:

      a. Supported version of .NET Framework

     b. Visual C++ Redistributable Package for Visual Studio 2012

        If you're using unattended Setup from the command line to prepare Active Directory,
        this package isn't required. For an overview of the latest supported versions and more
        information, please refer to Prepare Active Directory and domains.

        The system requirements for the Visual C++ Redistributable package do not explicitly
        mention support for the latest Windows Server versions. However, the redistributable
        package is safe to install on these versions of Windows.

   2. Install the Remote Server Administration Tools (RSAT) for Active Directory Domain
     Services (ADDS) by running the following command in Windows PowerShell:

        PowerShell

        Install-WindowsFeature RSAT-ADDS

Exchange 2016 Management tools
   1. Install the following software:

<!-- p.362 -->

   a. Supported version of .NET Framework

   b. Visual C++ Redistributable Package for Visual Studio 2012

      The system requirements for the Visual C++ Redistributable package do not explicitly
      mention support for the latest Windows Server versions. However, the redistributable
      package is safe to install on these versions of Windows.

 2. Install the following Windows features:
   a. If you want to install the Exchange Server Management tools on supported Windows
      Server OS, make sure to install the following Windows features:

        PowerShell

        Install-WindowsFeature -Name Web-Mgmt-Console, Web-Metabase

   b. If you want to install the Exchange Server Management tools on supported Windows
      Client OS, make sure to install the following Windows features:

        PowerShell

        Enable-WindowsOptionalFeature -Online -FeatureName IIS-ManagementConsole,
        IIS-Metabase -All

Exchange 2016 Mailbox server role
 1. Run the following command in Windows PowerShell to install the required Windows
   components depending on the operating system on which you are installing Exchange
   Server:

   a. Windows Server 2016

        PowerShell

        Install-WindowsFeature NET-Framework-45-Core, NET-Framework-45-ASPNET, NET-
        WCF-HTTP-Activation45, NET-WCF-Pipe-Activation45, NET-WCF-TCP-Activation45,
        NET-WCF-TCP-PortSharing45, Server-Media-Foundation, RPC-over-HTTP-proxy,
        RSAT-Clustering, RSAT-Clustering-CmdInterface, RSAT-Clustering-Mgmt, RSAT-
        Clustering-PowerShell, WAS-Process-Model, Web-Asp-Net45, Web-Basic-Auth,
        Web-Client-Auth, Web-Digest-Auth, Web-Dir-Browsing, Web-Dyn-Compression,
        Web-Http-Errors, Web-Http-Logging, Web-Http-Redirect, Web-Http-Tracing,
        Web-ISAPI-Ext, Web-ISAPI-Filter, Web-Lgcy-Mgmt-Console, Web-Metabase, Web-
        Mgmt-Console, Web-Mgmt-Service, Web-Net-Ext45, Web-Request-Monitor, Web-
        Server, Web-Stat-Compression, Web-Static-Content, Web-Windows-Auth, Web-
        WMI, Windows-Identity-Foundation, RSAT-ADDS

<!-- p.363 -->

     or

  b. Windows Server 2012 (R2)

          PowerShell

          Install-WindowsFeature AS-HTTP-Activation, Server-Media-Foundation, NET-
          Framework-45-Core, NET-Framework-45-ASPNET, NET-WCF-HTTP-Activation45, NET-
          WCF-Pipe-Activation45, NET-WCF-TCP-Activation45, NET-WCF-TCP-PortSharing45,
          RPC-over-HTTP-proxy, RSAT-Clustering, RSAT-Clustering-CmdInterface, RSAT-
          Clustering-Mgmt, RSAT-Clustering-PowerShell, WAS-Process-Model, Web-Asp-
          Net45, Web-Basic-Auth, Web-Client-Auth, Web-Digest-Auth, Web-Dir-Browsing,
          Web-Dyn-Compression, Web-Http-Errors, Web-Http-Logging, Web-Http-Redirect,
          Web-Http-Tracing, Web-ISAPI-Ext, Web-ISAPI-Filter, Web-Lgcy-Mgmt-Console,
          Web-Metabase, Web-Mgmt-Console, Web-Mgmt-Service, Web-Net-Ext45, Web-
          Request-Monitor, Web-Server, Web-Stat-Compression, Web-Static-Content, Web-
          Windows-Auth, Web-WMI, Windows-Identity-Foundation, RSAT-ADDS

2. Install the following software in order:

   a. Supported version of .NET Framework

  b. Install KB3206632 or KB2999226 depending on the operating system on which you are
     installing Exchange Server

      i. Windows Server 2016: December 13, 2016 (KB3206632) security update

          You can only install this update if your Windows Server 2016 version is 14393.576 or
          earlier. You can check your Windows Server version by running the winver
          command. If your Windows Server 2016 version is greater than 14393.576 , you
          don't need this update or its replacement KB3213522       . Exchange 2016 setup looks
          for the installation of this update, won't allow you to continue if this update is
          missing, and informs you if you need it.

      ii. Windows Server 2012 (R2): Update for Universal C Runtime in Windows
          (KB2999226)

          The Update for Universal C Runtime in Windows (KB2999226) is required on Server
          2012 R2 with Cumulative Update 22 or later.

   c. Visual C++ Redistributable Package for Visual Studio 2012

  d. Visual C++ Redistributable Package for Visual Studio 2013

   e. IIS URL Rewrite Module

   f. Microsoft Unified Communications Managed API 4.0, Core Runtime 64-bit

<!-- p.364 -->

Exchange 2016 Edge Transport server role
 1. Run the following command in Windows PowerShell to install the required Windows
   components:

      PowerShell

      Install-WindowsFeature ADLDS

 2. Install the following software in order:
    a. Supported version of .NET Framework
   b. Visual C++ Redistributable Package for Visual Studio 2012

<!-- p.365 -->

Install Office Online Server in an Exchange
organization
Article • 04/30/2025

APPLIES TO:          2016    2019     Subscription Edition

An optional prerequisite for Exchange 2016 Cumulative Update 1 (CU1) or later, as well as for
Exchange 2019, is the installation of Office Online Server on one or more servers in your
organization. Office Online Server enables users to view supported file attachments within
Outlook on the web (formerly known as Outlook Web App) without downloading them first
and without having a local installation of the program. Without Office Online Server installed,
Outlook users need to download attachments to their local computer and then open them in a
local application.

  ７ Note

  Office Online Server is available for download as part of a volume licensing agreement. If
  you don't have a volume license agreement, you can skip the instructions in this step.
  However, without Office Online Server installed, Outlook users will need to download
  attachments to their local computer to view them; they won't be able to view them in
  Outlook.

You can configure an Office Online Server endpoint in two places in Exchange 2016 and later:
at the organization level, and at the Mailbox server level. Where you configure the endpoint
depends on the size of your organization and the location of your servers and users.

      Organization: There are a couple of reasons why you might configure the Office Online
      Server endpoint at the organization level:

         Single-server or single-location deployment: You can configure the endpoint at the
         organization level if all of your Exchange 2016 Mailbox servers are in the same location
         and you don't plan on having geographically distributed Office Online Server servers.

         Fallback for large deployments: You can configure endpoint at the organization level
         as a fallback if the endpoint configured on a Mailbox server isn't available. If an Office
         Web Apps server isn't available, the client will try to connect to the endpoint
         configured at the organization level.

         Notes:

             If you have Exchange 2013 servers in your organization, don't configure an endpoint
             at the organization level. Doing so will direct Exchange 2013 servers to use the

<!-- p.366 -->

           Office Online Server server. This isn't supported.

           Previewing attachments in S/MIME messages in Outlook on the web isn't supported
           by Office Online Server.

     Mailbox server: If you want to distribute client requests between two or more Office
     Online Server servers, if you want to geographically distribute Office Online Server
     servers, or if you have Exchange 2013 in your organization, configure the endpoints at the
     Exchange Mailbox server level. When you configure an endpoint at the server level,
     mailboxes located on that server will send requests to the configured Office Online Server
     server.

If you want users outside of your network to view supported file attachments in Outlook, Office
Online Server needs to be accessible from the Internet. TCP port 443 needs to be opened on
your firewall and forwarded to the Office Online Server server. If you deploy more than one
Office Online Server server, each server needs its own fully qualified domain name (FQDN).
Each server also needs to be accessible from the Internet via TCP port 443.

Office Online Server system requirements
To set up Office Online Server, you will need the following:

     Windows Server 2012 R2 or Windows Server 2016

     Exchange 2016 Cumulative Update 1 (CU1) or later, or Exchange 2019

        ７ Note

        If you're running Windows Server 2016, you will need Exchange 2016 CU3 or later, as
        detailed in Exchange Server prerequisites.

     Microsoft .NET Framework 4.5.2

     Visual C++ Redistributable for Visual Studio 2015

     Visual C++ Redistributable Packages for Visual Studio 2013

     Microsoft.IdentityModel.Extention.dll

     All available Windows updates installed

  ７ Note

<!-- p.367 -->

  Office Online Server can't be installed on an Exchange server, SharePoint server, Active
  Directory domain controller, or any other computer with existing applications installed.

Install Office Online Server
   1. To install Office Online Server, follow Steps 1 through 3 in the section Prepare servers to
     run Office Online Server of the article Deploy Office Online Server before proceeding.

   2. Obtain and import an SSL certificate with the fully qualified domain name(s) (FQDN) of
     the Office Online Server server. If your organization is configured for split DNS, you only
     need to configure one FQDN on the certificate. For example, oos.contoso.com. If you
     have different internal and external FQDNs, you'll need to configure both FQDNs on the
     certificate. For example, oos.internal.contoso.com and oos.contoso.com.

   3. Configure DNS records to point the FQDN(s) on the certificate to your Office Online
     Serverserver. If you have different DNS servers for internal and external users, you'll need
     to configure the appropriate FQDN on each server.

   4. Open Windows PowerShell and run the following commands. When you run the
     commands, replace the example FQDNs and certificate friendly name with your own.

        PowerShell

        New-OfficeWebAppsFarm -InternalURL "https://oos.contoso.com" -ExternalURL
        "https://oos.contoso.com" -CertificateName "Office Online Server Preview
        Certificate"`

        ７ Note

        You can configure different internal and external URLs, but in the next step you'll see
        that you can only configure one URL for Exchange. In this case, if you use the internal
        URL in the next step, this function will only work internally and external users will get
        an unexpected error. If you use the external URL, this function will only work for
        external users and internal users will get an unexpected error.

Configure the Office Online Server endpoint at the
Mailbox server level
After you've configured the Office Online Server server, do the following on your Exchange
2016 server. This will allow Outlook to send requests to the Office Online Server server.

<!-- p.368 -->

   1. Open the Exchange Management Shell and run the following command. Replace the
     example server name and URL with your own.

        PowerShell

        Set-MailboxServer MBX -WacDiscoveryEndpoint
        "https://oos.contoso.com/hosting/discovery"

   2. Restart the MsExchangeOwaAppPool by running the following command.

        PowerShell

        Restart-WebAppPool MsExchangeOwaAppPool

Configure the Office Online Server endpoint at the
organization level
After you've configured the Office Online Server server, do the following on your Exchange
2016 server. This will allow Outlook to send requests to the Office Online Server server.

   1. Open the Exchange Management Shell and run the following command. Replace the
     example URL with your own.

        PowerShell

        Set-OrganizationConfig -WacDiscoveryEndpoint
        "https://oos.internal.contoso.com/hosting/discovery"

        ） Important

        If you have Exchange 2013 servers in your organization, don't configure an endpoint
        at the organization level. Doing so will direct Exchange 2013 servers to use the Office
        Online Server server. This isn't supported.

   2. Restart the MsExchangeOwaAppPool by running the following command.

        PowerShell

        Restart-WebAppPool MsExchangeOwaAppPool

<!-- p.369 -->

Active Directory in Exchange Server
organizations
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Exchange Server 2016 and Exchange Server 2019 use Active Directory to store and share
directory information with Windows. Starting with Exchange 2013, we've made some changes
to how Exchange works with Active Directory. These changes are described in this topic.

Active Directory driver
The Active Directory driver is the core Microsoft Exchange component that allows Exchange
services to create, modify, delete, and query for Active Directory Domain Services (AD DS) data.
In Exchange 2013 and later, all access to Active Directory is done using the Active Directory
driver itself. In previous versions of Exchange, DSAccess provided directory lookup services for
components such as SMTP, message transfer agent (MTA), and the Exchange store.

The Active Directory driver also uses the Microsoft Exchange Active Directory Topology
(MSExchangeADTopology) server, which allows the Active Directory driver to use Directory
Service Access (DSAccess) topology data. This data includes the list of available domain
controllers and global catalog servers that are available to handle Exchange requests. For more
information about the Active Directory Driver, see Active Directory Domain Services.

Active Directory schema changes
Exchange add new attributes to the Active Directory domain service schema and also make
other modifications to existing classes and attributes. For more information about Active
Directory changes when you install Exchange, see Active Directory schema changes in
Exchange Server.

For more information
To learn more about how Exchange stores and retrieves information in Active Directory so that
you can plan for access to it, see Access to Active Directory in Exchange Server.

For more information about Active Directory forest design, see AD DS Design Guide.

To learn more about computers running Windows in an Active Directory domain and deploying
Exchange 2013 or later in a domain that has a disjoint namespace, see Disjoint Namespace

<!-- p.370 -->

Scenarios.

<!-- p.371 -->

Access to Active Directory by Exchange
servers
Article • 04/30/2025

APPLIES TO:        2016     2019        Subscription Edition

Exchange Server 2016 and Exchange Server 2019 store all configuration and recipient
information in the Active Directory directory service database. When an Exchange server
requires information about recipients the configuration of the Exchange organization, it queries
Active Directory. Active Directory servers must be available for Exchange to function correctly.

This topic explains how Exchange stores and retrieves information in Active Directory so that
you can plan access to Active Directory. This topic also discusses issues you should be aware of
if you try to recover deleted Exchange Active Directory objects.

Exchange information stored in Active Directory
The Active Directory database stores information in three types of logical partitions that are
described in the following sections:

      Schema partition

      Configuration partition

      Domain partition

Schema partition
The schema partition stores the following two types of information:

      Schema classes define all the types of objects that can be created and stored in Active
      Directory.

      Schema attributes define all the properties that can be used to describe the objects that
      are stored in Active Directory.

When you install the first Exchange server in the forest (or run the Active Directory preparation
process), the Active Directory preparation process adds many classes and attributes to the
Active Directory schema. The classes that are added to the schema are used to create
Exchange-specific objects (for example, agents and connectors). These attributes are used to
configure the Exchange-specific objects and the mail-enabled users and groups. These

<!-- p.372 -->

attributes include properties, such as Outlook on the web (formerly known as Outlook Web
App) settings.

Every domain controller and global catalog server in the forest contains a complete replica of
the schema partition.

For more information about schema modifications in Exchange, see Active Directory schema
changes in Exchange Server.

Configuration partition
The configuration partition stores information about the forest-wide configuration. This
configuration information includes the configuration of Active Directory sites, Exchange global
settings, transport settings, and mailbox policies. Each type of configuration information is
stored in a container in the configuration partition. Exchange configuration information is
stored in a subfolder under the configuration partition's Services container. The type of
information that's stored in this container includes:

     Address lists

     Address book mailbox policies

     Administrative groups

     Client Access settings

     Connections

     Mobile mailbox Settings

     Global settings

     Monitoring Settings

     System policies

     Retention policies container

     Transport settings

Every domain controller and global catalog server in the forest contains a complete replica of
the configuration partition.

Domain partition

<!-- p.373 -->

The domain partition stores information in default containers and in organizational units that
are created by the Active Directory administrator. These containers hold the domain-specific
objects. This data includes Exchange system objects and information about the computers,
users, and groups in that domain. When Exchange is installed, Exchange updates the objects in
this partition to support Exchange functionality. This functionality affects how recipient
information is stored and accessed.

Each domain controller contains a complete replica of the domain partition for the domain for
which it is authoritative. Every global catalog server in the forest contains a subset of the
information in every domain partition in the forest.

How Exchange accesses information in Active
Directory
Exchange uses an Active Directory API to access information that's stored in Active Directory.
This service reads information from all Active Directory partitions. The data that is retrieved is
cached and is used by Exchange servers to discover the Active Directory site location of all
Exchange services in the organization.

For more information about topology and service discovery in Exchange 2013 or later, see
Planning to use Active Directory sites for routing Mail.

Exchange is an Active Directory site-aware application that prefers to communicate with the
directory servers that are located in the same site as the Exchange server to optimize network
traffic. Each Exchange server must communicate with Active Directory to retrieve information
about recipients and information about the other Exchange servers. Mailbox servers store
configuration information about mailbox users and mailbox stores in Active Directory.
Additionally, the Mailbox server stores information in Active Directory for the Client Access
protocols, Transport service, Mailbox databases, and so on. The Mailbox server handles all
activity for the active mailboxes on that server.

By default, whenever an Exchange server starts, it binds to a randomly selected domain
controller and global catalog server in its own site. You can view the selected directory servers
by using the Get-ExchangeServer cmdlet in the Exchange Management Shell. You can also use
the Set-ExchangeServer cmdlet to configure a static list of domain controllers that an
Exchange 2016 server should bind to or a list of domain controllers that should be excluded.

  ） Important

  You can't deploy an Exchange server in any site that contains only read-only directory
  servers.

<!-- p.374 -->

Recovery of deleted Exchange objects
Active Directory Recycle Bin helps minimize directory service downtime by enhancing your
ability to preserve and recover accidentally deleted Active Directory objects without restoring
Active Directory data from backups, restarting Active Directory Domain Services (AD DS), or
rebooting domain controllers.

The most important thing to understand about recovering deleted Exchange-related Active
Directory objects is that Exchange objects don't exist in isolation. For example, when you mail-
enable a user, several different policies and links are calculated for the user based on your
current Exchange configuration. Two problems that may arise when you restore a deleted
Exchange configuration or recipient object are:

     Collisions: Some Exchange attributes must be unique across a forest. For example, all
     email addresses on a mail-enabled object (also known as proxy addresses) must be
     unique. Two different mail-enabled objects can't have the same email address. Active
     Directory doesn't enforce proxy address uniqueness (Exchange administrative tools check
     for uniqueness). Exchange email address policies also automatically resolve possible
     conflicts in proxy address assignment based on deterministic rules. Therefore, restoring
     an Exchange user object might create a collision with proxy addresses or other attributes
     that should be unique.

     Misconfigurations: Exchange has automated rules that assign various policies or settings.
     If you delete a recipient, and then change the rules or policies, restoring an Exchange user
     object may result in a user being assigned to the wrong policy (or even to a policy that no
     longer exists).

The following guidelines will help you minimize problems or issues when you recover deleted
Exchange-related objects:

     If you deleted an Exchange configuration object using Exchange management tools, don't
     restore the object. Instead, create the object again using the Exchange management tools
     (the Exchange admin center or the Exchange Management Shell).

     If you deleted an Exchange configuration object without using the Exchange
     management tools, recover the object as soon as possible. The more administrative and
     configuration changes that are made after the deletion, the more likely that restoring the
     objects will result in misconfiguration.

     If you recover deleted Exchange recipients (contacts, users, or distribution groups),
     monitor closely for collisions and errors relating to the recovered objects. If Exchange
     policies or other recipient configuration settings were modified after the deletion, re-

<!-- p.375 -->

     apply the current policies to the restored recipients to ensure that they're configured
     correctly.

For more information
Active Directory Recycle Bin Step-by-Step Guide

Introduction to Active Directory Administrative Center Enhancements (Level 100)

Advanced AD DS Management Using Active Directory Administrative Center (Level 200)

<!-- p.376 -->

Active Directory schema changes in
Exchange Server SE
06/16/2025

APPLIES TO:       2016      2019       Subscription Edition

   Tip

  Looking for the Active Directory schema changes for Exchange Server 2019? See Active
  Directory schema changes in Exchange Server 2019.

This reference topic provides a summary of the Active Directory schema changes that are made when
you install Exchange Server SE in your organization. Refer to the .ldf files for more information
about changes to the Active Directory schema. The .ldf files are located in the \Setup\Data\
directory in the Exchange installation files.

Exchange schema updates are cumulative. Each Cumulative Update (CU) includes all of the changes
that were included in previous releases. This means that if you skip a CU, you might still need to
apply schema updates even if the CU that you're installing doesn't include its own changes.

Exchange SE RTM Active Directory schema changes
This section summarizes the changes that are made to the Active Directory schema when you install
Exchange SE RTM. This section includes the following subsections:

     Classes added by Exchange SE RTM
     Classes modified by Exchange SE RTM
     Attributes added by Exchange SE RTM
     Global catalog attributes added by Exchange SE RTM
     Attributes modified by Exchange SE RTM
     Object IDs added by Exchange SE RTM
     Indexed attributes added by Exchange SE RTM
     Property sets modified by Exchange SE RTM
     MAPI IDs added by Exchange SE RTM
     Extended rights added by Exchange SE RTM

Classes added by Exchange SE RTM

                                                                                      ﾉ   Expand table

<!-- p.377 -->

Class                                           Change

Exch-Mapi-Virtual-Directory                     ntdsSchemaAdd

Exch-Push-Notifications-App                     ntdsSchemaAdd

ms-Exch-Account-Forest                          ntdsSchemaAdd

ms-Exch-ActiveSync-Device-Autoblock-Threshold   ntdsSchemaAdd

ms-Exch-Auth-Auth-Config                        ntdsSchemaAdd

ms-Exch-Auth-Auth-Server                        ntdsSchemaAdd

ms-Exch-Auth-Partner-Application                ntdsSchemaAdd

ms-Exch-Auth-Policy                             ntdsSchemaAdd

ms-Exch-Client-Access-Rule                      ntdsSchemaModify

ms-Exch-Config-Settings                         ntdsSchemaAdd

ms-Exch-Encryption-Virtual-Directory            ntdsSchemaAdd

ms-Exch-Exchange-Transport-Server               ntdsSchemaAdd

ms-Exch-Hosted-Content-Filter-Config            ntdsSchemaAdd

ms-Exch-Http-Delivery-Connector                 ntdsSchemaAdd

ms-Exch-Hygiene-Configuration                   ntdsSchemaAdd

ms-Exch-Intra-Organization-Connector            ntdsSchemaModify

ms-Exch-Mailbox-Policy                          ntdsSchemaAdd

ms-Exch-Mailflow-Policy                         ntdsSchemaAdd

ms-Exch-Mailflow-Policy-Collection              ntdsSchemaAdd

ms-Exch-Malware-Filter-Config                   ntdsSchemaAdd

ms-Exch-MSO-Forward-Sync-Divergence             ntdsSchemaAdd

ms-Exch-MSO-Sync-Service-Instance               ntdsSchemaAdd

ms-Exch-Organization-Upgrade-Policy             ntdsSchemaAdd

ms-Exch-Protocol-Cfg-SIP-Container              ntdsSchemaAdd

ms-Exch-Protocol-Cfg-SIP-FE-Server              ntdsSchemaAdd

ms-Exch-Resource-Policy                         ntdsSchemaAdd

ms-Exch-Safe-Attachment-Protection-Config       ntdsSchemaAdd

<!-- p.378 -->

Class                                                                        Change

ms-Exch-Smart-Links-Protection-Config                                        ntdsSchemaAdd

ms-Exch-Team-Mailbox-Provisioning-Policy                                     ntdsSchemaAdd

ms-Exch-Throttling-Policy                                                    ntdsSchemaModify

ms-Exch-Unified-Policy                                                       ntdsSchemaAdd

ms-Exch-Unified-Rule                                                         ntdsSchemaAdd

ms-Exch-Workload-Policy                                                      ntdsSchemaAdd

Classes modified by Exchange SE RTM

                                                                                        ﾉ    Expand table

Class                             Change            Attribute/Class

Mail-Recipient                    add: mayContain   msExchAdministrativeUnitLink

Mail-Recipient                    add: mayContain   msExchAuthPolicyLink

Mail-Recipient                    add: mayContain   msExchImmutableSid

Mail-Recipient                    add: mayContain   msExchUGEventSubscriptionLink

ms-Exch-Base-Class                add: mayContain   msExchUserHoldPolicies

ms-Exch-Configuration-Unit-       add: mayContain   msExchAuthPolicyLink
Container

ms-Exch-Configuration-Unit-       add: mayContain   msExchMSOForwardSyncReplayList
Container

ms-Exch-Container                 add: mayContain   msExchScopeFlags

ms-Exch-Mail-Storage              add: mayContain   msExchDataEncryptionPolicyLink

ms-Exch-Organization-Container    add: mayContain   msExchDataEncryptionPolicyLink

Exch-Accepted-Domain              add: mayContain   msExchOfflineOrgIdHomeRealmRecord

Exch-Base-Class                   add: mayContain   msExchCapabilityIdentifiers

Exch-Base-Class                   add: mayContain   msExchObjectID

Exch-Base-Class                   add: mayContain   msExchProvisioningTags

Exch-Configuration-Unit-          add: mayContain   msExchArchiveRelease
Container

<!-- p.379 -->

Class                             Change            Attribute/Class

Exch-Configuration-Unit-          add: mayContain   msExchMailboxRelease
Container

Exch-Exchange-Server              add: mayContain   msExchArchiveRelease

Exch-Exchange-Server              add: mayContain   msExchMailboxRelease

Exch-MDB-Availability-Group       add: mayContain   msExchEvictedMembersLink

Exch-OAB                          add: mayContain   msExchLastUpdateTime

Exch-OWA-Mailbox-Policy           add: mayContain   msExchConfigurationXML

Exch-OWA-Virtual-Directory        add: mayContain   msExchConfigurationXML

Exch-On-Premises-Organization     add: mayContain   msExchTrustedDomainLink

Exch-Organization-Container       add: mayContain   msExchMaxABP

Exch-Organization-Container       add: mayContain   msExchMaxOAB

Exch-Organization-Container       add: mayContain   pFContacts

Exch-Team-Mailbox-Provisioning-   add: mayContain   msExchConfigurationXML
Policy

Group                             add:              msExchMailStorage
                                  auxiliaryClass

Mail-Recipient                    add: mayContain   msExchLocalizationFlags

Mail-Recipient                    add: mayContain   msExchRoleGroupType

Mail-Recipient                    add: mayContain   ms-DS-GeoCoordinates-Altitude

Mail-Recipient                    add: mayContain   ms-DS-GeoCoordinates-Latitude

Mail-Recipient                    add: mayContain   ms-DS-GeoCoordinates-Longitude

Mail-Recipient                    add: mayContain   msExchRecipientSoftDeletedStatus

Mail-Recipient                    add: mayContain   msExchWhenSoftDeletedTime

Mail-Recipient                    add: mayContain   msExchHomeMTASL

Mail-Recipient                    add: mayContain   msExchMailboxMoveSourceArchiveMDBLinkSL

Mail-Recipient                    add: mayContain   msExchMailboxMoveSourceMDBLinkSL

Mail-Recipient                    add: mayContain   msExchMailboxMoveTargetArchiveMDBLinkSL

Mail-Recipient                    add: mayContain   msExchMailboxMoveTargetMDBLinkSL

Mail-Recipient                    add: mayContain   ms-exch-group-external-member-count

<!-- p.380 -->

Class                            Change            Attribute/Class

Mail-Recipient                   add: mayContain   ms-exch-group-member-count

Mail-Recipient                   add: mayContain   msExchGroupExternalMemberCount

Mail-Recipient                   add: mayContain   msExchGroupMemberCount

Mail-Recipient                   add: mayContain   msExchShadowWhenSoftDeletedTime

Mail-Recipient                   add: mayContain   msExchPublicFolderMailbox

Mail-Recipient                   add: mayContain   msExchPublicFolderSmtpAddress

Mail-Recipient                   add: mayContain   msExchAuxMailboxParentObjectIdLink

Mail-Recipient                   add: mayContain   msExchStsRefreshTokensValidFrom

Mail-Recipient                   add: mayContain   msDS-ExternalDirectoryObjectId

Mail-Recipient                   add: mayContain   msExchGroupSecurityFlags

Mail-Recipient                   add: mayContain   msExchMultiMailboxDatabasesLink

Ms-Exch-Organization-Container   add: mayContain   ms-exch-organization-flags-2

Top                              add: mayContain   msExchMultiMailboxDatabasesBL

Top                              add: mayContain   msExchMultiMailboxLocationsBL

Top                              add: mayContain   msExchAccountForestBL

Top                              add: mayContain   msExchTrustedDomainBL

Top                              add: mayContain   msExchAcceptedDomainBL

Top                              add: mayContain   msExchHygieneConfigurationMalwareBL

Top                              add: mayContain   msExchHygieneConfigurationSpamBL

Top                              add: mayContain   msExchEvictedMembersBL

Top                              add: mayContain   msExchOABGeneratingMailboxBL

Top                              add: mayContain   msExchAuxMailboxParentObjectIdBL

Top                              add: mayContain   msExchAdministrativeUnitBL

Top                              add: mayContain   msExchAuthPolicyBL

Top                              add: mayContain   msExchDataEncryptionPolicyBL

Top                              add: mayContain   msExchUGEventSubscriptionBL

ms-Exch-Auth-Auth-Server         add: mayContain   msExchCoexistenceDomains

<!-- p.381 -->

Class                           Change            Attribute/Class

ms-Exch-Accepted-Domain         add: mayContain   msExchHygieneConfigurationLink

ms-Exch-Accepted-Domain         add: mayContain   msExchTransportResellerSettingsLinkSL

ms-Exch-Account-Forest          possSuperiors     msExchContainer

ms-Exch-Account-Forest          add: mayContain   msExchPartnerId

ms-Exch-Active-Sync-Device      add: mayContain   msExchDeviceClientType

ms-Exch-Availability-Address-   add: mayContain   msExchFedTargetAutodiscoverEPR
Space

ms-Exch-Base-Class              add: mayContain   msExchDirsyncAuthorityMetadata

ms-Exch-Base-Class              add: mayContain   msExchDirsyncStatusAck

ms-Exch-Base-Class              add: mayContain   msExchEdgeSyncConfigFlags

ms-Exch-Base-Class              add: mayContain   msExchHABRootDepaPreviewentLink

ms-Exch-Base-Class              add: mayContain   msExchDefaultPublicFolderMailbox

ms-Exch-Base-Class              add: mayContain   msExchForestModeFlag

ms-Exch-Base-Class              add: mayContain   msExchELCMailboxFlags

ms-Exch-Base-Class              add: mayContain   msExchCanaryData0

ms-Exch-Base-Class              add: mayContain   msExchCanaryData1

ms-Exch-Base-Class              add: mayContain   msExchCanaryData2

ms-Exch-Base-Class              add: mayContain   msExchCorrelationId

ms-Exch-Base-Class              add: mayContain   msExchTenantCountry

ms-Exch-Base-Class              add: mayContain   msExchConfigurationXML

ms-Exch-Base-Class              add: mayContain   msExchMultiMailboxGUIDs

ms-Exch-Base-Class              add: mayContain   msExchMultiMailboxLocationsLink

ms-Exch-Coexistence-            add: mayContain   msExchCoexistenceOnPremisesSmartHost
Relationship

ms-Exch-Coexistence-            add: mayContain   msExchCoexistenceSecureMailCertificateThumbprint
Relationship

ms-Exch-Coexistence-            add: mayContain   msExchCoexistenceTransportServers
Relationship

ms-Exch-Configuration-Unit-     add: mayContain   msExchDirsyncStatus

<!-- p.382 -->

Class                          Change            Attribute/Class

Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchIsDirsyncStatusPending
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchDirSyncServiceInstance
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchOrganizationUpgradePolicyLink
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchManagementSiteLinkSL
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchOrganizationUpgradePolicyLinkSL
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantCompletionTargetVector
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantFlags
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantSafeLockdownSchedule
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantSourceForest
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantStartLockdown
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantStartRetired
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantStartSync
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantStatus
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantTargetForest
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchRelocateTenantTransitionCounter
Container

ms-Exch-Configuration-Unit-    add: mayContain   msExchSyncCookie
Container

ms-Exch-Control-Point-Config   add: mayContain   msExchRMSOnlineCertificationLocationUrl

<!-- p.383 -->

Class                            Change            Attribute/Class

ms-Exch-Control-Point-Config     add: mayContain   msExchRMSOnlineKeySharingLocationUrl

ms-Exch-Control-Point-Config     add: mayContain   msExchRMSOnlineLicensingLocationUrl

ms-Exch-Custom-Attributes        add: mayContain   msExchExtensionCustomAttribute1

ms-Exch-Custom-Attributes        add: mayContain   msExchExtensionCustomAttribute2

ms-Exch-Custom-Attributes        add: mayContain   msExchExtensionCustomAttribute3

ms-Exch-Custom-Attributes        add: mayContain   msExchExtensionCustomAttribute4

ms-Exch-Custom-Attributes        add: mayContain   msExchExtensionCustomAttribute5

ms-Exch-Domain-Content-Config    add: mayContain   msExchContentByteEncoderTypeFor7BitCharsets

ms-Exch-Domain-Content-Config    add: mayContain   msExchContentPreferredInternetCodePageForShiftJis

ms-Exch-Domain-Content-Config    add: mayContain   msExchContentRequiredCharSetCoverage

ms-Exch-Exchange-Server          add: mayContain   msExchWorkloadManagementPolicyLink

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringDeferAttempts

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringDeferWaitTime

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringFlags

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringPrimaryUpdatePath

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringSecondaryUpdatePath

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringUpdateFrequency

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringUpdateTimeout

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringScanTimeout

ms-Exch-Fed-OrgId                add: mayContain   msExchFedDelegationTrustSL

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamCountryBlockList
Config

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamLanguageBlockList
Config

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamNotifyOutboundRecipients
Config

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamDigestFrequency
Config

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamQuarantineRetention

<!-- p.384 -->

Class                       Change            Attribute/Class

Config

ms-Exch-MDB                 add: mayContain   msExchCalendarLoggingQuota

ms-Exch-MRS-Request         add: mayContain   msExchMailboxMoveSourceMDBLinkSL

ms-Exch-MRS-Request         add: mayContain   msExchMailboxMoveStorageMDBLinkSL

ms-Exch-MRS-Request         add: mayContain   msExchMailboxMoveTargetMDBLinkSL

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchMSOForwardSyncNonRecipientCookie
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchMSOForwardSyncRecipientCookie
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchMSOForwardSyncReplayList
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchAccountForestLink
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchActiveInstanceSleepInterval
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchPassiveInstanceSleepInterval
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchSyncDaemonMaxVersion
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchSyncDaemonMinVersion
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchSyncServiceInstanceNewTenantMaxVersion
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchSyncServiceInstanceNewTenantMinVersion
Instance

ms-Exch-Mail-Gateway        add: mayContain   msExchHomeMDBSL

ms-Exch-Mail-Gateway        add: mayContain   msExchHomeMTASL

ms-Exch-Mail-Storage        add: mayContain   msExchPreviousArchiveDatabase

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxExpiration

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxOwners

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxSharePointLinkedBy

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxSharePointUrl

<!-- p.385 -->

Class                            Change            Attribute/Class

ms-Exch-Mail-Storage             add: mayContain   msExchTeamMailboxShowInClientList

ms-Exch-Mail-Storage             add: mayContain   msExchCalendarLoggingQuota

ms-Exch-Mail-Storage             add: mayContain   msExchArchiveDatabaseLinkSL

ms-Exch-Mail-Storage             add: mayContain   msExchDisabledArchiveDatabaseLinkSL

ms-Exch-Mail-Storage             add: mayContain   msExchHomeMDBSL

ms-Exch-Mail-Storage             add: mayContain   msExchMailboxMoveTargetMDBLinkSL

ms-Exch-Mail-Storage             add: mayContain   msExchPreviousArchiveDatabaseSL

ms-Exch-Mail-Storage             add: mayContain   msExchPreviousHomeMDBSL

ms-Exch-Mail-Storage             add: mayContain   msExchMailboxContainerGuid

ms-Exch-Mail-Storage             add: mayContain   msExchUnifiedMailbox

ms-Exch-Mail-Storage             add: mayContain   msExchUserCulture

ms-Exch-Mailflow-Policy          add: mayContain   msExchImmutableId

ms-Exch-Malware-Filter-Config    add: mayContain   msExchMalwareFilterConfigExternalSenderAdminAddress

ms-Exch-Malware-Filter-Config    add: mayContain   msExchMalwareFilterConfigInternalSenderAdminAddress

ms-Exch-OAB                      add: mayContain   msExchOffLineABServerSL

ms-Exch-OAB                      add: mayContain   msExchOABGeneratingMailboxLink

ms-Exch-OWA-Mailbox-Policy       add: mayContain   msExchOWASetPhotoURL

ms-Exch-OWA-Virtual-Directory    add: mayContain   msExchOWASetPhotoURL

ms-Exch-Organization-Container   add: mayContain   msExchOrganizationFlags2

ms-Exch-Organization-Container   add: mayContain   msExchUMAvailableLanguages

ms-Exch-Organization-Container   add: mayContain   msExchWACDiscoveryEndpoint

ms-Exch-Organization-Container   add: mayContain   msExchAdfsAuthenticationRawConfiguration

ms-Exch-Organization-Container   add: mayContain   msExchServiceEndPointURL

ms-Exch-Private-MDB              add: mayContain   msExchMailboxDatabaseTransportFlags

ms-Exch-Public-Folder            add: mayContain   msExchPublicFolderEntryId

ms-Exch-Resource-Policy          add: mayContain   msExchCustomerExpectationCritical

ms-Exch-Resource-Policy          add: mayContain   msExchDiscretionaryCritical

<!-- p.386 -->

Class                             Change            Attribute/Class

ms-Exch-Resource-Policy           add: mayContain   msExchInternalMaintenanceCritical

ms-Exch-Resource-Policy           add: mayContain   msExchUrgentCritical

ms-Exch-Routing-Group-Connector   add: mayContain   msExchHomeMTASL

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigFlags
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigFromAddress
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigInternalBody
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigInternalSenderAdminAddress
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigInternalSubject
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilteringScanTimeout
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilteringUpdateFrequency
Protection-Config

ms-Exch-Site-Connector            add: mayContain   msExchHomeMTASL

ms-Exch-Smart-Links-Protection-   add: mayContain   msExchAddressRewriteExceptionList
Config

ms-Exch-Smart-Links-Protection-   add: mayContain   msExchSpamFlags
Config

ms-Exch-Tenant-Perimeter-         add: mayContain   msExchTransportResellerSettingsLinkSL
Settings

ms-Exch-Throttling-Policy         add: mayContain   msExchThrottlingPolicyFlags

ms-Exch-Throttling-Policy         add: mayContain   msExchAnonymousThrottlingPolicyStateEx

ms-Exch-Throttling-Policy         add: mayContain   msExchEASThrottlingPolicyStateEx

ms-Exch-Throttling-Policy         add: mayContain   msExchEWSThrottlingPolicyStateEx

ms-Exch-Throttling-Policy         add: mayContain   msExchGeneralThrottlingPolicyStateEx

ms-Exch-Throttling-Policy         add: mayContain   msExchIMAPThrottlingPolicyStateEx

ms-Exch-Throttling-Policy         add: mayContain   msExchOWAThrottlingPolicyStateEx

ms-Exch-Throttling-Policy         add: mayContain   msExchPOPThrottlingPolicyStateEx

<!-- p.387 -->

Class                            Change            Attribute/Class

ms-Exch-Throttling-Policy        add: mayContain   msExchPowershellThrottlingPolicyStateEx

ms-Exch-Throttling-Policy        add: mayContain   msExchRCAThrottlingPolicyStateEx

ms-Exch-Transport-Rule           add: mayContain   msExchTransportRuleImmutableId

ms-Exch-Transport-Rule           add: mayContain   msExchImmutableId

ms-Exch-Transport-Settings       add: mayContain   msExchTranspoPreviewaxRetriesForLocalSiteShadow

ms-Exch-Transport-Settings       add: mayContain   msExchTranspoPreviewaxRetriesForRemoteSiteShadow

ms-Exch-Transport-Settings       add: mayContain   msExchConfigurationXML

ms-Exch-Virtual-Directory        add: mayContain   msExchMRSProxyFlags

ms-Exch-Virtual-Directory        add: mayContain   msExchMRSProxyMaxConnections

Attributes added by Exchange SE RTM
    ms-DS-External-Directory-Object-Id

    ms-DS-GeoCoordinates-Altitude
    ms-DS-GeoCoordinates-Latitude

    ms-DS-GeoCoordinates-Longitude
    ms-Exch-Accepted-Domain-BL

    ms-Exch-Account-Forest-BL
    ms-Exch-Account-Forest-Link

    ms-Exch-ActiveSync-Device-AutoBlock-Duration

    ms-Exch-ActiveSync-Device-Autoblock-Threshold-Incidence-Duration
    ms-Exch-ActiveSync-Device-Autoblock-Threshold-Incidence-Limit

    ms-Exch-ActiveSync-Device-Autoblock-Threshold-Type
    ms-Exch-Adfs-Authentication-Raw-Configuration

    ms-Exch-Administrative-Unit-BL

    ms-Exch-Administrative-Unit-Link
    ms-Exch-Anonymous-Throttling-Policy-State-Ex

    ms-Exch-Archive-Database-Link-SL
    ms-Exch-Auth-Application-Identifier

    ms-Exch-Auth-App-Secret

    ms-Exch-Auth-Authorization-Url
    ms-Exch-Auth-Auth-Server-Type

    ms-Exch-Auth-Certificate-Data
    ms-Exch-Auth-Certificate-Thumbprint

    ms-Exch-Auth-Flags

<!-- p.388 -->

ms-Exch-Auth-Issuer-Name
ms-Exch-Auth-Issuing-Url

ms-Exch-Auth-Linked-Account
ms-Exch-Auth-Metadata-Url

ms-Exch-Auth-Policy-BL

ms-Exch-Auth-Policy-Link
ms-Exch-Auth-Realm

ms-Exch-Aux-Mailbox-Parent-Object-Id-BL
ms-Exch-Aux-Mailbox-Parent-Object-Id-Link

ms-Exch-Canary-Data-0

ms-Exch-Canary-Data-1
ms-Exch-Canary-Data-2

ms-Exch-Coexistence-Domains
ms-Exch-Content-Byte-Encoder-Type-For-7-Bit-Charsets

ms-Exch-Content-Preferred-Internet-Code-Page-For-Shift-Jis

ms-Exch-Content-Required-Char-Set-Coverage
ms-Exch-Correlation-Id

ms-Exch-Customer-Expectation-Critical
ms-Exch-Customer-Expectation-Overloaded

ms-Exch-Customer-Expectation-Underloaded

ms-Exch-Data-Encryption-Policy-BL
ms-Exch-Data-Encryption-Policy-Link

ms-Exch-Default-Public-Folder-Mailbox
ms-Exch-Device-Client-Type

ms-Exch-Dirsync-Authority-Metadata
ms-Exch-Dir-Sync-Service-Instance

ms-Exch-Dirsync-Status

ms-Exch-Dirsync-Status-Ack
ms-Exch-Disabled-Archive-Database-Link-SL

ms-Exch-Discretionary-Critical
ms-Exch-Discretionary-Overloaded

ms-Exch-Discretionary-Underloaded

ms-Exch-EAS-Throttling-Policy-State-Ex
ms-Exch-Edge-Sync-Config-Flags

ms-Exch-Encryption-Throttling-Policy-State-Ex
ms-Exch-EWS-Throttling-Policy-State-Ex

ms-Exch-Extension-Custom-Attribute-1

ms-Exch-Extension-Custom-Attribute-2
ms-Exch-Extension-Custom-Attribute-3

ms-Exch-Extension-Custom-Attribute-4

<!-- p.389 -->

ms-Exch-Extension-Custom-Attribute-5
ms-Exch-External-Directory-Object-Class

ms-Exch-Fed-Delegation-Trust-SL
ms-Exch-Forest-Mode-Flag

ms-Exch-General-Throttling-Policy-State-Ex

ms-Exch-Group-External-Member-Count
ms-Exch-Group-Member-Count

ms-Exch-Group-Security-Flags
ms-Exch-Home-MDB-SL

ms-Exch-Home-MTA-SL

ms-Exch-Hosted-Content-Filter-Config-Link
ms-Exch-Hygiene-Configuration-Link

ms-Exch-Hygiene-Configuration-Malware-BL
ms-Exch-Hygiene-Configuration-Spam-BL

ms-Exch-IMAP-Throttling-Policy-State-Ex

ms-Exch-Immutable-Sid
ms-Exch-Internal-Maintenance-Critical

ms-Exch-Internal-Maintenance-Overloaded
ms-Exch-Internal-Maintenance-Underloaded

ms-Exch-Is-Dirsync-Status-Pending,

ms-Exch-Localization-Flags
ms-Exch-Mailbox-Database-Transport-Flags

ms-Exch-Mailbox-Move-Source-Archive-MDB-Link-SL
ms-Exch-Mailbox-Move-Source-MDB-Link-SL

ms-Exch-Mailbox-Move-Storage-MDB-Link-SL
ms-Exch-Mailbox-Move-Target-Archive-MDB-Link-SL

ms-Exch-Mailbox-Move-Target-MDB-Link-SL

ms-Exch-Mailflow-Policy-Countries
ms-Exch-Mailflow-Policy-Keywords

ms-Exch-Mailflow-Policy-Publisher-Name
ms-Exch-Mailflow-Policy-Transport-Rules-Template-Xml

ms-Exch-Mailflow-Policy-Version

ms-Exch-Malware-Filter-Config-Alert-Text
ms-Exch-Malware-Filter-Config-External-Body

ms-Exch-Malware-Filter-Config-External-Sender-Admin-Address
ms-Exch-Malware-Filter-Config-External-Subject

ms-Exch-Malware-Filter-Config-Flags

ms-Exch-Malware-Filter-Config-From-Address
ms-Exch-Malware-Filter-Config-From-Name

ms-Exch-Malware-Filter-Config-Internal-Body

<!-- p.390 -->

ms-Exch-Malware-Filter-Config-Internal-Sender-Admin-Address
ms-Exch-Malware-Filter-Config-Internal-Subject

ms-Exch-Malware-Filter-Config-Link
ms-Exch-Malware-Filtering-Defer-Attempts

ms-Exch-Malware-Filtering-Defer-Wait-Time

ms-Exch-Malware-Filtering-Flags
ms-Exch-Malware-Filtering-Primary-Update-Path

ms-Exch-Malware-Filtering-Scan-Timeout
ms-Exch-Malware-Filtering-Secondary-Update-Path

ms-Exch-Malware-Filtering-Update-Frequency

ms-Exch-Malware-Filtering-Update-Timeout
ms-Exch-Management-Site-Link-SL

ms-Exch-MRS-Proxy-Flags
ms-Exch-MRS-Proxy-Max-Connections

ms-Exch-MSO-Forward-Sync-Divergence-Count

ms-Exch-MSO-Forward-Sync-Divergence-Related-Object-Link
ms-Exch-MSO-Forward-Sync-Divergence-Timestamp

ms-Exch-Multi-Mailbox-Databases-BL
ms-Exch-Multi-Mailbox-Databases-Link

ms-Exch-Multi-Mailbox-GUID

ms-Exch-Multi-Mailbox-Locations-BL
ms-Exch-Multi-Mailbox-Locations-Link

ms-Exch-OAB-Generating-Mailbox-BL
ms-Exch-OAB-Generating-Mailbox-Link

ms-Exch-Off-Line-AB-Server-SL
ms-Exch-Organization-Flags-2

ms-Exch-Organization-Upgrade-Policy-BL

ms-Exch-Organization-Upgrade-Policy-Date
ms-Exch-Organization-Upgrade-Policy-Enabled

ms-Exch-Organization-Upgrade-Policy-Link
ms-Exch-Organization-Upgrade-Policy-Link-SL

ms-Exch-Organization-Upgrade-Policy-MaxMailboxes

ms-Exch-Organization-Upgrade-Policy-Priority
ms-Exch-Organization-Upgrade-Policy-Source-Version

ms-Exch-Organization-Upgrade-Policy-Status
ms-Exch-Organization-Upgrade-Policy-Target-Version

ms-Exch-OWA-Set-Photo-URL

ms-Exch-OWA-Throttling-Policy-State-Ex
ms-Exch-POP-Throttling-Policy-State-Ex

ms-Exch-Powershell-Throttling-Policy-State-Ex

<!-- p.391 -->

ms-Exch-Previous-Archive-Database
ms-Exch-Previous-Archive-Database-SL

ms-Exch-Previous-Home-MDB-SL
ms-Exch-Public-Folder-EntryId

ms-Exch-Public-Folder-Mailbox

ms-Exch-Public-Folder-Smtp-Address
ms-Exch-RCA-Throttling-Policy-State-Ex

ms-Exch-Recipient-SoftDeleted-Status
ms-Exch-Relocate-Tenant-Completion-Target-Vector

ms-Exch-Relocate-Tenant-Flags

ms-Exch-Relocate-Tenant-Safe-Lockdown-Schedule
ms-Exch-Relocate-Tenant-Source-Forest

ms-Exch-Relocate-Tenant-Start-Lockdown
ms-Exch-Relocate-Tenant-Start-Retired

ms-Exch-Relocate-Tenant-Start-Sync

ms-Exch-Relocate-Tenant-Status
ms-Exch-Relocate-Tenant-Target-Forest

ms-Exch-Relocate-Tenant-Transition-Counter
ms-Exch-Resource-Type

ms-Exch-RMS-Computer-Accounts-Link-SL

ms-Exch-RMSOnline-Certification-Location-Url
ms-Exch-RMSOnline-Key-Sharing-Location-Url

ms-Exch-RMSOnline-Licensing-Location-Url
ms-Exch-RoleGroup-Type

ms-Exch-Service-End-Point-URL
ms-Exch-Shadow-When-Soft-Deleted-Time

ms-Exch-Spam-Add-Header

ms-Exch-Spam-Asf-Settings
ms-Exch-Spam-Asf-Test-Bcc-Address

ms-Exch-Spam-Country-Block-List
ms-Exch-Spam-Digest-Frequency

ms-Exch-Spam-False-Positive-Cc

ms-Exch-Spam-Flags
ms-Exch-Spam-Language-Block-List

ms-Exch-Spam-Modify-Subject
ms-Exch-Spam-Notify-Outbound-Recipients

ms-Exch-Spam-Outbound-Spam-Cc

ms-Exch-Spam-Quarantine-Retention
ms-Exch-Spam-Redirect-Address

ms-Exch-Sts-Refresh-Tokens-Valid-From

<!-- p.392 -->

   ms-Exch-Sync-Cookie
   ms-Exch-Sync-Service-Instance-New-Tenant-Max-Version

   ms-Exch-Sync-Service-Instance-New-Tenant-Min-Version
   ms-Exch-Team-Mailbox-Expiration

   ms-Exch-Team-Mailbox-Expiry-Days

   ms-Exch-Team-Mailbox-Owners
   ms-Exch-Team-Mailbox-SharePoint-Linked-By

   ms-Exch-Team-Mailbox-SharePoint-Url
   ms-Exch-Team-Mailbox-Show-In-Client-List

   ms-Exch-Tenant-Country

   ms-Exch-Throttling-Policy-Flags
   ms-Exch-Transport-MaxRetriesForLocalSiteShadow

   ms-Exch-Transport-MaxRetriesForRemoteSiteShadow
   ms-Exch-Transport-Reseller-Settings-Link-SL

   ms-Exch-Transport-Rule-Immutable-Id

   ms-Exch-Trusted-Domain-BL
   ms-Exch-Trusted-Domain-Link

   ms-Exch-UG-Event-Subscription-BL
   ms-Exch-UG-Event-Subscription-Link

   ms-Exch-UG-Member-BL

   ms-Exch-UG-Member-Link
   ms-Exch-Urgent-Critical

   ms-Exch-Urgent-Overloaded
   ms-Exch-Urgent-Underloaded

   ms-Exch-WAC-Discovery-Endpoint
   ms-Exch-When-Soft-Deleted-Time

   ms-Exch-Workload-Classification

   ms-Exch-Workload-Management-Is-Enabled
   ms-Exch-Workload-Management-Policy

   ms-Exch-Workload-Management-Policy-BL
   ms-Exch-Workload-Management-Policy-Link

Global catalog attributes added by Exchange SE RTM
   ms-Exch-Administrative-Unit-BL
   ms-Exch-Administrative-Unit-Link

   ms-Exch-Archive-Database-Link-SL
   ms-Exch-Auth-Policy-Link

   ms-Exch-Correlation-Id

   ms-Exch-Data-Encryption-Policy-BL

<!-- p.393 -->

ms-Exch-Data-Encryption-Policy-Link
ms-Exch-Default-Public-Folder-Mailbox

ms-Exch-Device-Client-Type
ms-Exch-Dirsync-Authority-Metadata

ms-Exch-Dirsync-Status

ms-Exch-Dirsync-Status-Ack
ms-Exch-Disabled-Archive-Database-Link-SL

ms-Exch-Edge-Sync-Config-Flags
ms-Exch-EvictedMembers-Link

ms-Exch-EvictedMembers-BL

ms-Exch-Extension-Custom-Attribute-1
ms-Exch-Extension-Custom-Attribute-2

ms-Exch-Extension-Custom-Attribute-3
ms-Exch-Extension-Custom-Attribute-4

ms-Exch-Extension-Custom-Attribute-5

ms-Exch-Group-External-Member-Count
ms-Exch-Group-Member-Count

ms-Exch-HAB-Root-DepaPreviewent-Link
ms-Exch-Home-MDB-SL

ms-Exch-Home-MTA-SL

ms-Exch-Is-Dirsync-Status-Pending
ms-Exch-Localization-Flags

ms-Exch-Mailbox-Container-Guid
ms-Exch-Mailbox-Move-Source-Archive-MDB-Link-SL

ms-Exch-Mailbox-Move-Source-MDB-Link-SL
ms-Exch-Mailbox-Move-Storage-MDB-Link-SL

ms-Exch-Mailbox-Move-Target-Archive-MDB-Link-SL

ms-Exch-Mailbox-Move-Target-MDB-Link-SL
ms-Exch-Offline-OrgId-Home-Realm-Record

ms-Exch-Previous-Archive-Database
ms-Exch-Previous-Archive-Database-SL

ms-Exch-Previous-Home-MDB-SL

ms-Exch-Recipient-SoftDeleted-Status
ms-Exch-Relocate-Tenant-Completion-Target-Vector,

ms-Exch-Relocate-Tenant-Flags
ms-Exch-Relocate-Tenant-Safe-Lockdown-Schedule

ms-Exch-Relocate-Tenant-Source-Forest

ms-Exch-Relocate-Tenant-Start-Lockdown
ms-Exch-Relocate-Tenant-Start-Retired

ms-Exch-Relocate-Tenant-Start-Sync

<!-- p.394 -->

      ms-Exch-Relocate-Tenant-Status
      ms-Exch-Relocate-Tenant-Target-Forest

      ms-Exch-Relocate-Tenant-Transition-Counter
      ms-Exch-RMS-Computer-Accounts-Link-SL

      ms-Exch-RoleGroup-Type

      ms-Exch-Sync-Cookie
      ms-Exch-Team-Mailbox-Expiration

      ms-Exch-Team-Mailbox-Expiry-Days
      ms-Exch-Team-Mailbox-Owners

      ms-Exch-Team-Mailbox-SharePoint-Linked-By

      ms-Exch-Team-Mailbox-SharePoint-Url
      ms-Exch-Team-Mailbox-Show-In-Client-List

      ms-Exch-UG-Event-Subscription-BL
      ms-Exch-UG-Event-Subscription-Link

      ms-Exch-Unified-Mailbox

      `ms-Exch-When-Soft-Deleted-Time

Attributes modified by Exchange SE RTM

                                                                                         ﾉ   Expand table

Class             Change                         Attribute/Class

Exch-             rangeUpper                     15254
Configuration-
Unit-Container

Exch-Mailflow-    rangeUpper                     256000
Policy-
Transport-
Rules-Template-
Xml

Mail-Recipient    replace: mayContain            msExchUGMemberLink

ms-Exch-          replace: searchFlags           9
Accepted-
Domain-Name

ms-Exch-          replace: searchFlags           9
Archive-GUID

ms-Exch-Bypass-   replace: searchFlags           19
Audit

ms-Exch-          ntdsSchemaAdd                  attributeID: 1.2.840.113556.1.4.7000.102.51992
Coexistence-On-                                  isMemberOfPartialAttributeSet: FALSE (not in global catalog)

<!-- p.395 -->

Class             Change                           Attribute/Class

Premises-Smart-                                    searchFlags: 0 (no index)
Host

ms-Exch-          ntdsSchemaAdd                    attributeID: 1.2.840.113556.1.4.7000.102.51991
Coexistence-                                       isMemberOfPartialAttributeSet: FALSE (not in global catalog)
Secure-Mail-                                       searchFlags: 0 (no index)
Certificate-
Thumbprint

ms-Exch-          rangeUpper                       1024
Coexistence-
Secure-Mail-
Certificate-
Thumbprintms-
Exch-Sync-
Cookie

ms-Exch-          ntdsSchemaAdd                    attributeID: 1.2.840.113556.1.4.7000.102.51990
Coexistence-                                       isMemberOfPartialAttributeSet: FALSE (not in global catalog)
Transport-                                         searchFlags: 0 (no index)
Servers

ms-Exch-ELC-      replace: attributeSecurityGuid   F6SzsVXskUGzJ7cuM+OK8g==
Mailbox-Flags

ms-Exch-          isMemberOfPartialAttributeSet:   TRUE
Extension-
Custom-
Attribute-1

ms-Exch-          isMemberOfPartialAttributeSet:   TRUE
Extension-
Custom-
Attribute-2

ms-Exch-          isMemberOfPartialAttributeSet:   TRUE
Extension-
Custom-
Attribute-3

ms-Exch-          isMemberOfPartialAttributeSet:   TRUE
Extension-
Custom-
Attribute-4

ms-Exch-          isMemberOfPartialAttributeSet    TRUE
Extension-
Custom-
Attribute-5

<!-- p.396 -->

Class             Change                          Attribute/Class

ms-Exch-Group-    ntdsSchemaModify                isMemberOfPartialAttributeSet: TRUE MAPIID:36066
External-
Member-Count

ms-Exch-Group-    ntdsSchemaModify                replace:
Member-Count                                      isMemberOfPartialAttributeSetisMemberOfPartialAttributeSet:
                                                  TRUE MAPIID: 36067

ms-Exch-Group-    ntdsSchemaModify                replace: mapiId: 36111
Security-Flags

ms-Exch-HAB-      replace:                        TRUE
Root-             isMemberOfPartialAttributeSet
DepaPreviewent-
Link

ms-Exch-          replace: searchFlags            19
Mailbox-Audit-
Enable

ms-Exch-          rangeUpper                      38880
Malware-
Filtering-
Update-
Frequency

ms-Exch-MSO-      rangeUpper                      20480
Forward-Sync-
Non-Recipient-
Cookie

ms-Exch-MSO-      rangeUpper                      20480
Forward-Sync-
Recipient-
Cookie

ms-Exch-Role-     rangeUpper                      8192
Entries

ms-Exch-Schema-   rangeUpper                      15137
Version-Pt

ms-Exch-Schema-   rangeUpper                      15281
Version-Pt

Ms-exch-schema-   rangeUpper                      15292
version-pt

ms-Exch-Smtp-     replace: rangeUpper             1024
Receive-Tls-

<!-- p.397 -->

 Class             Change                      Attribute/Class

 Certificate-
 Name

 ms-Exch-Smtp-     replace: rangeUpper         1024
 TLS-Certificate

 ms-Exch-Sync-      rangeUpper                 262144
 Cookie

 Top               replace: mayContain         msExchUGMemberBL

Object IDs added by Exchange SE RTM
The following class object IDs are added when you install Exchange SE RTM:

        1.2.840.113556.1.5.7000.62.50161
        1.2.840.113556.1.5.7000.62.50162
        1.2.840.113556.1.5.7000.62.50163
        1.2.840.113556.1.5.7000.62.50164
        1.2.840.113556.1.5.7000.62.50165
        1.2.840.113556.1.5.7000.62.50166
        1.2.840.113556.1.5.7000.62.50167
        1.2.840.113556.1.5.7000.62.50170
        1.2.840.113556.1.5.7000.62.50171
        1.2.840.113556.1.5.7000.62.50172
        1.2.840.113556.1.5.7000.62.50173
        1.2.840.113556.1.5.7000.62.50174
        1.2.840.113556.1.5.7000.62.50176
        1.2.840.113556.1.5.7000.62.50177
        1.2.840.113556.1.5.7000.62.50178
        1.2.840.113556.1.5.7000.62.50187
        1.2.840.113556.1.5.7000.62.50188
        1.2.840.113556.1.5.7000.62.50189
        1.2.840.113556.1.5.7000.62.50190
        1.2.840.113556.1.5.7000.62.50191
        1.2.840.113556.1.5.7000.62.50192
        1.2.840.113556.1.5.7000.62.50202
        1.2.840.113556.1.5.7000.62.50203
        1.2.840.113556.1.5.7000.62.50204
        1.2.840.113556.1.5.7000.62.50205
        1.2.840.113556.1.5.7000.62.50212
        1.2.840.113556.1.5.7000.62.50213
        1.2.840.113556.1.5.7000.62.50214

<!-- p.398 -->

The following attribute object IDs are added when you install Exchange SE RTM:

     1.2.840.113556.1.4.2183
     1.2.840.113556.1.4.2184
     1.2.840.113556.1.4.2185
     1.2.840.113556.1.4.7000.102.51773
     1.2.840.113556.1.4.7000.102.51774
     1.2.840.113556.1.4.7000.102.51775
     1.2.840.113556.1.4.7000.102.51786
     1.2.840.113556.1.4.7000.102.51787
     1.2.840.113556.1.4.7000.102.51788
     1.2.840.113556.1.4.7000.102.51789
     1.2.840.113556.1.4.7000.102.51790
     1.2.840.113556.1.4.7000.102.51791
     1.2.840.113556.1.4.7000.102.51792
     1.2.840.113556.1.4.7000.102.51794
     1.2.840.113556.1.4.7000.102.51795
     1.2.840.113556.1.4.7000.102.51796
     1.2.840.113556.1.4.7000.102.51797
     1.2.840.113556.1.4.7000.102.51798
     1.2.840.113556.1.4.7000.102.51799
     1.2.840.113556.1.4.7000.102.51800
     1.2.840.113556.1.4.7000.102.51801
     1.2.840.113556.1.4.7000.102.51805
     1.2.840.113556.1.4.7000.102.51806
     1.2.840.113556.1.4.7000.102.51807
     1.2.840.113556.1.4.7000.102.51808
     1.2.840.113556.1.4.7000.102.51809
     1.2.840.113556.1.4.7000.102.51810
     1.2.840.113556.1.4.7000.102.51811
     1.2.840.113556.1.4.7000.102.51812
     1.2.840.113556.1.4.7000.102.51813
     1.2.840.113556.1.4.7000.102.51814
     1.2.840.113556.1.4.7000.102.51815
     1.2.840.113556.1.4.7000.102.51816
     1.2.840.113556.1.4.7000.102.51818
     1.2.840.113556.1.4.7000.102.51819
     1.2.840.113556.1.4.7000.102.51820
     1.2.840.113556.1.4.7000.102.51821
     1.2.840.113556.1.4.7000.102.51822
     1.2.840.113556.1.4.7000.102.51823
     1.2.840.113556.1.4.7000.102.51824
     1.2.840.113556.1.4.7000.102.51826

<!-- p.399 -->

1.2.840.113556.1.4.7000.102.51827
1.2.840.113556.1.4.7000.102.51829
1.2.840.113556.1.4.7000.102.51830
1.2.840.113556.1.4.7000.102.51832
1.2.840.113556.1.4.7000.102.51833
1.2.840.113556.1.4.7000.102.51836
1.2.840.113556.1.4.7000.102.51837
1.2.840.113556.1.4.7000.102.51838
1.2.840.113556.1.4.7000.102.51839
1.2.840.113556.1.4.7000.102.51840
1.2.840.113556.1.4.7000.102.51851
1.2.840.113556.1.4.7000.102.51852
1.2.840.113556.1.4.7000.102.51859
1.2.840.113556.1.4.7000.102.51860
1.2.840.113556.1.4.7000.102.51861
1.2.840.113556.1.4.7000.102.51862
1.2.840.113556.1.4.7000.102.51863
1.2.840.113556.1.4.7000.102.51864
1.2.840.113556.1.4.7000.102.51865
1.2.840.113556.1.4.7000.102.51866
1.2.840.113556.1.4.7000.102.51867
1.2.840.113556.1.4.7000.102.51868
1.2.840.113556.1.4.7000.102.51869
1.2.840.113556.1.4.7000.102.51870
1.2.840.113556.1.4.7000.102.51871
1.2.840.113556.1.4.7000.102.51872
1.2.840.113556.1.4.7000.102.51873
1.2.840.113556.1.4.7000.102.51874
1.2.840.113556.1.4.7000.102.51875
1.2.840.113556.1.4.7000.102.51876
1.2.840.113556.1.4.7000.102.51877
1.2.840.113556.1.4.7000.102.51878
1.2.840.113556.1.4.7000.102.51879
1.2.840.113556.1.4.7000.102.51880
1.2.840.113556.1.4.7000.102.51881
1.2.840.113556.1.4.7000.102.51882
1.2.840.113556.1.4.7000.102.51883
1.2.840.113556.1.4.7000.102.51914
1.2.840.113556.1.4.7000.102.51915
1.2.840.113556.1.4.7000.102.51916
1.2.840.113556.1.4.7000.102.51917
1.2.840.113556.1.4.7000.102.51918
1.2.840.113556.1.4.7000.102.51919

<!-- p.400 -->

1.2.840.113556.1.4.7000.102.51920
1.2.840.113556.1.4.7000.102.51921
1.2.840.113556.1.4.7000.102.51922
1.2.840.113556.1.4.7000.102.51923
1.2.840.113556.1.4.7000.102.51924
1.2.840.113556.1.4.7000.102.51925
1.2.840.113556.1.4.7000.102.51926
1.2.840.113556.1.4.7000.102.51927
1.2.840.113556.1.4.7000.102.51928
1.2.840.113556.1.4.7000.102.51929
1.2.840.113556.1.4.7000.102.51930
1.2.840.113556.1.4.7000.102.51931
1.2.840.113556.1.4.7000.102.51932
1.2.840.113556.1.4.7000.102.51933
1.2.840.113556.1.4.7000.102.51934
1.2.840.113556.1.4.7000.102.51935
1.2.840.113556.1.4.7000.102.51936
1.2.840.113556.1.4.7000.102.51937
1.2.840.113556.1.4.7000.102.51938
1.2.840.113556.1.4.7000.102.51939
1.2.840.113556.1.4.7000.102.51940
1.2.840.113556.1.4.7000.102.51941
1.2.840.113556.1.4.7000.102.51942
1.2.840.113556.1.4.7000.102.51943
1.2.840.113556.1.4.7000.102.51944
1.2.840.113556.1.4.7000.102.51945
1.2.840.113556.1.4.7000.102.51946
1.2.840.113556.1.4.7000.102.51947
1.2.840.113556.1.4.7000.102.51948
1.2.840.113556.1.4.7000.102.51949
1.2.840.113556.1.4.7000.102.51950
1.2.840.113556.1.4.7000.102.51951
1.2.840.113556.1.4.7000.102.51952
1.2.840.113556.1.4.7000.102.51953
1.2.840.113556.1.4.7000.102.51954
1.2.840.113556.1.4.7000.102.51955
1.2.840.113556.1.4.7000.102.51993
1.2.840.113556.1.4.7000.102.51994
1.2.840.113556.1.4.7000.102.51995
1.2.840.113556.1.4.7000.102.51996
1.2.840.113556.1.4.7000.102.51997
1.2.840.113556.1.4.7000.102.51998
1.2.840.113556.1.4.7000.102.52001
