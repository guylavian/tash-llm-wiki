---
title: "Exchange Server — pages 2921-2960"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2921-2960
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2921-2960
family: exchange
documentKind: "doc"
abstract: "see Safelist aggregation. You can't directly modify the Safe Recipients list by using the Set- MailboxJunkEmailConfiguration cmdlet. You modify the Safe Senders list, and those changes are synchronized to the Safe Recipients list. The Outlook Junk Email Filter has additional saf"
---

# Exchange Server — pages 2921-2960

<!-- p.2921 -->

     see Safelist aggregation.

     You can't directly modify the Safe Recipients list by using the Set-
     MailboxJunkEmailConfiguration cmdlet. You modify the Safe Senders list, and those
     changes are synchronized to the Safe Recipients list.

     The Outlook Junk Email Filter has additional safelist collection settings (for example,
     Automatically add people I email to the Safe Senders list, and separate configuration of
     the Safe Senders list and Safe Recipients list). For more information, see Use Junk Email
     Filters to control which messages you see      .

How do you know this worked?
To verify that you have successfully configured the safelist collection on a mailbox, use any of
following procedures:

     Replace <MailboxIdentity> with the identity of the mailbox, and run the following
     command to verify the property values:

        PowerShell

        Get-MailboxJunkEmailConfiguration <MailboxIdentity> | Format-List
        trusted*,contacts*,blocked*

     If the list of email addresses is too long, use this syntax:

        PowerShell

        (Get-MailboxJunkEmailConfiguration
        <MailboxIdentity>).BlockedSendersAndDomains

     For bulk operations, specify the filter that you used to configure the safelist collection,
     and replace the Set-MailboxJunkEmailConfiguration command with Get-
     MailboxJunkEmailConfiguration | Format-List Identity,trusted*,contacts*,blocked* . For

     example:

        PowerShell

        Get-Mailbox -RecipientTypeDetails UserMailbox -OrganizationalUnit
        "contoso.com/North America" | Get-MailboxJunkEmailConfiguration | Format-List
        Identity,trusted*,contacts*,blocked*

<!-- p.2922 -->

Use the Exchange Management Shell to control the
availability of junk email settings in Outlook on the
web
Administrators can control whether users are allowed to enable or disable the junk email rule,
or configure the safelist collection on their own mailboxes in Outlook on the web. This setting
doesn't enable or disable the junk email rule in the mailbox; it controls the availability of the
junk email settings in Outlook on the web for the mailbox.

To use Outlook on the web mailbox policies to allow or prevent users from configuring the junk
email settings on their own mailbox, use the following syntax:

  PowerShell

  Set-OwaMailboxPolicy <OWAMailboxPolicyIdentity> -JunkEmailEnabled <$true | $false>

This example prevents all mailboxes that are assigned the Outlook on the web mailbox policy
named Default from configuring their junk email settings in Outlook on the web.

  PowerShell

  Set-OwaMailboxPolicy Default -JunkEmailEnabled $false

For more information, see Set-OwaMailboxPolicy.

To use Outlook on the web virtual directories to allow or prevent users from configuring the
junk email settings on their own mailbox in Outlook on the web, use the following syntax:

  PowerShell

  Set-OwaVirtualDirectory <OWAVirtualDirectoryIdentity> -JunkEmailEnabled <$true |
  $false>

This example prevents all users that connect to the Outlook on the web virtual directory named
owa (Default Web Site) on the server named Mailbox01 from configuring their junk email
settings.

  PowerShell

  Set-OwaVirtualDirectory "Mailbox01\owa (Default Web Site)" -JunkEmailEnabled
  $false

<!-- p.2923 -->

Note: To apply changes to the Outlook on the web virtual directories, you need to restart
Internet Information Services (IIS) by running the commands Stop-Service WAS -Force and
Start-Service W3SVC .

For more information, see Set-OwaVirtualDirectory.

How do you know this worked?
To verify that you have successfully configured the availability of junk email settings in Outlook
on the web, use either of the following procedures:

     For Outlook on the web mailbox policies, run the following command to verify the
     JunkEmailEnabled property value:

        PowerShell

        Get-OwaMailboxPolicy | Format-Table -Auto Name,JunkEmailEnabled

     For Outlook on the web virtual directories, run the following command to verify the
     JunkEmailEnabled property value:

        PowerShell

        Get-OwaVirtualDirectory | Format-Table -Auto Name,JunkEmailEnabled

Use the Exchange Management Shell to configure
the SCL thresholds on a mailbox
The SCL thresholds are a feature of the Content Filter agent that allows you to escalate the
actions that are taken on messages based on their SCL value. For more information, see
Exchange spam confidence level (SCL) thresholds.

When you configure an SCL threshold on a mailbox (the value is not blank), the setting on the
mailbox overrides the corresponding SCL threshold setting on the Content Filter agent or on
the Exchange organization. The SCL thresholds that are available on the mailbox are described
in the following table:

                                                                                 ﾉ   Expand table

<!-- p.2924 -->

 SCL           SCL value      Action                      Available on       Comments
 threshold**   comparison                                 the Content
               operator                                   Filter agent?

 Delete        Greater than   Silently deletes the        Yes                If this threshold is enabled,
               or equal to    message (no NDR).                              the SCL value should be
                                                                             greater than all others.

 Reject        Greater than   Rejects the message with    Yes                The SCL value should be
               or equal to    an NDR.                                        less than the delete value,
                                                                             but greater than the
                                                                             quarantine or Junk Email
                                                                             folder values.
                                                                             By default, this threshold is
                                                                             enabled on the Content
                                                                             Filter agent, and has the
                                                                             default value 7.

 Quarantine    Greater than   Redirects the message to    Yes                If this threshold is enabled,
               or equal to    the spam quarantine                            the SCL value should be
                              mailbox. For more                              less than the delete or
                              information about the                          reject values, but greater
                              configuring the spam                           than the Junk Email folder
                              quarantine mailbox, see                        value.
                              Configure a spam
                              quarantine mailbox.

 Junk Email    Greater than   Delivers the message to     No                 The SCL value should be
 folder                       the Junk Email folder in    You enable or      less than all others.
                              the mailbox.                disable the SCL    By default, this threshold is
                              This action is controlled   threshold on the   enabled on the Exchange
                              by the junk email rule      mailbox.           organization, and has the
                              that's enabled by default   You configure      default value 4. Because
                              in every mailbox. For       the SCL            the junk email rule is
                              more information, see       threshold value    enabled by default in all
                              the Use the Exchange        on the Exchange    mailboxes, messages that
                              Management Shell to         organization, or   arrive in the mailbox with
                              enable or disable the       on the mailbox.    an SCL value of 5 or higher
                              junk email rule in a                           are moved to the Junk
                              mailbox section in this                        Email folder.
                              topic.

