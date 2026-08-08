---
title: "Exchange Server — pages 1601-1640"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1601-1640
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1601-1640
family: exchange
documentKind: "doc"
abstract: "If anonymous relay works intermittently, you may need to modify the default message rate and throttling limits on the Receive connector. For more information, see Message throttling on Receive connectors. Send connectors in Exchange Server Article • 04/30/2025 APPLIES TO: 2016 2"
---

# Exchange Server — pages 1601-1640

<!-- p.1601 -->

If anonymous relay works intermittently, you may need to modify the default message
rate and throttling limits on the Receive connector. For more information, see Message
throttling on Receive connectors.

<!-- p.1602 -->

Send connectors in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016    2019     Subscription Edition

Exchange uses Send connectors for outbound SMTP connections from source Exchange servers
to destination email servers. The Send connector that's used to route messages to a recipient is
selected during the routing resolution phase of message categorization. For more information,
see Mail routing.

You can create Send connectors in the Transport service on Mailbox servers and on Edge
Transport servers. Send connectors are stored in Active Directory and are (by default) visible to
all Mailbox servers in the organization.

  ） Important

  By default, no Send connectors exist for external mail flow when you install Exchange. To
  enable outbound internet mail flow, you need to create a Send connector, or subscribe an
  Edge Transport server to your Exchange organization. For more information, see Create a
  Send connector to send mail to the Internet and Edge Transport servers.

You don't need to configure Send connectors to send mail between Exchange servers in the
same Active Directory forest. Implicit and invisible Send connectors that are fully aware of the
Exchange server topology are available for sending mail to internal Exchange servers. These
connectors are described in the Implicit Send connectors section.

These are the important settings on Send connectors:

      Usage type

      Network settings: Configure how the Send connector routes mail: by using DNS or by
      automatically forward all mail to a smart host.

      Address spaces: Configure the destination domains that the Send connector is
      responsible for.

      Scope: Configures the visibility of the Send connector to other Exchange servers in the
      organization.

      Source servers: Configure the Exchange servers where the Send connector is hosted. Mail
      that needs to be delivered by using the Send connector is routed to one of the source
      servers.

<!-- p.1603 -->

On Mailbox servers, you can create and manage Send connectors in the Exchange admin
center or in the Exchange Management Shell. On Edge Transport servers, you can only use the
Exchange Management Shell.

Send connector changes in Exchange Server
These are the notable changes to Send connectors in Exchange 2016 or Exchange 2019
compared to Exchange 2010:

     You can configure Send connectors to redirect or proxy outbound mail through the Front
     End Transport service. For more information, see Configure Send connectors to proxy
     outbound mail.

     The IsCoexistenceConnector parameter is no longer available.

     The LinkedReceiveConnector parameter is no longer available.

     The default maximum message size is increased to 35 MB (approximately 25 MB due to
     Base64 encoding). For more information, see Message size and recipient limits in
     Exchange Server.

     The TlsCertificateName parameter allows you to specify the certificate issuer and the
     certificate subject. This helps minimize the risk of fraudulent certificates.

Implicit Send connectors
Although no Send connectors are created during the installation of Exchange servers, a special
implicit Send connector named the intra-organization Send connector is present. This implicit
Send connector is automatically available, invisible, and requires no management. The intra-
organization Send connector exists in the transport services to send mail, either internally
between services on the local Exchange server, or to services on remote Exchange servers in
the organization. For example:

     Front End Transport service to the Transport service.

     Transport service to the Transport service on other servers.

     Transport service to subscribed Edge Transport servers.

     Transport service to the Mailbox Transport Delivery service.

     Mailbox Transport Submission service to the Transport service.

For more information, see Mail flow and the transport pipeline.

<!-- p.1604 -->

Send connector usage types
For Send connectors, the usage type is basically a descriptive label that identifies what the
Send connector is used for. All usage type values receive the same permissions.

You can specify the connector usage type only when you create Send connectors. When you
use the EAC, you must select a Type value. But when you use the New-SendConnector cmdlet
in the Exchange Management Shell, the usage type isn't required (either by using -Usage
<UsageType> or -<UsageType> ).

Specifying a usage type does configure a default maximum message size, which you can
change after you create the connector.

The available usage type values are described in the following table.

                                                                                     ﾉ   Expand table

 Usage      Maximum      Comments
 type       message
            size

 Custom     35 MB        None

 Internal   unlimited    When you create a Send connector of this usage type in the EAC, you can't
                         select MX record associated with recipient domain. After you create the
                         connector, you can go to the Delivery tab in the properties of the Send
                         connector and select MX record associated with recipient domain.

                         This same restriction doesn't exist in the Exchange Management Shell. You can
                         use the Internal switch and set the DNSRoutingEnabled to $true on the New-
                         SendConnector cmdlet.

 Internet   35 MB        None

 Partner    35 MB        When you create a Send connector of this usage type in the EAC, you can't
                         select Route mail through smart hosts or a smart host authentication
                         mechanism. After you create the connector, you can go to the Delivery tab in
                         the properties of the Send connector and select Route mail through smart
                         hosts and the smart host authentication mechanism.

                         This same restriction doesn't exist in the Exchange Management Shell. You can
                         use the Partner switch and set the DNSRoutingEnabled to $false and use the
                         SmartHosts and SmartHostAuthMechanism parameters on the New-
                         SendConnector cmdlet.

Send connector network settings

<!-- p.1605 -->

Every Send connector needs to be configured with one of these options:

     Use DNS to route mail.

     Use one or more smart hosts to route mail.

Use DNS to route mail
When you select DNS resolution to deliver mail, the source Exchange server for the Send
connector must be able to resolve the MX records for the address spaces that are configured
on the connector. Depending on the nature of the connector, and how many network adapters
are in the server, the Send connector could require access to an internal DNS server, or an
external (public) DNS server. You can configure the server to use specific DNS servers for
internal and external DNS lookups:

     In the EAC at Servers > Server > select the server and click Edit    > DNS lookups tab.

     In the Exchange Management Shell, you use the ExternalDNS* and InternalDNS*
     parameters on the Set-TransportService cmdlet.

If you've already configured the Exchange server with separate DNS settings to use for internal
and external DNS lookups, and the Send connector routes mail to an external address space,
you need to configure the Send connector to use the external DNS server:

     In the EAC, select Use the external DNS lookup setting on servers with transport roles
     (in the new Send connector wizard, or on the Delivery tab in the properties of existing
     connectors).

     In the Exchange Management Shell, use the UseExternalDNSServersEnabled parameter on
     the New-SendConnector and Set-SendConnector cmdlets.

