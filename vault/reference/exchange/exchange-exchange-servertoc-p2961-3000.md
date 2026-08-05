---
title: "Exchange Server — pages 2961-3000"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2961-3000
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2961-3000
family: exchange
documentKind: "doc"
abstract: "You can use MAPI utilities (for example, OutlookSpy or MFCMAPI) to find the MAPI properties in a quarantined message that contain the original sender, recipient, and SCL values. If you find that other MAPI properties give better results than the ones identified in this topic, yo"
---

# Exchange Server — pages 2961-3000

<!-- p.2961 -->

   You can use MAPI utilities (for example, OutlookSpy or MFCMAPI) to find the MAPI
   properties in a quarantined message that contain the original sender, recipient, and SCL
   values. If you find that other MAPI properties give better results than the ones identified in
   this topic, you can use them in the custom Outlook form.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server
 | Management.

Step 1: Use Notepad to create a custom Outlook form
 1. Open Notepad, and copy the following code into the document.

     text

     [Description]
     MessageClass=IPM.Note
     CLSID={00020D31-0000-0000-C000-000000000046}
     DisplayName=Quarantine Extension Form
     Category=Standard
     Subcategory=Form
     Comment=This form allows the Original Sender (ReceivedRepresentingEmailAddress),
     Original Recipient (To), and Original SCL (OriginalScl) values to be viewed as
     columns.
     LargeIcon=IPML.ico
     SmallIcon=IPMS.ico
     Version=3.0
     Locale=enu
     Hidden=1
     Owner=Microsoft Corporation
     Contact=Your Name
     [Platforms]
     Platform1=Win16
     Platform2=NTx86
     Platform9=Win95
     [Platform.Win16]
     CPU=ix86
     OSVersion=Win3.1
     [Platform.NTx86]
     CPU=ix86
     OSVersion=WinNT3.5
     [Platform.Win95]
     CPU=ix86

<!-- p.2962 -->

    OSVersion=Win95
    [Properties]
    Property01=ReceivedRepresentingEmailAddress
    Property02=DisplayTo
    Property03=OriginalScl
    [Property.ReceivedRepresentingEmailAddress]
    Type=31
    NmidInteger=0x0078
    DisplayName=ReceivedRepresentingEmailAddress
    [Property.DisplayTo]
    Type=31
    NmidInteger=0x0E04
    DisplayName=DisplayTo
    [Property.OriginalScl]
    Type=3
    NmidPropset={41F28F13-83F4-4114-A584-EEDB5A6B0BFF}
    NmidString=OriginalScl
    DisplayName=OriginalScl
    [Verbs]
    Verb1=1
    [Verb.1]
    DisplayName=&Open
    Code=0
    Flags=0
    Attribs=2
    [Extensions]
    Extensions1=1
    [Extension.1]
    Type=31
    NmidPropset={00020D0C-0000-0000-C000-000000000046}
    NmidInteger=1
    Value=1000000000000000

2. Save the file in your Office Forms folder using the following values:

        Path: <OfficeInstallPath>\<OfficeVersion>\Forms\<LCID>

        <OfficeInstallPath>:

           For 32-bit versions of Office on 32-bit versions of Microsoft Windows, or 64-bit
           versions of Office on 64-bit versions of Windows, the default path is C:\Program
           Files\Microsoft Office\root .

           For 32-bit versions of Office on 64-bit versions of Windows, the default path is
           C:\Program Files (x86)\Microsoft Office\root .

        <OfficeVersion>

           Outlook 2010: Office14

<!-- p.2963 -->

              Outlook 2013: Office15

              Outlook 2016: Office16

           <LCID>: This is your locale ID (LCID) value. For example, the LCID for US English is
           1033. For more information, see Language identifiers and OptionState Id values in
           Office.

           Name: For the rest of this procedure, assume the file is named QTNE.cfg . The name of
           the file isn't important, but be sure to save the file as QTNE.cfg and not QTNE.cfg.txt.

For example, for a 32-bit US English version of Outlook 2016 installed on a 64-bit version of
Windows, save the file as:

"C:\Program Files (x86)\Microsoft Office\root\Office16\Forms\1033\QTNE.cfg"

  ７ Note

  If Windows User Access Control (UAC) prevents you from saving the file in the correct
  location, save it first to a temporary location, and then copy it.

Step 2: Configure Outlook 2010 or later to use the
custom Outlook form
   1. Open the spam quarantine mailbox in Outlook on a client computer, and click File >
     Options > Advanced.

   2. In the Developers section, click Custom Forms.

   3. In the Options dialog box that opens, click Manage Forms.

   4. In the Forms Manager dialog box that opens, click Install. Browse to the location of the
     QTNE.cfg file, select it, and click Open. In the Form Properties dialog box, review the

     information, and then click OK to install the Quarantine Extension Form in your Personal
     Forms library.

   5. Back in the Forms Manager dialog box, click Close. Click OK twice to close the remaining
     dialog boxes and return to the main Outlook interface.

   6. In the Mail view of the Inbox, click View > Add columns.

<!-- p.2964 -->

   7. In the Show Columns dialog box that opens, in the Select available columns from drop-
      down list, scroll to the end of the list and select Forms.

   8. In the Select Enterprise forms for this folder dialog box that opens, in the Selected Forms
      field, select Message and click Remove. In the Personal Forms field, select Quarantine
      Extension Form, and then click Add. When you're finished, click Close.

   9. Back in the Show Columns dialog box, in the Available Columns section, select one or more
      of the following fields and click Add after each field you select.

            ReceivedRepresentingEmailAddress: Original sender

            DisplayTo: Original recipient (note that this appears as To after you add it)

            OriginalScl: Original SCL

            Use the Move Up or Move Down buttons to position the columns in the view. For best
            results, position the new fields after the Attachment field, and before the From field.
            When you're finished, click OK twice to return to the main Outlook interface.

How do you know this worked?
You know this procedure worked if you can see the original sender, original recipient, or original
SCL values for quarantined messages in the spam quarantine mailbox using Outlook.

 Last updated on 04/30/2025

<!-- p.2965 -->

Release quarantined messages from the
spam quarantine mailbox in Exchange
Server
07/22/2025

APPLIES TO:     2016      2019      Subscription Edition

After you configure the spam quarantine mailbox in Exchange Server, you can use Resend this
message in Microsoft Outlook to release quarantined messages to their intended recipients. To
configure the spam quarantine mailbox, see Configure a spam quarantine mailbox.

What do you need to know before you begin?
     Estimated time to complete this procedure: less than 5 minutes

     Resend this message isn't available in Outlook on the web. You need to configure an
     Outlook profile that you use to access the spam quarantine mailbox. For more
     information about configuring and using multiple Outlook profiles, see Overview of
     Outlook email profiles    .

     To make it easier to locate the message you that want to recover, you can create a
     custom Outlook form to show the original sender and recipients in the message view. For
     detailed steps, see Configure Outlook to show the original sender in the spam quarantine
     mailbox.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox access" entry in the Mail
     flow permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

