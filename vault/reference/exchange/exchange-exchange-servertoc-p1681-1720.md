---
title: "Exchange Server — pages 1681-1720"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1681-1720
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1681-1720
family: exchange
documentKind: "doc"
abstract: "security flaws may affect the stability and security of Exchange. Therefore, you should only install transport agents that you fully trust and that have been fully tested in a test environment. Transport agents are installed in a disabled state to make sure mail flow isn't affec"
---

# Exchange Server — pages 1681-1720

<!-- p.1681 -->

security flaws may affect the stability and security of Exchange. Therefore, you should only
install transport agents that you fully trust and that have been fully tested in a test
environment.

Transport agents are installed in a disabled state to make sure mail flow isn't affected by
transport agents that haven't been configured. Therefore, after a transport agent has been
configured correctly, you need to enable the transport agent.

Use the following syntax to install a transport agent.

  PowerShell

  Install-TransportAgent -Name <TransportAgentIdentity> -TransportAgentFactory
  <"TransportAgentFactory"> -AssemblyPath <"FilePath">

This example installs a fictitious transport agent named Contoso Transport Agent in the
Transport service.

  PowerShell

  Install-TransportAgent -Name "Contoso Transport Agent" -TransportAgentFactory
  "vendor.exchange.ContosoTransportAgentfactory" -AssemblyPath "C:\Program
  Files\Vendor\TransportAgent\ContosoTransportAgentFactory.dll"

How do you know this worked?

To verify that you have successfully installed the transport agent, run the command Get-
TransportAgent and confirm the transport agent is listed.

Use the Exchange Management Shell to enable a
transport agent
Use the following syntax to enable a transport agent.

  PowerShell

  Enable-TransportAgent <TransportAgentIdentity>

This example enables the transport agent named Contoso Transport Agent in the Transport
service.

  PowerShell

<!-- p.1682 -->

  Enable-TransportAgent "Contoso Transport Agent"

How do you know this worked?

To verify that you have successfully enabled a transport agent, run the command Get-
TransportAgent | Format-List Name,Enabled and confirm the transport agent is enabled.

Use the Exchange Management Shell to disable a
transport agent
Use the following syntax to disable a transport agent:

  PowerShell

  Disable-TransportAgent <TransportAgentIdentity>

This example disables the transport agent named Fabrikam Transport Agent in the Transport
service.

  PowerShell

  Disable-TransportAgent "Fabrikam Transport Agent"

How do you know this worked?

To verify that you have successfully disabled a transport agent, run the command Get-
TransportAgent | Format-List Name,Enabled and confirm the transport agent is disabled.

Use the Exchange Management Shell to view
transport agents
To view a summary list of transport agents, run the following command:

  PowerShell

  Get-TransportAgent

To view the detailed configuration of a specific transport agent, run the following command:

  PowerShell

<!-- p.1683 -->

  Get-TransportAgent <TransportAgentIdentity> | Format-List

This example provides a detailed configuration of the transport agent named Transport Rule
Agent.

  PowerShell

  Get-TransportAgent "Transport Rule Agent" | Format-List

Use the Exchange Management Shell to configure
the priority of a transport agent
Transport agents with a priority closest to 0 process email messages first. However, the SMTP
event in the transport pipeline where the transport agent is registered may cause a lower
priority agent to act on the message before a higher priority agent.

To modify the priority of an existing transport agent, run the following command:

  PowerShell

  Set-TransportAgent <TransportAgentIdentity> -Priority <Integer>

This example sets the priority agent value of 3 for the existing transport agent named Contoso
Transport Agent in the Transport service.

  PowerShell

  Set-TransportAgent "Contoso Transport Agent" -Priority 3

How do you know this worked?

To verify that you have successfully configured the priority of a transport agent, run the
command Get-TransportAgent | Format-List Name,Priority and confirm the priority value of
the transport agent.

Use the Exchange Management Shell to uninstall a
transport agent
When the transport agent is uninstalled, Exchange unregisters the DLL files used with the
agent. Exchange doesn't remove any files, registry keys, or other objects added by the

<!-- p.1684 -->

installation of the transport agent.

To uninstall a transport agent, run the following command:

  PowerShell

  Uninstall-TransportAgent <TransportAgentIdentity>

This example uninstalls the transport agent named Fabrikam Transport Agent from the
Transport service.

  PowerShell

  Uninstall-TransportAgent "Fabrikam Transport Agent"

How do you know this worked?

To verify that you have successfully uninstalled the transport agent, run the command Get-
TransportAgent and verify the transport agent isn't listed.

<!-- p.1685 -->

View transport agents in the transport
pipeline in Exchange Server
07/23/2025

APPLIES TO:      2016     2019      Subscription Edition

You can use the Exchange Management Shell to view a list of transport agents in the transport
pipeline on Microsoft Exchange Server 2016 or 2019. Specifically, the Get-TransportPipeline
cmdlet shows information about the following types of transport agents in the transport
pipeline:

     Agents based on the SmtpReceiveAgent, RoutingAgent, DeliveryAgent, and
     StorageAgent classes in the Transport service.

     Agents based on the SmtpReceiveAgentClass in the Front End Transport service.

You can view a list of all the enabled transport agents that have encountered messages in the
transport pipeline and the SMTP events they are registered on. For more information about
transport agents, see Transport agents in Exchange Server.

What do you need to know before you begin?
     Estimated time to complete: 5 minutes

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Transport agents" entry in the
     Mail flow permissions topic.

     You can only use the Exchange Management Shell to perform this procedure.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to view a list
of transport agents in the transport pipeline

<!-- p.1686 -->

To use the Shell to view a list of transport agents in the transport pipeline on an Exchange
server, run the following command:

  PowerShell

  Get-TransportPipeline | Format-List

To export the results to a text file named C:\My Documents\Transport Agents.txt, run the
following command:

  PowerShell

  Get-TransportPipeline | Format-List > "C:\My Documents\Transport Agents.txt"

How do you know this worked?
Only transport agents that have encountered messages in the transport pipeline between the
time when the transport service was started and the time when the Get-TransportPipeline
cmdlet was run are displayed by the cmdlet. A transport agent that hasn't encountered a
message in the transport pipeline won't appear in the results shown by the Get-
TransportPipeline cmdlet, even if that transport agent is enabled.

<!-- p.1687 -->

Transport high availability in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019        Subscription Edition

In Exchange Server, transport high availability is responsible for keeping redundant copies of
messages before and after the messages are successfully delivered. These features were
introduced in Exchange 2013. They serve as improvements to the transport high availability
features in Exchange 2010. For example, shadow redundancy and the transport dumpster help
ensure messages aren't lost in transit.

Key features that improve transport high availability in Exchange 2013, Exchange 2016, and
Exchange 2019 over Exchange 2010 includes:

      Shadow redundancy creates a redundant copy of the message on another server before
      the message is accepted or acknowledged. The sending server's support or lack of
      support for shadow redundancy is irrelevant.

      Shadow redundancy recognizes both database availability groups (DAGs) and Active
      Directory sites as transport high availability boundaries. This reduces the number of
      servers that can hold redundant copies of messages, and eliminates unnecessary
      redundant message maintenance traffic across DAGs or Active Directory sites.

      For more information, see Shadow redundancy in Exchange Server.

      The transport dumpster is improved and is now named Safety Net. Safety Net stores
      messages successfully processed by the Transport service on Mailbox servers. Safety Net
      works best for Mailbox servers in a DAG, but Safety Net also works for multiple Mailbox
      servers in the same Active Directory site that don't belong to a DAG.

      Safety Net itself is now made redundant on another server. This is important to avoid a
      single point of failure, because the Transport service and the mailbox databases are both
      located on the Mailbox server.

      For more information, see Safety Net in Exchange Server.

This diagram provides a high-level overview of how transport high availability works in
Exchange Server.

<!-- p.1688 -->