To configure the SCL threshold settings on a mailbox, use the following syntax.

  PowerShell

  Set-Mailbox <MailboxIdentity> -SCLDeleteEnabled <$true | $false | $null> -
  SCLDeleteThreshold <0-9 | $null> -SCLRejectEnabled <$true | $false | $null> -
  SCLRejectThreshold <0-9 | $null> -SCLQuarantineEnabled <$true | $false | $null> -

<!-- p.2925 -->

  SCLQuarantineThreshold <0-9 | $null> -SCLJunkEnabled <$true | $false | $null> -
  SCLJunkThreshold <0-9 | $null>

This example disables the SCL Junk email threshold on mailbox of the user named Jeff Phillips.

  PowerShell

  Set-Mailbox "Jeff Phillips" -SCLJunkEnabled $false

This example disables the SCL Junk email threshold on all user mailboxes in the Organizational
Unit named North America in the consoto.com domain.

  PowerShell

  Get-Mailbox -RecipientTypeDetails UserMailbox -OrganizationalUnit
  "contoso.com/North America" | Set-Mailbox -SCLJunkEnabled $false

This example disables the SCL Junk email threshold on all user mailboxes in the mailbox
database named MDB 01.

  PowerShell

  Get-Mailbox -RecipientTypeDetails UserMailbox -Database "MDB 01" | Set-Mailbox -
  SCLJunkEnabled $false

This example disables the SCL Junk email threshold on all user mailboxes in the organization.

  PowerShell

  $All = Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize Unlimited; $All |
  foreach {Set-Mailbox $_.Name -SCLJunkEnabled $false}

Notes:

     To remove the specific SCL thresholds on the mailbox so the SCL threshold is controlled
     by the Content Filter agent (delete, reject, or quarantine) or the Exchange organization
     (Junk Email folder), use the value $null .

     If you disable the SCL Junk Email folder threshold on the mailbox (SCLJunkEnabled is
     $false ), but the junk email rule is still enabled in the mailbox, Exchange can still deliver

     messages to the Junk Email folder based on the Blocked Senders list of the mailbox.
     Furthermore, even if you disable the Junk E-mail Rule on the mailbox, Outlook (in Cached
     Exchange mode) can still move messages to the Junk Email folder based on its own
     determination of whether the message is spam or the Blocked Senders list.

<!-- p.2926 -->

How do you know this worked?
To verify that you have successfully configured the SCL thresholds on a mailbox, use any of the
following procedures:

     For a single mailbox, replace <MailboxIdentity> with the identity of the mailbox, and run
     the following command to verify the property values:

        PowerShell

        Get-Mailbox <MailboxIdentity> | Format-List SCL*

     For bulk operations, specify the filter that you used to configure the SCL thresholds, and
     replace the Set-Mailbox command with Format-List Name,SCL* . For example:

        PowerShell

        Get-Mailbox -RecipientTypeDetails UserMailbox -OrganizationalUnit
        "contoso.com/North America" | Format-List Name.SCL*

Use the Exchange Management Shell to configure
the SCL Junk Email folder threshold value for all
mailboxes in your organization
The SCL Junk Email folder threshold that's configured on the Exchange organization causes the
junk email rule to deliver messages to the Junk Email folder of a mailbox when all of the
following conditions are true:

     The message is assigned an SCL value by Exchange (typically, by the Content Filter agent).

     The junk email rule in the mailbox is enabled. It's enabled by default, but it isn't fully
     functional until the mailbox has been opened in Outlook (in Cached Exchange mode) or
     Outlook on the web.

     An SCL Junk Email folder threshold isn't configured on the mailbox (by default, it's not
     configured).

     The SCL value of the message is greater than the SCL Junk Email folder threshold that's
     configured for the Exchange organization. The default value is 4, which means that
     messages with an SCL value of 5 or higher are moved to the Junk Email folder by the junk
     email rule.

<!-- p.2927 -->

To configure the SCL Junk Email folder threshold for all mailboxes in your organization, use the
following syntax:

  PowerShell

  Set-OrganizationConfig -SCLJunkThreshold <0-9>

This example sets the organization's SCL Junk Email folder threshold value to 5, which means
messages with an SCL value of 6 or higher are moved to the Junk Email folder by the junk
email rule..

  PowerShell

  Set-OrganizationConfig -SCLJunkThreshold 5

Notes:

     You can override the SCL Junk Email folder threshold value on a mailbox by configuring
     an SCL Junk Email folder threshold on the mailbox. For more information, see the Use the
     Exchange Management Shell to configure the SCL thresholds on a mailbox section in this
     topic.

     If you disable the junk email rule in the mailbox, the value of the SCL Junk Email folder
     threshold for the Exchange organization (or on the mailbox) is meaningless, because the
     junk email rule is required for Exchange to deliver messages to the Junk Email folder. For
     more information, see the Use the Exchange Management Shell to enable or disable the
     junk email rule in a mailbox section in this topic.

How do you know this worked?
To verify that you have successfully configured the SCL Junk Email folder threshold value for all
mailboxes in your organization, run the following command to verify the SCLJunkThreshold
property value:

  PowerShell

  Get-OrganizationConfig | Format-List SCLJunkThreshold

Use the Exchange Management Shell to configure
a mailbox to bypass Exchange antispam filtering

<!-- p.2928 -->

You can configure messages that are sent to specific mailboxes to bypass all Exchange
antispam filters. You can use this setting when Exchange antispam filters are enabled in your
organization, but you want to exempt messages that are sent to specific mailboxes from
antispam filtering. You can configure this setting for mailboxes with a very low tolerance for
false positives (for example, sales or support mailboxes where you can't risk blocking any
legitimate messages).

To configure a mailbox to bypass antispam filtering, use the following syntax:

  PowerShell

  Set-Mailbox <MailboxIdentity> -AntispamBypassEnabled <$true | $false>

This example exempts messages that are sent to the mailbox named Customer Support from
Exchange antispam filtering.

  PowerShell

  Set-Mailbox "Customer Support" -AntispamBypassEnabled $true

How do you know this worked?
To verify that you have successfully configured a mailbox to bypass antispam filtering, use the
following procedures:

     Replace <MailboxIdentity> with the identity of the mailbox, and run the following
     command to verify the AntispamBypassEnabled property value:

        PowerShell

        Get-Mailbox <MailboxIdentity> | Format-List AntispamBypassEnabled

     To find all mailboxes in your organization that are configured to bypass antispam filtering,
     run the following command:

        PowerShell

        Get-Mailbox -ResultSize Unlimited | where {$_.AntispamBypassEnabled -eq
        $true} | Format-Table Name,AntispamBypassEnabled

About junk email settings in Outlook

<!-- p.2929 -->

To enable, disable, and configure the client-side Junk Email Filter settings that are available in
Outlook, use Group Policy. For more information, see Administrative Template files
(ADMX/ADML) and Office Customization Tool for Microsoft 365 Apps for enterprise, Office
2019, and Office 2016        and How to deploy junk email settings, such as the Safe Senders list,
by using Group Policy    .

