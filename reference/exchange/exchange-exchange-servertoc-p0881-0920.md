---
title: "Exchange Server — pages 881-920"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0881-0920
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0881-0920
family: exchange
documentKind: "doc"
abstract: "Purpose Ports Source Destination Comments Exchange Active inbound mail on port 25 to organization Directory site any Mailbox server in the subscribed Active Directory site. For more information, see Send connectors created automatically by the Edge Subscription. The default Rece"
---

# Exchange Server — pages 881-920

<!-- p.881 -->

Purpose             Ports           Source               Destination      Comments

Exchange                                                 Active           inbound mail on port 25 to
organization                                             Directory site   any Mailbox server in the
                                                                          subscribed Active Directory
                                                                          site. For more information,
                                                                          see Send connectors
                                                                          created automatically by
                                                                          the Edge Subscription.

                                                                          The default Receive
                                                                          connector named "Default
                                                                          Frontend <Mailbox server
                                                                          name>" in the Front End
                                                                          Transport service on the
                                                                          Mailbox server listens for all
                                                                          inbound mail (including
                                                                          mail from Exchange 2013 or
                                                                          later Edge Transport
                                                                          servers) on port 25.

Outbound mail -     25/TCP (SMTP)   Mailbox servers in   Edge             Outbound mail always
Internal Exchange                   the subscribed       Transport        bypasses the Front End
organization to                     Active Directory     servers          Transport service on
Edge Transport                      site                                  Mailbox servers.
server                                                                    Mail is relayed from the
                                                                          Transport service on any
                                                                          Mailbox server in the
                                                                          subscribed Active Directory
                                                                          site to an Edge Transport
                                                                          server using the implicit
                                                                          and invisible intra-
                                                                          organization Send
                                                                          connector that
                                                                          automatically routes mail
                                                                          between Exchange servers
                                                                          in the same organization.

                                                                          The default Receive
                                                                          connector named "Default
                                                                          internal Receive connector
                                                                          <Edge Transport server
                                                                          name>" on the Edge
                                                                          Transport server listens for
                                                                          SMTP mail on port 25 from
                                                                          the Transport service on any
                                                                          Mailbox server in the
                                                                          subscribed Active Directory
                                                                          site.

<!-- p.882 -->

Purpose              Ports           Source                  Destination      Comments

Outbound mail -      25/TCP (SMTP)   Edge Transport          Internet (any)   The default Send connector
Edge Transport                       server                                   named "EdgeSync - <Active
server to internet                                                            Directory site name> to
                                                                              Internet" relays outbound
                                                                              mail on port 25 from the
                                                                              Edge Transport server to
                                                                              the internet.

EdgeSync             50636/TCP       Mailbox servers in      Edge             When the Edge Transport
synchronization      (secure LDAP)   the subscribed          Transport        server is subscribed to the
                                     Active Directory        servers          Active Directory site, all
                                     site that participate                    Mailbox servers that exist in
                                     in EdgeSync                              the site at the time
                                     synchronization                          participate in EdgeSync
                                                                              synchronization. However,
                                                                              any Mailbox servers that
                                                                              you add later don't
                                                                              automatically participate in
                                                                              EdgeSync synchronization.

DNS for name         53/UDP,53/TCP   Edge Transport          DNS server       See the Name resolution
resolution of the    (DNS)           server                                   section later in this topic.
next mail hop
(not pictured)

Open proxy           see comments    Edge Transport          Internet         By default, sender
server detection                     server                                   reputation (the Protocol
in sender                                                                     Analysis agent) uses open
reputation (not                                                               proxy server detection as
pictured)                                                                     one of the criteria to
                                                                              calculate the sender
                                                                              reputation level (SRL) of the
                                                                              source messaging server.
                                                                              For more information, see
                                                                              Sender reputation and the
                                                                              Protocol Analysis agent.

                                                                              Open proxy server
                                                                              detection uses the
                                                                              following protocols and TCP
                                                                              ports to test source
                                                                              messaging servers for open
                                                                              proxy:

                                                                                    SOCKS4, SOCKS5:
                                                                                    1081, 1080
                                                                                    Wingate, Telnet,
                                                                                    Cisco: 23

<!-- p.883 -->

 Purpose           Ports            Source              Destination    Comments

                                                                             HTTP CONNECT,
                                                                             HTTP POST: 6588,
                                                                             3128, 80

                                                                       Also, if your organization
                                                                       uses a proxy server to
                                                                       control outbound internet
                                                                       traffic, you need to define
                                                                       the proxy server name,
                                                                       type, and TCP port that
                                                                       sender reputation requires
                                                                       to access the internet for
                                                                       open proxy server
                                                                       detection.

                                                                       Alternatively, you can
                                                                       disable open proxy server
                                                                       detection in sender
                                                                       reputation.

                                                                       For more information, see
                                                                       Sender reputation
                                                                       procedures.

Name resolution
DNS resolution of the next mail hop is a fundamental part of mail flow in any Exchange
organization. Exchange servers that are responsible for receiving inbound mail or delivering
outbound mail must be able to resolve both internal and external host names for proper mail
routing. And all internal Exchange servers must be able to resolve internal host names for
proper mail routing. There are many different ways to design a DNS infrastructure, but the
important result is to ensure name resolution for the next hop is working properly for all of
your Exchange servers.

Network ports required for hybrid deployments
The network ports that are required for an organization that uses both on-premises Exchange
and Microsoft 365 or Office 365 are covered in Hybrid deployment protocols, ports, and
endpoints.

Network ports required for Unified Messaging in
Exchange 2016

<!-- p.884 -->

The network ports that are required for Unified Messaging in Exchange 2013 and Exchange
2016 are covered in the topic UM protocols, ports, and services.

<!-- p.885 -->

Overview of Exchange services on Exchange
servers
Article • 05/09/2025

APPLIES TO:        2016     2019      Subscription Edition

  ７ Note

  This article lists all the Exchange services and direct dependencies. There are other critical services
  deployed by the operating system, which may be indirectly used by the Exchange server. Microsoft
  doesn't test or recommend disabling various dependency services. These services shouldn't be disabled
  or stopped without proper functionality testing in the environment. If you stop these services and see
  negative effect on Exchange functionality, you must turn the services back on.

During the installation of Exchange Server 2016 or Exchange Server 2019, Setup runs a set of tasks that install
new services in Microsoft Windows. A service is a background process that can be launched during the
startup of the server by the Windows Service Control Manager. Services are executable files designed to
operate independently and without administrative intervention. A service can run using either a graphical user
interface (GUI) mode or a console mode.

All previous versions of Exchange included components that are implemented as services. Each Exchange
server role includes services that are part of (or may be needed by) the server role to perform its functions.
Note that some services only become active when specific features are used.

The sections in this topic describe the various services that are installed by Exchange 2016 and Exchange 2016
on Mailbox servers and Edge Transport servers. For services that are labeled as optional, you can disable the
service if you determine your organization doesn't need the functionality that's provided by the service.

Exchange services on Mailbox servers
The following table describes the Exchange services that are installed on Mailbox servers.

                                                                                                       ﾉ   Expand table

 Service         Service short name             Description         Default     Security   Dependencies           Required
 name                                           and                 startup     context                           or
                                                dependencies        type                                          optional

 Microsoft       MSExchangeADTopology           Provides            Automatic   Local      Net.TCP Port Sharing   Required
 Exchange                                       Active                          System     Service
 Active                                         Directory
 Directory                                      topology
 Topology                                       information to
                                                Exchange
                                                services. If this
                                                service is
                                                stopped, most
                                                Exchange

<!-- p.886 -->

Service      Service short name         Description      Default     Security   Dependencies         Required
name                                    and              startup     context                         or
                                        dependencies     type                                        optional

                                        services can't
                                        start.

Microsoft    MSExchangeAntispamUpdate   Provides         Automatic   Local      Microsoft Exchange   Optional
Exchange                                Exchange                     System     Active Directory
Anti-spam                               SmartScreen                             Topology
Update                                  spam
                                        definition
                                        updates.
                                        Note: In
                                        November,
                                        2016,
                                        Microsoft
                                        stopped
                                        producing
                                        spam
                                        definition
                                        updates for
                                        the
                                        SmartScreen
                                        filters in
                                        Exchange and
                                        Outlook. The
                                        existing
                                        SmartScreen
                                        spam
                                        definitions
                                        were left in
                                        place, but
                                        their
                                        effectiveness
                                        will likely
                                        degrade over
                                        time. For
                                        more
                                        information,
                                        see
                                        Deprecating
                                        support for
                                        SmartScreen
                                        in Outlook
                                        and
                                        Exchange .

Microsoft    MSComplianceAudit          Provides         Automatic   Local      Microsoft Exchange   Required
Exchange                                Exchange                     System     Active Directory
Compliance                              auditing                                Topology
Audit                                   features.

Microsoft    MSExchangeCompliance       Provides a       Automatic   Local      Microsoft Exchange   Required
Exchange                                host for                     System     Active Directory
Compliance                              Exchange                                Topology
Service

<!-- p.887 -->

Service       Service short name      Description      Default     Security   Dependencies           Required
name                                  and              startup     context                           or
                                      dependencies     type                                          optional

                                      compliance
                                      services.

Microsoft     MSExchangeDagMgmt       Provides         Automatic   Local      Microsoft Exchange     Required
Exchange                              storage and                  System     Active Directory
DAG                                   database                                TopologyNet.TCP Port
Management                            layout                                  Sharing Service
                                      management
                                      for Mailbox
                                      servers in
                                      database
                                      availability
                                      groups
                                      (DAGs).

Microsoft     MSExchangeDiagnostics   Provides an      Automatic   Local      None                   Required
Exchange                              agent that                   System
Diagnostics                           monitors
                                      Exchange
                                      server health.

Microsoft     MSExchangeEdgeSync      Replicates       Automatic   Local      Microsoft Exchange     Optional
Exchange                              configuration                System     Active Directory
EdgeSync                              and recipient                           Topology
                                      data between
                                      the Mailbox
                                      server and
                                      Active
                                      Directory
                                      Lightweight
                                      Directory
                                      Services (AD
                                      LDS) on
                                      subscribed
                                      Edge
                                      Transport
                                      servers over a
                                      secure LDAP
                                      channel.
                                      If you don't
                                      have any
                                      subscribed
                                      Edge
                                      Transport
                                      servers, you
                                      can disable
                                      this service.

Microsoft     MSExchange Mitigation   Auto applies     Automatic   Local      IIS URL Rewrite        Required
Exchange                              important                    System     Module
Emergency                             security
Mitigation                            mitigations on
                                      Exchange
                                      Server to

<!-- p.888 -->

Service     Service short name            Description       Default     Security   Dependencies           Required
name                                      and               startup     context                           or
                                          dependencies      type                                          optional

                                          secure against
                                          known
                                          threats.

Microsoft   MSExchangeFrontEndTransport   Proxies SMTP      Automatic   Local      Microsoft Exchange     Required
Exchange                                  connections                   System     Active Directory
Frontend                                  from external                            Topology
Transport                                 hosts to the
                                          Microsoft
                                          Exchange
                                          Transport
                                          service on
                                          Mailbox
                                          servers (the
                                          local server or
                                          remote
                                          servers).

Microsoft   MSExchangeHM                  Part of           Automatic   Local      Windows Event          Required
Exchange                                  managed                       System     LogWindows
Health                                    availability                             Management
Manager                                   that monitors                            Instrumentation
                                          the health of
                                          key
                                          components
                                          on the
                                          Exchange
                                          server.

Microsoft   MSExchangeHMRecovery          Part of           Automatic   Local           Windows Event     Required
Exchange                                  managed                       System          Log
Health                                    availability                                  Windows
Manager                                   that attempts                                 Management
Recovery                                  to recover                                    Instrumentation
                                          unhealthy
                                          components
                                          on the
                                          Exchange
                                          server.

Microsoft   MSExchangeIMAP4               Proxies IMAP4     Manual      Local      Microsoft Exchange     Optional
Exchange                                  client                        System     Active Directory
IMAP4                                     connections                              Topology
                                          from the
                                          Client Access
                                          (frontend)
                                          services to the
                                          backend
                                          IMAP4 service
                                          on Mailbox
                                          servers. By
                                          default, this
                                          service isn't
                                          running, so

<!-- p.889 -->

Service       Service short name   Description       Default     Security   Dependencies            Required
name                               and               startup     context                            or
                                   dependencies      type                                           optional

                                   IMAP4 clients
                                   can't connect
                                   to the
                                   Exchange
                                   server until
                                   this service is
                                   started.
                                   If you don't
                                   have any
                                   IMAP4 clients,
                                   you can
                                   disable this
                                   service.

Microsoft     MSExchangeIMAP4BE    Receives          Manual      Network    Microsoft Exchange      Optional
Exchange                           proxied                       Service    Active Directory
IMAP4                              IMAP4 client                             Topology
Backend                            connections
                                   from the from
                                   the Client
                                   Access
                                   (frontend)
                                   IMAP4 service.
                                   By default,
                                   this service
                                   isn't running,
                                   so IMAP4
                                   clients can't
                                   connect to the
                                   Exchange
                                   server until
                                   this service is
                                   started.
                                   If you don't
                                   have any
                                   IMAP4 clients,
                                   you can
                                   disable this
                                   service.

Microsoft     MSExchangeIS         Manages the       Automatic   Local           Microsoft          Required
Exchange                           mailbox                       System          Exchange
Information                        databases on                                  Active Directory
Store                              the server. If                                Topology
                                   this service is                               Remote
                                   stopped,                                      Procedure Call
                                   mailbox                                       (RPC)
                                   databases on                                  Server
                                   the server are                                Windows Event
                                   unavailable.                                  Log
                                                                                 Workstation

<!-- p.890 -->

Service         Service short name              Description       Default     Security   Dependencies            Required
name                                            and               startup     context                            or
                                                dependencies      type                                           optional

Microsoft       MSExchangeMailboxAssistants     Performs          Automatic   Local      Microsoft Exchange      Required
Exchange                                        background                    System     Active Directory
Mailbox                                         processing of                            Topology
Assistants                                      mailboxes in
                                                mailbox
                                                databases on
                                                the server.

Microsoft       MSExchangeMailboxReplication    Processes         Automatic   Local      Microsoft Exchange      Required
Exchange                                        mailbox                       System     Active Directory
Mailbox                                         moves and                                TopologyNet.TCP Port
Replication                                     move                                     Sharing Service
                                                requests.

Microsoft       MSExchangeDelivery              Receives          Automatic   Network    Microsoft Exchange      Required
Exchange                                        SMTP                          Service    Active Directory
Mailbox                                         messages                                 Topology
Transport                                       from the
Delivery                                        Microsoft
                                                Exchange
                                                Transport
                                                service (on the
                                                local or
                                                remote
                                                Mailbox
                                                servers) and
                                                delivers them
                                                to a local
                                                mailbox
                                                database
                                                using RPC.

Microsoft       MSExchangeSubmission            Receives RPC      Automatic   Local      Microsoft Exchange      Required
Exchange                                        messages                      System     Active Directory
Mailbox                                         from a local                             Topology
Transport                                       mailbox
Submission                                      database, and
                                                submits them
                                                over SMTP to
                                                the Microsoft
                                                Exchange
                                                Transport
                                                service (on the
                                                local or
                                                remote
                                                Mailbox
                                                servers).

Microsoft       MSExchangeNotificationsBroker   Provides          Automatic   Local           Microsoft          Required
Exchange                                        Exchange                      System          Exchange
Notifications                                   notifications                                 Active Directory
Broker                                          to local and                                  Topology
                                                remote

<!-- p.891 -->

Service       Service short name   Description       Default     Security   Dependencies           Required
name                               and               startup     context                           or
                                   dependencies      type                                          optional

(Exchange                          Exchange                                      Net.TCP Port
2016 only)                         processes.                                    Sharing Service

Microsoft     MSExchangePOP3       Proxies POP3      Manual      Network    Microsoft Exchange     Optional
Exchange                           client                        Service    Active Directory
POP3                               connections                              Topology
                                   from the
                                   Client Access
                                   (frontend)
                                   services to the
                                   backend
                                   IMAP4 service
                                   on Mailbox
                                   servers. By
                                   default, this
                                   service isn't
                                   running, so
                                   POP3 clients
                                   can't connect
                                   to the
                                   Exchange
                                   server until
                                   this service is
                                   started.

Microsoft     MSExchangePOP3BE     Receives          Manual      Network    Microsoft Exchange     Optional
Exchange                           proxied POP3                  Service    Active Directory
POP3                               client                                   Topology
Backend                            connections
                                   from the from
                                   the Client
                                   Access
                                   (frontend)
                                   POP3 service.
                                   By default,
                                   this service
                                   isn't running,
                                   so POP3
                                   clients can't
                                   connect to the
                                   Exchange
                                   server until
                                   this service is
                                   started.

Microsoft     MSExchangeRepl       Provides          Automatic   Local      Microsoft Exchange     Required
Exchange                           replication                   System     Active Directory
Replication                        functionality                            Topology
Service                            for mailbox
                                   databases in a
                                   database
                                   availability

<!-- p.892 -->

Service         Service short name      Description       Default     Security   Dependencies         Required
name                                    and               startup     context                         or
                                        dependencies      type                                        optional

                                        groups
                                        (DAGs).

Microsoft       MSExchangeRPC           Manages           Automatic   Network    Microsoft Exchange   Required
Exchange                                client RPC                    Service    Active Directory
RPC Client                              connections                              Topology
Access                                  for Exchange.

Microsoft       MSExchangeFastSearch    Provides          Automatic   Local      Microsoft Exchange   Required
Exchange                                indexing of                   System     Active Directory
Search                                  mailbox                                  Topology
                                        content, which
                                        improves the
                                        performance
                                        of content
                                        search.

Microsoft       HostControllerService   Provides          Automatic   Local      HTTP Service         Required
Exchange                                deployment                    System
Search Host                             and
Controller                              management
                                        services for
                                        applications
                                        on the local
                                        Exchange
                                        server.

Microsoft       WSBExchange             Enables           Manual      Local      None                 Optional
Exchange                                Windows                       System
Server                                  Server Backup
Extension for                           to back and
Windows                                 restore
Server                                  Exchange
Backup                                  server data.

Microsoft       MSExchangeServiceHost   Provides a        Automatic   Local      Microsoft Exchange   Required
Exchange                                service host                  System     Active Directory
Service Host                            for Exchange                             Topology
                                        components
                                        that don't
                                        have their
                                        own services.

Microsoft       MSExchangeThrottling    Provides user     Automatic   Network    Microsoft Exchange   Required
Exchange                                workload                      Service    Active Directory
Throttling                              management                               Topology
                                        that limits the
                                        rate of user
                                        operations
                                        (formerly
                                        known as user
                                        throttling).

<!-- p.893 -->

Service      Service short name             Description        Default     Security   Dependencies            Required
name                                        and                startup     context                            or
                                            dependencies       type                                           optional

Microsoft    MSExchangeTransport            Provides           Automatic   Network         Microsoft          Required
Exchange                                    SMTP server                    Service         Exchange
Transport                                   and transport                                  Active Directory
                                            stack.                                         Topology
                                                                                           Microsoft
                                                                                           Filtering
                                                                                           Management
                                                                                           Service

Microsoft    MSExchangeTransportLogSearch   Provides           Automatic   Local      Microsoft Exchange      Optional
Exchange                                    remote search                  System     Active Directory
Transport                                   capability for                            Topology
Log Search                                  transport log
                                            files (for
                                            example,
                                            message
                                            tracking).

Microsoft    MSExchangeUM                   Provides           Automatic   Local           CNG Key            Optional
Exchange                                    Unified                        System          Isolation
Unified                                     Messaging                                      Microsoft
Messaging                                   (UM) features:                                 Exchange
(Exchange                                   allows voice                                   Active Directory
2016 only)                                  and fax                                        Topology
                                            messages to
                                            be stored in
                                            Exchange
                                            2016 and
                                            gives users
                                            telephone
                                            access to
                                            email, voice
                                            mail, calendar,
                                            contacts, or
                                            an auto
                                            attendant. If
                                            this service is
                                            stopped,
                                            Unified
                                            Messaging
                                            isn't available.
                                            If you don't
                                            use UM in
                                            Exchange
                                            2016, you can
                                            disable this
                                            service.

Microsoft    MSExchangeUMCR                 Redirects UM       Automatic   Local           CNG Key            Optional
Exchange                                    client                         System          Isolation
Unified                                     connections                                    Microsoft
Messaging                                   from the                                       Exchange

<!-- p.894 -->

 Service        Service short name            Description       Default     Security   Dependencies            Required
 name                                         and               startup     context                            or
                                              dependencies      type                                           optional

 Call Router                                  Client Access                                 Active Directory
 (Exchange                                    (frontend)                                    Topology
 2016 only)                                   services to the
                                              backend
                                              Unified
                                              Messaging
                                              service on
                                              Exchange
                                              2016 Mailbox
                                              servers.
                                              If you don't
                                              use UM in
                                              Exchange
                                              2016, you can
                                              disable this
                                              service.

Exchange services on Edge Transport servers
The following table describes the Exchange services that are installed on Edge Transport servers.

                                                                                                    ﾉ   Expand table

 Service       Service short name           Description     Default       Security   Dependencies           Required
 name                                                       startup       context                           or
                                                            type                                            optional

 Microsoft     ADAM_MSExchange              Stores          Automatic     Network    COM+ Event System      Required
 Exchange                                   configuration                 Service
 ADAM                                       data and
                                            recipient
                                            data on the
                                            Edge
                                            Transport
                                            server. This
                                            service
                                            represents
                                            the named
                                            instance of
                                            the Active
                                            Directory
                                            Lightweight
                                            Directory
                                            Services (AD
                                            LDS) that's
                                            automatically
                                            created by
                                            Exchange
                                            Setup.

<!-- p.895 -->

Service      Service short name         Description     Default     Security   Dependencies         Required
name                                                    startup     context                         or
                                                        type                                        optional

Microsoft    MSExchangeAntispamUpdate   Provides        Automatic   Local      Microsoft Exchange   Optional
Exchange                                Exchange                    System     ADAM
Anti-spam                               SmartScreen
Update                                  spam
                                        definition
                                        updates.
                                        Note: In
                                        November,
                                        2016,
                                        Microsoft
                                        stopped
                                        producing
                                        spam
                                        definition
                                        updates for
                                        the
                                        SmartScreen
                                        filters in
                                        Exchange
                                        and Outlook.
                                        The existing
                                        SmartScreen
                                        spam
                                        definitions
                                        were left in
                                        place, but
                                        their
                                        effectiveness
                                        will likely
                                        degrade over
                                        time. For
                                        more
                                        information,
                                        see
                                        Deprecating
                                        support for
                                        SmartScreen
                                        in Outlook
                                        and
                                        Exchange .

Microsoft    MSExchangeEdgeCredential   Monitors        Automatic   Local      Microsoft Exchange   Required
Exchange                                credential                  System     ADAM
Credential                              changes in
Service                                 Active
                                        Directory
                                        Lightweight
                                        Directory
                                        Services (AD
                                        LDS) and
                                        installs the
                                        changes on
                                        the Edge

<!-- p.896 -->

Service       Service short name             Description      Default     Security   Dependencies             Required
name                                                          startup     context                             or
                                                              type                                            optional

                                             Transport
                                             server.

Microsoft     MSExchangeDiagnostics          Provides an      Automatic   Local      None                     Required
Exchange                                     agent that                   System
Diagnostics                                  monitors
                                             Exchange
                                             server health.

Microsoft     MSExchangeHM                   Part of          Automatic   Local             Windows Event     Required
Exchange                                     managed                      System            Log
Health                                       availability                                   Windows
Manager                                      that                                           Management
                                             monitors the                                   Instrumentation
                                             health of key
                                             components
                                             on the
                                             Exchange
                                             server.

Microsoft     MSExchangeHMRecovery           Part of          Automatic   Local      Windows Event            Required
Exchange                                     managed                      System     LogWindows
Health                                       availability                            Management
Manager                                      that                                    Instrumentation
Recovery                                     attempts to
                                             recover
                                             unhealthy
                                             components
                                             on the
                                             Exchange
                                             server.

Microsoft     MSExchangeServiceHost          Provides a       Automatic   Local      Microsoft Exchange       Required
Exchange                                     service host                 System     ADAM
Service                                      for Exchange
Host                                         components
                                             that don't
                                             have their
                                             own services.

Microsoft     MSExchangeTransport            Provides         Automatic   Network    Microsoft Exchange       Required
Exchange                                     SMTP server                  Service    ADAM
Transport                                    and
                                             transport
                                             stack.

Microsoft     MSExchangeTransportLogSearch   Provides         Automatic   Local      Microsoft Exchange       Optional
Exchange                                     remote                       System     ADAM
Transport                                    search
Log Search                                   capability for
                                             transport log
                                             files (for
                                             example,

<!-- p.897 -->

Service   Service short name   Description   Default   Security   Dependencies   Required
name                                         startup   context                   or
                                             type                                optional

                               message
                               tracking).

<!-- p.898 -->

Exchange Server preferred architecture
10/17/2025

APPLIES TO:        2016    2019     Subscription Edition

With each new release of Exchange Server for our on-premises customers, we update our
Preferred Architecture and discuss what changes we would like our customers to be aware of.
Exchange Server 2013 brought us the first of the Preferred Architectures    in modern Exchange
history and was then followed with a refresh   for Exchange Server 2016 by providing
refinements for the changes that came with the 2016 release. With this update, we'll iterate on
the previous PA to take advantage of new technologies and improvements.

The preferred architecture
The PA is the Exchange Server Engineering Team's best practice recommendation for what we
believe is the best deployment architecture for Exchange Server in an on-premises
environment.

While Exchange Server offers a wide variety of architectural choices for on-premises
deployments, the architecture discussed here is the most scrutinized one. While there are other
supported deployment architectures, they aren't our recommended practice.

Following the PA helps customers become a member of a community of organizations with
similar Exchange Server deployments. This strategy allows easier knowledge sharing and
provides a more rapid response to unforeseen circumstances. Our own support organization is
aware what an Exchange Server PA deployment should look like and prevents them from
spending lengthy cycles learning and understanding a customer's highly custom environment
before working with them towards a support case resolution.

The PA is designed with several business requirements in mind, such as the requirement that
the architecture be able to:

     Include both high availability within the datacenter, and site-resilience between
     datacenters

     Support multiple copies of each database, thereby allowing for quick activation

     Reduce the cost of the messaging infrastructure

     Increase availability by optimizing around failure domains and reducing complexity

The specific prescriptive nature of the PA means that not every customer will be able to deploy
it word for word. For example, not all our customers have multiple data centers. Some of our

<!-- p.899 -->

customers may have different business requirements or internal policies they must adhere to
which necessitate a different deployment architecture. If you fall into those categories, and you
want to deploy Exchange on-premises, there are still advantages to adhering as closely as
possible to the PA and deviate only where your requirements or policies force you to differ.
Alternatively, you can always consider Microsoft 365 or Office 365 where you no longer must
deploy or manage a large number of servers.

The PA removes complexity and redundancy where necessary to drive the architecture to a
predictable recovery model: when a failure occurs, another copy of the affected database is
activated.

The PA covers the following four areas of focus:

   1. Namespace design

   2. Site-resilient datacenter pair design

   3. Server design

   4. Database availability group design

We have no changes in three of the four categories from the Exchange Server 2016 Preferred
Architecture. The areas of Namespace design, Datacenter design, and DAG design are receiving
no major changes. We have been pleased with customer deployments that closely followed the
Exchange Server 2016 PA and see no need to deviate from the recommendations in those
areas.

The most noteworthy changes in the updated Exchange Server PA focus on the area of Server
design due to some new and exciting technologies.

Namespace design
In the Namespace Planning      and Load Balancing Principles    articles for Exchange Server
2016, Ross Smith IV outlined the various configuration choices that were available with
Exchange 2016 and these concepts continue to apply. For the namespace, the choices are to
either deploy a bound namespace       (having a preference for the users to operate out of a
specific datacenter) or an unbound namespace       (having the users connect to any datacenter
without preference).

The recommended approach is to use the unbounded model, deploying a single Exchange
namespace per client protocol for the site-resilient datacenter pair (where each datacenter is
assumed to represent its own Active Directory site - see more details on that below). For
example:

<!-- p.900 -->

     For the Autodiscover service: autodiscover.contoso.com

     For HTTP clients: mail.contoso.com

     For IMAP clients: imap.contoso.com

     For SMTP clients: smtp.contoso.com

Each Exchange namespace is load balanced across both datacenters in a layer 7 configuration
that doesn't use session affinity, resulting in 50 percent of traffic being proxied between
datacenters. Traffic is equally distributed across the datacenters in the site-resilient pair, via
round robin DNS, geo-DNS, or other similar solutions. From our perspective, the simpler
solution is the least complex and easier to manage, so our recommendation is to use round
robin DNS.

One caution we have for customers is to ensure you assign a low TTL (time to live) value for
any DNS record associated with your Exchange architecture. If a full datacenter outage
happens when you're using round robin DNS, you must maintain the ability to quickly update
your DNS records. You'll need to remove the IP addresses from the offline datacenter so they
aren't returned for DNS queries. For example, if your DNS records have a longer TTL value of
24 hours it may take up to a day for downstream DNS caches to properly update. If you don't
do this step, you may find some clients are unable to properly transition to the still available IP
addresses in your remaining datacenter. Don't forget to add the IP addresses back to your DNS
records when your previously offline datacenter is recovered and ready to host services once
again.

Data center affinity is required for the Office Online Server farms, thus a namespace is
deployed per datacenter with the load balancer utilizing layer 7, and maintaining session
affinity via cookie-based persistence.

<!-- p.901 -->

If you have multiple site-resilient datacenter pairs in your environment, you'll need to decide if
you want to have a single worldwide namespace, or if you want to control the traffic to each
specific datacenter by using regional namespaces. Your decision depends on your network
topology and the associated cost with using an unbound model; for example, if you have
datacenters located in North America and South Africa, the network link between these regions
might not only be costly, but it might also have high latency, which can introduce user pain
and operational issues. In that case, it makes sense to deploy a bound model with a separate
namespace for each region. However, options like geographical DNS offer you the ability to
deploy a single unified namespace, even when you have costly network links; geo-DNS allows
you to have your users directed to the closest datacenter based on their client's IP address.

Site-resilient datacenter pair design
To achieve a highly available and site-resilient architecture, you must have two or more
datacenters that are well connected (ideally, you want a low round-trip network latency,
otherwise replication and the client experience are adversely affected). In addition, the

<!-- p.902 -->

datacenters should be connected via redundant network paths supplied by different operating
carriers.

While we support stretching an Active Directory site across multiple datacenters, for the PA we
recommend that each datacenter be its own Active Directory site. There are two reasons:

   1. Transport site-resilience via Shadow redundancy in Exchange Server and Safety Net in
      Exchange Server can only be achieved when the DAG has members located in more than
      one Active Directory site.

   2. Active Directory has published guidance that states that subnets should be placed in
      different Active Directory sites when the round-trip latency is greater than 10 ms between
      the subnets.

Server design
In the PA, all servers are physical servers and use locally attached storage. Physical hardware is
deployed rather than virtualized hardware for two reasons:

   1. The servers are scaled to use 80% of resources during the worst-failure mode.

   2. Virtualization comes with a slight performance penalty and adding an additional layer of
      management and complexity, which introduces additional recovery modes that do not
      add value, particularly since Exchange Server natively provides the same functionality.

Commodity servers
Commodity server platforms are used in the PA. Current commodity platforms are and include:

      2U, dual socket servers with up to 48 physical processor cores (an increase from 24 cores
      in Exchange 2016)

      Up to 256 GB of memory (an increase from 192 GB in Exchange 2016)

      A battery-backed write cache controller

      12 or more drive bays within the server chassis

      The ability to mix traditional rotating platter storage (HDD) and solid-state storage (SSD)
      within the same chassis.

Scale Theory

<!-- p.903 -->

It's important to note even though we've increased the allowed processor and memory
capacity in Exchange Server 2019 and Exchange Server SE, the Exchange Server PG's
recommendation remains to scale out rather than up. Scaling out vs up means we would much
rather see you deploy a larger number of servers with slightly less resources per server rather
than a smaller number of dense servers using maximum resources and populated with large
numbers of mailboxes. By locating a reasonable number of mailboxes within a server, you
lessen the impact of any planned or unplanned outage and reduce the risk of discovering other
system bottlenecks.

An increase in system resources shouldn't result in the assumption you'll see linear
performance gains in this Exchange Server versions using the maximum allowed resources
when comparing it to Exchange 2016's maximum allowed resources. Each new version of
Exchange brings new processes and updates that in turn make it difficult to compare a current
version to prior version. Follow any and all sizing guidance from Microsoft when determining
your server design.

Storage
Additional drive bays may be directly attached per-server depending on the number of
mailboxes, mailbox size, and the server's resource scalability.

Each server houses a single RAID1 disk pair for the operating system, Exchange binaries,
protocol/client logs, and the transport database.

The remaining storage is configured as JBOD (Just a Bunch of Disks). Be aware some hardware
storage controllers may require each disk to each be configured as a single-disk RAID0 group
for write caching to be utilized. Consult with your hardware manufacturer to confirm the
proper configuration for your system that guarantees write-cache will be used.

New to the Exchange Server PA is the recommendation of having two classes of storage for
everything not already located on the RAID1 disk pair previously mentioned.

Traditional storage class

This storage class contains Exchange Server database files and Exchange Server transaction log
files. These disks are large capacity 7.2 K RPM serially attached SCSI (SAS) disks. While SATA
disks are also available, we observe better IO and a lower annualized failure rate using the SAS
equivalent.

To ensure the capacity and IO of each disk is used as efficiently as possible, up to four database
copies are deployed per-disk. The normal run-time copy layout ensures that there's no more
than a single active database copy per disk.

<!-- p.904 -->

At least one disk in the traditional storage disk pool is reserved as a hot spare. AutoReseed is
enabled and quickly restores database redundancy after a disk failure by activating the hot
spare and initiating database copy reseeds.

Solid-state storage class
This storage class contains Exchange Server's new MetaCache Database (MCDB) files. These
solid-state drives may come in different form factors such as but not limited to traditional
2.5"/3.5" SAS connected or M.2 PCIe connected drives.

Customers should expect to deploy roughly 5-10% additional storage as solid-state storage.
For example, if a single server was expected to hold 28 TB of mailbox database files on
traditional storage, then an additional 1.4-2.8 TB TB of solid-state storage would also be
recommended as additional storage for the same server.

Traditional and solid-state disks should be deployed in a 3:1 ratio where possible. For every
three traditional disks within the server, a single solid-state disk will be deployed. These solid-
state disks will hold the MCDBs for all DBs within the three associated traditional disks. This
recommendation limits the failure domain a solid-state drive failure can impose on a system.
When an SSD fails, Exchange Server will fail over all database copies using that SSD for their
MCDB to another DAG node with healthy MCDB resources for the affected database. Limiting
the number of database failovers reduce the chance of impacting users if many more
databases were sharing a smaller number of solid-state drives.

If there is a solid-state drive failure Exchange High Availability service, will attempt to mount
the affected databases on different DAG nodes where a healthy MCDB for each affected
database still exists. If for some reason no healthy MCDBs exist for one of the affected
databases, then Exchange High Availability services will leave the local affected database copy
running without the performance benefits of the MCDB.

For example, if a customer were to deploy a system capable of holding 20 drives it may have a
layout like the following.

     2 HDDs for OS mirror, Exchange Binaries, and Transport Database

     12 HDDs for Exchange Database storage

     1 HDD as the AutoReseed spare

     4 SSDs for Exchange MCDBs that provide between 5-10% of the cumulative database
     storage capacity.

     Optionally a customer may elect to add a spare SSD or a second AutoReseed drive.

<!-- p.905 -->

This configuration can be visualized using the following diagram:

In the example above, we have 120 TB of Exchange database storage and 7.68 TB of MCDB
storage that is roughly 6.4% the traditional database storage space. With this amount of MCBD
storage, we're perfectly aligned within the guidance of 5-10%. Each of the 10 TB drives will
hold four database copies and each MCDB drive would hold 12 MCDBs.

Common storage settings
Whether Traditional or Solid-State, all disks that house an Exchange data are formatted with
ReFS (with the integrity feature disabled) and the DAG is configured such that AutoReseed
formats the disks with ReFS:

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity <DAGIdentity> -FileSystem ReFS

BitLocker is used to encrypt each disk, thereby providing data encryption at rest and mitigating
concerns around data theft or disk replacement. For more information, see Enabling BitLocker
on Exchange Servers .

Database availability group design
Within each site-resilient datacenter pair, you'll have one or more DAGs. It isn't recommended
to stretch a DAG across more than two datacenters.

DAG configuration
As with the namespace model, each DAG within the site-resilient datacenter pair operates in an
unbound model with active copies distributed equally across all servers in the DAG. This model:

   1. Ensures that each DAG member's full stack of services (client connectivity, replication
     pipeline, transport, etc.) is being validated during normal operations.

<!-- p.906 -->

   2. Distributes the load across as many servers as possible during a failure scenario, thereby
      only incrementally increasing resource use across the remaining members within the
      DAG.

Each datacenter is symmetrical, with an equal number of DAG members in each datacenter.
This means that each DAG has an even number of servers and uses a witness server for quorum
maintenance.

The DAG is the fundamental building block in Exchange Server. With respect to DAG size, a
DAG with a greater number of participating member nodes provides more redundancy and
resources. Within the PA, the goal is to deploy DAGs with a greater number of member nodes,
typically starting with an eight-member DAG and increasing the number of servers as required
to meet your requirements. You should only create new DAGs when scalability introduces
concerns over the existing database copy layout.

DAG network design
The PA uses a single, non-teamed network interface for both client connectivity and data
replication. A single network interface is all that is needed because ultimately our goal is to
achieve a standard recovery model regardless of the failure - whether a server failure occurs, or
a network failure occurs, the result is the same: a database copy is activated on another server
within the DAG. This architectural change simplifies the network stack and obviates the need to
manually eliminate heartbeat cross-talk.

Witness server placement
The placement of the witness server determines whether the architecture can provide
automatic datacenter failover capabilities or whether it will require a manual activation to
enable service if there is a site failure.

If your organization has a third location with a network infrastructure that is isolated from
network failures that affect the site-resilient datacenter pair in which the DAG is deployed, then
the recommendation is to deploy the DAG's witness server in that third location. This
configuration gives the DAG the ability to automatically fail over databases to the other
datacenter in response to a datacenter-level failure event, regardless of which datacenter has
the outage.

If your organization doesn't have a third location, consider placing the server witness in Azure;
alternatively, place the witness server in one of the datacenters within the site-resilient
datacenter pair. If you have multiple DAGs within the site-resilient datacenter pair, then place
the witness server for all DAGs in the same datacenter (typically the datacenter where most of

<!-- p.907 -->

the users are physically located). Also, make sure the Primary Active Manager (PAM) for each
DAG is also located in the same datacenter.

Exchange Server doesn't support the use of the Cloud Witness feature first introduced in
Windows Server 2016 Failover Cluster.

Data resiliency
Data resiliency is achieved by deploying multiple database copies. In the PA, database copies
are distributed across the site-resilient datacenter pair, thereby ensuring that mailbox data is
protected from software, hardware, and even datacenter failures.

Each database has four copies, with two copies in each datacenter, which means at a minimum,
the PA requires four servers. Out of these four copies, three of them are configured as highly
available. The fourth copy (the copy with the highest Activation Preference number) is
configured as a lagged database copy. Due to the server design, each copy of a database is
isolated from its other copies, thereby reducing failure domains and increasing the overall
availability of the solution as discussed in DAG: Beyond the "A"   .

The purpose of the lagged database copy is to provide a recovery mechanism for the rare
event of system-wide, catastrophic logical corruption. It isn't intended for individual mailbox
recovery or mailbox item recovery.

The lagged database copy is configured with a seven-day ReplayLagTime. In addition, the
Replay Lag Manager is also enabled to provide dynamic log file play down for lagged copies
when availability is compromised due to the loss of non-lagged copies.

By using the lagged database copy in this manner, it's important to understand that the lagged
database copy isn't a guaranteed point-in-time backup. The lagged database copy will have an
availability threshold, typically around 90%, due to periods where the disk containing a lagged
copy is lost due to disk failure, the lagged copy becoming an HA copy (due to automatic play
down), and, the periods where the lagged database copy is rebuilding the replay queue.

To protect against accidental (or malicious) item deletion, Single Item Recover or In-Place Hold
technologies are used, and the Deleted Item Retention window is set to a value that meets or
exceeds any defined item-level recovery SLA.

With all of these technologies in play, traditional backups are unnecessary; as a result, the PA
uses Exchange Native Data Protection.

Office Online Server design

<!-- p.908 -->

At a minimum, you'll want to deploy an Office Online Server (OOS) farm with at least two OOS
nodes in each datacenter that hosts Exchange servers. Each Office Online Server should have at
least 8 processor cores, 32 GB of memory and at least 40 GB of space dedicated for log files.
Exchange Server mailbox servers should be configured to rely on the local OOS farm in their
datacenter to ensure the lowest possible latency and highest possible bandwidth between the
servers to render file content to users.

Summary
Exchange Server continues to improve upon the investments introduced in previous versions of
Exchange and introduces additional technologies originally invented for use in Microsoft 365
and Office 365.

By aligning with the Preferred Architecture, you'll take advantage of these changes and provide
the best on-premises user experience possible. You'll continue the tradition of having a highly
reliable, predictable, and resilient Exchange deployment.

<!-- p.909 -->

Exchange Server permissions
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Microsoft Exchange Server includes a large set of predefined permissions, based on the Role
Based Access Control (RBAC) permissions model, which you can use right away to easily grant
permissions to your administrators and users. You can use the permissions features in
Exchange Server so that you can get your new organization up and running quickly.

  ７ Note

  Disabling permissions inheritance on Active Directory (AD) objects, in an AD domain that
  is prepared to host Exchange, isn't supported. The removal of Exchange-related
  permissions on AD objects will cause Exchange tasks and functions to break or may lead
  to unknown issues.

Role-based permissions
In Exchange Server, the permissions that you grant to administrators and users are based on
management roles. A role defines the set of tasks that an administrator or user can perform.
For example, a management role called Mail Recipients defines the tasks that someone can
perform on a set of mailboxes, contacts, and distribution groups. When a role is assigned to an
administrator or user, that person is granted the permissions provided by the role.

There are two types of roles, namely administrative roles and end-user roles:

      Administrative roles: These roles contain permissions that can be assigned to
      administrators or specialist users using role groups that manage a part of the Exchange
      organization, such as recipients, servers, or databases.

      End-user roles: These roles, assigned using role assignment policies, enable users to
      manage aspects of the mailbox and distribution groups that they own. End-user roles
      begin with the prefix My .

When the roles are assigned to administrators and users, it gives them the permissions to
perform tasks by making cmdlets available for them. Because the Exchange admin center (EAC)
and the Exchange Management Shell use cmdlets to manage Exchange, granting access to a
cmdlet gives the administrator or user the permission to perform the task in each of the
Exchange management interfaces.

<!-- p.910 -->

Role groups and role assignment policies
Roles grant permissions to perform tasks in Exchange Server, but you need an easy way to
assign the roles to administrators and users. Exchange Server provides you with the following
methods to help you do that:

     Role groups: Role groups enable you to grant permissions to administrators and
     specialist users.

     Role assignment policies: Role assignment policies enable you to grant permissions to
     end users to change settings on the mailbox or distribution groups that they own.

For more information about role groups and role assignment policies, see the following
sections.

Role groups
Every administrator that manages Exchange Server needs to be assigned at least one or more
roles. Administrators might have more than one role because they may perform job functions
that span multiple areas in Exchange. For example, one administrator might manage both
recipients and Exchange servers. In this case, that administrator might be assigned both the
Mail Recipients and Exchange Servers roles.

To make it easier to assign multiple roles to an administrator, Exchange Server includes role
groups. Role groups are special universal security groups (USGs) used by Exchange Server that
can contain AD users, USGs, and other role groups. When a role is assigned to a role group, the
permissions granted by the role are granted to all the members of the role group. This feature
enables you to assign many roles to many role group members at once. Role groups typically
encompass broader management areas, such as recipient management. They're used only with
administrative roles, and not with end-user roles.

  ７ Note

  It's possible to assign a role directly to a user or USG without using a role group. However,
  that method of role assignment is an advanced procedure and isn't covered in this topic.
  We recommend that you use role groups to manage permissions.

The following figure shows the relationship between users, role groups, and roles.

Roles, role groups, and role group members

<!-- p.911 -->

Exchange Server includes several built-in role groups, each one providing permissions to
manage specific areas in Exchange Server. Some role groups may overlap with others. The
following table lists each role group with a description of its use. If you want to see the roles
assigned to each role group, click the name of the role group in the "Role group" column, and
then go to the "Management Roles Assigned to This Role Group" section.

  ） Important

  If an administrator is a member of more than one role group, Exchange Server grants the
  administrator all the permissions provided by those role groups.

Built-in role groups

                                                                                     ﾉ   Expand table

 Role group        Description

 Organization      Administrators who are members of the Organization Management role group have
 Management        administrative access to the entire Exchange Server organization and can perform
                   almost any task against any Exchange Server object, with some exceptions, such as
                   the Discovery Management role.
                   Important: Because the Organization Management role group is a powerful role, only
                   users or USGs that perform organizational-level administrative tasks that can
                   potentially impact the entire Exchange organization should be members of this role
                   group.

 View-Only         Administrators who are members of the View Only Organization Management role
 Organization      group can view the properties of any object in the Exchange organization.
 Management

<!-- p.912 -->

Role group        Description

Recipient         Administrators who are members of the Recipient Management role group have
Management        administrative access to create or modify Exchange Server recipients within the
                  Exchange Server organization.

UM                Administrators who are members of the UM Management role group can manage
Management        features in the Exchange organization such as Unified Messaging (UM) service
                  configuration, UM properties on mailboxes, UM prompts, and UM auto attendant
                  configuration. (Note: UM isn't available on Exchange 2019.)

Help Desk         The Help Desk role group, by default, enables members to view and modify the
                  "Outlook on the web" (formerly known as Outlook Web App) options of any user in
                  the organization. These options might include modifying the user's display name,
                  address, and phone number. These options don't include options that aren't available
                  in "Outlook on the web" options, such as modifying the size of a mailbox or
                  configuring the mailbox database on which a mailbox is located.

Hygiene           Administrators who are members of the Hygiene Management role group can
Management        configure the antivirus and antispam features of Exchange Server. Third-party
                  programs that integrate with Exchange Server can add service accounts to this role
                  group to grant those programs access to the cmdlets required to retrieve and
                  configure the Exchange configuration.

Records           Users who are members of the Records Management role group can configure
Management        compliance features, such as retention policy tags, message classifications, and mail
                  flow rules (also known as transport rules).

Discovery         Administrators or users who are members of the Discovery Management role group
Management        can perform searches of mailboxes in the Exchange organization for data that meets
                  specific criteria, and can also configure legal holds on mailboxes.

Public Folder     Administrators who are members of the Public Folder Management role group can
Management        manage public folders on servers running Exchange Server.

Server            Administrators who are members of the Server Management role group can configure
Management        server-specific configuration of transport, Unified Messaging, client access, and
                  mailbox features such as database copies, certificates, transport queues and Send
                  connectors, virtual directories, and client access protocols. (Note: UM isn't available
                  on Exchange 2019.)

Delegated Setup   Administrators who are members of the Delegated Setup role group can deploy
                  servers running Exchange Server that have been previously provisioned by a member
                  of the Organization Management role group.

Compliance        Users who are members of the Compliance Management role group can configure
Management        and manage Exchange compliance settings in accordance with their organization's
                  policy.

<!-- p.913 -->

If you work in a small organization that has only a few administrators, you might only ever use
the Organization Management role group, and none of the other role groups. If you work in a
larger organization, you might have administrators who perform specific tasks administering
Exchange, such as recipient or server management. In those cases, you might add one
administrator to the Recipient Management role group, and another administrator to the
Server Management role group. Those administrators can then manage their specific areas of
Exchange Server but won't have permissions to manage areas they're not responsible for.

If you can't find a built-in role group that fits the jobs your administrators need to do, you can
create role groups and add roles to them. For more information, see Work with role groups
later in this topic.

Role assignment policies
Exchange Server provides role assignment policies so that you can control what settings your
users can configure on the mailboxes and distribution groups they own. These settings include
their display name, contact information, voice mail settings, and distribution group
membership.

Your Exchange Server organization can have multiple role assignment policies that provide
different levels of permissions for the different types of users in your organizations. Some users
can be allowed to change their address or create distribution groups, while others can't. It all
depends on the role assignment policy associated with their mailbox. Role assignment policies
are added directly to mailboxes, and each mailbox can only be associated with one role
assignment policy at a time.

Of the role assignment policies in your organization, one is marked as default. The default role
assignment policy is associated with new mailboxes that aren't explicitly assigned a specific
role assignment policy when they're created. The default role assignment policy should contain
the permissions that should be applied to the majority of your mailboxes.

Permissions are added to role assignment policies using end-user roles. End-user roles begin
with My and grant permissions for users to manage only the mailbox or distribution groups
they own. They can't be used to manage any other mailbox. Only end-user roles can be
assigned to role assignment policies.

When an end-user role is assigned to a role assignment policy, all of the mailboxes associated
with that role assignment policy receive the permissions granted by the role. Therefore, you
can add or remove permissions to sets of users without having to configure individual
mailboxes. The following figure shows that:

      End-user roles are assigned to role assignment policies. Role assignment policies can
      share the same end-user roles.

<!-- p.914 -->

     Role assignment policies are associated with mailboxes. Each mailbox can only be
     associated with one role assignment policy.

     After a mailbox is associated with a role assignment policy, the end-user roles are applied
     to that mailbox. The permissions granted by the roles are granted to the user of the
     mailbox.

Roles, role assignment policies, and mailboxes

The Default Role Assignment Policy is included with Exchange Server. As the name implies, it's
the default role assignment policy. If you want to change the permissions provided by this role
assignment policy, or if you want to create role assignment policies, see Work with role
assignment policies later in this topic.

Work with role groups
To manage your permissions using role groups in Exchange Server, we recommend that you
use the Exchange admin center (EAC). When you use the EAC to manage role groups, you can
add and remove roles and members, create role groups, and copy role groups with a few clicks
of your mouse. The EAC provides simple dialog boxes, such as the new role group dialog box,
shown in the following figure, to perform these tasks.

New role group dialog box in the EAC

<!-- p.915 -->

If none of the role groups included with Exchange Server have the permissions you need, you
can use the EAC to create a role group and add the roles that have the permissions you need.
For your new role group, you'll need to:

   1. Choose a name.

   2. Select the roles you want to add.

   3. Add members.

   4. Save it.

After you create the role group, you manage it like any other role group.

<!-- p.916 -->

If there's an existing role group that has some, but not all, of the permissions you need, you
can copy it and then make changes to create a role group. Copying an existing role group lets
you make changes to it without affecting the original role group. As part of copying the role
group, you can add a new name and description, add and remove roles to and from the new
role group, and add new members. When you create or copy a role group, you use the same
dialog box that's shown in the preceding figure.

Existing role groups can also be modified. You can add and remove roles from existing role
groups, and add and remove members from it at the same time, using an EAC dialog box
similar to the one in the preceding figure. By adding and removing roles to and from role
groups, you turn on and off administrative features for members of that role group.

  ７ Note

  Although you can determine which roles are assigned to built-in role groups, we
  recommend that you copy built-in role groups, modify the role group copy, and then add
  members to the role group copy.

Work with role assignment policies
To manage the permissions that you grant end users for them to manage their own mailbox in
Exchange Server, we recommend that you use the EAC. When you use the EAC to manage end-
user permissions, you can add roles, remove roles, and create role assignment policies with a
few clicks of your mouse. The EAC provides simple dialog boxes, such as the role assignment
policy dialog box, shown in the following figure, to perform these tasks.

Role assignment policy dialog box in the EAC

<!-- p.917 -->

Exchange Server includes a role assignment policy named Default Role Assignment Policy. This
role assignment policy enables users whose mailboxes are associated with it to do the
following:

     Join or leave distribution groups that allow members to manage their own membership.

     View and modify basic mailbox settings on their own mailbox, such as Inbox rules,
     spelling behavior, junk mail settings, and Microsoft ActiveSync devices.

     Modify their contact information, such as work address and phone number, mobile phone
     number, and pager number.

<!-- p.918 -->

     Create, modify, or view text message settings.

     View or modify voice mail settings.

     View and modify their marketplace apps.

     Create team mailboxes and connect them to Microsoft SharePoint lists.

If you want to add or remove permissions from the Default Role Assignment Policy or any
other role assignment policy, you can use the EAC. When you open the role assignment policy
in the EAC, select the checkbox next to the roles you want to assign to it or clear the checkbox
next to the roles you want to remove. The change you make to the role assignment policy is
applied to every mailbox associated with it.

If you want to assign different end-user permissions to the various types of users in your
organization, you can create role assignment policies. You can specify a new name for the role
assignment policy, and then select the roles you want to assign to the role assignment policy.
After you create a role assignment policy, you can associate it with mailboxes using the EAC.

If you want to determine which role assignment policy is the default, you need to use the
Exchange Management Shell. When you change the default role assignment policy, any
mailboxes that are created will be associated with the new default role assignment policy if one
wasn't explicitly specified. The role assignment policy associated with existing mailboxes
doesn't change when you select a new default role assignment policy.

Notes:

     If you select a checkbox for a role that has child roles, the checkboxes for the child roles
     are also selected. If you clear the checkbox for a role with child roles, the checkboxes for
     the child roles are also cleared.

     For detailed steps about how to create role assignment policies or make changes to
     existing role assignment policies, see the following topics:

         Manage role assignment policies

         Change the assignment policy on a mailbox

<!-- p.919 -->

Manage role groups in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

A management role group is a universal security group (USG) used in the Role Based Access
Control (RBAC) permissions model in Exchange Server. A management role group simplifies the
assignment of management roles to a group of users. All members of a role group are
assigned the same set of roles. For more information about role groups in Exchange Server, see
Understanding Management Role Groups.

For additional management tasks related to role groups, see Permissions.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 to 10 minutes

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Role groups" entry in the Role
      management permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Create a role group
If you want to customize the permissions that you can assign to a group of users, create a new
custom management role group.

Use the EAC to create a role group
   1. In the Exchange admin center (EAC), navigate to Permissions > Admin Roles and then
      click Add    .

<!-- p.920 -->

   2. In the New role group window, provide a name for the new role group.

   3. You can either select the roles that you want to be assigned to the role group and the
     members you want to be added to the role group now, or you can do this at another
     time.

   4. Select the write scope that you want to apply to the new role group.

   5. Click Save to create the role group.

Use the Exchange Management Shell to create a role group
To create a role group, see the Examples section in New-RoleGroup.

How do you know this worked?
To verify that you have successfully created a role group, do the following:

   1. In the EAC, navigate to Permissions > Admin Roles.

   2. Verify that the new role group appears in the role group list and then select it.

   3. Verify that members, assigned roles, and scope that you specified on the new role group
     are listed in the role group details pane.

Copy a role group

Use the EAC to copy a role group
If you have a role group that contains the permissions you want to grant to users, but you want
to apply a different management scope, or remove or add one or two management roles
without having to add all the other roles manually, you can copy the existing role group.

  ） Important

  You can't use the EAC to copy a role group if you've used the Exchange Management Shell
  to configure multiple management role scopes or exclusive scopes on the role group. If
  you've configured multiple scopes or exclusive scopes on the role group, you must use
  the Exchange Management Shell procedures later in this topic to copy the role group. For
  more information about management role scopes, see Understanding Management Role
  Scopes.