<!-- p.2966 -->

Use Outlook 2010 or later to release a message
from the spam quarantine mailbox
   1. Open the spam quarantine mailbox in Outlook on a client computer.

   2. In the Mail view, find the message you want to recover in the Inbox, and then double-
     click the message to open it.

   3. In the Move section of the Ribbon, click Actions > Resend this Message.

   4. When the message opens, click Send to resend the message to the intended recipient.

Note: Resend this message doesn't work on multiple messages. You need to resend them one
at a time.

How do you know this worked?
To verify that you have successfully released the message from the spam quarantine mailbox,
contact the recipient and verify that they received the message.

<!-- p.2967 -->

Exchange spam confidence level (SCL)
thresholds
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

  ７ Note

  In November, 2016, Microsoft stopped producing spam definition updates for the
  SmartScreen filters in Exchange and Outlook. The existing SmartScreen spam definitions
  were left in place, but their effectiveness will likely degrade over time. For more
  information, see Deprecating support for SmartScreen in Outlook and Exchange            .

In Exchange Server, you can define specific actions for messages according to spam confidence
level (SCL) thresholds. For example, you can define different thresholds for rejecting, deleting,
or quarantining messages on an Exchange server that's running the Content Filter agent. These
SCL thresholds and actions are basically unchanged from Exchange Server 2010

The Content Filter agent assigns an SCL rating to messages late in the antispam cycle, after the
other antispam agents have processed inbound messages. Many of the other antispam agents
that process inbound messages before the Content Filter agent are absolute in how they act on
a message. For example, the Connection Filtering agent on an Edge Transport server rejects
messages from IP addresses based on a real-time block list. Similarly, the Sender Filter agent
blocks messages based on a list of blocked senders, and the Recipient Filter agent blocks
messages based on a list of blocked recipients. By processing messages first, the other
antispam agents greatly reduce the number of messages (in most cases, blatantly unwanted
messages) that need to be processed by the Content Filter agent. For more information about
the order that antispam agents process messages in, see Antispam protection in Exchange
Server.

Because content filtering isn't an exact science, it's important to be able to adjust the actions of
the Content Filter agent based on different SCL values. By carefully monitoring and adjusting
the SCL thresholds, you can minimize the following conditions:

      The number of messages in and the size of the spam quarantine mailbox.

      The number of legitimate email messages that are mistakenly quarantined or placed in
      the user's Junk Email folder (false positives).

      The number of offensive spam email messages that reach the user's mailbox (messages
      shouldn't even reach the Junk Email folder).

<!-- p.2968 -->

     The number of spam email messages that reach the user's Inbox.

The combination of this SCL thresholds in the Content Filter agent and the SCL Junk Email
folder threshold on the user's mailbox helps you implement a more comprehensive and precise
antispam strategy, which can help you reduce the overall cost of deploying and maintaining an
antispam solution across your Exchange organization.

SCL threshold actions
By adjusting SCL threshold actions, you can escalate the content filtering action taken on
messages that have a greater probability of being spam. To understand this functionality, it's
helpful to understand the different SCL threshold actions and how they're implemented:

     SCL delete threshold: When the message's SCL value is greater than or equal to the SCL
     delete threshold, the Content Filter agent silently deletes the message. There's no
     protocol-level communication that tells the source messaging server or sender that the
     message was deleted. If the message's SCL value is lower than the SCL delete threshold,
     the Content Filter agent compares the SCL value to the SCL reject threshold.

     SCL reject threshold: When the message's SCL value is greater than or equal to the SCL
     reject threshold, but less than the SCL delete threshold, the Content Filter agent rejects
     the message and sends a rejection response to the sending system. You can customize
     the rejection response. In some cases, a non-delivery report (also known as an NDR,
     delivery status notification, DSN, or bounce message) is sent to the original sender of the
     message. If the message's SCL value is lower than the SCL reject threshold, the Content
     Filter agent compares the SCL value to the SCL quarantine threshold.

     SCL quarantine threshold: When the message's SCL value is greater than or equal to the
     SCL quarantine threshold, but less than the SCL reject threshold, the Content Filter agent
     sends the message to the spam quarantine mailbox. For more information about the
     configuring the spam quarantine mailbox, see Configure a spam quarantine mailbox.

     Administrators need periodically review the spam quarantine mailbox to verify that too
     much obvious spam isn't unnecessarily quarantined (the SCL quarantine threshold is too
     high), and that too much legitimate email isn't quarantined (the SCL quarantine threshold
     is too low). To view the results of antispam tests on quarantined messages, see View
     antispam stamps in Outlook.

     If the message's SCL value is lower than the SCL quarantine threshold, the message is
     delivered to the appropriate Mailbox server, where the organization's or mailbox's SCL
     Junk Email folder threshold is evaluated.

<!-- p.2969 -->

     SCL Junk Email folder threshold: If the message's SCL value is greater than the SCL Junk
     Email folder threshold that's configured for the organization or on the mailbox, the
     message is delivered to the Junk Email folder. If the message's SCL value is equal to or
     lower than the Junk Email folder threshold, the message is delivered to the Inbox.

     Unlike the other SCL thresholds that are controlled by the Content Filter agent, the SCL
     Junk Email folder threshold is controlled by the junk email rule (a hidden Inbox rule
     named Junk E-mail Rule) that's enabled by default in every mailbox. The Content Filter
     agent assigns the SCL value to a message, but the Junk E-mail Rule is responsible for
     delivering the message to the Junk Email folder. For more information, see Use the
     Exchange Management Shell to enable or disable the junk email rule in a mailbox.

The Content Filter agent and the Junk Email folder process the SCL threshold value differently.
The Content Filter agent uses greater than or equal to for the SCL threshold value, but the Junk
Email folder uses greater than. For example, if you configure the Content Filter agent with an
SCL delete threshold of 8, all messages with an SCL of 8 or higher are silently deleted. However,
if you configure the Junk Email folder with an SCL threshold of 4, all messages with an SCL of 5
or higher are moved to the Junk Email folder, while messages with an SCL of 4 or lower are
delivered to the Inbox.

Scope of SCL thresholds
You can configure the SCL thresholds in the following locations:

     Server configuration: The SCL delete, reject, and quarantine thresholds on the Content
     Filter agent.

     Organization configuration: The SCL Junk Email folder threshold value on the Exchange
     organization.

     Mailbox configuration: The SCL thresholds on specific mailboxes.