Use smart hosts to route mail
When you route mail through a smart host, the Send connector forwards mail to the smart
host, and the smart host is responsible for routing mail to next hop on its way to the ultimate
destination. A common use for smart host routing is to send outgoing mail through an
antispam service or device.

You identify one or more smart hosts to use for the Send connector by an individual IP address
(for example 10.1.1.1), a fully qualified domain name (FQDN) (for example
spamservice.contoso.com), or combinations of both types of values. If you use an FQDN, the
source Exchange server for the Send connector must be able to resolve the FQDN (which could
be an MX record or an A record) by using DNS.

<!-- p.1606 -->

An important part of smart host routing is the authentication mechanism that the smart hosts
uses. The available authentication mechanisms are described in the following table.

                                                                                           ﾉ   Expand table

 Authentication mechanism             Description

 None ( None )                        No authentication. For example, when access to the smart host is
                                      restricted by the source IP address.

 Basic authentication ( BasicAuth )   Basic authentication. Requires a username and password. The
                                      username and password are sent in clear text.

 Offer basic authentication only      Basic authentication that's encrypted with TLS. This requires a server
 after starting TLS                   certificate on the smart host that contains the exact FQDN of the
 ( BasicAuthRequireTLS )              smart host that's defined on the Send connector.

                                      The Send connector attempts to establish the TLS session by sending
                                      the STARTTLS command to the smart host, and only performs Basic
                                      authentication after the TLS session is established.

                                      A client certificate is also required to support mutual TLS
                                      authentication.

 Exchange Server authentication       Generic Security Services application programming interface
 ( ExchangeServer )                   (GSSAPI) and Mutual GSSAPI authentication.

 Externally secured                   The connection is presumed to be secured by using a security
 ( ExternalAuthoritative )            mechanism that's external to Exchange. The connection may be an
                                      Internet Protocol security (IPsec) association or a virtual private
                                      network (VPN). Alternatively, the servers may reside in a trusted,
                                      physically controlled network.

Send connector address spaces
The address space specifies the destination domains that are serviced by the Send connector.
Mail is routed through a Send connector based on the domain of the recipient's email address.

The available SMTP address space values are described in the following table.

                                                                                           ﾉ   Expand table

 Address space                 Explanation

 *                             The Send connector routes mail to recipients in all domains.

<!-- p.1607 -->

 Address space             Explanation

 Domain (for example,      The Send connector routes mail to recipients in the specified domain, but
 contoso.com )             not in any subdomains.

 Domain and subdomains     The Send connector routes mail to recipients in the specified domain, and in
 (for example,             all subdomains.
  *.contoso.com )

 --                        The Send connector routes mail to recipients in all accepted domains in the
                           Exchange organization. This value is only available on Send connectors on
                           Edge Transport servers that send mail to the internal Exchange organization.

An address space also has Type and Cost values that you can configure.

On Edge Transport servers, the Type value must be SMTP . On Mailbox servers, you can also use
non-SMTP address space types like X400 or any other text string. X.400 addresses need to be
RFC 1685 compliant (for example, o=MySite;p=MyOrg;a=adatum;c=us ), but other Type values
accept any text value for the address space. If you specify a non-SMTP address space type, the
Send connector must use smart host routing, and SMTP is used to send messages to the smart
host. Delivery Agent connectors and Foreign connectors send non-SMTP messages to non-
SMTP servers without using SMTP. For more information, see Delivery Agents and Delivery
Agent Connectors and Foreign Connectors.

The Cost value on the address space is used for mail flow optimization and fault tolerance
when you have the same address spaces configured on multiple Send connectors on different
source servers. A lower priority value indicates a preferred Send connector.

The Send connector that's used to route messages to a recipient is selected during the routing
resolution phase of message categorization. The Send connector whose address space most
closely matches the recipient's email address, and whose priority value is lowest is selected.

For example, suppose the recipient is julia@marketing.contoso.com. If a Send connector is
configured for *.contoso.com, the message is routed through that connector. If no Send
connector is configured for *.contoso.com, the message is routed through the connector that's
configured for *. If multiple Send connectors in the same Active Directory site are configured
for *.contoso.com, the connector with the lower priority value is selected.

Send connector scope
The source servers for a Send connector determine the destination Exchange server for mail
that needs to be routed through the Send connector. The Send connector scope controls the
visibility of the connector within the Exchange organization.

<!-- p.1608 -->

By default, Send connectors are visible to all the Exchange servers in the entire Active Directory
forest, and are used in routing decisions. However, you can limit the scope of a Send connector
so that it's only visible to other Exchange servers in the same Active Directory site. The Send
connector is invisible to Exchange servers in other Active Directory sites, and isn't used in their
routing decisions. A Send connector that's restricted in this way is said to be scoped.

To configure scoped Send connectors in the EAC, you select Scoped send connector in the
Address space section of the new Send connector wizard, or on the Scoping tab in the
properties of existing Send connectors. In the Exchange Management Shell, you use the
IsScopedConnector parameter on the New-SendConnector and Set-SendConnector cmdlets.

Send connector permissions
When the Send connector establishes a connection with the destination email server, the Send
connector permissions determine the types of headers that can be sent in messages. If a
message includes headers that aren't allowed by the permissions, those headers are removed
from messages.

Permissions are assigned to Send connectors by well-known security principals. Security
principals include user accounts, computer accounts, and security groups (objects that are
identifiable by a security identifier or SID that can have permissions assigned to them). By
default, the same security principals with the same permissions are assigned on all Send
connectors, regardless of the usage type that you selected when you created the connector. To
modify the default permissions for a Send connector, you need to use the Add-ADPermission
and Remove-ADPermission cmdlets in the Exchange Management Shell.

The available Send connector permissions are described in the following table.

                                                                                      ﾉ   Expand table

 Permission        Assigned to             Description

 ms-Exch-Send-     <Domain>\Exchange       Controls the preservation of Exchange forest headers in
 Headers-Forest    Servers                 messages. Forest header names start with X-MS-Exchange-
                                           Forest-. If this permission isn't granted, all forest headers
                   MS Exchange\Edge        are removed from messages.
                   Transport Servers

                   MS Exchange\Hub
                   Transport Servers

 ms-Exch-Send-     <Domain>\Exchange       Controls the preservation of Exchange organization headers
 Headers-          Servers                 in messages. Organization header names start with X-MS-
 Organization

<!-- p.1609 -->

Permission        Assigned to              Description

                  MS Exchange\Edge         Exchange-Organization-. If this permission isn't granted, all
                  Transport Servers        organization headers are removed from messages.

                  MS Exchange\Hub
                  Transport Servers

