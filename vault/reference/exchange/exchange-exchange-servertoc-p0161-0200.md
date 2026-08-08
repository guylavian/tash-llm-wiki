---
title: "Exchange Server — pages 161-200"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0161-0200
family: exchange
documentKind: "doc"
abstract: "4.8 GB will be reserved by the Information Store for the two passive database copies in case they become active copies. If this happens, they'll use their Max Cache Target of 3 GB. Example 2 Mailbox server configuration: 48 GB of memory Two active databases and two passive datab"
---

# Exchange Server — pages 161-200

<!-- p.161 -->

     4.8 GB will be reserved by the Information Store for the two passive database copies in
     case they become active copies. If this happens, they'll use their Max Cache Target of 3
     GB.

Example 2
Mailbox server configuration:

     48 GB of memory

     Two active databases and two passive databases

     MaximumActiveDatabases parameter: 2

The amount of database cache is 5 GB for each active database copy worker process and 0.2
GB for each passive database copy worker process. Here's how these values are calculated:

     Server Cache Size Target: 25% of the amount of memory: 48 GB * 0.25 = 12 GB.

     Database Max Cache Target: Divide the Server Cache Size Target by the sum of:

        The number of active databases

        20% of the number of passive databases

     12 GB / (2A + (2P * 0.20)) = 5 GB

     Memory used for passive database copies: 20% of the Database Max Cache Target: 5 GB
     * 0.20 = 1 GB.

Out of the 12 GB of memory assigned to the Server Cache Size Target:

     12 GB will be in use by database worker processes

     No memory will be reserved by the Information Store for the two passive database copies
     because they can't become active copies (MaximumActiveDatabases is configured with a
     value of 2, and there are already 2 active database copies on the server).

<!-- p.162 -->

Managed Store Limits in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

The Managed Store in Exchange Server 2016 and Exchange Server 2019 is the name for the
Information Store (also known as the Store) processes that manages mailbox databases. The
Managed Store has connection and usage limits that prevent a single application or a single
user from using all of the available connections, which could result in downtime. This topic
describes the limits and how you can change them.

For more information about the Managed Store, see Managed Store in Exchange Server.

  ７ Note

  Connections by administrator accounts have maximum session limits of 64000.

  Exchange Online limits (including Managed Store limits) are described in the Exchange
  Online Limits.

Terminology
Knowledge of the following terms will help you understand the types of connections
referenced in this topic.

      Sessions

      Sessions represent the connections used by services and client applications (for example,
      Microsoft Outlook) to connect to the Managed Store. Services and clients can have
      multiple sessions at a particular time. The terms connections and sessions can be used
      interchangeably.

      Threads

      Threads represent concurrently executing requests to the Managed Store. For example, if
      a user opens a folder in Outlook, Outlook executes a request to the Managed Store on
      behalf of the user. That execution of the request is a single thread.

      For all clients, the maximum number of threads per mailbox database is 50. The
      exception is the Availability service, which has a maximum limit of 16 per user.

Session limits

<!-- p.163 -->

Session limits are based on connections per mailbox database on the server.

The types of connection limits are:

      Max sessions per process: The maximum number of sessions that an Exchange service
      can have open at one time on a mailbox database.

      Max user sessions per process: The maximum number of sessions for a specific protocol
      for a single user.

The types of client connections to the Managed Store and the limits based on those
connections are described in the following table.

                                                                                 ﾉ   Expand table

 Client type                               Max sessions per         Default number of user
                                           mailbox database         sessions per mailbox database

 Admin                                     10000                    n/a

 Availability service                      10000                    16

 Content indexing                          10000                    n/a

 Exchange ActiveSync                       n/a                      16

 Exchange Web Services                     n/a                      16

 Management                                n/a                      16

 MAPI on the Middle Tier (MoMT)            n/a                      32

 MSExchangeMailboxAssistants: Events       10000                    n/a

 MSExchangeMailboxAssistants: Timed        10000                    n/a

 MSExchange Remote Procedure Call          n/a                      16

 Outlook on the web (formerly known as     n/a                      16
 Outlook Web App)

 POP3 and IMAP4                            n/a                      16

 Transport                                 10000                    n/a

 Unified Messaging (Exchange 2016 only)    n/a                      16

 Others                                    n/a                      16

Use the following procedure to modify the default session limits.

<!-- p.164 -->

Notes:

     When you modify a session limit, you need to modify that limit on all Mailbox servers
     within a database availability group (DAG). If you don't make the same changes on all
     servers, the results will be inconsistent.

     To increase a session limit in the Client Access (frontend) services, you need to use the
     Set-ThrottlingPolicy cmdlet in the Exchange Management Shell.

  ２ Warning

  Incorrectly editing the registry can cause serious problems that may require you to
  reinstall your operating system. Problems resulting from editing the registry incorrectly
  may not be able to be resolved. Before editing the registry, back up any valuable data.

  1. Open the Registry Editor. For example, press Windows key + R, and then run regedit.

  2. Go to the following location in the registry:

     \\HKEY_LOCAL_MACHINE
     \SYSTEM\CurrentControlSet\Services\MSExchangeIS\ParametersSystem.

  3. Select the ParametersSystem subkey, click Edit > New, and then select DWORD (32-bit)
     Value.

     The new value is created as New Value #1 in the right pane.

  4. Rename the new key to one of the following values, and then press Enter:

          Maximum Allowed Sessions Per User: This limit specifies the maximum allowable
          sessions per user.

          Maximum Allowed Service Sessions Per User: This limit specifies the maximum
          allowed service sessions per user.

          Maximum Allowed Exchange Sessions Per Service: This limit specifies the maximum
          allowed Exchange sessions per service. The default value is 10,000.

  5. Select the new key, and then click Edit > Modify.

  6. In the dialog that opens, switch the Base value to Decimal and enter the new session limit
     in the Value data field.

     When you're finished, click OK.

<!-- p.165 -->

Open item limits
Open item limits are limits placed on the number of items that can be opened by a single
mailbox in a single session. However, a user can have multiple sessions opened simultaneously.
For example, if a user has two sessions opened, the user could open 1,000 folders.

The open item limits are described in the following table

                                                                               ﾉ     Expand table

 Item type                          Registry object type     Max opened per session

 ACL View                           objtACLView              500

 Attachment                         objtAttachment           500

 Attachment View                    objtAttachmentView       500

 CStream                            objtCStream              Not applicable

 Folder                             objtFolder               500

 Folder View                        objtFolderView           500

 FX Destination Stream              objtFXDstStrm            500

 FX Source Stream                   objtFXSrcStrm            500

 Message                            objtMessage              250

 Message View                       objtMessageView          500

 Notification                       objtNotify               500,000

 Rule View                          objtRulesView            Not applicable

 Stream                             objtStream               250

You can limit the maximum number of resources that a MAPI client (for example, Outlook) can
use simultaneously.

Note: When you modify a session limit, you need to modify that limit on all Mailbox servers
within a database availability group (DAG). If you don't make the same changes on all servers,
the results will be inconsistent.

  ２ Warning

