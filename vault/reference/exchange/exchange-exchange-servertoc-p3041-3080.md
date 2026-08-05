---
title: "Exchange Server — pages 3041-3080"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p3041-3080
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p3041-3080
family: exchange
documentKind: "doc"
abstract: "To configure an existing IP allowlist provider, use the following syntax: PowerShell Set-IPAllowListProvider <IPAllowListProviderIdentity> -Name \"<Descriptive Name>\" - LookupDomain <FQDN> [-Priority <Integer>] [-AnyMatch <$true | $false>] [- BitmaskMatch <IPAddress>] [-IPAddress"
---

# Exchange Server — pages 3041-3080

<!-- p.3041 -->

To configure an existing IP allowlist provider, use the following syntax:

  PowerShell

  Set-IPAllowListProvider <IPAllowListProviderIdentity> -Name "<Descriptive Name>" -
  LookupDomain <FQDN> [-Priority <Integer>] [-AnyMatch <$true | $false>] [-
  BitmaskMatch <IPAddress>] [-IPAddressesMatch
  <IPAddressStatusCode1,IPAddressStatusCode2...>]

For example, to add the IP address status code 127.0.0.1 to the list of existing status codes for
the provider named Contoso IP allowlist Provider, run the following command:

  PowerShell

  Set-IPAllowListProvider "Contoso IP allowlist Provider" -IPAddressesMatch
  @{Add="127.0.0.1"}

For more information, see Set-IPAllowListProvider.

How do you know this worked?

To verify that you successfully configured an IP allowlist provider, run the following command.
Be sure to replace <IPAllowListProviderIdentity> with the name of the IP allowlist provider.

  PowerShell

  Get-IPAllowListProvider <IPAllowListProviderIdentity> | Format-List

Use the Exchange Management Shell to test an IP allowlist
provider
To test an IP allowlist provider, use the following syntax:

  PowerShell

  Test-IPAllowListProvider <IPAllowListProviderIdentity> -IPAddress
  <IPAddressToTest>

This example tests the provider named Contoso IP allowlist Provider by looking up the IP
address 192.168.1.1.

  PowerShell

<!-- p.3042 -->

  Test-IPAllowListProvider "Contoso IP allowlist Provider" -IPAddress 192.168.1.1

For more information, see Test-IPAllowListProvider.

Use the Exchange Management Shell to remove an IP allowlist
provider
To remove an IP allowlist provider, use the following syntax:

  PowerShell

  Remove-IPAllowListProvider <IPAllowListProviderIdentity>

This example removes the IP allowlist provider named Contoso IP allowlist Provider.

  PowerShell

  Remove-IPAllowListProvider "Contoso IP allowlist Provider"

For more information, see Remove-IPAllowListProvider.

How do you know this worked?

To verify that you successfully removed an IP allowlist provider, run the following command
and verify that the IP allowlist provider you removed is gone.

  PowerShell

  Get-IPAllowListProvider

<!-- p.3043 -->

Recipient filtering on Edge Transport
servers in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016      2019       Subscription Edition

Recipient filtering is an antispam feature in Exchange Server that relies on the RCPT TO SMTP
header to determine what action, if any, to take on an inbound message. Recipient filtering is
performed by the Recipient Filter agent, and is basically unchanged from Exchange Server
2010.

The Recipient Filter agent blocks messages according to the characteristics of the intended
recipient in the organization. The Recipient Filter agent can help you prevent the acceptance of
messages in the following scenarios:

        Nonexistent recipients: You can prevent delivery to recipients that aren't in the
        organization's address book. For example, you may want to stop delivery to frequently
        misused account names, such as administrator@contoso.com or support@contoso.com.

        Restricted distribution groups: You can prevent delivery of Internet mail to distribution
        groups that should be used only by internal users.

        Mailboxes that should never receive messages from the Internet: You can prevent
        delivery of Internet mail to a specific mailbox or alias that's typically used inside the
        organization, such as Helpdesk.

The Recipient Filter agent acts on recipients from one or both of the following data sources:

        Recipient Block list: An administrator-defined list of recipients who should never receive
        messages from the Internet.

        Recipient Lookup: Queries Active Directory to verify that the recipient exists in the
        organization. On an Edge Transport server, Recipient Lookup requires access to Active
        Directory information that's provided by EdgeSync to the local instance of Active
        Directory Lightweight Directory Services (AD LDS). For more information, see Edge
        Subscriptions.

When you enable the Recipient Filter agent, one of the following actions is taken on inbound
messages according to the characteristics of the recipients. These recipients are indicated by
the RCPT TO header.

        If the inbound message contains a recipient that is on the Recipient Block list, the
        Exchange server sends a 550 5.1.1 User unknown SMTP session error to the sending

<!-- p.3044 -->

     server.

     If the inbound message contains a recipient that doesn't match any recipients in Recipient
     Lookup, the Exchange server sends a 550 5.1.1 User unknown SMTP session error to the
     sending server.

     If the recipient isn't on the Recipient Block list and the recipient is found in Recipient
     Lookup, the Exchange server sends a 250 2.1.5 Recipient OK SMTP response to the
     sending server, and the next antispam agent in the chain processes the message.

  ７ Note

  Although the Recipient Filter agent is available on Mailbox servers, you shouldn't
  configure it. When recipient filtering on a Mailbox server detects one invalid or blocked
  recipient in a message that contains other valid recipients, the message is rejected. The
  Recipient Filter agent is enabled when you install the antispam agents on a Mailbox server,
  but it isn't configured to block any recipients. For more information, see Enable antispam
  functionality on Mailbox servers.

Configuring recipient lookup
One of the most effective ways to reduce spam is to validate recipients before accepting
inbound messages from the Internet. You enable the blocking of messages sent to recipients
who don't exist in the Exchange organization, and the blocking of specific recipients using the
Set-RecipientFilterConfig cmdlet in the Exchange Management Shell.

Tarpitting functionality
Recipient Lookup functionality enables the sending server to determine whether an email
address is valid or invalid. As mentioned earlier, when the recipient of an inbound message is a
known recipient, the Exchange server sends back a 250 2.1.5 Recipient OK SMTP response to
the sending server. This functionality provides an ideal environment for a directory harvest
attack, where a spammer uses an automated program to collect email addresses that return a
250 2.1.5 Recipient OK SMTP response.

To combat directory harvest attacks, Exchange includes tarpitting functionality. Tarpitting is the
practice of artificially delaying server responses for specific SMTP communication patterns that
indicate high volumes of mail, so that the cost of sending spam increases for the spammer.

<!-- p.3045 -->

If tarpitting isn't configured, the Exchange server immediately returns a 550 5.1.1 User
unknown SMTP session error to the sender when a recipient isn't located in Recipient Lookup.

Alternatively, if tarpitting is configured, the Exchange server waits a specified number of
seconds before it returns the 550 5.1.1 User unknown error. This pause in the SMTP session
makes automating a directory harvest attack more difficult and less cost-effective for the
spammer. By default, tarpitting is configured for 5 seconds on Receive connectors.