ms-Exch-Send-     NT AUTHORITY\ANONYMOUS   Controls the preservation of RECEIVED headers in
Headers-Routing   LOGON                    messages. If this permission isn't granted, all received
                                           headers are removed from messages.
                  <Domain>\Exchange
                  Servers

                  MS Exchange\Edge
                  Transport Servers

                  MS Exchange\Externally
                  Secured Servers

                  MS Exchange\Hub
                  Transport Servers

                  MS Exchange\Legacy
                  Exchange Servers

                  MS Exchange\Partner
                  Servers

ms-Exch-SMTP-     <Domain>\Exchange        Allows the source Exchange server to submit XEXCH50
Send-Exch50       Servers                  commands on the Send connector. The X-EXCH50 binary
                                           large object (BLOB) was used by older versions of Exchange
                  MS Exchange\Edge         (Exchange 2003 and earlier) to store Exchange data in
                  Transport Servers        messages (for example, the spam confidence level or SCL).

                  MS Exchange\Externally   If this permission isn't granted, and messages contain the
                  Secured Servers          X-EXCH50 BLOB, the Exchange server sends the message
                                           without the X-EXCH50 BLOB.
                  MS Exchange\Hub
                  Transport Servers

                  MS Exchange\Legacy
                  Exchange Servers

ms-Exch-SMTP-     <Domain>\Exchange        This permission is reserved for internal Microsoft use, and is
Send-XShadow      Servers                  presented here for reference purposes only.

                  MS Exchange\Edge
                  Transport Servers

<!-- p.1610 -->

 Permission       Assigned to             Description

                   MS Exchange\Hub
                  Transport Servers

Note: Permissions names that contain ms-Exch-Send-Headers- are part of the header firewall
feature. For more information, see Header firewall.

Send connector permission procedures
To see the permissions that are assigned to security principals on a Send connector, use the
following syntax in the Exchange Management Shell:

  PowerShell

  Get-ADPermission -Identity <SendConnector> [-User <SecurityPrincipal>] | where
  {($_.Deny -eq $false) -and ($_.IsInherited -eq $false)} | Format-Table
  User,ExtendedRights

For example, to see the permissions that are assigned to all security principals on the Send
connector named To Fabrikam.com, run the following command:

  PowerShell

  Get-ADPermission -Identity "To Fabrikam.com" | where {($_.Deny -eq $false) -and
  ($_.IsInherited -eq $false)} | Format-Table User,ExtendedRights

To see the permissions that are assigned only to the security principal NT AUTHORITY\ANONYMOUS
LOGON on the Send connector named To Fabrikam, run the following command:

  PowerShell

  Get-ADPermission -Identity "To Fabrikam.com" -User "NT AUTHORITY\ANONYMOUS LOGON"
  | where {($_.Deny -eq $false) -and ($_.IsInherited -eq $false)} | Format-Table
  User,ExtendedRights

To add permissions to a security principal on a Send connector, use the following syntax:

  PowerShell

  Add-ADPermission -Identity <SendConnector> -User <SecurityPrincipal> -
  ExtendedRights "<Permission1>","<Permission2>"...

<!-- p.1611 -->

To remove permissions from a security principal on a Send connector, use the following syntax:

  PowerShell

  Remove-ADPermission -Identity <SendConnector> -User <SecurityPrincipal> -
  ExtendedRights "<Permission1>","<Permission2>"...

<!-- p.1612 -->

Create a Send connector in Exchange
Server to send mail to the internet
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

When install your first Exchange Server 2016 or Exchange 2019 server, the server isn't able to
send mail outside of your Exchange organization. To send mail outside your Exchange
organization, you need to create a Send connector.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Send connectors" entry in the
      Mail flow permissions topic.

      See Deploy a new installation of Exchange Server if you're beginning your installation.
      After the installation, you can use the steps in this topic to create an internet Send
      connector.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Create a Send connector to send mail to the
internet
Until you create a Send connector, mail can't flow from your Exchange to the internet. The
exception is if you install an Edge Transport in your perimeter network and subscribe the Edge
Transport to your Exchange organization. For more information, see Edge Transport servers.

See also Send connectors for more information about connectors and why you would may or
may not want to use them instead of Edge Transport Servers.

<!-- p.1613 -->

Use the EAC to create an internet Send connector
 1. In the EAC, navigate to Mail flow > Send connectors, and then click Add        . This starts
   the New Send connector wizard.

 2. On the first page, enter the following information:

         Name: Enter a descriptive name for the Send connector (for example, To internet).

         Type: Select Internet.

   When you're finished, click Next.

 3. On the next page, verify that MX record associated with recipient domain is selected.
   This means the connector uses DNS on the internet to route mail, as opposed to routing
   all outbound mail to a smart host. For information about creating a Send connector that
   uses smart host routing, see Create a Send connector to route outbound mail through a
   smart host.

   When you're finished, click Next.

 4. On the next page, enter the following information:

         In the Address space section, click Add      . In the Add domain dialog box that
         appears, in Fully Qualified Domain Name (FQDN), enter an asterisk (*), and then
         click Save. This value indicates that the Send connector applies to messages
         addressed to all external domains.

         The Scoped send connector setting is important if your organization has Exchange
         servers installed in multiple Active Directory sites:

            If you don't select Scoped send connector, the connector is usable by all
            transport servers (Exchange 2013 or later Mailbox servers and Exchange 2010
            Hub Transport servers) in the entire Active Directory forest. This is the default
            value.

            If you select Scoped send connector, the connector is only usable by other
            transport servers in the same Active Directory site.

   When you're finished, click Next.

 5. On the next page, in the Source server section, click Add      . In the Select a Server dialog
   box that appears, select one or more Mailbox servers that you want to use to send mail to
   the internet. If you have multiple Mailbox servers in your environment, select the ones

<!-- p.1614 -->

     that can route mail to the internet. If you have only one Mailbox server, select that one.
     After you've selected at least one Mailbox server, click Add, click OK, and then click Finish.

After you create the Send connector, it appears in the Send connector list. To configure the
Send connector to proxy outbound mail through the Front End Transport service, see Configure
Send connectors to proxy outbound mail.

Use the Exchange Management Shell to create an internet Send
connector

   1. Open the Exchange Management Shell. For more information, see Open the Exchange
     Management Shell.

   2. Use the following syntax:

       PowerShell

        New-SendConnector -Name <Name> -AddressSpaces * -Internet [-
        SourceTransportServer <fqdn1>,<fqdn2>...]

     This example creates the internet Send connector named "To internet" with the following
     properties:

           The usage type is Internet.

           The Send connector uses DNS routing. We aren't using the DNSRoutingEnabled
           parameter, and the default value is $true .

           The Send connector is for all external domains (*).

           The local Exchange server is the source server. We aren't using the
           SourceTransportServer parameter, and the default value is the local Exchange server.

           The Send connector isn't scoped to the local Active Directory site. We aren't using
           the IsScopedConnector parameter, and the default value is $false .

       PowerShell

        New-SendConnector -Name "To internet" -AddressSpaces * -Internet

     For information about other options, see New-SendConnector.

  ７ Note