<!-- p.166 -->

  Incorrectly editing the registry can cause serious problems that may require you to
  reinstall your operating system. Problems resulting from editing the registry incorrectly
  may not be able to be resolved. Before editing the registry, back up any valuable data.

   1. Open the Registry Editor. For example, press Windows key + R, and then run regedit.

   2. Go to the following location in the registry:

     \\HKEY_LOCAL_MACHINE
     \SYSTEM\CurrentControlSet\Services\MSExchangeIS\ParametersSystem

   3. Select the ParametersSystem subkey, click Edit > New, and then select Key.

     The new value is created as New Key #1 in the left pane.

   4. Rename the new key to MaxObjsPerMapiSession, and then press Enter.

   5. Select the MaxObjsPerMapiSession subkey, click Edit > New, and then select DWORD
     (32-bit) Value.

     The new key is created as New Value #1 in the right pane.

   6. Rename the key to match one of the Registry object type values in the table. For
     example, to modify the number of messages that can be opened, enter objtMessage and
     then press Enter.

   7. Select the new key, and then click Edit > Modify.

   8. In the dialog that opens, switch the Base value to Decimal and enter the new limit in the
     Value data field. For example, enter 350 to increase the value for objtMessage.

     When you're finished, click OK.

   9. Restart the Microsoft Exchange Information Store service by running the following
     command in Windows PowerShell or the Exchange Management Shell:

        PowerShell

        Restart-Service MSExchangeIS

Item size limits
Item size limits are the limits placed on items within a user's mailbox. You configure these limits
by using the MaxSendSize and MaxReceiveSize parameters on the Set-Mailbox cmdlet in the

<!-- p.167 -->

Exchange Management Shell.

                                                                       ﾉ   Expand table

 Item type               Limit

 Message (saved)         Maximum size of the SendLimit, ReceiveLimit

 Message (sent)          Maximum size of the SendLimit

<!-- p.168 -->

Exchange Server: Edge Transport servers
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Edge Transport servers handle all inbound and outbound Internet mail flow by providing mail
relay and smart host services for your Exchange organization. Agents running on the Edge
Transport server provide additional layers of message protection and security. These agents
provide protection against spam and apply mail flow rules (also known as transport rules) to
control mail flow. All of these features work together to help minimize the exposure of your
internal Exchange to threats on the Internet.

Because the Edge Transport server is installed in the perimeter network, it's never a member of
your organization's internal Active Directory forest and doesn't have access to Active Directory
information. However, the Edge Transport server requires data that resides in Active Directory:
for example, connector information for mail flow and recipient information for antispam
recipient lookup tasks. This data is synchronized to the Edge Transport server by the Microsoft
Exchange EdgeSync service (EdgeSync). EdgeSync is a collection of processes run on an
Exchange 2016 or Exchange 2019 Mailbox server to establish one-way replication of recipient
and configuration information from Active Directory to the Active Directory Lightweight
Directory Services (AD LDS) instance on the Edge Transport server. EdgeSync copies only the
information that's required for the Edge Transport server to perform antispam configuration
tasks and to enable end-to-end mail flow. EdgeSync performs scheduled updates so the
information in AD LDS remains current. For more information about Edge Subscriptions and
EdgeSync, see Edge Subscriptions.

You can install more than one Edge Transport server in the perimeter network. Deploying more
than one Edge Transport server provides redundancy and failover capabilities for your inbound
message flow. You can load balance the SMTP traffic to your organization among Edge
Transport servers by defining more than one MX record with the same priority value for your
mail domain. You can achieve consistency in the configuration among multiple Edge Transport
servers by using cloned configuration scripts.

The Edge Transport server role lets you manage the following message-processing scenarios.

Internet mail flow
Edge Transport servers accept messages coming into the Exchange organization from the
Internet. After the messages are processed by the Edge Transport server, mail is routed to an
internal Exchange Mailbox server; first to the Front End Transport service, and then to the
Transport service.

<!-- p.169 -->

All messages sent to the Internet from inside the organization are routed to Edge Transport
servers after the messages are processed by the Transport service on the Exchange Mailbox
server. You can configure the Edge Transport server to use DNS to resolve MX resource records
for external SMTP domains, or you can configure the Edge Transport server to forward
messages to a smart host for DNS resolution.

Antispam protection
In Exchange Server, antispam features provide services to block unsolicited commercial email
(spam) at the network perimeter.

Spammers use a variety of techniques to send spam into your organization. Edge Transport
servers help prevent users from ever receiving spam by providing a collection of agents that
work together to provide different layers of spam filtering and protection. Establishing
tarpitting intervals on connectors makes email harvesting attempts ineffective.

Mail flow rules on Edge Transport servers
Mail flow rules on Edge Transport servers are used to control the flow of messages sent to or
received from the internet. Mail flow rules are configured on each Edge Transport server to
help protect corporate network resources and data by applying an action to messages meeting
specified conditions. Mail flow rule conditions are based on data, such as specific words or text
patterns in the message subject, body, header, or from address; the spam confidence level
(SCL); or the attachment type. Actions determine how the message is processed when a
specified condition is true. Possible actions include quarantining a message, dropping or
rejecting a message, appending additional recipients, or logging an event. Optional exceptions
exempt particular messages from having an action applied.

Address rewriting
Address rewriting presents a consistent email address appearance to external recipients. You
configure address rewriting on Edge Transport servers to modify the SMTP addresses on
inbound and outbound messages. Address rewriting is especially useful for newly merged
organizations that want to present a consistent email address appearance.

<!-- p.170 -->

Edge Subscriptions in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016   2019       Subscription Edition

Edge Subscriptions are used to populate the Active Directory Lightweight Directory Services
(AD LDS) instance on the Edge Transport server with Active Directory data. Although creating
an Edge Subscription is optional, subscribing an Edge Transport server to the Exchange
organization provides a simpler management experience and enhances antispam features. You
need to create an Edge Subscription if you plan to use recipient lookup or safelist aggregation,
or if you plan to help secure SMTP communications with partner domains by using Mutual
Transport Layer Security (MTLS).

  ７ Note

  The Edge Subscription is mandatory if Edge Transport should handle hybrid mail flow.
  Organization headers are only promoted between Edge Transport and Mailbox servers
  through the Direct Trust Authentication (aka Mutual TLS) and Edge Subscription is
  required to achieve this authentication method.

Edge Subscription process
An Edge Transport server doesn't have direct access to Active Directory. The configuration and
recipient information the Edge Transport server uses to process messages is stored locally in
AD LDS. Creating an Edge Subscription establishes secure, automatic replication of information
from Active Directory to AD LDS. The Edge Subscription process provisions the credentials
used to establish a secure LDAP connection between the internal Exchange Mailbox servers
and a subscribed Edge Transport server. The Microsoft Exchange EdgeSync service (EdgeSync)
that runs on Mailbox servers performs periodic one-way synchronization to transfer up-to-date
data to AD LDS. This reduces the administration tasks you perform in the perimeter network by
letting you configure the Mailbox server and then synchronize that information to the Edge
Transport server.

You subscribe an Edge Transport server to the Active Directory site that contains the Mailbox
servers responsible for transferring messages to and from your Edge Transport servers. The
Edge Subscription process creates an Active Directory site membership affiliation for the Edge
Transport server. The site affiliation enables Mailbox servers in the Exchange organization to
relay messages to the Edge Transport server for delivery to the Internet without having to
configure explicit Send connectors.

<!-- p.171 -->

One or more Edge Transport servers can be subscribed to a single Active Directory site.
However, an Edge Transport server can't be subscribed to more than one Active Directory site.
If you have more than one Edge Transport server deployed, each server can be subscribed to a
different Active Directory site. Each Edge Transport server requires an individual Edge
Subscription.

To deploy an Edge Transport server and subscribe it to an Active Directory site, follow these
steps:

   1. Install the Edge Transport server role.

   2. Prepare for the Edge Subscription:

           License the Edge Transport server.

           Open ports in the firewall for mail flow and EdgeSync synchronization.

           Verify that the Mailbox servers and the Edge Transport server can locate one another
           using DNS name resolution.

           On the Mailbox Server, configure the transport settings to be replicated to the Edge
           Transport server.

   3. On the Edge Transport server, create and export an Edge Subscription file by running the
     New-EdgeSubscription cmdlet.

   4. Copy the Edge Subscription file to a Mailbox server or a file share that's accessible from
     the Active Directory site containing your Mailbox servers.

   5. Import the Edge Subscription file to the Active Directory site by running the New-
     EdgeSubscription cmdlet on the Mailbox server.