SCL thresholds on the Content Filter agent
You use the Set-ContentFilterConfig cmdlet to configure the SCL delete, reject, and quarantine
thresholds on an Edge Transport server or Mailbox server where you're running the Content
Filter agent. Over time, as you analyze the spam functionality and metrics provided by the
antispam logging and reporting features, you can make additional adjustments to these SCL
thresholds as needed.

The SCL threshold parameters that are available on the Set-ContentFilterConfig cmdlet are
described in the following table.

<!-- p.2970 -->

                                                                                         ﾉ   Expand table

 Parameter                Description

 SCLDeleteEnabled         Enables and disables the SCL delete threshold. Valid values are $true or
                          $false . The default value is $false , which means the SCL delete threshold
                          isn't enabled by default.
                          You set the SCL delete threshold value with the SCLDeleteThreshold parameter.

 SCLDeleteThreshold       The SCL value that's used when the SCL delete threshold is enabled. A
                          message with an SCL value that's greater than or equal to this value is silently
                          deleted. The maximum value is 9, which is also the default value.
                          When you enable the SCL delete threshold, this value should be greater than
                          all other SCL thresholds.

 SCLRejectEnabled         Enables and disables the SCL reject threshold. Valid values are $true or
                          $false . The default value is $true , which means the SCL reject threshold is
                          enabled by default.
                          You set the SCL reject threshold value with the SCLRejectThreshold parameter.

 SCLRejectThreshold       The SCL value that's used when the SCL reject threshold is enabled. A message
                          with an SCL value that's greater than or equal to this value is rejected, and an
                          NDR is sent to the sender. The maximum value is 9, and the default value is 7.
                          When you enable the SCL reject threshold, this value should be less than the
                          SCL delete threshold, but greater than the SCL quarantine and Junk Email
                          folder thresholds.

 SCLQuarantineEnabled     Enables and disables the SCL quarantine threshold. Valid values are $true or
                          $false . The default value is $false , which means the SCL quarantine threshold
                          isn't enabled by default.
                          You set the SCL quarantine threshold value with the SCLQuarantineThreshold
                          parameter.
                          For more information about the configuring the spam quarantine mailbox
                          that's required to quarantine messages, see Configure a spam quarantine
                          mailbox.

 SCLQuarantineThreshold   The SCL value that's used when the SCL quarantine threshold is enabled. A
                          message with an SCL value that's greater than or equal to this value is
                          redirected to the spam quarantine mailbox. The maximum value is 9, which is
                          also the default value.
                          When you enable the SCL quarantine threshold, this value should be less than
                          the SCL reject threshold, but greater than the SCL Junk Email folder threshold
                          (the SCLJunkThreshold parameter on the Set-OrganizationConfig or Set-
                          Mailbox cmdlets).

For examples of configuring the SCL thresholds on the Content Filter agent, see Use the
Exchange Management Shell to configure SCL thresholds for content filtering.

SCL thresholds on the organization

<!-- p.2971 -->

You use the SCLJunkThreshold parameter Set-OrganizationConfig cmdlet to set the SCL Junk
Email folder threshold value for all mailboxes in the organization. This is the only SCL threshold
that you can configure at the organization level. The SCL value is typically assigned to
messages by the Content Filter agent.

The SCLJunkThreshold parameter on the Set-OrganizationConfig cmdlet is described in the
following table.

                                                                                        ﾉ   Expand table

 Parameter          Description

 SCLJunkThreshold   The SCL value that's used when the junk email rule is enabled in the mailbox, and an
                    SCL Junk Email folder threshold isn't configured on the mailbox.
                    A message with an SCL value that's greater than this value is moved to the Junk Email
                    folder by the junk email rule. The maximum value is 9, and the default value is 4,
                    which means that messages with an SCL value of 5 or higher are moved to the Junk
                    Email folder, and messages with an SCL value of 4 or lower are delivered to the Inbox.

Notes:

     The SCL Junk Email folder threshold is enabled by default, because the junk email rule is
     enabled by default in all mailboxes. If the junk email rule is disabled in the mailbox, the
     SCL Junk Email folder threshold (for the organization or the mailbox) is disabled for the
     mailbox.

     You can disable the junk email rule in a mailbox by using the Enabled parameter on the
     Set-MailboxJunkEmailConfiguration cmdlet, but only after the mailbox has been opened
     in Outlook (in Cached Exchange mode) or Outlook on the web.

     You can control the availability of the junk email settings in Outlook on the web, which
     prevents users from enabling or disabling the junk email rule in their own mailbox.

For more information, see the Configure Exchange antispam settings on mailboxes topic.

SCL thresholds on a mailbox
You can use the Set-Mailbox cmdlet to configure all SCL thresholds on a mailbox. The same
SCL parameters that are available on the Set-ContentFilterConfig cmdlet are also available on
the Set-Mailbox cmdlet:

     SCLDeleteEnabled

     SCLDeleteThreshold

<!-- p.2972 -->

     SCLRejectEnabled

     SCLRejectThreshold

     SCLQuarantineEnabled

     SCLQuarantineThreshold

Unlike the SCL threshold parameters on Set-ContentFilterConfig, the parameters on the Set-
Mailbox cmdlet also accept the value $null (the value is blank), which is the default value for
all SCL thresholds on the mailbox. This blank default value indicates that no SCL thresholds are
configured on the mailbox, so the Content Filter agent uses its SCL threshold settings for
messages that are sent to the mailbox.