When the Outlook Junk Email Filter is set to No automatic filtering in Junk > Junk E-Mail
Options > Options, Outlook doesn't attempt to classify messages as spam, but still uses the
safelist collection (the Safe Senders list, Safe Recipients list, and Blocked Senders list) to move
messages to the Junk Email folder.

When the Outlook Junk Email Filter is set to Low or High, the Outlook Junk Email Filter uses its
own SmartScreen filter technology to identify and move spam to the Junk Email folder. This
spam classification is separate from the SCL Junk Email threshold that's configured on the
Exchange organization or on the mailbox. In fact, Outlook ignores the SCL value that's set on a
message by Exchange (for all SCL values other than -1), and uses its own criteria to determine
whether the message is spam (although the spam verdict from Exchange and Outlook might
be the same).

  ７ Note

  In November, 2016, Microsoft stopped producing spam definition updates for the
  SmartScreen filters in Exchange and Outlook. The existing SmartScreen spam definitions
  were left in place, but their effectiveness will likely degrade over time. For more
  information, see Deprecating support for SmartScreen in Outlook and Exchange             .

So, the Outlook Junk Email Filter is able to use the mailbox's safelist collection and its own
spam classification to move messages to the Junk Email folder, even if the junk email rule
and/or the SCL Junk Email threshold are disabled in the mailbox. The difference is whether the
junk email rule on the server or the Junk Email Filter in the Outlook client moves the message
to the Junk Email folder.

Outlook and Outlook on the web both support the safelist collection. The safelist collection is
saved in the Exchange mailbox, so changes to the safelist collection in Outlook appear in
Outlook on the web, and vice-versa. The safelist aggregation feature of the Content Filter
agent shares these lists with the built-in Exchange antispam agents. For more information, see
Safelist aggregation.

<!-- p.2930 -->

Content filtering
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

  ７ Note

  In November, 2016, Microsoft stopped producing spam definition updates for the
  SmartScreen filters in Exchange and Outlook. The existing SmartScreen spam definitions
  were left in place, but their effectiveness will likely degrade over time. For more
  information, see Deprecating support for SmartScreen in Outlook and Exchange          .

Content filtering evaluates inbound email messages by assessing the probability that the
messages are legitimate or spam. Unlike other filtering technologies, the content filtering uses
characteristics from a statistically significant sample of legitimate messages and spam to make
its determination. Content filtering in Exchange Server is provided by the Content Filter agent,
and is basically unchanged from Exchange Server 2010. Updates to the Content Filter agent are
available periodically through Microsoft Update.

By default, the Content Filter agent is enabled on Edge Transport servers, but you can enable it
on Mailbox servers. For more information, see Enable antispam functionality on Mailbox
servers.

For more information about how to configure the Content Filter agent, see Content filtering
procedures.

Using the Content Filter agent
The Content Filter agent assigns a spam confidence level (SCL) to each message by giving it a
rating between 0 and 9. A higher number indicates that a message is more likely to be spam.
Based on this rating, you can configure the agent to take the following actions:

      Delete: The message is silently dropped without a non-delivery report (also known as an
      NDR, delivery status notification, DSN, or bounce message).

      Reject: The message is rejected with an NDR.

      Quarantine: The message is sent to the spam quarantine mailbox. For more information
      about the spam quarantine mailbox, see Spam quarantine in Exchange Server.

For example, you may decide that messages with an SCL rating of 7 or higher should be
deleted, messages with an SCL rating of 6 should be rejected, and that messages with a SCL

<!-- p.2931 -->

rating of 5 should be quarantined.

You can adjust the SCL threshold behavior by assigning different SCL ratings to each of these
actions. For more information about how to adjust the SCL threshold to suit your
organization's requirements, see Exchange spam confidence level (SCL) thresholds.

  ７ Note

  Messages that are over 11 MB aren't scanned by the Intelligent Message Filter. Instead,
  they pass through the Content Filter agent without being scanned.

Allow phrases and Block phrases
You can customize how the Content Filter agent assigns SCL values by configuring custom
words or phrases the agent will use to apply filter processing. Approved words or phrases are
configured with Allow phrases, and unapproved words or phrases with Block phrases. When
the Content Filter agent detects an Allow phrase in an inbound message, the agent
automatically assigns an SCL value of 0 to the message. Alternatively, when the Content Filter
agent detects a Block phrase in an inbound message, the agent assigns an SCL rating of 9. You
can create up to 800 custom words or phrases in any combination of uppercase and lowercase
letters. However, the case is ignored by the Content Filter agent.

Outlook Email Postmark validation
The Content Filter agent also includes Outlook Email Postmark validation. This validation is
applied to outbound messages to help messaging systems distinguish legitimate email from
spam, and to help reduce false positives. In spam filtering, a false positive occurs when a spam
filter incorrectly identifies a legitimate message as spam. When Outlook Email Postmark
validation is enabled, the Content Filter agent parses the inbound message for a computational
postmark header. The presence of a valid, solved computational postmark header in the
message indicates the client computer that generated the message solved the computational
postmark, so the Content Filter agent is likely to lower the message's SCL rating.

Although computers don't require significant processing time to solve individual
computational postmarks, processing postmarks for millions of spam messages will be
prohibitive to a malicious sender. If a sender's message contains a valid, solved computational
postmark, it's unlikely that the sender is malicious, so the Content Filter agent would lower the
SCL rating. If the postmark validation feature is enabled and the computational postmark
header in an inbound message is invalid or missing, the Content Filter agent won't change the
SCL rating.

<!-- p.2932 -->

Bypassing the recipient, sender, and sender domain
In some organizations, all email messages to certain aliases must be accepted, which can cause
problems if your organization manages a significant volume of spam. You can configure
exceptions to content filtering for specific recipients, senders, and sender domains.

For example, a company named Woodgrove Bank has an alias named
customerloans@woodgrovebank.com that provides email support to external loan customers,
so the Exchange administrators configure Block phrases to filter messages that are typically
used in spam sent by unscrupulous loan agencies. To prevent potentially legitimate messages
from being rejected, the administrators set exceptions to content filtering by entering a list of
recipient email addresses in the Content Filter agent configuration.

Safelist aggregation
Safelist aggregation is a set of antispam functionality that's shared across Outlook and
Exchange. As its name suggests, it collects data from the antispam safe lists that Outlook users
configure, and makes this data available to the antispam agents on the Exchange server. The
Content Filter agent uses the Outlook Safe Senders Lists, Safe Recipients Lists, and trusted
contacts to optimize spam filtering. Email messages from these contacts are identified as safe
by the Content Filter agent. Sender filtering and the Sender Filter agent uses the Outlook
Blocked Senders list to perform per-recipient sender filtering. For more information, see Safelist
aggregation.