Prepare for the Edge Subscription
Before you can subscribe your Edge Transport server to your Exchange organization, you need
to make sure your infrastructure and your Mailbox servers are prepared for the EdgeSync
synchronization. To prepare for EdgeSync, you need to:

     License the Edge Transport server: The licensing information for the Edge Transport
     server is captured when the Edge Subscription is created. Subscribed Edge Transport
     servers need to be subscribed to the Exchange organization after the license key has been
     applied on the Edge Transport server. If the license key is applied on the Edge Transport
     server after you perform the Edge Subscription process, licensing information will not be
     updated in the Exchange organization, and you will need to resubscribe the Edge
     Transport server.

<!-- p.172 -->

   Verify that the required ports are open in the firewall: The following ports are used by
   subscribed Edge Transport servers:

     SMTP: Port 25/TCP must be open for inbound and outbound mail flow between the
     Internet and the Edge Transport server, and between the Edge Transport server and the
     internal Exchange organization.

     Secure LDAP: Non-standard port 50636/TCP is used for directory synchronization from
     Mailbox servers to AD LDS on the Edge Transport server. This port is required for
     successful EdgeSync synchronization.

     ７ Note

     Port 50389/TCP is used locally by LDAP to bind to the AD LDS instance. This port
     doesn't have to be open on the firewall; it's used locally on the Edge Transport
     server.

   If your environment requires specific ports, you can modify the ports used by AD LDS
   using the ConfigureAdam.ps1 script provided with Exchange. Modify the ports before you
   create the Edge Subscription. If you modify the ports after you create the Edge
   Subscription, you need to remove the Edge Subscription and create another one.

   Verify that DNS host name resolution is successful from the Edge Transport server to
   the Mailbox servers and from the Mailbox servers to the Edge Transport server

   Configure the following transport settings for propagation to the Edge Transport
   server

     Internal SMTP servers: Use the InternalSMTPServers parameter on the Set-
     TransportConfig cmdlet to specify a list of internal SMTP server IP addresses or IP
     address ranges to be ignored by the Sender ID and Connection Filtering agents on the
     Edge Transport server.

     Accepted domains: Configure all authoritative domains, internal relay domains, and
     external relay domains.

     Remote domains: Configure the settings for the default remote domain object (used
     for recipients in all remote domains), and configure remote domain objects as required
     for recipients in specific remote domains.

Create and export an Edge Subscription file on the Edge
Transport server

<!-- p.173 -->

When you create an Edge Subscription file by running the New-EdgeSubscription cmdlet on
the Edge Transport server, the following actions occur:

     An AD LDS account called the EdgeSync bootstrap replication account (ESBRA) is created.
     These ESBRA credentials are used to authenticate the first EdgeSync connection to the
     Edge Transport server. This account is configured to expire 24 hours after being created.
     Therefore, you need to complete the five-step subscription process described in the
     previous section within 24 hours. If the ESBRA expires before the Edge Subscription
     process is complete, you will need to run the New-EdgeSubscription cmdlet again to
     create a new Edge Subscription file.

     The ESBRA credentials are retrieved from AD LDS and written to the Edge Subscription
     file. The public key for the Edge Transport server's self-signed certificate is also exported
     to the Edge Subscription file. The credentials written to the Edge Subscription file are
     specific to the server that exported the file.

     Any previously created configuration objects on the Edge Transport server that will now
     be replicated to AD LDS from Active Directory are deleted from AD LDS, and the
     Exchange Management Shell cmdlets used to configure those objects are disabled.
     However, you can still use the Get-* cmdlets to view those objects. Running the New-
     EdgeSubscription cmdlet disables the following cmdlets on the Edge Transport server:

        Set-SendConnector

        New-SendConnector

        Remove-SendConnector

        New-AcceptedDomain

        Set-AcceptedDomain

        Remove-AcceptedDomain

        New-RemoteDomain

        Set-RemoteDomain

        Remove-RemoteDomain

This example creates and exports the Edge Subscription file on the Edge Transport server.

  PowerShell

  New-EdgeSubscription -FileName "C:\Data\EdgeSubscriptionInfo.xml"

<!-- p.174 -->

  ７ Note

  When you run the New-EdgeSubscription cmdlet on the Edge Transport server, you
  receive a prompt to acknowledge the commands that will be disabled and the
  configuration that will be overwritten on the Edge Transport server. To bypass this
  confirmation, you need to use the Force parameter. This parameter is useful when you
  script the New-EdgeSubscription cmdlet. You can also use the Force parameter to
  overwrite an existing file when you resubscribe an Edge Transport server.

Import the Edge Subscription file on a Mailbox server
When you import the Edge Subscription file to the Active Directory site by running the New-
EdgeSubscription cmdlet on a Mailbox server, the following actions occur:

     The Edge Subscription is created, joining the Edge Transport server to the Exchange
     organization. EdgeSync will propagate configuration data to this Edge Transport Server,
     creating an Edge configuration object in Active Directory.

     Each Mailbox server in the Active Directory site receives notification from Active Directory
     that a new Edge Transport server has been subscribed. The Mailbox server retrieves the
     ESBRA from the Edge Subscription file. The Mailbox server then encrypts the ESBRA by
     using the public key of the Edge Transport server's self-signed certificate. The encrypted
     credentials are then written to the Edge configuration object.

     Each Mailbox server also encrypts the ESBRA using its own public key and then stores the
     credentials in its own configuration object.

     EdgeSync replication accounts (ESRAs) are created in Active Directory for each Edge
     Transport-Mailbox server pair. Each Mailbox server stores its ESRA credentials as an
     attribute of the Mailbox server configuration object.

     Send connectors are automatically created to relay messages outbound from the Edge
     Transport server to the Internet, and inbound from the Edge Transport server to the
     Exchange organization. For more information, see the Send connectors created
     automatically by the Edge Subscription section in this topic.

     The Microsoft Exchange EdgeSync service that runs on Mailbox servers uses the ESBRA
     credentials to establish a secure LDAP connection between a Mailbox server and the Edge
     Transport server, and performs the initial replication of data. The following data is
     replicated to AD LDS:

        Topology data

<!-- p.175 -->

        Configuration data

        Recipient data

        ESRA credentials

     The Microsoft Exchange Credential Service that runs on the Edge Transport server installs
     the ESRA credentials. These credentials are used to authenticate and secure later
     synchronization connections.

     The EdgeSync synchronization schedule is established.

     The Microsoft Exchange EdgeSync service running on the Mailbox servers in the
     subscribed Active Directory site then performs one-way replication of data from Active
     Directory to AD LDS on a regular schedule. You can also use the Start-
     EdgeSynchronization cmdlet to override the EdgeSync synchronization schedule and
     immediately start synchronization.

This example subscribes an Edge Transport server to the specified site and automatically
creates the Internet Send connector and the Send connector from the Edge Transport server to
the Mailbox servers.

  PowerShell

  New-EdgeSubscription -FileData
  ([System.IO.File]::ReadAllBytes('C:\Data\EdgeSubscriptionInfo.xml')) -Site
  "Default-First-Site-Name"

  ７ Note

  The default values of the CreateInternetSendConnector and CreateInboundSendConnector
  parameters are both $true , so you don't need to use them in this command.