If you configure an SCL threshold on a mailbox (the value isn't blank), the setting override the
corresponding SCL threshold on the Content Filter agent for messages that are sent to the
mailbox. The SCL thresholds that you configure on the mailbox are stored in Active Directory,
and are replicated to subscribed Edge Transport servers by the Microsoft Exchange EdgeSync
service.

The results are similar for the SCLJunkThreshold parameter that's available on Set-
OrganizationConfig and Set-Mailbox: the SCL Junk Email folder threshold value that you
configure on the mailbox (the value isn't blank) overrides the SCL value on the organization for
messages that are sent to the mailbox.

  ７ Note

  SCL thresholds on a mailbox are not enforced for messages that are received from
  distribution groups.

The SCL threshold setting that's unique to a mailbox is the ability to enable or disable the SCL
Junk Email folder threshold. The SCLJunkEnabled parameter is only available on the Set-
Mailbox cmdlet, and is described in the following table.

                                                                                          ﾉ    Expand table

 Parameter        Description

 SCLJunkEnabled   Enables and disables the SCL Junk Email folder threshold on the mailbox. Valid values
                  are $true , $false , or $null (blank). The default value is blank ( $null ), which means
                  the SCL Junk Email folder threshold isn't configured on the mailbox, and is controlled
                  by whether the junk email rule is enabled or disabled in the mailbox.
                  The default SCL Junk Email folder threshold value is set by the SCLJunkThreshold

<!-- p.2973 -->

 Parameter        Description

                  parameter on the Set-OrganizationConfig cmdlet. You can override this value for the
                  mailbox by using the SCLJunkThreshold parameter on the Set-Mailbox cmdlet.

Notes:

     You can disable the SCL Junk Email folder threshold on a mailbox by disabling the junk
     email rule in the mailbox. However, disabling the rule also prevents the rule from using
     the mailbox's safelist collection (Safe Senders list, Safe Recipients list, Blocked Senders list)
     to move messages to the Junk Email folder, or keep messages out of the Junk Email
     folder.

     Even if the junk email rule is disabled in the mailbox, and the SCL Junk Email folder
     threshold is disabled on the mailbox, the client-side Outlook Junk Email Filter can still
     move messages to the Junk Email folder.

For more information, see the Configure Exchange antispam settings on mailboxes topic.

Monitoring the SCL thresholds
You can use several built-in scripts that are located in the %ExchangeInstallPath%Scripts folder,
such as Get-AntispamSCLHistogram.ps1, for gathering filtering result data. If the data indicates
that you need to make immediate adjustments, reconfigure the SCL thresholds. Otherwise,
collect data and analyze the spam reporting to determine whether adjustments are required.

<!-- p.2974 -->

Sender filtering in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Sender filtering compares a list of blocked senders that's maintained by the Exchange
administrator to the value of the MAIL FROM command in SMTP connections to determine
what to do with inbound email messages from those blocked senders. Sender filtering in
Exchange Server is provided by the Sender Filter agent, and is basically unchanged from
Exchange Server 2010.

You can configure the Sender Filter agent block single senders (for example,
kim@contoso.com), whole domains (contoso.com), or domains and all subdomains
(*.contoso.com). You can control whether the agent inspects messages from internal sources,
external sources, or both. You can also configure the action to take on messages from blocked
senders:

      Reject: The Sender Filter agent rejects the SMTP request with a 554 5.1.0 Sender Denied
      SMTP session error and closes the connection.

      Stamp status: The Sender Filter agent accepts the message and updates the message to
      indicate that it came from a blocked sender. The Content Filter agent uses this
      information when it calculates the spam confidence level (SCL) of the message. For more
      information about content filtering and the Content Filter agent, see Content filtering.

By default, the Sender Filter agent is enabled on Edge Transport servers, but you can enable it
on Mailbox servers. For more information, see Enable antispam functionality on Mailbox
servers.

For more information about how to configure the Sender Filter agent, see Sender filtering
procedures.

  ） Important

  The MAIL FROM: SMTP headers can be spoofed, so you shouldn't rely exclusively on the
  Sender Filter agent. Instead, you should use both the Sender Filter agent and the Sender
  ID agent. The Sender ID agent uses the originating IP address of the sending server to
  verify that the domain in the MAIL FROM: SMTP header matches the domain that's
  registered. For more information about the Sender ID agent, see Sender ID.

Using the Sender Filter agent to block messages

<!-- p.2975 -->

By default, the Sender Filter agent is configured to only inspect messages from external
sources. External sources are defined as unauthenticated sources. You can configure the Sender
Filter agent to inspect messages from internal (authenticated) sources. However, as best
practice, you typically don't need to apply antispam filters to messages from trusted partners
or from inside your organization.

You can also configure the Sender Filter agent to block inbound messages that don't specify a
sender and domain in the MAIL FROM SMTP command. This setting helps to prevent NDR
attacks on the Exchange server. Most legitimate SMTP messages come from SMTP servers that
provide a sender and domain in the MAIL FROM command.

Specify the action for messages from blocked
senders
After you've configured the blocked senders and the sources that are monitored by the Sender
Filter agent, you need to configure the Sender Filter agent to reject or accept and stamp
messages from those senders. We recommend that you reject the messages, because the
chance of false positives based on the specific list of blocked senders is much less than other
calculated message properties.

There are only two scenarios where a legitimate message might be rejected by the Sender
Filter agent:

     You mistype the blocked sender.

     The domain in your Blocked Senders list is later re-registered to a legitimate company.

<!-- p.2976 -->

Sender filtering procedures
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Sender filtering filters inbound messages by comparing a list of blocked senders to the value of
the MAIL FROM command in SMTP connections. For more information about sender filtering
and the Sender Filter agent, see Sender filtering.

You can configure many aspects of sender filtering. For example:

      Enable or disable sender filtering on inbound messages from internal (authenticated) and
      external (unauthenticated) sources (it's enabled by default for messages from external
      sources).

      Configure blocked senders and blocked domains.

      Specify whether to block messages with blank senders.

      Configure the action that sender filtering takes on messages that contain blocked senders
      or domains.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Antispam features" entry in the
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

<!-- p.2977 -->

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the Exchange Management Shell to enable or
disable sender filtering
To disable sender filtering, run the following command:

  PowerShell

  Set-SenderFilterConfig -Enabled $false

To enable sender filtering, run the following command:

  PowerShell

  Set-SenderFilterConfig -Enabled $true

  ７ Note

  When you disable sender filtering, the underlying Sender Filter agent is still enabled. To
  disable the Sender Filter agent, run the command: Disable-TransportAgent "Sender Filter
  Agent" .

How do you know this worked?
To verify that you have successfully enabled or disabled sender filtering, run the following
command to verify the Enabled property value:

  PowerShell

  Get-SenderFilterConfig | Format-List Enabled

Use the Exchange Management Shell to enable or
disable sender filtering for external connections
By default, sender filtering is enabled for external (unauthenticated) SMTP connections.

<!-- p.2978 -->

To disable sender filtering for external connections, run the following command:

  PowerShell

  Set-SenderFilterConfig -ExternalMailEnabled $false

To enable sender filtering for external connections, run the following command:

  PowerShell

  Set-SenderFilterConfig -ExternalMailEnabled $true

How do you know this worked?
To verify that you have successfully enabled or disabled sender filtering for external SMTP
connections, run the following command to verify the ExternalMailEnabled property value:

  PowerShell

  Get-SenderFilterConfig | Format-List ExternalMailEnabled

Use the Exchange Management Shell to enable or
disable sender filtering for internal connections
As a best practice, you don't need to apply antispam filters to messages from trusted partners
or from inside your organization. To reduce the chance that filters will mishandle legitimate
email messages, you typically configure antispam agents to only run on messages from
external sources.

To enable sender filtering for internal (authenticated) SMTP connections, run the following
command:

  PowerShell

  Set-SenderFilterConfig -InternalMailEnabled $true

To disable sender filtering for internal connections, run the following command:

  PowerShell

  Set-SenderFilterConfig -InternalMailEnabled $false

<!-- p.2979 -->

How do you know this worked?
To verify that you have successfully enabled or disabled sender filtering for internal SMTP
connections, run the following command to verify the InternalMailEnabled property value:

  PowerShell

  Get-SenderFilterConfig | Format-List InternalMailEnabled

Use the Exchange Management Shell to configure
blocked senders and domains for sender filtering
You can specify blocked senders and domains that replace the existing values, or you can add
or remove specific blocked senders and domains without affecting the other existing values.

To replace the existing values, use the following syntax:

  PowerShell

  Set-SenderFilterConfig -BlockedSenders <sender1,sender2...> -BlockedDomains
  <domain1,domain2...> -BlockedDomainsAndSubdomains <domain1,domain2...>

This example configures the Sender Filter agent to block messages from kim@contoso.com
and john@contoso.com, messages from the fabrikam.com domain, and messages from
northwindtraders.com and all its subdomains.

  PowerShell

  Set-SenderFilterConfig -BlockedSenders kim@contoso.com,john@contoso.com -
  BlockedDomains fabrikam.com -BlockedDomainsAndSubdomains northwindtraders.com

To add or remove entries without modifying other existing values, use the following syntax:

  PowerShell

  Set-SenderFilterConfig -BlockedSenders @{Add="<sender1>","<sender2>"...; Remove="
  <sender1>","<sender2>"...} -BlockedDomains @{Add="<domain1>","<domain2>"...;
  Remove="<domain1>","<domain2>"...} -BlockedDomainsAndSubdomains @{Add="
  <domain1>","<domain2>"...; Remove="<domain1>","<domain2>"...}

This example configures the Sender Filter agent with the following information:

<!-- p.2980 -->

     Add chris@contoso.com and michelle@contoso.com to the list of existing senders who
     are blocked.

     Remove tailspintoys.com from the list of existing sender domains that are blocked.

     Add blueyonderairlines.com to the list of existing sender domains and subdomains that
     are blocked.

  PowerShell

  Set-SenderFilterConfig -BlockedSenders
  @{Add="chris@contoso.com","michelle@contoso.com"} -BlockedDomains
  @{Remove="tailspintoys.com"} -BlockedDomainsAndSubdomains
  @{Add="blueyonderairlines.com"}

How do you know this worked?
To verify that you have successfully configured blocked senders, run the following command to
verify the property values:

  PowerShell

  Get-SenderFilterConfig | Format-List Blocked*

Use the Exchange Management Shell to configure
sender filtering to block messages with blank
senders
To enable or disable blocking messages that have blank senders, use the following syntax:

  PowerShell

  Set-SenderFilterConfig -BlankSenderBlockingenabled <$true | $false>

This example configures the Sender Filter agent to block messages that don't specify a sender
in the MAIL FROM: SMTP command:

  PowerShell

  Set-SenderFilterConfig -BlankSenderBlockingEnabled $true

<!-- p.2981 -->

How do you know this worked?
To verify that you have successfully enabled or disabled blocking messages with blank senders,
run the following command to verify the property value:

  PowerShell

  Get-SenderFilterConfig | Format-List BlankSenderBlockingEnabled

Use the Exchange Management Shell to configure
the action for sender filtering
Typically, you want to reject messages from blocked senders or domains, and this is the default
action. However, you can configure sender filtering to allow these message into your
organization for further analysis by other antispam agents.

To configure the action that sender filtering takes on messages from blocked senders or
domains, use the following syntax:

  PowerShell

  Set-SenderFilterConfig -Action <Reject | StampStatus>

This example configures the Sender Filter agent to allow messages from blocked senders or
domains. The Sender Filter agent updates the message to indicate that it came from a blocked
sender. This information is used in the calculation of the message's spam confidence level
(SCL).

  PowerShell

  Set-SenderFilterConfig -Action StampStatus

This example configures the Sender Filter agent to reject messages from blocked senders or
domains. The Sender Filter agent rejects the SMTP request with a 554 5.1.0 Sender Denied
SMTP session error and closes the connection.

  PowerShell

  Set-SenderFilterConfig -Action Reject

How do you know this worked?

<!-- p.2982 -->

To verify that you have successfully configured the action for sender filtering, run the following
command to verify the Action property value:

  PowerShell

  Get-SenderFilterConfig | Format-List Action

Use the Exchange Management Shell to configure
the action for sender filtering for blocked senders
from SafeList aggregation
SafeList aggregation adds blocked senders that are defined by your users in Microsoft Outlook
or Outlook on the web to the Blocked Senders list that's used by the Sender Filter agent. For
more information, see Safelist aggregation.

To configure the action that sender filtering takes on messages that contain blocked senders
that are defined by SafeList aggregation, use the following syntax:

  PowerShell

  Set-SenderFilterConfig -RecipientBlockedSenderAction <Delete | Reject>

This example configures the Sender Filter agent to silently drop messages that contain blocked
senders that are defined by SafeList aggregation.

  PowerShell

  Set-SenderFilterConfig -RecipientBlockedSenderAction Delete

This example configures the Sender Filter agent to reject messages that contain blocked
senders that are defined by SafeList aggregation with a non-delivery report (also known as an
NDR, delivery status notification, DSN or bounce message).

  PowerShell

  Set-SenderFilterConfig -RecipientBlockedSenderAction Reject

How do you know this worked?

<!-- p.2983 -->

To verify that you have successfully configured the action for sender filtering for blocked
senders from SafeList aggregation, run the following command to verify the
RecipientBlockedSenderAction property value:

  PowerShell

  Get-SenderFilterConfig | Format-List RecipientBlockedSenderAction

<!-- p.2984 -->

Sender ID in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Sender ID is used to detect spoofing. A spoofed email message is modified to appear as if it
originates from a sender other than the actual sender of the message. In the past, it was
relatively easy to send spoofed email messages, because the sender's email address in the
message header wasn't validated. Sender ID uses the RECEIVED SMTP header and a query to
the DNS records for the sender's domain to determine if the sender's email address is spoofed.
Sender ID in Exchange Server is provided by the Sender ID agent, and is basically unchanged
from Exchange Server 2010.

By default, the Sender ID agent is enabled on Edge Transport servers, but you can enable it on
Mailbox servers. For more information, see Enable antispam functionality on Mailbox servers.

For more information about how to configure the Sender ID agent, see Sender ID procedures.

Using Sender ID to combat spoofing
When the Exchange server receives an inbound message, the Sender ID agent verifies the
sender's IP address by querying the DNS records for the sender's domain. This check confirms
that the message was received from an authorized IP address for the sender's domain. The IP
address of the authorized sending server is referred to as the purported responsible address
(PRA).

Administrators publish sender policy framework (SPF) records in DNS that identify the
authorized outbound messaging servers for the domain. If an SPF record is available in DNS for
the sender's domain, the Sender ID agent parses the SPF record to determine if the source IP
address is authorized to send email for the domain that's specified in the sender's email
address. For more information about what an SPF record contains and how to create an SPF
record, see Sender Policy Framework: SPF Record Syntax .

Sender ID status values
The Sender ID agent generates a Sender ID status for the message. The Sender ID status can be
set to one of the following values:

      Pass: Both the IP address and the PRA passed the Sender ID verification check.

      Neutral: The published Sender ID data is explicitly inconclusive.

      Soft fail: The IP address for the PRA might be in the not permitted set.

<!-- p.2985 -->

     Fail: The IP Address is not permitted. No PRA is found in the incoming mail, or the
     sender's domain doesn't exist.

     None: No published SPF data exists in DNS for the sender's domain.

     TempError: A temporary DNS failure occurred, such as an unavailable DNS server.

     PermError: The DNS record is invalid, such as an error in the record format.

Note:: If the source IP address is missing, the Sender ID status can't be set. Exchange continues
to process the message without including a Sender ID status, and the message isn't returned or
rejected. In this scenario, the Sender ID status isn't set, and an application event is logged.

The Sender ID status is added to the message metadata, and is later converted to a MAPI
property. The junk email filter in Outlook uses this MAPI property during the calculation of the
spam confidence level (SCL).

Outlook neither displays the Sender ID status, nor flags a message as junk based solely on the
Sender ID value. Instead, Outlook uses the Sender ID status value only during the calculation of
the SCL for the message.

For more information about how the Sender ID status is displayed in messages, see Antispam
stamps.

Sender ID options for handling spoofed mail and unreachable
DNS servers
You can configure the actions to take when the Sender ID agent identifies messages that
contain spoofed senders (the Sender ID status is Fail ), and when a DNS server can't be
reached (the Sender ID status is TempError ):

     Stamp status: The Sender ID agent stamps the Sender ID status in the metadata of the
     message, and allows the delivery of the message to continue. This is the default option.

     Reject: The Sender ID agent rejects the message with a 5 xx level SMTP error response,
     which includes text that corresponds to the Sender ID status.

     Delete: The Sender ID agent silently deletes the message without an SMTP error
     response. The Exchange server sends a fake OK SMTP command to the source server, and
     then deletes the message. Because the source server assumes the message was sent, it
     doesn't try to resend the message in the same session.

For more information about how to configure the action to take for spoofed mail and
unreachable DNS servers, see Sender ID procedures.

<!-- p.2986 -->

Updating your organization's Internet facing DNS
to support Sender ID
The effectiveness of Sender ID depends on specific DNS data. The more organizations that
configure SPF records for their domains, the more effectively Sender ID is able to identify
spoofed messages.

To support the Sender ID infrastructure, you need to create SPF records for the domains that
your organization sends messages from. For more information about how to create and deploy
SPF records, see Sender Policy Framework: SPF Record Syntax      .

Specifying recipients and sender domains to
exclude from Sender ID filtering
You can exclude specific recipients and sender domains from Sender ID filtering by using the
Set-SenderIdConfig cmdlet in the Exchange Management Shell. For more information, see
Sender ID procedures.

<!-- p.2987 -->

Sender ID procedures
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

Sender ID detects spoofed email messages by using the Sender Policy Framework (SPF) record
in DNS to compare the source IP address with the domain in the sender's email address. For
more information about Sender ID and the Sender ID agent, see Sender filtering

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Antispam features" entry in the
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

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Use the Exchange Management Shell to enable or
disable Sender ID
To disable Sender ID, run the following command:

  PowerShell

<!-- p.2988 -->

  Set-SenderIDConfig -Enabled $false

To enable Sender ID, run the following command:

  PowerShell

  Set-SenderIDConfig -Enabled $true

  ７ Note

  When you disable Sender ID, the underlying Sender ID agent is still enabled. To disable
  the Sender ID agent, run the command: Disable-TransportAgent "Sender ID Agent" .

How do you know this worked?
To verify that you have successfully enabled or disabled Sender ID, run the following command
to verify the Enabled property value:

  PowerShell

  Get-SenderIDConfig | Format-List Enabled

Use the Exchange Management Shell to enable or
disable Sender ID for external connections
By default, Sender ID is enabled for external (unauthenticated) SMTP connections.

To disable sender filtering for external connections, run the following command:

  PowerShell

  Set-SenderIDConfig -ExternalMailEnabled $false

To enable Sender ID for external connections, run the following command:

  PowerShell

  Set-SenderIDConfig -ExternalMailEnabled $true

<!-- p.2989 -->

How do you know this worked?
To verify that you have successfully enabled or disabled Sender ID for external SMTP
connections, run the following command to verify the ExternalMailEnabled property value:

  PowerShell

  Get-SenderFilterConfig | Format-List ExternalMailEnabled

Use the Exchange Management Shell to enable or
disable Sender ID for internal connections
As a best practice, you don't need to apply antispam filters to messages from trusted partners
or from inside your organization. To reduce the chance that filters will mishandle legitimate
email messages, you typically configure antispam agents to only run on messages from
external sources.

To enable Sender ID for internal (authenticated) SMTP connections, run the following
command:

  PowerShell

  Set-SenderIDConfig -InternalMailEnabled $true

To disable Sender ID for internal connections, run the following command:

  PowerShell

  Set-SenderIDConfig -InternalMailEnabled $false

How do you know this worked?
To verify that you have successfully enabled or disabled Sender ID for internal SMTP
connections, run the following command to verify the InternalMailEnabled property value:

  PowerShell

  Get-SenderIDConfig | Format-List InternalMailEnabled

<!-- p.2990 -->

Use the Exchange Management Shell to configure
the Sender ID action for spoofed messages
To configure the Sender ID action for spoofed messages, use the following syntax:

  PowerShell

  Set-SenderIDConfig -SpoofedDomainAction <StampStatus | Reject | Delete>

This example configures the Sender ID agent to reject any messages with a 5 xx SMTP error
response when sender's domain has an SPF record, and the IP address of the source server isn't
listed as an authoritative server for the domain (the Sender ID status is Fail ).

  PowerShell

  Set-SenderIDConfig -SpoofedDomainAction Reject

How do you know this worked?
To verify that you have successfully configured the Sender ID action for spoofed messages, run
the following command to verify the SpoofedDomainAction property value:

  PowerShell

  Get-SenderIDConfig | Format-List SpoofedDomainAction

Use the Exchange Management Shell to configure
the Sender ID action for transient errors
To configure the Sender ID action for transient errors, use the following syntax:

  PowerShell

  Set-SenderIDConfig -TempErrorAction <StampStatus | Reject | Delete>

This example configures the Sender ID agent to stamp the messages when the Sender ID status
can't be determined due to a temporary DNS server error (the Sender ID status is TempError ).
The message will be processed by other antispam agents and the Content Filter agent will use
the mark when determining the SCL value for the message.

<!-- p.2991 -->

  PowerShell

  Set-SenderIDConfig -TempErrorAction StampStatus

Note that StampStatus is the default value for the TempErrorAction parameter.

How do you know this worked?
To verify that you have successfully configured the Sender ID action for transient errors, run the
following command to verify the TempErrorAction property value:

  PowerShell

  Get-SenderIDConfig | Format-List TempErrorAction

Use the Exchange Management Shell to configure
recipient and sender domain exceptions
To replace the existing values, run the following command:

  PowerShell

  Set-SenderIDConfig -BypassedRecipients <recipient1,recipient2...> -
  BypassedSenderDomains <domain1,domain2...>

This example configures the Sender ID agent to bypass the Sender ID check for messages sent
to kim@contoso.com and john@contoso.com, and to bypass the Sender ID check for
messages sent from the fabrikam.com domain.

  PowerShell

  Set-SenderIDConfig -BypassedRecipients kim@contoso.com,john@contoso.com -
  BypassedSenderDomains fabrikam.com

To add or remove entries without modifying other existing values, use the following syntax:

  PowerShell

  Set-SenderIDConfig -BypassedRecipients @{Add="<recipient1>","<recipient2>"...;
  Remove="<recipient1>","<recipient2>"...} -BypassedSenderDomains @{Add="
  <domain1>","<domain2>"...; Remove="<domain1>","<domain2>"...}

<!-- p.2992 -->

This example configures the Sender ID agent with the following settings:

     Add chris@contoso.com and michelle@contoso.com to the list of existing recipients who
     bypass the Sender ID check.

     Remove tailspintoys.com from the list of existing domains that bypass the Sender ID
     check.

  PowerShell

  Set-SenderIDConfig -BypassedRecipients
  @{Add="chris@contoso.com","michelle@contoso.com"} -BypassedSenderDomains
  @{Remove="tailspintoys.com"}

How do you know this worked?
To verify that you have successfully configured recipient and sender domain exceptions, run the
following command to verify the property values:

  PowerShell

  Get-SenderIDConfig | Format-List BypassedRecipients,BypassedSenderDomains

<!-- p.2993 -->

Sender reputation and the Protocol
Analysis agent in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Sender reputation is part of the Exchange antispam functionality that blocks messages
according to many characteristics of the sender. Sender reputation relies on persisted data
about the sender to determine the action to take on inbound messages. The Protocol Analysis
agent is the underlying agent for sender reputation functionality.

For more information about how to configure sender reputation and the Protocol Analysis
agent, see Sender reputation procedures.

By default, the Protocol Analysis agent is enabled on Edge Transport servers, but you can
enable it on Mailbox servers. For more information, see Enable antispam functionality on
Mailbox servers.

Calculating the sender reputation level (SRL)
A sender reputation level (SRL) is calculated from the following statistics:

      HELO/EHLO analysis: The HELO and EHLO SMTP commands are intended to provide the
      domain name, such as Contoso.com, or IP address of the sending SMTP server to the
      receiving SMTP server. Malicious users, or spammers, frequently forge the HELO/EHLO
      statement in various ways. For example, they type an IP address that doesn't match the IP
      address from which the connection originated. Spammers also put domains that are
      known to be locally supported at the receiving server in the HELO statement in an
      attempt to appear as if the domains are in the organization. In other cases, spammers
      change the domain that's passed in the HELO statement. The typical behavior of a
      legitimate user may be to use a different, but relatively constant, set of domains in their
      HELO statements.

      Therefore, analysis of the HELO/EHLO statement on a persender basis may indicate that
      the sender is likely to be a spammer. For example, a sender that provides many different
      unique HELO/EHLO statements in a specific time period is more likely to be a spammer.
      Senders who consistently provide an IP address in the HELO statement that doesn't match
      the originating IP address as determined by the Connection Filtering agent are also more
      likely to be spammers. Remote senders who consistently provide a local domain name in
      the HELO statement that's in the same organization as the Exchange server are also more
      likely to be spammers.

<!-- p.2994 -->

Reverse DNS lookup: Sender reputation also verifies that the originating IP address from
which the sender transmitted the message matches the registered domain name that the
sender submits in the HELO or EHLO SMTP command.

Sender reputation performs a reverse DNS query by submitting the originating IP address
to DNS. The result that's returned by DNS is the domain name that's registered by using
the domain naming authority for that IP address. Sender reputation compares the domain
name that's returned by DNS to the domain name that the sender submitted in the
HELO/EHLO SMTP command. If the domain names don't match, the sender is likely to be
a spammer, and the overall SRL rating for the sender is increased.

The Sender ID agent performs a similar task, but the success of the Sender ID agent relies
on legitimate senders to update their DNS infrastructure to identify all the email-sending
SMTP servers in their organization. By performing a reverse DNS lookup, you can help
identify potential spammers.

Analysis of SCL ratings on messages from a particular sender: When the Content Filter
agent processes a message, it assigns a spam confidence level (SCL) rating to the
message. The SCL rating is a number from 0 through 9. A higher SCL rating indicates that
a message is more likely to be spam. Data about each sender and the SCL ratings that
their messages yield is persisted for analysis by sender reputation. Sender reputation
calculates statistics about a sender according to the ratio between all messages from that
sender that had a low SCL rating in the past and all messages from that sender that had a
high SCL rating in the past. Additionally, the number of messages that have a high SCL
rating that the sender has sent in the last day is applied to the overall SRL.

Sender open proxy test: An open proxy is a proxy server that accepts connection requests
from anyone anywhere and forwards the traffic as if it originated from the local hosts.
Proxy servers relay TCP traffic through firewall hosts to provide user applications
transparent access across the firewall. Because proxy protocols are lightweight and
independent of user application protocols, proxies can be used by many different
services. Proxies can also be used to share a single Internet connection by multiple hosts.
Proxies are usually set up so that only trusted hosts inside the firewall can cross through
the proxies. A legitimate sender may be an open proxy because of an unintentional
misconfiguration or malware.

Open proxies provide an ideal way for malicious users to hide their true identities and
launch denial of service attacks (DoS) or send spam. As more proxy servers are configured
to be open by default, open proxies have become more common. Additionally, malicious
users can use multiple open proxies together to hide the sender's originating IP address.

When sender reputation performs an open proxy test, it does so by formatting an SMTP
request in an attempt to connect back to the Exchange server from the open proxy. If an

<!-- p.2995 -->

      SMTP request is received from the proxy, sender reputation verifies that the proxy is an
      open proxy and updates the open proxy test statistic for that sender.

Sender reputation weighs each of these statistics and calculates an SRL for each sender. The
SRL is a number from 0 through 9 that predicts the probability that a specific sender is a
spammer or otherwise malicious user. A value of 0 indicates that the sender isn't likely to be a
spammer; a value of 9 indicates that the sender is likely to be a spammer.

You can configure a block threshold from 0 through 9 at which sender reputation issues a
request to the Sender Filter agent, and, therefore, blocks the sender from sending a message
into the organization. When a sender is blocked, the sender is added to the Blocked Senders
list for a configurable time period. How blocked messages are handled depends on the
configuration of the Sender Filter agent. The following actions are the options for handling
blocked messages:

      Reject: Messages are returned in a non-delivery report (also known as an NDR, delivery
      status notification, DSN, or bounce message)

      Delete: Messages are silently deleted without an NDR.

      Accept: Messages are accepted and marked as coming from a blocked sender

For more information about the Sender Filter agent, see Sender filtering.

If a sender is included in the IP Block list or Microsoft IP Reputation Service, sender reputation
issues an immediate request to the Sender Filter agent to block the sender. To take advantage
of this functionality, you need to enable and configure the Microsoft Exchange Antispam
Update Service.

By default, sender reputation sets a rating of 0 for senders that haven't been analyzed. After a
sender has sent 20 or more messages, sender reputation calculates an SRL that's based on the
statistics described earlier in this topic.

When to use the SRL
Sender reputation acts on messages during two phases of the SMTP session:

      At the MAIL FROM: SMTP command: Sender reputation acts on a message only if the
      message was blocked or otherwise acted on by the Connection Filtering agent, Sender
      Filter agent, Recipient Filter agent, or Sender ID agent. In this case, sender reputation
      retrieves the sender's current SRL rating from the sender profile that's persisted about
      that sender on the Exchange server. After this rating is retrieved and evaluated, the
      Exchange server configuration dictates the behavior that occurs at a particular connection
      according to the block threshold.

<!-- p.2996 -->

         After the "end of data" SMTP command: The end of data transfer (EOD) SMTP command
         is given when all the actual message data is sent. At this point in the SMTP session, many
         of the antispam agents have processed the message. As a by-product of antispam
         processing, the statistics that sender reputation relies on are updated. Therefore, sender
         reputation has the data to calculate or recalculate an SRL rating for the sender.

Configuring the detection of open proxy servers
When sender reputation calculates an SRL, sender reputation tries to connect to the sender's
originating IP address by using a variety of common proxy protocols, such as SOCKS4, SOCKS5,
HTTP, Telnet, Cisco, and Wingate. Sender reputation formats a protocol-specific request in an
attempt to connect back to the Exchange server from the open proxy server by using an SMTP
request. If an SMTP request is received from the proxy server, sender reputation verifies that
the proxy server is an open proxy server and adjusts the SRL rating according to this result. By
default, the detection of open proxy servers is enabled in sender reputation.

For more information about how to configure the detection of open proxy servers, see Sender
reputation procedures.

Setting the SRL block threshold
The SRL is a number from 0 through 9 that predicts the probability that a specific sender is a
spammer or otherwise malicious user. You need to set an SRL threshold for sender blocking to
specify the SRL value that causes sender reputation to block a sender. By default, the SRL block
threshold is 7, which means senders that have an SRL of 7, 8 or 9 are blocked.. You should
monitor the effectiveness of sender reputation and the Protocol Analysis agent at the default
level.

On an Edge Transport server, if the SRL block threshold is met or exceeded by a particular
sender, sender reputation adds the sender to the IP Block list on the Connection Filtering
agent. Sometimes, spammers send batches of spam from a single sender. In this scenario, if
sender reputation calculates an SRL that exceeds the SRL block threshold, the sender is added
to the Sender Block List for a configurable duration of time. The default duration is 24 hours.
After 24 hours, the sender is removed from the Sender Block List and can send messages again.

When a sender is added to the IP Block list, sender reputation deletes the profile for the
sender. Sender reputation deletes the profile because the blocked sender's existing profile
indicates that the sender's SRL exceeds the SRL block threshold. This would cause the blocked
sender to be added to the IP Block list again as soon as the duration for sender blocking ends.

<!-- p.2997 -->

For more information about how to configure sender blocking, see Sender reputation
procedures.

<!-- p.2998 -->

Sender reputation procedures
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

Sender reputation and the Protocol Anaysis agent block unwanted messages according to
various characteristics of the sender. Sender reputation relies on persisted data about the
sender to determine what action, if any, to take on an inbound message. For more information,
see Sender reputation and the Protocol Analysis agent.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Antispam features" entry in the
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

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Use the Exchange Management Shell to enable or
disable sender reputation
To disable sender reputation, run the following command:

  PowerShell

<!-- p.2999 -->

  Set-SenderReputationConfig -Enabled $false

To enable sender reputation, run the following command:

  PowerShell

  Set-SenderReputationConfig -Enabled $true

  ７ Note

  The Protocol Analysis agent is the underlying agent for sender reputation functionality.
  When you disable sender reputation, the Protocol Analysis agent is still enabled. To
  disable the Protocol Analysis agent, run the command: Disable-TransportAgent "Protocol
  Analysis Agent" .

How do you know this worked?
To verify that you have successfully enabled or disabled sender reputation, run the following
command to verify the Enabled property value:

  PowerShell

  Get-SenderReputationConfig | Format-List Enabled

Use the Exchange Management Shell to enable or
disable sender reputation for external messages
By default, sender reputation is enabled for external messages (messages from external
sources).

To disable sender reputation for external messages, run the following command:

  PowerShell

  Set-SenderReputationConfig -ExternalMailEnabled $false

To enable sender reputation for external messages, run the following command:

  PowerShell

<!-- p.3000 -->

  Set-SenderReputationConfig -ExternalMailEnabled $true

How do you know this worked?
To verify that you have successfully enabled or disabled sender reputation for external
messages, run the following command to verify the ExternalMailEnabled property value:

  PowerShell

  Get-SenderReputationConfig | Format-List ExternalMailEnabled

Use the Exchange Management Shell to enable or
disable sender reputation for internal messages
As a best practice, you don't need to apply antispam filters to messages from trusted partners
or from inside your organization. There's always a chance that the filters will detect false
positives. To reduce the chance that filters will mishandle legitimate email messages, you
should typically configure antispam agents to only run on messages from untrusted and
unknown sources.

To enable sender reputation for internal messages, run the following command:

  PowerShell

  Set-SenderReputationConfig -InternalMailEnabled $true

To disable sender reputation for internal messages, run the following command:

  PowerShell

  Set-SenderReputationConfig -InternalMailEnabled $false

How do you know this worked?
To verify that you have successfully enabled or disabled sender reputation for internal
messages, run the following command to verify the InternalMailEnabled property value:

  PowerShell
