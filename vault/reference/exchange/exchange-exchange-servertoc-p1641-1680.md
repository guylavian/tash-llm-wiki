---
title: "Exchange Server — pages 1641-1680"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1641-1680
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1641-1680
family: exchange
documentKind: "doc"
abstract: "421 service not available 450 requested action not taken TLS or certificate-related failures Protocol logs confirm whether Exchange Server is attempting delivery and how the remote server is responding. Recipient rejections If messages are rejected for specific recipients: Searc"
---

# Exchange Server — pages 1641-1680

<!-- p.1641 -->

          421 service not available
          450 requested action not taken

         TLS or certificate-related failures

Protocol logs confirm whether Exchange Server is attempting delivery and how the remote
server is responding.

Recipient rejections
If messages are rejected for specific recipients:

      Search for RCPT TO commands.
      Examine the SMTP response returned by Exchange.
      Errors such as 550 5.1.1 User unknown or 550 5.7.1 Access denied typically indicate
      directory, policy, or permission issues.

Correlating protocol logs with message tracking
logs
Protocol logs capture SMTP communication details, while message tracking logs show how
Exchange Server processed the message internally. Use both logs together to troubleshoot
mail flow issues:

   1. Use protocol logs to confirm SMTP acceptance or rejection.
   2. Use message tracking logs to trace the message inside Exchange Server.
   3. Correlate timestamps, sender, recipient, and message IDs.

These logs together provide a complete picture of the mail flow path.

 Last updated on 03/03/2026

<!-- p.1642 -->

Mail routing in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016   2019      Subscription Edition

The primary task of the Transport service that exists on Mailbox servers in your Exchange
organization is to route messages received from users and external sources to their ultimate
destinations. Routing decisions are made during message categorization. The categorizer is a
component of the Transport service that processes all incoming messages and determines
what to do with the message based on information about their destinations.

Routing in Exchange 2016 and Exchange 2019 is virtually unchanged from Exchange 2013.
These are the notable changes to routing compared to Exchange 2010:

      Routing is fully aware of database availability groups (DAGs), and is able to use DAG
      membership in routing decisions, even when the DAG members are in different Active
      Directory sites. For Mailbox servers that don't belong to DAGs and for interoperability
      with previous versions of Exchange, Active Directory site membership is still used in
      routing decisions.

      The Transport service never communicates directly with a mailbox database. Instead, the
      Transport service communicates with the Mailbox Transport service locally or on remote
      Mailbox servers. Only the Mailbox Transport service communicates with the local mailbox
      database. When the Mailbox server is a member of a DAG, only the Mailbox Transport
      service on the Mailbox server that holds the active copy of the mailbox database accepts
      messages for the destination recipient.

      Remote procedure calls (RPCs) are used only by the Mailbox Transport service to send
      messages to or receive messages from the local mailbox database. When the Mailbox
      server is a member of a DAG, the Mailbox Transport service only uses RPCs to
      communicate locally with the active copies of the mailbox databases. In other words, RPC
      is never used for cross-server or cross-service communication. Instead, the Mailbox
      Transport service and the Transport service always communicate using SMTP.

      Exchange now uses more precise queuing for remote destinations. Instead of using one
      queue for all destinations in a remote Active Directory site, Exchange now queues
      messages for specific destinations within the Active Directory site, such as individual Send
      connectors.

      Linked connectors are no longer available. A linked connector was a Receive connector
      that was linked to a Send connector. All messages received by the Receive connector
      were automatically forwarded to the Send connector.

<!-- p.1643 -->

Routing components
When a message is received by the Transport service on a Mailbox server, the message must be
categorized. The first phase of message categorization is recipient resolution. After the
recipient has been resolved, the ultimate destination can be determined. The next phase,
routing, determines how to best reach that destination. Routing in Exchange is generalized for
increased flexibility and decreased complexity by using the concepts of routing destinations
and delivery groups.

Routing destinations
The ultimate destination for a message is called a routing destination. Regardless of the
complexity of an Exchange organization, there are surprisingly few routing destinations. They
are:

       A mailbox database: This is the routing destination for any recipient with a mailbox in the
       Exchange organization. In Exchange 2013 or later, public folders are a type of mailbox, so
       routing messages to public folder recipients is the same as routing messages to mailbox
       recipients.

       A connector: A Send connector is used as a routing destination for SMTP messages based
       on the configuration of the Send connector (address spaces, scoped or not, etc.).
       Similarly, a Delivery Agent connector or Foreign connector is used as a routing
       destination for non-SMTP messages.

       A distribution group expansion server: This is the routing destination when a distribution
       group has a designated expansion server (a server that's responsible for expanding the
       membership list of the group). A distribution group expansion server is an Exchange 2013
       or later Mailbox server or an Exchange 2010 Hub Transport server.

Note that these routing destinations existed in previous versions of Exchange, but they weren't
called routing destinations.

Delivery groups
A collection of one or more transport servers is responsible for delivering mail to each routing
destination. This collection of transport servers is called a delivery group. The term transport
servers is used because the servers could be a mixture of Exchange 2013 or later Mailbox
servers (the Transport service) or Exchange 2010 Hub Transport servers. The relationship
between routing destinations and delivery groups is explained in the following table:

<!-- p.1644 -->

                                                                                    ﾉ    Expand table

 Routing destination                           Delivery group

 Exchange 2013 or later mailbox databases      Exchange 2013 or later Mailbox servers.

 Exchange 2010 mailbox databases in Exchange   Only Exchange 2010 Hub Transport servers.
 2016 organizations

 Connectors                                    Exchange 2013 or later Mailbox servers or Exchange
                                               2010 Hub Transport servers.

 Distribution group expansion servers          Exchange 2013 or later Mailbox servers or Exchange
                                               2010 Hub Transport servers.

How the message is routed depends on the relationship between the source delivery group
and the destination delivery group:

     If the source and destination delivery group are the same, no routing decisions are
     required. The routing destination is the next hop for the message.

     If the source delivery group is outside the destination delivery group, routing decisions
     are required. The message is relayed along the least-cost routing path to the destination
     delivery group. Depending on the size and complexity of the Exchange environment, the
     message might be relayed through many transport servers to reach the destination
     delivery group for delivery to the routing destination.

The different types of delivery groups that exist in Exchange 2016 are summarized in the
following table.

                                                                                    ﾉ    Expand table

<!-- p.1645 -->

Delivery     Delivery group             Routing               Comments
group type                              destination

Routable           Exchange 2019        Mailbox               After the message arrives at a Mailbox
DAG                Mailbox servers      databases in the      server in the DAG, the Transport service
                   that belong to the   DAG                   routes the message to the Mailbox
                   Exchange 2019                              Transport Delivery service on the DAG
                   DAG.                                       member that holds the active copy of the
                   Exchange 2016                              destination mailbox database. The
                   Mailbox servers                            Mailbox Transport Delivery service then
                   that belong to the                         delivers the message to the local mailbox
                   Exchange 2016                              database. Although a DAG might contain
                   DAG.                                       Mailbox servers located in different Active
                   Exchange 2013                              Directory sites, the DAG defines the
                   Mailbox servers                            delivery group, not the Active Directory
                   that belong to the                         site.
                   Exchange 2013
                   DAG.

Mailbox      Exchange 2013 or later     Mailbox               Mailbox databases located on servers that
delivery     Mailbox servers in the     databases on          don't belong to a DAG are serviced by the
group        Active Directory site.     Exchange 2013         Transport service on Mailbox servers in the
(Exchange                               or later servers in   same Active Directory site.
2013 or                                 the Active            After the message arrives on a Mailbox
later)                                  Directory site        server in the Active Directory site, the
                                        that don't belong     Transport service uses SMTP to transfer
                                        to a DAG.             the message to the Mailbox Transport
                                                              Delivery service on the Mailbox server that
                                                              holds the mailbox database. The Mailbox
                                                              Transport Delivery service then delivers
                                                              the message to the local mailbox database
                                                              using RPC.

                                                              In other words, the following mail delivery
                                                              paths are supported between the different
                                                              versions of Exchange:

                                                                    Exchange 2019 Transport service to
                                                                    Exchange 2016 Mailbox Transport
                                                                    Delivery service to Exchange 2016
                                                                    mailbox database.
                                                                    Exchange 2019 Transport service to
                                                                    Exchange 2013 Mailbox Transport
                                                                    Delivery service to Exchange 2013
                                                                    mailbox database.
                                                                    Exchange 2016 Transport service to
                                                                    Exchange 2019 Mailbox Transport
                                                                    Delivery service to Exchange 2019
                                                                    mailbox database.