Send connectors created automatically by the Edge
Subscription
By default, when you import the Edge Subscription file to a Mailbox server, the Send
connectors required to enable end-to-end mail flow between the Internet and the Exchange
organization are created automatically, and any existing Send connectors on the Edge
Transport server are deleted.

The Edge Subscription creates the following Send connectors:

<!-- p.176 -->

     A Send connector named EdgeSync - Inbound to <Site Name> that's configured to relay
     messages from the Edge Transport server to the Exchange organization.

     A Send connector named EdgeSync - <Site Name> to Internet that's configured to relay
     messages from the Exchange organization to the Internet.

Also, subscribing an Edge Transport server to the Exchange organization allows the Mailbox
servers in the subscribed Active Directory site to use the invisible and implicit intra-
organization Send connector to relay messages to the Edge Transport server.

Inbound Send connector to receive messages from the
Internet
When you run the New-EdgeSubscription cmdlet on the Mailbox server, the
CreateInboundSendConnector parameter is set to the value $true . This creates the Send
connector needed to send messages from the Edge Transport server to the Exchange
organization. The following table shows the configuration of this Send connector.

Automatic inbound Send connector configuration

                                                                                           ﾉ   Expand table

 Property                 Value

 Name                     EdgeSync - Inbound to < Site Name>

 AddressSpaces            SMTP:--;1
                          The -- value in the address space represents all authoritative and internal relay
                          accepted domains for the Exchange organization. Any messages the Edge
                          Transport server receives for these accepted domains are routed to this Send
                          connector and relayed to the smart hosts.

 SourceTransportServers   < Edge Subscription name>

 Enabled                  True

 DNSRoutingEnabled        False

 SmartHosts               --
                          The -- value in the list of smart hosts represents all Mailbox servers in the
                          subscribed Active Directory site. Any Mailbox servers you add to the subscribed
                          Active Directory site after you establish the Edge Subscription don't participate
                          in the EdgeSync synchronization process. However, they are automatically added
                          to the list of smart hosts for the automatically created inbound Send connector.
                          If more than one Mailbox server is located in the subscribed Active Directory
                          site, inbound connections will be load balanced across the smart hosts.

<!-- p.177 -->

You can't modify the address space or list of smart hosts at creation time for the automatically
created inbound Send connector. However, you can set the CreateInboundSendConnector
parameter to the value $false when you create an Edge Subscription. This allows you to
manually configure a Send connector from the Edge Transport server to the Exchange
organization.

Outbound Send connector to send messages to the Internet
When you run the New-EdgeSubscription cmdlet on the Mailbox server, the
CreateInternetSendConnector parameter is set to the value $true . This creates the Send
connector needed to send messages from the Exchange organization to the Internet. The
following table shows the default configuration of this Send connector.

Automatic Internet Send connector configuration

                                                                                      ﾉ   Expand table

 Property                 Value

 Name                     EdgeSync - < Site Name> to Internet

 AddressSpaces            SMTP:*;100

 SourceTransportServers   < Edge Subscription name>
                          The name of the Edge Subscription is the same as the name of the subscribed
                          Edge Transport server.

 Enabled                  True

 DNSRoutingEnabled        True

 DomainSecureEnabled      True

If more than one Edge Transport server is subscribed to the same Active Directory site, no
additional Send connectors to the Internet are created. Instead, all Edge Subscriptions are
added to the same Send connector as the source server. This load balances outbound
connections to the Internet across the subscribed Edge Transport servers.

The outbound Send connector is configured to send email messages from the Exchange
organization to all remote SMTP domains, using DNS routing to resolve domain names to MX
resource records.

Details about the EdgeSync service

<!-- p.178 -->

After you subscribe an Edge Transport server to an Active Directory site, EdgeSync will replicate
configuration and recipient data to the Edge Transport servers. The service replicates the
following data from Active Directory to AD LDS:

     Send connector configuration

     Accepted domains

     Remote domains

     Safe Senders Lists

     Blocked Senders Lists

     Recipients

     List of send and receive domains used in domain secure communications with partners

     List of SMTP servers listed as internal in your organization's transport configuration

     List of Mailbox servers in the subscribed Active Directory site

EdgeSync uses a mutually authenticated and authorized secure LDAP channel to transfer data
from the Mailbox server to the Edge Transport server.

To replicate data to AD LDS, the Mailbox server binds to a global catalog server to retrieve
updated data. EdgeSync initiates a secure LDAP session between a Mailbox server and the
subscribed Edge Transport server over the non-standard TCP port 50636.

When you first subscribe an Edge Transport server to an Active Directory site, the initial
replication that populates AD LDS with data from Active Directory can take five minutes or
more, depending on the quantity of data in the directory service. After initial replication,
EdgeSync only synchronizes new and changed objects, and removes any deleted objects.

Synchronization schedule
Different types of data synchronize on different schedules. The EdgeSync synchronization
schedule specifies the maximum interval between EdgeSync synchronizations. EdgeSync
synchronization occurs at the following intervals:

     Configuration data: 3 minutes.

     Recipient data: 5 minutes.

     Topology data: 5 minutes

<!-- p.179 -->

If you want to change these intervals, use the Set-EdgeSyncServiceConfig cmdlet. Using the
Start-EdgeSynchronization cmdlet on the Mailbox server to force Edge Subscription
synchronization overrides the timer for the next scheduled EdgeSync synchronization, and
starts EdgeSync immediately.

Selection of Mailbox servers
Each subscribed Edge Transport server is associated with a particular Active Directory site. If
more than one Mailbox server exists in the site, any of these Mailbox servers can replicate data
to the subscribed Edge Transport servers. To avoid contention among Mailbox servers when
synchronizing, the preferred Mailbox server is selected as follows:

   1. The first Mailbox server in the Active Directory site to perform a topology scan and
     discover the new Edge Subscription performs the initial replication. Because this discovery
     is based on the timing of the topology scan, any Mailbox server in the site may perform
     the initial replication.

   2. The Mailbox server performing the initial replication establishes an EdgeSync lease option
     and sets a lock on the Edge Subscription. The lease option establishes that particular
     Mailbox server as the preferred server providing synchronization services to that Edge
     Transport server. The lock prevents EdgeSync running on another Mailbox server from
     taking over the lease option.

   3. The EdgeSync lease option lasts for one hour. During that hour, no other EdgeSync
     service can take over the option unless a manual synchronization is started before the
     end of the hour. If the preferred Mailbox server isn't available to provide EdgeSync service
     at the time manual synchronization is started, after a five-minute wait, the lock is released
     and another EdgeSync service can take over the lease option and perform
     synchronization.

   4. Unless manual synchronization is started, synchronization occurs based on the EdgeSync
     synchronization schedule. If the preferred server isn't available when a scheduled
     synchronization occurs, after a five-minute wait, the lock is released and another
     EdgeSync service can take over the lease option and perform synchronization.

This method of locking and leasing prevents more than one instance of EdgeSync from
pushing data to the same Edge Transport server at the same time.

Notes:

     In Exchange 2016 organizations, if you also have Exchange 2010 Hub Transport servers in
     the subscribed Active Directory site, Exchange 2016 Mailbox servers will always take
     precedence and perform the replication.

<!-- p.180 -->

     When you subscribe an Edge Transport server to an Active Directory site, all Mailbox
     servers installed in that Active Directory site at that time can participate in the EdgeSync
     synchronization process. If one of those servers is removed, the EdgeSync service that's
     running on the remaining Mailbox servers will continue the data synchronization process.
     However, if you later install new Mailbox servers in the Active Directory site, they won't
     automatically participate in EdgeSync synchronization. Additionally, they won't be
     automatically added to the Edge Server's internal Delivery Group. If you want to enable
     those new Mailbox servers to participate in EdgeSync synchronization and automatic
     Edge to Mailbox mail flow, you will need to subscribe the Edge Transport server again.