1. An Exchange Mailbox server named Mailbox01 receives a message from an SMTP server
  that's outside the transport high availability boundary. The transport high availability
  boundary is a DAG or an Active Directory site in non-DAG environments. The message
  could come from:

       An internal third-party messaging server.

       An Internet messaging server proxied through the Front End Transport service on a
       Mailbox server.

       Another Exchange server in your organization.

2. Before acknowledging receipt of the message, Mailbox01 initiates a new SMTP session to
  another Exchange Mailbox server named Mailbox03 that's within the Transport high
  availability boundary, and Mailbox03 makes a shadow copy of the message. In DAG
  environments, a shadow server in a remote Active Directory site is preferred. Mailbox01 is
  the primary server holding the primary message, and Mailbox03 is the shadow server
  holding the shadow message.

3. The Transport service on Mailbox01 processes the primary message.

  a. In this example, the recipient's mailbox is located on Mailbox01, so the Transport
  service transmits the message to the local Mailbox Transport service.

  b. The Mailbox Transport service delivers the message to the local mailbox database.

  c. Mailbox01 queues a discard status for Mailbox03 that indicates the primary message
  was successfully processed, and Mailbox01 moves a copy of the primary message into the

<!-- p.1689 -->

     local Primary Safety Net. The message moves between queues within the same queue
     database.

   4. Mailbox03 periodically polls Mailbox01 for the discard status of the primary message.

   5. When Mailbox03 determines Mailbox01 successfully processed the primary message,
     Mailbox03 moves the shadow message into the local Shadow Safety Net. The message
     moves between queues within the same queue database.

The message is retained in Primary Safety Net and Shadow Safety Net until the message
expires based on a configurable timeout value. If a mailbox database failover occurs before the
message expires, the Primary Safety Net on Mailbox01 resubmits the message. If the
Mailbox01 isn't available, the Shadow Safety Net on Mailbox03 takes over and resubmits the
message.

Message redundancy in the Front End Transport
service on Mailbox servers
The Front End Transport service on a Mailbox server (part of the Client Access services) has no
message queues. It's a stateless proxy that accepts incoming SMTP connections, and proxies
them to the Transport service on a Mailbox server. The Front End Transport service keeps the
SMTP session with the sending server open while:

     The primary message is transmitted to the Transport service on a Mailbox server.

     and

     A shadow copy of the message is made by the Transport service on a different Mailbox
     server within the transport high availability boundary (DAG or Active Directory site).

Only after both the primary message and shadow message are successfully created, the end of
data SMTP command is sent back to the sending SMTP server through the Front End Transport
service.

<!-- p.1690 -->

Shadow redundancy in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016         2019        Subscription Edition

Shadow redundancy was introduced in Exchange 2010 to provide redundant copies of
messages before they're delivered to mailboxes. In Exchange 2010, shadow redundancy
delayed deleting a message from the queue database on a Hub Transport server until the
server verified that the next hop in the message delivery path had completed delivery. If the
next hop failed before reporting successful delivery back to the Hub Transport server, the
server resubmitted the message to that next hop. Exchange 2010 Hub Transport servers used
the XSHADOW verb to advertise their shadow redundancy support. If a source messaging
server didn't support shadow redundancy, Exchange 2010 used delayed acknowledgment
based on a configured time interval on the Receive connector to make a redundant copy of the
message.

Exchange 2016 and Exchange 2019 have the same improvements that were made to shadow
redundancy in Exchange 2013: the Transport service on a Mailbox server now makes a
redundant copy of any message it receives before acknowledging the receipt of the message
to the sending server. Maintaining redundant copies of messages in transit is more than a best
effort that may or may not work, because now shadow redundancy doesn't depend the
sending server's supported features (support or lack of support for shadow redundancy
doesn't matter). This helps to ensure that all messages in the transport pipeline are made
redundant while they're in transit. If Exchange determines the original message was lost in
transit, the redundant copy of the message is redelivered.

For more information about transport high availability features in Exchange Server, see
Transport high availability in Exchange Server. For more information about message
redundancy after a message has been successfully delivered, see Safety Net in Exchange Server.

Shadow redundancy components
This table describes the components of shadow redundancy in the Transport service on
Mailbox servers. These terms are used throughout the topic.

                                                                                          ﾉ   Expand table

 Term                  Description

 Transport high        A database availability group (DAG) in DAG environments, or an Active Directory site
 availability          in non-DAG environments. For DAGs that span multiple Active Directory sites, the
 boundary              DAG itself is still the boundary (not the site).

<!-- p.1691 -->

 Term              Description

                   When a message arrives on a Mailbox server in the transport high availability
                   boundary, Exchange tries to maintain two redundant copies of the message on
                   Mailbox servers within the boundary. When a message leaves the transport high
                   availability boundary, Exchange stops maintaining redundant copies of the message.

 Primary message   The message submitted into the transport pipeline for delivery.

 Shadow message    The redundant copy of the message that the shadow server retains until it confirms
                   the primary message was successfully processed by the primary server.

 Primary server    The Mailbox server that's currently processing the primary message.

 Shadow server     The Mailbox server that holds the shadow message for the primary server. A Mailbox
                   server may be the primary server for some messages and the shadow server for other
                   messages simultaneously.

 Shadow queue      The delivery queue where the shadow server stores shadow messages. For messages
                   with multiple recipients, each next hop for the primary message requires separate
                   shadow queues.

 Discard status    The information that the Mailbox server maintains for shadow messages to indicate
                   the primary message has been successfully processed.

 Discard           The response a shadow server receives from a primary server indicating a shadow
 notification      message is ready to be discarded.

 Safety Net        The improved version of the transport dumpster in Exchange 2013 or later. Messages
                   that are successfully processed or delivered to a mailbox recipient by the Transport
                   service on a Mailbox server are moved into Safety Net. For more information, see
                   Safety Net in Exchange Server.

 Shadow            The transport component that manages shadow redundancy.
 Redundancy
 Manager

 Heartbeat         The process that allows primary servers and shadow servers to verify the availability
                   of each other.

Requirements for shadow redundancy
Although it may seem obvious, shadow redundancy requires multiple Mailbox servers:

     If the Mailbox server isn't a member of a DAG, the other Mailbox servers must be in the
     local Active Directory site.

     If the Mailbox server is a member of a DAG, the other Mailbox servers must belong to the
     same DAG. The other DAG members can be in the local Active Directory site, or in a

<!-- p.1692 -->

     remote site. By default, if the DAG spans multiple Active Directory sites, shadow
     redundancy prefers creating a redundant copy of the message in a remote site for site
     resiliency.

These are the situations where shadow redundancy can't protect messages in transit:

     In single Exchange server environments.

     In under-provisioned DAGs.

     During the simultaneous failure of two or more Mailbox servers involved in the shadow
     redundancy of a message.

Shadow redundancy is enabled by default
By default, shadow redundancy is enabled globally in the Transport service on all Mailbox
servers. This table describes the parameters that enable shadow redundancy.

                                                                                    ﾉ   Expand table

 Parameter                      Default   Description
                                value

 ShadowRedundancyEnabled on      $true    $true : Shadow redundancy is enabled on all Mailbox
 Set-TransportConfig                      servers in the organization.

                                          $false : Shadow redundancy is disabled on all Mailbox
                                          servers in the organization.

 RejectMessageOnShadowFailure    $false   $false : When a shadow copy of the message can't be
 on Set-TransportConfig                   created, the primary message is accepted anyway by
                                          Mailbox servers in the organization. These messages aren't
                                          redundantly persisted while they're in transit.

                                          $true : No message is accepted or acknowledged by any
                                          Mailbox server in the organization until a shadow copy of
                                          the message is successfully created. If a shadow copy of
                                          the message can't be created, the primary message is
                                          rejected with a transient error, but the sending server can
                                          transmit the message again. The SMTP response code is
                                           451 4.4.0 Message failed to be made redundant . All
                                          messages in the organization are redundantly persisted
                                          while they're in transit.

                                          Note: Use $true only if you have multiple Mailbox servers
                                          in the same DAG or Active Directory site so a shadow copy
                                          of the message can be created.