To configure the delay before SMTP returns the 550 5.1.1 User unknown error, you set the
tarpitting interval using the TarpitInterval parameter on the Set-ReceiveConnector cmdlet. For
more information, see Message throttling on Receive connectors.

Multiple namespaces
The Recipient Filter agent performs recipient lookups only for authoritative domains. If your
organization accepts and forwards messages on behalf of another domain that's configured as
an internal relay or external relay domain, the Recipient Filter agent doesn't perform a recipient
lookup on recipients in those domains. However, if the recipient is specified in the Recipient
Block list, the recipient will still be blocked by the Recipient Filter agent.

Note that you can also configure accepted domains locally on an Edge Transport server. If the
domain is configured as internal relay or external relay domain, the Recipient Filter agent on
the Edge Transport server also doesn't perform a recipient lookup on recipients in those
domains.

<!-- p.3046 -->

Antimalware protection in Exchange Server
07/28/2025

APPLIES TO:        2016      2019       Subscription Edition

Antimalware protection in Exchange Server 2016 helps combat viruses and spyware in your
email messaging environment. Viruses infect other programs and data, and they spread
throughout your computer looking for programs to infect. Spyware gathers personal
information (for example, sign-in information and personal data) and sends it back to its
author.

The antimalware protection in Exchange Server was introduced in Exchange 2013, and is
provided by the Transport agent named Malware Agent. The agent scans messages as they
travel through the Transport service on a Mailbox server. You configure malware filtering by
using:

     Antimalware policies: Specify inbound and outbound scanning and notification options
     for malware filtering. There's a default policy that applies to all recipients in the Exchange
     organization, and you can create addtional policies that are applied in a specific order.

     Antimalware server settings: Specify the error and retry actions, and the engine and
     definition update settings for malware filtering. The Malware agent uses Internet access
     on TCP port 80 (HTTP) to check for engine and definition updates every hour.

     Antimalware scripts: Enable or disable malware filtering on the server, and manually
     download engine and definition updates.

For procedures related to malware filtering, see Procedures for antimalware protection in
Exchange Server. For more information about the antispam features in Exchange Server, see
Antispam protection in Exchange Server.

Antimalware policies
Antimalware policies control the actions and notification options for malware detections. The
important settings in antimalware policies are:

     Action: Specifies what to do when a message is found to contain malware. The options
     are:

          Delete the message (this is the default value).

          Replace all attachments with a text file that contains this default text:

<!-- p.3047 -->

           Malware was detected in one or more attachments included with this email. All
           attachments have been deleted.

        Replace all attachments with a text file that contains the custom text you specify.

     Notifications: When an antimalware policy is configured to delete messages, you can
     choose whether to send a notification message to the sender. You can send notification
     messages based on whether the sender is internal or external. The default notification
     message has these properties:

        From: Postmaster postmaster@ <defaultdomain>.com

        Subject: Undeliverable message

        Message text: This message was created automatically by mail delivery software. Your
        email message wasn't delivered to the intended recipients because malware was
        detected.

     You can customize the message properties for internal and external notifications. You can
     also specify additional recipients (administrators) to receive notifications for undeliverable
     messages from internal or external senders.

     Recipient filters: For custom antimalware policies, you can specify recipient conditions
     and exceptions that determine who the policy applies to. You can use these properties for
     conditions and exceptions:
        By recipient
        By accepted domain
        By group membership

     You can only use a condition or exception once, but the condition or exception can
     contain multiple values. Multiple values of the same condition or exception use OR logic
     (for example, <recipient1> or <recipient2>). Different conditions or exceptions use AND
     logic (for example, <recipient1> and <member of group 1>).

     Priority: If you create multiple custom antimalware policies, you can specify the order that
     they're applied.

Antimalware policies in the Exchange admin center vs the
Exchange Management Shell
The basic elements of an antimalware policy are:

     The malware filter policy: Specifies the action and notification options for malware
     filtering.

<!-- p.3048 -->

     The malware filter rule: Specifies the priority and recipient filters (who the policy applies
     to) for a malware filter policy.

The difference between these two elements isn't obvious when you manage antimalware
policies in the Exchange admin center (EAC):

     When you create an antimalware policy in the EAC, you're actually creating a malware
     filter rule and the associated malware filter policy at the same time using the same name
     for both.
     When you modify an antimalware policy in the EAC, settings related to the name, priority,
     enabled or disabled, and recipient filters modify the malware filter rule. Other settings
     (actions and notification options) modify the associated malware filter policy.
     When you remove an antimalware policy from the EAC, the malware filter rule and the
     associated malware filter policy are removed.

In the Exchange Management Shell, the difference between malware filter policies and malware
filter rules is apparent. You manage malware filter policies by using the *-MalwareFilterPolicy
cmdlets, and you manage malware filter rules by using the *-MalwareFilterRule cmdlets.

     In the Exchange Management Shell, you create the malware filter policy first, then you
     create the malware filter rule that identifies the policy that the rule applies to.
     In the Exchange Management Shell, you modify the settings in the malware filter policy
     and the malware filter rule separately.
     When you remove a malware filter policy from the Exchange Management Shell, the
     corresponding malware filter rule isn't automatically removed, and vice versa.

Default antimalware policy
Every Mailbox server has a built-in antimalware policy named Default that has these properties:

     The malware filter policy named Default is applied to all recipients in the Exchange
     organization, even though there's no malware filter rule (recipient filters) associated with
     the policy.

     The policy named Default has the custom priority value Lowest that you can't modify (the
     policy is always applied last). Any custom antimalware policies that you create always
     have a higher priority than the policy named Default.

     The policy named Default is the default policy (the IsDefault property has the value True ),
     and you can't delete the default policy.

Antimalware server settings

<!-- p.3049 -->

You can use the Get-MalwareFilteringServer and Set-MalwareFilteringServer cmdlets in the
Exchange Management Shell to view and configure the update, timeout, and download
settings for the Malware agent on the Mailbox server. For procedures that use these cmdlets,
see Use the Exchange Management Shell to bypass malware filtering on Mailbox servers and
Use the Exchange Management Shell to configure malware filtering to rescan messages that
were already scanned by Microsoft 365.

Antimalware scripts
Exchange includes two Exchange Management Shell scripts that you can use to manage
malware filtering:

      Disable-Antimalwarescanning.ps1 disables the Malware agent, and malware engine and

     definition updates on the Mailbox server.

      Enable-Antimalwarescanning.ps1 enables the Malware agent, enables malware engine and

     definition updates, and runs engine and definition updates on the Mailbox server.

      Update-MalwareFilteringServer.ps1 manually runs malware engine and definition

     updates on the Mailbox server.

For more information about using these scripts, see Use the Exchange Management Shell to
enable or disable malware filtering on Mailbox servers and Download antimalware engine and
definition updates.