The following table lists the EdgeSync properties related to locking and leasing. You can use
the Set-EdgeSyncServiceConfig cmdlet to configure these properties.

EdgeSync lease properties

                                                                                        ﾉ   Expand table

 Parameter             Default      Description
                       value

 LockDuration          00:05:00     This setting determines how long a particular EdgeSync service will
                       (5           acquire a lock. If the EdgeSync service on the Mailbox server that's
                       minutes)     holding this lock doesn't respond, after five minutes the EdgeSync
                                    service on another Mailbox server will take over the lease. Forcing
                                    immediate EdgeSync synchronization doesn't override this setting.

 OptionDuration        01:00:00     This setting determines how long an EdgeSync service can declare a
                       (1 hour)     lease option on an Edge Transport server. If the EdgeSync service
                                    holding the lease is unavailable and doesn't restart during this
                                    option period, no other Exchange EdgeSync service will take over
                                    the lease option unless you force EdgeSync synchronization.

 LockRenewalDuration   00:01:00     This setting determines how frequently the lock field is updated
                       (1 minute)   when an EdgeSync service has acquired a lock to an Edge Transport
                                    server.

<!-- p.181 -->

Procedures for Edge Subscriptions
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

After you've subscribed an Edge Transport server to an Active Directory site in your Exchange
organization as described in Edge Subscriptions, you might need to perform maintenance tasks
on the Edge Subscription. These tasks are described in this topic.

What do you need to know before you begin?
      Estimated time to complete each procedure: 10 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "EdgeSync" entry and the "Edge
      Transport servers" section in the Mail flow permissions topic.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Remove an Edge Subscription
You may occasionally want to remove an Edge Subscription from the Exchange organization or
from both the Exchange organization and the Edge Transport server. If you plan to later
resubscribe the Edge Transport server to the Exchange organization, don't remove the Edge
Subscription from the Edge Transport server. When you remove the Edge Subscription from an
Edge Transport server, all replicated data is deleted from AD LDS. This can take a long time if
you have lots of recipient data.

To completely remove an Edge Subscription, you need to run this procedure on the Edge
Transport server you wish to remove and on an Exchange 2016 or Exchange 2019 Mailbox
server in the Active Directory site where the Edge Transport server is subscribed.

After you remove the Edge Subscription, synchronization of information from AD LDS stops. All
accounts stored in AD LDS are removed, and the Edge Transport server is removed from the
source server list of any Send connector. You will no longer be able to use Edge Transport
server features that rely on Active Directory data.

<!-- p.182 -->

   1. To remove the Edge Subscription from the Edge Transport server, use the following
     syntax.

       PowerShell

       Remove-EdgeSubscription <EdgeTransportServerIdentity>

     For example, to remove the Edge Subscription on the Edge Transport server named
     Edge01, run the following command.

       PowerShell

       Remove-EdgeSubscription Edge01

   2. To remove the Edge Subscription from the Mailbox server, use the following syntax.

       PowerShell

       Remove-EdgeSubscription <EdgeTransportServerIdentity>

     For example, to remove the Edge Subscription for the Edge Transport server named
     Edge01 on a Mailbox server in the subscribed Active Directory site, run the following
     command.

       PowerShell

       Remove-EdgeSubscription Edge01

You will need to remove the Edge Subscription if:

     You no longer want the Edge Transport server to participate in EdgeSync synchronization.
     You will need to remove the Edge Subscription from both the Edge Transport server and
     from the Exchange organization.

     An Edge Transport server is being decommissioned. In this scenario, you only need to
     remove the Edge Subscription from the Exchange organization. If you uninstall the Edge
     Transport server role from the computer, the AD LDS instance and all Active Directory
     data stored in AD LDS will also be removed.

     You want to change the Active Directory site association for the Edge Subscription. You
     will only need to remove the Edge Subscription from the Exchange organization. After the
     Edge Subscription is removed from the Exchange organization, you can resubscribe the
     Edge Transport server to a different Active Directory site.

<!-- p.183 -->

When you remove an Edge Subscription from the Exchange organization:

      Synchronization of information from Active Directory to AD LDS stops.

      The ESRA accounts are removed from both Active Directory and AD LDS.

      The Edge Transport server is removed from the SourceTransportServers property of any
      Send connector.

      The automatic inbound Send connector from the Edge Transport server to the Exchange
      organization is removed from AD LDS.

When you remove the Edge Subscription from an Edge Transport server:

      You can no longer use Edge Transport server features that rely on Active Directory data.

      Replicated data is removed from AD LDS.

      Tasks that were disabled when the Edge Subscription was created are re-enabled to allow
      for local configuration.

Resubscribe an Edge Transport server
Occasionally you may have to resubscribe an Edge Transport server to an Active Directory site.
When the Edge Subscription is re-created, new credentials are generated and you need to
follow the complete Edge Subscription process. You will need to resubscribe an Edge Transport
server if:

      You add new Mailbox servers in the subscribed Active Directory site, and you want the
      new Mailbox server to participate in EdgeSync synchronization.

      You applied the license key for the Edge Transport server after creating the Edge
      Subscription. Licensing information for the Edge Transport server is captured when the
      Edge Subscription is created. Subscribed Edge Transport servers only appear as licensed if
      they are subscribed to the Exchange organization after the license key has already been
      applied on the Edge Transport server. If the license key is applied on the Edge Transport
      server after you perform the Edge Subscription process, the licensing information won't
      be updated in the Exchange organization, and you will need to resubscribe the Edge
      Transport server.

      The ESRA credentials are compromised.

  ） Important

<!-- p.184 -->

   To resubscribe an Edge Transport server, export a new Edge Subscription file on the Edge
   Transport server and then import the XML file on a Mailbox server. You will need to
   resubscribe the Edge Transport server to the same Active Directory site where it was
   originally subscribed. You don't need to first remove the original Edge Subscription; the
   resubscription process will overwrite the existing Edge Subscription.

Add or Remove a Mailbox server
If you add a Mailbox server to an Active Directory site that already has an Edge Transport
server subscribed, the new Mailbox server doesn't automatically participate in EdgeSync
synchronization. To enable a newly deployed Mailbox server to participate in EdgeSync
synchronization, you need to resubscribe each Edge Transport server to the Active Directory
site.

Removing a Mailbox server from an Active Directory site where an Edge Transport server is
subscribed won't affect EdgeSync synchronization unless that Mailbox server is the only
Mailbox server in that site. If you remove all Mailbox servers from the Active Directory site
where an Edge Transport server is subscribed, that site's subscribed Edge Transport servers are
orphaned.

Run EdgeSync manually
You may want to manually run EdgeSync if you've made significant changes to the
configuration or recipients in Active Directory and want your changes synchronized
immediately. You can run a full synchronization, or only synchronize changes made since the
last replication.

A manual EdgeSync resets the EdgeSync synchronization schedule. The next automatic
synchronization is based on when you ran the manual synchronization.