<!-- p.1646 -->

Delivery      Delivery group              Routing            Comments
group type                                destination

                                                                    Exchange 2016 Transport service to
                                                                    Exchange 2013 Mailbox Transport
                                                                    Delivery service to Exchange 2013
                                                                    mailbox database.
                                                                    Exchange 2013 Transport service to
                                                                    Exchange 2019 Mailbox Transport
                                                                    Delivery service to Exchange 2019
                                                                    mailbox database.
                                                                    Exchange 2013 Transport service to
                                                                    Exchange 2016 Mailbox Transport
                                                                    Delivery service to Exchange 2016
                                                                    mailbox database.

Mailbox       Exchange 2010 Hub           Mailbox            Mailbox databases located on Exchange
delivery      Transport servers in the    databases on       2010 Mailbox servers are serviced by the
group         Active Directory site.      Exchange 2010      Exchange 2010 Hub Transport servers in
(Exchange                                 Mailbox servers    the same Active Directory site. p> After
2010)                                     in the Active      the message arrives at a random Exchange
                                          Directory site.    2010 Hub Transport server in the Active
                                                             Directory site, the store driver on the Hub
                                                             Transport server uses RPC to write the
                                                             message to the mailbox database.

Connector     A mixture of any            A Send             If the connector is scoped (that is,
source        Exchange 2013 or later      connector,         restricted to transport servers in the same
server        Mailbox servers or          Delivery Agent     Active Directory site), then only other
              Exchange 2010 Hub           connector, or      transport servers in that site are aware of
              Transport servers that      Foreign            the connector, and can use the connector
              are defined as source       connector.         to route mail.
              transport servers for the                      If the connector isn't scoped, then all
              connector.                                     transport servers in the entire Active
                                                             Directory forest are aware of the
                                                             connector, and can use the connector to
                                                             route mail.

Server list   The Exchange 2013 or        The distribution   none
              later Mailbox server or     group expansion
              Exchange 2010 Hub           server.
              Transport server that's
              defined as the expansion
              server for the
              distribution group.

AD site       Any mixture of Exchange     None. The          This delivery group type is the only
              2013 or later Mailbox       message must       routing scenario in Exchange 2013 or later
              servers or Exchange         travel through     where delayed fan-out is still used.
                                          the Active         Delayed fan-out attempts to reduce the

<!-- p.1647 -->

 Delivery     Delivery group             Routing             Comments
 group type                              destination

              2010 Hub Transport         Directory site on   number of message transmissions when
              servers that exist in:     the way to the      multiple routing destinations share part of
                    Active Directory     actual routing      the least-cost routing path.
                    sites that are       destination.
                    configured as hub                        Hub sites are used only if the Active
                    sites.                                   Directory site exists along the least-cost
                    Active Directory                         routing path for the message. br/> For
                    sites that have                          Edge Transport servers, the Transport
                    subscribed Edge                          service on any Mailbox server in the
                    Transport servers.                       subscribed Active Directory site is able to
                                                             send messages to the Edge Transport
                                                             server, regardless of whether that server
                                                             participates in EdgeSync synchronization.
                                                             For more information, see Edge Transport
                                                             servers.

  ７ Note

  Delivery group membership isn't mutually exclusive. For example, a Mailbox server that's a
  member of a DAG can also be the source transport server of a Send connector. The
  Mailbox server belongs to the routable DAG delivery group for the mailbox databases in
  the DAG, and the connector source server delivery group for the Send connector.

Queues
From the perspective of the sending transport server, each message delivery queue represents
the destination for a particular message. When the Transport service selects the destination for
a message, the destination is stamped on the recipient as the NextHopSolutionKey attribute. If
a single message is sent to more than one recipient, each recipient has the
NextHopSolutionKey attribute. The receiving transport server also performs message
categorization and queues the message for delivery. After a message is queued, you can
examine the delivery type for a particular queue to determine whether a message will be
relayed again when it reaches the next hop destination. Every unique value of the
NextHopSolutionKey attribute corresponds to a separate message delivery queue.

For more information, see NextHopSolutionKey.

Routing messages

<!-- p.1648 -->

When a message needs to be delivered to a remote delivery group, a routing path must be
determined for the message. Exchange uses the following logic to select the routing path for a
message. This logic is basically unchanged from Exchange 2010:

   1. Calculate the least-cost routing path by adding the cost of the IP site links that must be
     traversed to reach the destination. If the destination is a connector, the cost assigned to
     the address space is added to the cost to reach the selected connector. If multiple routing
     paths are possible, the routing path with the lowest aggregate cost is used.

     Note: Size limits on connectors are a factor here. Connectors that are configured with
     message size limits smaller than the size of the message are eliminated from
     consideration. For more information, see Connector selection in external message
     routing.

   2. If more than one routing path has the same aggregate cost, the number of hops in each
     path is evaluated and the routing path with the least number of hops is used.

   3. If more than one routing path is still available, the name assigned to the Active Directory
     sites before the destination is considered. The routing path where the Active Directory
     site nearest the destination is lowest in alphanumeric order is used. If the site nearest the
     destination is the same for all routing paths being evaluated, an earlier site name is
     considered.

In Exchange 2010, each message recipient is associated with only one Active Directory site, and
there is only one least cost routing from the source Active Directory site to the destination site.
In Exchange 2013 or later, a delivery group might span multiple Active Directory sites, and
there might be multiple least-cost routing paths to those sites. Exchange designates a single
Active Directory site in the destination delivery group as the primary site. The primary site is
closest Active Directory site based on the routing logic described earlier. To successfully route
messages between delivery groups, Exchange takes the following issues into consideration:

     The presence of one or more hub sites along the least-cost routing path: If the least-
     cost routing path to the primary site contains any hub sites, the message must be routed
     through the hub sites. The closest hub site along the least-cost routing path is selected as
     a new delivery group of the type AD site, which includes all transport servers in the hub
     site. After the message traverses the hub site, routing of the message along the least-cost
     routing path continues. If the primary site happens to be a hub site, the primary site is still
     considered a hub site for the following reasons:

        If the destination delivery group spans multiple Active Directory sites, the source server
        should only attempt to connect to the servers in the hub site.

        The servers in the hub site that belong to the target delivery group are preferred.

<!-- p.1649 -->

           As in previous version of Exchange, hub sites that aren't in the least-cost routing path
           to the primary site are ignored.

        The target Exchange server to select in the destination routing group: When the
        destination delivery group spans multiple Active Directory sites, the routing path to
        specific servers within the delivery group might have different costs. Servers located in
        the closest Active Directory site are selected as the target servers for the delivery group
        based on the least-cost routing path, and the Active Directory site those servers are in is
        selected as the primary site.

        Fallback options when connection attempts to all servers in the destination routing
        group fail: If the destination delivery group spans multiple Active Directory sites, the first
        fallback option is all other servers in the destination delivery group in other Active
        Directory sites that aren't selected as target servers. Server selection is based on the least-
        cost routing path to the other Active Directory sites. If the destination delivery group has
        any servers in the local Active Directory site, there are no other fallback options because
        the message is already as close to the target routing destination as possible. If the
        destination delivery group has servers in remote Active Directory sites, the option is to try
        to connect to all other servers in the primary site.

Routing messages between Active Directory sites
The way that Exchange routes messages between Active Directory sites is virtually the same as
Exchange 2010. For more information, see Route Mail Between Active Directory Sites.

Routing in the Front End Transport service on Mailbox servers
The Front End Transport service acts as a stateless proxy for all inbound and (optionally)
outbound external SMTP traffic for the Exchange organization. For outgoing messages, the
Transport service communicates with the Front End Transport service only when it's specifically
configured to do so. For more information, see Configure Send connectors to proxy outbound
mail.

For incoming messages, the Front End Transport service must quickly find a single, healthy
Transport service to receive the message transmission, regardless of the number or type of
recipients. Failure to do so results in the email service being perceived as unavailable by the
sending server. Like the Transport service, the Front End Transport service loads routing tables
based on information from Active Directory, and uses delivery groups to determine how to
route messages. However, the routing tables used by the Front End Transport service have the
following unique characteristics:

<!-- p.1650 -->

     The Front End Transport service is never considered a member of a delivery group, even
     when the Mailbox server and the Client access server are installed on the same physical
     server (which is always the case in Exchange 2016 or later). This forces the Front End
     Transport service to communicate only with the Transport service.

     The routing tables don't contain any Send connector routes.

     The routing tables contain a special list of Mailbox servers in the local Active Directory site
     for fast fail-over purposes.

Routing in the Front End Transport service resolves message recipients to mailbox databases.
The list of Mailbox servers used by the Front End Transport service is based on the mailbox
databases of the message recipients. Note that it's possible that none of the recipients have
mailboxes, for example, if the recipient is a distribution group or a mail user. For each mailbox
database, the Front End Transport service looks up the delivery group and the associated
routing information. The delivery groups used by the Front End Transport service are:

     Routable DAG

     Mailbox delivery group

     AD site

Depending on the number and type of recipients, the Front End Transport service performs one
of the following actions:

     For messages with a single mailbox recipient, select a Mailbox server in the target delivery
     group, and give preference to the Mailbox server based on the proximity of the Active
     Directory site. Routing the message to the recipient might involve routing the message
     through a hub site.

     For messages with multiple mailbox recipients, use the first 20 recipients to select a
     Mailbox server in the closest delivery group, based on the proximity of the Active
     Directory site. Note that message bifurcation doesn't occur in Front End Transport, so only
     one Mailbox server is ultimately selected, regardless of number of recipients in a
     message.

     If the message has no mailbox recipients, select a random Mailbox server in the local
     Active Directory site.

Routing in the Mailbox Transport service on Mailbox servers
The Mailbox Transport service consists of two separate services: the Mailbox Transport
Submission service and Mailbox Transport Delivery service. The Mailbox Transport Delivery

<!-- p.1651 -->

service receives SMTP messages from the Transport service, and connects to the local mailbox
database by using RPC to deliver the message. The Mailbox Transport Submission service
connects to the local mailbox database by using RPC to retrieve messages, and submits the
messages over SMTP to the Transport service. The Mailbox Transport service is stateless, and
doesn't use message delivery queues.

Like the Transport service, the Mailbox Transport service loads routing tables based on
information from Active Directory, and uses delivery groups to determine how to route
messages. However, there are routing aspects that are unique to the Mailbox Transport service:

     Because the Transport service and the Mailbox Transport service exist on the same
     Mailbox server, the Mailbox Transport service always belongs to the same delivery group
     as the Mailbox server. This delivery group is referred to as the local delivery group.

     The Mailbox Transport Submission service doesn't automatically send messages to the
     Transport service on the local Mailbox server or on other Mailbox servers in its own local
     delivery group. The Mailbox Transport Submission service has access to the same routing
     topology information as the Transport service, so the Mailbox Transport submission
     service can send messages to the Transport service on Mailbox servers outside the
     delivery group. The Mailbox servers in the local delivery group are used as fallback
     options, and for delivery to non-mailbox recipients.

     The Mailbox Transport service only communicates with the Transport service on Mailbox
     servers.

     The Mailbox Transport service only communicates with local mailbox databases. The
     Mailbox Transport service never communicates with mailbox databases on other Mailbox
     servers.

When a user sends a message from their mailbox, the Mailbox Transport Submission service
resolves the message recipients to mailbox databases. The list of Mailbox servers used by the
Mailbox Transport Submission service is based on the mailbox databases of the message
recipients. Note that it's possible that none of the recipients have mailboxes, for example, if the
recipient is a distribution group or a mail user. For each mailbox database, the Mailbox
Transport Submission service looks up the delivery group and the associated routing
information. The delivery groups used by the Mailbox Transport Submission service are:

     Routable DAG

     Mailbox delivery group

     AD site

<!-- p.1652 -->

Depending on the number and type of recipients, the Mailbox Transport Submission service
performs one of the following actions:

     For messages with a single mailbox recipient, select a Mailbox server in the target delivery
     group, and give preference to the Mailbox server based on the proximity of the Active
     Directory site. Routing the message to the recipient might involve routing the message
     through a hub site.

     For messages with multiple mailbox recipients, use the first 20 recipients to select a
     Mailbox server in the closest delivery group, based on the proximity of the Active
     Directory site.

     If the message has no mailbox recipients, select a Mailbox server in the local delivery
     group.

When the Mailbox Transport Delivery service receives a message from the Transport service, it
accepts or rejects the message for delivery to a local mailbox database. The Mailbox Transport
Delivery service can deliver the message if the recipient resides in an active copy of a local
mailbox database. But, if the recipient doesn't reside in an active copy of a local mailbox
database, the Mailbox Transport Delivery service can't deliver the message, and must provide a
non-delivery response to the Transport service. For example, if the active copy of the mailbox
database recently moved to another server, the Transport service might erroneously transmit a
message to a Mailbox server that now holds an inactive copy of the mailbox database. The
non-delivery responses that the Mailbox Transport Delivery service returns to the Transport
service include:

     Retry delivery

     Generate an NDR (also known as a non-delivery report, delivery status notification, DSN,
     or bounce message)

     Reroute the message

Routing in the Transport service on Edge Transport servers
The Transport service on Edge Transport servers provides SMTP relay and smart host services
for all Internet mail flow. Messages that come and go from the Internet are stored in message
delivery queues on the Edge Transport server. The queues correspond to external domains or
Send connectors. For more information, see NextHopSolutionKey.

Typically, when you install an Edge Transport server in your perimeter network, you subscribe
the Edge Transport server to an Active Directory site. The Active Directory site contains the
Mailbox servers that relay messages to and from the Edge Transport server. The Edge

<!-- p.1653 -->

Subscription process creates an Active Directory site membership affiliation for the Edge
Transport server. The site affiliation enables the Mailbox servers in the Active Directory site to
relay messages to the Edge Transport server without having to configure explicit Send
connectors.

In organizations that have Exchange servers in multiple Active Directory sites, outbound mail
from internal recipients to external recipients is first routed to the subscribed Active Directory
site. Transport servers in the target Active Directory site are the delivery group. The routing
destination is the intra-organization Send connector in the Transport service on any of the
Mailbox servers in the subscribed Active Directory site. The intra-organization Send connector is
special Send connector that exists in the Transport service on every Mailbox server. This Send
connector is implicitly created, invisible, requires no management, and is used to relay
messages between Exchange servers.

For more information about how mail is routed to and from Edge Transport servers, see Mail
flow and the transport pipeline.

<!-- p.1654 -->

Connector selection in external message
routing
Article • 04/30/2025

APPLIES TO:        2016        2019      Subscription Edition

Like previous versions of Exchange, Exchange Server 2016 and Exchange Server 2019 use
connectors to deliver messages to external recipients (recipients that don't exist in the
Exchange organization). Exchange uses Send connectors to route messages to external SMTP
domains. If the external recipient isn't on an SMTP messaging system, Exchange uses Delivery
Agent connectors or Foreign connectors.

For more information about the different types of connectors, see Connectors. For more
information about how Exchange makes routing decisions, see Mail routing.

Connector considerations in message routing
The settings that are configured on connectors might eliminate an otherwise available
connector from routing consideration. These settings are described in the following table:

                                                                                           ﾉ   Expand table

 Connector       Comments
 setting

 State           Only enabled connectors are used in routing decisions. If a connector is disabled, it's not
 (enabled or     considered when routing messages.
 disabled)

 Address         The address spaces defines the destination domains or other address spaces that are
 space           serviced by the connector. When Exchange selects a connector for routing a message, it
                 only considers connectors that have a matching address space. If more than one
                 connector matches the destination address space, the connector with the more precise
                 address match is selected.

                 For example, suppose the recipient is julia@marketing.contoso.com, and separate Send
                 connectors are configured for *, *.contoso.com and marketing.contoso.com. The order of
                 connector preference based solely on the address space is:

                       1. marketing.contoso.com
                       2. *.contoso.com
                       3. *