Antimalware protection options in Exchange Server
This list describes the antimalware options for Exchange:

     Built-in antimalware protection: You can use the built-in antimalware protection in
     Exchange to help you combat malware. You can use it by itself, or you can pair it with
     other antimalware solutions to provide a layered defense against malware.

     Cloud antimalware protection: You can buy an Exchange Online Protection (EOP)
     subscription for cloud protection of on-premises email environments. Cloud antimalware
     protection for email is multi-layered and designed to catch malware that travels into or
     out of your organization. The advantages of paring built-in antimalware protection with
     cloud email protection are:

        Powerful heuristic detection that provides protection even during the early stages of a
        malware outbreak.

        Reporting capabilities, including malware statistics.

<!-- p.3050 -->

        Message trace for self-troubleshooting mail flow problems including malware
        detections.

        For more information about cloud antimalware protection, see Anti-malware
        protection for cloud mailboxes.

     Third-party antimalware protection: You can buy a third-party antimalware program.

Antimalware FAQ for Exchange
This section answers the frequently asked questions about built-in malware filtering and
scanning in Exchange.

Why did malware that was identified by other antimalware
services get past Exchange antimalware filtering?
There are two likely reasons:

     The most likely scenario is the message attachment doesn't actually contain any active
     malicious code. Some antimalware engines are more aggressive than others, and these
     engines might stop messages simply because they contain truncated malware payloads
     that don't actually do anything.
     The malware you received is a new variant without a pattern file in the antimalware
     engine (yet).

I received a message with an unfamiliar attachment. Is this
malware or can I disregard this attachment?
We strongly advise that you don't open any attachments that you don't recognize. If you would
like us to investigate the attachment, submit it to us as described in the next item.

How do I submit known malware, suspicious files, or false
positives to Microsoft?
Save a copy of the message and upload the message to the Microsoft Security Intelligence
website so we can examine it.

If the sample contains malware, we take corrective action to prevent the virus from going
undetected. If the sample is clean, we take corrective action to prevent the file from being
detected as malware.

<!-- p.3051 -->

Where can I get the messages that the malware filter deleted?
You can't. The messages were found to contain active malicious code, so they were deleted.

Can I use mail flow rules to bypass malware filtering?
No, you can't use mail flow rules (also known as transport rules) to bypass the Malware agent.
Instead, send the attachment in a password-protected .zip file (malware filtering skips
password-protected .zip files).

<!-- p.3052 -->

Procedures for anti-malware protection in
Exchange Server
07/22/2025

APPLIES TO:      2016      2019       Subscription Edition

Exchange Server includes the Malware Agent on Mailbox servers. For more information about
malware filtering in Exchange, see anti-malware protection in Exchange Server.

This article describes the following procedures for managing malware filtering in Exchange:

     Disable or enable malware filtering on a Mailbox server
     Bypass malware filtering on a Mailbox server
     Create anti-malware policies
     View anti-malware policies
     Modify anti-malware policies
     Enable and disable anti-malware policies
     Set the priority of anti-malware policies
     Remove anti-malware policies
     Configure malware filtering to scan messages already scanned by Exchange Online
     Protection (EOP).
     Configure a malware filtering bypass for a recipient or group of recipients.

What do you need to know before you begin?
     We recommend that you manually download anti-malware engine and definition updates
     on your Exchange server before placing it into production. For more information, see
     Download anti-malware engine and definition updates.

     An anti-malware policy consists of a malware filter policy and a malware filter rule. Each
     element controls different settings that don't overlap. The difference between these
     elements isn't visible in the Exchange admin center (EAC), but it's obvious in the Exchange
     Management Shell because you use different cmdlets to manage the settings (*-
     MalwareFilterPolicy and *-MalwareFilterRule). This article refers to anti-malware policies
     for procedures in the EAC, and malware filter policies and malware filter rules for
     procedures in the Exchange Management Shell. For more information, see anti-malware
     protection in Exchange Server.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "anti-malware" entry in the
     Antispam and anti-malware permissions article.

<!-- p.3053 -->

     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to enable or
disable malware filtering on Mailbox servers
Disabling malware filtering on a Mailbox server disables the Malware agent and definition and
engine updates.

   1. To disable malware filtering on the local Mailbox server, run this command in the
     Exchange Management Shell:

       PowerShell

       & $env:ExchangeInstallPath\Scripts\Disable-AntimalwareScanning.ps1

     To enable malware filtering on the local Mailbox server, run this command in the
     Exchange Management Shell:

       PowerShell

       & $env:ExchangeInstallPath\Scripts\Enable-AntimalwareScanning.ps1

     If the command was successful, you see this message:

     Anti-malware scanning is successfully <enabled or disabled>. Please restart
     MSExchangeTransport for the changes to take effect.

     Note: The enable script also applies malware engine and definition updates as needed.

   2. Restart the Exchange Transport service by running this command, which temporarily
     interrupts mail flow on the server:

       PowerShell

       Restart-Service MSExchangeTransport

<!-- p.3054 -->

     The change might take up to 10 minutes to take effect.

How do you know you successfully enabled or disabled
malware filtering on a Mailbox server?
To verify you successfully enabled or disabled malware filtering on a Mailbox server, run this
command in the Exchange Management Shell, and verify the value of the Enabled property:

  PowerShell

  Get-TransportAgent "Malware Agent"

Use the Exchange Management Shell to bypass
malware filtering on Mailbox servers
Bypassing malware filtering allows you to temporarily disable malware filtering on the server
without disrupting mail flow (you don't need to restart the Exchange Transport service).

Note: You should only bypass malware filtering on a Mailbox server when you're
troubleshooting a problem. When you're done, you should turn malware filtering back on.

To bypass or reenable malware filtering on a Mailbox server, use this syntax:

  PowerShell

  Set-MalwareFilteringServer -Identity <ServerIdentity> -BypassFiltering <$true |
  $false>

This example bypasses malware filtering on the server named Mailbox01.

  PowerShell

  Set-MalwareFilteringServer -Identity Mailbox01 -BypassFiltering $true

This example reenables malware filtering on the same server.

  PowerShell

  Set-MalwareFilteringServer -Identity Mailbox01 -BypassFiltering $false

The change might take up to 10 minutes to take effect.

<!-- p.3055 -->

For detailed syntax and parameter information, see Set-MalwareFilteringServer.

How do you know you temporarily bypassed or reenabled
malware filtering on a Mailbox server?
To verify you temporarily bypassed or reenabled malware filtering on a Mailbox server, run this
command in the Exchange Management Shell, and verify the value of the BypassFiltering
property:

  PowerShell

  Get-MalwareFilteringServer | Format-List Name,BypassFiltering

Create anti-malware policies

Use the EAC to create anti-malware policies
Creating an anti-malware policy in the EAC creates the malware filter rule and the associated
malware filter policy at the same time using the same name for both.

   1. In the EAC, go to Protection > Malware filter, and then select New       .

   2. In the New anti-malware policy page that opens, configure these settings:

            Name: Enter a unique, descriptive name for the policy.

            Description: Enter an optional description for the policy.

            Malware detection response: Select one of these options:

               Delete the entire message: Prevents the entire message from being delivered to
               the intended recipients. This value is the default.

               Delete all attachments and use default alert text: Replaces all message
               attachments (not just the detected ones) with a text file that contains this default
               text:

                 Malware was detected in one or more attachments included with this email.
                 All attachments have been deleted.

               Delete all attachments and use custom alert text: Replaces all message
               attachments (not just the detected ones) with a text file that contains custom text

<!-- p.3056 -->

   you specify in the Custom alert text field.

  ７ Note

  If malware is detected in the message body of an inbound or outbound
  message, the entire message is deleted, regardless of the setting you configure
  for Malware detection response.

Notification: The settings in this section control notifications when malware filtering
deletes the message. The settings don't apply to messages where default or custom
alert text replaces all attachments.

   Sender Notifications: Select one or both of these options:

      Notify internal senders: An internal sender is inside the Exchange
      organization.

      Notify external senders: An external sender is outside the Exchange
      organization.

   Administrator Notifications: Select one or both of these options:

      Notify administrator about undelivered messages from internal senders: If
      you select this option, enter a notification email address in the Administrator
      email address field.

      Notify administrator about undelivered messages from external senders: If
      you select this option, enter a notification email address in the Administrator
      email address field.

   Customize Notifications: These settings replace the default notification text that's
   used for senders or administrators. For more information about the default
   values, see anti-malware policies.

      Use customized notification text: If you select this option, you need to use the
      From name and From address fields to specify the sender's name and email
      that's used in the customized notification message.

      Messages from internal senders: If you elected to notify senders or
      administrators about undeliverable messages from internal senders, you need
      to use the Subject and Message fields to specify the subject and message
      body of the custom notification message.

<!-- p.3057 -->

                 Messages from external senders: If you elected to notify senders or
                 administrators about undeliverable messages from external senders, you need
                 to use the Subject and Message fields to specify the subject and message
                 body of the custom notification message.

           Applied to: The settings in this section identify the internal recipients that the policy
           applies to.

              If: Click on the Select one drop-down, and select conditions for the rule:

                 The recipient is: Specifies one or more mailboxes, mail users, or mail contacts
                 in the Exchange organization. In the Select members dialog box that appears,
                 select one or more recipients from the list, and then select add ->. In the
                 Check names field, you can use wildcards for multiple email addresses (for
                 example: *@fabrikam.com). When you're finished, select OK.

                 The recipient domain is: Specifies recipients in one or more of the configured
                 accepted domains in the Exchange organization. In the dialog box that
                 appears, select one or more domains, and then select add ->. When you're
                 finished, select OK.

                 The recipient is a member of: Specifies one or more groups in the Exchange
                 organization. In the Select members dialog box that appears, select one or
                 more groups from the list, and then select add ->. When you're finished, select
                 OK.

           You can only use one a condition once, but you can specify multiple values for the
           condition. To add more conditions, select Add condition and select from the
           remaining options.
              Except if: To add exceptions for the rule, select Add exception, click on the Select
              one drop-down, and configure an exception for the rule. The settings and
              behavior are exactly like the conditions.

  3. When you're finished, select Save.

Use the Exchange Management Shell to create anti-malware
policies
Creating an anti-malware policy in the Exchange Management Shell is a two-step process:

  1. Create the malware filter policy.
  2. Create the malware filter rule that specifies the malware filter policy that the rule applies
     to.

<!-- p.3058 -->

Notes:

     You can create a new malware filter rule and assign an existing, unassociated malware
     filter policy to it. A malware filter rule can't be associated with more than one malware
     filter policy.

     There are two settings that you can configure on new anti-malware policies in the
     Exchange Management Shell that aren't available in the EAC until after you create the
     policy:

         Create the new policy as disabled (Enabled $false on the New-MalwareFilterPolicy
         cmdlet).

         Set the priority of the policy during creation (Priority <Number>) on the New-
         MalwareFilterRule cmdlet).

     Malware filter policies that you create in the Exchange Management Shell don't appear in
     the EAC until you assign the malware filter policy to a malware filter rule.

     A setting that's available in the Exchange Management Shell that isn't available in the EAC
     is the ability to turn malware filtering on or off for inbound messages or outbound
     messages by using the BypassInboundMessages or BypassOutboundMessages parameters
     on the New-MalwareFilterPolicy cmdlet.

Step 1: Use the Exchange Management Shell to create a malware filter
policy
To create a malware filter policy, use this syntax:

  PowerShell

  New-MalwareFilterPolicy -Name "<PolicyName>" [-Action <DeleteMessage |
  DeleteAttachmentAndUseDefaultAlert | DeleteAttachmentAndUseCustomAlert>] [-
  AdminDisplayName "<OptionalComments>"] [-BypassInboundMessages <$true | $false>]
  [-BypassOutboundMessages <$true | $false>] [-CustomNotifications <$true | $false>]
  [<Inbound notification options>] [<Outbound notification options>]

This example creates a new malware filter policy named Contoso Malware Filter Policy with
these settings:

     Block messages that contain malware (we aren't using the Action parameter, and the
     default value is DeleteMessage ).

     Don't notify the message sender when malware is detected in the message (we aren't
     using the EnableExternalSenderNotifications or EnableInternalSenderNotifications

<!-- p.3059 -->

     parameters, and the default value for both is $false ).

     Notify the administrator admin@contoso.com when malware is detected in a message
     from an internal sender.

  PowerShell

  New-MalwareFilterPolicy -Name "Contoso Malware Filter Policy" -
  EnableInternalSenderAdminNotifications $true -InternalSenderAdminAddress
  admin@contoso.com

For detailed syntax and parameter information, see New-MalwareFilterPolicy.

Step 2: Use the Exchange Management Shell to create a malware filter
rule
To create a malware filter rule, use this syntax:

  PowerShell

  New-MalwareFilterRule -Name "<RuleName>" -MalwareFilterPolicy "<PolicyName>"
  <Recipient filters> [<Recipient filter exceptions>] [-Comments "
  <OptionalComments>"]

This example creates a new malware filter rule named Contoso Recipients with these settings:

     The malware filter policy named Contoso Malware Filter Policy is associated with the rule.

     The rule applies to recipients in the contoso.com domain.

  PowerShell

  New-MalwareFilterRule -Name "Contoso Recipients" -MalwareFilterPolicy "Contoso
  Malware Filter Policy" -RecipientDomainIs contoso.com

For detailed syntax and parameter information, see New-MalwareFilterRule.

How do you know you successfully created an anti-malware
policy?
To verify you successfully created an anti-malware policy, do any of these steps:

     In the EAC, go to Protection > Malware filter. Verify that the rule you created is in the list.
     Select Edit     to verify the settings of the rule.

<!-- p.3060 -->

    In the Exchange Management Shell, replace <PolicyName> with the name of the malware
    filter policy, and run this command to verify the property values:

 PowerShell

 Get-MalwareFilterPolicy -Identity "<PolicyName>" | Format-List

    In the Exchange Management Shell, replace <RuleName> with the name of the malware
    filter rule, and run this command to verify the property values:

       PowerShell

       Get-MalwareFilterRule -Identity "<RuleName>" | Format-List

    Use a European Institute for Computer Antivirus Research (EICAR) test file to verify that
    the malware filter is working correctly:

 1. Open Notepad, and insert this text (and only this text) into an empty file:

       PowerShell

       X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

    Save the file as EICAR.txt in a location that's easy for you to find, and that's excluded from
    scanning by your computer's antivirus program. The file is 68 bytes in size.

 2. Create an email messages, attach the EICAR.txt file to the message, and send the message
    to a recipient in your Exchange organization who the malware policy should affect.

 3. Check the recipient's mailbox to verify that malware filtering acted on the message:

          The message was deleted.
          The message was delivered with the replacement alert text file for the attachment.
          Notification messages were delivered to the sender and/or administrators.

 4. When you're finished, delete the EICAR.TXT file so other users aren't unnecessarily
    alarmed.

View anti-malware policies

Use the EAC to view anti-malware policies
 1. In the EAC, go to Protection > Malware filter.

<!-- p.3061 -->

   2. When you select a policy, information about the policy is displayed in the details pane. To
     see more information about the policy, select Edit      .

           The Enabled property value, the Priority property value, and the settings on the
           Applied to tab are in the malware filter rule.

           The settings on the General and Settings tabs are in the malware filter policy.

Use the Exchange Management Shell to view malware filter
policies
To return a summary list of all malware filter policies, run this command:

  PowerShell

  Get-MalwareFilterPolicy

To return detailed information about a specific malware filter policy, use this syntax:

  PowerShell

  Get-MalwareFilterPolicy -Identity "<PolicyName>" | Format-List [<Specific
  properties to view>]

This example returns all the property values for the malware filter policy named Executives.

  PowerShell

  Get-MalwareFilterPolicy -Identity "Executives" | Format-List

This example returns only the specified properties for the same policy.

  PowerShell

  Get-MalwareFilterPolicy -Identity "Executives" | Format-List
  Action,AdminDisplayName,CustomNotifications,Enable*Notifications

For detailed syntax and parameter information, see Get-MalwareFilterPolicy.

Use the Exchange Management Shell to view malware filter
rules
To return a summary list of all malware filter rules, run this command:

<!-- p.3062 -->

  PowerShell

  Get-MalwareFilterRule

To return detailed information about a specific malware filter rule, use this syntax:

  PowerShell

  Get-MalwareFilterRule -Identity "<RuleName>" | Format-List [<Specific properties
  to view>]

This example returns all the property values for the malware filter rule named Executives.

  PowerShell

  Get-MalwareFilterRule -Identity "Executives" | Format-List

This example returns only the specified properties for the same rule.

  PowerShell

  Get-MalwareFilterRule -Identity "Executives" | Format-List
  Name,Priority,State,MalwareFilterPolicy,*Is,*SentTo,*MemberOf

For detailed syntax and parameter information, see Get-MalwareFilterRule.

Modify anti-malware policies
No extra settings are available when you modify a malware policy in the EAC or the Exchange
Management Shell. They're the same settings that were available when you created the policy.

Use the EAC to modify an anti-malware policy
   1. In the EAC, go to Protection > Malware filter.

   2. Select the policy, and then select Edit   . For information about the settings, see the Use
     the EAC to create anti-malware policies section in this article.

     Notes:

           Instead of everything on one page, the settings are divided among the General,
           Settings, and Applied to tabs. The Applied to tab isn't available on the default
           policy named Default.

<!-- p.3063 -->

            You can't rename the default policy.

Use the Exchange Management Shell to modify a malware
filter policy
To modify a malware filter policy, use this syntax:

  PowerShell

   Set-MalwareFilterPolicy -Identity "<PolicyName>" <Settings>

For detailed syntax and parameter information, see Set-MalwareFilterPolicy.

Use the Exchange Management Shell to modify a malware
filter rule
When you modify a malware filter rule in the Exchange Management Shell, you can't disable or
enable the rule (there's no Enabled parameter on the Set-MalwareFilterRule cmdlet). Instead,
you use the Disable-MalwareFilterRule and Enable-MalwareFilterRule cmdlets as described
later in this article.

To modify a malware filter rule, use this syntax:

  PowerShell

   Set-MalwareFilterRule -Identity "<RuleName>" <Settings>

For detailed syntax and parameter information, see Set-MalwareFilterRule.

Enable or disable anti-malware policies
By default, anti-malware policies are enabled when you create them in the EAC or the Exchange
Management Shell, but you can use the Exchange Management Shell to create a disabled
malware filter rule (use the New-MalwareFilterRule cmdlet and the Enabled parameter with the
value $false ).

Use the EAC to enable or disable an anti-malware policy
   1. In the EAC, go to Protection > Malware filter.

   2. Select the policy from the list, and then configure one of the following settings:

<!-- p.3064 -->

           Disable the policy: Clear the check box in the Enabled column.

           Enable the policy: Select the check box in the Enabled column.

Use the Exchange Management Shell to enable or disable
malware filter rules
To enable or disable a malware filter rule in the Exchange Management Shell, use this syntax:

  PowerShell

  <Enable-MalwareFilterRule | Disable-MalwareFilterRule> -Identity "<RuleName>"

This example disables the malware filter rule named Marketing Department.

  PowerShell

  Disable-MalwareFilterRule -Identity "Marketing Department"

This example enables same rule.

  PowerShell

  Enable-MalwareFilterRule -Identity "Marketing"

For detailed syntax and parameter information, see Enable-MalwareFilterRule and Disable-
MalwareFilterRule.

How do you know you successfully enabled or disabled an
anti-malware policy?
To verify you successfully enabled or disabled an anti-malware policy, use either of these
procedures:

     In the EAC, go to Protection > Malware filter, and in the list of anti-malware policies,
     verify the status of the check box in the Enabled column.

     In the Exchange Management Shell, run this command to see the list of rules and their
     State property values:

        PowerShell

<!-- p.3065 -->

            Get-MalwareFilterRule

Set the priority of custom anti-malware policies
By default, anti-malware policies are given a priority based on the order they were created in
(newer policies are lower priority than older policies). A lower priority number indicates a
higher priority for the policy, and policies are processed in priority order (higher priority
policies are processed before lower priority policies). No two policies can have the same
priority.

Notes:

      In the EAC, you can only change the priority of the anti-malware policy after you create it.
      In the Exchange Management Shell, you can override the default priority when you create
      the malware filter rule (which can affect the priority of existing rules).

      The default anti-malware policy named Default has the priority value Lowest, and you
      can't change it.

Use the EAC to set the priority of custom anti-malware
policies
In the EAC, anti-malware policies are processed in the order that they're displayed (the first
policy has the Priority value 0). To change the priority of a policy, move the policy up or down
in the list (you can't directly modify the Priority number in the EAC).

   1. In the EAC, go to Protection > Malware filter.

   2. Select a policy, and then select Move up ( ) or Move down ( ) to move the rule up or
      down in the list.

Use the Exchange Management Shell to set the priority of
custom malware filter rules
The highest priority value you can set on a rule is 0. The lowest value you can set depends on
the number of rules. For example, if you have five rules, you can use the priority values 0
through 4. Changing the priority of an existing rule can have a cascading effect on other rules.
For example, if you have five rules (priorities 0 through 4), and you change the priority of a rule
to 2, the existing rule with priority 2 is changed to priority 3, and the rule with priority 3 is
changed to priority 4.

<!-- p.3066 -->

To set the priority of a malware filter rule in the Exchange Management Shell, use the following
syntax:

  PowerShell

  Set-MalwareFilterRule -Identity "<RuleName>" -Priority <Number>

This example sets the priority of the rule named Marketing Department to 2. All existing rules
that have a priority less than or equal to 2 are decreased by 1 (their priority numbers are
increased by 1).

  PowerShell

  Set-MalwareFilterRule -Identity "Marketing Department" -Priority 2

Note: To set the priority of a new rule when you create it, use the Priority parameter on the
New-MalwareFilterRule cmdlet.

How do you know you successfully modified the priority of an
anti-malware policy?
To verify you successfully modified the priority of an anti-malware policy, use either of these
procedures:

     In the EAC, go to Protection > Malware filter, and verify the Priority value of the anti-
     malware policies in the list.

     In the Exchange Management Shell, run this command to see the list of rules and their
     Priority property values:

          PowerShell

          Get-MalwareFilterRule

Remove anti-malware policies
Note: You can't remove the default anti-malware policy.

Use the EAC to remove anti-malware policies

<!-- p.3067 -->

When you use the EAC to remove an anti-malware policy, the malware filter rule and the
corresponding malware filter policy are both removed.

   1. From the EAC, go to Protection > Malware filter.

   2. Select the anti-malware policy you want to remove from the list, and then select Delete (
       ).

Use the Exchange Management Shell to remove malware filter
policies
When you use the Exchange Management Shell to remove a malware filter policy, the
corresponding malware filter rule isn't removed.

To remove a malware filter policy in the Exchange Management Shell, use this syntax:

  PowerShell

  Remove-MalwareFilterPolicy -Identity "<PolicyName>"

This example removes the malware filter policy named Marketing Department.

  PowerShell

  Remove-MalwareFilterPolicy -Identity "Marketing Department"

For detailed syntax and parameter information, see Remove-MalwareFilterPolicy.

Use the Exchange Management Shell to remove malware filter
rules
When you use the Exchange Management Shell to remove a malware filter rule, the associated
malware filter policy isn't removed.

To remove a malware filter rule in the Exchange Management Shell, use this syntax:

  PowerShell

  Remove-MalwareFilterRule -Identity "<RuleName>"

This example removes the malware filter rule named Marketing Department:

  PowerShell

<!-- p.3068 -->

  Remove-MalwareFilterRule -Identity "Marketing Department"

For detailed syntax and parameter information, see Remove-MalwareFilterRule.

How do you know you successfully removed an anti-malware
policy?
To verify you successfully removed an anti-malware policy, use either of these procedures:

     In the EAC, go to Protection > Malware filter, and verify that the policy you removed is
     no longer in the list.

     In the Exchange Management Shell, run this command to verify that the malware filter
     policy you removed is no longer listed:

        PowerShell

        Get-MalwareFilterPolicy

     In the Exchange Management Shell, run this command to verify that the malware filter
     rule you removed is no longer listed:

        PowerShell

        Get-MalwareFilterRule

Use the Exchange Management Shell to configure
malware filtering to rescan messages already
scanned by EOP
By default, the Malware agent in Exchange doesn't rescan messages in transit that were already
scanned by Exchange Online Protection (EOP). But, rescanning these messages can provide
another layer of defense against malware.

To enable or disable scanning for messages already scanned by EOP, use this syntax in the
Exchange Management Shell:

  PowerShell

  Set-MalwareFilteringServer -Identity <ServerIdentity> -ForceRescan <$true |

<!-- p.3069 -->

  $false>

This example enables scanning for malware in messages already scanned by EOP on the
Mailbox server named Mailbox01.

  PowerShell

  Set-MalwareFilteringServer -Identity Mailbox01 -ForceRescan $true

This example disables scanning for malware in messages already scanned by EOP on the same
server.

  PowerShell

  Set-MalwareFilteringServer -Identity Mailbox01 -ForceRescan $false

How do you know you configured malware filtering to rescan
messages already scanned by EOP?
To verify you configured malware filtering to rescan messages already scanned by EOP, run this
command in the Exchange Management Shell, and verify the value of the ForceRescan
property:

  PowerShell

  Get-MalwareFilteringServer | Format-List Name, ForceRescan

Configure a malware filtering bypass for specific
recipients
To allow for a particular recipient or group of recipients to receive email with attachments that
would otherwise be detected and deleted by the default anti-malware policy, a new anti-
malware policy has to be created, either using EAC or PowerShell. This policy should be set to
scan emails for all recipients and an exclusion condition must be set within that policy for the
recipient or group that is intended to receive such content.

Use the EAC to create the new anti-malware policy:

<!-- p.3070 -->

<!-- p.3071 -->

This procedure creates a malware policy that scans all email traffic except messages sent to the
specified users or groups.

Use the Exchange Management Shell to create an anti-malware policy:

Use the Exchange Management Shell to modify a malware filtering rule.

After you create the anti-malware policy and set the appropriate exclusion, a new anti-malware
policy has to be created in order for the unscanned messages to bypass the default anti-
malware policy that always has the lowest priority. This change can be achieved by using
Exchange Management Shell to set the value of the parameter -BypassInboundMessages of
this anti-malware filtering rule to True. For detailed syntax and parameter information, see Set-
MalwareFilterPolicy.

  PowerShell

  Set-MalwareFilterPolicy -Identity "<PolicyName>" -BypassInboundMessages $true

This method doesn't require a service restart and can allow for Exchange administrators and
security teams to temporarily or permanently bypass anti-malware detection for a particular
recipient or group, thus having otherwise undeliverable messages delivered to that particular
subgroup without compromising the security of the entire Exchange organization and
ultimately retaining security within their systems and for their clients.

How do you know you successfully configured a malware
filtering bypass for specific recipients?
To verify you successfully configured a malware filtering bypass for specific recipients, replace
<PolicyName> with the name of the policy, and run the follow command in the Exchange
Management Shell:

  PowerShell

  Get-MalwareFilterPolicy "<PolicyName>" | Format-List BypassInboundMessages

<!-- p.3072 -->

Download anti-malware engine and
definition updates
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Administrators can manually download anti-malware engine and definition (signature) updates.
We strongly recommend that you download engine and definition updates before you put the
Exchange server into production.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      You can only use PowerShell to perform this procedure.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      To download updates, your computer needs to be able to access the Internet and to
      establish a connection on TCP port 80 (HTTP). If your organization uses a proxy server for
      Internet access, see the following section in this topic.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "anti-malware" entry in the
      Antispam and anti-malware permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Use the Exchange Management Shell to manually
download engine and definition updates
To download engine and definition updates, run the following command:

  PowerShell

<!-- p.3073 -->

  & $env:ExchangeInstallPath\Scripts\Update-MalwareFilteringServer.ps1 -Identity
  <FQDN of server>

This example manually downloads the engine and definition updates on the Exchange server
named mailbox01.contoso.com:

  PowerShell

  & $env:ExchangeInstallPath\Scripts\Update-MalwareFilteringServer.ps1 -Identity
  mailbox01.contoso.com

Optionally, you can use the EngineUpdatePath parameter to download updates from
somewhere other than the default location. You can use this parameter to specify an alternate
HTTP address or a UNC path. If you specify a UNC path, the network service must have access
to the path.

This example manually downloads engine and definition updates on the Exchange server
named mailbox01.contoso.com from the UNC path \\FileServer01\Data\MalwareUpdates :

  PowerShell

  & $env:ExchangeInstallPath\Scripts\Update-MalwareFilteringServer.ps1 -Identity
  mailbox01.contoso.com -EngineUpdatePath \\FileServer01\Data\MalwareUpdates

How do you know this worked?
In order to verify that updates were downloaded successfully, you need to access Event Viewer
and view the event log. We recommend that you filter only FIPFS events, as described in the
following procedure.

   1. From the Start menu, select All Programs > Administrative Tools > Event Viewer.

   2. In Event Viewer, expand the Windows Logs folder, and then select Application.

   3. In the Actions menu, select Filter Current Log.

   4. In the Filter Current Log dialog box, from the Event sources drop-down list, select the
     FIPFS check box, and then select OK.

If engine updates were downloaded successfully, you'll see Event ID 6033, which will appear
similar to the following:

MS Filtering Engine Update process performed a successful scan engine update.

<!-- p.3074 -->

Scan Engine: Microsoft

Update Path: http://forefrontdl.microsoft.com/server/scanengineupdate

Last Update time: 2012-08-16T13:22:17.000Z

Engine Version: 1.1.8601.0

Signature Version: 1.131.2169.0

Use the Exchange Management Shell to configure
proxy server settings for anti-malware updates
If your organization uses a proxy server to control access to the Internet, you need to identify
the proxy server so that you can successfully download anti-malware engine and definition
updates. Proxy server settings that are available using the Netsh.exe tool, Internet Explorer
connection settings, and the InternetWebProxy parameter on the Set-ExchangeServer cmdlet
don't affect how anti-malware updates are downloaded.

To configure the proxy server settings for anti-malware updates, perform the following steps.

   1. Run the following command:

        PowerShell

        Add-PsSnapin Microsoft.Forefront.Filtering.Management.Powershell

   2. Use the Get-ProxySettings and Set-ProxySettings cmdlets to view and configure the
     proxy server settings that are used to download anti-malware updates. The Set-
     ProxySettings cmdlet uses the following syntax:

        PowerShell

        Set-ProxySettings -Enabled <$true | $false> -Server <Name or IP address of
        proxy server> -Port <TCP port of proxy server>

     For example, to configure anti-malware updates to use the proxy server at address
     172.17.17.10 on TCP port 80, run the following command.

        PowerShell

        Set-ProxySettings -Enabled $true -Server 172.17.17.10 -Port 80

<!-- p.3075 -->

To verify the proxy server settings, run the Get-ProxySettings cmdlet.

For more information
     Procedures for anti-malware protection in Exchange Server
     Manually update scan engines in Microsoft Exchange Server

<!-- p.3076 -->

Exchange Server AMSI integration
APPLIES TO:      2016      2019      Subscription Edition

The Windows Antimalware Scan Interface (AMSI) is a versatile interface standard that allows
your applications and services to integrate with any anti-malware product that's present on a
Windows Server. AMSI is vendor agnostic and designed to allow for the most common
malware scanning and protection techniques provided by today's products to be integrated
into applications. It was introduced with Windows Server 2016.

AMSI supports a calling structure allowing for file and memory or stream scanning, content
source URL/IP reputation checks, and other techniques. It also supports the notion of a session
so that anti-malware vendors can correlate different scan requests.

For instance, the different fragments of a malicious payload can be associated to reach a more
informed decision. This association would be harder to reach just by looking at those
fragments in isolation.

AMSI integration in Exchange Server provides the ability for an AMSI-capable antivirus/anti-
malware solution to scan content in HTTP requests sent to Exchange and block malicious
requests before Exchange handles the request. The scan is performed in real-time by any
AMSI-capable antivirus/anti-malware (AV) solution that runs on the Exchange server as the
server begins to process the request. This feature provides automatic mitigation and protection
that compliments the existing anti-malware protection in Exchange Server to help make your
Exchange servers more secure.

In the Exchange Server November 2024 Security Update (SU)        , AMSI integration was
enhanced to include new capabilities for scanning the HTTP message body . This feature is
enabled by default for all protocols beginning with the installation of the August 2025
Exchange Server Security Updates     . For details on how to manage or customize this
functionality, refer to the Enable Exchange Server AMSI Body scanning section.

Prerequisites
To benefit from the AMSI integration in Exchange Server, you need to meet the following
prerequisites:

     Windows Server 2016 or later.
     Partial functionality (no AMSI body scanning):
        Exchange Server 2016 CU21 / Exchange Server 2019 CU10.
     Full functionality (with AMSI body scanning):

<!-- p.3077 -->

        Exchange Server 2016 CU23 / Exchange Server 2019 CU13/CU14 + Exchange Server
        November 2024 Security Update (SU)         or later.
     Microsoft Defender with AV engine version 1.1.18300.4 or later, or a compatible AMSI
     capable non-Microsoft AV provider (check with your vendor).

Be sure to always install the latest Exchange Server update     to benefit from bug fixes and the
latest improvements.

How to verify the Exchange Server AMSI
integration
In this section, we provide information to help you check if Exchange Server AMSI integration is
configured correctly. Exchange Server AMSI integration is enabled by default, except for the
Exchange Server AMSI body scanning feature.

Find your installed AMSI provider
To confirm that you have an AMSI provider installed on your Exchange Server, run the
following Windows PowerShell commands and validate the output:

 PowerShell
 $AMSI = Get-ChildItem -Path "HKLM:\SOFTWARE\Microsoft\AMSI\Providers" -Recurse

 $AMSI | foreach {$_ -match "[0-9A-Fa-f\-]{36}"}

 $Matches.Values | ForEach-Object {Get-ChildItem -Path "HKLM:\SOFTWARE\Classes\CLSID\
 {$_}" | Format-Table -AutoSize}

The output is similar to the following example, depending on your installed antivirus product:

 PowerShell

 Name                    Property
 ----                    --------
 Hosts                   (default) : Scanned Hosting Applications
 Implemented Categories
 InprocServer32          (default) : "C:\ProgramData\Microsoft\Windows
 Defender\Platform\4.18.2106.6-0\MpOav.dll"
                         ThreadingModel : Both

The results indicate that the only provider installed is located at
C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2106.6-0\MpOav.dll , which

<!-- p.3078 -->

corresponds to Microsoft Windows Defender . Windows Server 2016 or later operating systems
recognize our AMSI Provider installation, as confirmed by this information.

Validate AMSI IIS configuration
One of the core components of the Exchange Server AMSI integration is the
HttpRequestFilteringModule . This module is configured in the web.config file for most services,

which are located in the FrontEnd and ClientAccess directories. If you regularly replace or
modify web.config files, ensure that this module is included. Otherwise, the AMSI integration
doesn't work correctly. The configuration line looks like this:

 XML

 <add name="HttpRequestFilteringModule"
 type="Microsoft.Exchange.HttpRequestFiltering.HttpRequestFilteringModule,
 Microsoft.Exchange.HttpRequestFiltering, Version=15.0.0.0, Culture=neutral,
 PublicKeyToken=31bf3856ad364e35" />

Validate Windows Defender version
To validate the signatures using Microsoft Windows Defender, run the following command in
PowerShell to check for the latest definitions and display your current engine version:

 PowerShell

 Get-MpComputerStatus | Format-List *version,*signature*

The output should look similar to the following example:

 PowerShell
 PS C:\> Get-MpComputerStatus | Format-List *version,*signature*
 AMEngineVersion                 : 1.1.25070.4
 AMProductVersion                : 4.18.25070.5
 AMServiceVersion                : 4.18.25070.5
 AntispywareSignatureVersion     : 1.435.556.0
 AntivirusSignatureVersion       : 1.435.556.0
 FullScanSignatureVersion        :
 NISEngineVersion                : 1.1.25070.4
 NISSignatureVersion             : 1.435.556.0
 QuickScanSignatureVersion       : 1.431.627.0
 AntispywareSignatureAge         : 0
 AntispywareSignatureLastUpdated : 9/3/2025 9:37:50 AM
 AntispywareSignatureVersion     : 1.435.556.0
 AntivirusSignatureAge           : 0
 AntivirusSignatureLastUpdated   : 9/3/2025 9:37:51 AM

<!-- p.3079 -->

 AntivirusSignatureVersion           : 1.435.556.0
 DefenderSignaturesOutOfDate         : False
 FullScanSignatureVersion            :
 NISSignatureAge                     : 0
 NISSignatureLastUpdated             : 9/3/2025 9:37:51 AM
 NISSignatureVersion                 : 1.435.556.0
 QuickScanSignatureVersion           : 1.431.627.0

Confirm that AMSI integration works
If the AMSI module detects a malicious request, it's logged in the
%ExchangeInstallPath%\Logging\HttpRequestFiltering folder with a ScanResult value of

Detected . The module doesn't log safe calls; therefore, the presence of a log indicates that a

malicious call was detected. Otherwise there maybe no log files. When a request is blocked,
Internet Information Service (IIS) returns a 400 (Bad Request) status code to the requester.

The following output is an example of a log file, which contains HTTP POST requests that AMSI
helped block:

 text
 DateTime,MajorVersion,MinorVersion,BuildVersion,RevisionVersion,ServerHostName,Share
 dCacheLatency,TotalLatency,HttpMethod,UrlHost,UrlStem,UrlQuery,ServerIP,Protocol,Hea
 derNames,CookieNames,ScanResult,GenericInfo,GenericErrors
 #Software: Microsoft Exchange Server
 #Version: 15.01.build
 #Log-type: Http Request Filtering Logs
 #Date: 2021-06-30T10:03:57.573Z
 #Fields:
 DateTime,MajorVersion,MinorVersion,BuildVersion,RevisionVersion,ServerHostName,Share
 dCacheLatency,TotalLatency,HttpMethod,UrlHost,UrlStem,UrlQuery,ServerIP,Protocol,Hea
 derNames,CookieNames,ScanResult,GenericInfo,GenericErrors
 6/30/2021 10:03:57
 AM,15,1,2334,0,SERVER01,,,POST,localhost,/ecp/x.js,,::1,FrontEnd.Ecp,Content-
 Length;Cookie;Host,X-BEResource,Detected,,
 6/30/2021 10:09:41
 AM,15,1,2334,0,SERVER01,,,POST,SERVER01.contoso.com,/ecp/x.js,,192.168.10.52,FrontEn
 d.Ecp,Content-Length;Cookie;Host,X-BEResource,Detected,,
 6/30/2021 10:09:43
 AM,15,1,2334,0,SERVER01,,,POST,SERVER01.contoso.com,/ecp/x.js,,192.168.10.52,FrontEn
 d.Ecp,Content-Length;Cookie;Host,X-BEResource,Detected,,

You can use the Test-AMSI     script to verify if the AMSI integration functions as expected. The
script sends a crafted HTTP request to trigger the anti-malware scanner, and you can check the
log files on the Exchange Server for Detected entries after execution. Additionally, the script
can be used to check your AMSI Providers on the system and to enable or disable AMSI
integration.

<!-- p.3080 -->

If Exchange Server AMSI body scanning is enabled, you can run the following command from
the Exchange Management Shell (EMS):

 PowerShell

  Get-Mailbox -Anr "amsiscantest:x5opap4pzx54p7cc7$eicar-standard-antivirus-test-
 fileh+h*"

The command should fail to run, and if you open Microsoft Defender or run Get-MpThreat via
PowerShell, you should see the threat Exploit:Script/ExchangeEicar.A being blocked.

Enable Exchange Server AMSI body scanning
The Exchange AMSI body scanning feature, which was introduced with the Exchange Server
November 2024 Security Update (SU)       , is disabled by default. It can be enabled and
configured by creating a setting override via the New-SettingOverride cmdlet. The feature can
be enabled on a per-protocol base or for all protocols. The New-SettingOverride commands in
this section create a Global override, which configures the feature across all Exchange servers
within the organization. It's possible to enable it on just a subset of servers. To do so, add the -
Server parameter as described in the New-SettingOverride documentation.

  ） Important

  This feature is enabled by default for all protocols beginning with the installation of the
  August 2025 Exchange Server Security Updates          .

To enable the AMSI body scanning feature for a specific protocol, you can select from a
predefined set of protocols. Exchange Server AMSI body scanning supports all protocols
except RPC over HTTP :

     EnabledAll
     EnabledApi
     EnabledAutoD
     EnabledEcp
     EnabledEws
     EnabledMapi
     EnabledEas
     EnabledOab
     EnabledOwa
     EnabledPowerShell
     EnabledOthers