<!-- p.1693 -->

 Parameter                        Default   Description
                                  value

                                            This parameter is only meaningful when
                                            ShadowRedundancyEnabled is $true .

How shadow messages are created
The main goal of shadow redundancy is to always have two copies of a message within a
transport high availability boundary while the message is in transit. Where and when the
redundant copy of the message is created depends on where the message came from, and
where the message is going. There are three determining factors for creating shadow
messages:

     Messages received from outside a transport high availability boundary (the DAG, or an
     Active Directory site in non-DAG environments).

     Messages sent outside a transport high availability boundary.

     Messages received from the Mailbox Transport Submission service from a Mailbox server
     within the transport high availability boundary.

Shadow redundancy never tracks shadow messages across a transport high availability
boundary. When a message crosses the transport high availability boundary, shadow
redundancy begins or restarts. This reduces shadow message maintenance traffic and prevents
shadow message resubmissions across the transport high availability boundary. Exchange 2010
Hub Transport servers are a special case, and are discussed later in this topic.

Messages received from outside a transport high availability
boundary
When the Transport service on a Mailbox server receives a message from outside the transport
high availability boundary, the Mailbox server isn't concerned about the support or lack of
support for shadow redundancy by the sending server. As long as shadow redundancy is
enabled, the Mailbox server that receives the message makes a redundant copy of the message
on another Mailbox server within the transport high availability boundary before
acknowledging receipt of the message back to the sending server. Here's an example of how
the process works:

<!-- p.1694 -->

1. A messaging server transmits a message to the Transport service on a Mailbox server. The
  Mailbox server is the primary server, and the message is the primary message.

2. While the original SMTP session with the messaging server is still active, the Transport
  service on primary server opens a new, simultaneous SMTP session with the Transport
  service on a different Mailbox server in the organization to create a redundant copy of
  the message.

        If the primary server is a member of a DAG, the primary server connects to a
        different Mailbox server in the same DAG. If the DAG spans multiple Active Directory
        sites, a Mailbox server in a different Active Directory site is preferred by default (the
        default value of the ShadowMessagePreferenceSetting parameter on the Set-
        TransportConfig cmdlet is PreferRemote , but you can change it to RemoteOnly or
        LocalOnly ).

        If the primary server isn't a member of a DAG, the primary server connects to a
        different Mailbox server in the same Active Directory site (regardless of the value of
        the ShadowMessagePreferenceSetting parameter).

3. The primary server transmits a copy of the message to the Transport service on another
  Mailbox server, and Transport service on the other Mailbox server acknowledges that the
  copy of the message was created successfully. The copy of the message is the shadow
  message, and the Mailbox server that holds it is the shadow server for the primary server.
  The message exists in a shadow queue on the shadow server.

4. After the primary server receives acknowledgment from the shadow server, the primary
  server acknowledges the receipt of the primary message to the original messaging server

<!-- p.1695 -->

     in the original SMTP session, and the SMTP session is closed.

Messages sent outside a transport high availability boundary
When a Mailbox server transmits a message outside the transport high availability boundary,
and the messaging server on the other side acknowledges successful receipt of the message,
and the Mailbox server moves the message into Safety Net. No resubmission of the message
from Safety Net can occur after the primary message has been successfully transmitted across
the transport high availability boundary. For more information about Safety Net, see Safety Net
in Exchange Server.

Messages transmitted within a transport high availability
boundary
Message routing is optimized so that when the ultimate destination is in a DAG or Active
Directory site, multiple hops between servers within the destination DAG or site aren't typically
required. After the message is accepted by the Transport service on a Mailbox server in the
destination DAG or Active Directory, the next hop for the message is typically the ultimate
destination itself (for example, the Mailbox server that holds the active copy of the destination
mailbox). Shadow redundancy's goal of keeping two copies of a message in transit is fulfilled
when one shadow copy of the message exists anywhere within the DAG or Active Directory site.
Typically, only failover scenarios in a DAG that require the Redirect-Message cmdlet to drain
the active message queues on a Mailbox server would require multiple hops within the same
transport high availability boundary.

Shadow redundancy with Exchange 2010 Hub Transport
servers in the same Active Directory site in Exchange 2016
organizations
When an Exchange 2010 Hub Transport server transmits a message to an Exchange 2016
Mailbox server in the same Active Directory site, the Exchange 2010 Hub Transport server
advertises support for shadow redundancy using the XSHADOW command, but the Mailbox
server doesn't advertise support for shadow redundancy. This prevents the Exchange 2010 Hub
Transport server from creating a shadow copy of the message on an Exchange 2016 Mailbox
server.

When the Transport service on an Exchange 2016 Mailbox server transmits a message to an
Exchange 2010 Hub Transport in the same Active Directory site, the Exchange 2016 Mailbox
server shadows the message for the Exchange 2010 Hub Transport server. After the Exchange
2016 Mailbox server receives acknowledgment from the Exchange 2010 Hub Transport server

<!-- p.1696 -->

that the message was successfully received, the Exchange 2016 Mailbox server moves the
successfully processed message into Safety Net. However, the successfully processed messages
stored in Safety Net by Exchange 2016 Mailbox are never resubmitted to the Exchange 2010
Hub Transport servers.

SMTP timeouts
During the attempt to make a redundant copy of the message, the SMTP connection between
servers (the sending server and the primary server, or the primary server and the shadow
server) could timeout. Receive connectors and Send connectors both have a
ConnectionInactivityTimeOut parameter for when data is actually being transmitted on the
connector. Receive connectors also have an absolute ConnectionTimeOut parameter.

If any of the SMTP sessions time out before the shadow copy of the message is successfully
created and acknowledged, the result is controlled by the RejectMessageOnShadowFailure
parameter on the Set-TransportConfig cmdlet. By default, the value of this parameter is
$false , which means the primary message is accepted without a shadow copy being created. If

the value of this parameter is $true the primary message is rejected with the transient error
451 4.4.0 .

If the shadow copy of a message is successfully created, but the SMTP session between the
sending server and the primary server times out, the primary server accepts and processes the
primary message. The sending server will re-deliver the unacknowledged message, but
duplicate message detection will prevent Exchange mailbox users from seeing the duplicate
messages. When the sending server resubmits the message, the primary server will create
another shadow copy of the message. There's no relationship between the shadow messages
created during message resubmissions by the sending server.

The following table describes the parameters that control the creation of shadow messages

                                                                                   ﾉ   Expand table

 Source                           Default value   Description

 ShadowMessagePreferenceSetting   PreferRemote    This parameter is only used when the primary
 on Set-TransportConfig                           server that's trying to make a shadow copy of the
                                                  message is a member of a DAG that spans multiple
                                                  Active Directory sites.
                                                         PreferRemote : Try to make a shadow copy of
                                                        the message on a DAG member in a different
                                                        Active Directory site based on the number of
                                                        attempts specified by the
                                                        MaxRetriesForRemoteSiteShadow parameter.
                                                        If the operation fails, try make a shadow

<!-- p.1697 -->

Source                            Default value   Description

                                                        copy of the message on a DAG member in
                                                        the local Active Directory site based on the
                                                        number of attempts specified by the
                                                        MaxRetriesForLocalSiteShadow parameter.
                                                         LocalOnly : Try to make a shadow copy of the
                                                        message only on a DAG member in the local
                                                        Active Directory site based on the number of
                                                        attempts specified by the
                                                        MaxRetriesForLocalSiteShadow parameter.
                                                        RemoteOnly : Try to make shadow copy of the
                                                        message only on a DAG member in a
                                                        different Active Directory site based on the
                                                        number of attempts specified by the
                                                        MaxRetriesForRemoteSiteShadow parameter.