To manually run EdgeSync, use the following syntax.

   PowerShell

   Start-EdgeSynchronization [-Server <MailboxServerIdentity>] [-TargetServer
   <EdgeTransportServerIdentity> [-ForceFullSync]

The following example starts EdgeSync with the following options:

        The synchronization is initiated from the Exchange Mailbox server named Mailbox01.

        All Edge Transport servers are synchronized.

<!-- p.185 -->

     Only the changes since the last replication are synchronized.

  PowerShell

  Start-EdgeSynchronization -Server Mailbox01

This example starts EdgeSync with the following options:

     The synchronization is initiated from the local Mailbox server.

     Only the Edge Transport server named Edge03 is synchronized.

     All recipient and configuration data are fully synchronized.

  PowerShell

  Start-EdgeSynchronization -TargetServer Edge03 -ForceFullSync

Verify EdgeSync results
You can use the Test-EdgeSynchronization cmdlet to verify that the Edge synchronization is
working. This cmdlet reports synchronization status of subscribed Edge Transport servers.

The output of this cmdlet lets you view objects that have not been synchronized to the Edge
Transport server. The task compares data stored in Active Directory against data stored in AD
LDS and reports any data inconsistencies.

You can use the ExcludeRecipientTest parameter on the Test-EdgeSynchronization cmdlet to
exclude validation of recipient data synchronization. If you include this parameter, only the
synchronization of configuration objects is validated. Validating recipient data will take longer
than validating only configuration data.

Verify EdgeSync results for a single recipient
To verify EdgeSync results for a single recipient, use the following syntax on a Mailbox server in
the subscribed Active Directory site.

  PowerShell

  Test-EdgeSynchronization -VerifyRecipient <emailaddress>

This example verifies EdgeSync results for the user kate@contoso.com.

<!-- p.186 -->

PowerShell

Test-EdgeSynchronization -VerifyRecipient kate@contoso.com

<!-- p.187 -->

Configure internet mail flow through Edge
Transport servers without using EdgeSync
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

We recommend that you use the Edge Subscription process to establish mail flow between
your Exchange organization and an Edge Transport server as described in Edge
Subscriptions. However, certain situations may prevent you from subscribing the Edge
Transport server to your Exchange organization. To manually establish mail flow between your
Exchange organization and an unsubscribed Edge Transport server, you need to manually
create and/or modify the following Send connectors and Receive connectors:

On the Edge Transport server:

      Create a dedicated Send connector to only send messages to the internet.

      Create a dedicated Send connector to only send messages to Mailbox servers in the
      Exchange organization.1

      Create a dedicated Receive connector to only receive messages from Mailbox servers in
      the Exchange organization2

      Modify the default Receive connector to only accept messages only from the internet.

On a Mailbox server:

      Create a dedicated Send connector to relay outgoing messages to the Edge Transport
      server

1The Send connector that's created by an EdgeSync subscription for delivering email into the

Exchange organization is configured to use Exchange Server (GSSAPI) authentication. The
EdgeSync subscription identifies the Edge Transport server as an Exchange server to the
internal Active Directory forest, which also allows Exchange Server authentication. By definition,
there is no EdgeSync subscription in this scenario, so you'll need to improvise:

      You can configure Basic authentication over TLS to provide authentication and encryption
      for email traffic between the Edge Transport server and the internal Exchange
      organization. This method has the following issues:

         You need to configure an Active Directory account that belongs to the Exchange
         Servers universal security group for authentication on the Send connector that relays
         messages from the Edge Transport server to the internal Exchange organization. Be
         sure to safeguard the account credentials, and you can configure the account to allow

<!-- p.188 -->

        logon only to specific computers. You also need a local account on the Edge Transport
        server for authentication on the Send connector that relays messages from the internal
        Exchange organization to the Edge Transport server.

        Messages coming from these Send connectors will be seen as authenticated SMTP by
        the destination Mailbox server. This means the default Receive connector named Client
        Frontend <ServerName> in the Front End Transport service will accept the messages
        on port 587, and the messages are accepted in the backend Transport service using the
        default Receive connector named Client Proxy <ServerName> on port 465.

        To provide encryption, you need to use a certificate. The self-signed certificate on the
        Edge Transport server won't be recognized by the internal Exchange Organization
        (again, the EdgeSync subscription usually takes care of this). You'll need to manually
        import the self-signed certificate on each Mailbox or use a certificate from a trusted
        third-party certification authority.

     If you don't want the messages coming from the Edge Transport server to be identified as
     authenticated SMTP and therefore using the corresponding client Receive connectors,
     you can use Externally Secured as the authentication method, which means email traffic
     between the Edge Transport server and the internal Exchange organization isn't
     authenticated or encrypted by Exchange. If you use this method, you must configure and
     use an external encryption method (for example, IPsec or a VPN).

2
Instead of a dedicated Receive connector, you can configure and use the default Receive
connector on the Edge Transport server for both incoming internet messages and incoming
messages from internal Mailbox servers (an EdgeSync subscription uses this Receive connector
for both connections).

For more information about Send connectors, see Send connectors. For more information
about Receive connectors, see Receive connectors.

Before you begin
     Estimated time to complete this task: 30 minutes.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Send connectors" entry, the
     "Send connectors - Edge Transport" entry, and the "Receive connectors - Edge Transport"
     entry in the Mail flow permissions topic.

     On Edge Transport servers, you can only use the Exchange Management Shell to create
     Send connectors and Receive connectors. On Mailbox servers, you can use the Exchange
     admin center (EAC) or the Exchange Management Shell to create Send connectors.

<!-- p.189 -->

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

     For information about opening and using the EAC, see Exchange admin center in
     Exchange Server.

     The basic configuration of an Edge Transport server in the perimeter network must allow
     for resolving public domains for internet email and internal host names for internal email.
     There are different ways to do this, but you can configure the network adapter that's
     connected to the external (public) network segment to use a public DNS server, and
     configure the network adapter that's connected to the internal (private) network segment
     to use a DNS server in the perimeter network.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server .

Edge Transport Server Procedures

Step 1: Create a dedicated Send connector to only send
messages to the internet
This Send connector requires the following configuration:

     Name: To Internet (or any descriptive name)

     Usage type: Internet

     Address spaces: "*" (all domains)

     Network settings: Use DNS MX records to route mail automatically. Depending on your
     network configuration, you can also route mail through a smart host. The smart host then
     routes mail to the internet.

To create a Send connector that's configured to send messages to the internet, run this
command:

  PowerShell

<!-- p.190 -->

  New-SendConnector -Name "To Internet" -AddressSpaces * -Usage Internet -
  DNSRoutingEnabled $true

For detailed syntax and parameter information, see New-SendConnector.

Step 2: Create a dedicated Send connector to only send
messages to the Exchange organization
This Send connector requires the following configuration:

     Name: To Internal Org (or any descriptive name)

     Usage type: Internal

     Address spaces: -- (indicates all accepted domains for the Exchange organization)

     DNS routing disabled (smart host routing enabled)

     Smart hosts: FQDN of one or more Mailbox servers as smart hosts. For example,
     mbxserver01.contoso.com and mbxserver02.contoso.com.

     Smart host authentication methods: Basic authentication over TLS

     Smart host authentication credentials: Credentials for the user account in the internal
     domain that's a member of the Exchange Servers universal security group. You need to
     use the Get-Credential cmdlet to store the credentials. Use the format <Domain>\
     <UserName> or the user principal name (UPN; for example, chris@contoso.com) to enter
     the username.

To create a Send connector configured to send messages to the Exchange organization, replace
the smart host values with the Mailbox servers in your organization, and run this command:

  PowerShell

  New-SendConnector -Name "To Internal Org" -Usage Internal -AddressSpaces "--" -
  DNSRoutingEnabled $false -SmartHosts
  mbxserver01.contoso.com,mbxserver02.contoso.com -SmartHostAuthMechanism
  BasicAuthRequireTLS -AuthenticationCredential (Get-Credential)

For detailed syntax and parameter information, see New-SendConnector.

Step 3: Modify the default Receive connector to only accept
messages from the internet

<!-- p.191 -->

Make the following configuration changes to the default Receive connector:

     Modify the name to indicate that the connector will be used solely to receive email from
     the internet (the default name is Default internal receive connector <ServerName>).

     Change the network bindings to accept messages only from the network adapter that is
     accessible from the internet (for example, 10.1.1.1 and the standard SMTP TCP port value
     of 25).

To modify the default Receive connector to only accept messages from the internet, replace <
ServerName> and bindings ith the name of your Edge Transport server and external network
adapter configuration, and run this command:

  PowerShell

  Set-ReceiveConnector -Identity "Default internal Receive connector ServerName>" -
  Name "From Internet" -Bindings 10.1.1.1:25

For detailed syntax and parameter information, see Set-ReceiveConnector.

Step 4: Create a dedicated Receive connector to only accept
messages from the Exchange organization
This Receive connector requires the following configuration:

     Name: From Internal Org (or any descriptive name)

     Usage type: Internal

     Local network bindings: Internal network-facing network adapter (for example, 10.1.1.2
     and the standard SMTP TCP port value of 25).

     Remote network settings: IP address of one or more Mailbox servers in the Exchange
     organization. For example, 192.168.5.10 and 192.168.5.20.

     Authentication methods: TLS, Basic authentication, Basic authentication over TLS, and
     Exchange Server authentication.

To create a Receive connector configured to only accept messages from the Exchange
organization, replace the bindings and remote IP ranges with your values, and run this
command.

  PowerShell

<!-- p.192 -->

  New-ReceiveConnector -Name "From Internal Org" -Usage Internal -AuthMechanism
  TLS,BasicAuth,BasicAuthRequireTLS,ExchangeServer -Bindings 10.1.1.2:25 -
  RemoteIPRanges 192.168.5.10,192.168.5.20

For detailed syntax and parameter information, see New-ReceiveConnector.

How do you know this worked?
To verify that you have successfully configured the required Send connectors and Receive
connectors on the Edge Transport server, run this command on the Edge Transport server and
verify the property values:

  PowerShell

  Get-SendConnector | Format-List
  Name,Usage,AddressSpaces,SourceTransportServers,DSNRoutingEnabled,SmartHosts,Smart
  HostAuthMechanism; Get-ReceiveConnector | Format-List
  Name,Usage,AuthMechanism,Bindings,RemoteIPRanges

Mailbox server procedures
You don't need to modify the default Receive connectors on Mailbox servers. For more
information about default Receive connectors on Mailbox servers, see Default Receive
connectors created during setup.

Step 5: Create a dedicated Send connector to send outgoing
messages to the Edge Transport server
This Send connector requires the following configuration:

     Name: To Edge (or any descriptive name)

     Usage type: Internal

     Address spaces: "*" (all external domains)

     DNS routing disabled (smart host routing enabled)

     Smart hosts: IP address or FQDN of the Edge Transport server. For example,
     edge01.contoso.net.

     Source servers: FQDN of one or more Mailbox servers. For example,
     mbxserver01.contoso.com and mbxserver02.contoso.com.

<!-- p.193 -->

    Smart host authentication methods: Basic authentication over TLS.

    Smart host authentication credentials: Credentials for the user account on the Edge
    Transport server.

Use the EAC to create a Send connector to send outgoing messages to
the Edge Transport server

  1. In the EAC, go to Mail flow > Send connectors, and then click Add     . This starts the
    New Send connector wizard.

  2. On the first page, configure these settings:

          Name: Enter To Edge.

          Type: Select Internal.

    Click Next.

  3. On the next page, select Route mail through smart hosts, and then click Add      . In the
    Add smart host dialog box that appears, identify the Edge Transport server by using one
    of these values:

          IP address: For example, 10.1.1.2.

          Fully qualified domain name (FQDN): For example, edge01.contoso.net. Note that
          the source Mailbox servers for the Send connector must be able to resolve the Edge
          Transport server in DNS by using this FQDN. If they can't, use the IP address instead.

    Click Save.

  4. On the next page, in the Smart host authentication section, select Basic authentication,
    and then configure these additional settings:

          Select Offer basic authentication only after starting TLS

          In the User name and Password fields, enter the credentials for the local user
          account on the Edge Transport server.

    Click Next.

  5. On the next page, in the Address space section, click Add    . In the Add domain dialog
    box that appears, enter the following information:

          Type: Verify SMTP is selected.

<!-- p.194 -->

           Fully Qualified Domain Name (FQDN): Enter an asterisk (*) to indicate the Send
           connector is used for all external domains.

           Cost: Verify 1 is entered. A lower value indicates a more preferred route.

     Click Save.

   6. Back on the previous page, the Scoped send connector setting is important if your
     organization has Exchange servers installed in multiple Active Directory sites:

           If you don't select Scoped send connector, the connector is usable by all transport
           servers (Exchange 2019 Mailbox servers, Exchange 2016 Mailbox servers, Exchange
           2013 Mailbox servers, and Exchange 2010 Hub Transport servers) in the entire Active
           Directory forest. This is the default value.

           If you select Scoped send connector, the connector is only usable by other
           transport servers in the same Active Directory site.

     Click Next.

   7. On the next page, in the Source server section, click Add    . In the Select a Server dialog
     box that appears, select one or more Mailbox servers that you want to use to send
     outgoing mail through the Edge Transport server. Select a Mailbox server and click Add -
     > (repeat as many times a necessary), click OK, and then click Finish.

Use the Exchange Management Shell to create a Send connector to send
outgoing messages to the Edge Transport server
To create a Send connector to send outgoing messages to the Edge Transport server, replace
the smart hosts and source Mailbox servers with your values, and run this command:

  PowerShell

  New-SendConnector -Name "To Edge" -Usage Internal -AddressSpaces * -
  DNSRoutingEnabled $false -SmartHosts edge01.contoso.com -SourceTransportServers
  mbxserver01.contoso.com,mbxserver02.contoso.com -SmartHostAuthMechanism
  BasicAuthRequireTLS -AuthenticationCredential (Get-Credential)

For detailed syntax and parameter information, see New-SendConnector.

How do you know this worked?
To verify that you've successfully created a Send connector to send outgoing messages to the
Edge Transport server, use either of these steps:

<!-- p.195 -->

In the EAC, go to Mail flow > Send connectors, select the Send connector named To
Edge > click Edit   , and verify the property values.

In the Exchange Management Shell, run this command on a Mailbox server to verify the
property values:

  PowerShell

  Get-SendConnector -Identity "To Edge" | Format-List
  Usage,AddressSpaces,DSNRoutingEnabled,SmartHosts,SourceTransportServers,Smart
  HostAuthMechanism

<!-- p.196 -->

Exchange Server: Address rewriting on
Edge Transport servers
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Address rewriting in Exchange Server modifies the email addresses of senders and recipients in
messages that enter or leave your organization through an Edge Transport server. Two
transport agents on the Edge Transport server provide the rewriting functionality: the Address
Rewriting Inbound Agent and the Address Rewriting Outbound Agent. The primary reason for
address rewriting on outbound messages is to present a single, consistent email domain to
external recipients. The primary reason for address rewriting on inbound messages is to deliver
messages to the correct recipient.

The address rewrite entry, which you create, specifies the internal addresses (the email
addresses you want to change) and the external addresses (the final email addresses you want).
You can specify whether email addresses are rewritten in inbound and outbound messages, or
in outbound messages only. You can create address writing entries for a single user
(chris@contoso.com to support@contoso.com), a single domain (contoso.com to
fabrikam.com), or for multiple subdomains with exceptions (*.fabrikam.com to contoso.com,
except legal.fabrikam.com).

  ） Important

  Regardless of how you plan to use address rewriting, you need to verify that the resulting
  email addresses are unique in your organization so you don't end up with duplicates.
  Address rewriting doesn't verify the uniqueness of a rewritten email address.

  ） Important

  DKIM signing is not supported for outbound email messages using rewritten addresses as
  it happens before the address rewriting process. If your organization requires DKIM
  signing for outbound email, be aware that DKIM validation will fail after implementing
  address rewriting.

To configure address rewriting, see Address rewriting procedures on Edge Transport servers.

Scenarios for address rewriting

<!-- p.197 -->

The following scenarios are examples of how you can use address rewriting:

     Group consolidation: Some organizations segment their internal businesses into separate
     domains that are based on business or technical requirements. This configuration can
     cause email messages to appear as if they come from separate groups or even separate
     organizations.

     The following example shows how an organization, Contoso, Ltd., can hide its internal
     subdomains from external recipients:

        Outbound messages from the northamerica.contoso.com, europe.contoso.com, and
        asia.contoso.com domains are rewritten so they appear to originate from a single
        contoso.com domain. All messages are rewritten as they pass through Edge Transport
        servers that provide SMTP connectivity between the whole organization and the
        Internet.

        Inbound messages to contoso.com recipients are relayed by the Edge Transport server
        to a Mailbox server. The message is delivered to the correct recipient based on the
        proxy address that's configured on the recipient's mailbox.

     Mergers and acquisitions: An acquired company might continue to run as a separate
     business, but you can use address rewriting to make the two organizations appear as if
     they're one integrated organization.

     The following example shows how Contoso, Ltd. can hide the email domain of the newly
     acquired company, Fourth Coffee:

        Contoso, Ltd. wants all outbound messages from Fourth Coffee's Exchange
        organization to appear as if they originate from contoso.com. All messages from both
        organizations are sent through the Edge Transport servers at Contoso, Ltd., where
        email messages are rewritten from user@fourthcoffee.com to user@contoso.com.

        Inbound messages to user@contoso.com are rewritten and routed to
        user@fourthcoffee.com mailboxes. Inbound messages that are sent to
        user@fourthcoffee.com are routed directly to Fourth Coffee's email servers.

     Partners: Many organizations use external partners to provide services for their
     customers, other organizations, or their own organization. To avoid confusion, the
     organization might replace the email domain of the partner organization with its own
     email domain.

     The following example shows how Contoso, Ltd. can hide a partner's email domain:

        Contoso, Ltd. provides support for the larger Wingtip Toys organization. Wingtip Toys
        wants a unified email experience for its customers, and it requires all messages from

<!-- p.198 -->

        support personnel at Contoso, Ltd. to appear as if they were sent from Wingtip Toys.
        All outbound messages that relate to Wingtip Toys are sent through their Edge
        Transport servers, and all contoso.com email addresses are rewritten to
        wingtiptoys.com email addresses.

        Inbound messages for support@wingtiptoys.com are accepted by Wingtip Toy's Edge
        Transport servers, rewritten, and then routed to the support@contoso.com email
        address.

Message properties modified by address rewriting
A standard SMTP email message consists of a message envelope and message content. The
message envelope contains information that's required for transmitting and delivering the
message between SMTP messaging servers. The message content contains message header
fields (collectively called the message header) and the message body. The message envelope is
described in RFC 2821, and the message header is described in RFC 2822.

When a sender composes an email message and submits it for delivery, the message contains
the basic information that's required to comply with SMTP standards, such as a sender, a
recipient, the date and time that the message was composed, an optional subject line, and an
optional message body. This information is contained in the message itself and, by definition,
in the message header.

The sender's mail server generates a message envelope for the message by using the sender's
and recipient's information found in the message header. It then transmits the message to the
Internet for delivery to the recipient's messaging server. Recipients never see the message
envelope because it's generated by the message transmission process, and it isn't actually part
of the message.

Address rewriting changes an email address by rewriting specific fields in the message header
or message envelope. Address rewriting changes several fields in outbound messages, but only
one field in inbound email messages. The following table shows which SMTP header fields are
rewritten in outbound and inbound messages.

Message fields rewritten on outbound and inbound messages

                                                                               ﾉ   Expand table

 Field name                    Location            Outbound messages       Inbound messages

 MAIL FROM                     Message envelope    Rewritten               Not rewritten

 RCPT TO                       Message envelope    Not rewritten           Rewritten

<!-- p.199 -->

 Field name                    Location              Outbound messages      Inbound messages

 To                            Message header        Not Rewritten          Rewritten

 Cc                            Message header        Rewritten              Rewritten

 From                          Message header        Rewritten              Not rewritten

 Sender                        Message header        Rewritten              Not rewritten

 Reply-To                      Message header        Rewritten              Not rewritten

 Return-Receipt-To             Message header        Rewritten              Not rewritten

 Disposition-Notification-To   Message header        Rewritten              Not rewritten

 Resent-From                   Message header        Rewritten              Not rewritten

 Resent-Sender                 Message header        Rewritten              Not rewritten

What address rewriting doesn't change
Address rewriting doesn't modify any message header fields that would break SMTP
functionality. For example, modifying certain header fields can affect routing loop detection,
invalidate the digital signature, or make a rights-protected message unreadable. Therefore, the
following header fields aren't modified by address rewriting.

      Return-Path

      Received

      Message-ID

      X-MS-TNEF-Correlator

      Content-Type Boundary=string

      Header fields located inside MIME body parts

Address rewriting ignores domains that aren't controlled by the Exchange organization. In
other words, the domain needs to be configured as an authoritative accepted domain in the
Exchange organization. Rewriting non-authoritative domains would cause an uncontrollable
form of message relay.

Address rewriting also doesn't modify the header fields of messages that are embedded in
another message. Senders and recipients expect embedded messages to remain intact and be

<!-- p.200 -->

delivered without modification, as long as the messages don't trigger mail flow rules (also
known as transport rules) that are implemented between the sender and recipient.