<!-- p.1615 -->

  To configure the Send connector to proxy outbound mail through the Front End Transport
  service, add -FrontEndProxyEnabled $true to the command. For more information, see
  Configure Send connectors to proxy outbound mail.

How do you know this worked?
To verify that you have successfully created a Send Connector that sends mail to the internet,
create and send a message from an internal mailbox to an outside recipient, and verify the
recipient receives the message.

You can also turn on protocol logging for the Send connector, and view the information in the
log. For more information, see Protocol logging.

<!-- p.1616 -->

Create a Send connector to route
outbound mail through a smart host
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

Instead of routing all outbound messages directly to the Internet, you may need to route your
organization's outbound mail through a third-party smart host. For example, your organization
may have an appliance that scans outbound mail for spam and malware.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      See Deploy a new installation of Exchange Server if you're beginning your installation.
      After the installation you can use the steps in this topic to create your outbound
      connector.

      The smart host described in this topic needs to use SMTP to transmit messages. If it
      doesn't, you need to use a Delivery Agent connector or a Foreign connector. For more
      information, seeDelivery Agents and Delivery Agent Connectors and Foreign Connectors.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Send connectors" entry in the
      Mail flow permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Use the EAC to create a Send connector that uses
smart host routing
   1. In the EAC, navigate to Mail flow > Send connectors, and then click Add      . This starts
      the New Send connector wizard.

<!-- p.1617 -->

2. On the first page, enter the following information:

        Name: Enter a descriptive name for the Send connector, for example, Smart host to
        Internet.

        Type: Select a descriptive value. For example, Internet or Custom. For more
        information about Send connector usage types, see Send connector usage types.

  When you're finished, click Next.

3. On the next page, select Route mail through smart hosts, and then click Add                . In the
  Add smart host dialog box that appears, identify the smart host by using one of the
  following values:

        IP address: For example, 192.168.3.2.

        Fully qualified domain name (FQDN): For example, securitydevice01.contoso.com.
        Note that the Exchange source servers for the Send connector must be able to
        resolve the smart host in DNS by using this FQDN.

  When you're finished, click Save.

4. You can enter multiple smart hosts by repeating Step 3. When you're finished, click Next.

5. On the next page, in the Route mail through smart hosts section, select the
  authentication method that's required by the smart host. Valid values are:

                                                                                      ﾉ   Expand table

   Authentication          Description
   mechanism

   None                    No authentication. For example, when access to the smart host is
                           restricted by the source IP address.

   Basic authentication    Basic authentication. Requires a username and password. The username
                           and password are sent in clear text.

   Offer basic             Basic authentication that's encrypted with TLS. This requires a server
   authentication only     certificate on the smart host that contains the exact FQDN of the smart
   after starting TLS      host that's defined on the Send connector.

   Exchange Server         Generic Security Services application programming interface (GSSAPI) and
   authentication          Mutual GSSAPI authentication.

   Externally secured      The connection is presumed to be secured by using a security mechanism
                           that's external to Exchange. The connection may be an Internet Protocol
                           security (IPsec) association or a virtual private network (VPN).

<!-- p.1618 -->

      Authentication          Description
      mechanism

                              Alternatively, the servers may reside in a trusted, physically controlled
                              network.

     When you're finished, click Next.

   6. On the next page, in the Address space section, click Add           . In the Add domain dialog
     box that appears, enter the following information:

          Type: Verify SMTP is entered.

          Fully Qualified Domain Name (FQDN): Enter an asterisk (*) to indicate the Send
          connector applies to messages addressed to all external domains. Alternatively, you
          can enter a specific external domain (for example, contoso.com), or a domain and all
          subdomains (for example, *.contoso.com).

          Cost: Verify 1 is entered. A lower value indicates a more preferred route for the
          domains you specified.

     When you're finished, click Save.

   7. Back on the previous page, the Scoped send connector setting is important if your
     organization has Exchange servers installed in multiple Active Directory sites:

          If you don't select Scoped send connector, the connector is usable by all transport
          servers (Exchange 2013 or later Mailbox servers and Exchange 2010 Hub Transport
          servers) in the entire Active Directory forest. This is the default value.

          If you select Scoped send connector, the connector is only usable by other
          transport servers in the same Active Directory site.

     When you're finished, click Next.

   8. On the next page, in the Source server section, click Add          . In the Select a Server dialog
     box that appears, select one or more Mailbox servers that you want to use to send
     outbound mail to the smart host. If you have multiple Mailbox servers in your
     environment, select the ones that can route mail to the smart host. If you have only one
     Mailbox server, select that one. After you've selected at least one Mailbox server, click
     Add, click OK, and then click Finish.

After you create the Send connector, it appears in the Send connector list.

<!-- p.1619 -->

Use the Exchange Management Shell to create a
Send connector that uses smart host routing
  1. Open the Exchange Management Shell. For more information, see Open the Exchange
     Management Shell.

  2. Use the following syntax:

       PowerShell

       New-SendConnector -Name <Name> -AddressSpaces * -Custom -DnsRoutingEnabled
       $false -SmartHosts <SmartHost1>[,<SmartHost2>...] [-SourceTransportServer
       <fqdn1>,<fqdn2>...]

     This example creates the Internet Send connector named "Smart host to Internet" with
     the following properties:

          The usage type is Custom.

          The Send connector uses smart host routing (the DNSRoutingEnabled parameter is
          set to the value $false ). The smart host's IP address is 192.168.3.2, and the
          authentication method is None, because the smart host is configured to listen for
          connections only from a restricted list of source servers.

          The Send connector is for all external domains (*). The value * is equivalent to the
          value "SMTP:*;1" , where the address space type is SMTP , and the address space cost
          value is 1 .

          The local Exchange server is the source server. We aren't using the
          SourceTransportServer parameter, and the default value is the local Exchange server.

          The Send connector isn't scoped to the local Active Directory site. We aren't using
          the IsScopedConnector parameter, and the default value is $false . The Send
          connector is useable by all Exchange transport servers in the Active Directory forest.

       PowerShell

       New-SendConnector -Name "Smart host to Internet" -AddressSpaces * -Custom -
       DNSRoutingEnabled $false -SmartHosts 192.168.3.2 -SmartHostAuthMechanism None

