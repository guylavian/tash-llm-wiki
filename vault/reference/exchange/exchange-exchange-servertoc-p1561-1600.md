---
title: "Exchange Server — pages 1561-1600"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1561-1600
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1561-1600
family: exchange
documentKind: "doc"
abstract: "This example enables Recipient Lookup on a Edge Transport server for the internal relay domain named Fabrikam Corp. All external recipients in the fabrikam.com domain are represented in Exchange as mail users. PowerShell Set-AcceptedDomain -Identity \"Fabrikam Corp\" -AddressBookE"
---

# Exchange Server — pages 1561-1600

<!-- p.1561 -->

This example enables Recipient Lookup on a Edge Transport server for the internal relay
domain named Fabrikam Corp. All external recipients in the fabrikam.com domain are
represented in Exchange as mail users.

  PowerShell

  Set-AcceptedDomain -Identity "Fabrikam Corp" -AddressBookEnabled $true

For detailed syntax and parameter information, see Set-AcceptedDomain.

How do you know this worked?
To verify that you've successfully modified an accepted domain, use either of the following
procedures:

     In the EAC, go to Mail flow > Accepted domains, and verify the property values.

     Notes:

        To verify that the accepted domain is the default domain, you need to select the
        accepted domain from the list, and then click Edit (   ). If Make this the default
        domain is selected, it's the default domain.

        You can't use the EAC to verify that Recipient Lookup is enabled or disabled for the
        accepted domain. You need to use the Exchange Management Shell.

     In the Exchange Management Shell, run the following command to verify the property
     values:

        PowerShell

        Get-AcceptedDomain | Format-Table -Auto
        Name,DomainName,DomainType,Default,AddressBookEnabled

Remove accepted domains
     You can't remove the default domain. First, you need to configure another accepted
     domain as the default domain.

     You can't remove an accepted domain that's defined anywhere in an email address policy
     (including in the disabled email address templates). To see all the domains that are used
     in email address policies, run the following command in the Exchange Management Shell:

<!-- p.1562 -->

        PowerShell

        Get-EmailAddressPolicy | Format-List Name,*EmailAddressTemplate*

     For more information about modifying email address policies, see Modify email address
     policies[Modify email address policies]).

Use the EAC to remove accepted domains
   1. In the EAC, go to Mail flow > Accepted domains, select the accepted domain from the
     list, and then click Remove (   ).

   2. In the Warning dialog that appears, click Yes to confirm.

Use the Exchange Management Shell to remove accepted
domains
To remove an accepted domain, use the following syntax:

  PowerShell

  Remove-AcceptedDomain -Identity <AcceptedDomainIdentity>

This example removes the accepted domain named Fabrikam Corp.

  PowerShell

  Remove-AcceptedDomain -Identity "Fabrikam Corp"

For detailed syntax and parameter information, see remove-AcceptedDomain.

How do you know this worked?
To verify that you've successfully removed an accepted domain, use either of the following
procedures:

     In the EAC, go to Mail flow > Accepted domains, and verify that the accepted domain is
     no longer listed.

     In the Exchange Management Shell, run the following command to verify that the
     accepted domain isn't listed:

<!-- p.1563 -->

       PowerShell

       Get-AcceptedDomain

Configure Exchange to accept mail for multiple
authoritative domains
These are some scenarios that require multiple authoritative domains:

     Your organization is changing its SMTP domain name.

     You want to provision different email addresses for different business units within your
     organization.

     You provide email hosting services, and you need to accept email for more than one
     SMTP domain.

After you configure one or more authoritative domains, you need to decide how to use those
domains in your organization. For example:

     Do you want to replace the existing primary (Reply-To:) address for the recipients, or add
     the new email address as a proxy address?

     Do you want to keep old email addresses as a proxy addresses so the recipients continue
     to receive mail that's sent to their old email addresses?

     Do you want the email addresses in the new authoritative domain to apply to all
     recipients and all types of recipients, or only to specific types of recipients or specific
     recipients based on their user properties (for example, only users in the Finance
     department)?

These are the steps that are required to configure Exchange to accept mail for multiple
authoritative domains:

   1. Create one or more authoritative domains as described in the Create accepted domains
     section.

     For example, if you already have contoso.com configured as an authoritative domain, add
     fourthcoffee.com as an authoritative domain.

   2. Create or modify an email address policy that uses the authoritative domains to meet
     your requirements. For example:

<!-- p.1564 -->

          Modify the default email address policy so all recipients get the required primary
          and proxy email addresses.

     For example, modify the default policy so <alias>@fourthcoffee.com is the primary SMTP
     email address, and <alias>@contoso.com is kept as a proxy address. For instructions, see
     Modify email address policies.

          Create a new email address policy that applies the required primary and proxy email
          addresses to a filtered set of recipients.

     For example, create a new policy named Fourth Coffee Recipients with the following
     settings:

          Precanned recipient filter: All users with mailboxes where the Company value is
          Fourth Coffee.

          Primary SMTP email address: <alias>@fourthcoffee.com.

          Additional proxy email addresses: None. The affected recipients can no longer
          receive messages sent to their old @contoso.com primary email address.

          Priority: 1. The first email address policy that identifies a recipient configures the
          recipient's email addresses. All other policies are ignored, even if the first policy is
          unapplied and can't configure the recipient's email addresses.

          For instructions, see Create email address policies.

   3. Apply the new or updated email address policy to the affected recipients. For instructions,
     see Apply email address policies to recipients.

To verify that you've configured Exchange to accept mail for multiple authoritative domains,
perform the following procedures:

   1. Send test messages to an affected recipient from a mailbox that's outside of your
     Exchange organization, and verify the email addresses that accept or reject mail.

   2. Send test messages from an affected mailbox to an external recipient, and verify the From
     address of the message.

<!-- p.1565 -->

Connectors on Exchange servers
Article • 04/30/2025

APPLIES TO:         2016      2019        Subscription Edition

Exchange uses connectors to enable incoming and outgoing mail flow on Exchange servers,
and also between services in the transport pipeline on the local Exchange server.

These are the types of connectors that are available in Exchange.

                                                                                           ﾉ   Expand table

 Connector             Description

 Receive               Receive connectors control incoming SMTP mail flow. They listen for incoming
 connectors            connections that match the configuration of the connector. Multiple default Receive
                       connectors are created when you install Exchange.
                       For more information, see Receive connectors.

 Send connectors       Send connectors control outgoing SMTP mail flow. A Send connector is chosen
                       based on the message recipients and the configuration of the connector. No default
                       Send connectors for external mail flow are created when you install Exchange, but
                       implicit and invisible Send connectors exist, and are used to route mail between
                       internal Exchange servers.
                       For more information, see Send connectors.

 Delivery agents       Delivery agents and Delivery Agent connectors control outgoing mail flow to non-
 and Delivery          SMTP systems. Outgoing messages are put into message queues for delivery to the
 Agent Connectors      non-SMTP system. Delivery agents and Delivery agent connectors are preferred over
                       Foreign connectors due to their improved performance and management.
                       For more information, see Delivery Agents and Delivery Agent Connectors.

 Foreign               Foreign connectors control outgoing mail flow to non-SMTP systems. Outgoing
 connectors            messages are written to files in a location called the Drop directory to be picked up
                       by the non-SMTP system.
                       For information, see Foreign Connectors.

<!-- p.1566 -->

Receive connectors in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

Exchange servers use Receive connectors to control inbound SMTP connections from:

      Messaging servers that are external to the Exchange organization.

      Services in the transport pipeline on the local Exchange server or on remote Exchange servers.

      Email clients that need to use authenticated SMTP to send messages.

You can create Receive connectors in the Transport service on Mailbox servers, the Front End Transport service on Mailbox servers, and on
Edge Transport servers. By default, the Receive connectors that are required for inbound mail flow are created automatically when you
install an Exchange Mailbox server, and when you subscribe an Edge Transport server to your Exchange organization.

A Receive connector is associated with the Mailbox server or Edge Transport server where it's created, and determines how that specific
server listens for SMTP connections. On Mailbox servers, the Receive connector is stored in Active Directory as a child object of the server.
On Edge Transport servers, the Receive connector is stored in Active Directory Lightweight Directory Services (AD LDS).

These are the important settings on Receive connectors:

      Local adapter bindings: Configure the combination of local IP addresses and TCP ports that the Receive connector uses to accept
      connections.

      Remote network settings: Configure the source IP addresses that the Receive connector listens to for connections.

      Usage type: Configure the default permission groups and smart host authentication mechanisms for the Receive connector.

      Permission groups: Configure who's allowed to use the Receive connector, and the permissions that they receive.

A Receive connector listens for inbound connections that match the configuration settings of the connector. Each Receive connector on
the Exchange server uses a unique combination of local IP address bindings, TCP ports, and remote IP address ranges that define if and
how connections from SMTP clients or servers are accepted.