MaxRetriesForRemoteSiteShadow     4               This parameter specifies the maximum number of
on Set-TransportConfig                            attempts to create a shadow copy of the message
                                                  on another server in the DAG when the value of the
                                                  ShadowMessagePreferenceSetting parameter is
                                                  PreferRemote (the default value) or RemoteOnly .

                                                  This parameter is only used when the Mailbox
                                                  server is a member of a DAG that spans multiple
                                                  Active Directory sites.

                                                  If a shadow copy of the message isn't successfully
                                                  created after the specified number of attempts, the
                                                  result depends of the value of the
                                                  RejectMessageOnShadowFailure parameter:

                                                        $true : The primary message is rejected with
                                                        a transient error.
                                                        $false : The primary message is accepted
                                                        anyway, but isn't redundantly persisted.

MaxRetriesForLocalSiteShadow on   2               This parameter specifies the maximum number of
Set-TransportConfig                               attempts to create a shadow copy of the message
                                                  on another Mailbox server in the local Active
                                                  Directory site when:
                                                        The Mailbox server is a member of a DAG
                                                        that spans multiple Active Directory sites,
                                                        and the value of the
                                                        ShadowMessagePreferenceSetting parameter
                                                        is PreferRemote (the default value) or
                                                        LocalOnly .
                                                        The Mailbox server is a member of a DAG
                                                        that's in one Active Directory site.

<!-- p.1698 -->

 Source                           Default value    Description

                                                         The Mailbox server isn't a member of a DAG.

                                                   If a shadow copy of the message isn't successfully
                                                   created after the specified number of attempts, the
                                                   result depends of the value of the
                                                   RejectMessageOnShadowFailure parameter:

                                                         $true : The primary message is rejected with
                                                         a transient error.
                                                         $false : The primary message is accepted
                                                         anyway, but isn't redundantly persisted.

 ConnectionInactivityTimeout on   5 minutes for    This parameter specifies the maximum time that an
 Set-ReceiveConnector             Receive          open SMTP connection with the source messaging
                                  connectors in    server can remain idle before the connection is
                                  the Transport    closed. The value of this parameter must be greater
                                  service on       than the value of the ConnectionTimeout
                                  Mailbox          parameter.
                                  servers

 ConnectionTimeout on Set-        10 minutes for   This parameter specifies the maximum time that an
 ReceiveConnector                 Receive          SMTP connection with the source messaging server
                                  connectors in    can remain open, even if the server is transmitting
                                  the Transport    data. The value of this parameter must be greater
                                  service on       than the value of the ConnectionInactivityTimeout
                                  Mailbox          parameter.
                                  servers

 ConnectionInactivityTimeOut on   10 minutes       This parameter specifies the maximum time that an
 Set-SendConnector                                 open SMTP connection with a destination
                                                   messaging server can remain idle before the
                                                   connection is closed.

How shadow messages are maintained
After a shadow message is successfully created, the work of shadow redundancy has only just
begun. The primary server and the shadow server need to stay in contact with each other to
track the progress of the message.

When the primary server successfully transmits the message to the next hop, and the next hop
acknowledges receipt of the message, the primary server updates the discard status of the
message as delivery complete. The discard status is basically a message that contains of list of
messages that are being monitored. A successfully delivered message doesn't need to be kept
in a shadow queue, so once the shadow server knows the primary server has successfully

<!-- p.1699 -->

transmitted the message to the next hop, the shadow server moves the shadow message from
the shadow queue into Safety Net.

The shadow server determines the discard status of the shadow messages in its shadow
queues by querying the primary server. If the shadow server opens an SMTP session with the
primary server for any reason (including the transmission of other unrelated messages), the
shadow server issues the XQDISCARD command to determine the discard status of the primary
messages. Otherwise, the shadow server will automatically open an SMTP session with the
primary server after a preconfigured time interval (the ShadowHeartbeatFrequency parameter
on the Set-TransportConfig cmdlet; the default value is 2 minutes).

After the shadow server opens an SMTP session with the primary server, the primary server
responds with the discard notifications for messages that apply to the querying shadow server.
Discard notifications are stored on disk (not in memory) so, if the Microsoft Exchange Transport
service restarts, the discard notifications persist. After the service starts, the primary server still
knows about the messages it successfully processed, and that information is available to the
shadow server.

The SMTP communication between the shadow server and the primary server is used as the
heartbeat that determines the availability of the servers. If the shadow server can't open an
SMTP session with the primary server after a preconfigured time interval (the
ShadowResubmitTimeSpan parameter on the Set-TransportConfig cmdlet; the default value is 3
hours) the shadow server promotes itself as the primary server, promotes the shadow
messages as primary messages, and transmits the messages to the next hop. But, whenever the
shadow server detects that the queue database ID of the primary server has changed, the
shadow server also promotes itself as the primary server, promotes the shadow messages as
primary messages, and transmits the messages to the next hop. This could happen well before
the ShadowResubmitTimeSpan parameter value has passed.

Shadow Redundancy Manager is the core component on a Mailbox server that's responsible for
managing shadow redundancy. Shadow Redundancy Manager is responsible for maintaining
the following information for all the primary messages that a server is currently processing:

     The shadow server for each primary message that's being processed.

     The discard status to be sent to shadow servers.

Shadow Redundancy Manager is responsible for the following actions for all the shadow
messages that a shadow server has in its shadow queues:

     Maintaining the list of primary servers for each shadow message.

     Comparing the original database ID and the current database ID of the queue database
     where the primary copy of the message is stored.

<!-- p.1700 -->

     Checking the availability of each primary server for which a shadow message is queued.

     Processing discard notifications from primary servers.

     Removing the shadow messages from the shadow queues after all expected discard
     notifications are received.

     Deciding when the shadow server should take ownership of shadow messages, becoming
     a primary server.

     Tracking message bifurcations and other side-effect messages like delivery status
     notifications (also known as DSNs, non-delivery reports, NDRs, or bounce messages) and
     journal reports to verify that the redundant copy of the message isn't released until all
     forks of the message are fully processed.

This table describes the parameters that control how shadow messages are maintained.

                                                                                       ﾉ   Expand table

 Parameter                           Default     Description
                                     value

 ShadowHeartbeatFrequency on Set-    2           The maximum amount of time a shadow server waits
 TransportConfig                     minutes     before opening an SMTP connection to the primary
                                                 server to check the discard status of messages.

 ShadowResubmitTimeSpan on Set-      3 hours     How long a server waits before deciding that a
 TransportConfig                                 primary server has failed and assumes ownership of
                                                 shadow messages in the shadow queue for the
                                                 primary server that's unreachable.
                                                 Note that a shadow server can also promote itself as
                                                 the primary server before the value of this parameter
                                                 when the queue database of the primary server is
                                                 found to have a different database ID.

 ShadowMessageAutoDiscardInterval    2 days      How long a server retains discard events for
 on Set-TransportConfig                          successfully delivered messages. A primary server
                                                 queues discard events until it's queried by the shadow
                                                 server. However, if the shadow server doesn't query
                                                 the primary server for the duration specified in this
                                                 parameter, the primary server deletes the queued
                                                 discard events.

 SafetyNetHoldTime on Set-           2 days      How long successfully processed messages are
 TransportConfig                                 retained in Safety Net. Unacknowledged shadow
                                                 messages eventually expire from Safety Net after the
                                                 sum of the SafetyNetHoldTime and

<!-- p.1701 -->

 Parameter                                 Default   Description
                                           value

                                                     MessageExpirationTimeout parameter values on the
                                                     Set-TransportService cmdlet.

 MessageExpirationTimeout on Set-          2 days    How long a message can remain in a queue before it
 TransportService                                    expires.