For information about other options, see New-SendConnector.

How do you know this worked?

<!-- p.1620 -->

To verify that you have successfully created a Send connector to route outbound email through
a smart host, send a message from a user in your organization to an external domain that's
serviced by the Send connector.

You can also turn on protocol logging for the Send connector, and view the information in the
log. For more information, see Protocol logging.

<!-- p.1621 -->

Configure Send connectors to proxy
outbound mail
Article • 04/30/2025

APPLIES TO:        2016    2019     Subscription Edition

When you create Send connectors, outbound mail flows through the Send connector in the
Transport service on the Mailbox server or servers you specify, as shown in the following
diagram.

However, you can configure a Send connector to relay or proxy outbound mail through the
Front End Transport service on the Mailbox server, as shown in the following diagram.

<!-- p.1622 -->

By default, all inbound mail enters your Exchange organization through the Front End
Transport service, and the Front End Transport service proxies inbound mail to the Transport
service. For more information, see Mail flow and the transport pipeline.

When you configure a Send connector to proxy outbound mail through the Front End
Transport service, the Receive connector named "Outbound Proxy Frontend <Mailbox server
name>" in the Front End Transport service listens for these outbound messages from the
Transport service, and then the Front End Transport service sends the messages to the internet.

What do you need to know before you begin?
     Estimated time to complete: less than 5 minutes

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Send connectors" entry in the
     Mail flow permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

<!-- p.1623 -->

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Configure Send connectors to proxy outbound
mail through the Front End Transport service

Use the EAC to configure Send connectors to proxy outbound
mail
In the Exchange admin center (EAC), you can only configure existing Send connectors to proxy
outbound mail.

  1. In the EAC, navigate to Mail flow > Send connectors, select the Send connector, and then
     click Edit     .

  2. On the General tab, in the Connector status section, select Proxy through client access
     server, and then click Save.

Use PowerShell to configure Send Connectors to proxy
outbound mail
In the Exchange Management Shell, you can configure new or existing Send connectors to
proxy outbound mail.

For information about how to open the Exchange Management Shell, see Open the Exchange
Management Shell.

     To configure a new Send connector to proxy outbound mail, add -FrontEndProxyEnabled
     $true to the New-SendConnector command.

     To configure an existing Send connector to proxy outbound mail, run the following
     command:

       PowerShell

       Set-SendConnector <Send connector identity>      -FrontEndProxyEnabled $true

     This example configures the existing Send connector named "Contoso.com Outbound" to
     proxy outbound mail.

<!-- p.1624 -->

       PowerShell

       Set-SendConnector "Contoso.com Outbound" -FrontendProxyEnabled $true

How do you know this worked?
To verify that a Send connector is configured for outbound proxy, perform either of the
following procedures:

     In the EAC, navigate to Mail flow > Send connectors, select the Send connector, and then
     click Edit     . On the General tab, in the Connector status section, verify Proxy through
     client access server is selected.

     In the Exchange Management Shell, run the following command:

       PowerShell

       Get-SendConnector | Format-Table -Auto Name,FrontEndProxyEnabled

     Verify the FrontEndProxyEnabled value is True for the Send connector.

<!-- p.1625 -->

Protocol logging in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Protocol logging records the SMTP conversations that occur between messaging servers and
between Exchange services in the transport pipeline as part of message delivery. You can use
protocol logging to diagnose mail flow problems. The SMTP conversations that can be
recorded by protocol logging occur in the following locations:

      Send connectors and Receive connectors in the Transport service on Mailbox servers.

      Send connectors and Receive connectors in the Transport service on Edge Transport
      servers.

      Receive connectors in the Front End Transport service on Mailbox servers.

      The implicit and invisible intra-organization Send connector in the Transport service on
      Mailbox servers.

      The implicit and invisible intra-organization Send connector in the Front End Transport
      service on Mailbox servers.

      The implicit and invisible intra-organization Send connector in the Mailbox Transport
      Submission service on Mailbox servers.

      The implicit and invisible Mailbox Delivery Receive connector in the Mailbox Transport
      Delivery service on Mailbox servers.

By default, protocol logging is enabled on the following connectors:

      The default Receive connector named Default Frontend <ServerName> in the Front End
      Transport service on Mailbox servers.

      The implicit and invisible Send connector in the Front End Transport service on Mailbox
      servers.

By default, protocol logging is disabled on all other connectors. You need to enable or disable
protocol logging on each individual connector. You configure other protocol logging options
for all Receive connectors or all Send connectors that exist in each individual transport service
on the Exchange server. All Receive connectors in a transport service share the same protocol
log files and protocol log options. These files and options are separate from the Send
connector protocol log files and protocol log options in the same transport service on the
Exchange server.

<!-- p.1626 -->

By default, Exchange uses circular logging to limit the protocol log based on file size and file
age to help control the hard disk space that's used by the log files. To configure protocol
logging, see Configure protocol logging.

Structure of the protocol log files
By default, the protocol log files exist in the following locations:

     Front End Transport service on Mailbox servers:

        Receive connectors:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpReceive

        Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpSend

     Transport service on Mailbox servers:

        Receive connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Hub\ProtocolLog\SmtpReceive

        Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Hub\ProtocolLog\SmtpSend

     Mailbox Transport Delivery service on Mailbox servers (Receive connectors):
      %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpReceive\Delivery

     Mailbox Transport Submission service on Mailbox servers (Send connectors):
      %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpSend\Submission

     Note: Protocol logging for side effect messages that are submitted after messages are
     delivered to mailboxes occurs in
      %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpSend\Delivery . For

     example, a message that's delivered to a mailbox triggers an Inbox rule that redirects the
     message to another recipient.

     Transport service on Edge Transport servers:

        Receive connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Edge\ProtocolLog\SmtpReceive

        Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Edge\ProtocolLog\SmtpSend

<!-- p.1627 -->

The naming convention for log files is SENDyyyyMMddhh-nnnn.log for Send connectors and
RECVyyyyMMddhh-nnnn.log for Receive connectors. The placeholders represent the following

information:

     yyyyMMddhh is the coordinated universal time (UTC) date when the log file was created.
     yyyy = year, MM = month, dd = day and hh = hour.

     nnnn is an instance number that starts at the value 1 every hour.

Information is written to the log file until the file reaches its maximum size. Then, a new log file
that has an incremented instance number is opened (the first log file is -1, the next is -2, and so
on). Circular logging deletes the oldest log files when either of the following conditions is true:

     A log file reaches its maximum age.

     The protocol log folder reaches its maximum size.

