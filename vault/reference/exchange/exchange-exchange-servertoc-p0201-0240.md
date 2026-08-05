---
title: "Exchange Server — pages 201-240"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0201-0240
family: exchange
documentKind: "doc"
abstract: "Add proxy addresses: The rewritten email address needs to be configured as a proxy address on all affected senders in the affected domains. For example, if joe@sales.contoso.com is rewritten to joe@contoso.com, you need to add the proxy address joe@contoso.com to Joe's mailbox."
---

# Exchange Server — pages 201-240

<!-- p.201 -->

     Add proxy addresses: The rewritten email address needs to be configured as a proxy
     address on all affected senders in the affected domains. For example, if
     joe@sales.contoso.com is rewritten to joe@contoso.com, you need to add the proxy
     address joe@contoso.com to Joe's mailbox. This allows replies and inbound messages to
     be delivered correctly.

     Mail contacts for non-Exchange organizations: If you're rewriting email addresses from a
     non-Exchange email system, you need to create mail contacts in Exchange to represent
     the users in the non-Exchange email system. These email contacts need to contain the
     original email addresses and the rewritten email addresses. For example, if
     joe@unix.contoso.com is rewritten to joe@contoso.com, you need to create a mail
     contact with joe@unix.contoso.com as the external email address and joe@contoso.com
     as a proxy address.

Verify unique aliases
When you rewrite email addresses in multiple subdomains, you need to make sure that all
email aliases are unique across all your subdomains. For example, consider the following
configuration:

The following users are in the subdomains sales.contoso.com, marketing.contoso.com, and
research.contoso.com:

     maria@sales.contoso.com

     chris@sales.contoso.com

     david@marketing.contoso.com

     brian@marketing.contoso.com

     chris@research.contoso.com

     adam@research.contoso.com

Suppose you want to rewrite the subdomains sales.contoso.com, marketing.contoso.com, and
research.contoso.com into the single domain contoso.com.

When the email addresses in each subdomain are rewritten, a conflict occurs between
chris@sales.contoso.com and chris@research.contoso.com, because both email addresses are
rewritten to chris@contoso.com. To resolve this issue, you need to change the email address of
one of the affected recipients. For example, you can change chris@research.contoso.com to
christopher@research.contoso.com so the email address is rewritten to
christopher@contoso.com.

<!-- p.202 -->

Priority of address rewrite entries
If a user's email address matches multiple address rewrite entries, the email address is only
rewritten once based on the closest match. The following list describes the order of precedence
of address rewrite entries from highest priority to lowest priority:

   1. Individual email addresses: An address rewrite entry is configured to rewrite the email
     address of john@contoso.com to support@contoso.com.

   2. Domain or subdomain mapping: An address rewrite entry is configured to rewrite all
     contoso.com email addresses to northwindtraders.com or all sales.contoso.com email
     addresses to contoso.com.

   3. Domain flattening: An address rewrite entry is configured to rewrite *.contoso.com email
     addresses to contoso.com.

For example, consider an Edge Transport server where the following outbound address rewrite
entries are configured:

     *.contoso.com email addresses are rewritten to contoso.com

     japan.sales.contoso.com email addresses are rewritten to contoso.jp

If masato@japan.sales.contoso.com sends an email message, the address is rewritten to
masato@contoso.jp, because that entry most closely matches the sender's email address.

Digitally signed, encrypted, and rights-protected
messages
Address rewriting shouldn't affect most signed, encrypted, or rights-protected messages. If
address rewriting were to invalidate or otherwise change the security status of these types of
messages in any way, address rewriting isn't applied.

The following values can be rewritten because the information isn't part of message signing,
encryption, or rights protection:

     Fields in the message envelope.

     Top-level message body headers.

The following values aren't rewritten because the information is part of message signing,
encryption, or rights protection:

     Header fields located inside MIME body parts that may be signed.

<!-- p.203 -->

The boundary string parameter of the MIME content type.

<!-- p.204 -->

Address rewriting procedures on Edge
Transport servers
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

You can create address rewrite entries on Edge Transport servers that apply to a single
recipient, a specific domain or subdomain, or multiple subdomains. Address rewriting can be
outbound only, or inbound and outbound (bidirectional). When you create address rewrite
entries, remember the following:

      Verify that the resulting email addresses are unique in your organization.

      Only literal strings are supported in the email address values.

      The wildcard character (*) is supported only in the internal address (the addresses you
      want to change). Valid syntax for using the wildcard character is *.contoso.com. The
      values *contoso.com or sales.*.com are not allowed.

      When you use the wildcard character, you need to configure the address rewriting as
      outbound only (you need to set the OutboundOnly parameter to the value $true ), and
      outbound only address rewriting requires that you configure the rewritten email address
      as a proxy address on the affected recipients.

      By default, address rewriting is bidirectional for a single recipient, or for a specific domain
      or subdomain (the default value for the OutboundOnly parameter is $false ).

For more information about address rewriting, see Address rewriting on Edge Transport
servers.

What do you need to know before you begin?
      Estimated time to complete each procedure: 10 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Edge Transport servers" section
      in the Mail flow permissions topic.

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

<!-- p.205 -->

     Be careful when you configure address rewriting. Any changes that you make are
     immediately applied when you run the command. Consider running the command with
     the WhatIf parameter. For more information about the WhatIf parameter, see WhatIf and
     Confirm.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Use the Exchange Management Shell to enable or
disable address rewriting
To completely enable or disable address rewriting, you enable or disable the address rewriting
agents. By default, the address rewriting agents on an Edge Transport server are enabled.

To disable address rewriting, run the following command:

  PowerShell

  Disable-TransportAgent "Address Rewriting Inbound Agent"; Disable-TransportAgent
  "Address Rewriting Outbound Agent"

To enable address rewriting, run the following command:

  PowerShell

  Enable-TransportAgent "Address Rewriting Inbound Agent"; Enable-TransportAgent
  "Address Rewriting Outbound Agent"

How do you know this worked?
To verify that you have successfully enabled or disabled address rewriting, run the following
command to verify the Enabled property value:

  PowerShell

  Get-TransportAgent "Address Rewriting *"

<!-- p.206 -->

Use the Exchange Management Shell to view
address rewrite entries
To view a summary list of all address rewrite entries, run the following command.

  PowerShell

  Get-AddressRewriteEntry

To view details of an address rewrite entry, use the following syntax.

  PowerShell

  Get-AddressRewriteEntry <AddressRewriteEntryIdentity> | Format-List

The following example displays the details of the address rewrite entry named Rewrite
Contoso.com to Northwindtraders.com:

  PowerShell

  Get-AddressRewriteEntry "Rewrite Contoso.com to Northwindtraders.com" | Format-
  List

For more information, see Get-AddressRewriteEntry.

Use the Exchange Management Shell to create
address rewrite entries

Rewrite the email address for a single recipient
To rewrite the email address for a single recipient, use the following syntax:

  PowerShell

  New-AddressRewriteEntry -Name "<Descriptive Name>" -InternalAddress <internal
  email address> -ExternalAddress <external email address> [-OutboundOnly <$true |
  $false>]

This example rewrites the email address of all messages entering and leaving the Exchange
organization for joe@contoso.com. Outbound messages are rewritten so they appear to come
from support@nortwindtraders.com. Inbound messages sent to

<!-- p.207 -->

support@northwindtraders.com are rewritten to joe@contoso.com for delivery to the recipient
(the OutboundOnly parameter is $false by default).

  PowerShell

  New-AddressRewriteEntry -Name "joe@contoso.com to support@northwindtraders.com" -
  InternalAddress joe@contoso.com -ExternalAddress support@northwindtraders.com

Rewrite email addresses in a single domain or subdomain
To rewrite the email addresses in a single domain or subdomain, use the following syntax:

  PowerShell

  New-AddressRewriteEntry -Name "<Descriptive Name>" -InternalAddress <domain or
  subdomain> -ExternalAddress <domain> [-OutboundOnly <$true | $false>]

This example rewrites the email addresses of all messages entering and leaving the Exchange
organization for the contoso.com domain. Outbound messages are rewritten so they appear to
come from the fabrikam.com domain. Inbound messages sent to fabrikam.com email
addresses are rewritten to contoso.com for delivery to the recipients (the OutboundOnly
parameter is $false by default).

  PowerShell

  New-AddressRewriteEntry -Name "Contoso to Fabrikam" -InternalAddress contoso.com -
  ExternalAddress fabrikam.com

This example rewrites the email addresses of all messages leaving the Exchange organization
for the sales.contoso.com subdomain. Outbound messages are rewritten so they appear to
come from the contoso.com domain. Inbound messages sent to contoso.com email addresses
aren't rewritten.

  PowerShell

  New-AddressRewriteEntry -Name "sales.contoso.com to contoso.com" -InternalAddress
  sales.contoso.com -ExternalAddress contoso.com -OutboundOnly $true

Rewrite email addresses in multiple subdomains
To rewrite the email addresses in a domain and all subdomains, use the following syntax.

<!-- p.208 -->

  PowerShell

  New-AddressRewriteEntry -Name "<Descriptive Name>" -InternalAddress *.<domain> -
  ExternalAddress <domain> -OutboundOnly $true [-ExceptionList <domain1,domain2...>]

This example rewrites the email addresses of all messages leaving the Exchange organization
for the contoso.com domain and all subdomains. Outbound messages are rewritten so they
appear to come from the contoso.com domain. Inbound messages sent to contoso.com
recipients can't be rewritten, because a wildcard is used in the InternalAddress parameter.

  PowerShell

  New-AddressRewriteEntry -Name "Rewrite all contoso.com subdomains" -
  InternalAddress *.contoso.com -ExternalAddress contoso.com -OutboundOnly $true

This example is just like the previous example, except now messages sent from the
legal.contoso.com and corp.contoso.com subdomains are never rewritten:

  PowerShell

  New-AddressRewriteEntry -Name "Rewrite all contoso.com subdomains except
  legal.contoso.com and corp.contoso.com" -InternalAddress *.contoso.com -
  ExternalAddress contoso.com -OutboundOnly $true -ExceptionList
  legal.contoso.com,corp.contoso.com

For more information, see New-AddressRewriteEntry.

How do you know this worked?
To verify that you have successfully created address rewrite entries, do the following:

   1. Replace <AddressRewriteEntryIdentity> with the name of the address rewrite entry, and
     run the following command to verify the property values:

        PowerShell

        Get-AddressRewriteEntry <AddressRewriteEntryIdentity> | Format-List

   2. From a mailbox that's affected by the address rewrite entry, send a test message to an
     external mailbox. Verify the test message appears to originate from the rewritten email
     address.

   3. Reply to the test message from the external mailbox. Verify the original mailbox receives
     the reply.

<!-- p.209 -->

Use the Exchange Management Shell to modify
address rewrite entries
The configuration options that are available when you modify an existing address rewrite entry
are identical to the configuration options when you create a new address rewrite entry.

Modify an address rewrite entry for a single recipient
To modify an address rewrite entry that rewrites the email address of a single recipient, use the
following syntax:

  PowerShell

  Set-AddressRewriteEntry <AddressRewriteEntryIdentity> [-Name "<Descriptive Name>"]
  [-InternalAddress <internal email address>] [-ExternalAddress <external email
  address>] [-OutboundOnly <$true | $false>]

This example modifies the following properties of the address rewrite entry named
"joe@contoso.com to support@nortwindtraders.com":

     Changes the external address to support@northwindtraders.net.

     Changes the name of the address rewrite entry to "joe@contoso.com to
     support@northwindtraders.net".

     Changes the value of OutboundOnly to $true . Note that this change requires you to
     configure support@northwindtraders.net as a proxy address on Joe's mailbox.

  PowerShell

  Set-AddressRewriteEntry "joe@contoso.com to support@nortwindtraders.com" -Name
  "joe@contoso.com to support@northwindtraders.net" -ExternalAddress
  support@northwindtraders.net -OutboundOnly $true

Modify an address rewrite entry for a single domain or
subdomain
To modify an address rewrite entry that rewrites the email addresses from a single domain or
subdomain, use the following syntax.

  PowerShell

<!-- p.210 -->

  Set-AddressRewriteEntry <AddressRewriteEntryIdentity> [-Name "<Descriptive Name>"]
  [-InternalAddress <domain or subdomain>] [-ExternalAddress <domain>] [-
  OutboundOnly <$true | $false>]

This example changes the internal address value of the address rewrite entry named
"Northwind Traders to Contoso".

  PowerShell

  Set-AddressRewriteEntry "Northwindtraders to Contoso" -InternalAddress
  northwindtraders.net

Modify an address rewrite entry for multiple subdomains
To modify an address rewrite entry that rewrites the email addresses in a domain and all
subdomains, use the following syntax.

  PowerShell

  Set-AddressRewriteEntry <AddressRewriteEntryIdentity> [-Name "<Descriptive Name>"]
  [-InternalAddress *.<domain>] [-ExternalAddress <domain>] [-ExceptionList <list of
  domains>]

To replace the existing exception list values of an address rewrite entry, use the following
syntax:

  PowerShell

  Set-AddressRewriteEntry <AddressRewriteEntryIdentity> -ExceptionList
  <domain1,domain2,...>

This example replaces the existing exception list for the address rewrite entry named Contoso
to Northwind Traders with the values marketing.contoso.com and legal.contoso.com:

  PowerShell

  Set-AddressRewriteEntry "Contoso to Northwind Traders" -ExceptionList
  sales.contoso.com,legal.contoso.com

To add or remove exception list values without affecting other exception list entries, use the
following syntax:

  PowerShell

<!-- p.211 -->

  Set-AddressRewriteEntry <AddressRewriteEntryIdentity> -ExceptionList @{Add="
  <domain1>","<domain2>"...; Remove="<domain3>","<domain4>"...}

This example adds finanace.contoso.com and removes marketing.contoso.com from the
exception list of the address rewrite entry named Contoso to Northwind Traders:

  PowerShell

  Set-AddressRewriteEntry "Contoso to Northwind Traders" -ExceptionList
  @{Add="finanace.contoso.com"; Remove="marketing.contoso.com"}

For more information, see Set-AddressRewriteEntry.

How do you know this worked?
To verify that you have successfully modified an address rewrite entry, do the following:

   1. Replace <AddressRewriteEntryIdentity> with the name of the address rewrite entry, and
     run the following command to verify the property values:

        PowerShell

        Get-AddressRewriteEntry <AddressRewriteEntryIdentity> | Format-List

   2. From a mailbox that's affected by the address rewrite entry, send a test message to an
     external mailbox. Verify the test message appears to originate from the rewritten email
     address.

   3. From the external mailbox, reply to the test message. Verify the original mailbox receives
     the reply.

Use the Exchange Management Shell to remove
address rewrite entries
To remove a single address rewrite entry, use the following syntax:

  PowerShell

  Remove-AddressRewriteEntry <AddressRewriteEntryIdentity>

<!-- p.212 -->

This example removes the address rewrite entry named "Contoso.com to
Northwindtraders.com":

  PowerShell

  Remove-AddressRewriteEntry "Contoso.com to Northwindtraders.com"

To remove multiple address rewrite entries, use the following syntax:

  PowerShell

  Get-AddressRewriteEntry [<search criteria>] | Remove-AddressRewriteEntry [-WhatIf]

This example removes all address rewrite entries:

  PowerShell

  Get-AddressRewriteEntry | Remove-AddressRewriteEntry

This example simulates the removal of address rewrite entries that contain the text "to
contoso.com" in the name. The WhatIf switch allows you to preview the result without
committing any changes.

  PowerShell

  Get-AddressRewriteEntry "*to contoso.com" | Remove-AddressRewriteEntry -WhatIf

If you're satisfied with the result, run the command again without the WhatIf switch to remove
the address rewrite entries.

  PowerShell

  Get-AddressRewriteEntry "*to contoso.com" | Remove-AddressRewriteEntry

For more information, see Remove-AddressRewriteEntry.

How do you know this worked?
To verify that you have successfully removed an address rewrite entry, do the following:

   1. Run the command Get-AddressRewriteEntry , and verify that the address rewrite entries
     you removed aren't listed.

<!-- p.213 -->

2. From a mailbox that was affected by the address rewrite entry, send a test message to an
  external mailbox. Verify the test message is no longer affected by the removed address
  rewrite entry.

3. From the external mailbox, reply to the test message. Verify the original mailbox receives
  the reply and that the message is unaffected by the removed address rewrite entry.

<!-- p.214 -->

Import address rewrite entries on Edge
Transport servers in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016       2019      Subscription Edition

You can bulk-create or import address rewriting information into an Edge Transport server by
using a comma-separated value (CSV) file. The following list describes common scenarios that
require you to do this:

      You are replacing an address rewriting solution with an Edge Transport server.

      You enter into an agreement with a third-party solution provider that requires you to
      rewrite their email addresses.

      You acquire another organization, and you need to temporarily rewrite the email
      addresses in the acquired organization.

You can use a spreadsheet application like Microsoft Excel to create the CSV file. Format the file
as described in this topic and save it as a .csv file.

The first row, or header row, of the CSV file lists the names of the parameters. Each parameter is
separated by a comma. The required and optional parameters are described in the following
table.

                                                                                         ﾉ   Expand table

 Parameter         Required    Description
                   or
                   optional

 Name              Required    A unique, descriptive name for the address rewrites entry.

 InternalAddress   Required    The address you want to change. You can use the following values:
                                     A single email address (chris@contoso.com)
                                     A single domain or subdomain (contoso.com or sales.contoso.com)
                                     A domain and all subdomains (*.contoso.com)

 ExternalAddress   Required    The final email address you want. You can use the following values:
                                     A single email address if you specified a single email address for
                                     InternalAddress
                                     A single domain or subdomain for all other values of
                                     InternalAddress

<!-- p.215 -->

 Parameter       Required   Description
                 or
                 optional

 ExceptionList   Optional   Available only when you're rewriting email addresses in a domain and all
                            subdomains (*.contoso.com). Specifies one or more subdomains you want
                            to exclude from address rewriting. Enclose the value in double quotation
                            marks, and separate multiple values by commas. For example,
                             "marketing.contoso.com" or "marketing.contoso.com,legal.contoso.com" .

 OutboundOnly    Optional    False means that addresses are written on inbound and outbound mail.
                             True means that addresses are rewritten on outbound mail only, and you
                            need to manually configure the rewritten email address as a proxy address
                            on the affected recipients.
                            The default value is False , but you need to set it to True if
                            InternalAddress contains the wildcard character (*.contoso.com).
                            The OutboundOnly parameter value in the CSV file is True or False , not
                             $True or $False .

Each row under the header row represents an individual address rewrite entry. The values in
each row need to be in the same order as the parameter names in the header row. Each value
is separated by a comma.

What do you need to know before you begin?
     Estimated time to complete this task: 15 minutes

     Make sure you understand the ramifications of address rewriting. For example, the
     rewritten email address need to be unique in your Exchange organization, and you might
     need to configure proxy addresses on the affected recipients. For more information, see
     Address rewriting on Edge Transport servers and Address rewriting procedures on Edge
     Transport servers.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Address Rewriting agent" entry in
     the Mail flow permissions topic.

     If you have more than one Edge Transport server, we recommend that you use the
     procedures in this topic to import the address rewrite entries into a single Edge Transport
     server and then clone the configuration of that Edge Transport server to the other Edge
     Transport servers in your organization. For more information about how to clone an Edge
     Transport server, see Using Edge Transport Server Cloned Configuration.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

<!-- p.216 -->

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Step 1: Create the CSV file
When you create the CSV file, consider the following items:

     If you specify values for optional parameters in the CSV file, every row must include a
     value in that column. If you want to create multiple address rewrite entries where some
     entries have optional parameters and some entries do not, you need to separate those
     address rewrite entries into different CSV files, and then import each CSV file separately.

     If the CSV file contains non-ASCII characters, be sure to save the CSV file with UTF-8
     encoding or other Unicode encoding. Saving the CSV file with UTF-8 encoding or other
     Unicode encoding might be easier when the system locale of the computer matches the
     language that's used in the CSV file.

The following example shows how a CSV file can be populated with the optional ExceptionList
and OutboundOnly parameters included:

  CSV

  Name,InternalAddress,ExternalAddress,ExceptionList,OutboundOnly
  "Wingtip
  UK",*.wingtiptoys.co.uk,tailspintoys.com,"legal.wingtiptoys.co.uk,finance.wingtipt
  oys.co.uk,support.wingtiptoys.co.uk",True
  "Wingtip
  USA",*.wingtiptoys.com,tailspintoys.com,"legal.wingtiptoys.com,finance.wingtiptoys
  .com,support.wingtiptoys.com,corp.wingtiptoys.com",True
  "Wingtip
  Canada",*.wingtiptoys.ca,tailspintoys.com,"legal.wingtiptoys.ca,finance.wingtiptoy
  s.ca,support.wingtiptoys.ca",True

Step 2: Import the CSV file
To import the CSV file, use the following syntax:

  PowerShell

  Import-Csv <FileNameAndPath> | ForEach {New-AddressRewriteEntry -Name $_.Name -
  InternalAddress $_.InternalAddress -ExternalAddress $_.ExternalAddress -

<!-- p.217 -->

  OutboundOnly ([Bool]::Parse($_.OutboundOnly)) -ExceptionList $_.ExceptionList}

This example imports the address rewrite entries from C:\My
Documents\ImportAddressRewriteEntries.csv.

  CSV

  Import-Csv "C:\My Documents\ImportAddressRewriteEntries.csv" | ForEach {New-
  AddressRewriteEntry -Name $_.Name -InternalAddress $_.InternalAddress -
  ExternalAddress $_.ExternalAddress -OutboundOnly ([Bool]::Parse($_.OutboundOnly))
  -ExceptionList $_.ExceptionList}

How do you know this step worked?
To verify that you have successfully imported address rewrite entries from a CSV file, use either
of the following procedures:

     To see all address rewrite entries, run the following command:

        PowerShell

        Get-AddressRewriteEntry

     To see details about a specific address rewrite entry, replace <AddressRewriteIdentity>
     with the name of the address rewrite entry, and run the following command:

        PowerShell

        Get-AddressRewriteEntry "<AddressRewriteIdentity>" | Format-List

<!-- p.218 -->

Client Access services
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

In Exchange Server, the Client Access services on Mailbox servers provide authentication and
proxy services for internal and external client connections. The Client Access services are
stateless, so data isn't queued or stored in them. In Exchange Server, the Client Access services
are part of the Mailbox server, so you can't configure a standalone Client Access server like you
could in previous versions of Exchange. For more information, see Client access protocol
architecture.

Client connectivity in Exchange 2016 and Exchange 2019 is similar to Exchange 2013, but
different from Exchange 2010:

      Outlook clients use MAPI over HTTP or Outlook Anywhere (RPC over HTTP). In Exchange
      2016 and Exchange 2019, MAPI over HTTP is enabled by default.

      Exchange 2016 and Exchange 2019 require fewer namespaces for site-resilient solutions
      than Exchange 2010. For more information, see Namespace Planning in Exchange 2016              .

Client Access services functionality
The Client Access services in Exchange Server function much like a front door, admitting all
client connection requests and routing them to the correct mailbox database. The Client Access
services provide network security such as Transport Layer Security (TLS) encryption, and
manage client connections through redirection and proxying. The Client Access services
authenticate client connections and typically proxy the connection request to the Mailbox
server that holds the active copy of the user's mailbox. In some cases, the Client Access services
might redirect the request to the Client Access services on another Exchange server, either in a
different location or on a more recent version of Exchange.

The Client Access services have the following features:

      Stateless services: In previous versions of Exchange, many of the Client Access protocols
      required session affinity. For example, Outlook Web App in Exchange 2010 required that
      all requests from a particular client be handled by a specific Client Access server within a
      load balanced array of Client Access servers. In Exchange 2016 and Exchange 2019, the
      Client Access services are stateless. In other words, because all processing for the mailbox
      happens in the backend services on the Mailbox server, it doesn't matter which instance
      of the Client Access service in an array of Client Access services receives each individual
      client request. This means that session affinity is no longer required at the load balancer

<!-- p.219 -->

    level. This allows inbound connections to Client Access services to be balanced by using
    simple load balancing techniques such as DNS round-robin. It also allows hardware load
    balancing devices to support significantly more concurrent connections. For more
    information, see Load Balancing in Exchange 2016 .

    Connection pooling: The Client Access services handle client authentication and send the
    AuthN data to the backend services on the Mailbox server. The account that's used by the
    Client Access services to connect to the backend services on Mailbox servers is a
    privileged account that's a member of the Exchange Servers group. This allows the Client
    Access services to pool connections to the backend services on Mailbox servers
    effectively. An array of Client Access services can handle millions of client connections
    from the Internet, but far fewer connections are used to proxy the requests to the
    backend services on Mailbox servers than in Exchange 2010. This improves processing
    efficiency and end-to-end latency.

 ７ Note

 Don't confuse an array of Client Access services with an RPC Client Access Server array
 that was used for RPC over TCP client connections in Exchange 2010. In Exchange 2016
 and Exchange 2019, an array of Client Access services simply indicates a group of load-
 balanced Client Access services on Exchange 2016 or Exchange 2019 servers.

Management tasks in the Client Access services
    Digital certificates: Although Exchange Server uses self-signed certificates to encrypt and
    authenticate connections between Exchange servers, you need to install and configure
    certificates to encrypt client connections. For more information, see Digital certificates
    and encryption in Exchange Server.

    Kerberos authentication for load-balanced Client Access services: For more information,
    see Configure Kerberos authentication for load-balanced Client Access services.

<!-- p.220 -->

Exchange admin center in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

The Exchange admin center (EAC) is the web-based management console in Exchange Server
that's optimized for on-premises, online, and hybrid Exchange deployments. The EAC was
introduced in Exchange Server 2013, and replaces the Exchange Management Console (EMC)
and the Exchange Control Panel (ECP), which were the two management interfaces in Exchange
Server 2010.

Looking for the Exchange Online version of this article? See Exchange admin center in
Exchange Online.

Looking for the standalone Exchange Online Protection (EOP) version of this article? See
Exchange admin center in EOP.

Accessing the EAC
The URL of the EAC is controlled by the Internet Information Services (IIS) virtual directory
named ECP in the Client Access (frontend) services on the Mailbox server. Yes, the virtual
directory is named ECP, not EAC.

      Internal URL: By default, this value contains the fully qualified domain name (FQDN) of
      the Exchange server in the format https://<ServerFQDN>/ecp . For example,
      https://mailbox01.contoso.com/ecp . To access the EAC in a web browser on the Exchange

      server itself, you can use the value https://localhost/ecp .

      External URL: By default, this value is unconfigured. Before you can connect to the EAC
      from the Internet, you need to configure the following settings:

         The external URL value on the ECP virtual directory. For more information, see Step 4:
         Configure external URLs in Configure mail flow and client access on Exchange servers.

         A corresponding record in your public DNS.

         A TLS certificate that contains or matches the host name entry. Likely, this certificate is
         a subject alternative name (SAN) certificate or a wildcard certificate, because most of
         the client services are all available under the same website on the Exchange server. For
         more information, see Certificate requirements for Exchange services.

         After you configure the settings, a common external URL value for the EAC would
         resemble https://mail.contoso.com/ecp .

<!-- p.221 -->

        Note: External users who connect to Outlook on the web (formerly known as Outlook
        Web App) also need access to the EAC to access their own Options page. You can
        disable external administrator access to the EAC while still allowing users to access
        their Options page in Outlook on the web. For more information, see Turn off access
        to the Exchange admin center.

The easiest way to find the internal and external URL values for the EAC (without using Servers
> Virtual directories in the EAC itself) is by using the Get-EcpVirtualDirectory cmdlet in the
Exchange Management Shell. To learn how to open the Exchange Management Shell in your
on-premises Exchange organization, see Open the Exchange Management Shell.

These examples show you how to find the internal and external URL values for the EAC virtual
directories in your organization:

     To find the values on all Exchange servers in your organization, run the following
     command:

        PowerShell

        Get-EcpVirtualDirectory | Format-List Server,Name,*Url

     To find the values on the server named Mailbox01 , run the following command:

        PowerShell

        Get-EcpVirtualDirectory | Format-List Name,*Url

     To find the value for the virtual directory named ecp (Default Web Site) on the server
     named Mailbox01 , run the following command.

        PowerShell

        Get-EcpVirtualDirectory -Identity "Mailbox01\ecp (Default Web Site)" |
        Format-List *Url

For more information, see Get-EcpVirtualDirectory.

In Exchange 2016, if you're in a coexistence environment with Exchange 2010, the location of
your mailbox controls the default behavior for opening the EAC or ECP:

     If your mailbox is located on the Exchange 2010 Mailbox server, you get the Exchange
     2010 ECP by default. You can access the EAC by adding the Exchange version to the URL
     (which is 15 for both Exchange 2013 and Exchange 2016). For example, to access the EAC

<!-- p.222 -->

     through the Client Access (frontend) services on the Mailbox server named Mailbox01 ,
     use the following URL: https://Mailbox01/ecp/?ExchClientVer=15 .

     If your mailbox is located on an Exchange 2016 Mailbox server, and you want to access
     the ECP on the Exchange 2010 Client Access server named CAS01, use the following URL:
      https://CAS01/ecp/?ExchClientVer=14 .

Common user interface elements in the EAC
The section describes the user interface elements that are common across the EAC.

1: Cross-premises navigation
The cross-premises navigation allows you to easily switch between your Exchange Online and
on-premises Exchange deployments. If you don't have an Exchange Online organization, the
Office 365 link takes you to a page that compares plans and pricing for Microsoft 365 and
Office 365 services.

2: Feature pane
The feature pane is the first level of navigation for most tasks that you perform in the EAC, and
is organized by the following feature areas:

<!-- p.223 -->

Recipients: Manage mailboxes, groups, resource mailboxes (room and equipment
mailboxes), contacts, shared mailboxes, and mailbox migrations and moves. For more
information, see the following articles:

   Create user mailboxes in Exchange Server and Manage user mailboxes

   Manage distribution groups and Manage dynamic distribution groups

   Create and manage room mailboxes

   Manage mail contacts and Manage mail users

   Create shared mailboxes in the Exchange admin center

Permissions: Manage role-based access control (RBAC) administrator roles, user roles,
and Outlook on the web policies. For more information, see the following articles.

   Manage role groups , Manage role group members, and Manage role assignment
   policies.

   View or configure Outlook on the web mailbox policy properties

Compliance management: This is where you manage In-Place eDiscovery, In-Place Hold,
auditing (mailbox audit logging and administrator audit logging), data loss prevention
(DLP), retention policies, retention tags, and journal rules. For more information, see the
following articles:

   In-Place eDiscovery in Exchange Server and In-Place Hold and Litigation Hold in
   Exchange Server

   Mailbox audit logging in Exchange Server and Administrator audit logging in Exchange
   Server

   Data loss prevention in Exchange Server

   Retention policies and Retention tags.

   Journaling in Exchange Server

Organization: Manage federated sharing, Outlook Apps, and address lists. For more
information, see the following articles:

   Sharing

   Install or remove add-ins for Outlook for your Exchange 2013 organization

   Address lists in Exchange Server

<!-- p.224 -->

Protection: Manage antimalware protection for your organization. For more information,
see Antimalware protection in Exchange Server.

Mail flow: Manage mail flow rules (also known as transport rules), delivery reports,
accepted domains, remote domains, email address policies, Receive connectors, and Send
connectors. For more information, see the following articles:

   Mail flow rules in Exchange Server

   Track messages with delivery reports

   Address lists in Exchange Server

   Accepted domains in Exchange Server

   Remote Domains

   Email address policies in Exchange Server

   Receive connectors

   Send connectors

Mobile: Manage the mobile devices that you allow to connect to your organization. You
can manage mobile device access and mobile device mailbox policies. For more
information, see the following articles:

   Mobile devices

   Mobile device mailbox policies

Public folders: Manage public folders and public folder mailboxes. For more information,
see Public folders.

Unified Messaging: Manage UM dial plans and UM IP gateways. (UM isn't available in
Exchange 2019.) For more information, see the following articles:

   UM Dial Plans

   UM IP Gateways

Servers: View and manage server-specific settings, databases, database availability
groups (DAGs), virtual directories, and certificates. For more information, see the following
articles:

   POP3 and IMAP4 in Exchange Server

<!-- p.225 -->

          Configure the Startup Mode on a Client Access Server and Configure the Startup Mode
          on a Mailbox Server

          Message retry, resubmit, and expiration intervals

          Configure message tracking , Configure connectivity logging in Exchange Server, and
          Protocol logging

          Manage Outlook Anywhere

          Manage mailbox database copies

          Manage database availability groups

          Virtual Directory Management

          Certificate procedures in Exchange Server

        Hybrid: Set up and configure a Hybrid organization.

3: Tabs
The Setup tab allows you to run the Hybrid Configuration Wizard or modify the settings of
your existing hybrid deployment.

4: Toolbar
When you select most tabs, you see a toolbar. The toolbar has icons that perform specific
actions. The following table describes the most common icons and their actions. To see the
action that's associated with an icon (the icon's title), simply hover over the icon.

                                                                                         ﾉ   Expand table

 Icon     Name          Action

          Add, New      Create a new object.
                        Some of these icons have an associated down arrow you can select to show
                        additional objects you can create. For example, in Recipients > Mailboxes, clicking
                        the down arrow displays User mailbox and Linked mailbox as additional options.

          Edit          Edit an object.

          Delete        Delete an object. Some delete icons have a down arrow you can select to show
                        additional options.

          Search        Open a search box so you can enter text for an object that you want to find you

<!-- p.226 -->

 Icon     Name           Action

                         want to find in a long list of objects.

          Refresh        Refresh the list view.

          More options   View more actions you can perform for that tab's objects.
                         For example, in Recipients > Mailboxes clicking this icon shows the following
                         options: Disable, Add/Remove columns, Export data to a CSV file, Connect a
                         mailbox, and Advanced search.

          Up arrow       Move an object up or down in the list, when the order is important.
          and down       For example, in Mail flow > Email address policies select the up arrow to move
          arrow          the policy higher in the list, which increases the priority of the policy by specifying
                         which policy is applied first.
                         You can also use these arrows to navigate the public folder hierarchy and to move
                         rules up or down in the list view.

          Copy           Copy an object so you can make changes to it without changing the original
                         object.
                         For example, in Permissions > Admin roles, select a role from the list view, and
                         then select this icon to create a new role group based on an existing one.

          Remove         Remove an item from a list.
                         For example, in the Public Folder Permissions dialog box, you can remove users
                         from the list of users allowed to access the public folder by selecting the user and
                         clicking this icon.

5: List view
Tabs that contain many objects display those objects in a list view. The viewable limit in the EAC
list view is approximately 20,000 objects. Paging is included so you can skip to the results that
you want to see. In the Recipients list view, you can also configure page size and export the
data to a CSV file.

6: Details pane
When you select an object from the list view, more information about that object is displayed
in the details pane. For some object types, the details pane includes quick management tasks.
For example, if you navigate to Recipients > Mailboxes and select a mailbox from the list view,
the details pane (among other options) displays an option to enable or disable the archive for
that mailbox.

Some object types also allow bulk editing of multiple objects in the details pane. You can select
multiple objects in the list view by selecting an object and doing one of the following steps:

        Holding the Shift key, and selecting an object farther down in the list.

<!-- p.227 -->

     or

     Holding down the CTRL key as you select each object.

If bulk edit is available for the object types that you selected, you see the available options in
the details pane. For example, at Recipients > Mailboxes, when you select multiple mailboxes
of the same type, the title of the details pane changes to Bulk Edit, and you can update contact
and organization information, custom attributes, mailbox quotas, Outlook on the web settings,
and more.

7: Notifications
The EAC includes a notification viewer that displays information about the following items:

     Expiring and expired certificates.

     The status of mailbox moves and migrations (also known as Mailbox Replication Service
     tasks or MRS tasks). You can also use the notification viewer to opt in to receive email
     notifications about these tasks.

     Exporting mailbox content to .pst files.

To show or hide the notification viewer, select the icon (   ).

<!-- p.228 -->

Notifications are alerts that are sent to the arbitration mailbox named
FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042 . The EAC checks this mailbox for alerts

every 30 seconds. Notifications remain in the arbitration mailbox until they're removed by the
component that sent them, or until they expire (removed by the Managed Folder Assistant
after 30 days).

You can also use the Get-Notification cmdlet in the Exchange Management Shell to view more
details about notifications, and the Set-Notification cmdlet to request notification emails for
future alerts.

8: Me tile and Help
The Me tile allows you to sign out of the EAC and sign in as a different user by clicking on the
drop-down menu that's next to your account name.

Select the help icon ( ) to view the help content for the tab that you're currently on. If you
select on the drop-down menu that's next to the help icon, you can perform the following
actions:

      Disable Help bubble: The Help bubble displays contextual help for fields when you create
      or edit objects in the EAC. From here, you can globally turn off or turn on the Help bubble
      for all fields in the EAC.

      Performance console: The Performance console displays many counters that relate to the
      performance of the EAC.

      Copyright and Privacy: Select these links to read the copyright and privacy information
      for Exchange Server.

Supported browsers
The list of supported web browsers for accessing the EAC can be found in the Exchange Server
supportability matrix. Web browsers that aren't listed are unsupported. Please note that third-
party plug-ins may cause issues with the EAC on supported browsers.

<!-- p.229 -->

Exchange Server: Turn off access to the
Exchange admin center
Article • 05/09/2025

APPLIES TO:        2016    2019      Subscription Edition

The Exchange admin center (EAC) is the primary management interface for Exchange 2013 or
later. For more information, see Exchange admin center in Exchange Server. By default, access
to the EAC isn't restricted, and access to Outlook on the web (formally known as Outlook Web
App) on an on an Internet-facing Exchange server also gives access to the EAC. You still need
valid credentials to sign in to the EAC, but organizations may want to restrict access to the EAC
for client connections from the Internet.

  ） Important

  The procedure described in this document is no longer recommended for Exchange Server
  2019 and later. Instead, you can use Client Access Rules to block client access to the EAC.
  For more information, see Client Access Rules in Exchange Server.

The EAC virtual directory is named ECP, and is managed by the *- ECPVirtualDirectory cmdlets.
When you set the AdminEnabled parameter to the value $false on the EAC virtual directory,
you disable access to the EAC for internal and external client connections, without affecting
access to the Settings > Options page in Outlook on the web.

But, this configuration introduces a new problem: access to the EAC is completely disabled on
the server, even for administrators on the internal network. To fix this issue, you have two
choices:

      Configure a second Exchange server that's only accessible from the internal network to
      handle internal EAC connections.

<!-- p.230 -->

     On the existing Exchange server, create a new Internet Information Services (IIS) web site
     with new virtual directories for the EAC and Outlook on the web that's only accessible
     from the internal network.

     Note: You need to configure the EAC and Outlook on the web in the new web site,
     because the EAC requires the Outlook on the web authentication module from the same
     web site.

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Exchange admin center
     connectivity" entry in the Exchange infrastructure and PowerShell permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Step 1: Use the Exchange Management Shell to
disable access to the EAC
Remember, this step disables access to the EAC on the server for internal and external
connections, but still allows users to access their own Settings > Options page in Outlook on
the web.

To disable access to the EAC on an Exchange server, use the following syntax:

  PowerShell

  Set-ECPVirtualDirectory -Identity "<Server>\ecp (Default Web Site)" -AdminEnabled
  $false

This example turns disables access to the EAC on the server named MBX01.

  PowerShell

<!-- p.231 -->

  Set-ECPVirtualDirectory -Identity "MBX01\ecp (Default Web Site)" -AdminEnabled
  $false

How do you know this step worked?
To verify that you've disabled access to the EAC on the server, replace <Server> with the name
of your Exchange server, and run the following command to verify the value of the
AdminEnabled property:

  PowerShell

   Get-ECPVirtualDirectory -Identity "MBX01\ecp (Default Web Site)" | Format-List
  AdminEnabled

When you open https://<servername>/ecp or from the internal network, your own Settings >
Options page in Outlook on the web opens instead of the EAC.

Step 2: Give access to the EAC on the internal
network
Choose either of the following options.

Option 1: Configure a second Exchange server that's only
accessible from the internal network
The default value of the AdminEnabled property is True on the default EAC virtual directory.
To confirm this value on the second server, replace <Server> with the name of the server, and
run the following command:

  PowerShell

  Get-ECPVirtualDirectory -Identity "<Server>\ecp (Default Web Site)" | Format-List
  AdminEnabled

If the value is False , replace <Server> with the name of the server, and run the following
command:

  PowerShell

<!-- p.232 -->

  Set-ECPVirtualDirectory -Identity "<Server>\ecp (Default Web Site)" -AdminEnabled
  $true

Option 2: Create a new web site on the existing Exchange
server, and configure the EAC and Outlook on the web in the
new web site for the internal network
The required steps are:

   1. Add a second IP address to the Exchange server.

   2. Create a new web site in IIS that uses the second IP address, and assign file and folder
     permissions.

   3. Copy the contents of the default web sites to the new web site.

   4. Create new EAC and Outlook on the web virtual directories for the new web site.

   5. Restart IIS for the changes to take effect.

  ） Important

  When you install an Exchange Server Cumulative Update (CU), the CU won't update files in
  the new web site and virtual directories. After you apply the CU, you need to completely
  remove the new web site, virtual directories, and content in the folders and then re-create
  the new web site, virtual directories, and content in the folders.

Step 2a: Add a second IP address to the Exchange server
You can add a second network adapter and assign the IP address to the second network
adapter, or you can assign a second IP address to the existing network adapter.

The steps to assign a second IP address to the existing network adapter are described below.

   1. Open the properties of the network adapter. For example:

     a. From a Command Prompt window, the Exchange Management Shell, or the Run dialog,
     run ncpa.cpl .

     b. Right-click on the network adapter, and then choose Properties.

<!-- p.233 -->

2. In the properties of the network adapter, select Internet Protocol Version 4 (TCP/IPv4),
  and then click Properties.

3. In the Internet Protocol Version 4 (TCP/IPv4) Properties window that opens, on the
  General tab, click Advanced.

4. In the Advanced TCP/IP Settings window that opens, on the IP Settings tab, in the IP
  addresses section, click Add and enter the IP address.

  Note: If you add a second network adapter, in the Advanced TCP/IP Settings window, on
  the DNS tab, un-check Register this connection's address in DNS.

<!-- p.234 -->

Step 2b: Create a new web site in IIS that uses the second IP address,
and assign file and folder permissions

  1. Open IIS Manager on the Exchange server. An easy way to do this in Windows Server
    2012 or later is to press Windows key + Q, type inetmgr, and select Internet Information
    Services (IIS) Manager in the results.

  2. In the Connections pane, expand the server, select Sites, and in the Actions pane, click
    Add Website.

  3. In the Add Website window that appears, configure the following settings:

         Site name: EAC_Secondary

         Physical path: C:\inetpub\EAC_Secondary

         Binding

            Type: https

            IP address: Select the second IP address that you added in the previous step.

            Port: 443

<!-- p.235 -->

       SSL certificate: Choose the certificate that you want to use (for example, the default
       Exchange certificate named Microsoft Exchange).

  When you're finished, click OK.

4. Create ecp and owa folders in C:\inetpub\EAC_Secondary .

  a. In IIS Manager, select the EAC_Secondary web site, and in the Actions pane, click
  Explore.

  b. In the File Explorer window that opens, create the following folders in
  C:\inetpub\EAC_Secondary :

        ecp

        owa

<!-- p.236 -->

    When you're finished, close File Explorer.

  5. Assign Read & Execute permissions to the local security group named IIS_IUSRS on the
    C:\inetpub\EAC_Secondary folder.

    a. In IIS Manger, select the EAC_Secondary web site, and in the Actions pane, click Edit
    Permissions.

    b. In the EAC_Secondary Properties window that opens, click the Security tab, and then
    click Edit.

    c. In the Permissions for EAC_Secondary window that opens, click Add.

    d. In the Select Users, Computers, Service Accounts or Groups window that opens,
    perform the following steps:

    i. Click Locations, and in the Locations dialog box that opens, select the local server, and
    then click OK.

    ii. In the Enter the object names to select field, type IIS_IUSRS, click Check Names, and
    then click OK.

    e. Back on the Permissions for EAC_Secondary window, select IIS_IUSRS, and in the
    Allow column, select Read & Execute (which automatically selects the List Folder
    Contents and Read permissions), and then click OK twice.

Step 2c: Copy the contents of the default web sites to the new web site
    Copy all files and folders from the Default Web Site ( C:\inetpub\wwwroot ) to
    C:\inetpub\EAC_Secondary . You can skip the following files that can't be copied:

       MacCertification.asmx

       MobileDeviceCertification.asmx

       decomission.asmx

       editissuancelicense.asmx

<!-- p.237 -->

     Copy all files and folders from %ExchangeInstallPath%FrontEnd\HttpProxy\ecp to
     C:\inetpub\EAC_Secondary\ecp .

     Copy all files and folders from %ExchangeInstallPath%FrontEnd\HttpProxy\owa to
     C:\inetpub\EAC_Secondary\owa .

Step 2d: Use the Exchange Management Shell to create new EAC and
Outlook on the web virtual directories for the new web site
To learn how to open the Exchange Management Shell in your on-premises Exchange
organization, see Open the Exchange Management Shell.

Replace <Server> with the name of your server, and run the following commands to create the
new EAC and Outlook on the web virtual directories for the new web site.

  PowerShell

  New-EcpVirtualDirectory -Server <Server> -Role ClientAccess -WebSiteName
  EAC_Secondary -Path "C:\inetpub\EAC_Secondary\ecp"

  PowerShell

  New-OwaVirtualDirectory -Server <Server> -Role ClientAccess -WebSiteName
  EAC_Secondary -Path "C:\inetpub\EAC_Secondary\owa"

Step 2e: Restart IIS
   1. In IIS Manager, in the Connections pane, select the server.

   2. In the Actions pane, click Restart.

Note: To restart IIS from the command line, open an elevated command prompt (a Command
Prompt window that you opened by selecting Run as administrator) and run the following
commands:

  Console

  net stop w3svc /y

  Console

  net start w3svc

<!-- p.238 -->

How do you know this task worked?
To verify that you have successfully disabled access to the EAC on an Exchange server, perform
the following steps:

   1. Test your organization's internal and external URL for Outlook on the web. For example, if
     the external URL is https://mail.contoso.com/owa , and the internal URL is
     https://mbx01.contoso.com/owa         use the following procedures to verify your
     configuration:

           Verify that internal and external users can open their mailboxes by using Outlook on
           the web, including the Settings > Options page.

           Verify that https://mail.contoso.com/ecp     and https://mbx01.contoso.com/ecp
           return either of the following results:

              404 - website not found

              The user is redirected to their Settings > Options page in Outlook on the web.

   2. Verify that administrators can access the EAC on the internal network based on your
     configuration selection:

           Second Exchange server: If the second Exchange server is named MBX02, verify that
           https://mbx02.contoso.com/ecp        opens the EAC.

           New EAC web site on the existing Exchange server: If the IP address of the new
           EAC web site is 10.1.1.12, verify that https://10.1.1.12/ecp   opens the EAC.

<!-- p.239 -->

Autodiscover service in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

The Autodiscover service minimizes user configuration and deployment steps by providing
clients access to Exchange features. For Exchange Web Services (EWS) clients, Autodiscover is
typically used to find the EWS endpoint URL. However, Autodiscover can also provide
information to configure clients that use other protocols. Autodiscover works for client
applications that are inside or outside firewalls and in resource forest and multiple forest
scenarios.

Exchange 2016 introduced changes to services that were previously handled by the multiple
servers. The Mailbox server now provides Client Access services, so you can't configure a
standalone Client Access server like you could in previous versions of Exchange. Autodiscover
service in Exchange 2016 and Exchange 2019 is possible because:

      Exchange creates a virtual directory named autodiscover under the default web site in
      Internet Information Services (IIS).

      Active Directory stores and provides authoritative URLs for domain-joined computers.

      Client Access services on Mailbox servers provide authentication and proxy services for
      internal and external client connections.

      Outlook configures services with only the username and password.

  ７ Note

  If you are a user looking for help with connecting your Outlook client to your Exchange
  server, see Outlook email setup .

Autodiscover services and Active Directory
Exchange stores in Active Directory the configuration of Exchange servers in the organization
as well as information about your users' mailboxes. Before you install Exchange Server, you
need to prepare your Active Directory forest and its domains. If you aren't familiar with
Exchange forests or domains, see Step 3: Prepare Active Directory domains.

Exchange automatically creates at installation the virtual directory autodiscover in IIS, the
frontend Client Access services web site that clients connect to. This allows Outlook to discover

<!-- p.240 -->

the Exchange mailbox settings so that users don't have to deal with manually configuring
advanced settings.

The SCP object is also created in Active Directory at the same time as the Autodiscover service
virtual directory. The SCP stores and provides authoritative URLs of the Autodiscover service for
domain-joined computers.

You need to update the SCP object to point to the Exchange server. This is necessary because
Exchange servers provide additional Autodiscover information to clients to improve the
discovery process. You can use the Set-ClientAccessService cmdlet to update the SCP object.
For more information, see Set-ClientAccessService.

  ） Important

  You need to be assigned permissions before you can run the Set-ClientAccessService
  cmdlet. To find the permissions required to run any cmdlet or parameter in your
  organization, see Find the permissions required to run any Exchange cmdlet.

Autodiscover makes it easy to retrieve the information that you need to connect to mailboxes
on Exchange servers. SCP objects locate those Autodiscover servers or endpoints appropriate
for the user you're retrieving settings for. And SCP objects in AD DS provide an easy way for
domain-joined clients to look up Autodiscover servers.

Exchange publishes two types of SCP objects for the Autodiscover service:

     SCP pointers: Contains information that points to specific LDAP servers that should be
     used to locate Autodiscover SCP objects for the user's domain. SCP pointers are stamped
     with the following GUID: 67661d7F-8FC4-4fa7-BFAC-E1D7794C1F68.