<!-- p.1655 -->

 Connector         Comments
 setting

 Address           By default, the address space type on a new Send connector is SMTP. If you specify a
 space type        non-SMTP address space, the messages are still sent to the destination (a smart host) by
                   using SMTP. You need to create a Delivery Agent connector or a Foreign connector to
                   route non-SMTP messages to non-SMTP messaging servers without using SMTP.

 Address           You use the cost value on the address space for mail flow optimization and fault tolerance
 space cost        when the same address space is configured on multiple connectors. A lower cost value
                   indicates a preferred connector.

 Source server     At least one Mailbox server or Edge Transport server must be configured to host the
                   connector. You can configure multiple source servers to provide load balancing and fault
                   tolerance for the address spaces that are defined on the connector.

 Scope             The connector's scope controls its visibility within the Exchange organization.

                   By default, connectors are visible to all the Exchange servers in the entire Active Directory
                   forest. However, you can limit the scope of a connector so that it's only visible to other
                   Exchange servers in the local Active Directory site. The connector is invisible to Exchange
                   servers in other Active Directory sites, and isn't used in their routing decisions. A
                   connector that's restricted in this way is said to be scoped.

 Message size      A message size restriction on a connector can eliminate the connector from selection if
 limits            the message is larger than the maximum size that's allowed on the connector.

                   For more information about message size limits on connectors, see Connector limits.

Selecting the connector for an external recipient
For messages that are sent to external recipients, Exchange must select the best connector to
route the message through. The decisions that are required to select this connector are
described in the following list:

   1. Exchange eliminates all connectors that have a message size limit that's smaller than the
      size of the message.

   2. Exchange narrows the list of remaining connectors to those that satisfy all of the
      following criteria:

              The connector is scoped to another Exchange server in the local Active Directory
              site, or isn't scoped at all (is available to all Exchange in the Active Directory forest).

              The connector is enabled.

<!-- p.1656 -->

           The connector is configured with an address space that matches the recipient's
           email address.

   3. From the resulting list of connectors, Exchange selects the connector with the most
     specific address space match. If multiple connectors have the same address space
     specificity, Exchange uses the following criteria to select a connector:

      a. Aggregate cost: This is the sum of the cost that's assigned to all the IP site links
        between the source Active Directory site and the Active Directory site that contains the
        source servers for the connector, and the cost that's assigned to the address space on
        the connector (IP site link costs + connector cost). The connector with the lowest
        aggregate cost is selected. If multiple connectors have the same aggregate cost, the
        selection process continues to the next step.

      b. Hop count: The source server for the connector that can be reached in the least
        number of hops is selected. Typically, this means the general order of preference is:

          i. The local Exchange server.

         ii. An Exchange server in the same Active Directory site.

        iii. An Exchange server in a remote Active Directory site.

        If multiple connectors have the same hop count, the selection process continues to the
        next step.

      c. Connector name: If more than one routing path has the same aggregate cost and hop
        count, the connector with the name that has the lowest alphanumeric value is selected.

Handling messages that can't be routed
If no connector satisfies all of the selection criteria, one of the following actions occurs:

     If there is no matching connector for an SMTP address space, the recipient is marked as
     unreachable and the message is routed to the Unreachable queue. For more information
     about the Unreachable queue, see Types of queues.

     If there is no matching connector for a non-SMTP address space, a non-delivery report
     (also known as an NDR or bounce message) is returned to the sender.

     If the message size exceeds the connector size restriction for all connectors, an NDR is
     returned to the sender.

<!-- p.1657 -->

Recipient resolution in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016       2019    Subscription Edition

Recipient resolution is when the Exchange server expands and resolves all recipients in a
message. Recipient resolution is responsible for these actions:

      Matching the recipient to the corresponding Active Directory object.

      Expanding distribution groups into a list of individual recipients.

      Applying message limits and any alternative recipients to each recipient.

Recipient resolution in Exchange 2016 or Exchange 2019 is basically unchanged from Exchange
2013. Recipient resolution is done by the categorizer in the Transport service on Mailbox
servers. Each message is processed by the categorizer after the message is put in the
Submission queue, but before the message is put in a delivery queue. The component of the
categorizer that's responsible for recipient resolution is frequently called the resolver. For more
information about the categorizer and the Submission queue, see Understanding the Transport
service on Mailbox servers.

This topic explains the various stages and components of recipient resolution that occur on the
Exchange server.

Top-level resolution
Top-level resolution is the first stage of recipient resolution that associates each recipient in an
incoming message to a matching recipient object in Active Directory. The categorizer creates a
list that contains the sender and the initial, unexpanded recipient email addresses from the
message, and uses that list to query Active Directory. When a match is found in the email
address properties for mail-enabled Active Directory objects, the categorizer caches the
properties of the objects, and enforces any sender message restrictions.

Recipient email addresses
Top-level resolution begins with a message and the initial, unexpanded list of recipients from
the message envelope. The message envelope contains the SMTP commands that are used to
transmit messages between messaging servers:

      The sender's email address is contained in the MAIL FROM command.
      Each recipient's email address is contained in a separate RCPT TO command.

<!-- p.1658 -->

The envelope sender and envelope recipients are typically created from the sender and
recipients in the To: , From: , Cc: , and Bcc: header fields in the message header. However,
these header fields are easily forged and may not match the actual sender or recipient email
addresses that were used to transmit the message.

Encapsulated email addresses

Standard SMTP email addresses follow the specifications in RFC 5321 and RFC 5322 (for
example chris@contoso.com). However, an email address can also be a non-SMTP address
that's encapsulated in an SMTP address. Exchange supports the Internet Mail Connector
Encapsulated Address (IMCEA) encapsulation method that replaces characters that would be
invalid in an SMTP email address with valid characters.

IMCEA addresses use the syntax IMCEA<Type>-<address>@<domain> :

     <Type> identifies the type of non-SMTP address (for example EX , X400 , or FAX ).
     Although SMTP and X500 are theoretically valid values for <Type>, Exchange recipient
     resolution rejects any IMCEA-encoded addresses that use either of these types.
     <address> is the encoded version of original address:
        Alphanumeric characters, the equal sign (=) and the hyphen (-) aren't replaced.
        Forward slashes (/) are replaced by underscores (_).
        Other US-ASCII characters are replaced by a plus sign (+) and the two digits of the
        ASCII value in hexadecimal (for example, the space character has the encoded value
        +20 ).

     <domain> is SMTP domain that's used to encapsulate the non-SMTP address (for
     example, contoso.com).

IMCEA addresses are returned to their original values (unencapsulated) only when the domain
matches the default accepted domain in the Exchange organization. For more information
about the default accepted domain, see Default domain.

The maximum length for an SMTP email address in Exchange is 571 characters. This limit
includes:

     315 characters for the name part of the address
     255 characters for the domain name
     The at sign (@) character that separates the name from the domain name

Exchange doesn't support IMCEA-encoded messages where the name part of the address
exceeds 315 characters, even if the complete email address is less than 571 characters.

Address resolution

<!-- p.1659 -->

For each message, the sender's email address and all recipient addresses are added to a list
that's used to query Active Directory. Any encapsulated addresses are unencapsulated before
they're added to the list. The Active Directory query is performed on up to 20 email addresses
at a time. If the query encounters transient errors, the message is returned to the Submission
queue and deferred for the time that's specified by the ResolverRetryInterval key in the
%ExchangeInstallPath%Bin\EdgeTransport.exe.config XML application configuration file that's

associated with the Transport service. The default value is 30 minutes.

The Active Directory recipient objects that are used by Exchange are described in the following
table. For more information about Exchange recipient types, see Recipients.

                                                                                        ﾉ    Expand table

 Active Directory recipient   Description
 type

 DistributionGroup            Any mail-enabled group object. The distribution group object types are:
                                    MailUniversalDistributionGroup: A universal distribution group
                                    object
                                    MailUniversalSecurityGroup: A universal security group (USG)
                                    object that has an email address

 DynamicDistributionGroup     An object that has the Active Directory class
                              msExchDynamicDistributionList. For more information, see Manage
                              dynamic distribution groups.

 Mailbox                      An object that has an email address and a defined Database parameter.

 MailUser                     A user object that has an email address without a defined Database
                              parameter. For more information, see Manage mail users.

 MailContact                  A contact object that has an email address. Typically, a mail contact is
                              used for recipients outside the Exchange organization. A mail contact is
                              also used in cross-forest Exchange environments. For more information,
                              see Manage mail contacts.

 MailPublicFolder             A public folder object that has an email address. For more information,
                              see Public folders.

 MicrosoftExchangeRecipient   An object that has the Active Directory class
                              msExchExchangeServerRecipient. For more information about the
                              Exchange recipient object, see Recipients.

 SystemMailbox                A user object that has an email address and is located in the Microsoft
                              Exchange System Objects container. There should be one system mailbox
                              for each mailbox database in the Exchange organization.