The protocol log files are text files that contain data in the comma-separated value file (CSV)
format. Each protocol log file has a header that contains the following information:

     #Software: The value is Microsoft Exchange Server .

     #Version: Version number of the Exchange server that created the message tracking log
     file. The value uses the format 15.01.nnnn.nnn .

     #Log-Type: The value is either SMTP Receive Protocol Log or SMTP Send Protocol Log .

     #Date: UTC date-time when the log file was created. The UTC date-time is represented in
     the ISO 8601 date-time format: yyyy-MM-ddThh:mm:ss.fffZ, where yyyy = year, MM =
     month, dd = day, T indicates the beginning of the time component, hh = hour, mm =
     minute, ss = second, fff = fractions of a second, and Z signifies Zulu, which is another way
     to denote UTC.

     #Fields: Comma-delimited field names that are used in the protocol log files.

Fields in the protocol log
The protocol log stores each SMTP protocol event on a single line in the log. The information
stored on each line is organized by fields, and these fields are separated by commas. The fields
that are used in the protocol log are described in the following table.

                                                                                  ﾉ   Expand table

<!-- p.1628 -->

 Field name   Description

 date-time    UTC date-time of the protocol event. The UTC date-time is represented in the ISO 8601
              date-time format: yyyy-MM-ddThh:mm:ss.fffZ, where yyyy = year, MM = month, dd = day,
              T indicates the beginning of the time component, hh = hour, mm = minute, ss = second,
              fff = fractions of a second, and Z signifies Zulu, which is another way to denote UTC.

 connector-   Distinguished name (DN) of the connector that's associated with the SMTP event.
 id

 session-id   GUID value that's unique for each SMTP session, but is the same for every event that's
              associated with that SMTP session.

 sequence-    Counter that starts at 0 and is incremented for each event in the same SMTP session.
 number

 local-       Local endpoint of an SMTP session. This consists of an IP address and TCP port number
 endpoint     formatted as <IP address>: <port>.

 remote-      Remote endpoint of an SMTP session. This consists of an IP address and TCP port number
 endpoint     formatted as <IP address>: <port>.

 event        Single character that represents the protocol event. Valid values are:
              + : Connect
               - : Disconnect
               > : Send
               < : Receive
               * : Information

 data         Text information associated with the SMTP event.

 context      Additional contextual information that may be associated with the SMTP event.

One SMTP conversation that represents sending or receiving a single email message generates
multiple SMTP events. Each event is recorded on a separate line in the protocol log. An
Exchange server has many SMTP conversations going on at any given time. This creates
protocol log entries from different SMTP conversations that are mixed together. You can use
the session-id and sequence-number fields to sort the protocol log entries by each individual
SMTP conversation.

<!-- p.1629 -->

Configure protocol logging in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Protocol logging records the SMTP conversations that occur between messaging servers and
between Exchange services in the transport pipeline as part of message delivery.

The following options are available for the protocol logs of all Send connectors and Receive
connectors on the Exchange server:

      Specify the location of the protocol log files. The default locations are:

         Front End Transport service on Mailbox servers:

         Receive connectors:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpReceive

         Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpSend

         Transport service on Mailbox servers:

         Receive connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Hub\ProtocolLog\SmtpReceive

         Send connectors:
         %ExchangeInstallPath%TransportRoles\Logs\Hub\ProtocolLog\SmtpSend

         Mailbox Transport Delivery service on Mailbox servers (Receive connectors):
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpReceive\Delivery

         Mailbox Transport Submission service on Mailbox servers (Send connectors):
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpSend\Submission

         Note: Protocol logging for side effect messages that are submitted after messages are
         delivered to mailboxes occurs in
         %ExchangeInstallPath%TransportRoles\Logs\Mailbox\ProtocolLog\SmtpSend\Delivery .

         For example, a message that's delivered to a mailbox triggers an Inbox rule that
         redirects the message to another recipient.

         Transport service on Edge Transport servers:

<!-- p.1630 -->

    Receive connectors:
     %ExchangeInstallPath%TransportRoles\Logs\Edge\ProtocolLog\SmtpReceive

    Send connectors:
     %ExchangeInstallPath%TransportRoles\Logs\Edge\ProtocolLog\SmtpSend

  Specify a maximum size for the protocol log files. The default size is 10 megabytes (MB).

  Specify a maximum size for the directory that contains the protocol log files. The default
  size is 250 MB.

  Specify a maximum age for the protocol log files. The default age is 30 days.

What do you need to know before you begin?
  Estimated time to complete: 5 minutes

  You need to be assigned permissions before you can perform this procedure or
  procedures. To see what permissions you need, see the "Transport Service", "Front End
  Transport service", "Mailbox Transport service", "Receive connectors" and "Send
  connectors" entries in the Mail flow permissions topic.

  You can use the Exchange admin center (EAC) to enable or disable protocol logging for
  Receive connectors and Send connectors on Mailbox servers. You can also use the EAC to
  configure the protocol log paths for the Transport service only. For all other protocol
  logging options, you need to use the Exchange Management Shell. To learn how to open
  the Exchange Management Shell in your on-premises Exchange organization, see Open
  the Exchange Management Shell.

  You enable or disable protocol logging on each individual connector. You configure other
  protocol logging options for all Receive connectors or all Send connectors that affect
  each individual transport service on the Exchange server. All Receive connectors in a
  transport service share the same protocol log files and protocol log options. These files
  and options are separate from the Send connector protocol log files and protocol log
  options in the same transport service.

    Ｕ Caution

    Don't perform this procedure on an Edge Transport server that has been subscribed
    to the Exchange organization by using EdgeSync. Instead, make the changes in the
    Transport service on the Mailbox server. The changes are then replicated to the Edge
    Transport server the next time EdgeSync synchronization occurs.

<!-- p.1631 -->

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the EAC to configure protocol logging

Use the EAC to enable or disable protocol logging on a
connector
Use this procedure to enable or disable protocol logging on a Send connector or a Receive
connector in the Transport service on Mailbox servers, or a Receive connector in the Front End
Transport service on Mailbox servers.

   1. Open the EAC and navigate to one of the following locations:

           Mail flow > Send connectors.

           Mail flow > Receive connectors.

   2. Select the connector you want to configure, and then click Edit   .

   3. On the General tab in the Protocol logging level section, select one of the following
     options:

           None: Protocol logging disabled on the connector.

           Verbose: Protocol logging is enabled on the connector.

   4. When you're finished, click Save.

Use the EAC to configure the location of the protocol logs on
an Exchange server
Use this procedure to configure the location of the protocol logs for all Send connectors or all
Receive connectors in the Transport service on Mailbox servers.

   1. Open the EAC and navigate to Servers > Servers.