Message processing after an outage
This table summarizes how shadow redundancy minimizes message loss due to server outages.
For clarity, the server that had an outage is named Mailbox01.

                                                                                          ﾉ   Expand table

 Recovery scenario                         Actions taken

 Mailbox01 comes back online with a        When the new queue database ID is detected on Mailbox01,
 new queue database before the value       each server that has shadow messages queued for Mailbox01
 of the ShadowResubmitTimeSpan             will assume ownership of those messages and resubmit them.
 parameter has passed (by default, 3       The messages are then delivered to their destinations.
 hours).                                   The maximum delay for message submission after the new
                                           queue database is detected is the value of the
 This scenario can occur when the          ShadowHeartbeatFrequency parameter (by default, 2 minutes).
 queue database is unrecoverable due
 to data corruption or hardware failure.

 Mailbox01 comes back online with the      After Mailbox01 comes back online, it will deliver the messages
 same database after the value of the      in its queues, which have already been delivered by the servers
 ShadowResubmitTimeSpan parameter          that hold shadow copies of messages for Mailbox01. This will
 has passed (by default, 3 hours).         result in duplicate delivery of these messages. Exchange mailbox
                                           users won't see duplicate messages due to duplicate message
 This scenario can occur after a           detection. However, recipients on other messaging systems
 network card failure, or time-            might see duplicate copies of messages.
 consuming maintenance on the              The maximum delay for message submission is the value of the
 server.                                   ShadowResubmitTimeSpan parameter.

<!-- p.1702 -->

Safety Net in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

In Exchange 2010, the transport dumpster helped protect against data loss by maintaining a
queue of successfully delivered messages that hadn't replicated to the passive mailbox
database copies in the database availability group (DAG). When a mailbox database or server
failure required the promotion of an out-of-date copy of the mailbox database, the messages
in the transport dumpster were automatically resubmitted to the new active copy of the
mailbox database.

The transport dumpster was improved in Exchange 2013 and is now called Safety Net.
Exchange 2016 and Exchange 2019 have these same improvements.

Here's how Safety Net is similar to the transport dumpster in Exchange 2010:

      Safety Net is a queue that's associated with the Transport service on a Mailbox server. This
      queue stores copies of messages that were successfully processed by the server.

      You can specify how long Safety Net stores copies of the successfully processed messages
      before they expire and are automatically deleted. The default is 2 days.

Here's how Safety Net is improved from the transport dumpster in Exchange 2010:

      Safety Net doesn't require a DAG: For Mailbox servers that don't belong to a DAG, Safety
      Net stores copies of the delivered messages on other Mailbox servers in the local Active
      Directory site.

      Safety Net itself isn't a single point of failure: Redundancy is provided by using a
      Primary Safety Net and a Shadow Safety Net. If the Primary Safety Net is unavailable for
      more than 12 hours, resubmit requests become shadow resubmit requests, and messages
      are re-delivered from the Shadow Safety Net.

      Safety Net takes over some responsibility from shadow redundancy in DAG
      environments: Shadow redundancy doesn't need to keep another copy of the delivered
      message in a shadow queue while it waits for the delivered message to replicate to the
      passive copies of mailbox database. The copy of the delivered message is already stored
      in Safety Net, so the message can be resubmitted from Safety Net if necessary.

      Safety Net tries to guarantee message redundancy: Safety Net is more than just a best
      effort for message redundancy, so you can't specify a maximum size limit for Safety Net.
      You can only specify how long Safety Net stores messages before they're automatically
      deleted.

<!-- p.1703 -->

For more information about transport high availability features in Exchange Server, see
Transport high availability in Exchange Server. For more information about message
redundancy for messages in transit, see Shadow redundancy in Exchange Server.

How Safety Net works
Shadow redundancy keeps a redundant copy of the message while the message is in transit.
Safety Net keeps a redundant copy of a message after the message is successfully processed.
So, Safety Net begins where shadow redundancy ends. concepts in shadow redundancy,
including the transport high availability boundary, primary messages, primary servers, shadow
messages and shadow servers also apply to Safety Net. For more information, see Shadow
redundancy in Exchange Server.

The Primary Safety Net exists on the Mailbox server that held the primary message before the
message was successfully processed by the Transport service. This could mean the message
was delivered to the Mailbox Transport Delivery service on the destination Mailbox server. Or,
the message could have been relayed through the Mailbox server in an Active Directory site
that's designated as a hub site on the way to the destination DAG or Active Directory site. After
the primary server processes the primary message, the message is moved from the active
delivery queue into the Primary Safety Net on the same server.

