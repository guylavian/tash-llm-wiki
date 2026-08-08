---
title: "Exchange Server — pages 2881-2920"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2881-2920
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2881-2920
family: exchange
documentKind: "doc"
abstract: "Configure managed availability overrides in Exchange Server 07/23/2025 APPLIES TO: 2016 2019 Subscription Edition Managed availability performs continuous probing to detect possible problems with Exchange components or their dependencies. It also does recovery actions to make su"
---

# Exchange Server — pages 2881-2920

<!-- p.2881 -->

Configure managed availability overrides in
Exchange Server
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

Managed availability performs continuous probing to detect possible problems with Exchange
components or their dependencies. It also does recovery actions to make sure the user
experience isn't affected due to a problem with any of these components. However, there
might be scenarios where the out-of-box settings might not be suitable for your environment.
Managed availability probes, monitors, and responders can be customized by creating an
override.

There are two types of overrides: local and global. As their names imply, a local override is
available only on the server where the override was created, and a global override is used to
apply an override to multiple servers. Both types of override can be created for a specific
duration or for a specific version of Exchange, but not both at the same time.

  ７ Note

  When you create an override, it doesn't take effect immediately. The Microsoft Exchange
  Health Management service checks for configuration changes every 10 minutes and loads
  any detected configuration changes. If you don't want to wait, you can restart the service.

To learn more about managed availability, see Managed availability. For other management
tasks related to managed availability, see Manage health sets and server health.

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes

     The procedures in this article require the Exchange Management Shell. To open the
     Exchange Management Shell, see Open the Exchange Management Shell.

     You can only use PowerShell to perform this procedure. To learn how to open the
     Exchange Management Shell in your on-premises Exchange organization, see Open the
     Exchange Management Shell.

     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

<!-- p.2882 -->

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to create
local overrides
To create a local override for a specific duration, use the following syntax:

  PowerShell

  Add-ServerMonitoringOverride -Server <ServerName> -Identity <HealthSetName>\
  <MonitoringItemName>[\<TargetResource>] -ItemType <Probe | Monitor | Responder |
  Maintenance> -PropertyName <PropertyName> -PropertyValue <Value> -Duration
  <dd.hh:mm:ss>

To create a local override for a specific version of Exchange, use the following syntax.

  PowerShell

  Add-ServerMonitoringOverride -Server <ServerName> -Identity <HealthSetName>\
  <MonitoringItemName>[\<TargetResource>] -ItemType <Probe | Monitor | Responder |
  Maintenance> -PropertyName <PropertyName> -PropertyValue <Value> -Version
  <15.01.xxxx.xxx>

  ７ Note

  When you create the override, the values used in the Identity parameter are case-sensitive.

This example adds a local override that disables the responder
ActiveDirectoryConnectivityConfigDCServerReboot on the server named EXCH03 for 20 days.

  PowerShell

  Add-ServerMonitoringOverride -Server EXCH03 -Identity
  "AD\ActiveDirectoryConnectivityConfigDCServerReboot" -ItemType Responder -
  PropertyName Enabled -PropertyValue 0 -Duration 20.00:00:00

How do you know you successfully created a local override?

<!-- p.2883 -->

To verify you successfully created a local override, use the Get-ServerMonitoringOverride
cmdlet to view the list of local overrides:

  PowerShell

  Get-ServerMonitoringOverride       -Server <ServerIdentity> | Format-List

The override should appear in the list.

Use the Exchange Management Shell to remove
local overrides
To remove a local override, use the following syntax.

  PowerShell

  Remove-ServerMonitoringOverride -Server <ServerName> -Identity <HealthSetName>\
  <MonitoringItemName>[\<TargetResource>] -ItemType <ExistingItemTypeValue> -
  PropertyName <PropertytoRemove>

This example removes the existing local override of the
ActiveDirectoryConnectivityConfigDCServerReboot responder in the Exchange health set from

server EXCH01.

  PowerShell

  Remove-ServerMonitoringOverride -Server EXCH01 -Identity
  Exchange\ActiveDirectoryConnectivityConfigDCServerReboot -ItemType Responder -
  PropertyName Enabled

How do you know you successfully removed a local override?
To verify you successfully removed a local override, use the Get-ServerMonitoringOverride
cmdlet to view the list of local overrides:

  PowerShell

  Get-ServerMonitoringOverride       -Server <ServerIdentity> | Format-List

The removed override shouldn't appear in the list.

<!-- p.2884 -->

Use the Exchange Management Shell to create
global overrides
To create a global override for a specific duration, use the following syntax.

  PowerShell

  Add-GlobalMonitoringOverride -Identity <HealthSetName>\<MonitoringItemName>[\
  <TargetResource>] -ItemType <Probe | Monitor | Responder | Maintenance> -
  PropertyName <PropertytoOverride> -PropertyValue <NewPropertyValue> -Duration
  <dd.hh:mm:ss>

To create a global override for a specific version of Exchange, use the following syntax.

  PowerShell

  Add-GlobalMonitoringOverride -Identity <HealthSetName>\<MonitoringItemName>[\
  <TargetResource>] -ItemType <Probe | Monitor | Responder | Maintenance> -
  PropertyName <PropertytoOverride> -PropertyValue <NewPropertyValue> -ApplyVersion
  <15.01.xxxx.xxx>

  ７ Note

  When you create the override, the values used in the Identity parameter are case-sensitive.

This example adds a global override that disables the OnPremisesInboundProxy probe for 30
days.

  PowerShell

  Add-GlobalMonitoringOverride -Identity "FrontendTransport\OnPremisesInboundProxy"
  -ItemType Probe -PropertyName Enabled -PropertyValue 0 -Duration 30.00:00:00

This example adds a global override that disables the StorageLogicalDriveSpaceEscalate
responder for all servers running Exchange version 15.01.0225.042.

  PowerShell

  Add-GlobalMonitoringOverride -Identity
  "MailboxSpace\StorageLogicalDriveSpaceEscalate" -PropertyName Enabled -
  PropertyValue 0 -ItemType Responder -ApplyVersion "15.01.0225.042"

<!-- p.2885 -->

How do you know you successfully created a global override?
To verify you successfully created a global override, use the Get-GlobalMonitoringOverride
cmdlet to view the list of global overrides:

  PowerShell

  Get-GlobalMonitoringOverride

The override should appear in the list.

Use the Exchange Management Shell to remove
global overrides
To remove a global override, use the following syntax.

  PowerShell

  Remove-GlobalMonitoringOverride -Identity <HealthSetName>\<MonitoringItemName>[\
  <TargetResource>] -ItemType <ExistingItemTypeValue> -PropertyName
  <OverriddenProperty>