<!-- p.1632 -->

   2. Select the Mailbox server you want to configure, and then click Edit     .

   3. On the server properties page, click Transport logs. In the Protocol log section, change
     the following settings:

           Send protocol log path

           Receive protocol log path

     Specify a location on the local Exchange server. If the folder doesn't exist, it's created
     when you click Save.

   4. When you're finished, click Save.

How do you know this worked?
To verify that you have successfully used the EAC to configure protocol logging, browse to the
location that you specified for the Send connector or the Receive connector protocol logs. If
you enabled protocol logging, verify that a log file exists, and that the file is being updated for
the connector. If you disabled protocol logging, verify that the latest log file is no longer being
updated for the connector.

Use the Exchange Management Shell to enable or
disable protocol logging on a connector

Use the Exchange Management Shell to enable or disable
protocol logging on a Send connector or a Receive connector
Use this procedure to enable or disable protocol logging on:

     A Send connector or a Receive connector in the Transport service on Mailbox servers.

     A Receive connector in the Front End Transport service on Mailbox servers.

     A Send connector or a Receive connector in the Transport service on Edge Transport
     servers.

To enable or disable protocol logging on a Send connector or a Receive connector, use the
following syntax in the Exchange Management Shell:

  PowerShell

<!-- p.1633 -->

  <Set-SendConnector | Set-ReceiveConnector> <ConnectorIdentity> -
  ProtocolLoggingLevel <Verbose | None>

This example enables protocol logging for the Receive connector named Connection from
Contoso.com on the server named Mailbox01.

  PowerShell

  Set-ReceiveConnector "Mailbox01\Connection from Contoso.com" -ProtocolLoggingLevel
  Verbose

This example disables protocol logging for the Send connector named Connection to Internet.

  PowerShell

  Set-ReceiveConnector "Connection to Internet" -ProtocolLoggingLevel None

Use the Exchange Management Shell to enable or disable
protocol logging on the intra-organization Send connector
Use this procedure to enable or disable protocol logging on the implicit and invisible intra-
organization Send connector that exists in the Transport service, the Front End Transport
service, and the Mailbox Transport Submission service on Mailbox servers. For more
information about these connectors, see Implicit Send connectors.

Protocol logging for the intra-organization Send connector occurs in the Send connector
protocol logs for the specified transport service. Note that the Transport service setting
controls protocol logging for the intra-organization Send connector in the Transport service
and in the Mailbox Transport Submission service.

To enable or disable protocol logging on the intra-organization Send connector, use the
following syntax in the Exchange Management Shell:

  PowerShell

  <Set-TransportService | Set-FrontEndTransportService> <ServerIdentity> -
  IntraOrgConnectorProtocolLoggingLevel <Verbose | None>

This example enables protocol logging on the intra-organization Send connector in the
Transport service and in the Mailbox Transport Submission service on the server named
Mailbox01.

<!-- p.1634 -->

  PowerShell

  Set-TransportService Mailbox01 -IntraOrgConnectorProtocolLoggingLevel Verbose

This example disables protocol logging on the intra-organization Send connector in the Front
End Transport service on the same server.

  PowerShell

  Set-FrontEndTransportService Mailbox01 -IntraOrgConnectorProtocolLoggingLevel None

Use the Exchange Management Shell to enable or disable
protocol logging on the mailbox delivery Receive connector
Use this procedure to enable or disable protocol logging on the implicit and invisible mailbox
delivery Receive connector that exists in the Mailbox Transport Delivery service. Protocol
logging for this connector occurs in the Receive connector protocol logs for the Mailbox
Transport Delivery service. For more information about this connector, see Implicit Receive
connectors in the Mailbox Transport Delivery service on Mailbox servers.

To enable or disable protocol logging on the mailbox delivery Receive connector, use the
following syntax in the Exchange Management Shell:

  PowerShell

  Set-MailboxTransportService <ServerIdentity> -
  MailboxDeliveryConnectorProtocolLoggingLevel <Verbose | None>

This example enables protocol logging on the mailbox delivery Receive connector on the
server named Mailbox01.

  PowerShell

  Set-MailboxTransportService Mailbox01 -
  MailboxDeliveryConnectorProtocolLoggingLevel Verbose

This example disables protocol logging on the mailbox delivery Receive connector on the same
server.

  PowerShell

  Set-MailboxTransportService Mailbox01 -

<!-- p.1635 -->

  MailboxDeliveryConnectorProtocolLoggingLevel None

How do you know this worked?
To verify that you have successfully used the Exchange Management Shell to enable or disable
protocol logging on a connector, perform the following steps:

   1. Run the following command in the Exchange Management Shell to verify whether
     protocol logging is enabled or disabled for all connectors on the Exchange server:

          PowerShell

          Write-Host "Send Connectors:" -ForegroundColor yellow; Get-SendConnector |
          Format-List Name,ProtocolLoggingLevel; Write-Host "Receive Connectors:" -
          ForegroundColor yellow; Get-ReceiveConnector | Format-List
          Name,TransportRole,ProtocolLoggingLevel; Write-Host "Mailbox Transport
          Delivery service:" -ForegroundColor yellow; Get-MailboxTransportService |
          Format-List *ProtocolLoggingLevel; Write-Host "Front End Transport service:"
          -ForegroundColor yellow; Get-FrontEndTransportService | Format-List
          *ProtocolLoggingLevel; Write-Host "Transport service and Mailbox Transport
          Submission service:" -ForegroundColor yellow; Get-TransportService | Format-
          List *ProtocolLoggingLevel

   2. Browse to the location of the protocol log. If you enabled protocol logging, verify that a
     log file exists, and that the file is being updated for the connector. If you disabled
     protocol logging, verify that the latest log file is no longer being updated for the
     connector.

Use the Exchange Management Shell to configure
the protocol log settings on an Exchange server
Use this procedure to configure the protocol log settings for all Send connectors or Receive
connectors in a transport service on a Mailbox server, and in the Transport service on an Edge
Transport server.

To configure the protocol log settings in the Exchange Management Shell, use the following
syntax:

  PowerShell

  <Set-FrontEndTransportService | Set-MailboxTransportService | Set-
  TransportService> <ServerIdentity> -ReceiveProtocolLogPath <LocalFilePath> -
  ReceiveProtocolLogMaxFileSize <Size> -ReceiveProtocolLogMaxDirectorySize <Size> -
  ReceiveProtocolLogMaxAge <dd.hh:mm:ss> -SendProtocolLogPath <LocalFilePath> -