The Shadow Safety Net exists on the Mailbox server that held the shadow message. After the
shadow server determines the primary server has successfully processed the primary message,
the shadow server moves the shadow message from the shadow queue into the Shadow Safety
Net on the same server. Although it may seem obvious, the existence of the Shadow Safety Net
requires shadow redundancy to be enabled (it's is enabled by default).

This table describes the parameters that are used by Safety Net.

                                                                                   ﾉ   Expand table

 Parameter                    Default      Description
                              value

 SafetyNetHoldTime on Set-    2 days       The length of time successfully processed primary
 TransportConfig                           messages are stored in Primary Safety Net, and
                                           acknowledged shadow messages are stored in Shadow
                                           Safety Net.
                                           You can also specify this value in the Exchange admin
                                           center (EAC) at Mail flow > Receive connectors > More
                                           options    > Organization transport settings > Safety
                                           Net > Safety Net hold time.

<!-- p.1704 -->

 Parameter                     Default       Description
                               value

                                             Unacknowledged shadow messages eventually expire
                                             from Shadow Safety Net after the sum of
                                             SafetyNetHoldTime and MessageExpirationTimeout
                                             parameter values.

                                             To avoid data loss during Safety Net resubmits, the value
                                             of this parameter must be greater than or equal to the
                                             value of ReplayLagTime on Set-MailboxDatabaseCopy for
                                             the lagged copy of the mailbox database.

 ReplayLagTime on Set-         Not           The amount of time that the Microsoft Exchange
 MailboxDatabaseCopy           configured    Replication service should wait before replaying log files
                                             that have been copied to the passive database copy.
                                             Setting this parameter to a value greater than 0 creates a
                                             lagged copy of the mailbox database. The maximum value
                                             is 14 days.
                                             To avoid data loss during Safety Net resubmits, the value
                                             of this parameter for the lagged copy of the mailbox
                                             database must be less than or equal to the value of
                                             SafetyNetHoldTime on Set-TransportConfig.

 MessageExpirationTimeout on   2 days        How long a message can remain in a queue before it
 Set-TransportService                        expires.

 ShadowRedundancyEnabled       $true         $true : Shadow redundancy is enabled on all Mailbox
 on Set-TransportConfig                      servers in the organization.

                                             $false : Shadow redundancy is disabled on all transport
                                             servers in the organization.

                                             Redundancy for Safety Net requires shadow redundancy
                                             to be enabled.

Safety Net maximum supported sizes
In Microsoft Exchange Server 2019 and 2016, the maximum supported database size for the
transport Safety Net JET database is 2 TB.

When a Hub-and-spoke topology is used, the transport Safety Net JET database can grow
beyond 2 TB. To stay within the supported limit of 2 TB, follow these guidelines:

     Hub servers that are used for message relay can't be configured to deliver messages to
     mailboxes.

<!-- p.1705 -->

     Disable Safety Net on hub servers that are used for message relay. To do this, follow these
     steps:

        1. In a Command prompt window, open the EdgeTransport.exe.config file in Notepad
          by running the following command on the server:

              DOS

              Notepad %ExchangeInstallPath%Bin\EdgeTransport.exe.config

        2. Add the following key in the appSettings section.

              XML

              <add key="SafetyNetHoldTimeInterval" value="0.00:00:15" />

          When you're finished, save and close the EdgeTransport.exe.config file.

        3. Restart the Exchange Transport service by running the following command:

              DOS

              net stop MSExchangeTransport && net start MSExchangeTransport

Message resubmission from Safety Net
The Active Manager component of the Microsoft Exchange Replication service
(MSExchangeRepl.exe) manages DAGs and mailbox database copies. Message resubmissions
from Safety Net require no manual actions, and are initiated by the Active Manager. For more
information about Active Manager, see Active Manager.

There are two basic Safety Net message resubmission scenarios:

     After the automatic or manual failover of a mailbox database in a DAG.

     After you activate a lagged copy of a mailbox database.

A lagged mailbox database copy or lagged copy is a passive copy of a mailbox database where
updates to the database are intentionally delayed to protect against logical corruption of the
mailbox database. For more information, see Manage mailbox database copies.

The only significant difference between the two scenarios is how far back in time to go to
resubmit messages from Safety Net. Typically, for database failover in a DAG, the new active
copy of the mailbox database is anywhere from several minutes to several hours behind the old

<!-- p.1706 -->

active copy. A lagged copy of a mailbox database is typically several days behind the old active
copy.

The main requirement for successful message resubmission from Safety Net for a lagged copy
is: the length of time messages are stored in Safety Net must be greater than or equal to the
lag time of the lagged copy. In other words, the value of SafetyNetHoldTime on Set-
TransportConfig must be greater than or equal to the value of the ReplayLagTime on Set-
MailboxDatabaseCopy for the lagged copy.

Message resubmission from Shadow Safety Net
Message resubmission from Shadow Safety Net (like message resubmission from Primary
Safety Net), is fully automated, and requires no manual intervention. This scenario describes
the interaction of Primary Safety Net and Shadow Safety Net during message resubmission:

   1. Active Manager requests message resubmission from Safety Net for a mailbox database
        for the specified time interval (for example, 5:00 to 9:00). However, the Mailbox server
        that holds the Primary Safety Net has crashed due to a hardware failure. Active Manager
        unsuccessfully tries to contact the Primary Safety Net for the next 12 hours.

   2. After 12 hours, Active Manager sends a broadcast message to the Transport service on all
        Mailbox servers in the transport high availability boundary (the DAG or Active Directory
        site in non-DAG environments) looking for other Safety Nets that contain messages for
        the target mailbox database for the specified time interval. The Shadow Safety Net
        responds and resubmits messages for the mailbox database for the time interval 5:00 to
        9:00.

When a Shadow Safety Net responds, it only resubmits the messages for the required mailbox
database during the required time interval. This restriction by mailbox database and time
interval helps reduce these potential issues:

        Resubmitting messages from Safety Net could result in duplicate deliveries. This isn't an
        issue for mailboxes in the Exchange organization, because duplicate message detection
        prevents mailbox users from seeing the duplicate messages. But, duplicate message
        delivery to external recipients could result in duplicate copies of messages that the
        recipient would see.

        Shadow messages resubmitted from Shadow Safety Net require full categorization and
        processing through the Transport service on the Mailbox server. Resubmission of a large
        number of shadow messages can be expensive in terms of Mailbox server system
        resources.

<!-- p.1707 -->

These are some important considerations for the shadow messages that are stored in Shadow
Safety Net:

     Shadow Safety Net doesn't know where the primary server transmitted the primary
     message.

     The shadow messages in Shadow Safety Net only contain original message envelope
     recipients, not the actual recipients where the primary message was delivered (for
     example, the message envelope recipient might be a distribution group that requires
     expansion).

     The messages in Shadow Safety net don't contain any message updates that occurred
     after the primary server processed the message (for example, message encoding or
     content conversion).

This scenario describes what happens if the Primary Safety Net is offline during part of the
requested resubmit interval:

   1. The queue database on the Mailbox server that holds the Primary Safety Net is corrupt,
     and a new queue database is created at 7:00. All of the primary messages stored in the
     Primary Safety Net from 1:00 to 7:00 are lost, but the server is able to store copies of
     successfully delivered messages in Safety Net starting at 7:00.

   2. Active Manager requests a resubmission of messages from Safety Net for a mailbox
     database for the time interval 1:00 to 9:00.

   3. The Primary Safety Net resubmits messages for the time interval 7:00 to 9:00.

   4. Because the Primary Safety Net doesn't have the required messages for 1:00 to 7:00. the
     Primary Safety Net sends a broadcast message to the Transport service on all Mailbox
     servers in the transport high availability boundary looking for other Safety Nets that
     contain the required messages. The Shadow Safety Net generates a second resubmit
     request on behalf of the Primary Safety Net to resubmit the shadow messages for the
     target mailbox database for the time interval 1:00 to 7:00.

These are some other issues to consider when messages are resubmitted from Safety Net:

     All delivery status notifications (also known as DSNs, non-delivery reports, NDRs or
     bounce messages) are suppressed for Safety Net message resubmissions: For example,
     if the primary message resulted in an NDR, the NDR for the resubmitted message won't
     be delivered.

     Users removed from a distribution group may not receive a resubmitted message when
     the Shadow Safety Net resubmits the message: For example, a message is sent to a
     group containing User A and User B, and both recipients receive the message. User B is

<!-- p.1708 -->

subsequently removed from the group. Later, a resubmit request from Primary Safety Net
is made for the mailbox database that holds User B's mailbox. However, the Primary
Safety Net is unavailable for more than 12 hours, so the Shadow Safety Net server
responds and resubmits the affected message. During message resubmission when the
distribution group is expanded, User B is no longer a member of the group, and won't
receive a copy of the resubmitted message.

New Users added to a distribution group may receive an old resubmitted message
when the Shadow Safety Net resubmits the message: For example, a message is sent to
a group containing User A and User B, and both recipients receive the message. User C is
subsequently added to the group. Later, a resubmit request from Primary Safety Net is
made for the mailbox database that holds User C's mailbox. However, the Primary Safety
Net server is unavailable for more than 12 hours, so the Shadow Safety Net server
responds and resubmits the affected messages. During message resubmission when the
distribution group is expanded, User C is now a member of the group, and will receive a
copy of the resubmitted message.

Deploying Safety Net in Hub and Spoke Topology: Safety Net is designed to protect
message delivery on Exchange Servers hosting end-user mailboxes. Customers who have
deployed a hub and spoke routing topology should disable Safety Net on transport
servers in hub sites to avoid a large growth in the size of the transport database in hub
locations.

<!-- p.1709 -->

Transport logs in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Transport logs provide information about what's happening in the transport pipeline. For more
information about the transport pipeline, see Mail flow and the transport pipeline.

The transport logs in Exchange Server are described in the following sections.

Agent logging
Agent logging records the actions that are performed on messages by specific antispam
transport agents on the Exchange server. For more information, see these topics:

      Antispam Agent Logging

      Configure Antispam Agent Logging

      Enable antispam functionality on Mailbox servers

Enabled by default?: Yes

Default location of log files: Note that the folder isn't created until an agent attempts to write
information to the log.

      Mailbox servers:

         Front End Transport service:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\AgentLog

         Transport service: %ExchangeInstallPath%TransportRoles\Logs\Hub\AgentLog

      Transport service on Edge Transport servers:
      %ExchangeInstallPath%TransportRoles\Logs\Edge\AgentLog

Connectivity logging
Connectivity logging records outbound message transmission activity by the transport services
on the Exchange server. For more information, see these topics:

      Connectivity logging in Exchange Server

      Configure connectivity logging in Exchange Server

<!-- p.1710 -->

Enabled by default?: Yes

Default location of log files:

     Mailbox servers:

          Front End Transport service:
          %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\Connectivity

          Transport service: %ExchangeInstallPath%TransportRoles\Logs\Hub\Connectivity

          Mailbox Transport Delivery service:
          %ExchangeInstallPath%TransportRoles\Logs\Mailbox\Connectivity\Delivery

          Mailbox Transport Submission service:

     Transport service on Edge Transport servers:
      %ExchangeInstallPath%TransportRoles\Logs\Edge\Connectivity

Message tracking and delivery reports for
administrators
Message tracking is a detailed record of all message activity as mail flows through the
transport pipeline on an Exchange server. For more information, see these topics:

     Message tracking

     Configure message tracking

     Search message tracking logs

Delivery reports for administrators is a targeted search of the message tracking log for
messages that were sent to or from a specified mailbox. For more information, see these
topics:

     Delivery reports for administrators

     Track messages with delivery reports

Enabled by default?: Yes

Default location of log files:

     Mailbox servers: %ExchangeInstallPath%TransportRoles\Logs\MessageTracking :

          MSGTRK files for the Transport service.

<!-- p.1711 -->

         MSGTRMD files for the Mailbox Transport Delivery service.

         MSGTRMS files for the Mailbox Transport Submission service.

     Transport service on Edge Transport servers:
      %ExchangeInstallPath%TransportRoles\Logs\MessageTracking

Pipeline tracing
Pipeline tracing records snapshots of messages before and after the message is affected by
transport agents in the transport pipeline. For more information, see these topics:

     Pipeline Tracing

     Configure Pipeline Tracing

Enabled by default?: No

Default location of log files: Note that the folder isn't created until pipeline tracing is enabled.

     Mailbox servers:

        Transport service: %ExchangeInstallPath%TransportRoles\Logs\Hub\PipelineTracing

        Mailbox Transport service:
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\PipelineTracing

     Transport service on Edge Transport servers:
      %ExchangeInstallPath%TransportRoles\Logs\Edge\PipelineTracking

Protocol logging
Protocol logging records the SMTP conversations that occur on Send connectors and Receive
connectors during message delivery. For more information, see these topics:

     Protocol logging

     Configure protocol logging

Enabled by default?: Only on these connectors:

     The default Receive connector named Default Frontend <ServerName> in the Front End
     Transport service on Mailbox servers.

<!-- p.1712 -->

     The implicit and invisible Send connector in the Front End Transport service on Mailbox
     servers.

For more information about these connectors, see Default Receive connectors created during
setup and Implicit Send connectors.

Default location of log files:

     Mailbox servers:

        Front End Transport service:

        Receive connectors:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpReceive

        Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpSend

        Transport service:

        Receive connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Hub\ProtocolLog\SmtpReceive

        Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Hub\ProtocolLog\SmtpSend

        Mailbox Transport Delivery service (Receive Connectors):
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpReceive\Delivery

        Mailbox Transport Submission service:

        Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpSend\Submission

        Side effect messages:
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpSend\Delivery

     Transport service on Edge Transport servers:

        Receive connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Edge\ProtocolLog\SmtpReceive

        Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Edge\ProtocolLog\SmtpSend

<!-- p.1713 -->

Routing table logging
Note: The Routing Log Viewer is no longer available in the Exchange Toolbox.

Routing table logging periodically records snapshots of the routing table that Exchange servers
uses to deliver messages. For more information, see these topics:

     Understanding Routing Table Logging

     Configure Routing Table Logging

Enabled by default?: Yes

Default location of log files:

     Mailbox servers:

        Front End Transport service:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\Routing

        Transport service: %ExchangeInstallPath%TransportRoles\Logs\Hub\Routing

        Mailbox Transport service::
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\Routing :

         MDRoutingConfig files for the Mailbox Transport Delivery service.

         MSRoutingConfig files for the Mailbox Transport Submission service.

     Transport service on Edge Transport servers:
      %ExchangeInstallPath%TransportRoles\Logs\Edge\Routing

<!-- p.1714 -->

Message tracking
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

The message tracking log is a detailed record of all activity as mail flows through the transport
pipeline on Mailbox servers and Edge Transport servers. You can use message tracking for
message forensics, mail flow analysis, reporting, and troubleshooting.

By default, Exchange uses circular logging to limit the message tracking log based on file size
and file age to help control the hard disk space that's used by the log files. To configure the
message tracking log, see Configure message tracking.

Search the message tracking log
Message tracking logs contain vast amounts of data as messages move through a Mailbox
server or Edge Transport server. When it comes to searching the message tracking logs, you
have options:

      Get-MessageTrackingLog: Administrators can use this Exchange Management Shell
      cmdlet to search the message tracking log for information about messages using a wide
      range of filter criteria. For more information, see Search message tracking logs.

      Delivery reports for administrators: Administrators can use the Delivery reports tab in
      the Exchange admin center or the underlying Search-MessageTrackingReport and Get-
      MessageTrackingReport cmdlets in the Exchange Management Shell to search the
      message tracking logs for information about messages sent by or received by a specific
      mailbox in the organization. For more information, see Delivery reports for administrators.

Structure of the message tracking log files
By default, the message tracking log files exist in
%ExchangeInstallPath%TransportRoles\Logs\MessageTracking . The folder contains log files that

have different names, but they all follow the naming convention MSGTRKServiceyyyyMMdd-
nnnn.log . The different log file names are described in the following table.

                                                                                 ﾉ   Expand table

<!-- p.1715 -->

 File         Servers                    Description
 name

 MSGTRK       Mailbox servers and Edge   Log files for the Transport service.
              Transport servers

 MSGTRKMA     Mailbox servers            Log files for the approvals and rejections in moderated transport.
                                         For more information, see Manage message approval.

 MSGTRKMD     Mailbox servers            Log files for messages delivered to mailboxes by the Mailbox
                                         Transport Delivery service.

 MSGTRKMS     Mailbox servers            Log files for messages sent from mailboxes by the Mailbox
                                         Transport Submission service.

The other placeholders in the log file names represent the following information:

     yyyyMMdd is the coordinated universal time (UTC) date when the log file was created.
     yyyy = year, MM = month, and dd = day.

     nnnn is an instance number that starts at the value 1 every day for each log.

Information is written to the log file until the file reaches its maximum size. Then, a new log file
that has an incremented instance number is opened (the first log file is -1, the next is -2, and so
on). Circular logging deletes the oldest log files for a service when either of the following
conditions are true:

     A log file reaches its maximum age.

     The message tracking log folder reaches its maximum size.

     Notes:

          The maximum size of the message tracking log folder is calculated as the total size of
          all log files that have the same name prefix. Other files that do not follow the name
          prefix convention are not counted in the total folder size calculation. Renaming old log
          files or copying other files into the message tracking log folder could cause the folder
          to exceed its specified maximum size.

          On Mailbox servers, the maximum size of the message tracking log folder is three
          times the specified value. Although the message tracking log files are generated by the
          four different services and have four different name prefixes, the amount and
          frequency of data written to the moderated transport log ( MSGTRKMA ) is negligible
          compared to the other three logs.

The message tracking log files are text files that contain data in the comma-separated value
(CSV) format. Each message tracking log file has a header that contains the following

<!-- p.1716 -->

information:

      #Software: The value is Microsoft Exchange Server .

      #Version: Version number of the Exchange server that created the message tracking log
      file. The value uses the format 15.01.nnnn.nnn .

      #Log-Type: The value is Message Tracking Log .

      #Date: The UTC date-time when the log file was created. The UTC date-time is
      represented in the ISO 8601 date-time format: yyyy-MM-ddThh:mm:ss.fffZ, where yyyy =
      year, MM = month, dd = day, T indicates the beginning of the time component, hh =
      hour, mm = minute, ss = second, fff = fractions of a second, and Z signifies Zulu, which is
      another way to denote UTC.

      #Fields: Comma-delimited field names that are used in the message tracking log files.

Fields in the message tracking log files
The message tracking log stores each message event on a single line in the log. The message
event information is organized by fields, and these fields are separated by commas. The field
name is generally descriptive enough to determine the type of information that it contains.
However, some fields may be blank, or the type of information in the field may change based
on the message event type and the service that recorded the event. General descriptions of the
fields that are used to classify each message tracking event are explained in the following table.

                                                                                          ﾉ   Expand table

 Field name      Description

 date-time       The UTC date-time of the message tracking event. The UTC date-time is represented in
                 the ISO 8601 date-time format: yyyy-MM-ddThh:mm:ss.fffZ, where yyyy = year, MM =
                 month, dd = day, T indicates the beginning of the time component, hh = hour, mm =
                 minute, ss = second, fff = fractions of a second, and Z signifies Zulu, which is another
                 way to denote UTC.

 client-ip       The IPv4 or IPv6 address of the messaging server or messaging client that submitted the
                 message.

 client-         The host name or FQDN of the messaging server or messaging client that submitted the
 hostname        message.

 server-ip       The IPv4 or IPv6 address of the source or destination server.

 server-         The host name or FQDN of the destination server.
 hostname

<!-- p.1717 -->

Field name     Description

source-        Extra information associated with the source field. For example:
context        CatContentConversion
               250 2.0.0 OK;ClientSubmitTime:<UTC>

connector-id   The name of the Send connector or Receive connector that accepted the message. For
               example, ServerName\ ConnectorName or ConnectorName.

source         The Exchange transport component that's responsible for the event. These values are
               described in the Source values in the message tracking log section later in this topic.

event-id       The message event type. These values are described in the Event types in the message
               tracking log section later in this topic.

internal-      A message identifier that's assigned by the Exchange server that's currently processing
message-id     the message.
               The internal-message-id of a message is different in the message tracking log of every
               Exchange server that's involved in the transmission of the message. An example value is
               73014444033 .

message-id     The value of the Message-Id: header field in the message header. If the Message-Id:
               header field doesn't exist or is blank, Exchange assigns an arbitrary value. This value is
               constant for the lifetime of the message. For messages created in Exchange, the value is
               in the format <GUID@ServerFQDN> , including the angle brackets ( < > ). For example,
                <4867a3d78a50438bad95c0f6d072fca5@mailbox01.contoso.com> . Other messaging systems
               may use different syntax or values.

network-       A unique message ID value that persists across copies of the message that may be
message-id     created due to bifurcation or distribution group expansion. An example value is
               1341ac7b13fb42ab4d4408cf7f55890f .

recipient-     The email addresses of the message's recipients. Multiple email addresses are separated
address        by the semicolon character (;).

recipient-     The recipient status for each recipient separated by the semicolon character (;). The
status         status values are presented for the recipients in the same order as the values in the
               recipient-address field. Example status values include:
               To , Cc or Bcc
               250 2.1.5 Recipient OK
               550 4.4.7 QUEUE.Expired;<ErrorText>

total-bytes    The total size of the message in bytes, including all attachments.

recipient-     The total number of recipients in the message.
count

related-       This field is used with EXPAND, REDIRECT, and RESOLVE events to display other
recipient-     recipient email addresses that are associated with the message.
address

<!-- p.1718 -->

Field name       Description

reference        This field contains additional information for specific types of events. For example:
                 DSN: Contains the report link, which is the Message-Id value of the associated delivery
                 status notification (also known as a DSN, bounce message, non-delivery report, or NDR)
                 if a DSN is generated subsequent to this event. If this is a DSN message, the Reference
                 field contains the Message-Id value of the original message that the DSN was generated
                 for.
                 EXPAND: Contains the related-recipient-address value of the related messages.
                 RECEIVE: May contain the Message-Id value of the related message if the message was
                 generated by other processes, for example, journaling or inbox rules.
                 SEND: Contains the Internal-Message-Id value of any DSN messages.
                 THROTTLE: Contains the reason why the message was throttled.
                 TRANSFER: Contains the Internal-Message-Id value of the message that's being forked.
                 Message generated by inbox rules: Contains the Internal-Message-Id value of the
                 inbound message that caused the inbox rule to generate the outbound message.
                 Forked messages: Might contain the Internal-Message-Id value.
                 For other types of events, this field is usually blank.

message-         The message's subject found in the Subject: header field. The tracking of message
subject          subjects is controlled by the MessageTrackingLogSubjectLoggingEnabled parameter on
                 the Set-TransportService cmdlet. By default, message subject tracking is enabled.

sender-          The email address specified in the Sender: header field, or the From: header field if the
address          Sender: field doesn't exist.

return-path      The return email address specified by the MAIL FROM command that sent the message.
                 Although this field is never empty, it can have the null sender address value represented
                 as <> .

message-info     Additional information about the message. For example:
                 The message origination date-time in UTC for DELIVER and SEND events. The origination
                 date-time is the time when the message first entered the Exchange organization. The
                 UTC date-time is represented in the ISO 8601 date-time format: yyyy-MM-
                 ddThh:mm:ss.fffZ, where yyyy = year, MM = month, dd = day, T indicates the beginning
                 of the time component, hh = hour, mm = minute, ss = second, fff = fractions of a
                 second, and Z signifies Zulu, which is another way to denote UTC.
                 Authentication errors. For example, you may see the value 11a and the type of
                 authentication that was used when the authentication error occurred.

directionality   The direction of the message. Example values include Incoming , Undefined , and
                 Originating .

tenant-id        This field isn't used in on-premises Exchange organizations.

original-        The IPv4 or IPv6 address of the original client.
client-ip

original-        The IPv4 or IPv6 address of the original server.
server-ip

<!-- p.1719 -->

 Field name     Description

 custom-data    This field contains data related to specific event types. For example, the Transport Rule
                agent uses this field to record the GUID of the mail flow rule (also known as a transport
                rule) or DLP policy that acted on the message. For more information, see View DLP policy
                detection reports.

 transport-     In on-premises Exchange, this field is blank or has the value Email .
 traffic-type

 log-id         A unique identifier for a row in the in the message tracking log. This field isn't important
                in on-premises Exchange organizations.

 schema-        Version number of the Exchange server that created the entry in the message tracking
 version        log. The value uses the format 15.01.nnnn.nnn .

Event types in the message tracking log
Various event types in the event-id field are used to classify the message events in the message
tracking log. Some message events appear in only one type of message tracking log file, and
some message events appear in all types of message tracking log files. The events types that
are used to classify each message event are explained in the following table.

                                                                                          ﾉ   Expand table

 Event name                    Description

 AGENTINFO                     This event is used by transport agents to log custom data.

 BADMAIL                       A message submitted by the Pickup directory or the Replay directory that
                               can't be delivered or returned.

 CLIENTSUBMISSION              A message was submitted from the Outbox of a mailbox.

 DEFER                         Message delivery was delayed.

 DELIVER                       A message was delivered to a local mailbox.

 DELIVERFAIL                   An agent tried to deliver the message to a folder that doesn't exist in the
                               mailbox.

 DROP                          A message was dropped without a delivery status notification (also known
                               as a DSN, bounce message, non-delivery report, or NDR). For example:
                                     Completed moderation approval request messages.
                                     Spam messages that were silently dropped without an NDR.

 DSN                           A delivery status notification (DSN) was generated.

<!-- p.1720 -->

Event name           Description

DUPLICATEDELIVER     A duplicate message was delivered to the recipient. Duplication may
                     occur if a recipient is a member of multiple nested distribution groups.
                     Duplicate messages are detected and removed by the information store.

DUPLICATEEXPAND      During the expansion of the distribution group, a duplicate recipient was
                     detected.

DUPLICATEREDIRECT    An alternate recipient for the message was already a recipient.

EXPAND               A distribution group was expanded.

FAIL                 Message delivery failed. Sources include SMTP, DNS, QUEUE, and
                     ROUTING.

HADISCARD            A shadow message was discarded after the primary copy was delivered to
                     the next hop. For more information, see Shadow redundancy in Exchange
                     Server.

HARECEIVE            A shadow message was received by the server in the local database
                     availability group (DAG) or Active Directory site.

HAREDIRECT           A shadow message was created.

HAREDIRECTFAIL       A shadow message failed to be created. The details are stored in the
                     source-context field.

INITMESSAGECREATED   A message was sent to a moderated recipient, so the message was sent to
                     the arbitration mailbox for approval. For more information, see Manage
                     message approval.

LOAD                 A message was successfully loaded at boot.

MODERATIONEXPIRE     A moderator for a moderated recipient never approved or rejected the
                     message, so the message expired. For more information about moderated
                     recipients, see Manage message approval.

MODERATORAPPROVE     A moderator for a moderated recipient approved the message, so the
                     message was delivered to the moderated recipient.

MODERATORREJECT      A moderator for a moderated recipient rejected the message, so the
                     message wasn't delivered to the moderated recipient.

MODERATORSALLNDR     All approval requests sent to all moderators of a moderated recipient
                     were undeliverable, and resulted in non-delivery reports (also known as
                     NDRs or bounce messages).

NOTIFYMAPI           A message was detected in the Outbox of a mailbox on the local server.

NOTIFYSHADOW         A message was detected in the Outbox of a mailbox on the local server,
                     and a shadow copy of the message needs to be created.