<!-- p.1660 -->

The Active Directory query classifies an object with missing or malformed critical properties as
an invalid object (for example, a dynamic distribution group object without an email address).
Messages sent to recipients that are classified as invalid objects generate a non-delivery report
(also known as an NDR or bounce message).

For each email address, the categorizer does a single initial query for all possible recipient
properties (for example, the recipient identifiers, recipient type, message limits, email
addresses, and alternative recipients). The applicable recipient properties are cached for later
use. Recipient resolution classifies recipients based on similarities in how the recipients are
resolved, and the similarity of the applicable recipient properties.

The LDAP filter that's used for address resolution depends on the recipient's email address:

     For the EX email address type, the LDAP filter is based on the recipient's
     legacyExchangeDN attribute (higher priority) or the recipient's proxyAddresses attribute
     (lower priority).
     For all other email addresses types, the recipient proxyAddresses attribute is used as the
     LDAP filter.

If the email address doesn't match the recipient's primary SMTP address, the categorizer
rewrites the email address in the message to match the primary SMTP address. The original
email address is saved in the ORCPT= entry in the RCPT TO command in the message envelope.

Sender message restrictions
The size of a message can change because of content conversion, encoding, and agent
processing. When a message enters the Exchange organization, the original size of the
message is recorded in the X-MS-Exchange-Organization-OriginalSize: header field in the
message header. The lower value of the current message size or the original message size is
used to enforce sender message size limits. If the original message size header field doesn't
exist, it's created using the current size of the message. If the message is too large, it's returned
to the sender in an NDR, and additional message processing is stopped.

The sender recipient limit is only enforced in the Transport service on the first Mailbox server
that processes the message. The original, unexpanded message envelope recipient count is
compared to the sender recipient limit.