Although the default Receive connectors are adequate in most cases, you can create custom Receive connectors for specific scenarios. For
example:

      To apply special properties to an email source, for example, a larger maximum message size, more recipients per message or more
      simultaneous inbound connections.

      To accept encrypted mail by using a specific TLS certificate.

On Mailbox servers, you can create and manage Receive connectors in the Exchange admin center (EAC) or in the Exchange Management
Shell. On Edge Transport servers, you can only use the Exchange Management Shell.

Receive connector changes in Exchange Server
These are the notable changes to Receive connectors in Exchange 2016 and Exchange 2019 compared to Exchange 2010:

      The TlsCertificateName parameter allows you to specify the certificate issuer and the certificate subject. This helps minimize the risk
      of fraudulent certificates.

      The TransportRole parameter allows you to distinguish between frontend (Client Access) and backend connectors on Mailbox servers.

Default Receive connectors created during setup
Several different Receive connectors are created by default when you install Exchange. By default, these connectors are enabled, and
protocol logging is disabled for most of them. For more information about protocol logging on Receive connectors, see Protocol logging.

<!-- p.1567 -->

Default Receive connectors in the Front End Transport service on Mailbox
servers
The primary function of Receive connectors in the Front End Transport service is to accept anonymous and authenticated SMTP
connections into your Exchange organization. The TransportRole property value for these connectors is FrontendTransport . The Front End
Transport service relays or proxies these connections to the Transport service for categorization and routing to the final destination.

The default Receive connectors that are created in the Front End Transport service on Mailbox servers are described in the following table.

                                                                                                                                    ﾉ   Expand table

 Name            Description      Protocol   TCP    Local IP    Remote IP address ranges                   Authentication        Permission groups
                                  logging    Port   address                                                mechanisms
                                                    bindings

 Client          Accepts          None       587    All         {::-                                       TLS                   ExchangeUsers
 Frontend        connections                        available   ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff,   BasicAuth
 <ServerName>    from                               IPv4 and    0.0.0.0-255.255.255.255} (all IPv4 and     BasicAuthRequireTLS
                 authenticated                      IPv6        IPv6 addresses)                            Integrated
                 SMTP clients.                      addresses
                                                    ( 0.0.0.0
                                                    and
                                                    [::]: )

 Default         Accepts          Verbose    25     All         {::-                                       TLS                   AnonymousUsers
 Frontend        anonymous                          available   ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff,   BasicAuth             ExchangeLegacyServers
 <ServerName>    connections                        IPv4 and    0.0.0.0-255.255.255.255} (all IPv4 and     BasicAuthRequireTLS   ExchangeServers
                 from external                      IPv6        IPv6 addresses)                            ExchangeServer
                 SMTP                               addresses                                              Integrated
                 servers. This                      ( 0.0.0.0
                 is the                             and
                 common                             [::]: )
                 messaging
                 entry point
                 into your
                 Exchange
                 organization.

 Outbound        Accepts          None       717    All         {::-                                       TLS                   ExchangeServers
 Proxy           authenticated                      available   ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff,   BasicAuth
 Frontend        connections                        IPv4 and    0.0.0.0-255.255.255.255} (all IPv4 and     BasicAuthRequireTLS
 <ServerName>    from the                           IPv6        IPv6 addresses)                            ExchangeServer
                 Transport                          addresses                                              Integrated
                 service on                         ( 0.0.0.0
                 Mailbox                            and
                 servers. The                       [::]: )
                 connections
                 are
                 encrypted
                 with the
                 Exchange
                 server's self-
                 signed
                 certificate.
                 This
                 connector is
                 used only if
                 the Send
                 connector is
                 configured to
                 use
                 outbound
                 proxy. For
                 more
                 information,
                 see
                 Configure
                 Send
                 connectors to

<!-- p.1568 -->

 Name            Description         Protocol    TCP     Local IP      Remote IP address ranges                    Authentication          Permission groups
                                     logging     Port    address                                                   mechanisms
                                                         bindings

                 proxy
                 outbound
                 mail.

Default Receive connectors in the Transport service on Mailbox servers
The primary function of Receive connectors in the Transport service is to accept authenticated and encrypted SMTP connections from
other transport services on the local Mailbox server or remote Mailbox servers in your organization. The TransportRole property value on
theses connectors is HubTransport . Clients don't directly connect to these connectors.

The default Receive connectors that are created in the Transport service on Mailbox servers are described in the following table.

                                                                                                                                              ﾉ   Expand table

 Name            Description          Protocol    TCP      Local IP     Remote IP address ranges                    Authentication          Permission groups
                                      logging     Port     address                                                  mechanisms
                                                           bindings

 Client Proxy    Accepts              None        465      All           {::-                                        TLS                     ExchangeServers
 <ServerName>    authenticated                             available    ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff,     BasicAuth               ExchangeUsers
                 client                                    IPv4 and     0.0.0.0-255.255.255.255} (all IPv4 and       BasicAuthRequireTLS
                 connections                               IPv6         IPv6 addresses)                              ExchangeServer
                 that are                                  addresses                                                 Integrated
                 proxied from                              ( 0.0.0.0
                 the Front End                             and
                 Transport                                 [::]: )
                 service.

 Default         Accepts              None        2525     All           {::-                                        TLS                     ExchangeLegacyServers
 <ServerName>    authenticated                             available    ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff,     BasicAuth               ExchangeServers
                 connections                               IPv4 and     0.0.0.0-255.255.255.255} (all IPv4 and       ExchangeServer          ExchangeUsers
                 from:                                     IPv6         IPv6 addresses)                              Integrated
                         The                               addresses
                         Front                             ( 0.0.0.0
                         End                               and
                         Transport                         [::]: )
                         service
                         on the
                         local or
                         remote
                         Mailbox
                         servers
                         The
                         Transport
                         service
                         on
                         remote
                         Mailbox
                         servers
                         The
                         Mailbox
                         Transport
                         service
                         on the
                         local or
                         remote
                         Mailbox
                         servers
                         Edge
                         Transport
                         servers

                 The
                 connections
                 are encrypted

<!-- p.1569 -->

 Name                Description        Protocol       TCP    Local IP         Remote IP address ranges                     Authentication         Permission groups
                                        logging        Port   address                                                       mechanisms
                                                              bindings

                     with the
                     Exchange
                     server's self-
                     signed
                     certificate.

Default Receive connectors in the Transport service on Edge Transport servers
The primary function of the Receive connector on Edge Transport servers is to accept mail from the Internet. Subscribing the Edge
Transport server to your Exchange organization automatically configures the connector permissions and authentication mechanisms that
are required for Internet mail flow to and from your organization. For more information, see Edge Transport servers.

The default Receive connector that's created in the Transport service on Edge Transport servers is described in the following table.

                                                                                                                                                    ﾉ   Expand table

 Name                         Description                Protocol         TCP      Local IP         Remote IP address          Authentication       Permission
                                                         logging          Port     address          ranges                     mechanisms           groups
                                                                                   bindings

 Default internal             Accepts anonymous          None             25       All available     {0.0.0.0-                 TLS                  AnonymousUsers
 receive connector            connections from                                     IPv4 addresses   255.255.255.255} (all      ExchangeServer       ExchangeServers
 <ServerName>                 external SMTP servers.                               ( 0.0.0.0 )      IPv4 addresses)                                 Partners

Implicit Receive connectors in the Mailbox Transport Delivery service on
Mailbox servers
In addition to the Receive connectors are created during the installation of Exchange servers, there's a special implicit Receive connector in
the Mailbox Transport Delivery service on Mailbox servers. This implicit Receive connector is automatically available, invisible, and requires
no management. The primary function of this connector is to accept mail from the Transport service on the local Mailbox server or remote
Mailbox servers in your organization.

The implicit Receive connector that exists in the Mailbox Transport Delivery service on Mailbox servers is described in the following table.

                                                                                                                                                    ﾉ   Expand table

 Name          Description              Protocol       TCP    Local IP           Remote IP address ranges                        Authentication     Permission
                                        logging        Port   address                                                            mechanisms         groups
                                                              bindings

 Mailbox       Accepts                  None           475    All available      {::-                                             ExchangeServer     ExchangeServers
 delivery      authenticated                                  IPv4 and           ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff,
 Receive       connections from                               IPv6               0.0.0.0-255.255.255.255} (all IPv4 and IPv6
 connector     the Transport                                  addresses          addresses)
               service on the                                 ( 0.0.0.0
               local or remote                                and [::]: )
               Mailbox servers.

Receive connector local address bindings
Local address bindings restrict the Receive connector to listen for SMTP connections on a specific local IP address (network adapter) and
TCP port. Typically, the combination of local IP address and TCP port is unique for every Receive connector on a server. However, multiple
Receive connectors on a server can have the same local IP addresses and TCP ports if the remote IP address ranges are different. For more
information, see the Receive connector remote addresses section.