Considerations for outbound-only address
rewriting
Outbound-only address rewriting on an Edge Transport server modifies the sender's email
address as messages leave the Exchange organization. You can configure outbound-only
address rewriting for a single user (chris@contoso.com to support@contoso.com), or for a
single domain (contoso.com to fabrikam.com). You are required to configure outbound-only
address rewriting for multiple subdomains (*.fabrikam.com to contoso.com).

The rewritten email address needs to be configured as a proxy address on the affected
recipients. For example, if laura@sales.contoso.com is rewritten to laura@contoso.com, the
proxy address laura@contoso.com needs to be configured on Laura's mailbox. This allows
replies and inbound messages to be delivered correctly.

Considerations for inbound and outbound address
rewriting
Inbound and outbound, or bidirectional address rewriting on an Edge Transport server modifies
the sender's email address as messages leave the Exchange organization, and the recipient's
email address as messages enter the Exchange organization.

You can configure bidirectional address rewriting for a single user (chris@contoso.com to
support@contoso.com), and a single domain (contoso.com to fabrikam.com). You can't
configure bidirectional address rewriting for multiple subdomains (*.fabrikam.com to
contoso.com).

Considerations for rewriting email addresses in
multiple domains
When you flatten multiple internal domains or subdomains into a single external domain, you
need to consider the following factors:

     Verify unique aliases: All email aliases (the part to the left of the @ sign) need to be
     unique across all subdomains. For example, if there is a joe@sales.contoso.com, there
     can't be a joe@marketing.contoso.com because the rewritten email address for both
     users would be joe@contoso.com.