Configuring the Content Filter agent
You configure the Content Filter agent by using the Exchange Management Shell. For more
information, see Content filtering procedures.

The Content Filter agent depends on updates to determine whether a message is spam. These
updates contain data about phishing web sites, Microsoft SmartScreen spam heuristics, and
other Intelligent Message Filter updates. These updates generally contain about 6 MB of data
that's useful for longer periods of time than other antispam update data.

Content filter updates are available from Microsoft Update. The content filter update data is
updated and available for download every two weeks.

Using the SCL value in mail flow rules on Edge
Transport servers

<!-- p.2933 -->

On Edge Transport servers, the Edge Rule agent acts on messages before the SCL value is
added by the Content Filter agent. If you want to use the SCLOver mail flow rule (also known as
a transport rule) condition, you need to configure the Content Filter agent to run before the
Edge Rule agent by changing the transport agent priorities. For more information, see Make
message SCL values available to mail flow rules on Edge Transport servers.

Notes:

     Although the Content Filter agent runs on other SMTP events, the SCL value is stamped
     on the message by the instance of the Content Filter agent that's registered on the
     OnEndOfData SMTP event.

     If you configure the Content Filter agent to act on messages before the Edge Rule agent
     on an Edge Transport server, the server might incur additional processing costs, because
     messages that would normally be rejected by other mail flow rules are received and
     evaluated by the Content Filter agent before they are rejected by the Edge Rule agent.
     Also, you won't be able to configure a mail flow rule to stamp a message that has an SCL
     value of -1 , which tells the Content Filter agent to ignore the message.

For more information about transport agents and transport agent priority, see Transport
Agents in Exchange Server.

<!-- p.2934 -->

Content filtering procedures
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Content filtering evaluates incoming messages to determine if a message is legitimate or spam.
For more information about content filtering and the Content Filter agent, see Content
filtering.

You can configure many aspects of content filtering. For example:

      Enable or disable content filtering on messages from internal (authenticated) and external
      (unauthenticated) sources (it's enabled by default for incoming messages from external
      sources).

      Configure exceptions to content filtering for specific senders, recipients, and source
      domains.

      Configure allowed phrases and blocked phrases to look for in messages.

      Configure the spam confidence level (SCL) thresholds that tell what content filtering
      should do to messages (delete, reject, or quarantine)

What do you need to know before you begin?
      Estimated time to complete each procedure: less than 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Antispam feature" entry in the
      Antispam and antimalware permissions topic.

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      By default, antispam features aren't enabled in the Transport service on a Mailbox server.
      Typically, you only enable the antispam features on a Mailbox server if your Exchange
      organization doesn't do any prior antispam filtering before accepting incoming messages.
      For more information, see Enable antispam functionality on Mailbox servers.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

<!-- p.2935 -->

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online       , or Exchange Online Protection .

Use the Exchange Management Shell to enable or
disable content filtering
To disable content filtering, run the following command:

  Set-ContentFilterConfig -Enabled $false

To enable content filtering, run the following command:

  Set-ContentFilterConfig -Enabled $true

  ７ Note

  When you disable content filtering, the underlying Content Filter agent is still enabled. To
  disable the Content Filter agent, run the command: Disable-TransportAgent "Content
  Filter Agent" .

How do you know this worked?
To verify that you have successfully enabled or disabled content filtering, run the following
command to verify the Enabled property value:

  Get-ContentFilterConfig | Format-List Enabled

Use the Exchange Management Shell to enable or
disable content filtering for external messages
By default, content filtering functionality is enabled for external messages.

<!-- p.2936 -->

To disable content filtering for external messages, run the following command:

  Set-ContentFilterConfig -ExternalMailEnabled $false

To enable content filtering for external messages, run the following command:

  Set-ContentFilterConfig -ExternalMailEnabled $true

How do you know this worked?
To verify that you have successfully enabled or disabled content filtering for external messages,
run the following command to verify the ExternalMailEnabled property value:

  Get-ContentFilterConfig | Format-List ExternalMailEnabled

Use the Exchange Management Shell to enable or
disable content filtering for internal messages
As a best practice, you don't need to apply antispam filters to messages from trusted partners
or from inside your organization. There's always a chance that the filters will detect false
positives. To reduce the chance that filters will mishandle legitimate email messages, you
should typically configure antispam agents to only run on messages from untrusted and
unknown sources.

To enable content filtering for internal messages, run the following command:

  Set-ContentFilterConfig -InternalMailEnabled $true

To disable content filtering for internal messages, run the following command:

  Set-ContentFilterConfig -InternalMailEnabled $false

<!-- p.2937 -->

How do you know this worked?
To verify that you have successfully enabled or disabled content filtering for internal messages,
run the following command to verify the InternalMailEnabled property value:

  Get-ContentFilterConfig | Format-List InternalMailEnabled

Use the Exchange Management Shell to configure
recipient and sender exceptions for content
filtering
You can specify recipient and sender exceptions that replace the existing values, or you can add
or remove specific sender and recipient exceptions without affecting the other existing values.

To replace the existing values, use the following syntax:

  Set-ContentFilterConfig -BypassedRecipients <recipient1,recipient2...> -
  BypassedSenders <sender1,sender2...> -BypassedSenderDomains <domain1,domain2...>

This example configures the following exceptions in content filtering:

     The recipients laura@contoso.com and julia@contoso.com aren't checked by content
     filtering.

     The senders steve@fabrikam.com and cindy@fabrikam.com aren't checked by content
     filtering.

     All senders in the domain nwtraders.com and all subdomains aren't checked by content
     filtering.

  Set-ContentFilterConfig -BypassedRecipients laura@contoso.com,julia@contoso.com -
  BypassedSenders steve@fabrikam.com,cindy@fabrikam.com -BypassedSenderDomains
  *.nwtraders.com

To add or remove entries without modifying other existing values, use the following syntax:

<!-- p.2938 -->

  Set-ContentFilterConfig -BypassedRecipients @{Add="<recipient1>","
  <recipient2>"...; Remove="<recipient1>","<recipient2>"...} -BypassedSenders
  @{Add="<sender1>","<sender2>"...; Remove="<sender1>","<sender2>"...} -
  BypassedSenderDomains @{Add="<domain1>","<domain2>"...; Remove="<domain1>","
  <domain2>"...}

This example configures the following exceptions in content filtering:

     Add tiffany@contoso.com and chris@contoso.com to the list of existing recipients who
     aren't checked by content filtering.

     Add joe@fabrikam.com and michelle@fabrikam.com to the list of existing senders who
     aren't checked by content filtering.

     Add blueyonderairlines.com to the list of existing domains whose senders aren't checked
     by content filtering.

     Remove the domain woodgrovebank.com and all subdomains from the list of existing
     domains whose senders aren't checked by content filtering.

  Set-ContentFilterConfig -BypassedRecipients
  @{Add="tiffany@contoso.com","chris@contoso.com"} -BypassedSenders
  @{Add="joe@fabrikam.com","michelle@fabrikam.com"} -BypassedSenderDomains
  @{Add="blueyonderairlines.com"; Remove="*.woodgrovebank.com"}

How do you know this worked?
To verify that you have successfully configured the recipient and sender exceptions, run the
following command to verify the property values:

  Get-ContentFilterConfig | Format-List Bypassed*

Use the Exchange Management Shell to configure
allowed and blocked phrases for content filtering
To add allowed and blocked words and phrases, use the following syntax:

<!-- p.2939 -->

  Add-ContentFilterPhrase -Influence GoodWord -Phrase <Phrase> -Influence BadWord -
  Phrase <Phrase>

This example allows all messages that contain the phrase "customer feedback".

  Add-ContentFilterPhrase -Influence GoodWord -Phrase "customer feedback"

This example blocks all messages that contain the phrase "stock tip".

  Add-ContentFilterPhrase -Influence BadWord -Phrase "stock tip"

To remove allowed or blocked phrases, use the following syntax:

  Remove-ContentFilterPhrase -Phrase <Phrase>

This example removes the phrase "stock tip":

  Remove-ContentFilterPhrase -Phrase "stock tip"

How do you know this worked?
To verify that you have successfully configured the allowed and block phrases, run the
following command to verify the property values:

  Get-ContentFilterPhrase | Format-Table -Auto Influence,Phrase

Use the Exchange Management Shell to configure
SCL thresholds for content filtering
To configure the spam confidence level (SCL) thresholds and actions, use the following syntax:

<!-- p.2940 -->

  Set-ContentFilterConfig -SCLDeleteEnabled <$true | $false> -SCLDeleteThreshold
  <Value> -SCLRejectEnabled <$true | $false> -SCLRejectThreshold <Value> -
  SCLQuarantineEnabled <$true | $false> -SCLQuarantineThreshold <Value>

Notes:

     The Delete action takes precedence over the Reject action, and the Reject action takes
     precedence over the Quarantine action. Therefore, the SCL threshold for the Delete action
     should be greater than the SCL threshold for the Reject action, which in turn should be
     greater than the SCL threshold for the Quarantine action. Only the Reject action is
     enabled by default, and it has the SCL threshold value 7.

     The Quarantine action requires a spam quarantine mailbox. For more information, see
     Configure a spam quarantine mailbox.

This example configures the following values for the SCL thresholds:

     The Delete action is enabled and the corresponding SCL threshold is set to 9.

     The Reject action is enabled and the corresponding SCL threshold is set to 8.

     The Quarantine action is enabled and the corresponding SCL threshold is set to 7.

  Set-ContentFilterConfig -SCLDeleteEnabled $true -SCLDeleteThreshold 9 -
  SCLRejectEnabled $true -SCLRejectThreshold 8 -SCLQuarantineEnabled $true -
  SCLQuarantineThreshold 7

How do you know this worked?
To verify that you have successfully configured the SCL thresholds, run the following command
to verify the property values:

  Get-ContentFilterConfig | Format-List SCL*

Use the Exchange Management Shell to configure
the rejection response for content filtering

<!-- p.2941 -->

When the Reject action is enabled, you can customize the rejection response that's sent to the
message sender. The rejection response can't exceed 240 characters.

To configure a custom rejection response, use the following syntax:

  Set-ContentFilterConfig -RejectionResponse "<Custom Text>"

This example configures the Content Filter agent to send a customized rejection response.

  Set-ContentFilterConfig -RejectionResponse "Your message was rejected because it
  appears to be SPAM."

How do you know this worked?
To verify that you have successfully configured the rejection response, run the following
command to verify the property values:

  Get-ContentFilterConfig | Format-List *Reject*

Use the Exchange Management Shell to enable or
disable Outlook Email Postmarking
Outlook Email Postmarking validation is a computational proof that Microsoft Outlook applies
to outgoing messages to help messaging systems distinguish legitimate email from junk email
(reduce false positives). Postmarking was first introduced in Outlook 2007, and is enabled in
Outlook by default.

To disable Outlook Email Postmarking, run the following command:

  Set-ContentFilterConfig -OutlookEmailPostmarkValidationEnabled $false

To enable Outlook Email Postmarking, run the following command:

<!-- p.2942 -->

  Set-ContentFilterConfig -OutlookEmailPostmarkValidationEnabled $true

How do you know this worked?
To verify that you have successfully configured Outlook Email Postmarking, run the following
command to verify the OutlookEmailPostmarkValidationEnabled property value:

  Get-ContentFilterConfig | Format-List OutlookEmailPostmarkValidationEnabled

<!-- p.2943 -->

Safelist aggregation
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

In Exchange Server, safelist aggregation refers to sender and recipient email addresses that are
collected from all users' Junk Email options in Microsoft Outlook, Outlook on the web, or the
Set-MailboxJunkEmailConfiguration cmdlet, and shared with the built-in Exchange antispam
agents. Safelist aggregation is basically unchanged from Exchange Server 2010.

When you enable and configure safelist aggregation, Exchange can take the following actions
based on the safelist aggregation data:

      Deliver incoming messages from senders that have been identified as safe without
      additional antispam processing (which could potentially identify the messages as spam).

      Block incoming messages from senders that have been identified as malicious.

To configure safelist aggregation, see Safelist aggregation procedures.

In the context of spam filtering, a false-positive is a legitimate message that's identified as
spam. For organizations that filter hundreds of thousands of messages from the Internet every
day, even a small percentage of false-positives means that users might not receive many
legitimate messages. Safelist aggregation is likely the most effective way to reduce false-
positives.

Information stored in the user's safelist collection
A safelist collection is the combined data from the user's Safe Senders list, Safe Recipients list,
Blocked Senders list, and (optionally) external contacts. This data is stored in Outlook and in
the Exchange mailbox. For more information about adding and removing entries from a user's
safelist collection, see Use the Exchange Management Shell to configure the safelist collection
on a mailbox.

The following information is stored in a user's safelist collection:

      Safe senders: The SMTP email address in the From: field.

      Safe recipients: The SMTP email address in the To: field.

      Blocked senders: Just like safe senders, users can block unwanted senders by adding
      them to their Blocked Senders list.

<!-- p.2944 -->

     Safe domain: This is part of the Safe Senders list, but instead of an SMTP email address
     (masato@contoso.com), the domain of the sender is specified (lcontoso.com).

     Note: By default, Exchange doesn't include safe domains during safelist aggregation.
     However, you can configure safelist aggregation to include the safe domain data. For
     more information, see Configure Content Filtering to Use Safe Domain Data.

     External contacts: Two types of external contact information can be included in the
     safelist collection:

        Recipients that the user has sent mail to: These email address are added to the Safe
        Senders list if the user selects Automatically add people I e-mail to the Safe Senders
        list in the Junk Email options in Outlook.

        Contacts in the user's Contacts folder: These email address are added to the Safe
        Senders list if the user selects Also trust e-mail from my Contacts in the Junk Email
        options in Outlook, Outlook on the web, or the Set-MailboxJunkEmailConfiguration
        cmdlet.

How Exchange uses the safelist collection
The safelist collection is stored on the user's Mailbox server. A user can have up to 1,024
unique entries in a safelist collection. Exchange has a mailbox assistant, called the Junk Email
Options mailbox assistant, that monitors changes to the safelist collection for mailboxes on the
server. It then replicates these changes to Active Directory, where the safelist collection is
stored on each user object. The safelist collection is optimized for minimized storage and
replication. If you have a subscribed Edge Transport server in your perimeter network, the
Microsoft Exchange EdgeSync service replicates the safelist collection to the Active Directory
Lightweight Directory Services (AD LDS) instance on the Edge Transport server.

The following Exchange antispam agents use the safelist collection:

     The Content Filter agent uses the Safe Senders list data to deliver messages from those
     senders without additional (unnecessary) processing.

     The Sender Filter agent uses the Blocked Senders list data to reject or delete messages
     from those senders. For more information, see Sender filtering procedures.

Note:Although the Safe Recipients list can be included in safelist aggregation, the Content
Filter agent doesn't act on safe recipient data.

Hashing of safelist collection entries

<!-- p.2945 -->

Safelist collection entries are hashed (SHA-256) one way before they are stored as array sets
across three user object attributes, msExchSafeSenderHash, msExchSafeRecipientHash, and
msExchBlockedSendersHash, as a binary large object. When data is hashed, an output of fixed
length is produced, and the output is likely to be unique. For hashing of safelist collection
entries, a 4-byte hash is produced. When a message is received from the Internet, Exchange
hashes the sender's email address and compares it to the hashes that are stored on behalf of
the destination mailbox. If the sender matches the safe senders hash, the message bypasses
content filtering. If the sender matches the blocked senders hash, the message is blocked.

One-way hashing of safelist collection entries performs the following important functions:

     Minimizes storage and replication space: Most of the time, hashing reduces the size of
     the data. Therefore, saving and transmitting a hashed version of a safelist collection entry
     conserves storage space and replication time. For example, a user who has 200 entries in
     his or her safelist collection would create about 800 bytes of hashed data stored and
     replicated in Active Directory.

     Renders user safelist collections unusable by malicious users: Because one-way hash
     values are impossible to reverse-engineer into the original SMTP address or domain, the
     safelist collections don't yield usable email addresses for malicious users who might
     compromise an Exchange server.

Enabling safelist aggregation
Safelist aggregation is enabled by default. The safelist collection data is written to Active
Directory by the Junk Email Options mailbox assistant. Unlike previous versions of Exchange,
you don't need to manually run the Update-SafeList cmdlet to hash and write the safelist
collection data to Active Directory.

You can still manually run safelist aggregation by using the Update-Safelist cmdlet. However,
you need to be aware of the replication traffic that might be generated when you run this
command. Running Update-Safelist on multiple mailboxes where safelists are heavily used
might generate a significant amount of network traffic. We recommend that if you run the
command on multiple mailboxes, you should run the command during off-peak, non-business
hours.

The Update-SafeList cmdlet reads the safelist collection from the user's mailbox, hashes each
entry, sorts the entries for easy search, and then converts the hash to a binary attribute. Finally,
the Update-SafeList cmdlet compares the binary attribute that was created to any value stored
on the attribute. If the two values are identical, the Update-SafeList cmdlet doesn't update the
user attribute value with the safelist aggregation data. If the two attribute values are different,
the Update-SafeList cmdlet updates the safelist aggregation value.

<!-- p.2946 -->

For more information about using Update-SafeList, see Safelist aggregation procedures.

<!-- p.2947 -->

Safelist aggregation procedures
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

In Exchange Server, safelist aggregation refers to sender and recipient data that's collected
from all users' Junk Email options in Microsoft Outlook, Outlook on the web, or the Set-
MailboxJunkEmailConfiguration cmdlet and shared with the built-in Exchange antispam
agents. For more information, see Safelist aggregation.

You can use the procedures in this topic to:

      Configure limits on the number of safe senders and blocked senders that are stored for
      specific mailboxes.

      Manually run safelist aggregation

      Verify that safelist aggregation is working correctly.

For more information about adding and removing entries from a user's safelist collection, see
Use the Exchange Management Shell to configure the safelist collection on a mailbox.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Recipient Provisioning
      Permissions" section in the Recipients Permissions topic, and the "Antispam features"
      section in the Antispam and antimalware permissions topic.

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      By default, antispam features aren't enabled in the Transport service on a Mailbox server.
      Typically, you only enable the antispam features on a Mailbox server if your Exchange
      organization doesn't do any prior antispam filtering before accepting incoming messages.
      For more information, see Enable antispam functionality on Mailbox servers.

      Be aware of the replication traffic that might be generated when you run the Update-
      SafeList cmdlet. Running the command on multiple mailboxes where safelists are heavily
      used might generate a significant amount of network traffic. We recommend that if you

<!-- p.2948 -->

     run the command on multiple mailboxes, you should run the command during off-peak,
     non-business hours.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online       , or Exchange Online Protection .

Use the Exchange Management Shell to configure
the mailbox safelist collection limits
You can configure the maximum number of safe senders and blocked senders a user can
configure. By default, users can configure up to 5,000 safe senders and 500 blocked senders.

To configure the maximum number of safe senders and blocked senders, use the following
syntax:

  PowerShell

  Set-Mailbox <MailboxIdentity> -MaxSafeSenders <Integer> -MaxBlockedSenders
  <Integer>

This example configures the mailbox john@contoso.com to have a maximum of 2,000 safe
senders and 200 blocked senders.

  PowerShell

  Set-Mailbox john@contoso.com -MaxSafeSenders 2000 -MaxBlockedSenders 200

How do you know this worked?
To verify that you have successfully configured the mailbox safelist collection limits, replace
<MailboxIdentity> with the identity of the mailbox, and run the following command to verify
the mailbox property values.

  PowerShell

<!-- p.2949 -->

  Get-Mailbox <MailboxIdentity> | Format-List Name,Max*Senders

Use the Exchange Management Shell to manually
run safelist aggregation
Safelist aggregation is done automatically, so you don't need to schedule or manually run the
Update-Safelist cmdlet. However, you may want to occasionally run this cmdlet to test safelist
aggregation.

To manually run safelist aggregation, use the following syntax:

  PowerShell

  Update-Safelist <MailboxIdentity> [-Type <SafeSenders | SafeRecipients | Both>] [-
  IncludeDomains]

This example writes the Safe Senders List for the mailbox john@contoso.com to Active
Directory.

  PowerShell

  Update-Safelist john@contoso.com

For detailed syntax and parameter information, see Update-SafeList.

Notes:

     You don't need to use the Type parameter because:

         The default value is SafeSenders .

         The Content Filter agent doesn't use Safe Recipients list data, so the SafeRecipients or
         Both values are unnecessary.

     By default, safelist aggregation doesn't include domain entries from the Safe Senders list
     (just email addresses), but you can configure it to include domain entries from the safelist
     collection. For more information, see Configure Content Filtering to Use Safe Domain
     Data.

How do you know this worked?

<!-- p.2950 -->

To verify that you have successfully configured safelist aggregation, perform the following
steps:

Step 1: Use the Exchange Management Shell to verify the
Content Filter agent is enabled on the Exchange server
Run the following command:

  PowerShell

  Get-ContentFilterConfig | Format-List Enabled

If the output shows the Enabled property to be True , content filtering is enabled. If it isn't, run
the following command to enable content filtering and the Content Filter agent on the
Exchange server:

  PowerShell

  Set-ContentFilterConfig -Enabled $true

Step 2: (Optional) Use ADSI Edit to verify replication of the
safelist aggregation data to Edge Transport servers
This step is only required if you run the Content Filter agent on a subscribed Edge Transport
server in your perimeter network.

You can view the user objects in the Active Directory Lightweight Directory Services (AD LDS)
instance on the Edge Transport server to:

     Verify that the safelist collection data is updated for the user objects.

     Verify that the Microsoft Exchange EdgeSync service has replicated the data to the AD
     LDS instance.

There are three safelist collection attributes for each user object:

     msExchSafeRecipientsHash: Stores the hash of the Safe Recipients List collection for the
     user.

     msExchSafeSendersHash: Stores the hash of the Safe Senders List collection for the user.

     msExchBlockedSendersHash: Stores the hash of the Blocked Senders List collection for
     the user.

<!-- p.2951 -->

If a hexadecimal string, such as 0xac 0xbd 0x03 0xca , is present on the attribute, the user
object was updated. If the attribute has a value of <Not Set> , the attribute wasn't updated.

You can search for and view the attributes by using ADSI Edit on the Edge Transport server (run
ADSIEdit.msc).

Step 3: Send a test message to verify safelist aggregation is
working
To test whether safelist aggregation is functioning, you need to send yourself a message from a
safe sender that would otherwise be blocked by content filtering (for example, the message
contains a blocked phrase). If safelist aggregation is functioning, the message should arrive in
your Inbox.

   1. Open your Exchange mailbox in Outlook, and add an external email address (associated
     with an account that you can access) to your Safe Senders List. For more information, see
     Add names to the Junk Email Filter lists   .

   2. Use the Update-SafeList cmdlet to manually replicate the safelist collection from your
     mailbox to Active Directory:

        PowerShell

        Update-Safelist <YourMailboxIdentity>

   3. Optional: if you're running the Content Filter agent on a subscribed Edge Transport server
     in the perimeter network, run the Start-EdgeSynchronization cmdlet to force EdgeSync
     replication.

   4. Add a specific word as a blocked phrase to your content filtering configuration. For
     example:

        PowerShell

        Add-ContentFilterPhrase -Influence BadWord -Phrase "SafeList aggregation
        test"

     For details, see Use the Exchange Management Shell to configure allowed and blocked
     phrases for content filtering.

   5. From the external email account in step 1, send a message to your Exchange mailbox that
     includes the blocked phrase that you configured in step 4.

<!-- p.2952 -->

If the message is successfully delivered to your Inbox, safelist aggregation is working
correctly.

<!-- p.2953 -->

Spam quarantine in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Many organizations are bound by legal or regulatory requirements to preserve or deliver all
legitimate email messages. In Exchange Server, spam quarantine is a feature of the Content
Filter agent that reduces the risk of losing legitimate incoming email messages by providing a
temporary storage location for messages that are identified as spam. Spam quarantine is
basically unchanged from Exchange Server 2010.

Messages that are identified as spam by the Content Filter agent are wrapped in a non-delivery
report (also known as an NDR, delivery status notification, DSN, or bounce message) and
delivered to the designated spam quarantine mailbox inside the organization. Administrators
can use Microsoft Outlook to review the messages in the spam quarantine mailbox and take
appropriate action. For example, you can delete messages, or release legitimate messages to
their intended recipients. In addition, you can configure the spam quarantine mailbox to
automatically delete messages after a designated time period.

To use the spam quarantine, follow these steps:

   1. Verify content filtering is enabled.

   2. Create a dedicated mailbox for spam quarantine.

   3. Specify the spam quarantine mailbox.

   4. Configure the SCL quarantine threshold.

   5. Manage the spam quarantine mailbox.

   6. Adjust the SCL quarantine threshold as needed.

For detailed instructions, see Configure a spam quarantine mailbox.

More information
The Content Filter agent evaluates incoming messages and applies a spam confidence level
(SCL) to each message. The SCL is a numeric value from 0 through 9, where 0 is considered
very unlikely to be spam, and 9 is considered very likely to be spam. You can configure the
Content Filter agent to take progressively more serious action based on a higher SCL value. For
example:

      SCL is 8 or higher: Silently delete the message.

<!-- p.2954 -->

     SCL is 7: Reject the message with an NDR.

     SCL is 6: Quarantine the message.

     SCL is 5: Deliver the message to the user's Junk Email folder.

     SCL is 4 or lower: Deliver the message to the user's Inbox.

For more information, see Exchange spam confidence level (SCL) thresholds.

As you monitor the spam quarantine mailbox, you can view the results of antispam filtering by
inspecting the antispam stamps (X-header fields) that were applied to the message. For more
information, see View antispam stamps in Outlook. You can then adjust the SCL thresholds to
more accurately filter the spam that's coming into your organization. For example:

     Too many legitimate messages are sent to the spam quarantine mailbox (too many false
     positives).

     Too many obvious spam messages are sent to the quarantine mailbox (not enough spam
     is rejected or deleted).

To release a false positive from the spam quarantine to the intended recipient, see the
following topics:

     Configure Outlook to show the original sender in the spam quarantine mailbox

     Release quarantined messages from the spam quarantine mailbox

<!-- p.2955 -->

Configure a spam quarantine mailbox in
Exchange Server
APPLIES TO:      2016      2019     Subscription Edition

Messages determined to be spam by the Content Filter agent can be directed to a spam
quarantine mailbox. If the spam confidence level (SCL) quarantine threshold is enabled, all
messages that are quarantined are wrapped as non-delivery reports (also known as NDRs,
delivery status notifications, DSN, or bounce messages) and are delivered to the spam quarantine
mailbox that you specify. Administrators can review quarantined messages and release them to
their intended recipients by using Microsoft Outlook.

What do you need to know before you begin?
     Estimated time to complete this task: 30 minutes.

     By default, antispam features aren't enabled in the Transport service on a Mailbox server.
     Typically, you only enable the antispam features on a Mailbox server if your Exchange
     organization doesn't do any prior antispam filtering before accepting incoming messages.
     For more information, see Enable antispam functionality on Mailbox servers.

     The person that's responsible for the spam quarantine mailbox can view potentially private
     and sensitive messages, and then send mail on behalf of anybody in the Exchange
     organization.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server
  | Management.

Step 1: Verify content filtering is enabled
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Antispam features" entry in the Antispam and

<!-- p.2956 -->

antimalware permissions topic.

   1. Run the following command to verify that the Content Filter agent is installed and enabled
     on the Exchange server:

       PowerShell

       Get-TransportAgent "Content Filter Agent"

   2. Run the following command to verify content filtering is enabled:

       PowerShell

       Get-ContentFilterConfig | Format-List Enabled

For more information, see Content filtering procedures.

Step 2: Create a dedicated mailbox for spam quarantine
To create a spam quarantine mailbox, follow these steps:

     Create a dedicated Exchange database: We recommend that you create a dedicated
     database for the spam quarantine mailbox. The spam quarantine mailbox should have a
     large database, because if the storage quota limit is reached, messages will be lost. For
     more information, see Manage mailbox databases in Exchange Server.

     Create a dedicated mailbox and user account: We recommend that you create a dedicated
     mailbox and user account for the spam quarantine mailbox. For more information, see
     Create user mailboxes in Exchange Server.

     You can apply recipient policies, such as messaging records management, mailbox quotas,
     and delegation rights, according to your organization's compliance policies and needs. For
     more information, see Messaging records management in Exchange Server.

       ７ Note

       If a quarantined message is rejected because of a storage quota, the message will be
       lost. Exchange doesn't generate NDRs for quarantined messages because the
       quarantined messages are wrapped as NDRs.

<!-- p.2957 -->

     Configure Outlook: You need to configure the Outlook delegate access permissions to
     meet the needs of your organization. In addition, you can configure the Outlook profile to
     show the original sender, recipient, and SCL value of the message. For more information,
     see Configure Outlook to show the original sender in the spam quarantine mailbox.

Step 3: Specify the spam quarantine mailbox
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Antispam features" entry in the Antispam and
antimalware permissions topic.

Use the following syntax:

 PowerShell

 Set-ContentFilterConfig -QuarantineMailbox <SmtpAddress>

This example sends all messages that exceed the spam quarantine threshold to
spamQ@contoso.com.

 PowerShell

 Set-ContentFilterConfig -QuarantineMailbox spamQ@contoso.com

How do you know this step worked?
To verify that you have successfully specified the spam quarantine mailbox, run the following
command to verify the value of the QuarantineMailbox property:

 PowerShell

 Get-ContentFilterConfig | Format-List QuarantineMailbox

Step 4: Configure the SCL quarantine threshold
The SCL quarantine threshold is the SCL value that redirects a message to the spam quarantine
mailbox. You can set the SCL quarantine threshold to a value from 0 through 9, where 0 is
considered less likely to be spam, and 9 is considered most likely to be spam.

For more information about how to adjust SCL thresholds to suit your organization's
requirements, and how to configure per-mailbox SCL thresholds, see Use the Exchange

<!-- p.2958 -->

Management Shell to configure SCL thresholds for content filtering and Use the Exchange
Management Shell to configure the SCL thresholds on a mailbox.

Step 5: Manage the spam quarantine mailbox
When you manage your spam quarantine mailbox, follow these guidelines:

     Use Resend this message in Outlook to release quarantined messages to their intended
     recipients. For more information, see Release quarantined messages from the spam
     quarantine mailbox.

     Monitor the size of the spam quarantine mailbox. The volume of email messages can
     change because of a large influx of new employees, the natural trend of larger message
     sizes, or the threshold value on the SCL quarantine action.

     Monitor the spam quarantine mailbox for false positives. If your spam quarantine mailbox
     includes many false positives, increase your SCL quarantine threshold. For more information
     about how to determine why false positives are being delivered to the spam quarantine
     mailbox, see View antispam stamps in Outlook.

     Use the same Outlook profile to view and release quarantined messages from the spam
     quarantine mailbox. Applying permissions to a different Outlook profile to release messages
     isn't supported.

  ） Important

  NDRs for quarantined messages aren't delivered to the spam quarantine mailbox. NDRs that
  are identified as spam are deleted, even if their SCL value indicates that they should be
  quarantined. To track these messages, use the agent log or the message tracking log. For
  more information, see Antispam Agent Logging.

Step 6: Adjust the SCL quarantine threshold
After you configure the SCL quarantine threshold, periodically monitor the settings and adjust
them based on your organization's needs. For example, if too many false positives are delivered
to the spam quarantine mailbox, raise the SCL quarantine threshold to a larger value. For more
information about how to adjust the SCL quarantine threshold, see Use the Exchange
Management Shell to configure SCL thresholds for content filtering.

<!-- p.2959 -->

Last updated on 04/30/2025

<!-- p.2960 -->

Configure Outlook to show the original
sender in the spam quarantine mailbox
APPLIES TO:      2016      2019      Subscription Edition

Spam quarantine is a feature of the Content Filter agent that reduces the risk of losing legitimate
messages. Spam quarantine provides a temporary storage location for messages that are
identified as spam and that shouldn't be delivered to a user mailbox inside the organization. For
more information, see Spam quarantine in Exchange Server.

When a message meets the spam quarantine threshold, it's wrapped in a non-delivery report
(also known as an NDR, delivery status notification, DSN, or bounce message) and delivered to
the spam quarantine mailbox. Because the quarantined messages are stored as NDRs, the
postmaster address of your organization will be listed as the From: address for all messages.
However, having the original sender address, the original recipient address, and the original spam
confidence level (SCL) in the field list would make it easier to locate the message you want to
recover.

By default, you can't add these fields in the message view in Microsoft Outlook. You need to
create an Outlook form that adds the original sender, original recipient, and original SCL as
optional fields that you can select. After you create this custom form, you can configure Outlook
to display these fields in the message view.

What do you need to know before you begin?
     Estimated time to complete this procedure: 15 minutes.

     You need to be assigned permissions before you can perform this procedure or procedures.
     To see what permissions you need, see the "Mailbox access" entry in the Mail flow
     permissions topic.

     This procedure requires that you've configured the quarantine mailbox. For more
     information, see Configure a spam quarantine mailbox.

     You need to configure an Outlook profile that you use to access the spam quarantine
     mailbox. For more information about configuring and using multiple Outlook profiles, see
     Overview of Outlook e-mail profiles       .