<!-- p.1636 -->

  SendProtocolLogMaxFileSize <Size> -SendProtocolLogMaxDirectorySize <Size> -
  SendProtocolLogMaxAge <dd.hh:mm:ss>

This example sets the following protocol log settings in the Transport service on the server
named Mailbox01:

     Sets the location of protocol log for all Receive connectors to D:\Hub SMTP Receive Log
     and the location for all Send connectors to D:\Hub SMTP Send Log. If the folder doesn't
     exist, it's created for you.

     Sets the maximum size of a connector protocol log file for Receive connectors and Send
     connectors to 20 MB.

     Sets the maximum size of the connector protocol log folder for Receive connectors and
     Send connectors to 400 MB.

     Sets the maximum age of a protocol log file for Receive connectors and Send connectors
     to 45 days.

  PowerShell

  Set-TransportService Mailbox01 -ReceiveProtocolLogPath "D:\Hub SMTP Receive Log" -
  ReceiveProtocolLogMaxFileSize 20MB -ReceiveProtocolLogMaxDirectorySize 400MB -
  ReceiveProtocolLogMaxAge 45.00:00:00 -SendProtocolLogPath "D:\Hub SMTP Send Log" -
  SendProtocolLogMaxFileSize 20MB -SendProtocolLogMaxDirectorySize 400MB -
  SendProtocolLogMaxAge 45.00:00:00

Notes:

     Setting the SendProtocolLogPath or ReceiveProtocolLogPath parameters to the value
     $null effectively disables protocol logging for all Send connectors or Receive connectors

     on the server. However, setting the value to $null generates event log errors when
     protocol logging is enabled for any Send connector or Receive connector on the server,
     including the intra-organization Send connector or the mailbox delivery Receive
     connector.

     Setting the ReceiveProtocolLogMaxAge or SendProtocolLogMaxAge parameters to the
     value 00:00:00 prevents the automatic removal of protocol log files because of their age.

How do you know this worked?
To verify that you have successfully used the Exchange Management Shell to configure the
protocol logging settings on an Exchange server, perform the following steps:

<!-- p.1637 -->

1. Run the following command in the Exchange Management Shell and verify the protocol
  log settings on the Exchange server:

    PowerShell

     Write-Host "Front End Transport service:" -ForegroundColor yellow; Get-
     FrontEndTransportService | Format-List ReceiveProtocolLog*,SendProtocolLog*;
     Write-Host "Mailbox Transport Submission and Mailbox Transport Delivery
     services:" -ForegroundColor yellow; Get-MailboxTransportService | Format-List
     ReceiveProtocolLog*,SendProtocolLog*; Write-Host "Transport service:" -
     ForegroundColor yellow; Get-TransportService | Format-List
     ReceiveProtocolLog*,SendProtocolLog*

2. Open the location of the protocol log in Windows Explorer or File Explorer to verify that
  the log files exist, that data is being written to the files, and that the files are being
  recycled based on the maximum file size and maximum directory size values that you
  configured.

<!-- p.1638 -->

Analyze Exchange Server protocol logs
ﾃ   Summarize this article for me

APPLIES TO:         2016            2019   Subscription Edition

Overview
Protocol logs record step-by-step SMTP communication between Exchange Server and other
mail systems. You can use protocol logs to diagnose mail flow issues such as delays, queuing,
rejections, or silent drops. This article describes how to analyze Exchange Server protocol logs
to troubleshoot these issues systematically.

What are Exchange protocol logs
Protocol logs capture SMTP conversations between Exchange servers and other mail servers,
recording each stage of the transaction, such as connection attempts, commands, responses,
and failures. For more information about where protocol logging occurs or the structure and
fields of these logs, see Protocol logging in Exchange Server.

To enable protocol logging and locate the log files, see Configure protocol logging in
Exchange Server.

You can analyze protocol logs using tools such as Notepad, Excel, or PowerShell.

Understanding the log structure
Each protocol log entry contains multiple fields, typically separated by commas. Common fields
include:

      date-time - timestamp of the event

      connector-id - connector handling the session
      session-id - unique identifier of the SMTP session

      sequence-number - order of commands in the session

      local-endpoint / remote-endpoint - IP and port information
      event - type of SMTP action (CONNECT, EHLO, MAIL, RCPT, DATA, QUIT)

      data - SMTP commands or server responses

The session-id is especially important because it allows you to trace a complete SMTP
conversation from start to finish.

<!-- p.1639 -->

Tips for analyzing logs
When troubleshooting, identifying the exact issue within large log volumes is challenging. On a
busy server, logs can grow large, and a single SMTP session might span multiple log files. Use
the Select-String command to search for specific strings in these logs. You can search using the
sender's email address, recipient's email address, remote server's IP address, or similar
identifiers.

For example, to search for emails from John@contoso.com , run the following command:

  PowerShell

  Get-ChildItem | Select-String -Pattern "john@contoso.com"

If multiple emails from John@contoso.com exist, first identify the UTC time when the issue
occurred and copy the session ID from the log entry.

                                                                                              

Next, run a recursive search for that session ID across all log files in the folder and export the
results. Make sure to replace the session ID in the command with the one you copied from the
log entry. This approach lets you trace the complete SMTP conversation for that session:

  PowerShell

  Get-ChildItem | Select-String -Pattern "08DE5DE2C7E763C9" | Out-File -FilePath
  "C:\ProtocolLogAnalysis\Output.log"

The output file will have the SMTP conversation for that session, from start to finish.

What to look for in the protocol log
When you have the filtered protocol log, review the following items to troubleshoot a mail flow
issue:

connector-id - Check the connector-id to verify that email is using the correct connector for
outbound or inbound delivery. This is especially important for hybrid mail flow scenarios where

<!-- p.1640 -->

Exchange Server sends email to Exchange Online through a connector named Outbound to
Office 365 .

                                                                                           

TLS and Certificate Issues - Check for STARTTLS commands and responses. Verify that the on-
premises Exchange Server uses the correct certificate by examining the certificate subject name
and issuer name. Confirm that TLS negotiation succeeds and note the certificate thumbprint.

                                                                                           

Inbound mail not received

When external senders report delivery failures or delays:

     Search the protocol logs for the sender's IP address or domain.
     Look for CONNECT and EHLO events to confirm whether the remote server reached your
     Exchange Server.
     Check for 550 , 554 , or 451 SMTP responses indicating rejection, policy blocks, or
     temporary failures.

If the logs show no connection attempt, the issue likely exists upstream (DNS, firewall, or on
the sender's side).

Outbound mail stuck in the queue
For messages stuck in the outbound queue:

     Review send connector protocol logs.
     Identify repeated connection attempts to the same remote host.
     Look for errors such as:
