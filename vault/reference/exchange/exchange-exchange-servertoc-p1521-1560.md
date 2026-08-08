---
title: "Exchange Server — pages 1521-1560"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1521-1560
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1521-1560
family: exchange
documentKind: "doc"
abstract: "$false -OAuthAuthentication $false -WindowsAuthentication $false PowerShell Get-OwaVirtualDirectory | Set-OwaVirtualDirectory -AdfsAuthentication $true - BasicAuthentication $false -DigestAuthentication $false -FormsAuthentication $false -OAuthAuthentication $false -WindowsAuthe"
---

# Exchange Server — pages 1521-1560

<!-- p.1521 -->

  $false -OAuthAuthentication $false -WindowsAuthentication $false

  PowerShell

  Get-OwaVirtualDirectory | Set-OwaVirtualDirectory -AdfsAuthentication $true -
  BasicAuthentication $false -DigestAuthentication $false -FormsAuthentication
  $false -OAuthAuthentication $false -WindowsAuthentication $false

Step 8: Restart IIS on the Exchange server
  1. Open IIS Manager on the Exchange server. An easy way to do this in Windows Server
     2012 or later is to press Windows key + Q, type inetmgr, and select Internet Information
     Services (IIS) Manager in the results.

  2. In IIS Manager, select the server.

  3. In the Actions pane, click Restart.

Note: To perform this procedure on the command line, open an elevated command prompt on
the Exchange server (a Command Prompt window you open by selecting Run as administrator)
and run the following commands:

  Console

  net stop w3svc /y

  Console

<!-- p.1522 -->

  net start w3svc

How do you know this worked?
To test the AD FS claims for Outlook on the web:

   1. In a web browser, open Outlook on the web (for example,
     https://mail.contoso.com/owa ).

   2. If you get a certificate error in the web browser, just continue on to the Outlook on the
     web site. You should be redirected to the AD FS sign-in page or the AD FS prompt for
     credentials.

   3. Type your username (domain\user) and password, and then click Sign in.

   4. Outlook on the web will load in the window.

To test the AD FS claims for EAC:

   1. In a web browser, open EAC (for example, https://mail.contoso.com/ecp       ).

   2. If you get a certificate error in the web browser, just continue on to the EAC web site. You
     should be redirected to the AD FS sign-in page or the AD FS prompt for credentials.

   3. Type your username (domain\user) and password, and then click Sign in.

   4. EAC will load in the window.

Additional considerations

Multifactor authentication
Deploying and configuring AD FS for claims-based authentication allows Outlook on the web
and the EAC to support multifactor authentication, such as certificate-based authentication,
authentication or security tokens, and fingerprint authentication. Multifactor authentication
requires two of these three authentication factors:

     Something only the user knows (for example, the password, PIN, or pattern).

     Something only the user has (for example, an ATM card, security token, smart card, or
     mobile phone).

     Something only the user is (for example, a biometric characteristic, such as a fingerprint).

<!-- p.1523 -->

For example, a password and a security code that's sent to a mobile phone, or a PIN and a
fingerprint.

For details on multifactor authentication in Windows Server 2012 R2, see Overview: Manage
Risk with Additional Multi-Factor Authentication for Sensitive Applications and Walkthrough
Guide: Manage Risk with Additional Multi-Factor Authentication for Sensitive Applications.

On the AD FS server, the federation service functions as a security token service, and provides
the security tokens that are used with claims. The federation service issues tokens based on the
credentials that are presented. After the account store verifies a user's credentials, the claims
for the user are generated according to the rules of the trust policy and then added to a
security token that is issued to the client. For more information about claims, see
Understanding Claims.

Co-existence with other versions of Exchange
You can use AD FS authentication for Outlook on the web and the EAC when you have more
than one version of Exchange deployed in your organization. This scenario is supported only if
all clients are connecting through Exchange servers, and all of those servers have been
configured for AD FS authentication.

In Exchange 2016 organizations, users with mailboxes on Exchange 2010 servers can access
their mailboxes through an Exchange 2016 server that's configured for AD FS authentication.
The initial client connection to the Exchange 2016 server uses AD FS authentication. However,
the proxied connection to Exchange 2010 uses Kerberos. There's no supported way to
configure Exchange 2010 for direct AD FS authentication.

Known issues
For environments that have deployed Web Application Proxy servers on Windows Server 2019
and higher, you may find OWA/ECP login to Exchange mailboxes stuck at "Still working on it"
screen forever. The issue doesn't occur when WAP is bypassed.

Solution

   1. Run the following command to disable HTTP2:

        PowerShell

        New-ItemProperty -path
        'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp' -
        name 'EnableDefaultHttp2' -value '0' -PropertyType 'DWord' -Force | Out-Null

<!-- p.1524 -->

2. Restart the WAP server.

<!-- p.1525 -->

Client Access Rules in Exchange 2019
Article • 05/09/2025

APPLIES TO:          2016       2019    Subscription Edition

Client Access Rules help you control access to your Exchange 2019 organization in the Exchange admin center (EAC) and remote
PowerShell based on client properties or client access requests. Client Access Rules are like mail flow rules (also known as transport rules)
for EAC and remote PowerShell connections to your Exchange organization. You can prevent EAC and remote PowerShell clients from
connecting to Exchange based on their IP address (IPv4 and IPv6), authentication type, and user property values. For example:

      Prevent client access using remote PowerShell (which also includes the Exchange Management Shell).
      Block access to the EAC for users in a specific country or region.

For Client Access Rule procedures, see Procedures for Client Access Rules in Exchange Server.

Client Access Rule components
A rule is made of conditions, exceptions, an action, and a priority value.

      Conditions: Identify the client connections to apply the action to. For a complete list of conditions, see the Client Access Rule
      conditions and exceptions section later in this topic. When a client connection matches the conditions of a rule, the action is applied
      to the client connection, and rule evaluation stops (no more rules are applied to the connection).

      Exceptions: Optionally identify the client connections that the action shouldn't apply to. Exceptions override conditions and prevent
      the rule action from being applied to a connection, even if the connection matches all of the configured conditions. Rule evaluation
      continues for client connections that are allowed by the exception, but a subsequent rule could still affect the connection.

      Action: Specifies what to do to client connections that match the conditions in the rule, and don't match any of the exceptions. Valid
      actions are:

         Allow the connection (the AllowAccess value for the Action parameter).

         Block the connection (the DenyAccess value for the Action parameter).

         Note: When you block connections for a specific protocol, other applications that rely on the same protocol might also be
         affected.

      Priority: Indicates the order that the rules are applied to client connections (a lower number indicates a higher priority). The default
      priority is based on when the rule is created (older rules have a higher priority than newer rules), and higher priority rules are
      processed before lower priority rules. Remember, rule processing stops once the client connection matches the conditions in the
      rule.

      For more information about setting the priority value on rules, see Use the Exchange Management Shell to set the priority of Client
      Access Rules.

How Client Access Rules are evaluated
How multiple rules with the same condition are evaluated, and how a rule with multiple conditions, condition values, and exceptions are
evaluated are described in the following table.

                                                                                                                                         ﾉ   Expand table

 Component              Logic                  Comments

 Multiple rules that    The first rule is      For example, if your highest priority rule blocks remote PowerShell connections, and you create another
 contain the same       applied, and           rule that allows remote PowerShell connections for a specific IP address range, all remote PowerShell
 condition              subsequent rules are   connections are still blocked by the first rule. Instead of creating another rule for remote PowerShell, you
                        ignored                need to add an exception to the existing remote PowerShell rule to allow connections from the specified IP
                                               address range.

 Multiple conditions    AND                    A client connection must match all conditions in the rule. For example, EAC connections from users in the
 in one rule                                   Accounting department.

<!-- p.1526 -->

 Component              Logic              Comments

 One condition with     OR                 For conditions that allow more than one value, the connection must match any one (not all) of the specified
 multiple values in a                      conditions. For example, EAC or remote PowerShell connections.
 rule

 Multiple exceptions    OR                 If a client connection matches any one of the exceptions, the actions are not applied to the client
 in one rule                               connection. The connection doesn't have to match all the exceptions. For example, IP address 19.2.168.1.1
                                           or Basic authentication.

You can test how a specific client connection would be affected by Client Access Rules (which rules would match and therefore affect the
connection). For more information, see Use the Exchange Management Shell to test Client Access Rules.

Important notes

Client connections from your internal network
Connections from your local network aren't automatically allowed to bypass Client Access Rules. Therefore, when you create Client Access
Rules that block client connections to Exchange, you need to consider how connections from your internal network might be affected.
The preferred method to allow internal client connections to bypass Client Access Rules is to create a highest priority rule that allows
client connections from your internal network (all or specific IP addresses). That way, the client connections are always allowed, regardless
of any other blocking rules that you create in the future.

Client Access Rules and middle-tier applications
Many applications that access Exchange use a middle-tier architecture (clients talk to the middle-tier application and the middle-tier
application talks to Exchange). A Client Access Rule that only allows access from your local network might block middle-tier applications.
So, your rules need to allow the IP addresses of middle-tier applications.

Middle-tier applications owned by Microsoft (for example, Outlook for iOS and Android) will bypass blocking by Client Access Rules, and
will always be allowed. To provide additional control over these applications, you need to use the control capabilities that are available in
the applications.

Timing for rule changes
To improve overall performance, Client Access Rules use a cache, which means changes to rules don't immediately take effect. The first
rule that you create in your organization can take up to 24 hours to take effect. After that, modifying, adding, or removing rules can take
up to one hour to take effect.

Administration
You can only use the Exchange Management Shell (remote PowerShell) to manage Client Access Rules, so you need to be careful about
rules that block your access to remote PowerShell.

As a best practice, create a Client Access Rule with the highest priority to preserve your access to remote PowerShell. For example:

  PowerShell

  New-ClientAccessRule -Name "Always Allow Remote PowerShell" -Action Allow -AnyOfProtocols RemotePowerShell -Priority 1

Authentication types and protocols
Not all authentication types are supported for all protocols. The supported authentication types per protocol in Exchange Server are
described in this table:

                                                                                                                                    ﾉ   Expand table

<!-- p.1527 -->

 Protocol              AdfsAuthentication   BasicAuthentication   CertificateBasedAuthentication        NonBasicAuthentication     OAuthAuthentication

 ExchangeAdminCenter   supported            supported             n/a                                   n/a                        n/a

 RemotePowerShell      n/a                  supported             n/a                                   supported                  n/a

Client Access Rule conditions and exceptions
Conditions and exceptions in Client Access Rules identify the client connections that the rule is applied to or not applied to. For example,
if the rule blocks access by remote PowerShell clients, you can configure the rule to allow remote PowerShell connections from a specific
range of IP addresses. The syntax is the same for a condition and the corresponding exception. The only difference is conditions specify
client connections to include, while exceptions specify client connections to exclude.

This table describes the conditions and exceptions that are available in Client Access Rules:

                                                                                                                                     ﾉ   Expand table

 Condition parameter in the         Exception parameter in the Exchange     Description
 Exchange Management Shell          Management Shell

 AnyOfAuthenticationTypes           ExceptAnyOfAuthenticationTypes          Valid values in Exchange Server are:
                                                                                   For the EAC: AdfsAuthentication and BasicAuthentication
                                                                                   For remote PowerShell: BasicAuthentication and
                                                                                   NonBasicAuthentication

                                                                            You can specify multiple values separated by commas. You can use
                                                                            quotation marks around each individual value ("value1","value2"), but
                                                                            not around all values (don't use "value1,value2").

 AnyOfClientIPAddressesOrRanges     ExceptAnyOfClientIPAddressesOrRanges    IPv4 and IPv6 addresses are supported. Valid values are:
                                                                                  A single IP address: For example, 192.168.1.1 or
                                                                                   2001:DB8::2AA:FF:C0A8:640A.
                                                                                   An IP address range: For example, 192.168.0.1-192.168.0.254 or
                                                                                   2001:DB8::2AA:FF:C0A8:640A-2001:DB8::2AA:FF:C0A8:6414.
                                                                                   Classless Inter-Domain Routing (CIDR) IP: For example,
                                                                                   192.168.3.1/24 or 2001:DB8::2AA:FF:C0A8:640A/64.

                                                                            You can specify multiple values separated by commas.

                                                                            For more information about IPv6 addresses and syntax, see this
                                                                            Exchange 2013 topic: IPv6 address basics.

 AnyOfProtocols                     ExceptAnyOfProtocols                    Valid values in Exchange Server are:
                                                                                   ExchangeAdminCenter
                                                                                   RemotePowerShell

                                                                            You can specify multiple values separated by commas. You can use
                                                                            quotation marks around each individual value (" value1","value2"), but
                                                                            not around all values (don't use "value1,value2").

                                                                            Note: If you don't use this condition in a rule, the rule is applied to
                                                                            both protocols.

 Scope                              n/a                                     Specifies the type of connections that the rule applies to. Valid values
                                                                            are:
                                                                                   Users : The rule only applies to end-user connections.
                                                                                   All : The rule applies to all types of connections (end-users and
                                                                                   middle-tier apps).

 UsernameMatchesAnyOfPatterns       ExceptUsernameMatchesAnyOfPatterns      Accepts text and the wildcard character (*) to identify the user's
                                                                            account name in the format <Domain>\<UserName> (for example,
                                                                             contoso.com\jeff or *jeff* , but not jeff* ). Non-alphanumeric
                                                                            characters don't require an escape character.

                                                                            You can specify multiple values separated by commas.

 UserRecipientFilter                n/a                                     Uses OPath filter syntax to identify the user that the rule applies to. For
                                                                            example, "City -eq 'Redmond'" .

<!-- p.1528 -->

Condition parameter in the   Exception parameter in the Exchange   Description
Exchange Management Shell    Management Shell

                                                                   The filterable attributes are:

                                                                          City
                                                                          Company
                                                                          CountryOrRegion
                                                                          CustomAttribute1 to CustomAttribute15
                                                                          Department
                                                                          Office
                                                                          PostalCode
                                                                          StateOrProvince
                                                                          StreetAddress

                                                                   The search criteria uses the syntax "<Property> -<Comparison operator>
                                                                   '<Value>'" .

                                                                          <Property> is a filterable property.
                                                                          -<Comparison Operator> is an OPATH comparison operator. For
                                                                         example -eq for exact matches (wildcards are not supported)
                                                                         and -like for string comparison (which requires at least one
                                                                         wildcard in the property value). For more information about
                                                                         comparison operators, see about_Comparison_Operators.
                                                                         <Value> is the property value. Text values with or without spaces
                                                                         or values with wildcards (*) need to be enclosed in quotation
                                                                         marks (for example, '<Value>' or '*<Value>' ). Don't use
                                                                         quotation marks with the system value $null (for blank values).

                                                                   You can chain multiple search criteria together using the logical
                                                                   operators -and and -or . For example, "<Criteria1> -and <Criteria2>"
                                                                   or "(<Criteria1> -and <Criteria2>) -or <Criteria3>" . For more
                                                                   information about OPATH filter syntax, see Additional OPATH syntax
                                                                   information.

<!-- p.1529 -->

Procedures for Client Access Rules in
Exchange 2019
Article • 05/09/2025

APPLIES TO:        2016    2019      Subscription Edition

Client Access Rules allow or block Exchange admin center (EAC) or remote PowerShell
connections to your Exchange 2019 organization based on the properties of the connection.
For more information about Client Access Rules, see Client Access Rules in Exchange Server.

   Tip

  Verify that your rules work the way you expect. Be sure to thoroughly test each rule and
  the interactions between rules. For more information, see the Use the Exchange
  Management Shell to test Client Access Rules section later in this topic.

What do you need to know before you begin?
      Estimated time to complete each procedure: less than 5 minutes.

      The procedures in this topic are only available in the Exchange Management Shell. For
      more information, see Open the Exchange Management Shell or Connect to Exchange
      servers using remote PowerShell.

      Client Access Rules support IPv4 and IPv6 addresses. For more information about IPv6
      addresses and syntax, see this Exchange 2013 topic: IPv6 address basics.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mail flow" entry in Mail flow
      permissions.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at Exchange
  Server .

Use the Exchange Management Shell to view Client
Access Rules

<!-- p.1530 -->

To return a summary list of all Client Access Rules, run this command:

  PowerShell

  Get-ClientAccessRule

To return detailed information about a specific rule, use this syntax:

  PowerShell

  Get-ClientAccessRule -Identity "<RuleName>" | Format-List [<Specific properties to
  view>]

This example returns all the property values for the rule named "Block Client Connections from
192.168.1.0/24".

  PowerShell

  Get-ClientAccessRule -Identity "Block Client Connections from 192.168.1.0/24" |
  Format-List

This example returns only the specified properties for the same rule.

  PowerShell

  Get-ClientAccessRule -Identity "Block Client Connections from 192.168.1.0/24" |
  Format-List Name,Priority,Enabled,Scope,Action

For detailed syntax and parameter information, see Get-ClientAccessRule.

Use the Exchange Management Shell to create
Client Access Rules
To create Client Access Rules in the Exchange Management Shell, use this syntax:

  PowerShell

  New-ClientAccessRule -Name "<RuleName>" [-Priority <PriorityValue>] [-Enabled
  <$true | $false>] -Action <AllowAccess | DenyAccess> [<Conditions>] [<Exceptions>]

This example creates a new Client Access Rule named Block PowerShell that blocks remote
PowerShell access, except for clients in the IP address range 192.168.10.1/24.

<!-- p.1531 -->

  PowerShell

  New-ClientAccessRule -Name "Block PowerShell" -Action DenyAccess -AnyOfProtocols
  RemotePowerShell -ExceptAnyOfClientIPAddressesOrRanges 192.168.10.1/24

Notes:

     As a best practice, create a Client Access Rule with the highest priority to preserve your
     administrator access to remote PowerShell. For example: New-ClientAccessRule -Name
     "Always Allow Remote PowerShell" -Action Allow -AnyOfProtocols RemotePowerShell -

     Priority 1 .

     The rule has the default priority value, because we didn't use the Priority parameter. For
     more information, see the Use the Exchange Management Shell to set the priority of
     Client Access Rules section later in this topic.
     The rule is enabled, because we didn't use the Enabled parameter, and the default value is
     $true .

This example creates a new Client Access Rule named Restrict EAC Access that blocks access
for the Exchange admin center, except if the client is coming from an IP address in the
192.168.10.1/24 range or if the user account name contains "tanyas".

  PowerShell

  New-ClientAccessRule -Name "Restrict EAC Access" -Action DenyAccess -
  AnyOfProtocols ExchangeAdminCenter -ExceptAnyOfClientIPAddressesOrRanges
  192.168.10.1/24 -ExceptUsernameMatchesAnyOfPatterns *tanyas*

For detailed syntax and parameter information, see New-ClientAccessRule.

How do you know this worked?
To verify that you've successfully created a Client Access Rule, use any of these procedures:

     Run this command in the Exchange Management Shell to see the new rule in the list of
     rules:

         PowerShell

         Get-ClientAccessRule

     Replace <RuleName> with the name of the rule, and run this command to see the details
     of the rule:

<!-- p.1532 -->

        PowerShell

        Get-ClientAccessRule -Identity "<RuleName>" | Format-List

     See which Client Access Rules would affect a specific client connection to Exchange by
     using the Test-ClientAccessRule cmdlet. For more information, see the Use the Exchange
     Management Shell to test Client Access Rules section later in this topic.

Use the Exchange Management Shell to modify
Client Access Rules
No additional settings are available when you modify a Client Access Rule. They're the same
settings that were available when you created the rule.

To modify a Client Access Rule in the Exchange Management Shell, use this syntax:

  PowerShell

  Set-ClientAccessRule -Identity "<RuleName>" [-Name "<NewName>"] [-Priority
  <PriorityValue>] [-Enabled <$true | $false>] -Action <AllowAccess | DenyAccess>
  [<Conditions>] [<Exceptions>]

This example disables the existing Client Access Rule named Allow EAC.

  PowerShell

  Set-ClientAccessRule -Identity "Allow EAC" -Enabled $false

An important consideration when you modify Client Access Rules is modifying conditions or
exceptions that accept multiple values:

     The values that you specify will replace any existing values.
     To add or remove values without affecting other existing values, use this syntax: @{Add="
     <Value1>","<Value2>"...; Remove="<Value1>","<Value2>"...}

This example adds the IP address range 172.17.17.27/16 to the existing Client Access Rule
named Allow EAC without affecting the existing IP address values.

  PowerShell

  Set-ClientAccessRule -Identity "Allow EAC" -AnyOfClientIPAddressesOrRanges
  @{Add="172.17.17.27/16"}

<!-- p.1533 -->

For detailed syntax and parameter information, see Set-ClientAccessRule.

How do you know this worked?
To verify that you've successfully modified a Client Access Rule, use any of these procedures:

     Replace <RuleName> with the name of the rule, and run this command to see the details
     of the rule:

         PowerShell

         Get-ClientAccessRule -Identity "<RuleName>" | Format-List

     See which Client Access Rules would affect a specific client connection to Exchange by
     using the Test-ClientAccessRule cmdlet. For more information, see the Use the Exchange
     Management Shell to test Client Access Rules section later in this topic.

Use the Exchange Management Shell to set the
priority of Client Access Rules
By default, Client Access Rules are given a priority that's based on the order they were created
in (newer rules are lower priority than older rules). A lower priority number indicates a higher
priority for the rule, and rules are processed in priority order (higher priority rules are
processed before lower priority rules). No two rules can have the same priority.

The highest priority you can set on a rule is 1. The lowest value you can set depends on the
number of rules. For example, if you have five rules, you can use the priority values 1 through 5.
Changing the priority of an existing rule can have a cascading effect on other rules. For
example, if you have five rules (priorities 1 through 5), and you change the priority of a rule
from 5 to 2, the existing rule with priority 2 is changed to priority 3, the rule with priority 3 is
changed to priority 4, and the rule with priority 4 is changed to priority 5.

To set the priority of a Client Access Rule in the Exchange Management Shell, use this syntax:

  PowerShell

  Set-ClientAccessRule -Identity "<RuleName>" -Priority <Number>

This example sets the priority of the rule named Disable PowerShell to 3. All existing rules that
have a priority less than or equal to 3 are decreased by 1 (their priority numbers are increased
by 1).

<!-- p.1534 -->

  PowerShell

  Set-ClientAccessRule -Identity "Disable PowerShell" -Priority 4

Note: To set the priority of a new rule when you create it, use the Priority parameter on the
New-ClientAccessRule cmdlet.

How do you know this worked?
To verify that you've successfully set the priority of a Client Access Rule, use either of these
procedures:

     Run the this command in the Exchange Management Shell to see the list of rules and
     their Priority values:

        PowerShell

        Get-ClientAccessRule

     Replace <RuleName> with the name of the rule, and run this command:

        PowerShell

        Get-ClientAccessRule -Identity "<RuleName>" | Format-List Name,Priority

Use the Exchange Management Shell to remove
Client Access Rules
To remove Client Access Rules in the Exchange Management Shell, use this syntax:

  PowerShell

  Remove-ClientAccessRule -Identity "<RuleName>"

This example removes the Client Access Rule named Block EAC.

  PowerShell

  Remove-ClientAccessRule -Identity "Block EAC"

<!-- p.1535 -->

Note: To disable a Client Access Rule without deleting it, use the Enabled parameter with the
value $false on the Set-ClientAccessRule cmdlet.

For detailed syntax and parameter information, see Remove-ClientAccessRule.

How do you know this worked?
To verify that you've successfully removed a Client Access Rule, run this command in the
Exchange Management Shell to verify that the rule is no longer listed:

  PowerShell

  Get-ClientAccessRule

Use the Exchange Management Shell to test Client
Access Rules
To see which Client Access Rules would affect a specific client connection to Exchange, use this
syntax:

  PowerShell

  Test-ClientAccessRule -User <MailboxIdentity> -AuthenticationType
  <AuthenticationType> -Protocol <Protocol> -RemoteAddress <ClientIPAddress> -
  RemotePort <TCPPortNumber>

This example returns the Client Access Rules that would match a client connection to Exchange
that has these properties:

     Authentication type: Basic
     Protocol: ExchangeAdminCenter
     Remote address: 172.17.17.26
     Remote port: 443
     User: julia@contoso.com

  PowerShell

  Test-ClientAccessRule -User julia@contoso.com -AuthenticationType
  BasicAuthentication -Protocol ExchangeAdminCenter -RemoteAddress 172.17.17.26 -
  RemotePort 443

For detailed syntax and parameter information, see Test-ClientAccessRule.

<!-- p.1536 -->

<!-- p.1537 -->

Mail flow and the transport pipeline
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

In Exchange Server, mail flow occurs through the transport pipeline. The transport pipeline is a
collection of services, connections, components, and queues that work together to route all
messages to the categorizer in the Transport service on an Exchange Mailbox server inside the
organization.

For information about how to configure mail flow in a new Exchange 2016 or Exchange 2019
organization, see Configure mail flow and client access.

Understanding the transport pipeline
The transport pipeline consists of the following services:

      Front End Transport service on Mailbox servers: This service acts as a stateless proxy for
      all inbound and (optionally) outbound external SMTP traffic for the Exchange Server
      organization. The Front End Transport service doesn't inspect message content, doesn't
      communicate with the Mailbox Transport service, and doesn't queue any messages
      locally.

      Transport service on Mailbox servers: This service is virtually identical to the Hub
      Transport server role in Exchange Server 2010. The Transport service handles all SMTP
      mail flow for the organization, performs message categorization, and performs message
      content inspection. Unlike Exchange 2010, the Transport service never communicates
      directly with mailbox databases. That task is now handled by the Mailbox Transport
      service. The Transport service routes messages among the Mailbox Transport service, the
      Transport service, the Front End Transport service, and (depending on your configuration)
      the Transport service on Edge Transport servers. The Transport service on Mailbox servers
      is described in more detail later in this topic.

      Mailbox Transport service on Mailbox servers: This service consists of two separate
      services:

         Mailbox Transport Submission service: This service connects to the local mailbox
         database using an Exchange remote procedure call (RPC) to retrieve messages. The
         service submits the messages over SMTP to the Transport service on the local Mailbox
         server or on other Mailbox servers. The Mailbox Transport Submission service has
         access to the same routing topology information as the Transport service.

<!-- p.1538 -->

        Mailbox Transport Delivery service: This service receives SMTP messages from the
        Transport service on the local Mailbox server or on other Mailbox servers and connects
        to the local mailbox database using RPC to deliver the messages.

     The Mailbox Transport service doesn't communicate with the Front End Transport service,
     the Mailbox Transport service, or mailbox databases on other Mailbox servers. It also
     doesn't queue any messages locally.

     Transport service on Edge Transport servers: This service is very similar to the Transport
     service on Mailbox servers. If you have an Edge Transport server installed in the perimeter
     network, all mail coming from the Internet or going to the Internet flows through the
     Transport service Edge Transport server. This service is described in more detail later in
     this topic.

The following diagram shows the relationships among the components in the Exchange
transport pipeline.

  ７ Note

  Although the diagrams in this topic show the components on a single Exchange server,
  communication also occurs between those components on different Exchange servers.
  The only communication that always occurs on the local Exchange server is between the
  Mailbox Transport service and the local mailbox database.

<!-- p.1539 -->

How messages from external senders enter the transport
pipeline

<!-- p.1540 -->

The way messages from outside the Exchange organization enter the transport pipeline
depends on whether you have a subscribed Edge Transport server deployed in your perimeter
network.

Inbound mail flow (no Edge Transport servers)
The following diagram and list describe inbound mail flow with only Exchange Mailbox servers.

   1. A message from outside the organization enters the transport pipeline through the
     default Receive connector named "Default Frontend <Mailbox server name>" in the Front
     End Transport service.

   2. The message is sent to the Transport service on the local Mailbox server or on a different
     Mailbox server. The Transport service listens for messages on the default Receive
     connector named "Default <Mailbox server name>".

<!-- p.1541 -->

   3. The message is sent from the Transport service to the Mailbox Transport Delivery service
     on the local Mailbox server or on a different Mailbox server.

   4. The Mailbox Transport Delivery service uses RPC to deliver the message to the local
     mailbox database.

Inbound mail flow with Edge Transport servers

The following diagram and list describe inbound mail flow with an Edge Transport server
installed in the perimeter network

   1. A message from outside the Exchange organization enters the transport pipeline through
     the default Receive connector named "Default internal Receive connector <Edge Transport
     server name>" in the Transport service on the Edge Transport server.

<!-- p.1542 -->

   2. In the Transport service on the Edge Transport server, the default Send connector named
     "EdgeSync - Inbound to <Active Directory site name>" sends the message to a Mailbox
     server in the subscribed Active Directory site.

   3. In the Front End Transport service on the Mailbox server, the default Receive connector
     named "Default Frontend <Mailbox server name>" accepts the message.

   4. The message is sent from the Front End Transport service to the Transport service on the
     local Mailbox server or on a different Mailbox server. The Transport service listens for
     messages on the default Receive connector named "Default <Mailbox server name>".

   5. The message is sent from the Transport service to the Mailbox Transport Delivery service
     on the local Mailbox server, or on a different Mailbox server.

   6. The Mailbox Transport Delivery service uses RPC to deliver the message to the local
     mailbox database.

How messages from internal senders enter the transport
pipeline
SMTP messages from inside the organization enter the transport pipeline through the
Transport service on a Mailbox server in one of the following ways:

     Through a Receive connector.
     From the Pickup directory or the Replay directory.
     From the Mailbox Transport Submission service.
     Through agent submission.

The message is routed based on the routing destination or delivery group.

Outbound mail flow (no Edge Transport servers)

By default, in a new Exchange Server organization, there's no Send connector that's configured
to send messages to the Internet. You need to create the Send connector yourself. After you do
that, Outbound mail flow occurs as described in the following diagram and list.

<!-- p.1543 -->

1. The Mailbox Transport Submission service uses RPC to retrieve the outbound message
  from the local mailbox database.

2. The Mailbox Transport Submission service uses SMTP to send the message to the
  Transport service on the local Mailbox server or on a different Mailbox server.

3. In the Transport service, the default Receive connector named "Default <Mailbox server
  name>" accepts the message.

4. What happens next depends on the configuration of the Send connector:

       Default: The Transport service uses the Send connector you created to send the
       message to the Internet.

<!-- p.1544 -->

           Outbound proxy: The Transport service uses the Send connector you created to
           send the message to the Front End Transport service on the local Mailbox server or
           on a remote Mailbox server. In the Front End Transport service, the default Receive
           connector named "Outbound Proxy Frontend <Mailbox server name>" accepts the
           message. The Front End Transport services sends the message to the Internet.

Outbound mail flow with Edge Transport servers
If you have an Edge Transport server installed in the perimeter network, outbound mail never
flows through the Front End Transport service. Outbound mail flow with an Edge Transport
server is described in the following diagram and list.

   1. The Mailbox Transport Submission service uses RPC to retrieve the outbound message
     from the local mailbox database.

   2. The Mailbox Transport Submission service uses SMTP to send the message to the
     Transport service on the local Mailbox server or on a different Mailbox server.

<!-- p.1545 -->

   3. In the Transport service on a Mailbox server in the subscribed Active Directory site, the
     default Receive connector named "Default <Mailbox server name>" accepts the message.

   4. The message is sent to the Edge Transport server using the implicit and invisible intra-
     organization Send connector that automatically sends mail between Exchange servers in
     the same organization.

   5. In the Transport service on the Edge Transport server, the default Receive connector
     named "Default internal Receive connector <Edge Transport server name>" accepts the
     message.

   6. In the Transport service on the Edge Transport server, the default Send connector named
     "EdgeSync - <Active Directory site name> to Internet" sends the message to the Internet.

Understanding the Transport service on Mailbox
servers
Every message that's sent or received in an Exchange Server organization must be categorized
in the Transport service on a Mailbox server before it can be routed and delivered. After a
message has been categorized, it's put in a delivery queue for delivery to the destination
mailbox database, the destination database availability group (DAG), Active Directory site or
Active Directory forest, or to the destination domain outside the organization.

The Transport service on a Mailbox server consists of the following components and processes:

     SMTP Receive: When messages are received by the Transport service, message content
     inspection is performed and antispam inspection is performed if is enabled. The SMTP
     session has a series of events that work together in a specific order to validate the
     contents of a message before it's accepted. After a message has passed completely
     through SMTP Receive and isn't rejected by receive events, or by an antispam agent, it's
     put in the Submission queue.

     Submission: Submission is the process of putting messages into the Submission queue.
     The categorizer picks up one message at a time for categorization. Submission happens
     in three ways:
        From SMTP Receive through a Receive connector.
        Through the Pickup directory or the Replay directory. These directories exist on
        Mailbox servers and Edge Transport servers. Correctly formatted message files that are
        copied into the Pickup directory or the Replay directory are put directly into the
        Submission queue.
        Through a transport agent.

<!-- p.1546 -->

     Categorizer: The categorizer picks up one message at a time from the Submission queue.
     The categorizer completes the following steps:

        Recipient resolution, which includes top-level addressing, distribution group
        expansion, and message bifurcation.

        Routing resolution.

        Content conversion.

        Additionally, mail flow rules that the organization defined are applied. After messages
        have been categorized, they're put into a delivery queue that's based on the
        destination of the message. Messages are queued by the destination mailbox
        database, DAG, Active Directory site, Active Directory forest, or external domain.

     SMTP Send: How messages are routed from the Transport service depends on the
     location of the message recipients relative to the Mailbox server where categorization
     occurred. The message could be routed to one of the following locations:
        To the Mailbox Transport Delivery service on the same Mailbox server.
        To the Mailbox Transport Delivery service on a different Mailbox server that's part of
        the same DAG.
        To the Transport service on a Mailbox server in a different DAG, Active Directory site, or
        Active Directory forest.
        For delivery to the Internet through:
           A Send connector on the same Mailbox server.
           The Transport service on a different Mailbox server.
           The Front End Transport service on the same Mailbox server or a different Mailbox
           server (if outbound proxy is configured).
           The Transport service on an Edge Transport server in the perimeter network.

Understanding the Transport service on Edge
Transport servers
The components of the Transport service on Edge Transport servers are identical to the
components of the Transport service on Mailbox servers. However, what actually happens
during each stage of processing on Edge Transport servers is different. The differences are
described in the following list.

     SMTP Receive: When an Edge Transport server is subscribed to an internal Active
     Directory site, the default Receive connector named "Default <Edge Transport server
     name>" is automatically configured to accept mail from internal Mailbox servers and
     from the Internet. When Internet messages arrive at the Edge Transport server, antispam

<!-- p.1547 -->

agents filter connections and message contents and help identify the sender and the
recipient while the message is being accepted into the organization. The antispam agents
are installed and enabled by default. Additional attachment filtering and connection
filtering features are available, but built-in malware filtering is not. Also, mail flow rules
(also known as transport rules) are controlled by the Edge Rule agent. Compared to the
Transport Rule agent on Mailbox servers, only a small subset of mail flow rule conditions
are available on Edge Transport servers. But, there are unique mail flow rule actions
related to SMTP connections that are available only on Edge Transport servers.

Submission: On an Edge Transport server, messages typically enter the Submission queue
through a Receive connector. However, the Pickup directory and the Replay directory are
also available.

Categorizer: On an Edge Transport server, categorization is a short process in which the
message is put directly into a delivery queue for delivery to internal or external recipients.

SMTP Send: When an Edge Transport server is subscribed to an internal Active Directory
site, two Send connectors are automatically created and configured. One named
"EdgeSync - <Active Directory site name> to Internet" is responsible for sending
outbound mail to Internet recipients; the other named "EdgeSync - Inbound to <Active
Directory site name>" is responsible for sending inbound mail from the Internet to
internal recipients. Inbound mail is sent to the Front End Transport service on an available
Mailbox server in the subscribed Active Directory site.

<!-- p.1548 -->

Regular expressions that are used in
transport rules
Article • 05/09/2025

APPLIES TO:        2016     2019      Subscription Edition

You can use regular expressions in Microsoft Exchange Servers 2016 and 2019 transport rule
predicates to match text patterns in different parts of a message (such as message headers,
sender, recipients, message subject, and body). Predicates are used by conditions and
exceptions to determine whether a configured action should be applied to an e-mail message.

  ７ Note

  Due to the variances in customer environments, Microsoft Customer Support Services
  (CSS) can't participate in the development or testing of custom Regular Expression scripts
  ("RegEx scripts"). For RegEX custom script development, testing, and debugging, Office
  365 customers will need to rely upon internal IT resources. Alternatively, Office 365
  customers may choose to use an external consulting resource such as Microsoft
  Consulting Services (MCS). Regardless of the script development resource, CSS EXO and
  EOP support engineers aren't available to assist customers with custom RegEx script
  inquiries.

Looking for management tasks related to transport rules? See Managing Transport Rules.

Contents
This article contains the following sections:

      Regular expressions that are used in transport rules
         Contents
            Simple expressions vs regular expressions
            Regular expressions in Exchange Servers 2016 and 2019
               Constructing regular expressions
            Creating a transport rule that uses a regular expression

Simple expressions vs regular expressions
To understand regular expressions, you must first understand simple expressions. A simple
expression is a specific value that you want to match exactly in a message. Predicates using
simple expressions match specific words or strings. An example of a simple expression is the

<!-- p.1549 -->

title of a document that your organization doesn't want to be distributed outside the
organization, such as Yearly Sales Forecast.doc. A piece of data in an email message must
exactly match a simple expression to satisfy a condition or exception in transport rules.

A regular expression is a concise and flexible notation for finding patterns of text in a message.
The notation consists of two basic character types:

     Literal characters: Text that must exist in the target string. These characters are normal
     characters, as typed.
     Metacharacters: One or more special characters that aren't interpreted literally. These
     characters indicate how the text can vary in the target string.

You can use regular expressions to quickly parse email messages to find specific text patterns.
These expressions enable you to detect messages with specific types of content, such as social
security numbers (SSNs), patent numbers, and phone numbers.

You can't reasonably match this data with a simple expression because a simple expression
requires that you enter every possible variation of the value that you want to detect. In many
cases, using simple expressions for such applications becomes a logistical challenge, and
matching a large number of simple expressions in message content can be resource intensive.
Using regular expressions is more efficient. Instead of specifying all possible variations, you can
configure the transport rule predicate to search for a text pattern.

Regular expressions in Exchange Servers 2016 and 2019
In the Exchange Management Shell, you can use regular expressions in any predicate that
accepts the Patterns predicate property. In the Exchange Management Console, you can use
regular expressions with any condition or exception that contains the words with text patterns.
For more information about predicates, see Transport Rule Predicates.

  ２ Warning

  You must carefully test the regular expressions that you construct to ensure that they yield
  the expected results. An incorrectly configured regular expression could yield unexpected
  matches and cause unwanted transport rule behavior. These implications may result in
  undesirable actions being taken on messages and message content, potentially resulting
  in data loss when actions such as rejecting or bouncing a message are used. Also, complex
  regular expressions may affect email transport performance. Test your regular expressions
  in a test environment before you implement them in production.

The following table lists the pattern strings that you can use to create a pattern-matching
regular expression in Exchange Servers 2016 and 2019:

<!-- p.1550 -->

                                                                                                ﾉ    Expand table

 Pattern      Description
 String

 \S           The \S pattern string matches any single character that's not a space.

 \s           The \s pattern string matches any single white-space character.

 \D           The \D pattern string matches any non-numeric digit.

 \d           The \d pattern string matches any single numeric digit.

 \w           The \w pattern string matches any single Unicode character categorized as a letter or a
              decimal digit.

 \W           The \W pattern string matches any single Unicode character not categorized as a letter or a
              decimal digit.

 *            The asterisk ( * ) character matches zero or more instances of the previous character. For
              example, ab*c matches the following strings: ac, abc, and abbbbc.

 ()           Parentheses act as grouping delimiters. For example, a(bc)* matches the following strings: a,
              abc, abcbc, abcbcbc, and so on.

 \            A backslash is used as an escaping character before a special character. Special characters are
              characters used in pattern strings: Backslash ( \ ); Pipe; Asterisk ( * ); Opening parenthesis ( ( );
              Closing parenthesis ( ) ); Caret ( ^ ); Dollar sign ( $ ). For example, if you want to match a
              string that contains (525), you would type (525).

 ^            The caret ( ^ ) character indicates that the pattern string that follows the caret must exist at
              the start of the text string being matched. For example, ^fred@contoso matches
              fred@contoso.com and fred@contoso.co.uk but not alfred@contoso.com.

 $            The dollar-sign $ character indicates that the preceding pattern string must exist at the end
              of the text string being matched. For example, contoso.com$ matches adam@contoso.com
              and kim@research.contoso.com, but doesn't match kim@contoso.com.au.

Constructing regular expressions

By using the preceding table, you can construct a regular expression that matches the pattern
of the data that you want to match. Working from left to right, examine each character or
group of characters in the data that you want to match. Read the description of each pattern
string to determine how it's applied to the data that you're matching. Then, determine which
pattern string in the table represents that character or group of characters, and add that
pattern string to the regular expression. When finished, you have a fully constructed regular
expression.

<!-- p.1551 -->

This example of a regular expression matches North American telephone numbers in the
formats 425 555-0100 and 425.555.0100.

  PowerShell

      425(\s|.)\d\d\d(-|.)\d\d\d\d

You can expand on this example by adding the telephone format (425) 555-0100, which uses
parentheses around the area code. This example of a regular expression matches all three
telephone number formats.

\d\d\d((\s|.|-|)|)\s)\d\d\d(\s|.|-)\d\d\d\d

You can analyze the previous example as follows:

      \d\d\d: This portion requires that exactly three numeric digits appear first.
      ((\s|.|-|)|)\s): This portion requires that a space, a period, or a hyphen exists after the
      three-digit number. Each character-matching string is contained in the grouping
      delimiters and is separated by the pipe character. This separation means that only one of
      the specified characters inside the grouping delimiters can exist in this location in the
      string being matched. For the separation between area code and the next three digits, it
      also looks for a closed parenthesis, or closed parenthesis and space.
      \d\d\d: This portion requires that exactly three numeric digits appear next.
      (\s|.|-): This portion requires that a space, a period, or a hyphen exists after the three-digit
      number.
      \d\d\d\d: This portion requires that exactly four numeric digits appear next.

The above regular expression will match the following sample values:

      (425)555.0100
      425 555 0100
      425 555 0100
      (425) 555-0100
      425-555-0100
      (425) 555-0100

Creating a transport rule that uses a regular expression
This example creates a transport rule in the PowerShell that uses regular expressions to match
SSNs in the subject of an email message.

  PowerShell

<!-- p.1552 -->

     New-TransportRule -Name "Social Security Number Block Rule" -
  SubjectOrBodyMatchesPatterns '\d\d\d-\d\d-\d\d\d\d' -
  RejectMessageEnhancedStatusCode "5.7.1" -RejectMessageReasonText "This message has
  been rejected because of content restrictions"

This example lets you view the new transport rule.

  PowerShell

     Get-TransportRule "Social Security Number Block Rule" | Format-List

<!-- p.1553 -->

Accepted domains in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Accepted domains are the SMTP name spaces (also known as address spaces) that you
configure in an Exchange organization to receive email messages. For example, if your
company registered the domain contoso.com, and you configured a mail exchanger (MX)
record in your Internet DNS for contoso.com, you need to configure contoso.com as an
accepted domain in your Exchange organization to accept messages that are addressed to
@contoso.com recipients.

Accepted domains in Exchange 2016 and Exchange 2019 are basically unchanged from
Exchange Server 2010, and consist of the following types:

      Authoritative domains: Recipients (in particular, mailboxes) are configured with email
      addresses in these domains. The Exchange organization accepts messages that are
      addressed to recipients in these domains, and is responsible for generating non-delivery
      reports (also known as NDRs or bounce messages) for non-existent recipients.

      Relay domains: The Exchange organization accepts messages that are addressed to
      recipients in relay domains, but isn't responsible for generating NDRs for non-existent
      recipients. Instead, Exchange (with additional configuration) relays the messages to
      messaging servers that are external to the Exchange organization. Relay domains can be
      internal (for domains that you control) or external (for domains that you don't control).

An accepted domain can be a single domain (contoso.com) or a domain with subdomains
(*.contoso.com). Accepted domains are a global setting for the Exchange organization, and you
can have multiple accepted domains of the same or different types.

To configure accepted domains, see Procedures for accepted domains in Exchange Server.

  ７ Note

  If you have a subscribed Edge Transport server in your perimeter network, you configure
  accepted domains on a Mailbox server in your Exchange organization. The accepted
  domains configuration is replicated to the Edge Transport server during EdgeSync
  synchronization. For more information, see Edge Subscriptions.

Authoritative domains

<!-- p.1554 -->

You configure an accepted domain as an authoritative domain when all recipients in that
domain exist in your Exchange organization.

By default, when you install the first Exchange Mailbox server, the fully qualified domain name
(FQDN) of your forest root domain in Active Directory is configured as an authoritative domain.
If you don't want to use this domain for email, you need to add another authoritative domain.
For instructions, see Create accepted domains.

An organization can be configured with multiple authoritative domains. The set of email
domains for an organization are the authoritative domains. You can use authoritative domains
in email address policies, and Exchange is responsible for generating NDRs for non-existent
recipients in authoritative domains.

Relay domains
You configure an accepted domain as a relay domain (also known as non-authoritative domain)
when some or none of the recipients in that domain exist in your Exchange organization (for
example, partners or subsidiaries). Exchange isn't responsible for generating NDRs for non-
existent recipients in a relay domain. Instead, you configure a Send connector with the address
space of the relay domain, and you configure this Send connector to use smart host routing to
relay messages to their destination (directly or to the next hop). For more information about
creating Send connectors that use smart host routing, see Create a Send connector to route
outbound mail through a smart host.

You configure a relay domain as an internal relay domain or as an external relay domain. The
differences are described in the following list:

     Internal relay domains

        Some of the recipients in the internal relay domain don't exist in the Exchange
        organization. For example:

           You share the domain between the Exchange organization and a third-party
           messaging system.

           You share the domain between Exchange organizations in different Active Directory
           forests.

        Recipients in the internal relay domain can be represented as mail contacts or mail
        users in the Exchange organization (manually created or automatically created by
        using directory synchronization).

        The Send connector that you configure for the internal relay domain is sourced on an
        internal Mailbox server.

<!-- p.1555 -->

          Note: By default, you can't configure a Send connector for an internal relay domain on
          a subscribed Edge Transport server. Messages sent to recipients in the internal relay
          domain are automatically forwarded to internal Mailbox servers in the subscribed
          Active Directory site by using the default "EdgeSync - Inbound to <Active Directory site
          name>" Send connector. This Send connector is automatically configured to route mail
          for all authoritative domains and internal relay domains (the address space value is -
          - ). For more information, see Send connectors created automatically by the Edge

          Subscription.

          You can use internal relay domains in email address policies.

     External relay domains

          None of the recipients in the external relay domain exist in the Exchange organization
          (including mail contacts or mail users). For example, your Exchange organization is the
          central location for accepting Internet email for a group of separate organizations.

          The Send connector that you configure for the external relay domain is sourced on an
          Edge Transport server or Internet-facing Mailbox server.

          You can't use external relay domains in email address policies.

Accepted domains and email address policies
Email address policies assign email addresses to recipients. You need to add an authoritative
domain or an internal relay domain before you can use that domain in an email address policy.
For more information about email address policies, see Email address policies in Exchange
Server.

Recipient Lookup in accepted domains
Recipient filtering on a subscribed Edge Transport server can block messages that are
addressed to non-existent recipients in your Exchange organization. This feature is known as
Recipient Lookup. For more information about recipient filtering, see Recipient filtering on Edge
Transport servers.

You can enable or disable Recipient Lookup for an accepted domain by using the
AddressBookEnabled parameter on the Set-AcceptedDomain cmdlet. The default value for each
accepted domain type is described in the following table:

                                                                                 ﾉ   Expand table

<!-- p.1556 -->

 Accepted         Default Recipient Lookup          Comments
 domain type      (AddressBookEnabled
                  parameter) value

 Authoritative    Enabled ( $true )                 All recipients in an authoritative domain exist in
 domain                                             the Exchange organization, so Recipient Lookup
                                                    for the domain is enabled by default.

 Internal relay   Disabled ( $false )               If all recipients in the internal relay domain exist in
 domain                                             the Exchange organization (including mail
                                                    contacts and mail users), you can enable Recipient
                                                    Lookup for the domain.
                                                    If some or none of the recipients in the internal
                                                    relay domain exist in the Exchange organization,
                                                    you shouldn't enable Recipient Lookup for the
                                                    domain.

 External relay   Disabled ( $false )               No recipients in the authoritative domain exist in
 domain                                             the Exchange organization, so you shouldn't
                                                    enable Recipient Lookup for the domain.

For configuration instructions, see Modify accepted domains.

Default domain
Because the forest root FQDN is automatically configured as the first accepted domain in your
organization, that accepted domain is also configured as the default domain. However, after
you add additional accepted domains, you can configure one of them as the default domain.
Here's some information about the default domain:

      You can't delete the default domain. You need to configure another accepted domain as
      the default domain (one accepted domain is always configured as the default domain).

      The default domain is used in the external postmaster address: postmaster@<default
      domain> .

      The default domain is used in encapsulated non-SMTP email addresses (Internet Mail
      Connector Encapsulated Address or IMCEA encapsulation).

      The first default domain is used as the primary address for all recipients in the default
      email address policy. If you configure another accepted domain as the default domain,
      the default email address policy isn't automatically updated.

      Although you can configure any accepted domain as the default domain, you typically
      specify an authoritative domain.

<!-- p.1557 -->

Procedures for accepted domains in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

Accepted domains are the SMTP name spaces (also known as address spaces) that you
configure in an Exchange organization to receive email messages. You use the Exchange admin
center (EAC) or the Exchange Management Shell to configure accepted domains in Exchange
Server.

For more information about accepted domains, see Accepted domains in Exchange Server. The
types of accepted domains are summarized in the following list:

      Authoritative domains

          All recipients in the authoritative domain exist in the Exchange organization.

          Exchange is responsible for generating non-delivery reports (also known as NDRs or
          bounce messages) for non-existent recipients in an authoritative domain.

      Internal relay domains

          Some recipients in the internal relay domain might exist in the Exchange organization.

          Exchange isn't responsible for generating NDRs for non-existent recipients in an
          internal relay domain. Instead, you create a Send connector with the address space of
          the internal relay domain. You source this Send connector on an internal Mailbox
          server to relay messages for the non-existent recipients in the domain.

      External relay domains

          None of the recipients in the external relay domain exist in the Exchange organization.

          Exchange isn't responsible for generating NDRs for non-existent recipients in an
          external relay domain. Instead, you create a Send connector with the address space of
          the external relay domain. You source this Send connector on an Edge Transport server
          or Internet-facing Mailbox server to relay messages for all the recipients in the domain.

What do you need to know before you begin?
      Estimated time to complete each task: 5 minutes.

<!-- p.1558 -->

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Accepted domains" entry in the
     Mail flow permissions topic and the "Email address policies" entry in the Recipients
     Permissions topic.

     If you have a subscribed Edge Transport server in your perimeter network, you configure
     accepted domains on a Mailbox server in your Exchange organization. The accepted
     domains configuration is replicated to the Edge Transport server during EdgeSync
     synchronization. For more information, see Edge Subscriptions.

     If Exchange accepts mail for recipients in an accepted domain from the Internet, you need
     to configure an MX record for the domain in your Internet-facing (public) DNS servers.
     Each MX record should resolve to the Internet-facing server that receives email for your
     organization.

     You need to create a Send connector to route mail for non-existent recipients in internal
     or external relay domains. For more information, see Create a Send connector to route
     outbound mail through a smart host.

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online     , or Exchange Online Protection .

Create accepted domains
After you create an accepted domain, you can't change the domain value (for example, from
contoso.com to *.contoso.com, or vice-versa).

Use the EAC to create accepted domains
   1. In the EAC, go to Mail flow > Accepted domains, and then click Add (    ).

   2. In the New accepted domain window that opens, configure the following settings:

          Name: Enter a unique, descriptive name.

<!-- p.1559 -->

           Accepted domain: Enter a single domain (for example, contoso.com) or a domain
           with subdomains (for example, *.contoso.com).

           This domain is: Select Authoritative, Internal Relay, or External Relay.

     When you're finished, click Save.

Use the Exchange Management Shell to create accepted
domains
To create an accepted domain, use the following syntax:

  PowerShell

  New-AcceptedDomain -Name <Name> -DomainName <DomainOrDomainWithSubdomains> -
  DomainType <Authoritative | InternalRelay | ExternalRelay>

This example creates a new authoritative domain named Contoso Corp for contoso.com.

  PowerShell

  New-AcceptedDomain -Name "Contoso Corp" -DomainName contoso.com

Note: We didn't need to use the DomainType parameter, because the default value is
Authoritative .

For detailed syntax and parameter information, see New-AcceptedDomain.

How do you know this worked?
To verify that you've successfully created an accepted domain, use either of the following
procedures:

     In the EAC, go to Mail flow > Accepted domains, verify that the accepted domain is
     listed, and the details are correct.

     In the Exchange Management Shell, run the following command to verify the property
     values:

        PowerShell

        Get-AcceptedDomain | Format-Table -Auto
        Name,DomainName,DomainType,Default,AddressBookEnabled

<!-- p.1560 -->

Modify accepted domains
     You can only replace the default domain with a new default domain (one accepted
     domain is always configured as the default domain). For more information about the
     default domain, see Default domain.

     You can enable and disable Recipient Lookup for an accepted domain only in the
     Exchange Management Shell. For more information, see Recipient Lookup in accepted
     domains.

Use the EAC to modify accepted domains
  1. In the EAC, go to Mail flow > Accepted domains, select the accepted domain from the
     list, and then click Edit (   ).

  2. In the properties window that opens, you can configure the following settings:

           Name

           This domain is: Authoritative, Internal Relay, or External Relay.

           Make this the default domain: If the check box is cleared, select it to configure the
           accepted domain as the default domain.

     When you're finished, click Save.

Use the Exchange Management Shell to modify accepted
domains
To modify an accepted domain, use the following syntax:

  PowerShell

  Set-AcceptedDomain -Identity <AcceptedDomainIdentity> [-Name <Name>] [-DomainType
  <Authoritative | InternalRelay | ExternalRelay>] [-AddressBookEnabled <$true |
  $false>] [-MakeDefault $true]

This example configures the authoritative domain named Contoso Corp as the default domain.

  PowerShell

  Set-AcceptedDomain -Identity "Contoso Corp" -MakeDefault $true