By default, a Receive connector listens for connections on all available local IPv4 and IPv6 addresses ( 0.0.0.0 and [::]: ). If the server has
multiple network adapters, you can configure Receive connectors to accept connections only from IP addresses that are configured for a
specific network adapter. For example, on an Internet-facing Exchange server, you can have a Receive connector that's bound to the IP

<!-- p.1570 -->

address of the external network adapter to listen for anonymous Internet connections. You can have a separate Receive connector that's
bound to the IP address of the internal network adapter to listen for authenticated connections from internal Exchange servers.

  ７ Note

  If you bind a Receive connector to a specific IP address, make sure that the address is configured on a local network adapter. If you
  specify an invalid local IP address, the Microsoft Exchange Transport service may fail to start when the server or service is restarted.

In the EAC, you use the Network adapter bindings field to configure the local address bindings in the new Receive connector wizard, or on
the Scoping tab in the properties of existing Receive connectors. In the Exchange Management Shell, you use the Bindings parameter on
the New-ReceiveConnector and Set-ReceiveConnector cmdlets. Depending on the usage type that you select, you might not be able to
configure the local address bindings when you create the Receive connector, but you can modify them after you create the Receive
connector. The affected usage types are identified in the Receive connector usage types section.

Receive connector remote addresses
Remote addresses define from where the Receive connector receives SMTP connections. By default, Receive connectors listen for
connections from all IPv4 and IPv6 addresses (0.0.0.0-255.255.255.255 and ::-ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff). If you create a custom Receive
connector to receive mail from a specific source, configure the connector to listen for connections only from the specific IP address or
address ranges.

Multiple Receive connectors on the server can have overlapping remote IP address ranges as long as one range is completely overlapped
by another. When remote IP address ranges overlap, the remote IP address range that has the most specific match to the connecting
server's IP address is used.

For example, consider the following Receive connectors in the Front End Transport service on the server named Exchange01:

     Connector name: Client Frontend Exchange01

         Network adapter bindings: All available IPv4 on port 25.

         Remote network settings: 0.0.0.0-255.255.255.255

     Connector name: Custom Connector A

         Network adapter bindings: All available IPv4 on port 25.

         Remote network settings: 192.168.1.0-192.168.1.255

     Connector name: Custom Connector B

         Network adapter bindings: All available IPv4 on port 25.

         Remote network settings: 192.168.1.75

SMTP connections from 192.168.1.75 are accepted by Custom Connector B, because that connector has the most specific IP address
match.

SMTP connections from 192.168.1.100 are accepted by Custom Connector A, because that connector has the most specific IP address
match.

In the EAC, you use the Remote network settings field to configure the remote IP addresses in the new Receive connector wizard, or on
the Scoping tab in the properties of existing Receive connectors. In the Exchange Management Shell, you use the RemoteIPRanges
parameter on the New-ReceiveConnector and Set-ReceiveConnector cmdlets.

Receive connector usage types
The usage type determines the default security settings for the Receive connector. The usage type specifies who is authorized to use the
connector, the permissions they get, and the authentication methods that are supported.

When you use the EAC to create Receive connectors, the wizard prompts you to select the Type value for the connector. When you use the
New-ReceiveConnector cmdlet in the Exchange Management Shell, you use the Usage parameter with one of the available values (for

<!-- p.1571 -->

example, -Usage Custom ), or the designated switch for the usage type (for example, -Custom ).

You can specify the connector usage type only when you create Receive connectors. After you create a connector, you can modify the
available authentication mechanisms and permission groups in the EAC, or by using the Set-ReceiveConnector cmdlet in the Exchange
Management Shell.

The available usage types are described in the following table.

                                                                                                                                             ﾉ   Expand table

 Usage      Permission groups                Authentication mechanisms          Comments
 type       assigned                         available

 Client     Exchange users                   Transport Layer Security ( TLS )   Used by POP3 and IMAP4 clients that need to submit email messages by
            ( ExchangeUsers )                Basic authentication               using authenticated SMTP.
                                             ( BasicAuth )                      When you create a Receive connector of this usage type in the EAC or in the
                                             Offer basic authentication only    Exchange Management Shell, you can't select the local IP address bindings or
                                             after starting TLS                 TCP port. By default, this usage type is bound to all local IPv4 and IPv6
                                             ( BasicAuthRequireTLS )            addresses on TCP port 587. You can change these bindings after you create
                                             Integrated Windows                 the connector.
                                             authentication ( Integrated )      This usage type isn't available on Edge Transport servers.

 Custom     None selected ( None )           Transport Layer Security ( TLS )   Used in cross-forest scenarios, for receiving mail from third-party messaging
                                                                                servers, and for external relay.
                                                                                After you create a Receive connector of this usage type, you need to add
                                                                                permissions groups in the EAC or in the Exchange Management Shell.

 Internal   Legacy Exchange servers          Transport Layer Security ( TLS )   Used in cross-forest scenarios, for receiving mail from previous versions of
            ( ExchangeLegacyServers )        Exchange Server                    Exchange, for receiving mail from third-party messaging servers, or on Edge
            Exchange servers                 authentication                     Transport servers to receive outbound mail from the internal Exchange
            ( ExchangeServers )              ( ExchangeServers )                organization.
                                                                                When you create a Receive connector of this usage type in the EAC or in the
                                                                                Exchange Management Shell, you can't select the local IP address bindings or
                                                                                TCP port. By default, the connector is bound to all local IPv4 and IPv6
                                                                                addresses on TCP port 25. You can change these bindings after you create the
                                                                                connector.
                                                                                The ExchangeLegacyServers permission group isn't available on Edge
                                                                                Transport servers.

 Internet   Anonymous users                  Transport Layer Security ( TLS )   Used to receive mail from the Internet.
            ( AnonymousUsers )                                                  When you create a Receive connector of this usage type in the EAC or in the
                                                                                Exchange Management Shell, you can't select the remote IP addresses. By
                                                                                default, the connector accepts remote connections from all IPv4 addresses
                                                                                (0.0.0.0-255.255.255.255). You can change these bindings after you create the
                                                                                connector.

 Partner    Partners ( Partners )            Transport Layer Security ( TLS )   Used to configure secure communication with an external partner (mutual TLS
                                                                                authentication, also known as domain secure).

Receive connector authentication mechanisms
Authentication mechanisms specify the logon and encryption settings that are used for incoming SMTP connections. You can configure
multiple authentication mechanisms for a Receive connector. In the EAC, authentication mechanisms are available in the Security tab in the
properties of the Receive connector. In the Exchange Management Shell, permission groups are available in the AuthMechanisms
parameter on the New-ReceiveConnector and Set-ReceiveConnector cmdlets.

The available authentication mechanisms are described in the following table.

                                                                                                                                             ﾉ   Expand table

 Authentication mechanism                 Description

 None selected ( None )                   No authentication.

 Transport Layer Security (TLS) ( TLS )   Advertise STARTTLS in the EHLO response. TLS encrypted connections require a server certificate that includes the
                                          name that the Receive connector advertises in the EHLO response. For more information, see Modify the SMTP

<!-- p.1572 -->

 Authentication mechanism              Description

                                       banner on Receive connectors. Other Exchange servers in your organization trust the server's self-signed certificate,
                                       but clients and external servers typically use a trusted third-party certificate.

 Basic authentication ( BasicAuth )    Basic authentication (clear text).

 Offer basic authentication only       Basic authentication that's encrypted with TLS.
 after starting TLS
 ( BasicAuthRequireTLS )

 Integrated Windows authentication     NTLM and Kerberos authentication.
 ( Integrated )

 Exchange Server authentication        Generic Security Services application programming interface (GSSAPI) and Mutual GSSAPI authentication.
 ( ExchangeServer )

 Externally secured                    The connection is presumed to be secured by using a security mechanism that's external to Exchange. The
 ( ExternalAuthoritative )             connection may be an Internet Protocol security (IPsec) association or a virtual private network (VPN). Alternatively,
                                       the servers may reside in a trusted, physically controlled network.
                                       This authentication mechanism requires the ExchangeServers permission group. This combination of authentication
                                       mechanism and security group permits the resolution of anonymous sender email addresses for messages that are
                                       received through the connector.

Receive connector permission groups
A permission group is a predefined set of permissions that's granted to well-known security principals and assigned to a Receive connector.
Security principals include user accounts, computer accounts, and security groups (objects that are identifiable by a security identifier or
SID that can have permissions assigned to them). Permission groups define who can use the Receive connector, and the permissions that
they get. You can't create permission groups, nor can you modify the permission group members or the default permissions of the
permission group.

In the EAC, permission groups are available in the Security tab in the properties of the Receive connector. In the Exchange Management
Shell, permission groups are available in the PermissionGroups parameter in the New-ReceiveConnector and Set-ReceiveConnector
cmdlets.

The available permission groups are described in the following table.

                                                                                                                                             ﾉ   Expand table

 Permission group                     Associated security principals                                                            Permissions granted

 Anonymous users ( Anonymous )        NT AUTHORITY\ANONYMOUS LOGON                                                              ms-Exch-Accept-Headers-
                                                                                                                                Routing
                                                                                                                                ms-Exch-SMTP-Accept-Any-
                                                                                                                                Sender
                                                                                                                                ms-Exch-SMTP-Accept-
                                                                                                                                Authoritative-Domain-Sender
                                                                                                                                ms-Exch-SMTP-Submit

 Exchange users ( ExchangeUsers )     NT AUTHORITY\Authenticated Users                                                          ms-Exch-Accept-Headers-
                                                                                                                                Routing
                                                                                                                                ms-Exch-Bypass-Anti-Spam
                                                                                                                                ms-Exch-SMTP-Accept-Any-
                                                                                                                                Recipient
                                                                                                                                ms-Exch-SMTP-Submit

 Exchange servers                     <Domain>\Exchange Servers                                                                 ms-Exch-Accept-Headers-
 ( ExchangeServers )                  MS Exchange\Edge Transport Servers                                                        Forest
                                      MS Exchange\Hub Transport Servers                                                         ms-Exch-Accept-Headers-
                                      Note: These security principals also have other internal permissions assigned to them.    Organization
                                      For more information, see the end of the Receive connector permissions section.           ms-Exch-Accept-Headers-
                                                                                                                                Routing
                                                                                                                                ms-Exch-Bypass-Anti-Spam
                                                                                                                                ms-Exch-Bypass-Message-
                                                                                                                                Size-Limit
                                                                                                                                ms-Exch-SMTP-Accept-Any-
                                                                                                                                Recipient

<!-- p.1573 -->

 Permission group                     Associated security principals                                                        Permissions granted

                                                                                                                             ms-Exch-SMTP-Accept-Any-
                                                                                                                            Sender
                                                                                                                             ms-Exch-SMTP-Accept-
                                                                                                                            Authentication-Flag
                                                                                                                             ms-Exch-SMTP-Accept-
                                                                                                                            Authoritative-Domain-Sender
                                                                                                                             ms-Exch-SMTP-Accept-Exch50
                                                                                                                             ms-Exch-SMTP-Submit

 Exchange servers                     MS Exchange\Externally Secured Servers                                                 ms-Exch-Accept-Headers-
 ( ExchangeServers )                                                                                                        Routing
                                                                                                                             ms-Exch-Bypass-Anti-Spam
                                                                                                                             ms-Exch-Bypass-Message-
                                                                                                                            Size-Limit
                                                                                                                             s-Exch-SMTP-Accept-Any-
                                                                                                                            Recipient
                                                                                                                             ms-Exch-SMTP-Accept-Any-
                                                                                                                            Sender
                                                                                                                             ms-Exch-SMTP-Accept-
                                                                                                                            Authentication-Flag
                                                                                                                             ms-Exch-SMTP-Accept-
                                                                                                                            Authoritative-Domain-Sender
                                                                                                                             ms-Exch-SMTP-Accept-Exch50
                                                                                                                             ms-Exch-SMTP-Submit

 Legacy Exchange servers              <Domain>\ExchangeLegacyInterop                                                         ms-Exch-Accept-Headers-
 ( ExchangeLegacyServers )                                                                                                  Routing
                                                                                                                             ms-Exch-Bypass-Anti-Spam
                                                                                                                             ms-Exch-Bypass-Message-
                                                                                                                            Size-Limit
                                                                                                                             ms-Exch-SMTP-Accept-Any-
                                                                                                                            Recipient
                                                                                                                             ms-Exch-SMTP-Accept-Any-
                                                                                                                            Sender
                                                                                                                             ms-Exch-SMTP-Accept-
                                                                                                                            Authentication-Flag
                                                                                                                             ms-Exch-SMTP-Accept-
                                                                                                                            Authoritative-Domain-Sender
                                                                                                                             ms-Exch-SMTP-Accept-Exch50
                                                                                                                             ms-Exch-SMTP-Submit

 Partners ( Partner )                 MS Exchange\Partner Servers                                                            ms-Exch-Accept-Headers-
                                                                                                                            Routing
                                                                                                                             ms-Exch-SMTP-Submit

The permissions are explained in the Receive connector permissions section later in this topic.

Receive connector permissions
Typically, you apply permissions to Receive connectors by using permission groups. However, you can configure granular permissions on a
Receive connector by using the Add-ADPermission and Remove-ADPermission cmdlets.

Receive connector permissions are assigned to security principals by the permission groups for the connector. When an SMTP server or
client establishes a connection to a Receive connector, the Receive connector permissions determine whether the connection is accepted,
and how messages are processed.

The available Receive connector permissions are described in the following table.

                                                                                                                                         ﾉ   Expand table

 Receive connector           Description
 permission

 ms-Exch-Accept-Headers-     Controls the preservation of Exchange forest headers in messages. Forest header names start with X-MS-Exchange-Forest-. If
                             this permission isn't granted, all forest headers are removed from messages.

<!-- p.1574 -->

 Receive connector          Description
 permission

 Forest

 ms-Exch-Accept-Headers-    Controls the preservation of Exchange organization headers in messages. Organization header names start with X-MS-
 Organization               Exchange-Organization-. If this permission isn't granted, all organization headers are removed from messages.

 ms-Exch-Accept-Headers-    Controls the preservation of Received and Resent-* headers in messages. If this permission isn't granted, all of these headers
 Routing                    are removed from messages.

 ms-Exch-Bypass-Anti-       Allows SMTP clients or servers to bypass antispam filtering.
 Spam

 ms-Exch-Bypass-Message-    Allows SMTP clients or servers to submit messages that exceed the maximum message size that's configured for the Receive
 Size-Limit                 connector.

 ms-Exch-SMTP-Accept-       Allows SMTP clients or servers to relay messages through the Receive connector. If this permission isn't granted, only messages
 Any-Recipient              that are sent to recipients in accepted domains that are configured for the Exchange organization are accepted by the Receive
                            connector.

 ms-Exch-SMTP-Accept-       Allows SMTP clients or servers to bypass the sender address spoofing check that normally requires the sender's email address
 Any-Sender                 to be in an accepted domain that's configured for Exchange organization.

 ms-Exch-SMTP-Accept-       Controls whether messages from SMTP clients or servers are treated as authenticated. If this permission isn't granted, messages
 Authentication-Flag        from theses sources are identified as external (unauthenticated). This setting is important for distribution groups that are
                            configured to accept mail only from internal recipients (for example, the RequireSenderAuthenticationEnabled parameter value
                            for the group is $true ).

 ms-Exch-SMTP-Accept-       Allows access to the Receive connector by senders that have email addresses in authoritative domains that are configured for
 Authoritative-Domain-      the Exchange organization.
 Sender

 ms-Exch-SMTP-Accept-       Allows SMTP clients or servers to submit XEXCH50 commands on the Receive connector. The X-EXCH50 binary large object
 Exch50                     (BLOB) was used by older versions of Exchange (Exchange 2003 and earlier) to store Exchange data in messages (for example,
                            the spam confidence level or SCL).

 ms-Exch-SMTP-Submit        This permission is required to submit messages to Receive connectors. If this permission isn't granted, the MAIL FROM and
                            AUTH commands will fail.

Notes:

        In addition to the documented permissions, there are permissions that are assigned to all of the security principals in the Exchange
        servers ( ExchangeServers ) permission group except MS Exchange\Externally Secured Servers . These permissions are reserved for
        internal Microsoft use, and are presented here for reference purposes only.

           ms-Exch-SMTP-Accept-Xattr

           ms-Exch-SMTP-Accept-XProxyFrom

           ms-Exch-SMTP-Accept-XSessionParams

           ms-Exch-SMTP-Accept-XShadow

           ms-Exch-SMTP-Accept-XSysProbe

           ms-Exch-SMTP-Send-XMessageContext-ADRecipientCache

           ms-Exch-SMTP-Send-XMessageContext-ExtendedProperties

           ms-Exch-SMTP-Send-XMessageContext-FastIndex

        Permissions names that contain ms-Exch-Accept-Headers- are part of the header firewall feature. For more information, see Header
        firewall.

Receive connector permission procedures
To see the permissions that are assigned to security principals on a Receive connector, use the following syntax in the Exchange
Management Shell:

<!-- p.1575 -->

  PowerShell

  Get-ADPermission -Identity <ReceiveConnector> [-User <SecurityPrincipal>] | where {($_.Deny -eq $false) -and
  ($_.IsInherited -eq $false)} | Format-Table User,ExtendedRights

For example, to see the permissions that are assigned to all security principals on the Receive connector named Client Frontend
Mailbox01, run the following command:

  PowerShell

  Get-ADPermission -Identity "Client Frontend Mailbox01" | where {($_.Deny -eq $false) -and ($_.IsInherited -eq $false)} |
  Format-Table User,ExtendedRights

To see the permissions that are assigned only to the security principal NT AUTHORITY\Authenticated Users on the Receive connector named
Default Mailbox01, run the following command:

  PowerShell

  Get-ADPermission -Identity "Default Mailbox01" -User "NT AUTHORITY\Authenticated Users" | where {($_.Deny -eq $false) -and
  ($_.IsInherited -eq $false)} | Format-Table User,ExtendedRights

To add permissions to a security principal on a Receive connector, use the following syntax:

  PowerShell

  Add-ADPermission -Identity <ReceiveConnector> -User <SecurityPrincipal> -ExtendedRights "<Permission1>","<Permission2>"...

To remove permissions from a security principal on a Receive connector, use the following syntax:

  PowerShell

  Remove-ADPermission -Identity <ReceiveConnector> -User <SecurityPrincipal> -ExtendedRights "<Permission1>","
  <Permission2>"...

<!-- p.1576 -->

Scenarios for custom Receive connectors in
Exchange Server
Article • 04/30/2025

APPLIES TO:         2016    2019      Subscription Edition

By default, Exchange Server comes with many different Receive connectors that are configured
for most common mail flow scenarios. For more information about these connectors, see
Default Receive connectors created during setup.

However, you might need to process messages from another messaging system that's not
running Exchange. Or, if you have a network appliance that performs policy checks and then
routes messages to your Exchange server, you'll need to manually configure a Receive
connector.

If you need to create a custom Receive connector, consider these issues:

      You can create custom Receive connectors in the following services on Exchange servers:

         Mailbox servers: The Transport (Hub) service and the Front End Transport service.

         Edge Transport servers: The Transport service.

      Each Receive connector on an Exchange server requires a unique combination of network
      adapter bindings (the combination of local IP address and TCP port) and remote
      network settings (remote IP addresses).

         A default Receive connector that listens on port 25 on all available local IP addresses
         from all remote IP addresses already exists on all Mailbox servers and Edge Transport
         servers.

         If you create a custom Receive connector that listens on port 25 on all available local IP
         addresses, but the connector is restricted to a limited range of remote IP addresses, the

<!-- p.1577 -->

       new connector won't conflict with any of the default Receive connectors on the server.
       For a detailed explanation, see Receive connector remote addresses.

       If you can't restrict the remote IP addresses of the custom Receive connector, your only
       other option is to restrict the local IP address that the connector uses for port 25. You'll
       need to modify the local IP address of the conflicting default Receive connector, and
       then use a different local IP address when you create custom Receive connector.

     For Mailbox servers, you need to create custom Receive connectors that use port 25 in
     the Front End Transport service, not the Transport (Hub) service. Receive connectors in the
     Transport service on Mailbox servers accept authenticated and encrypted SMTP
     connections from other transport services on the local server or other Mailbox servers in
     your organization. Clients don't directly connect to these connectors. This is different than
     Exchange 2010, because you could only create Receive connectors on Hub Transport
     servers (not Client Access servers).

Read more about Receive connectors in Exchange Server see, Receive connectors.

What do you need to know before you begin?
     Estimated time to complete each procedure: 10 minutes

     The Exchange admin center (EAC) procedures are only available on Mailbox servers. For
     more information about the EAC, see Exchange admin center in Exchange Server.

     The Exchange Management Shell procedures are available on Mailbox servers and Edge
     Transport servers. To learn how to open the Exchange Management Shell in your on-
     premises Exchange organization, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Receive connectors" entry in the
     Mail flow permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Scenario 1: Receive email from the Internet

<!-- p.1578 -->

For this scenario, the Receive connector listens for anonymous SMTP connections on port 25
from all remote IP addresses. Typically, you don't need to manually configure a Receive
connector to receive mail from the Internet. A Receive connector with these settings is
automatically created by the installation of a Mailbox server or an Edge Transport server:

     The Receive connector named Default Frontend <ServerName> in the Front End
     Transport service on Mailbox servers.

     The Receive connector named Default internal receive connector <ServerName> on Edge
     Transport servers.

If one of these connectors exists, and you try to create a custom Receive connector on the
server that also listens for anonymous SMTP connections on port 25 from all remote IP
addresses, you'll get an error. You'll need to change the network adapter binding on the
conflicting Receive connector to a specific local IP address. When you create the custom
Internet Receive connector, you'll need to specify a different network adapter binding.

Use the EAC to create an Internet Receive connector on
Mailbox servers
   1. In the EAC, go to Mail flow > Receive connectors, and then click Add (    ).

   2. The New receive connector wizard opens. On the first page, configure these settings:

           Name: Type something descriptive. For example, Internet Receive Connector.

           Role: Select Frontend Transport.

           Type: Select Internet.

     When you're finished, click Next.

   3. On the last page of the wizard, do one of these steps in the Network adapter bindings
     section:

           If you're recreating an Internet Receive connector to replace the missing default
           Receive connector named Default Frontend <ServerName> on the Mailbox server,
           leave the default values of IP addresses: (All available IPv4) and Port: 25 (when you
           click Finish, you won't receive an error message).

           If you're creating an Internet Receive connector while the default Receive connector
           named Default Frontend <ServerName> still exists on the Mailbox server, do these
           steps:

<!-- p.1579 -->

               a. Select the default entry IP addresses: (All available IPv4) and Port: 25, and then
                 click Edit (   ).

               b. In the Edit IP address dialog that opens, configure these settings:

                    Address: Select Specify an IPv4 address or an IPv6 address, and type in a
                    valid local IP address to use for the connector.

                    Port: Leave the default value 25 selected.

                 When you're finished, click Save.

         ７ Note

         After you've created the new Internet Receive connector on the Mailbox server, be
         sure to modify the local IP address settings in the properties of the default Receive
         connector named Default Frontend <ServerName>. You'll need to go to Scoping >
         Network adapter bindings in the properties of the connector, and then select a
         different local IP address to replace the default IP addresses: (All available IPv4) and
         Port: 25 entry.

     When you're finished, click Finish.

Use the Exchange Management Shell to create an Internet
Receive connector
To create an Internet Receive connector, use this syntax:

  PowerShell

  New-ReceiveConnector -Name <UniqueName> [-TransportRole Frontend] -Internet -
  Bindings <UniqueValidLocalIPAddress>

This example creates a new Receive connector named Internet Receive Connector on a Mailbox
server that listens on port 25 on the local IP address 10.1.15 from all remote IP addresses:

  PowerShell

  New-ReceiveConnector -Name "Internet Receive Connector" -TransportRole Frontend -
  Internet -Bindings 10.10.1.1:25

Notes:

<!-- p.1580 -->

     To run this command on an Edge Transport server, omit the TransportRole parameter.

     If another Receive connector is configured to listen on port 25 using all available local IP
     addresses on the server, you'll need to use the Bindings parameter on the Set-
     ReceiveConnector cmdlet to specify a unique local IP address for the other connector
     after you create the new Internet Receive connector.

This example creates a new Receive connector named Internet Receive Connector that listens
on port 25 from all remote IP addresses, but on all available local IP addresses. You can only
run this command if the server has no other Receive connectors that are configured to listen
on port 25 using all available local IP addresses.

  PowerShell

  New-ReceiveConnector -Name "Internet Receive Connector" -TransportRole Frontend -
  Internet -Bindings "0.0.0.0","[::]:"

Note: To run this command on an Edge Transport server, omit the TransportRole parameter.

For detailed syntax and parameter information, see New-ReceiveConnector.

How do you know this worked?
To verify that you've successfully created a Receive connector to receive messages from the
Internet, do any of these steps:

     In the EAC, go to Mail flow > Receive connectors, select the Receive connector, select
     Edit (    ), and verify the property values

     In the Exchange Management Shell, run this command on the server, and verify the
     property values:

        PowerShell

        Get-ReceiveConnector | where {$_.Bindings -like '*25' -AND
        $_.PermissionGroups -like '*AnonymousUsers*'} | Format-List
        Identity,Bindings,RemoteIPRanges,PermissionGroups

     Enable protocol logging for the Receive connector. For more information, see Configure
     protocol logging.

     From an external client, send a test message to someone in your organization. You can
     also connect to the Receive connector by using Telnet. For more information, see Use
     Telnet to test SMTP communication on Exchange servers.

<!-- p.1581 -->

Scenario 2: Receive email from a partner
For this scenario, the Receive connector listens for TLS authenticated SMTP connections on
port 25, but only from the specific IP addresses of the partner organization. No default Receive
connector is suitable for this scenario; you need to create a custom Receive connector.

Note: Creating a dedicated Receive connector is only one step in TLS encrypting
communication between your organization a trusted partner (for example, creating and
installing certificates).

Use the EAC to create a Receive connector to encrypt
messages from a partner on Mailbox servers
   1. In the EAC, go to Mail flow > Receive connectors, and then click Add (       ).

   2. The New receive connector wizard opens. On the first page, configure these settings:

            Name: Type something descriptive. For example, TLS Encrypted Messages from
            Fabrikam.com.

            Role: Select Frontend Transport.

            Type: Select Partner.

      When you're finished, click Next.

   3. On the second page of the wizard, do one of these steps in the Network adapter
      bindings section:

            Leave the default values of IP addresses: (All available IPv4) and Port: 25.

            If it's required for your scenario, you can restrict the Receive connector to a valid
            local IP address on the server:

             a. Select the default entry IP addresses: (All available IPv4) and Port: 25, and then
               click Edit (   ).

            b. In the Edit IP address dialog that opens, configure these settings:

                   Address: Select Specify an IPv4 address or an IPv6 address, and type in a
                   valid local IP address to use for the connector.

                   Port: Leave the default value 25 selected.

               When you're finished, click Save.

<!-- p.1582 -->

     When you're finished, click Next.

   4. On the last page of the wizard, configure these settings in the Remote network settings
     section:

      a. Select the default entry 0.0.0.0-255.255.255.255, and then click Edit (   ).

     b. In the Edit IP address dialog that opens, enter the IP address or IP address range of
          the remote partner organization.

          When you're finished, click Save.

     When you're finished, click Finish.

Use the Exchange Management Shell to create a Receive
connector to encrypt messages from a partner
To create a Receive connector that uses TLS to encrypt messages from a partner, use this
syntax:

  PowerShell

  New-ReceiveConnector -Name <UniqueName> [-TransportRole Frontend] -Partner -
  Bindings <0.0.0.0:25 | LocalIPAddress:25> -RemoteIPRanges <RemoteIPAddresses>

This example creates a Receive connector named Fabrikam.com TLS on a Mailbox server that
only accepts messages from the IP addresses 17.17.17.1/24 using all available local IP
addresses.

  PowerShell

  New-ReceiveConnector -Name "Fabrikam.com TLS" -TransportRole Frontend -Partner -
  RemoteIPRanges 17.17.17.1/24 -Bindings 0.0.0.0:25

Note: To run this command on an Edge Transport server, omit the TransportRole parameter.

For detailed syntax and parameter information, see New-ReceiveConnector.

How do you know this worked?
To verify that you've successfully created a Receive connector to receive TLS encrypted
messages from a partner, do any of these steps:

<!-- p.1583 -->

     In the EAC, go to Mail flow > Receive connectors, select the Receive connector, select
     Edit (     ), and verify the property values

     In the Exchange Management Shell, run this command on the server, and verify the
     property values:

        PowerShell

        Get-ReceiveConnector | where {$_.Bindings -like '*25' -AND
        $_.PermissionGroups -like '*Partners*'} | Format-List
        Identity,Bindings,RemoteIPRanges,PermissionGroups

     Enable protocol logging for the Receive connector. For more information, see Configure
     protocol logging.

     Have someone in the partner organization send a test message to someone in your
     organization. Verify that the message is encrypted (you can verify that TLS is used by
     checking the message header).

Scenario 3: Receive messages from a server,
service, or device that doesn't use Exchange
For this scenario, the Receive connector listens for connections on port 25, but only from the
specific IP address of the service, or device. It's also likely that this scenario requires some type
of authentication (consult the documentation for the service or device).

Use the EAC to create a Receive connector that only accepts
messages from a specific service or device on Mailbox servers
   1. In the EAC, go to Mail flow > Receive connectors, and then click Add (        ).

   2. The New receive connector wizard opens. On the first page, configure these settings:

              Name: Type something descriptive. For example, Inbound mail from security
              appliance.

              Role: Select Frontend Transport.

              Type: Select Custom.

     When you're finished, click Next.

<!-- p.1584 -->

3. On the second page of the wizard, do one of these steps in the Network adapter
  bindings section:

        Leave the default values of IP addresses: (All available IPv4) and Port: 25.

        If it's required for your scenario, you can restrict the Receive connector to a valid
        local IP address on the server:

         a. Select the default entry IP addresses: (All available IPv4) and Port: 25, and then
             click Edit (   ).

        b. In the Edit IP address dialog that opens, configure these settings:

                 Address: Select Specify an IPv4 address or an IPv6 address, and type in a
                 valid local IP address to use for the connector.

                 Port: Leave the default value 25 selected.

             When you're finished, click Save.

  When you're finished, click Next.

4. On the last page of the wizard, configure these settings in the Remote network settings
  section:

  a. Select the default entry 0.0.0.0-255.255.255.255, and then click Edit (     ).

  b. In the Edit IP address dialog that opens, enter the IP address or IP address range of
     the service or device.

     When you're finished, click Save.

  When you're finished, click Finish.

5. Back at Mail flow > Receive connectors, select the connector you just created, and then
  click Edit (    ).

6. On the Security tab, configure the combination of authentication mechanisms and
  permission groups that are required for the service or device. For example:

        Leave Transport Layer Security (TLS) selected, select Basic authentication, and then
        select the Anonymous users permission group.

        Clear Transport Layer Security (TLS), select Basic authentication and Exchange
        server authentication, and then select the Exchange users and Legacy Exchange
        servers permission group.

<!-- p.1585 -->

           For more information about permission groups, see Receive connector permission
           groups.

               Ｕ Caution

               Be very careful using the authentication mechanism Externally secured with the
               permission group Exchange servers. This combination allows the remote IP
               addresses specified in the Remote network settings section on the Scoping tab
               to anonymously relay messages through the Exchange server. For more
               information, see Allow anonymous relay on Exchange servers.

               ２ Warning

               When using the authentication mechanism Basic authentication or Offer basic
               authentication only after starting TLS without the permission group
               Anonymous users as an authenticated relay connector, the routing of mail will
               always try to select the authenticated user or the organization's arbitration
               mailbox active mailbox server.

     When you're finished, click Save.

Use the Exchange Management Shell to create a Receive
connector that only accepts messages from a specific service
or device
To create a Receive connector that only accepts messages from a specific service or device, use
this syntax:

  PowerShell

  New-ReceiveConnector -Name <UniqueName> [-TransportRole Frontend] -Custom -
  Bindings <0.0.0.0:25 | LocalIPAddress:25> -RemoteIPRanges <RemoteIPAddresses> -
  AuthMechanism <AuthMechanism1>,<AuthMechanism2>... - PermissionGroups
  <PermissionGroup1>,<PermissionGroup2>...

This example creates a Receive connector named Inbound From Service on a Mailbox server:

     Bindings: All available local IP addresses.

     Remote IP address ranges: 192.168.5.1/24.

     Authentication mechanisms: Basic authentication.

<!-- p.1586 -->

     Permission groups: Anonymous users.

  PowerShell

  New-ReceiveConnector -Name "Inbound From Service" -TransportRole Frontend -Custom
  -Bindings 0.0.0.0:25 -RemoteIPRanges 192.168.10.5 -AuthMechanism BasicAuth -
  PermissionGroups AnonymousUsers

Note: To run this command on an Edge Transport server, omit the TransportRole parameter.

For detailed syntax and parameter information, see New-ReceiveConnector.

How do you know this worked?
To verify that you've successfully created a Receive connector that only accepts messages from
a specific service or device, do any of these steps:

     In the EAC, go to Mail flow > Receive connectors, select the Receive connector, select
     Edit (      ), and verify the property values.

     In the Exchange Management Shell, run this command on the server, and verify the
     property values:

           PowerShell

           Get-ReceiveConnector | where {$_.Bindings -like '*25'} | Format-List
           Identity,RemoteIPRanges,PermissionGroups,AuthMechanism

     Enable protocol logging for the Receive connector. For more information, see Configure
     protocol logging.

     Send a test message or connect to the Receive connector by using Telnet from the server
     or device. For more information, see Use Telnet to test SMTP communication on Exchange
     servers.

Scenario 4: Receive messages from internal
Exchange servers
You don't need to configure custom Receive connectors for internal mail flow between Mailbox
servers. However, you might need to create a custom Receive connector on an unsubscribed
Edge Transport server to receive messages from Mailbox servers. For this scenario, the Edge
Transport server listens on port 25, but only from the IP address of the specified Mailbox
servers.

<!-- p.1587 -->

Use the Exchange Management Shell to create a Receive
connector that only accepts messages from an internal
Exchange server
To create a Receive connector that only accepts messages from an internal Exchange server,
use this syntax:

  PowerShell

  New-ReceiveConnector -Name <UniqueName> [-TransportRole Frontend] -Internal -
  RemoteIPRanges <RemoteIPAddress>

This example creates a Receive connector named Inbound From Organization on an
unsubscribed Edge Transport server that listens for inbound messages from the internal
Mailbox servers at IP addresses 10.1.2.10, 10.1.2.15, and 10.1.2.20.

  PowerShell

  New-ReceiveConnector -Name "Inbound From Organization" -Internal -RemoteIPRanges
  10.1.2.10,10.1.2.15,10.1.2.20

Note: If your Edge Transport server uses different network adapters for internal and external
networks, be sure to use the Bindings parameter on the Set-ReceiveConnector cmdlet after
you create the connector to specify the correct local IP address for the connector.

For detailed syntax and parameter information, see New-ReceiveConnector.

How do you know this worked?
To verify that you've successfully created a Receive connector that only accepts messages from
an internal Exchange server, do any of these steps:

     In the EAC, go to Mail flow > Receive connectors, select the Receive connector, select
     Edit (    ), and verify the property values.

     In the Exchange Management Shell, run this command on the server, and verify the
     property values:

        PowerShell

        Get-ReceiveConnector | where {$_.Bindings -like '*25'} | Format-List
        Identity,RemoteIPRanges,PermissionGroups,AuthMechanism

<!-- p.1588 -->

Enable protocol logging for the Receive connector. For more information, see Configure
protocol logging.

Send a test message or connect to the Receive connector by using Telnet from the
remote Exchange server. For more information, see Use Telnet to test SMTP
communication on Exchange servers.

<!-- p.1589 -->

Modify the SMTP banner on Receive
connectors
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The SMTP banner is the initial SMTP connection response that a messaging server receives after
it connects to an Exchange server. Specifically, the messaging server connects to a Receive
connector that's configured on the Exchange server. For Exchange Mailbox servers, external
messaging servers connect through Receive connectors that are configured in the Front End
Transport service. The default Receive connector that's configured to accept anonymous SMTP
connections is named Default Frontend <ServerName>. For Edge Transport servers, the default
Receive connector in the Transport service named Default internal receive connector
<ServerName>> is configured to accept anonymous SMTP connections. For more information,
see How messages from external senders enter the transport pipeline and Default Receive
connectors created during setup.

By default, the connection response looks like this:

220 <ServerName> Microsoft ESMTP MAIL service ready at <RegionalDay-Date-
24HourTimeFormat><RegionalTimeZoneOffset>

Here are some reasons that you might want to modify the default SMTP banner:

      You don't want Exchange or the internal Exchange server name disclosed in the
      connection response to external messaging servers.

      You want the connection response to include your domain name to satisfy antispam or
      reverse DNS to SMTP banner checks.

      You want the connection response to include the name of the Receive connector to make
      it easier to troubleshoot connection problems.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      The replacement SMTP banner text string must always start with 220 (the default "Service
      ready" SMTP response code is 220).

<!-- p.1590 -->

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Receive connectors" entry in the
     Mail flow permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online     , or Exchange Online Protection .

Use the Exchange Management Shell to modify the
SMTP banner on a Receive connector
Use the following syntax:

  PowerShell

  Set-ReceiveConnector -Identity <ConnectorIdentity> -Banner "220 <Banner Text>"

This example changes the SMTP banner on the Receive connector named Default Frontend
Mailbox01 to the value 220 contoso.com.

  PowerShell

  Set-ReceiveConnector -Identity "Default Frontend Mailbox01" -Banner "220
  consoso.com"

This example removes the custom SMTP banner, which returns the SMTP banner to the default
value.

  PowerShell

  Set-ReceiveConnector -Identity "Default Frontend Mailbox01" -Banner $null

How do you know this worked?
To verify that you have successfully modified the SMTP banner on a Receive connector, do
these steps:

<!-- p.1591 -->

   1. Open a Telnet client on a computer that can access the Receive connector, and run the
     following command:

           open <Connector FQDN or IP address><TCPPort>

   2. Verify the that response contains the SMTP banner you configured.

Note that this procedure only works on Receive connectors that allow anonymous or Basic
authentication. For more information, see Use Telnet to test SMTP communication on Exchange
servers.

<!-- p.1592 -->

Allow anonymous relay on Exchange
servers
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Open relay is a very bad thing for messaging servers on the Internet. Messaging servers that
are accidentally or intentionally configured as open relays allow mail from any source to be
transparently re-routed through the open relay server. This behavior masks the original source
of the messages, and makes it look like the mail originated from the open relay server. Open
relay servers are eagerly sought out and used by spammers, so you never want your messaging
servers to be configured for open relay.

On the other hand, anonymous relay is a common requirement for many businesses that have
internal web servers, database servers, monitoring applications, or other network devices that
generate email messages, but are incapable of actually sending those messages.

In Exchange Server, you can create a dedicated Receive connector in the Front End Transport
service on a Mailbox server that allows anonymous relay from a specific list of internal network
hosts. Here are some key considerations for the anonymous relay Receive connector:

      You need to create a dedicated Receive connector to specify the network hosts that are
      allowed to anonymously relay messages, so you can exclude anyone or anything else
      from using the connector. Don't attempt to add anonymous relay capability to the default
      Receive connectors that are created by Exchange. Restricting access to the Receive
      connector is critical, because you don't want to configure the server as an open relay.

      You need to create the dedicated Receive connector in the Front End Transport service,
      not in the Transport service. In Exchange Server, the Front End Transport service and the
      Transport service are always located together on Mailbox servers. The Front End Transport
      service has a default Receive connector named Default Frontend <ServerName> that's
      configured to listen for inbound SMTP connections from any source on TCP port 25. You
      can create another Receive connector in the Front End Transport service that also listens
      for incoming SMTP connections on TCP port 25, but you need to specify the IP addresses
      that are allowed to use the connector. The dedicated Receive connector will always be
      used for incoming connections from those specific network hosts (the Receive connector
      that's configured with the most specific match to the connecting server's IP address wins).

      In contrast, the Transport service has a Default receive connector named Default
      <ServerName> that's also configured to listed for inbound SMTP connections from any
      source, but this connector listens on TCP port 2525 so that it doesn't conflict with the
      Receive connector in the Front End Transport service. Furthermore, only other transport

<!-- p.1593 -->

    services and Exchange servers in your organization are expected to use this Receive
    connector, so the authentication and encryption methods are set accordingly.

    For more information, see Mail flow and the transport pipeline and Default Receive
    connectors created during setup.

    After you create the dedicated Receive connector, you need to modify its permissions to
    allow anonymous relay only by the specified network hosts as identified by their IP
    addresses. At a minimum, the network hosts need the following permissions on the
    Receive connector to anonymously relay messages:

        ms-Exch-Accept-Headers-Routing

        ms-Exch-SMTP-Accept-Any-Recipient

        ms-Exch-SMTP-Accept-Any-Sender

        ms-Exch-SMTP-Accept-Authoritative-Domain-Sender

        ms-Exch-SMTP-Submit

        For more information about permissions on Receive connectors, see Receive connector
        permission groups and Receive connector permissions.

        There are two different methods that you can use to configure the permissions that are
        required for anonymous relay on a Receive connector. These methods are described in
        the following table.

                                                                                        ﾉ   Expand table

Method                            Permissions granted        Pros                   Cons

Add the Anonymous users           Connections use the NT     Grants the minimum     More difficult to
( Anonymous ) permission group    AUTHORITY\ANONYMOUS        required               configure (must use
to the Receive connector and      LOGON security principal   permissions to allow   the Exchange
add the Ms-Exch-SMTP-Accept-      with the following         anonymous relay.       Management Shell).
Any-Recipient permission to       permissions:                                      The network hosts
the NT AUTHORITY\ANONYMOUS                                                          are considered
LOGON security principal on the         ms-Exch-Accept-                             anonymous senders.
Receive connector.                      Headers-Routing                             Messages don't
                                        ms-Exch-SMTP-                               bypass antispam or
                                        Accept-Any-                                 message size limit
                                        Recipient                                   checks, and the
                                        ms-Exch-SMTP-                               sender's email
                                        Accept-Any-Sender                           address can't be
                                        ms-Exch-SMTP-                               resolved to the
                                        Accept-                                     corresponding

<!-- p.1594 -->

 Method                           Permissions granted        Pros                    Cons

                                        Authoritative-                               display name (if any)
                                        Domain-Sender                                in the global address
                                        ms-Exch-SMTP-                                list.
                                        Submit

 Add the Exchange servers         Connections use the MS     Easier to configure     Grants the
 ( ExchangeServers ) permission   Exchange\Externally        (can do everything      permissions to
 group and the Externally         Secured Servers security   in the Exchange         submit messages as
 secured                          principal with the         admin center).          if they originated
 ( ExternalAuthoritative )        following permissions:     The network hosts       from internal senders
 authentication mechanism to                                 are considered          within your Exchange
 the Receive connector.                 ms-Exch-Accept-      authenticated           organization. The
                                        Headers-Routing      senders. Messages       network hosts are
                                        ms-Exch-Bypass-      bypass antispam         considered
                                        Anti-Spam            and message size        completely
                                        ms-Exch-Bypass-      limit checks, and the   trustworthy,
                                        Message-Size-        sender's email          regardless of the
                                        Limit                address can be          volume, size, or
                                        ms-Exch-SMTP-        resolved to a           content of the
                                        Accept-Any-          corresponding           messages that they
                                        Recipient            display name in the     send.
                                        ms-Exch-SMTP-
                                                             global address list.

                                        Accept-Any-Sender
                                        ms-Exch-SMTP-
                                        Accept-
                                        Authentication-
                                        Flag
                                        ms-Exch-SMTP-
                                        Accept-
                                        Authoritative-
                                        Domain-Sender
                                        ms-Exch-SMTP-
                                        Accept-Exch50
                                        ms-Exch-SMTP-
                                        Submit

Ultimately, you need to decide on the approach that best fits the needs of your organization.
We'll show you how to configure both methods. Just remember that it's one method or the
other, and not both at the same time.

What do you need to know before you begin?
     Estimated time to complete this task: 10 minutes.

<!-- p.1595 -->

     Some of these procedures require the Exchange Management Shell. To learn how to open
     the Exchange Management Shell in your on-premises Exchange organization, see Open
     the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Receive connectors" entry in the
     Mail flow permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online       , or Exchange Online Protection .

Step 1: Create a dedicated Receive connector for
anonymous relay
You can create the Receive connector in the EAC or in the Exchange Management Shell.

Use the EAC to create a dedicated Receive connector for
anonymous relay
  1. In the EAC, navigate to Mail flow > Receive connectors, and then click Add        . This starts
     the New Receive connector wizard.

  2. On the first page, enter the following information:

          Name: Enter a descriptive name for the Receive connector, for example, Anonymous
          Relay.

          Role: Select Frontend Transport.

          Type: Select Custom.

          When you're finished, click Next.

  3. On the next page, in the Network adapter bindings section, do one of the following:

          If the Exchange server has one network adapter, and doesn't segregate internal and
          external traffic by using different subnets, accept the existing (All available IPv4)

<!-- p.1596 -->

            entry on port 25.

            If the Exchange server has an internal network adapter and an external network
            adapter, and segregates internal and external network traffic by using different
            subnets, you can further enhance security for the connector by limiting the use of
            the connector to requests that originate on the internal network adapter. To do this:

               a. Select the existing (All available IPv4) entry, click Remove   , and then click Add
                   .

               b. In the resulting Network Adapter Bindings dialog, select Specify an IPv4 address
                 or an IPv6 address, and enter a valid and available IP address that's configured
                 on the internal network adapter, and then click Save.

     When you're finished, click Next.

   4. On the next page, in the Remote network settings section, do the following steps:

      a. Select the existing 0.0.0.0-255.255.255.255 entry, and then click Remove         , and then
          click Add     .

     b. In the resulting Remote Address Settings dialog, enter an IP address or IP address
          range that identifies the network hosts that are allowed use this connector, and then
          click Save. You can repeat this step to add multiple IP addresses or IP address ranges.
          Err on the side of being too specific instead of too general to clearly identify the
          network hosts that are allowed to use this connector.

     When you're finished, click Finish.

Use the Exchange Management Shell to create a dedicated
Receive connector for anonymous relay
To create the same Receive connector in the Exchange Management Shell, use the following
syntax:

  PowerShell

  New-ReceiveConnector -Name <ConnectorName> -TransportRole FrontendTransport -
  Custom -Bindings <LocalIPAddresses>:25 -RemoteIpRanges <RemoteIPAddresses>

This example creates a new Receive connector with the following configuration options:

     Name: Anonymous Relay

     Transport role: FrontEndTransport

<!-- p.1597 -->

        Usage type: Custom

        Bindings: 0.0.0.0:25 (listen for inbound messages on all IP addresses that are configured
        on all network adapters in the Exchange server on TCP port 25.)

        Remote IP addresses that are allowed to use this connector: 192.168.5.10 and
        192.168.5.11

     PowerShell

     New-ReceiveConnector -Name "Anonymous Relay" -TransportRole FrontendTransport -
     Custom -Bindings 0.0.0.0:25 -RemoteIpRanges 192.168.5.10,192.168.5.11

Notes:

        The Bindings parameter is required when you specify the Custom usage type.

        The RemoteIpRanges parameter accepts an individual IP address, an IP address range (for
        example, 192.168.5.10-192.168.5.20 ), or Classless InterDomain Routing (CIDR) (for
        example, 192.168.5.1/24 ). You can specify multiple values separated by commas.

Step 2: Configure the permissions for anonymous
relay on the dedicated Receive connector
As described in the introduction, there are two different methods you can use to configure the
required permissions on the Receive connector:

        Configure the connections as anonymous.

        Configure the connections as externally secured.

Choose one method or the other. The examples use the Receive connector named Anonymous
Relay that you created in Step 1.

Configure the connections as anonymous
Run the following commands in the Exchange Management Shell:

1.

     PowerShell

     Set-ReceiveConnector "Anonymous Relay" -PermissionGroups AnonymousUsers

<!-- p.1598 -->

   2.

  PowerShell

  Get-ReceiveConnector "Anonymous Relay" | Add-ADPermission -User "NT
  AUTHORITY\ANONYMOUS LOGON" -ExtendedRights "Ms-Exch-SMTP-Accept-Any-Recipient"

Configure the connections as externally secured
   1. In the EAC, navigate to Mail flow > Receive connectors, select the Anonymous Relay
        connector, and then click Edit      .

   2. In the properties of the connector, click Security and make the following selections:

             Authentication: Deselect Transport Layer Security (TLS) and select Externally
             secured (for example, with IPsec).

             Permission groups: Select Exchange servers.

        When you're finished, click Save.

To perform these same steps in the Exchange Management Shell, run the following command:

  PowerShell

  Set-ReceiveConnector "Anonymous Relay" -AuthMechanism ExternalAuthoritative -
  PermissionGroups ExchangeServers

How do you know this worked?
To verify that you've successfully configured anonymous relay, do the following steps:

        Verify the configuration of the dedicated Receive connector.

          PowerShell

          Get-ReceiveConnector "Anonymous Relay" | Format-List
          Enabled,TransportRole,Bindings,RemoteIPRanges

        Verify the permissions on the dedicated Receive connector.

          PowerShell

          Get-ADPermission "Anonymous Relay" -User "NT AUTHORITY\ANONYMOUS LOGON" |
          where {($_.Deny -eq $false) -and ($_.IsInherited -eq $false)} | Format-Table

<!-- p.1599 -->

     User,ExtendedRights

Or

  PowerShell

     Get-ADPermission "Anonymous Relay" -User "MS Exchange\Externally Secured
     Servers" | where {($_.Deny -eq $false) -and ($_.IsInherited -eq $false)} |
     Format-Table User,ExtendedRights

Use Telnet to test if one or more of the specified network hosts can connect to the
dedicated Receive connector, and can anonymously relay mail through the connector. By
default, the Telnet Client isn't installed in most client or server versions of Microsoft
Windows. To install it, see Install Telnet Client.

For more information, see Use Telnet to test SMTP communication on Exchange servers.

If the network host is a device that doesn't have Telnet, you could temporarily add the IP
address of a computer to the Receive connector, and then remove the IP address from
the Receive connector when you're finished testing.

For the test, the you'll need the following values:

     Destination: This is the IP address or FQDN that you use to connect to the dedicated
     Receive connector. This is likely the IP address of the Mailbox server where the Receive
     connector is defined. This relates to the Network adapter bindings property (or the
     Bindings parameter) value that you configured on the connector. You'll need to use the
     valid value for your environment. In this example, we'll use 10.1.1.1.

     Sender's email address: You'll probably configure the servers or devices that are
     anonymously relaying mail to use a sending email address that's in an authoritative
     domain for your organization. In this example, we'll use chris@contoso.com.

     Recipient's email address: Use a valid email address. In this example, we'll use
     kate@fabrikam.com.

     Message subject: Test

     Message body: This is a test message

     1. Open a Command Prompt window, type telnet, and then press Enter.

     2. Type set localecho, and then press Enter.

     3. Type OPEN 10.1.1.1 25, and then press Enter.

<!-- p.1600 -->

 4. Type EHLO, and then press Enter.

 5. Type MAIL FROM:chris@contoso.com, and then press Enter.

 6. Type RCPT TO:kate@fabrikam.com, and then press Enter.

      If you receive the response 250 2.1.5 Recipient OK , the Receive connector allows
      anonymous relay from the network host. Continue to the next step to finish
      sending the test message.

      If you receive the response 550 5.7.1 Unable to relay , the Receive connector
      doesn't allow anonymous relay from the network host. If this happens, do the
      following:

         Verify that you're connecting to the correct IP address or FQDN for the
         dedicated Receive connector.

         Verify that the computer where you're running Telnet is allowed to use the
         Receive connector.

         Verify the permissions on the Receive connector.

 7. Type DATA, and then press Enter.

   You should receive a response that looks like this:

    354 Start mail input; end with <CLRF>.<CLRF>

 8. Type Subject: Test, and then press Enter.

 9. Press Enter again.

10. Type This is a test message, and then press Enter.

11. Press Enter, type a period ( . ), and then press Enter.

   You should receive a response that looks like this:

    250 2.6.0 <GUID> Queued mail for delivery

12. To disconnect from the SMTP server, type QUIT, and then press Enter.

   You should receive a response that looks like this:

    221 2.0.0 Service closing transmission channel

13. To close the Telnet session, type quit, and then press Enter.