This example removes the existing global override of the ExtensionAttributes property of the
OnPremisesInboundProxy probe in the FrontEndTransport health set.

  PowerShell

  Remove-GlobalMonitoringOverride -Identity FrontEndTransport\OnPremisesInboundProxy
  -ItemType Probe -PropertyName ExtensionAttributes

How do you know you successfully removed a global
override?
To verify you successfully removed a global override, use the Get-GlobalMonitoringOverride
cmdlet to view the list of global overrides:

  PowerShell

  Get-GlobalMonitoringOverride

The removed override shouldn't appear in the list.

<!-- p.2886 -->

Server health and performance in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016       2019       Subscription Edition

Understanding server health and performance is critical to designing and maintaining a high-
performance messaging infrastructure. Exchange 2016 and Exchange 2019 continue the
features that were introduced in Exchange 2013 to help you manage server health and
performance.

Managed availability
Managed availability provides built-in monitoring and recovery actions that preserve the end-
user experience. Managed availability is made of two processes: the Exchange Health Manager
Service (MSExchangeHMHost.exe) and the Exchange Health Manager Worker process
(MSExchangeHMWorker.exe), and the following components:

      Probe engine: The probe engine takes measurements on the server.

      Monitoring probe engine: The monitoring probe engine stores the business logic about
      what constitutes a healthy state. Like a pattern recognition engine, the monitoring probe
      engine looks for patterns and measurements that differ from a healthy state, and then
      evaluates whether a component or feature is unhealthy.

      Responder engine: When the responder engine is alerted about an unhealthy component,
      it first tries to recover that component. Managed availability enables multi-stage recovery
      actions. The first attempt may be to restart the application pool, the second attempt may
      be to restart the corresponding service, and the third attempt may be to restart the
      server. And, the final attempt may be to put the server offline, so that it no longer accepts
      traffic. If all of these actions fail, an alert is sent to the help desk.

For more information about managed availability, see Managed availability.

Workload management
Workload management is made of these components:

      User workload management is the new name for the user throttling features that were
      introduced in Exchange 2010. You can customize these setting based on the needs of
      your environment.

<!-- p.2887 -->

     System workload management automatically throttles specific Exchange workloads by
     monitoring the health of key server resources. These settings should be customized only
     under the direction of Microsoft Customer Service and Support.

For more information about user workload management, see User workload management in
Exchange Server.

<!-- p.2888 -->

User workload management in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

User workload management allows you to control how Exchange system resources are
consumed by users. This feature was available in Exchange 2010 (known as user throttling), and
was expanded to its current level in Exchange 2013.

A workload is a feature, protocol, or service that's been explicitly defined to manage system
resources on Exchange servers. Each workload consumes system resources on the Exchange
server (for example CPU, memory, network, and disk bandwidth). Examples of workloads
include Outlook on the web (formerly known as Outlook Web App), Exchange ActiveSync,
mailbox migration, and mailbox assistants.