The message sender and all recipients are marked as resolved by stamping an extended
property in the message. This extended property allows the message to bypass top-level
resolution if the message goes through recipient resolution again (for example, because the
Exchange Transport service restarted.

<!-- p.1661 -->

Expansion
Expansion occurs after top-level resolution. Expansion completely expands nested levels of
recipients into individual recipients. Expansion may require multiple trips through the
expansion process to expand all recipients. Not all recipients have to be expanded. However, all
recipients go through the expansion process to enforce recipient message restrictions for all
kinds of recipients.

The types of recipients that require expansion are described in this list:

        Distribution groups and dynamic distribution groups: Distribution groups are expanded
        based on the memberOf Active Directory property. Dynamic distribution groups are
        expanded by using the Active Directory query definition. If the ExpansionServer parameter
        is set on the group in the Exchange Management Shell, the group is routed to the
        specified server for expansion.

        Note: When you specify an expansion server for a group, the group becomes dependent
        on the availability of the expansion server (messages can't be delivered to the group if the
        expansion server is unavailable). Therefore, consider implementing high availability
        solutions for expansion servers.

        Alternative recipients: You can configure mailboxes and mail-enabled public folders to
        forward messages to other recipients:

          Mailboxes: You can configure forwarding to another recipient in the Exchange
          organization, or to an external email address. For more information, see Configure
          email forwarding for a mailbox.

          Mail-enabled public folders: You can configure forwarding to another recipient in the
          Exchange organization.

          You can configure the mailbox or mail-enabled public folder to only send messages to
          the forwarding address, or to the forwarding address and the original recipient.

        Contact chains: A contact chain is a mail user or mail contact where the external email
        address is set to the email address of another recipient in the Exchange organization.

Recipient loop detection
As groups, alternative recipients, and contacts chains are expanded, the categorizer checks for
recipient loops. A recipient loop is a configuration problem that causes message delivery to the
same recipients in an endless circle. The different types of recipient loops are described in this
list:

<!-- p.1662 -->

     Harmless recipient loop: These are the two scenarios when harmless recipient can loops
     occur:
        When two groups contain one another as members.
        When mailboxes or mail-enabled public folders are set to deliver and forward to one
        another (the message is delivered to the original recipient and forwarded).

     When the categorizer detects a harmless recipient loop, the message is delivered to the
     recipient, but no additional attempts are made to deliver the message to the same
     recipient.

     Broken recipient loop: When mailboxes or mail-enabled public folders are set to forward
     to one another (the messages are only forwarded).

     A broken recipient loop can't result in successful message delivery. When the categorizer
     detects a broken recipient loop, expansion activity for the current recipient stops, and an
     NDR is generated.

Recipient loop detection doesn't prevent duplicate message delivery. For example, consider
this scenario:

     Distribution Group A has Distribution Group B and Distribution Group C as members.
     Distribution Group C is also a member of Distribution Group B.

In this scenario, Distribution Group C will experience duplicate message delivery.

Delivery report redirection for groups
When a group is expanded, the message type is checked to see if it's a delivery report
message. If the message is a delivery report, the redirection settings of the group are checked
to see if redirection of the delivery report is required. You may want to suppress delivery
reports for the group because a delivery report might disclose unwanted information about the
membership of the group.

The delivery report redirection settings that are available in the Exchange Management Shell
for distribution groups and dynamic distribution groups are described in this list:

     ReportToManagerEnabled parameter: Enables or disables sending delivery reports to the
     group manager. Valid values are $true or $false . The default value is $false . For a
     distribution group, the manager is controlled by the ManagedBy parameter on the Set-
     Group (distribution groups), or Set-DynamicDistributionGroup (dynamic distribution
     groups) cmdlets.

     ReportToOriginatorEnabled parameter: Enables or disables sending delivery reports to
     the message sender for messages that are sent to the group. Valid values are $true or

<!-- p.1663 -->

      $false . The default value is $true .

     Note: The values of ReportToManagerEnabled parameter and ReportToOriginatorEnabled
     can't both be $true . If one parameter is set to $true , the other must be set to $false .
     The values of both parameters can be $false , which suppresses the redirection of all
     delivery report messages for the group.

The different types of delivery report messages that can be affected by delivery report
redirection for groups are described in this list:

     Delivery receipt (DR): Confirms that a message was delivered to its intended recipient.

     Delivery status notification (DSN): Describes the result of an attempt to deliver a
     message that didn't result in the message being returned to the sender in an non-delivery
     report (NDR). For more information about DSN messages, see DSNs and NDRs in
     Exchange Server.

     Message disposition notification (MDN): Describes the status of a message after it has
     been successfully delivered to a recipient. Read notifications (RNs) and non-read
     notification (NRNs) are both examples of MDN messages. MDN messages are defined in
     RFC 2298 and are controlled by the Disposition-Notification-To: header field in the
     message header. MDN settings that use this header field are compatible with many
     different kinds of messaging servers. MDN settings can also be defined by using MAPI
     properties in Outlook and Exchange.

     Non-delivery report (NDR): Indicates to the message sender that the message couldn't
     be delivered to the specified recipients. The message is returned to the sender in the
     NDR.

     Non-read notification (NRN): Indicates that a message was deleted before it was read.

     Out of office (OOF): Indicates that the recipient won't respond to email messages. The
     acronym OOF dates back to the original Microsoft messaging system where the
     corresponding notification was named "out of facility."

     Read notification (RN): Indicates that a message was read.

     Recall Report: Indicates the status of a recall request for a specific recipient (the sender
     tried to recall a sent message by using Outlook).

These are the settings that cause delivery report messages to be deleted when they're sent to a
group:

     Report redirection isn't configured for the group, or report redirection is set to the
     message sender.

<!-- p.1664 -->

     Report redirection is set to the group manager, and the delivery report message isn't an
     NDR.

If report redirection is set to the group manager, and the delivery report message is an NDR,
the message is delivered to the group manager.

The affect of group delivery report redirection settings on regular messages that contain report
requests are described in this list:

     If report redirection is set to the message sender, the report request settings aren't
     modified.
     If report redirection isn't configured for the group, all report requests are suppressed. The
      NOTIFY=NEVER entry is added to RCPT TO for each recipient in the message envelope.

     If report redirection is set to the group manager, NDRs are sent to the group manager,
     but all other report requests are suppressed.

Message restrictions on recipients
The expansion process also enforces any message restrictions that are configured on
recipients. These restrictions may be configured individually for each recipient or
organizationally for all servers in the Exchange organization.

For more information on message size limits, see Recipient limits and Organizational limits.

                                                                                    ﾉ   Expand table

 Restriction   EAC                  Exchange Management Shell configuration      Description
               configuration

 Maximum       Organization:        Organization cmdlet: Set-TransportConfig     Specifies the
 size of a     Mail flow >                                                       maximum size of a
 message       Receive              Recipient cmdlets: Set-DistributionGroup,    message, which
 received      connectors >         Set-DynamicDistributionGroup, Set-Mailbox,   includes the
               More options         Set-MailContact, Set-MailPublicFolder, and   message header, the
               > Organization       Set-MailUser                                 message body, and
               transport settings                                                any attachments.
                                    Parameter: MaxReceiveSize
               > Limits tab >                                                    Whenever Exchange
               Maximum receive                                                   checks the message
               message size                                                      size, the lower value
               (MB)                                                              of the current
                                                                                 message size or the
               Mailboxes:                                                        original message
               Recipients >                                                      size (the X-MS-
               Mailboxes >                                                       Exchange-
               select the mailbox                                                Organization-
               > Edit     >                                                      OriginalSize:

<!-- p.1665 -->

Restriction    EAC                  Exchange Management Shell configuration       Description
               configuration

               Mailbox features                                                   message header) is
               > Mail flow                                                        used. The size of the
               section >                                                          message can change
               Message size                                                       because of content
               restrictions                                                       conversion,
               section > View                                                     encoding, and
               details >                                                          transport agent
               Received                                                           processing.
               messages section
               > Maximum                                                          Note: The specified
               message size (KB)                                                  maximum message
                                                                                  size is inflated by
               Mail users:                                                        approximately 33%
               Recipients >                                                       to account for
               Contacts > select                                                  Base64 encoding
               the mail user >                                                    (for example, the
               Edit     > Mail                                                    specified value 64
               flow settings >                                                    MB results in a
               Message size                                                       realistic maximum
               restrictions                                                       message size of
               section > View                                                     approximately 48
               details >                                                          MB).
               Received
               messages section                                                   For more
               > Maximum                                                          information, see
               message size (KB)                                                  Message size and
                                                                                  recipient limits in
                                                                                  Exchange Server.

The            Mailboxes:           Cmdlets: New-DistributionGroup, Set-          You can configure
recipient      Recipients >         DistributionGroup, Set-                       the recipient to only
can only       Mailboxes >          DynamicDistributionGroup, Set-Mailbox,        accept messages
accept         select the mailbox   Set-MailContact, Set-MailPublicFolder, Set-   from authenticated
messages       > Edit     >         MailUser, and Set-RemoteMailbox               (internal) senders, or
from           Mailbox features                                                   to accept messages
internal       > Mail flow          Parameter:                                    from authenticated
senders, and   section >            RequireSenderAuthenticationEnabled            and unauthenticated
must reject    Message delivery                                                   (external) senders.
messages       restrictions
from           section > View
external       details > Accept
senders        messages from
               section > check or
               uncheck Require
               that all senders
               are authenticated

<!-- p.1666 -->

Restriction   EAC                  Exchange Management Shell configuration   Description
              configuration

              Remote
              mailboxes:
              Recipients >
              Mailboxes >
              select the
              Microsoft 365 or
              Office 365
              mailbox > Edit
              > Mail flow
              settings >
              Message delivery
              restrictions
              section > View
              details > Accept
              messages from
              section > check or
              uncheck Require
              that all senders
              are authenticated

              Mail users:
              Recipients >
              Contacts > select
              the mail user >
              Edit     > Mail
              flow settings >
              Message delivery
              restrictions
              section > View
              details > Accept
              messages from
              section > check or
              uncheck Require
              that all senders
              are authenticated

              Groups:
              Recipients >
              Groups > select
              the group > Edit
                  > Delivery
              management >
              select Only
              senders inside
              my organization
              or Senders inside

<!-- p.1667 -->

Restriction     EAC                  Exchange Management Shell configuration       Description
                configuration

                and outside of
                my organization

Senders         Mailboxes:           Cmdlets: Set-DistributionGroup, Set-          The categorizer
who are         Recipients >         DynamicDistributionGroup, Set-Mailbox,        checks the recipient
allowed or      Mailboxes >          Set-MailContact, Set-MailPublicFolder, Set-   permission in two
aren't          select the mailbox   MailUser, and Set-RemoteMailbox               passes. The first pass
allowed to      > Edit     >                                                       determines whether
send            Mailbox features     Accept parameters:                            the sender is present
messages to     > Mail flow          AcceptMessagesOnlyFromSendersOrMembers        in the accept or
the recipient   section >            (or AcceptMessagesOnlyFrom for individual     reject lists. If the
                Message delivery     recipients only and                           sender isn't found in
                restrictions         AcceptMessagesOnlyFromDLMembers for           either list, the
                section > View       group members only)                           distribution groups
                details > Accept                                                   in those parameters
                                     Reject parameters:
                messages from                                                      are fully expanded.
                                     RejectMessagesFromSendersOrMembers (or
                section: All                                                       This complete group
                                     RejectMessagesOnlyFrom for individual
                senders or Only                                                    expansion might
                                     recipients only and
                senders in the                                                     take some time, so
                                     RejectMessagesOnlyFromDLMembers for
                following list or                                                  we recommend that
                                     group members only)
                Reject messages                                                    you minimize the
                from section: No                                                   depth of nested
                senders or                                                         groups in the accept
                Senders in the                                                     or reject lists.
                following list

                Remote
                mailboxes:
                Recipients >
                Mailboxes >
                select the
                Microsoft 365 or
                Office 365
                mailbox > Edit
                > Mail flow
                settings >
                Message delivery
                restrictions
                section > View
                details > Accept
                messages from
                section: All
                senders or Only
                senders in the
                following list or
                Reject messages
                from section: No

<!-- p.1668 -->

 Restriction   EAC                  Exchange Management Shell configuration   Description
               configuration

               senders or
               Senders in the
               following list

               Mail users:
               Recipients >
               Contacts > select
               the mail user >
               Edit    > Mail
               flow settings >
               Message delivery
               restrictions
               section > View
               details > Accept
               messages from
               section: All
               senders or Only
               senders in the
               following list or
               Reject messages
               from section: No
               senders or
               Senders in the
               following list

               Groups:
               Recipients >
               Groups > select
               the group > Edit
                  > Delivery
               management >
               click Add       or
               Remove         to
               specify users or
               group members
               who can send to
               the group
               (messages from
               others senders
               are rejected).

Certain types of messages that are sent by authenticated senders are exempt from restrictions.
The following list describes the messages that are exempt from recipient restrictions:

     Messages sent by the Microsoft Exchange recipient: These messages include DSNs and
     NDRs , journal reports, quota messages, and other system-generated messages that are

<!-- p.1669 -->

     sent to internal message senders. For more information about the Microsoft Exchange
     recipient, see Recipients.
     Messages sent by the external postmaster address: These messages include DSNs and
     NDRs, and other system-generated messages that are sent to external message senders.
     For more information about the external postmaster address, see Managing the External
     Postmaster Address.

Exchange blocks certain types of messages that are sent to external domains (for example,
internal OOF messages, automatic replies, and meeting forward notifications). You configure
these settings in remote domains (the default remote domain, or remote domains for specific
external domains). For more information, see Managing Remote Domains.

Bifurcation and controlling recipient expansion
Because the complete list of message recipients is expanded and resolved by recipient
resolution, there are occasions when different copies of the same message need to be created:

     Recipients require different message settings: Creating a new version of the message
     that has slightly different properties than the original is called bifurcation. For example,
     Exchange might need to bifurcate a message when read receipts are enabled for some
     recipients and blocked for others.
     Limit the number of envelope recipients in a single message: Expanding large group can
     generate thousands of individual recipients. Instead of creating a single copy of the
     message that has thousands of envelope recipients, Exchange creates multiple copies of
     the same message that have a limited number of recipients in the message envelope.

Bifurcation
Recipient resolution bifurcates a message if the following conditions are true:

     When the message sender in MAIL FROM in the message envelope is updated (for
     example, when the ReportToManagerEnabled parameter on a group has the value $true ).
     When auto-response messages (for example, DSNs and NDRs, OOF messages, and recall
     reports) need to be suppressed.
     When alternative recipients are expanded.
     When a Resent-From: header field is added to the message header. Resent header fields
     are informational header fields that can be used to determine whether a message has
     been forwarded by a user. Resent header fields are used so that the message appears to
     the recipient as if it was sent directly by the original sender. The recipient can view the
     message header to discover who forwarded the message. Resent header fields are
     defined in section 3.6.6 of RFC 5322.

<!-- p.1670 -->

     When the expansion history of the group needs to be transmitted.

Controlling recipient expansion
When the number of expanded recipients is too large, the categorizer splits the message into
multiple copies to reduce the system resources that are used during message expansion. The
maximum number of envelope recipients in a message is controlled by the ExpansionSizeLimit
key in the %ExchangeInstallPath%Bin\EdgeTransport.exe.config application configuration file.
The default value is 1000.

  Ｕ Caution

  We recommend that you don't modify the value of the ExpansionSizeLimit key on an
  Exchange transport server in a production environment.

Recipient resolution diagnostics
Exchange provides reporting and diagnostic information for recipient resolution in
performance counters, message tracking log entries, and recipient resolution logging. These
sources can help you identify and diagnose problems with recipient resolution.

Recipient resolution performance counters
The performance counters that are available for recipient resolution are described in this table.

                                                                                     ﾉ   Expand table

 Counter name                 Display        Description
                              name

 AmbiguousRecipientsTotal     Ambiguous      The total number of ambiguous recipients that were
                              Recipients     detected during recipient resolution. Ambiguous
                                             recipients are different recipients that have matching
                                             legacyExchangeDN Active Directory attributes or
                                             matching proxyAddresses Active Directory attributes.

 AmbiguousSendersTotal        Ambiguous      This is the number of ambiguous senders that were
                              Senders        detected during recipient resolution. Ambiguous senders
                                             are different senders that have matching
                                             legacyExchangeDN Active Directory attributes or
                                             matching proxyAddresses Active Directory attributes.

<!-- p.1671 -->

 Counter name                     Display        Description
                                  name

 FailedRecipientsTotal            Failed         The number of failed recipients that were detected
                                  Recipients     during recipient resolution.

 LoopRecipientsTotal              Loop           The number of recipients that failed recipient resolution
                                  Recipients     because of recipient loops.

 MessagesChippedTotal             Messages       The total number of copies of the same message that
                                  Chipped        were created during recipient resolution to control the
                                                 number of envelope recipients in a single message. This
                                                 process is referred to as chipping.

 MessagesCreatedTotal             Messages       The number of messages that were created during
                                  Created        recipient resolution.

 MessagesRetriedTotal             Messages       The number of messages that were scheduled for retry
                                  Retried        during recipient resolution.

 UnresolvedOrgRecipientsTotal     Unresolved     The number of unresolved recipients from an
                                  Org            authoritative domain that were detected during recipient
                                  Recipients     resolution.

 UnresolvedOrgSendersTotal        Unresolved     The number of unresolved senders from an authoritative
                                  Org Senders    domain that were detected during recipient resolution.

Recipient resolution events in the message tracking log
The recipient resolution events that are written in the message tracking log are described in
this table.

                                                                                         ﾉ   Expand table

 Message            Description
 tracking event

 EXPAND             A distribution group was expanded.

 REDIRECT           A message was redirected to the forwarding address that's configured on the mailbox
                    or mail-enabled public folder.

 RESOLVE            A recipient's email address was changed to the primary SMTP email address of the
                    corresponding Active Directory recipient object (in other words, the message was sent
                    to a proxy address of the recipient).

 TRANSFER           Message bifurcation or chipping occurred (for example, due to content conversion,
                    message recipient limits, or transport agents).

<!-- p.1672 -->

For more information about message tracking, see Message tracking.

Recipient resolution logging
Recipient resolution logging is controlled by the ResolverLogLevel key in the
%ExchangeInstallPath%Bin\EdgeTransport.exe.config application configuration file. Valid values

for this key are:

      Disabled : No recipient resolution data is logged. This is the default value.

      Enabled : Only message envelope data is logged.
      FullContent : Message envelope data and message header data is logged

The log files are stored at %ExchangeInstallPath%Logging\Resolver .

  ７ Note

  Any customized Exchange or Internet Information Server (IIS) settings that you made in
  Exchange XML application configuration files on the Exchange server (for example,
  web.config files or the EdgeTransport.exe.config file) will be overwritten when you install
  an Exchange CU. Be sure save this information so you can easily re-apply the settings after
  the install. After you install the Exchange CU, you need to re-configure these settings.

<!-- p.1673 -->

Transport agents in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019        Subscription Edition

Transport agents let you install custom software that is created by Microsoft, by third-party
vendors, or by your organization, on an Exchange server. This software can then process email
messages that pass through the transport pipeline. In Microsoft Exchange Server 2016 or 2019,
the transport pipeline is made of the following processes:

      The Front End Transport service on Mailbox servers
      The Transport service on Mailbox servers
      The Mailbox Transport service on Mailbox servers
      The Transport service on Edge Transport servers

For more information about the transport pipeline, see Mail flow and the transport pipeline

Exchange transport provides extensibility through the Microsoft Exchange Server Transport
Agents SDK. The Exchange version of the SDK allows third parties to implement the following
predefined classes:

      SmtpReceiveAgent
      RoutingAgent
      DeliveryAgent

When complied against libraries in the SDK, the resulting assemblies are registered with
Exchange, which loads the agents and invokes their event handlers during specific stages of
the SMTP sessions or message processing. These stages, or events, are part of the agent
definitions. The agent registration information is stored in an XML configuration file.

The following list explains the requirements for using transport agents in Exchange.

      The Transport service on Mailbox servers and Edge Transport servers fully supports all the
      predefined classes in the SDK.
      The Front End Transport service only supports the SmtpReceiveAgent class in the SDK,
      and third-party agents can't operate on the OnEndOfData SMTP event.
      The Mailbox Transport service doesn't support the SDK at all, so you can't use any third-
      party agents in the Mailbox Transport service.

Transport agent management
The transport agent cmdlets need to distinguish between the Transport service and the Front
End Transport service. Transport Agent management cmdlets manipulate the configuration file

<!-- p.1674 -->

agents.config located at %ExchangeInstallPath%TransportRoles\Shared .

For more information, see Manage transport agents in Exchange Server.

Transport agents and SMTP events
Transport agents use SMTP events. These events are triggered as messages move through the
transport pipeline. SMTP events give transport agents access to messages at specific points
during the SMTP conversation and during routing of messages through the organization.

SMTP Receive exists in the Front End Transport service on Mailbox servers, the Transport service
on Mailbox servers and Edge Transport servers, and the Mailbox Transport Delivery service on
Mailbox servers. The categorizer exists only in the Transport service on Mailbox servers and
Edge Transport servers. For more information about transport services and the categorizer, see
Mail routing in Exchange Server.

The following tables list the SMTP events that provide access to messages in the transport
pipeline.

SMTP Receive events

                                                                                     ﾉ   Expand table

 Sequence   SMTP event                   Description

     1      OnConnectEvent               This event is triggered by the initial connection from a
                                         remote SMTP host.

     2      OnHeloCommand                This event is triggered when the HELO command is issued
                                         by the remote SMTP host.

     3      OnEhloCommand                This event is triggered when the EHLO command is issued
                                         by the remote SMTP host.

     4      OnStartTlsCommand            This event is triggered when the STARTTLS command is
                                         issued by the remote SMTP host.

     5      OnAuthCommand                This event is triggered when the AUTH command is issued
                                         by the remote SMTP host.

     6      OnProcessAuthentication      This event is triggered when authentication with the remote
                                         SMTP host is being processed.

     7      OnEndOfAuthentication        This event is triggered when the remote SMTP host has
                                         completed authentication.

<!-- p.1675 -->

 Sequence   SMTP event                 Description

    8       OnXSessionParamsCommand    This event is triggered when the XSESSIONPARAMS command
                                       is issued by the remote SMTP host.

    9       OnMailCommand              This event is triggered when the MAIL FROM command is
                                       issued by the remote SMTP host.

    10      OnRcptToCommand            This event is triggered when the RCPT TO command is
                                       issued by the remote SMTP host.

    11      OnDataCommand              This event is triggered when the DATA (text) or BDAT (binary
                                       data) command is issued by the remote SMTP host.

    12      OnEndOfHeaders             This event is triggered when the remote SMTP host has
                                       completed submitting the email message headers. This is
                                       indicated by a blank line ( <CRLF> ) that separates the
                                       message headers and the message body.

    13      OnProxyInboundMessage      This event is triggered when an inbound SMTP session is
                                       relayed or proxied by the Front End Transport service to the
                                       Transport service on a Mailbox server.

    14      OnEndOfData                This event is triggered when the remote SMTP host issues
                                       an end of data command:
                                             For text sessions started by the DATA command, the
                                             end of data indicator is <CRLF>.<CRLF> .
                                             For binary sessions started by the BDAT command, the
                                             end of data indicator is BDAT LAST .

    **      OnHelpCommand              This event is triggered if the HELP command is issued by the
                                       remote SMTP host.

    **      OnNoopCommand              This event is triggered if the NOOP command is issued by the
                                       remote SMTP host.

    **      OnReject                   This event is triggered if the receiving SMTP host issues a
                                       temporary or permanent delivery status notification (also
                                       known as a DSN, non-delivery report, NDR, or bounce
                                       message) code to the sending SMTP host.

    **      OnRsetCommand              This event is triggered if the RSET command is issued by the
                                       sending SMTP host.

    15      OnDisconnectEvent          This event is triggered by the disconnection of the SMTP
                                       conversation by either the receiving or sending SMTP host.
                                       Typically, this happens when the QUIT command is issued
                                       by the remote SMTP host.

** These events can occur at any time after OnConnectEvent but before OnDisconnectEvent.

<!-- p.1676 -->

Categorizer events

                                                                                       ﾉ   Expand table

 Sequence   Categorizer event        Description

     1      OnSubmittedMessage       This event is triggered when a message arrives in the Submission
                                     queue in the Transport service on the receiving Exchange server.

     2      OnResolvedMessage        This event is triggered after all the recipients have been resolved,
                                     but before the next hop has been determined for each recipient.
                                     The OnResolvedMessage routing event enables subsequent
                                     events to override the default routing behavior by using the per-
                                     recipient SetRoutingOverride method.

     3      OnRoutedMessage          This event is triggered after messages have been categorized,
                                     distribution lists have been expanded, and recipients have been
                                     resolved.

     4      OnCategorizedMessage     This event is triggered when the categorizer completes processing
                                     the message.

Priority of transport agents
Two factors determine the order that transport agents act on messages in the transport
pipeline:

   1. The SMTP event where the transport agent is registered, and when that SMTP event
     encounters messages.
   2. The priority value that's assigned to the transport agent if there are multiple agents
     registered to the same SMTP event. The highest priority is 1. A higher integer value
     indicates a lower agent priority.

For example, suppose you configured the following transport agents:

     Transport Agent A with a priority of 1 and Transport Agent C with a priority of 2 are
     registered to the OnEndOfHeaders SMTP event.
     Transport Agent B with a priority of 4 is registered to the OnMailCommand SMTP event.

Transport Agent B is applied to messages first because the OnMailCommand event encounters
messages before the OnEndOfHeaders event. When messages reach the OnEndOfHeaders
event, Transport Agent A is applied before Transport Agent C because Transport Agent A has a
higher priority (lower integer value) than Transport Agent C.

<!-- p.1677 -->

Built-in transport agents
Exchange Server includes many built-in transport agents that provide features such as anti-
spam, transport rules and journaling. Most of the built-in transport agents on Exchange
Mailbox servers are invisible and unmanageable by the transport agent management cmdlets.
Virtually all of the built-in transport agents that are visible and manageable are in the Transport
service on Mailbox servers and Edge Transport servers.

The more interesting built-in transport agents on Mailbox servers are described in the
following table. Note that this table doesn't include many of the invisible and unmanageable
transport agents.

Interesting built-in transport agents on Mailbox servers

                                                                                  ﾉ   Expand table

 Agent name                         Manageable?         Priority       SMTP or categorizer events

 Transport Rule Agent                    Yes               1           OnResolvedMessage

 DLP Policy Agent                        Yes               2           OnResolvedMessage

 Retention Policy Agent                  Yes               3           OnResolvedMessage

 Supervisory Review Agent                Yes               4           OnResolvedMessage

 Malware Agent                           Yes               5           OnSubmittedMessage

 Text Messaging Routing Agent            Yes               6           OnSubmittedMessage

 Text Messaging Delivery Agent           Yes               7           n/a

 System Probe Drop Smtp Agent            Yes               8           OnEndOfHeaders

 System Probe Drop Routing Agent         Yes               9           OnCategorizedMessage

 Journal Agent                           No         Not configurable   OnRoutedMessage

 Journal Report Decryption Agent         No         Not configurable   OnCategorizedMessage

 RMS Decryption Agent                    No         Not configurable   OnSubmittedMessage

 RMS Encryption Agent                    No         Not configurable   OnSubmittedMessage

                                                                       OnRoutedMessage

 RMS Protocol Decryption Agent           No         Not configurable   OnEndOfData

<!-- p.1678 -->

Interesting built-in transport agents on Edge Transport
servers
On Edge Transport servers, most of the built-in transport agents are visible and manageable by
the transport agent management cmdlets or by other feature-specific cmdlets.

The more interesting built-in transport agents on Edge Transport servers are described in the
following table. Note that this table doesn't include invisible or unmanageable transport
agents.

                                                                                 ﾉ   Expand table

 Agent name                            Manageable?      Priority   SMTP or categorizer events

 Connection Filtering Agent                 Yes            1       OnConnectEvent

                                                                   OnMailCommand

                                                                   OnRcptCommand

                                                                   OnEndOfHeaders

 Address Rewriting Inbound Agent            Yes            2       OnRcptCommand

                                                                   OnEndOfHeaders

 Edge Rule Agent                            Yes            3       OnEndOfData

 Content Filter Agent*                      Yes            4       OnEndOfData

 Sender ID Agent*                           Yes            5       OnEndOfHeaders

 Sender Filter Agent*                       Yes            6       OnMailCommand

                                                                   OnEndOfHeaders

 Recipient Filter Agent                     Yes            7       OnRcptCommand

 Protocol Analysis Agent*                   Yes            8       OnConnectEvent

                                                                   OnEndOfHeaders

                                                                   OnEndOfData

                                                                   OnReject

                                                                   OnRsetCommand

                                                                   OnDisconnectEvent

 Attachment Filtering Agent                 Yes            9       OnEndOfData

<!-- p.1679 -->

    Agent name                            Manageable?      Priority   SMTP or categorizer events

    Address Rewriting Outbound Agent           Yes           10       OnSubmittedMessage

                                                                      OnRoutedMessage

*
    You can also install and configure these anti-spam agents on Mailbox servers. For more
information, see Enable antispam functionality on Mailbox servers.

Troubleshoot transport agents
To help you troubleshoot issues with transport agents, you can use the following features:

        Get-TransportPipeline: This cmdlet shows the SMTP events and the corresponding
        transport agents that encounter messages on the Exchange server. For more information,
        see View transport agents in the transport pipeline in Exchange Server.

        Pipeline Tracing: Pipeline tracing creates an exact snapshot of a message before and after
        it encounters each transport agent. This allows you to find a transport agent that's
        causing unexpected results. For more information, see Pipeline tracing.

<!-- p.1680 -->

Manage transport agents in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Transport agents use SMTP events to operate on messages as the messages move through the
transport pipeline. Most of the built-in transport agents that are included with Microsoft
Exchange Server 2016 or 2019 are invisible and unmanageable. However, you can install and
configure third-party transport agents on Exchange servers in your organization. For more
information about transport agents, see Transport agents in Exchange Server.

What do you need to know before you begin?
      Estimated time to complete each procedure: 10 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Transport agents" entry in the
      Mail flow permissions topic.

      You can only use the Exchange Management Shell to perform this procedure.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server .

Use the Exchange Management Shell to install a
transport agent
When you install a transport agent, Exchange only registers the DLLs associated with the
transport agent. You need to make sure all files, registry keys, and other objects that the
transport agent depends on are installed correctly and configured. After Exchange loads the
DLLs, it continues to reference the DLLs after the command has completed.

Transport agents have full access to all email messages that they encounter. Exchange puts no
restrictions on a transport agent's behavior. Transport agents that are unstable or contain