Control the user consumption of Exchange system
resources
By default, the user workload settings allow users to increase their resource consumption for
brief periods without experiencing a reduction in bandwidth. Because you can limit user access
to resources, there are fewer instances of large resource consumers being locked out. You can
further budget user resource consumption by setting a recharge rate for users. The important
concepts for user workload management are describe in this list:

      Burst allowances: Allows users perform short periods of increased resource consumption
      without experiencing any throttling.

      Recharge rate: Uses a budget system to manage user resource consumption, and
      specifies the rate at which the user's budget is charged (how much the budget grows by)
      during the budget time. For example, if the budget time is one hour, a recharge rate value
      of 600,000 milliseconds indicates that resource budgets for users are recharged at the
      rate of ten minutes of usage per hour.

      Traffic shaping (microdelays): Works by delaying the user for short periods of time when
      their resource usage reaches the configured limit over a specific time interval. This delay
      occurs for very short periods of time (users generally don't notice the delay), and well
      before the resource consumption causes a significant impact the Exchange server's
      performance. Traffic shaping preserves the availability of the Exchange server without
      blocking user productivity, has less user impact than a user lockout, and significantly
      reduces the chance of a user lockout.

<!-- p.2889 -->

     Maximum usage: Temporarily blocks a user who reaches a maximum user resource
     threshold (the user consumes an unusually high amount of resources over a short time
     interval). Users who are temporarily blocked from resource usage are unblocked as soon
     as their resource usage budget allows it (as their budgets are recharged).

You manage user workload settings with these cmdlets in the Exchange Management Shell:

     View, create, remove, and modify user workload settings: Get-ThrottlingPolicy, New-
     ThrottlingPolicy, Remove-ThrottlingPolicy and Set-ThrottlingPolicy.

     Assign user workload settings to users or computers: Get-ThrottlingPolicyAssociation
     and Set-ThrottlingPolicyAssociation

Scopes in user workload settings
By default, there's one throttling policy named GlobalThrottlingPolicy . This policy has the
scope value Global, which means it applies to all users in the organization. Typically, the
settings in the default throttling policy are adequate for users in most Exchange organizations.
Instead of customizing the default throttling policy, you can create custom throttling policies
that have different settings that the default policy. The scopes that are available in custom
throttling policies are:

     Organization: The throttling settings apply to all users in the organization.

     Regular: The throttling settings that apply only to specific users in the organization.

The order of precedence for throttling polices are:

   1. Throttling policies with the scope value Regular are applied to users before Organization
     policies and the default throttling policy.

   2. Throttling policies with the scope value Organization are applied to users before the
     default throttling policy.

   3. The default throttling policy is applied last, or exclusively to users who don't have Regular
     or Organization policies assigned to them.

If you create custom throttling policies, the settings should be different than the default
throttling policy, and you should plan for the difference in settings from Regular policies to
Organization policies to the default policy (for example, least restrictive to most restrictive, or
vice-versa).

  ７ Note

<!-- p.2890 -->

  We strongly recommend that you don't modify the default throttling policy, because
  changes to the default policy could be overwritten by future Exchange updates. Instead,
  you should create custom throttling policies that contain customized settings.

User throttling in Exchange 2010 coexistence
environments
Users with mailboxes on Exchange 2016 servers are throttled using Exchange 2016 throttling
features, even if you install Exchange 2016 in an Exchange 2010 organization. This list describes
the important considerations for throttling in coexistence environments:

     Exchange 2010 mailboxes remain throttled by Exchange 2010 throttling features when
     users access their mailboxes through Exchange 2010 Client Access servers.

     When you install Exchange 2016 in an Exchange 2010 organization, Exchange 2016 setup
     might try to carry some of the Exchange 2010 throttling settings forward. However, the
     throttling functionality is so different that the effects of any legacy throttling settings will
     generally not alter how throttling works in Exchange 2016.

<!-- p.2891 -->

Diagnostic Data collected for Exchange
Server
APPLIES TO:      2016     2019      Subscription Edition

Microsoft collects diagnostic data to keep Exchange Server secure and up to date, find and fix
problems, and identify and mitigate threats. When the September 2021 (or later) Cumulative
Update (CU) is installed on a Mailbox server, Exchange Server 2016 or Exchange Server 2019
has the ability to send diagnostic data from each Exchange server to the Office Config Service
(OCS) in the Microsoft cloud. There's a change to the License Agreement acceptance process to
allow you to choose whether to share diagnostic data with Microsoft.

Change in License Term acceptance process
When using the graphical user interface (GUI) version of Exchange Setup, a new License
Agreement screen will appear, as shown below.

Instead of two options, there are now three options.

<!-- p.2892 -->

Choose one of the following options:

                                                                                      ﾉ   Expand table

 Selection                                       Description

 I accept the license agreement and will share   This is the default option that accepts the license
 diagnostic data with Microsoft                  agreement and enables sending data to Microsoft.

 I accept the license agreement, but I'm not     This option accepts the license agreement but
 ready to share diagnostic data with Microsoft   disables sending data to Microsoft.

 I do not accept the license agreement           If you don't accept the EULA, you can't install the CU.

Unattended Setup of Exchange Server
The acceptance options are also available via an unattended command-line setup using the
new Setup switches:

<!-- p.2893 -->

                                                                                         ﾉ    Expand table

 Selection                                                     Description

 /IAcceptExchangeServerLicenseTerms_DiagnosticDataON           Use this switch to accept the license terms
                                                               and send optional data to Microsoft when
                                                               the EM service requests mitigations.

 /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF          Use this new setup switch to accept the
                                                               license terms and disable sending optional
                                                               data to Microsoft.

  ） Important

  /IAcceptExchangeServerLicenseTerms has been removed from Exchange server
  command-line Setup and replaced with the two new Setup switches shown above.

Diagnostic Data collected
When diagnostic data collection is enabled, your Exchange server sends the following
information hourly to the Office Config Service:

                                                                                         ﾉ    Expand table

 Data                    Description

 ExchangeVersion         The server version (CU and SU build information)

 ServiceState            Information about the Emergency Mitigation Service state ( enabled or disabled )

 ImmutableDeviceId       Unique identifier for the server

 ImmutableOrgId          Unique identifier for the Exchange organization

 ConfigurationsApplied   A list of all mitigations that were applied

 ConfigurationsBlocked   A list of all mitigations that were blocked

 MiscConfigurations      Information about the following Exchange Server component state:
                               SerializationSigningEnabled
                               MSIPCEnabled
                               EncryptionAlgorithmCBCEnabled

Starting with the Exchange Server 2019 CU15 (2025H1), Exchange Server collects the following
additional telemetry data:

<!-- p.2894 -->

                                                                             ﾉ   Expand table

Data                  Description

PrimaryKey            A unique identifier for the server that acts as primary key:
                      {OrganizationId}.{DeviceId}

OrganizationId        Unique identifier for the Exchange organization

Oauth2ClientProfile   Indicates whether modern authentication is enabled or disabled for
                      the Exchange organization, controlled by OAuth2ClientProfileEnabled
                      setting

DeviceId              Unique MachineId identifier for the server

RemoteMailboxCount    Total count of mailboxes where RecipientTypeDetails is
                      RemoteUserMailbox

ServerVersion         The build number of the Exchange Server build running on the server

ServerRole            The Exchange Server role running on the server

IsPPE                 Indicates whether this is a preproduction Exchange Server installation
                      (default is false )

MailBoxDataValue      Total count of mailboxes within the organization and on a per
                      Exchange server base

AuthServerDataList    Information about the Auth Server configured in the organization:

                             Name
                             AuthMetaDataURL
                             IsDefaultAuthorizationEndpoint
                             TokenIssuingEndpoint
                             ApplicationIdentifier
                             Enabled
                             Type

AcceptedDomainsList   Information about the Accepted Domains configured in the
                      organization:

                             DomainName
                             IsTenantDomain
                             IsDefault

<!-- p.2895 -->

Data                               Description

FederationTrustDataList            Information about the Federation Trusts configured in the
                                   organization:

                                         Name
                                         IsValid

OrganizationRelationshipDataList   Information about the Organization Relationships configured in the
                                   organization:

                                         Name
                                         DomainNames
                                         Enabled
                                         FreeBusyAccessEnabled
                                         FreeBusyAccessLevel
                                         MailTipsAccessEnabled
                                         MailTipsAccessLevel

SharingPolicyDataList              Information about the Sharing Policies configured in the
                                   organization:

                                         Name
                                         Enabled
                                         Domains

AmsiDataValue                      Information about the AMSI configuration:

                                         EnabledAll
                                         EnabledApi
                                         EnabledAutoD
                                         EnabledEas
                                         EnabledEcp
                                         EnabledEws
                                         EnabledMapi
                                         EnabledOab
                                         EnabledOwa
                                         EnabledPowerShell
                                         EnabledOthers

BinaryFormatterDataValue           Information about the Binary Formatter configuration:

                                         EnableSecureDeserializerLocation
                                         EnableFirstFallbackDeserializerLocation
                                         EnableSecondFallbackDeserializerLocation

<!-- p.2896 -->

 Data                           Description

 FlightingDataValue             Information about the flights configured via Feature Flighting :

                                      FeaturesAwaitingAdminApproval
                                      FeaturesBlocked
                                      FeaturesEnabled
                                      RingLevel

 IsAppIdIsolationEnabled        Indicates whether the dedicated Exchange hybrid application feature
                                is enabled

How to configure the Diagnostic Data setting after
installation is complete
After the Setup has completed, you can enable and disable sending the diagnostic data to the
OCS on any Exchange server using the Set-ExchangeServer cmdlet.

To disable sending optional data to Microsoft:

 Powershell
 Set-ExchangeServer -Identity <ServerName> -DataCollectionEnabled:$false

To enable sending optional data to Microsoft:

 Powershell
 Set-ExchangeServer -Identity <ServerName> -DataCollectionEnabled:$true

Last updated on 12/09/2025

<!-- p.2897 -->

Antispam and antimalware protection in
Exchange Server
07/28/2025

APPLIES TO:       2016       2019      Subscription Edition

Antispam and antimalware protection are included in Exchange Server 2016 and Exchange
Server 2019.

     Antispam protection is provided by the same built-in transport agents that were
     introduced in Exchange Server 2010. These agents are enabled by default on Edge
     Transport servers, and you can enable many of them on Exchange Mailbox servers.

     Antimalware protection is provided by the Malware agent that was introduced in
     Exchange Server 2013. The Malware agent is available and enabled by default on
     Exchange Mailbox servers.

The following table contains links to topics that provide overview information and
configuration steps for customizing the built-in spam and malware filtering settings for your
organization.

                                                                                       ﾉ   Expand table

 Topic                              Description

 Antispam protection in Exchange    Describes the built-in antispam protection features in Exchange
 Server                             Server, and how to configure the antispam protection options.

 Running Windows antivirus          Describes considerations for running Windows antivirus programs on
 software on Exchange servers       Exchange servers.

If you're looking for information about antispam features in the cloud, see Anti-spam
protection in cloud organizations.

<!-- p.2898 -->

Antispam protection in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

Spammers, or malicious senders, use a variety of techniques to send unwanted email into your
organization. No single tool or process can eliminate all spam. However, Microsoft Exchange
provides a layered, multifaceted approach to reducing these unwanted messages. Exchange
uses transport agents to provide antispam protection, and the built-in agents that are available
in Exchange Server 2016 and Exchange Server 2019 are relatively unchanged from Exchange
Server 2010. In Exchange 2016 and Exchange 2019, configuration and management of these
agents is available only in the Exchange Management Shell.

For more antispam features and easier management, you can purchase Exchange Online
Protection (EOP), which is part of Microsoft 365 and Office 365. To learn more about Microsoft
365 or Office 365 antispam protection, see Anti-spam protection in EOP.

Antispam agents on Mailbox servers
Typically, you enable the antispam agents on a Mailbox server if your organization doesn't
have an Edge Transport server, or if it doesn't do other antispam filtering on incoming
messages. For more information, see Enable antispam functionality on Mailbox servers.

Like all transport agents, each antispam agent is assigned a priority value. A lower value
indicates a higher priority, so typically, an antispam agent with priority 1 acts on a message
before an antispam agent with priority 9. However, the SMTP event in the transport pipeline
where the antispam agent is registered is also very important in determining the order that
antispam agent acts on messages. A low priority antispam agent that's registered early in the
transport pipeline acts on messages before a high priority antispam agent that's registered
later in the transport pipeline.

Based on the default priority value of the agent and the SMTP event where the agent is
registered, this is the order that the antispam agents are applied to messages on Mailbox
servers:

   1. Sender Filter agent: Sender filtering compares the sending server to a list of senders or
      sender domains that are prohibited from sending messages to your organization. For
      more information, see Sender filtering.

   2. Sender ID agent: Sender ID relies on the IP address of the sending server and the
      Purported Responsible Address (PRA) of the sender to determine whether the sending
      email address is spoofed. For more information, see Sender ID.

<!-- p.2899 -->

   3. Content Filter agent: Content filtering agent assigns a spam confidence level (SCL) to
     each message based on data from legitimate and spam messages. For more information,
     see Content filtering.

     Spam quarantine is a component of the Content Filter agent that reduces the risk of
     losing legitimate messages that are incorrectly classified as spam. Spam quarantine
     provides a temporary storage location for suspicious messages so an administrator can
     review the messages. For more information, see Spam quarantine in Exchange Server.

     Content filtering also uses the safelist aggregation feature. Safelist aggregation collects
     safe list data that users configure in Microsoft, Outlook, and Outlook on the web and
     makes this information available to the Content Filter agent. For more information, see
     Safelist aggregation.

   4. Protocol Analysis agent (sender reputation): The Protocol Analysis agent is the agent
     that provides sender reputation. Sender reputation uses several tests to calculate a sender
     reputation level (SRL) on incoming messages that determines the action to take on those
     messages. For more information, see Sender reputation and the Protocol Analysis agent.

Antispam agents on Edge Transport servers
If your organization has an Edge Transport server installed in the perimeter network, all of the
antispam agents that are available on a Mailbox server are installed and enabled by default on
the Edge Transport server. However, the following antispam agents are available only on Edge
Transport servers:

     Connection Filtering agent: Connection filtering uses an IP block list, IP allow list, IP block
     list providers, and IP allow list providers to determine whether a connection should be
     blocked or allowed. For more information, see Connection filtering on Edge Transport
     servers.

     Recipient Filter agent: Recipient filtering uses a recipient block list to identify messages
     that aren't allowed to enter the organization. The recipient filter also uses the local
     recipient directory to reject messages sent to invalid recipients. For more information, see
     Recipient filtering on Edge Transport servers.

        ７ Note

        Although the Recipient Filter agent is available on Mailbox servers, you shouldn't
        configure it. When recipient filtering on a Mailbox server detects one invalid or
        blocked recipient in a message that contains other valid recipients, the message is

<!-- p.2900 -->

        rejected. The Recipient Filter agent is enabled when you install the antispam agents
        on a Mailbox server, but it isn't configured to block any recipients.

     Attachment Filtering agent: Attachment filtering blocks messages or attachments based
     on the attachment file name, extension, or MIME content type. For more information, see
     Attachment filtering on Edge Transport servers.

Based on the default priority value of the antispam agent, and the SMTP event in the transport
pipeline where the agent is registered, this is the order that the antispam agents are applied to
messages on Edge Transport servers:

   1. Connection Filtering agent

   2. Sender Filter agent

   3. Recipient Filter agent

   4. Sender ID agent

   5. Content Filter agent

   6. Protocol Analysis agent (sender reputation)

   7. Attachment Filtering agent

Antispam stamps
Antispam stamps are applied to messages and are used by the antispam agents. You can view
the antispam stamps to help you diagnose spam-related problems. For more information, see
Antispam stamps.

Strategy for antispam approach
Antispam is a balancing act between blocking unwanted messages and allowing legitimate
messages. If you configure the antispam features too aggressively, you'll likely block too many
legitimate messages (false positives). If you configure the antispam features too loosely, you
likely allow too much spam into your organization.

These are some best practices to consider when configuring the built-in antispam features in
Exchange:

     Reject messages that are identified by the Connection Filtering agent, Recipient Filter
     agent, and Sender Filter agent rather than quarantining the messages or applying

<!-- p.2901 -->

     antispam stamps. This approach is recommended for these reasons:

       Messages that are identified by the default settings of the connection filtering,
       recipient filtering, or sender filtering typically don't require further tests to determine if
       they're unwanted. For example, if you configured sender filtering to block specific
       senders, there's no reason to continue to process messages from those senders. (If you
       didn't want the messages rejected, you wouldn't have put them on the blocked
       senders list).

       Configuring a more aggressive level for the antispam agents that encounter messages
       early in the transport pipeline saves processing, bandwidth, and disk resources. The
       farther in transport pipeline a message travels, the greater number of variables that the
       remaining antispam features need to evaluate to successfully identify the message as
       spam. Reject obvious messages early so you can process ambiguous messages later.

     You need to monitor the effectiveness of the antispam features at their current
     configuration levels. Monitoring allows you to react to trends and increase or decrease
     the aggressiveness of the settings. You should start with the default settings to minimize
     the number of false positives. As you monitor the amount of spam and false positives,
     you can increase the aggressiveness of the settings based on the type of spam and spam
     attacks that your organization experiences.

See also
Anti-spam protection in EOP

<!-- p.2902 -->

Enable antispam functionality on Mailbox
servers
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

The following antispam agents are available in the Transport service on Exchange 2016 and
Exchange 2019 Mailbox servers, but they aren't installed by default:

      Content Filter agent

      Sender Filter agent

      Sender ID agent

      Protocol Analysis agent for sender reputation

You can install these antispam agents on a Mailbox server by using an Exchange Management
Shell script, which is important if these agents are your only defense to help prevent spam.
Typically, you don't need to install the antispam agents on a Mailbox server when your
organization uses other types of antispam filtering on incoming mail.

  ７ Note

  Although the Recipient Filter agent is available on Mailbox servers, you shouldn't
  configure it. When recipient filtering on a Mailbox server detects one invalid or blocked
  recipient in a message that contains other valid recipients, the message is rejected. The
  Recipient Filter agent is enabled when you install the antispam agents on a Mailbox server,
  but it isn't configured to block any recipients.

What do you need to know before you begin?
      Estimated time to complete this task: 15 minutes

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      The Connection Filtering agent and the Attachment Filtering agent aren't available on
      Mailbox servers. They're only available on Edge Transport servers, and they're installed
      and enabled there by default. However, the Malware agent is installed and enabled by

<!-- p.2903 -->

     default on Mailbox servers. For more information, see Antimalware protection in
     Exchange Server.

     If you have other Exchange antispam agents operating on the messages before they
     reach the Mailbox server (for example, an Edge Transport server in the perimeter
     network), the antispam agents on the Mailbox server recognize the antispam X-header
     values that already exist in messages, and those messages pass through without being
     scanned again.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Transport configuration" entry in
     the Mail flow permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Step 1: Run the Install-AntispamAgents.ps1
PowerShell script
Run the following command in the Exchange Management Shell on the Mailbox server:

  PowerShell

  & $env:ExchangeInstallPath\Scripts\Install-AntiSpamAgents.ps1

How do you know this step worked?
You know this step worked if the script runs without errors and asks you to restart the
Microsoft Exchange Transport service. The output looks like this:

  Output

  WARNING: Please exit Windows PowerShell to complete the installation.
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport

<!-- p.2904 -->

  Identity                                           Enabled         Priority
  --------                                           -------         --------
  Content Filter Agent                               True            8
  WARNING: Please exit Windows PowerShell to complete the installation.
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  Sender Id Agent                                    True            9
  WARNING: Please exit Windows PowerShell to complete the installation.
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  Sender Filter Agent                                True            10
  WARNING: Please exit Windows PowerShell to complete the installation.
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  Recipient Filter Agent                             True            11
  WARNING: Please exit Windows PowerShell to complete the installation.
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  WARNING: The following service restart is required for the change(s) to take
  effect : MSExchangeTransport
  Protocol Analysis Agent                            True            12
  WARNING: The agents listed above have been installed. Please restart the Microsoft
  Exchange Transport service for
  changes to take effect.

Step 2: Restart the Microsoft Exchange Transport
service
Run the following command in the Exchange Management Shell on the Mailbox server:

  PowerShell

  Restart-Service MSExchangeTransport

How do you know this step worked?
You know this step worked if the Microsoft Exchange Transport service restarts without errors.
The output looks like this:

  Output

<!-- p.2905 -->

  WARNING: Waiting for service 'Microsoft Exchange Transport (MSExchangeTransport)'
  to start...
  WARNING: Waiting for service 'Microsoft Exchange Transport (MSExchangeTransport)'
  to start...
  WARNING: Waiting for service 'Microsoft Exchange Transport (MSExchangeTransport)'
  to start...
  WARNING: Waiting for service 'Microsoft Exchange Transport (MSExchangeTransport)'
  to start...
  WARNING: Waiting for service 'Microsoft Exchange Transport (MSExchangeTransport)'
  to start...
  WARNING: Waiting for service 'Microsoft Exchange Transport (MSExchangeTransport)'
  to start...

Step 3: Specify the internal SMTP servers in your
organization
You need to specify the IP addresses of every internal SMTP server that should be ignored by
the Sender ID agent. In fact, you need to specify the IP address of at least one internal SMTP
server. If the Mailbox server where you're running the antispam agents is the only SMTP server
in your organization, specify the IP address of that computer.

To add the IP addresses of internal SMTP servers without affecting any existing values, run the
following command in the Exchange Management Shell on the Mailbox server:

  PowerShell

  Set-TransportConfig -InternalSMTPServers @{Add="<ip address1>","<ip address2>"...}

This example adds the internal SMTP server addresses 10.0.1.10 and 10.0.1.11 to the transport
configuration of your organization.

  PowerShell

  Set-TransportConfig -InternalSMTPServers @{Add="10.0.1.10","10.0.1.11"}

How do you know this step worked?
To verify that you have successfully specified the IP address of at least one internal SMTP
server, run the following command in the Exchange Management Shell on the Mailbox server,
and verify that the IP address of at least one valid internal SMTP server is displayed.

  PowerShell

<!-- p.2906 -->

 Get-TransportConfig | Format-List InternalSMTPServers

Step 4: Next steps
   The Content Filter agent, Sender ID agent, Sender Filter agent, and Protocol Analysis
   (sender reputation) agent should now be installed and running on the Mailbox server. To
   verify this, run the following commands in the Exchange Management Shell on the
   Mailbox server:

     PowerShell

     Get-TransportAgent

     PowerShell

     Get-ContentFilterConfig | Format-Table Name,Enabled; Get-SenderFilterConfig |
     Format-Table Name,Enabled; Get-SenderIDConfig | Format-Table Name,Enabled;
     Get-SenderReputationConfig | Format-Table Name,Enabled

   To see detailed information about the configuration of each agent, run the following
   commands:

     PowerShell

     Get-ContentFilterConfig | Format-List
     *Enabled,RejectionResponse,*Postmark*,Bypassed*,Quarantine*;

     PowerShell

     Get-SenderFilterConfig | Format-List *Enabled,*Block*

     PowerShell

     Get-SenderIDConfig | Format-List *Enabled*,*Action,Bypassed*

     PowerShell

     Get-SenderReputationConfig | Format-List *Enabled*,*Proxy*,*Block*,*Ports*

   To configure each agent, see the following topics:

<!-- p.2907 -->

        Content filtering procedures

        Safelist aggregation procedures

        Configure Content Filtering to Use Safe Domain Data

        Exchange spam confidence level (SCL) thresholds

        Sender filtering procedures

        Sender ID procedures

        Sender reputation procedures

     By default, the Content Filter agent, the Sender Filter agent, and the Sender ID agent
     record their activities in the antispam agent log on the Mailbox server. You can verify that
     these antispam agents are working when information is written to the log. To see the
     location and configuration of the log, run the following command in the Exchange
     Management Shell on the Mailbox server:

       PowerShell

       Get-TransportService | Format-List AgentLog*

For instructions on how to configure the log, see Configure antispam Agent Logging.

<!-- p.2908 -->

Antispam stamps
Article • 04/30/2025

APPLIES TO:        2016          2019   Subscription Edition

Antispam stamps in Exchange Server apply diagnostic metadata, or stamps, such as sender-
specific information, puzzle validation results, and content filtering results, to messages as they
pass through the antispam features that filter inbound messages from the Internet. You can use
antispam stamps to see the results of antispam filtering on a message, and to diagnose spam-
related problems. The antispam features and stamps are basically unchanged from Exchange
Server 2010. There are four major Exchange antispam stamps:

      The phishing confidence level (PCL) stamp

      The Sender ID stamp

      The spam confidence level (SCL) stamp

      The antispam report stamp

The antispam stamps are added to messages as X-header fields in the message header. You
can view antispam stamps on a message by using Outlook. For more information, see View
antispam stamps in Outlook.

The phishing confidence level stamp
The PCL stamp indicates the likelihood that a message is a phishing message based on its
content. The PCL stamp is applied when the message is processed by the Content Filter agent.
For more information about content filtering, see Content filtering.

The PCL values are described in the following table.

                                                                                           ﾉ   Expand table

 PCL value             Verdict          Description

 1 through 3           Neutral          The message content isn't likely to be phishing.

 4 through 8           Suspicious       The message content is likely to be phishing.

The PCL value appears in the X-MS-Exchange-Organization-PCL: X-header, and the PCL
verdict appears in the antispam report stamp as PCL:PhishingLevel <Verdict> . Outlook uses
the PCL stamp to block the content of suspicious messages.

<!-- p.2909 -->

The Sender ID stamp
The Sender ID stamp is based on the sender policy framework (SPF) that authorizes the use of
domains in email. The Sender ID agent determines the Sender ID status for the message. These
status values are described in the following table.

                                                                                        ﾉ   Expand table

 Status       Description

 Pass         Both the IP address and Purported Responsible Address (PRA) passed the Sender ID
              verification check.

 Neutral      Published Sender ID data is explicitly inconclusive.

 SoftFail     The IP address for the PRA may be in the not permitted set.

 Fail         The IP Address is not permitted. No PRA is found in the incoming mail or the sending
              domain does not exist.

 None         No published SPF data exists in the sender's DNS.

 TempError    A temporary DNS failure occurred, such as an unavailable DNS server.

 PermError    The DNS record is invalid, such as an error in the record format.

The Sender ID stamp is displayed in the X-MS-Exchange-Organization-SenderIdResult: X-
header, and also in the antispam report stamp as SenderIDStatus <Status> . The SPF result is
displayed in the Received-SPF header.

For more information, see the following topics:

        Sender ID

        Sender Policy Framework: SPF Record Syntax

The spam confidence level stamp

  ７ Note

  In November, 2016, Microsoft stopped producing spam definition updates for the
  SmartScreen filters in Exchange and Outlook. The existing SmartScreen spam definitions
  were left in place, but their effectiveness will likely degrade over time. For more
  information, see Deprecating support for SmartScreen in Outlook and Exchange                   .

<!-- p.2910 -->

The SCL stamp displays the rating of the message based on its content. The Content Filter
agent uses Microsoft SmartScreen technology to assess the contents of a message, and to
assign an SCL rating to each message. The SCL values are described in the following table.

                                                                                       ﾉ   Expand table

 SCL value     Description

 0 through     0 indicates an extremely low probability that the message is spam.
 9             9 indicates an extremely high probability that the message is spam.

 -1            The message bypassed antispam scanning (for example, the message was from an internal
               sender).

The SCL value appears in the X-MS-Exchange-Organization-SCL: X-header.

The actions that Exchange and Outlook take based on the SCL value depend on your SCL
threshold settings. For more information, see Exchange spam confidence level (SCL) thresholds.

The antispam report stamp
The antispam report stamp is a summary of the antispam filter results that have been applied
to the message. The Content Filter agent applies this stamp to the message in the X-MS-
Exchange-Organization-Antispam-Report: X-header. The anti spam report uses the following
syntax:

     X-MS-Exchange-Organization-Antispam-Report: DV:
     <DATVersion>;CW:CustomList;PCL:PhishingVerdict
     <verdict>;P100:PhishingBlock;PP:Presolve;SID:SenderIDStatus <status>;TIME:
     <SendReceiveDelta>;MIME:MimeCompliance;OrigIP:<SourceIPAddress>

The antispam filter information that can appear in the antispam report stamp is described in
the following table. Note that the antispam report stamp only contains results and conclusions
from antispam filters that were applied to the message. so the antispam report stamp usually
doesn't contain all of the possible stamps and values.

                                                                                       ﾉ   Expand table

 Stamp                              Description

 DV                                 The DAT version (DV) stamp indicates the version of the spam
                                    definition file that was used when scanning the message.

<!-- p.2911 -->

Stamp                    Description

SA                       The signature action (SA) stamp indicates that the message was either
                         recovered or deleted because of a signature that was found in the
                         message.

SV                       The signature DAT version (SV) stamp indicates the version of the
                         signature file that was used when scanning the message.

CW                       The custom weight (CW) stamp indicates that the message contains
                         an unapproved word or phrase and that the SCL value, or weight, of
                         that unapproved word or phrase was applied to the final SCL score:
                               Unapproved phrases, or Block phrases, have maximum weight
                               and change the SCL score to 9.
                               Approved words or phrases, or Allow phrases, have minimum
                               weight and change the SCL score to 0.

                         For more information about how to add approved and unapproved
                         words or phrases to the Content Filtering agent, see Content filtering
                         procedures.

PP                       The presolved puzzle (PP) stamp indicates that if a sender's message
                         contains a valid, solved computational postmark (based on Outlook E-
                         mail Postmark validation functionality), it's unlikely that the sender is a
                         malicious sender. In this case, the Content Filter agent would reduce
                         the SCL rating.
                         The Content Filter agent doesn't change the SCL rating if the E-mail
                         Postmark validation feature is enabled and either of the following
                         conditions is true:

                               An inbound message doesn't contain a computational postmark
                               header.
                               The computational postmark header isn't valid.

                         For more information about the postmark validation feature, see
                         Content filtering.

TIME:TimeBasedFeatures   Indicates that there was a significant time delay between the time that
                         the message was sent and the time that the message was received.
                         The TIME stamp is used to determine the final SCL rating for the
                         message.

OrigIP                   Indicates the IP address of the source messaging server.

MIME:MIMECompliance      Indicates that the email message isn't MIME compliant.

P100:PhishingBlock       Indicates that the message contains a URL that's present in a phishing
                         definition file.

IPOnAllowList            Indicates that the sender's IP address is on the IP Allow list. For more
                         information about the IP Allow list, see IP Allow list.

<!-- p.2912 -->

Stamp                           Description

MessageSecurityAntispamBypass   Indicates that the message wasn't filtered for content and that the
                                sender has been granted permission to bypass the antispam filters.

SenderBypassed                  Indicates that the Content Filter agent doesn't process any content
                                filtering for messages that are received from this sender. For more
                                information, see Content filtering procedures.

AllRecipientsBypassed           Indicates that one of the following conditions was met for all
                                recipients listed in the message:
                                       The AntispamBypassedEnabled parameter on the recipient's
                                       mailbox is set to $true . For more information, see Use the
                                      Exchange Management Shell to configure a mailbox to bypass
                                      Exchange antispam filtering.
                                      The message sender is in the recipient's Safe Senders List. For
                                      more information about the Safe Senders List, see Use the
                                      Exchange Management Shell to configure the safelist collection
                                      on a mailbox.
                                      The Content Filter agent doesn't process any content filtering
                                      for messages that are sent to this recipient. For more
                                      information about recipient exceptions, see Use the Exchange
                                      Management Shell to configure recipient and sender exceptions
                                      for content filtering.

<!-- p.2913 -->

View antispam stamps in Outlook
07/22/2025

APPLIES TO:       2016     2019      Subscription Edition

The built-in antispam agents in Exchange Server apply diagnostic metadata, or stamps, as X-
headers to messages as they enter your organization. For more information about these
stamps, see Antispam stamps. You can use Microsoft Outlook to view the antispam X-header
fields in messages to help you diagnose spam-related problems.

What do you need to know before you begin?
     Estimated time to complete this procedure: less than 5 minutes

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox access" entry in the Mail
     flow permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use Outlook 2010 or later to view antispam stamps
   1. Open Outlook on a client computer, and in the Mail view, double-click a message to
     open it.

   2. In the Tags section of the Ribbon, click the Message Options icon to display the message
     Properties dialog box.

   3. In the Properties dialog box, in the Internet headers section, use the scroll bar to view
     the antispam X-headers. The header fields to look for are:

             X-MS-Exchange-Organization-SenderIdResult:

             X-MS-Exchange-Organization-SCL:

             X-MS-Exchange-Organization-PCL:

<!-- p.2914 -->

           X-MS-Exchange-Organization-Antispam-Report:

It can be easier for you to find these values by selecting all of the text in the Internet headers
field (CTRL key + A), copying the text (CTRL key + C, or right-click and choose Copy), and
pasting the text into Notepad.

Here's an example of the values that you might find in a suspicious messages:

  X-MS-Exchange-Organization-SenderIdResult:Fail
  X-MS-Exchange-Organization-SCL:6
  X-MS-Exchange-Organization-PCL:7X-MS-Exchange-Organization-Antispam-Report:
  DV:3.3.15608.880;SID:SenderIDStatus Fail;PCL:PhishingLevel
  SUSPICIOUS;CW:CustomList;PP:Presolved;TIME:TimeBasedFeatures;OrigIP:10.1.1.1

<!-- p.2915 -->

Configure Exchange antispam settings on
mailboxes
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

In Exchange Server, you can configure specific antispam settings on individual mailboxes that
are different than the antispam settings that are applied to the rest of the mailboxes in your
organization. The antispam settings that are available on mailboxes are basically unchanged
from Exchange 2010.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Antispam features" entry in the
      Antispam and antimalware permissions topic, and the "Antispam" entry in the Recipients
      Permissions topic.

      By default, antispam features aren't enabled in the Transport service on a Mailbox server.
      Typically, you only enable the antispam features on a Mailbox server if your Exchange
      organization doesn't do any prior antispam filtering before accepting incoming messages.
      For more information, see Enable antispam functionality on Mailbox servers.

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Use the Exchange Management Shell to enable or
disable the junk email rule in a mailbox

<!-- p.2916 -->

By default, the junk email rule (a hidden Inbox rule named Junk E-mail Rule) is enabled in every
mailbox, and controls the following Exchange antispam features:

     Message delivery to the Junk Email folder based on the SCL Junk Email folder
     threshold: When a message is assigned a spam confidence level (SCL) value by Exchange,
     and the SCL value is greater than the SCL Junk Email folder threshold value that's
     configured for the Exchange organization (the default value is 4) or directly on the
     mailbox (the default value is not configured), the junk email filter rule moves the message
     to the Junk Email folder.

     Message delivery to the Junk Email folder based on the safelist collection on the
     mailbox: The entries in the Safe Senders list, Safe Recipients list, and Block Senders list
     that are configured on the mailbox determine whether the junk email rule delivers the
     message to the Inbox or the Junk Email folder. Users can configure the safelist collection
     for their own mailbox in Microsoft Outlook or Outlook on the web. Administrators can
     configure the safelist collection for a mailbox by using the Set-
     MailboxJunkEmailConfiguration cmdlet.

When the junk email rule is enabled in the mailbox, Exchange is able to deliver messages to the
Junk Email folder (based on the Blocked Senders list or SCL Junk Email folder threshold), and
prevent messages from being delivered to the Junk Email folder (based on the Safe Senders
list). This value corresponds to the Outlook on the web setting: Automatically filter junk email.

When the junk email rule is disabled on the mailbox, Exchange can't deliver messages to the
Junk Email folder based on the SCL Junk Email folder threshold or the safelist collection on the
mailbox. This value corresponds to the Outlook on the web setting: Don't move email to my
Junk Email folder.

To enable or disable the junk email rule on a mailbox, use the following syntax:

  PowerShell

  Set-MailboxJunkEmailConfiguration <MailboxIdentity> -Enabled <$true | $false>

This example disables the junk email rule on Ori Epstein's mailbox.

  PowerShell

  Set-MailboxJunkEmailConfiguration "Ori Epstein" -Enabled $false

This example disables the junk email rule on all user mailboxes in the Organizational Unit
named North America in the consoto.com domain.

<!-- p.2917 -->

  PowerShell

  Get-Mailbox -RecipientTypeDetails UserMailbox -OrganizationalUnit
  "contoso.com/North America" | Set-MailboxJunkEmailConfiguration -Enabled $false

This example disables the junk email rule on all user mailboxes in the mailbox database named
MDB 01.

  PowerShell

  Get-Mailbox -RecipientTypeDetails UserMailbox -Database "MDB 01" | Set-
  MailboxJunkEmailConfiguration -Enabled $false

This example disables the junk email rule on all user mailboxes in the organization.

  PowerShell

  $All = Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize Unlimited; $All |
  foreach {Set-MailboxJunkEmailConfiguration $_.Name -Enabled $false}

For more information, see Set-MailboxJunkEmailConfiguration.

Notes:

     You can only use the Set-MailboxJunkEmailConfiguration cmdlet to disable the junk
     email rule on a mailbox that's been opened in Outlook (in Cached Exchange mode) or
     Outlook on the web. If the mailbox hasn't been opened, you'll receive the error: The Junk
     Email configuration couldn't be set. The user needs to sign in to Outlook Web App
     before they can modify their Safe Senders and Recipients or Blocked Senders lists. If

     you want to suppress this error for bulk operations, you can add -ErrorAction
     SlientlyContinue to the Set-MailboxJunkEmailConfiguration command.

     Disabling the junk email rule on the mailbox prevents the rule from moving messages to
     the Junk Email folder. However, the Outlook Junk Email Filter can also determine whether
     a message is spam, and is able to use the safelist collection to move messages to the
     Inbox or the Junk Email folder. For more information, see the About junk email settings in
     Outlook section in this topic.

How do you know this worked?
To verify that you have successfully enabled or disabled the junk email rule on a mailbox, use
any of the following procedures:

<!-- p.2918 -->

     Replace <MailboxIdentity> with the identity of the mailbox, and run the following
     command to verify the Enabled property value:

        PowerShell

        Get-MailboxJunkEmailConfiguration <MailboxIdentity> | Format-List Enabled

     For bulk operations, use the same filter that identified the mailboxes, and replace the Set-
     MailboxJunkEmailConfiguration command with Get-MailboxJunkEmailConfiguration |
     Format-Table -Auto Identity,Enabled . For example:

        PowerShell

        Get-Mailbox -RecipientTypeDetails UserMailbox -OrganizationalUnit
        "contoso.com/North America" | Get-MailboxJunkEmailConfiguration | Format-
        Table -Auto Identity,Enabled

     Replace <MailboxIdentity> with the identity of the mailbox, and run the following
     command to verify the Enabled property value of the junk email rule.

        PowerShell

        Get-InboxRule "Junk E-mail Rule" -Mailbox <MailboxIdentity> -IncludeHidden

Use the Exchange Management Shell to configure
the safelist collection on a mailbox
The safelist collection on a mailbox includes the Safe Senders list, the Safe Recipients list, and
the Blocked Senders list. By default, users can configure the safelist collection on their own
mailbox in Outlook or Outlook on the web. Administrators can use the corresponding
parameters on the Set-MailboxJunkEmailConfiguration cmdlet to configure the safelist
collection on a user's mailbox. These parameters are described in the following table.

                                                                                  ﾉ   Expand table

 Parameter on Set-                            Outlook Web App setting
 MailboxJunkEmailConfiguration

 BlockedSendersAndDomains                     Move email from these senders or domains to my Junk
                                              Email folder

 ContactsTrusted                              Trust email from my contacts

<!-- p.2919 -->

 Parameter on Set-                           Outlook Web App setting
 MailboxJunkEmailConfiguration

 TrustedListsOnly                            Don't trust email unless it comes from someone in my
                                             Safe Senders and Recipients list

 TrustedSendersAndDomains                    Don't move email from these senders or domains to my
 TrustedRecipientsAndDomains                 Junk Email folder

To configure the safelist collection on a mailbox, use the following syntax:

  PowerShell

  Set-MailboxJunkEmailConfiguration <MailboxIdentity> -BlockedSendersAndDomains
  <EmailAddressesOrDomains | $null> -ContactsTrusted <$true | $false> -
  TrustedListsOnly <$true | $false> -TrustedSendersAndDomains
  <EmailAddressesOrDomains | $null>

To enter multiple values and overwrite any existing entries for the BlockedSendersAndDomains
and TrustedSendersAndDomains parameters, use the following syntax: "
<EmailAddressOrDomain1>","<EmailAddressOrDomain2>"... . To add or remove one or more values

without affecting other existing entries, use the following syntax: @{Add="
<EmailAddressOrDomain1>","<EmailAddressOrDomain2>"... ; Remove="
<EmailAddressOrDomain3>","<EmailAddressOrDomain4>...}

This example configures the following settings for the safelist collection on Ori Epstein's
mailbox:

     Adds the value shopping@fabrikam.com to the Blocked Senders list.

     Removes the value chris@fourthcoffee.com from the Safe Senders list and the Safe
     Recipients list.

     Configures contacts in the Contacts folder to be treated as trusted senders.

  PowerShell

  Set-MailboxJunkEmailConfiguration "Ori Epstein" -BlockedSendersAndDomains
  @{Add="shopping@fabrikam.com"} -TrustedSendersAndDomains
  @{Remove="chris@fourthcoffee.com"} -ContactsTrusted $true

This example empties the Blocked Senders list for all user mailboxes in the Organizational Unit
named North America in the contoso.com domain.

  PowerShell

<!-- p.2920 -->

  Get-Mailbox -RecipientTypeDetails UserMailbox -OrganizationalUnit
  "contoso.com/North America" | Set-MailboxJunkEmailConfiguration -
  BlockedSendersAndDomains $null

This example adds michelle@tailspintoys.com to the Safe Senders list and Safe Recipients list
on all user mailboxes in the mailbox database named MDB 01.

  PowerShell

  Get-Mailbox -RecipientTypeDetails UserMailbox -Database "MDB 01" | Set-
  MailboxJunkEmailConfiguration -TrustedSendersAndDomains
  @{Add="michelle@tailspintoys.com"}

This example removes the domain contoso.com from the Blocked Senders list in all user
mailboxes in the organization.

  PowerShell

  $All = Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize Unlimited; $All |
  foreach {Set-MailboxJunkEmailConfiguration $_.Name -BlockedSendersAndDomains
  @{Remove="contoso.com"}}

For more information, see Set-MailboxJunkEmailConfiguration.

Notes:

     You can only use the Set-MailboxJunkEmailConfiguration cmdlet to configure the safelist
     collection on a mailbox that's been opened in Outlook (in Cached Exchange mode) or
     Outlook on the web. If the mailbox hasn't been opened, you'll receive the error: The Junk
     Email configuration couldn't be set. The user needs to sign in to Outlook Web App
     before they can modify their Safe Senders and Recipients or Blocked Senders lists. If

     you want to suppress this error for bulk operations, you can add -ErrorAction
     SlientlyContinue to the Set-MailboxJunkEmailConfiguration command.

     Disabling the junk email rule in the mailbox prevents the rule from moving messages to
     the Junk Email folder or keeping messages out of the Junk Email folder based on the
     safelist collection. However, even with the junk email rule disabled, you can still configure
     the safelist collection, and the Outlook Junk Email Filter is able to use the safelist
     collection to move messages to the Inbox or the Junk Email folder. For more information,
     see the About junk email settings in Outlook section in this topic.

     The safelist aggregation feature of the Content Filter agent is able to share the safelist
     collection of mailboxes with the built-in Exchange antispam agents. For more information,
