---
title: "Exchange Server — pages 2521-2560"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2521-2560
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2521-2560
family: exchange
documentKind: "doc"
abstract: "Action parameter in the Exchange Property Description Available Available Management Shell on in Transport servers SetHeaderName First property: Adds or modifies the specified Mailbox Exchange MessageHeaderField header field in the message servers and 2010 or SetHeaderValue head"
---

# Exchange Server — pages 2521-2560

<!-- p.2521 -->

 Action parameter in the Exchange    Property             Description                            Available        Available
 Management Shell                                                                                on               in

                                                                                                 Transport
                                                                                                 servers

 SetHeaderName                       First property:      Adds or modifies the specified         Mailbox          Exchange
                                     MessageHeaderField   header field in the message            servers and      2010 or
 SetHeaderValue                                           header, and sets the header field      Edge             later
                                     Second property:     to the specified value.                Transport
                                     String                                                      servers

 SetSCL                              SCLValue             Sets the SCL of the message to         Mailbox          Exchange
                                                          the specified value.                   servers and      2010 or
                                                                                                 Edge             later
                                                                                                 Transport
                                                                                                 servers

 SmtpRejectMessageRejectText         First property:      Ends the SMTP connection               Edge             Exchange
                                     String               between the sending server and         Transport        2010 or
 SmtpRejectMessageRejectStatusCode                        the Edge Transport server with         servers only     later
                                     Second property:     the specified SMTP status code
                                     SMTPStatusCode       and the specified rejection text.
                                                          The recipient doesn't receive the
                                                          original message or notification.

                                                          Valid values for the SMTP status
                                                          code are integers from 400
                                                          through 500 as defined in RFC
                                                          3463.

                                                          If you specify the rejection text
                                                          without specifying the SMTP
                                                          status code, the default code 550
                                                          is used.

                                                          If you specify the SMTP status
                                                          code without specifying the
                                                          rejection text, the text that's used
                                                          is Delivery not authorized,
                                                          message refused .

 StopRuleProcessing                  n/a                  Specifies that after the message is    Mailbox          Exchange
                                                          affected by the rule, the message      servers and      2013 or
                                                          is exempt from processing by           Edge             later
                                                          other rules.                           Transport
                                                                                                 servers

Property values
The property values that are used for actions in mail flow rules are described in the following table.

                                                                                                           ﾉ    Expand table

<!-- p.2522 -->

Property                   Valid values                                  Description

AddedManagerAction         One of the following values:                  Specifies how to include the sender's manager
                                 To                                      in messages.
                                 Cc
                                 Bcc                                     If you select To, Cc, or Bcc, the sender's manager
                                 Redirect                                is added as a recipient in the specified field.

                                                                         If you select Redirect, the message is only
                                                                         delivered to the sender's manager without
                                                                         notifying the sender or the recipient.

                                                                         This action only works if the sender's Manager
                                                                         attribute is defined in Active Directory.

Addresses                  Exchange recipients                           Depending on the action, you might be able to
                                                                         specify any mail-enabled object in the
                                                                         organization, or you might be limited to a
                                                                         specific object type. Typically, you can select
                                                                         multiple recipients, but you can only send an
                                                                         incident report to one recipient.

AuditSeverityLevel         One of the following values:                  The values Low, Medium, or High specify the
                                 Uncheck Audit this rule with severity   severity level that's assigned to the incident
                                 level, or select Audit this rule with   report and to the corresponding entry in the
                                 severity level with the value Not       message tracking log.
                                 specified ( DoNotAudit )
                                 Low                                     The other value prevents an incident report from
                                 Medium                                  being generated, and prevents the
                                 High                                    corresponding entry from being written to the
                                                                         message tracking log.

DisclaimerFallbackAction   One of the following values:                  Specifies what to do if the disclaimer can't be
                                 Wrap                                    applied to a message. There are situations
                                 Ignore                                  where the contents of a message can't be
                                 Reject                                  altered (for example, the message is encrypted).
                                                                         The available fallback actions are:
                                                                               Wrap: The original message is wrapped in
                                                                               a new message envelope, and the
                                                                               disclaimer text is inserted into the new
                                                                               message. This is the default value.
                                                                                   Subsequent mail flow rules are applied
                                                                                   to the new message envelope, not to
                                                                                   the original message. Therefore,
                                                                                   configure these rules with a lower
                                                                                   priority than other rules.
                                                                                   If the original message can't be
                                                                                   wrapped in a new message envelope,
                                                                                   the original message isn't delivered.
                                                                                   The message is returned to the sender
                                                                                   in an NDR.
                                                                               Ignore: The rule is ignored and the
                                                                               message is delivered without the
                                                                               disclaimer
                                                                               Reject: The message is returned to the
                                                                               sender in an NDR.

<!-- p.2523 -->

Property                 Valid values                                     Description

DisclaimerText           HTML string                                      Specifies the disclaimer text, which can include
                                                                          HTML tags, inline cascading style sheet (CSS)
                                                                          tags, and images by using the IMG tag. The
                                                                          maximum length is 5000 characters, including
                                                                          tags.

DisclaimerTextLocation   Single value: Append or Prepend                  In the Exchange Management Shell, you use the
                                                                          ApplyHtmlDisclaimerTextLocation to specify the
                                                                          location of the disclaimer text in the message.

                                                                          Append : Add the disclaimer to the end of the
                                                                          message body. This is the default value.

                                                                          Prepend : Add the disclaimer to the beginning of
                                                                          the message body.

DSNEnhancedStatusCode    Single DSN code value:                           Specifies the DSN code that's used. You can
                               5.7.1                                      create custom DSNs by using the New-
                               5.7.900 through 5.7.999                    SystemMessage cmdlet.

                                                                          If you don't specify the rejection reason text
                                                                          along with the DSN code, the default reason
                                                                          text that's used is Delivery not authorized,
                                                                          message refused .

                                                                          When you create or modify the rule in the
                                                                          Exchange Management Shell, you can specify
                                                                          the rejection reason text by using the
                                                                          RejectMessageReasonText parameter.

IncidentReportContent    One or more of the following values:             Specifies the original message properties to
                               Sender                                     include in the incident report. You can choose to
                               Recipients                                 include any combination of these properties. In
                               Subject                                    addition to the properties you specify, the
                               Cc'd recipients ( Cc )                     message ID is always included. The available
                               Bcc'd recipients ( Bcc )                   properties are:
                               Severity
                               Sender override information                Sender: The sender of the original message.
                               ( Override )
                               Matching rules ( RuleDetections )          Recipients, Cc'd recipients, and Bcc'd
                               False positive reports ( FalsePositive )   recipients: All recipients of the message, or only
                               Detected data classifications              the recipients in the Cc or Bcc fields. For each
                               ( DataClassifications )                    property, only the first 10 recipients are included
                               Matching content ( IdMatch )               in the incident report.
                               Original mail ( AttachOriginalMail )
                                                                          Subject: The Subject field of the original
                                                                          message.

                                                                          Severity: The audit severity of the rule that was
                                                                          triggered. Message tracking logs include all the
                                                                          audit severity levels, and can be filtered by audit
                                                                          severity. In the EAC, if you clear the Audit this
                                                                          rule with severity level check box (in the
                                                                          Exchange Management Shell, the
                                                                          SetAuditSeverity parameter value DoNotAudit ),
                                                                          rule matches won't appear in the rule reports. If

<!-- p.2524 -->

Property                  Valid values                                Description

                                                                      a message is processed by more than one rule,
                                                                      the highest severity is included in any incident
                                                                      reports.

                                                                      Sender override information: The override if the
                                                                      sender chose to override a Policy Tip. If the
                                                                      sender provided a justification, the first 100
                                                                      characters of the justification are also included.

                                                                      Matching rules: The list of rules that the
                                                                      message triggered.

                                                                      False positive reports: The false positive if the
                                                                      sender marked the message as a false positive
                                                                      for a Policy Tip.

                                                                      Detected data classifications: The list of
                                                                      sensitive information types detected in the
                                                                      message.

                                                                      Matching content: The sensitive information
                                                                      type detected, the exact matched content from
                                                                      the message, and the 150 characters before and
                                                                      after the matched sensitive information.

                                                                      Original mail: The entire message that triggered
                                                                      the rule is attached to the incident report.

                                                                      In the Exchange Management Shell, you specify
                                                                      multiple values separated by commas.

MessageClassification     Single message classification object        In the EAC, you select from the list of available
                                                                      message classifications.

                                                                      In the Exchange Management Shell, use the Get-
                                                                      MessageClassification cmdlet to see the
                                                                      message classification objects that are available.

MessageHeaderField        Single string                               Specifies the SMTP message header field to add,
                                                                      remove, or modify.

                                                                      The message header is a collection of required
                                                                      and optional header fields in the message.
                                                                      Examples of header fields are To, From,
                                                                      Received, and Content-Type. Official header
                                                                      fields are defined in RFC 5322. Unofficial header
                                                                      fields start with X- and are known as X-headers.

NotificationMessageText   Any combination of plain text, HTML tags,   Specified the text to use in a recipient
                          and keywords                                notification message.

                                                                      In addition to plain text and HTML tags, you can
                                                                      specify the following keywords that use values
                                                                      from the original message:

                                                                             %%From%%
                                                                             %%To%%

<!-- p.2525 -->

Property           Valid values                                  Description

                                                                         %%Cc%%
                                                                         %%Subject%%
                                                                         %%Headers%%
                                                                         %%MessageDate%%

NotifySenderType   One of the following values:                  Specifies the type of Policy Tip that the sender
                         Notify the sender, but allow them to    receives if the message violates a DLP policy.
                         send ( NotifyOnly )                     The settings are described in the following list:
                         Block the message ( RejectMessage )             Notify the sender, but allow them to
                         Block the message unless it's a false           send: The sender is notified, but the
                         positive                                        message is delivered normally.
                         ( RejectUnlessFalsePositiveOverride )           Block the message: The message is
                         Block the message, but allow the                rejected, and the sender is notified.
                         sender to override and send                     Block the message unless it's a false
                         ( RejectUnlessSilentOverride )                  positive: The message is rejected unless
                         Block the message, but allow the                it's marked as a false positive by the
                         sender to override with a business              sender.
                         justification and send                          Block the message, but allow the sender
                         ( RejectUnlessExplicitOverride )                to override and send: The message is
                                                                         rejected unless the sender has chosen to
                                                                         override the policy restriction.
                                                                         Block the message, but allow the sender
                                                                         to override with a business justification
                                                                         and send: This value is similar to Block the
                                                                         message, but allow the sender to
                                                                         override and send, but the sender also
                                                                         provides a justification for overriding the
                                                                         policy restriction.

                                                                 When you use this action, you need to use the
                                                                 The message contains sensitive information
                                                                 (MessageContainsDataClassification) condition.

RMSTemplate        Single RMS template object                    Specifies the Rights Management Services (RMS)
                                                                 template that's applied to the message.

                                                                 In the EAC, you select the RMS template from a
                                                                 list.

                                                                 In the Exchange Management Shell, use the Get-
                                                                 RMSTemplate cmdlet to see the RMS templates
                                                                 that are available.

                                                                 RMS requires Exchange Enterprise client access
                                                                 licenses (CALs) for each mailbox. For more
                                                                 information about CALs, see Exchange licensing
                                                                 FAQs     .

SCLValue           One of the following values:                  Specifies the spam confidence level (SCL) that's
                         Bypass spam filtering ( -1 )            assigned to the message. A higher SCL value
                         Integers 0 through 9                    indicates that a message is more likely to be
                                                                 spam.

<!-- p.2526 -->

 Property                 Valid values                              Description

 String                   Single string                             Specifies the text that's applied to the specified
                                                                    message header field, NDR, or event log entry.

                                                                    In the Exchange Management Shell, if the value
                                                                    contains spaces, enclose the value in quotation
                                                                    marks (").

For more information
Mail flow rule conditions and exceptions (predicates) in Exchange Server

<!-- p.2527 -->

Organization-wide disclaimers, signatures,
footers, or headers in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016       2019       Subscription Edition

You can add an email disclaimer, legal disclaimer, disclosure statement, signature, or other
information to the top or bottom of email messages that enter or leave your organization. You
might be required to do this for legal, business, or regulatory requirements, to identify
potentially unsafe email messages, or for other reasons that are unique to your organization.

To create a disclaimer, you create a mail flow rule (also known as transport rule) with an action
that adds the specified text to email messages. You can configure the rule to apply the
disclaimer to all messages (no conditions), or you can define conditions that determine when
the disclaimer is added (for example, when the sender is a member of a specific group, when
the message includes specific words or text patterns, or outgoing messages only). You can also
define exceptions that prevent the disclaimer from being added to messages (for example,
messages from specific senders, messages sent to specific recipients, or messages that already
contain the disclaimer). To apply multiple disclaimers to the same message, you need to use
multiple rules. For more information about mail flow rules, see Mail flow rules in Exchange
Server.

Looking for procedures? See Procedures for mail flow rules in Exchange Server.

Examples
Note: The examples in this topic are not intended for use as-is. Modify them for your needs.

                                                                                             ﾉ   Expand table

 Type                      Sample text added

 Legal - outgoing          This email and any files transmitted with it are confidential and intended solely
 messages                  for the use of the individual or entity to whom they are addressed. If you have
                           received this email in error, please notify the system manager.

 Legal - incoming          Employees are expressly required not to make defamatory statements and not
 messages                  to infringe or authorize any infringement of copyright or any other legal right by
                           email communications. Employees who receive such an email must notify their
                           supervisor immediately.

 Notice that message       This message was sent to the Sales discussion group.
 was sent to an alias

<!-- p.2528 -->

 Type                    Sample text added

 Signature - uses        Kathleen Mayer
 unique data for each    Sales Department
 employee                Contoso
                         www.contoso.com
                         kathleen@contoso.com
                         cell: 111-222-1234

 Advertisement           Click here for March specials

Location for your disclaimer
You can choose whether to insert the disclaimer at the beginning of the message (prepend), or
at the end of the message (append).

In the EAC, you select the action Append the disclaimer or Apply a disclaimer to the message
> prepend a disclaimer.

In the Exchange Management Shell, you use the ApplyHtmlDisclaimerTextLocation parameter
with the value Append (default) or Prepend .

Format your disclaimer
Here's the formatting that you can use in your disclaimer text.

                                                                                        ﾉ   Expand table

 Type of            Description
 information

 Plain text         The maximum length is 5,000 characters, including any HTML tags and inline
                    Cascading Style Sheets (CSS).

 HTML and inline    You can use HTML and inline CSS styles to format the text. For example, use the <HR>
 CSS                tag to add a line before the disclaimer.

                    Disclaimer text also supports the following keywords that use values from the sender:

                          %%City%%
                          %%Company%%
                          %%CountryOrRegion%%
                          %%Department%%
                          %%DisplayName%%
                          %%Fax%%
                          %%FirstName%%

<!-- p.2529 -->

Type of            Description
information

                         %%HomePhone%%
                         %%Initials%%
                         %%LastName%%
                         %%Manager%%
                         %%MobilePhone%%
                         %%Notes%%
                         %%Office%%
                         %%Pager%%
                         %%Phone%%
                         %%PostalCode%%
                         %%PostOfficeBox%%
                         %%StateOrProvince%%
                         %%StreetAddress%%
                         %%Title%%
                         %%UserPrincipalName%%
                         %%WindowsEmailAddress%%

                   HTML is ignored if the disclaimer is added to a plain text message.

Images             Use the <IMG> tag to point to an image available on the Internet. For example, <IMG
                   src="http://contoso.com/images/companylogo.gif" alt="Contoso logo"> .
                   By default, Outlook and Outlook on the web (formerly known as Outlook Web App)
                   block external web content, including images. Users need to acknowledge and
                   download the blocked external content. We recommend that you test disclaimers that
                   have IMG tags to verify they display the way you want.

User information   You can use tokens to add unique attributes from the sender's Active Directory
for personalized   account:
signatures              %%City%%
                        %%Company%%
                         %%CountryOrRegion%%
                         %%Department%%
                         %%DisplayName%%
                         %%Fax%%
                         %%FirstName%%
                         %%HomePhone%%
                         %%Initials%%
                         %%LastName%%
                         %%Manager%%
                         %%MobilePhone%%
                         %%Notes%%
                         %%Office%%
                         %%Pager%%
                         %%Phone%%
                         %%PostalCode%%
                         %%PostOfficeBox%%

<!-- p.2530 -->

 Type of             Description
 information

                           %%StateOrProvince%%
                           %%StreetAddress%%
                           %%Title%%
                           %%UserPrincipalName%%
                           %%WindowsEmailAddress%%

Here's an example of an HTML disclaimer that includes a signature, an IMG tag, and embedded
CSS.

  HTML

  <div style="font-size:9pt; font-family: 'Calibri',sans-serif;">
  %%displayname%%<br/>
  %%title%%<br/>
  %%company%%<br/>
  %%street%%<br/>
  %%city%%, %%state%% %%zipcode%%</div>
  &nbsp;<br/>
  <div style="background-color:#D5EAFF; border:1px dotted #003333; padding:.8em; ">
  <div><img alt="Fabrikam" src="http://fabrikam.com/images/fabrikamlogo.png"></div>
  <span style="font-size:12pt; font-family: 'Cambria','times new
  roman','garamond',serif; color:#ff0000;">HTML Disclaimer Title</span><br/>
  <p style="font-size:8pt; line-height:10pt; font-family: 'Cambria','times
  roman',serif;">This message contains confidential information and is intended only
  for the individual(s) addressed in the message. If you aren't the named addressee,
  you should not disseminate, distribute, or copy this e-mail. If you aren't the
  intended recipient, you aren'tified that disclosing, distributing, or copying this
  e-mail is strictly prohibited. </p>
  <span style="padding-top:10px; font-weight:bold; color:#CC0000; font-size:10pt;
  font-family: 'Calibri',Arial,sans-serif; "><a
  href="http://www.fabrikam.com">Fabrikam, Inc. </a></span><br/><br/>
  </div>

Fallback options for disclaimer rules
Exchange can't modify the content of some messages (for example, encrypted messages). For
rules that add disclaimers to messages, you need to specify what to do if the disclaimer can't
be added. This contingency is known as the fallback option for the disclaimer rule. The available
fallback options are:

       Wrap: A new message is created and the original message is added to it as an
       attachment. The disclaimer text is added to the new message, which is delivered to the
       recipients. This is the default value.

<!-- p.2531 -->

         Subsequent mail flow rules that examine message properties (for example, the
         message subject or text in the message body) will examine the new message, not the
         original message (which is now an attachment in the new message). If you want other
         rules to examine and act on the original message, make sure those rules are applied
         before the disclaimer rule by using a lower priority for the disclaimer rule and higher
         priority for other rules.
         If the process of inserting the original message as an attachment in the new message
         fails, the original message isn't delivered. The original message is returned to the
         sender in a non-delivery report (also known as an NDR or a bounce message).

     Ignore: The rule is ignored and the original message is delivered without the disclaimer.

     Reject: The original message is returned to the sender in an NDR.

In the EAC, you select the fallback option in the rule action. In the Exchange Management Shell,
you use the ApplyHtmlDisclaimerFallbackAction parameter.

Scope your disclaimer
As you work on your disclaimers, consider which messages they should apply to. For example,
you might want different disclaimers for internal and external messages, or for messages sent
by users in specific departments. To make sure only the first message in a conversation gets a
disclaimer, add an exception that prevents the disclaimer text from being applied to the same
messages over and over again.

Here are some examples of the conditions and exceptions you can use.

                                                                                     ﾉ   Expand table

 Description                         Conditions and           Conditions and exceptions in the
                                     exceptions in EAC        Exchange Management Shell for the
                                                              New-TransportRule or Set-
                                                              TransportRule cmdlets

 The recipient is located outside    Condition: The           -FromScope NotInOrganization -ExceptIf
 your Exchange organization. An      recipient is located >   -SubjectOrBodyMatches "CONTOSO LEGAL
 exception is configured so          Outside the              NOTICE"
 messages that already contain the   organization
 disclaimer text "CONTOSO LEGAL      Exception: The subject
 NOTICE" don't have the disclaimer   or body > Subject or
 applied again.                      body matches these
                                     text patterns >
                                     CONTOSO LEGAL
                                     NOTICE

<!-- p.2532 -->

 Description                       Conditions and            Conditions and exceptions in the
                                   exceptions in EAC         Exchange Management Shell for the
                                                             New-TransportRule or Set-
                                                             TransportRule cmdlets

 Incoming messages with            Condition 1: The          -FromScope NotInOrganization -
 executable attachments            sender is located >       AttachmentHasExecutableContent
                                   Outside the
                                   organization
                                   Condition 2: Any
                                   attachment > has
                                   executable content

 Sender is in the marketing        Condition: The sender     -FromMemberOf "Marketing Team"
 department                        > is a member of this
                                   group > group name

 Every message that comes from     Condition 1: The          -FromScope NotInOrganization -SentTo
 an external sender to the sales   sender is located >       "Sales Discussion Group"
 discussion group                  Outside the
                                   organization
                                   Condition 2: The
                                   message > To or Cc
                                   box contains this
                                   person > group name

 Prepend an advertisement to       Condition 1: The          -ApplyHtmlDisclaimerLocation Prepend -
 outgoing messages for one month   recipient is located >    SentToScope NotInOrganization -
                                   Outside the               ActivationDate '03/1/2016' -ExpiryDate
                                   organization              '03/31/2016'
                                   Enter the dates in the
                                   Activate this rule on
                                   the following date and
                                   Deactivate this rule on
                                   the following date
                                   fields.

For a complete list of conditions and exceptions that you can use to target the disclaimer, see
Mail flow rule conditions and exceptions (predicates) in Exchange Server.

Limitations of organization wide signatures
Exchange Server signatures can't fulfill the following scenarios:

     Insert the signature directly under the latest email reply or forward.
     Display server-side email signatures in users' Sent Items folders.

<!-- p.2533 -->

     Skip lines which contain variables that couldn't be updated (for example, if the value
     wasn't provided for a user).

To gain these and other capabilities, use a third-party tool. Do an internet search for email
signature software. A number of these providers are Microsoft Gold Partners and their
software provides these capabilities.

For more information
Organization-wide disclaimers, signatures, footers, or headers in Exchange 2013

<!-- p.2534 -->

Procedures for mail flow rules in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

Mail flow rules (also known as transport rules) identify and take action on messages that flow
through your Exchange organization. For more information about mail flow rules, see Mail flow
rules in Exchange Server.

On Mailbox servers, you can manage mail flow rules in the Exchange admin center (EAC) and in
the Exchange Management Shell. On Edge Transport servers, you can only use the Exchange
Management Shell.

   Tip

  Verify that your rules work the way you expect. Be sure to thoroughly test each rule and
  the interactions between rules.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes.

      For more information about the EAC, see Exchange admin center in Exchange Server. To
      learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mail flow rules" entry in
      Messaging policy and compliance permissions in Exchange Server (Exchange Server), or in
      Feature Permissions in Exchange Online.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

<!-- p.2535 -->

Create mail flow rules
     Creating mail flow rules is mostly about the scenarios that you want to fulfill. For
     examples, see the following topics:

        Use mail flow rules to inspect message attachments

        Organization-wide disclaimers, signatures, footers, or headers in Exchange Server

        Manage message approval

     Data loss prevention (DLP) policies are collections of mail flow rules. To create DLP
     policies, see Exchange Server DLP Procedures.

Use the EAC to create mail flow rules
The EAC allows you to create mail flow rules by using a template (a filtered list of conditions
and actions), by copying an existing rule, or by creating a rule from scratch.

   1. In the EAC, go to Mail flow > Rules, and then select one of the following options:

           To create a rule from a template, click Add (    ) and select a template (a value other
           than Create new rule).

           To copy a rule, select the rule, and then select Copy (    ). Note that the option to
           copy a rule is only available in the EAC.

           To create a new rule from scratch, Add (     ) and then select Create a new rule.

   2. In the New rule page that opens, configure the following settings:

           Name: Enter a unique, descriptive name for the rule.

           Apply this rule if: Select a condition for the rule. If you want the rule to apply to all
           messages, select [Apply to all messages]. For an explanation of the available
           conditions, see Mail flow rule conditions and exceptions (predicates) in Exchange
           Server.

           Do the following: Select an action for the rule. The action is applied to messages
           that match the conditions. For an explanation of the available conditions, see Mail
           flow rule actions in Exchange Server.

     Optional properties:

           Audit this rule with severity level: For DLP policies, this setting specifies how rule
           match data is displayed in the DLP policy detection reports. For more information,

<!-- p.2536 -->

       View DLP policy detection reports. If you clear the check box, or select the value Not
       specified, rule matches won't appear in the rule reports.

       Choose a mode for this rule: You can use one of the two test modes to test the rule
       without impacting mail flow. In both test modes, when the conditions are met, an
       entry is added to the message tracking log. Select one of the following values:

       Enforce: This turns on the rule and it starts processing messages immediately. All
       actions on the rule will be performed. This is the default value.

       Test with Policy Tips: This turns on the rule, and any Policy Tip actions (Notify the
       sender with a Policy Tip) will be sent, but no actions related to message delivery will
       be performed. DLP is required to use this mode. To learn more, see Policy Tips.

       Test without Policy Tips: For DLP policies, only the Generate incident report and
       send it to action will be enforced. No actions related to message delivery are
       performed.

3. You can create the rule by clicking Save, or you can click More options to configure the
  following additional settings:

       To add more conditions, click Add condition. If you have more than one condition,
       you can remove a condition by clicking Remove X. Note that there are more
       conditions available after you click More options.

       To add more actions, click Add action. If you have more than one action, you can
       remove an action by clicking Remove X. Note that there are more actions available
       after you click More options.

       To add exceptions for the rule, click Add exception, and then select an exception by
       using the Except if drop down. You can remove an exception by clicking Remove X.

       Activate this rule on the following date: Specify the start date if you want the rule
       to take effect after a certain date. Note that the rule will still be enabled prior to that
       date, but it won't be processed.

       Deactivate this rule on the following date: Specify the end date if you want the rule
       to stop processing messages on a certain date. Note that the rule will still be
       enabled after that date, but it won't be processed.

       Stop processing more rules: Select this check box to avoid applying additional rules
       after this rule processes a message.

       Defer the message if rule processing doesn't complete: Select this check box to
       resubmit the message for processing. By default, the rule will be ignored, and

<!-- p.2537 -->

           delivery of the message will continue as normal.

           Match sender address in message: For conditions and exceptions that examine the
           sender's address, you can specify where the rule looks for the sender's address: in
           the message header (default), the message envelope, or the header and envelope.
           For more information, see Senders.

           Comments: Specify a descriptive comment for the rule.

     When you're finished, click Save.

Use the Exchange Management Shell to create mail flow rules
There are two settings that you can configure on new mail flow rules in the Exchange
Management Shell that aren't available in the EAC (until after you create the rule):

     Create the new rule as disabled (Enabled $false )

     Set the priority of the rule (Priority <Number>).

To create mail flow rules in the Exchange Management Shell, use the following syntax:

  PowerShell

  New-TransportRule -Name <RuleName> [<Conditions>] [<Exceptions>] <Actions>
  [<Properties>]

This example creates a new rule with the following settings:

     Name: Mark messages from the Internet to Sales DG.

     Conditions

        Messages from external senders.

        And

        Messages sent to the distribution group named Sales Department.

     Action: Prepend the message's Subject field with the value "External message to Sales
     DG: " . The trailing colon and space help to distinguish the added text from the original

     value.

  PowerShell

<!-- p.2538 -->

  New-TransportRule -Name "Mark messages from the Internet to Sales DG" -FromScope
  NotInOrganization -SentTo "Sales Department" -PrependSubject "External message to
  Sales DG: "

For detailed syntax and parameter information, see New-TransportRule.

Note: The conditions and actions in the example are for illustrative purposes only. Review the
available mail flow rule conditions, exceptions, and actions to determine which ones meet your
requirements.

How do you know this worked?
To verify that you've successfully created a mail flow rule, use either of the following
procedures:

     In the EAC, go to Mail flow > Rules, and verify that the rule you created is in the list.

     In the Exchange Management Shell, use either of the following procedures:
        Run the following command to see the new rule in the list of rules:

        PowerShell

        Get-TransportRule

        Replace <RuleName> with the name of the rule, and run the following command to
        see the details of the rule:

        PowerShell

        Get-TransportRule -Identity "<RuleName>" | Format-List

View mail flow rules
Mail flow rules that you create on a Mailbox server are stored in Active Directory, so when you
view the rules on a Mailbox server, you see all rules in your organization. When you use the
Exchange Management Shell to view mail flow rules on an Edge Transport server, you see the
rules that are stored on the local server.

Use the EAC to view mail flow rules
   1. In the EAC, go to Mail flow > Rules.

<!-- p.2539 -->

   2. When you select a rule, information about the rule is displayed in the details pane. To see
     more information about the rule, click Edit (   ).

     In the EAC, the Version property is only visible in the details pane. This property indicates
     the compatibility of the rule with previous versions of Exchange (14.n.n.n is Exchange
     2010, 15.0.n.n is Exchange 2013).

Use the Exchange Management Shell to view mail flow rules
To return a summary list of all mail flow rules, run the following command:

  PowerShell

  Get-TransportRule

To return detailed information about a specific rule, use the following syntax:

  PowerShell

  Get-TransportRule -Identity "<RuleName>" | Format-List [<Specific properties to
  view>]

This example returns all the property values for the rule named "Sender is a member of
marketing".

  PowerShell

<!-- p.2540 -->

  Get-TransportRule -Identity "Sender is a member of marketing" | Format-List

This example returns only the specified properties for the same rule.

  PowerShell

  Get-TransportRule -Identity "Sender is a member of marketing" | Format-List
  Name,State,Mode,Priority,Comments,Conditions,Exceptions,RuleVersion

For detailed syntax and parameter information, see Get-TransportRule.

Use the Exchange Management Shell to view the available
conditions and exceptions (predicates) for mail flow rules
The conditions and exceptions in mail flow rules are collectively known as predicates because
for every condition, there's a corresponding exception that uses the exact same settings and
syntax. The only difference is: conditions specify messages to include, while exceptions specify
messages to exclude. You can only view the list of conditions and exceptions in the Exchange
Management Shell.

To view the conditions and exceptions that are available in mail flow rules, run the following
command:

  PowerShell

  Get-TransportRulePredicate

For detailed syntax and parameter information, see Get-TransportRulePredicate.

Notes:

     Exceptions aren't distinguished from conditions.

     The predicates that are available on Edge Transport servers are a small subset of those
     available on Mailbox servers. For more information, see Mail flow rule conditions and
     exceptions (predicates) in Exchange Server.

     Some of the predicate names are different than the corresponding condition and
     exception parameter names on the New-TransportRule and Set-TransportRule cmdlets.
     And, some predicates require multiple parameters.

<!-- p.2541 -->

Use the Exchange Management Shell to view the available
actions for mail flow rules
You can only view the list of actions in the Exchange Management Shell.

To view the actions that are available in mail flow rules, run the following command:

  PowerShell

  Get-TransportRuleAction

For detailed syntax and parameter information, see Get-TransportRuleAction.

Notes:

     A small subset of actions that are available on Mailbox servers are also available on Edge
     Transport servers, but some actions are only available on Edge Transport servers. For
     more information, see Mail flow rule actions in Exchange Server.

     Some of the action names are different than the corresponding action parameter names
     on the New-TransportRule and Set-TransportRule cmdlets. And, some actions require
     multiple parameters.

Modify mail flow rules

Use the EAC to modify mail flow rules
No additional settings are available when you modify a mail flow rule in the EAC. They're the
same settings that were available when you created the rule.

   1. In the EAC, go to Mail flow > Rules.

   2. Select the rule, and then click Edit (   ). Note that the properties of the rule are fully
     expanded (there's no More options link available). For more information about the rule
     properties, see the Use the EAC to create mail flow rules section in this topic.

Use the Exchange Management Shell to modify mail flow
rules
When you modify a mail flow rule in the Exchange Management Shell, you can't disable or
enable the rule (there's no Enabled parameter on the Set-TransportRule cmdlet). Instead, you

<!-- p.2542 -->

use the Disable-TransportRule and Enable-TransportRule cmdlets as describe later in this
topic.

To modify a mail flow rule in the Exchange Management Shell, use the following syntax:

  PowerShell

  Set-MailFlowRule -Identity "<RuleName>" [<Conditions>] [<Exceptions>] [<Actions>]
  [<Properties>]

This example adds an exception to the rule named "Sender is a member of marketing" so that
it won't apply to messages that are sent by the user named Kelly Rollin.

  PowerShell

  Set-TransportRule -Identity "Sender is a member of marketing" -ExceptIfFrom "Kelly
  Rollin"

For detailed syntax and parameter information, see Set-TransportRule.

How do you know this worked?
To verify that you have successfully modified a mail flow rule, use either of the following
procedures:

     In the EAC, go to Mail flow > Rules, select the rule, and view the information in details
     pane. To see more settings, click Edit (    ).

     In the Exchange Management Shell, replace <RuleName> with the name of the rule, and
     run the following command:

         PowerShell

         Get-TransportRule -Identity "<RuleName>" | Format-List

Set the priority of mail flow rules
By default, mail flow rules are given a priority that's based on the order they were created in
(newer rules are lower priority than older rules). A lower priority number indicates a higher
priority for the rule, and rules are processed in priority order (higher priority rules are
processed before lower priority rules). No two rules can have the same priority.

Notes:

<!-- p.2543 -->

     You can prevent a message from being acted on by subsequent lower priority rules by
     including the Stop processing more rules (StopRuleProcessing $true ) action in the rule.

     In the EAC, you can only change the priority of the rule after you create it. In the
     Exchange Management Shell, you can override the default priority when you create the
     rule (which can affect the priority of existing rules).

Use the EAC to set the priority of mail flow rules
In the EAC, rules are processed in the order that they're displayed (the first rule has the Priority
value 0). To change the priority of a rule, move the rule up or down in the list (you can also
directly modify the Priority number by editing the rule in the EAC).

   1. In the EAC, go to Mail flow > Rules.

   2. Select a rule, and then click Move up ( ) or Move down ( ) to move the rule up or down
     in the list.

Use the Exchange Management Shell to set the priority of
mail flow rules
The highest priority value you can set on a rule is 0. The lowest value you can set depends on
the number of rules. For example, if you have five rules, you can use the priority values 0
through 4. Changing the priority of an existing rule can have a cascading effect on other rules.
For example, if you have five rules (priorities 0 through 4), and you change the priority of a rule
to 2, the existing rule with priority 2 is changed to priority 3, and the rule with priority 3 is
changed to priority 4.

To set the priority of a rule in the Exchange Management Shell, use the following syntax:

  PowerShell

  Set-TransportRule -Identity "<RuleName>" -Priority <Number>

This example sets the priority of the rule named "Sender is a member of marketing" to 2. All
existing rules that have a priority less than or equal to 2 are decreased by 1 (their priority
numbers are increased by 1).

  PowerShell

  Set-TransportRule -Identity "Sender is a member of marketing" -Priority 2

<!-- p.2544 -->

Note: To set the priority of a new rule when you create it, use the Priority parameter on the
New-TransportRule cmdlet.

How do you know this worked?
To verify that you have successfully modified the priority of a mail flow rule, use either of the
following procedures:

     In the EAC, go to Mail flow > Rules, and verify the Priority value of the rule in the list.

     In the Exchange Management Shell, use either of the following procedures:
        Run the following command to see the list of rules and their Priority values:

        PowerShell

        Get-TransportRule

        Replace <RuleName> with the name of the rule, and run the following command:

        PowerShell

        Get-TransportRule -Identity "<RuleName>" | Format-List Name,Priority

Enable or disable mail flow rules
Disabling a rule prevents the rule from acting on messages, but allows you to preserve the
settings of the rule.

By default, mail flow rules are enabled when you create them in the EAC or the Exchange
Management Shell, but you can use the Exchange Management Shell to create a disabled rule
(use the Enabled parameter with the value $false ).

Use the EAC to enable or disable mail flow rules
   1. In the EAC, go to Mail flow > Rules.

   2. Select the rule from the list, and then configure one of the following settings:

           Disable the rule: Clear the check box in the On column.

           Enable the rule: Select the check box in the On column.

<!-- p.2545 -->

Use the Exchange Management Shell to enable or disable mail
flow rules
To enable or disable a mail flow rule in the Exchange Management Shell, use the following
syntax:

  PowerShell

  <Enable-TransportRule | Disable-TransportRule> -Identity "<RuleName>"

This example disables the mail flow rule named "Sender is a member of marketing".

  PowerShell

  Disable-TransportRule "Sender is a member of marketing"

This example enables the mail flow rule named "Sender is a member of marketing".

  PowerShell

  Enable-TransportRule "Sender is a member of marketing"

For detailed syntax and parameter information, see Enable-TransportRule and Disable-
TransportRule.

How do you know this worked?
To verify that you have successfully enabled or disabled a mail flow rule, use either of the
following procedures:

     In the EAC, go to Mail flow > Rules, and in the list of rules verify the status of the check
     box in the On column.

     In the Exchange Management Shell, use either of the following procedures:
          Run the following command to see the list of rules and their State values:

          PowerShell

          Get-TransportRule

          Replace <RuleName> with the name of the rule, and run the following command:

          PowerShell

<!-- p.2546 -->

        Get-TransportRule -Identity "<RuleName>" | Format-List Name,State

Remove mail flow rules

Use the EAC to remove mail flow rules
   1. From the EAC, go to Mail flow > Rules.

   2. Select the rule you want to remove from the list, and then click Delete ( ).

Use the Exchange Management Shell to remove mail flow
rules
To remove mail flow rules in the Exchange Management Shell, use the following syntax:

  PowerShell

  Remove-TransportRule -Identity "<RuleName>"

This example removes the mail flow rule named "Sender is a member of marketing":

  PowerShell

  Remove-TransportRule -Identity "Sender is a member of marketing"

For detailed syntax and parameter information, see Remove-TransportRule.

How do you know this worked?
To verify that you have successfully removed a mail flow rule, use either of the following
procedures:

     In the EAC, go to Mail flow > Rules, and verify that the rule you removed is no longer in
     the list.

     In the Exchange Management Shell, run the following command to verify that the rule
     you removed is no longer listed:

        PowerShell

<!-- p.2547 -->

         Get-TransportRule

Import or export mail flow rule collections
You can import a mail flow rule collection that you've previously exported as a backup, or
import rules that you've exported from a previous version of Exchange.

Notes:

     You can't import or export mail flow rule collections in the EAC. You can only use the
     Exchange Management Shell.

     You can't import a mail flow rule collection into Exchange 2010 if that rule collection was
     exported from Exchange 2013 or later.

Use the Exchange Management Shell to export a mail flow
rule collection
   1. Run the following command:

         PowerShell

         $File = Export-TransportRuleCollection

   2. Use the following syntax:

         PowerShell

         [System.IO.File]::WriteAllBytes('<OutputFile>', $File.FileData)

     For example, to save the exported mail flow rule collection to the file C:\My
     Documents\Exported Rules.xml, run the following command:

         PowerShell

         [System.IO.File]::WriteAllBytes('C:\My Documents\Exported Rules.xml',
         $File.FileData)

For detailed syntax and parameter information, see Export-TransportRuleCollection.

<!-- p.2548 -->

Use the Exchange Management Shell to import a mail flow
rule collection
  1. Use the following syntax:

       PowerShell

       $Data = [System.IO.File]::ReadAllBytes('<OutputFile>')

     For example, to import the mail flow rule collection from C:\My Documents\Exported
     Rules.xml, run the following command:

       PowerShell

       $Data = [System.IO.File]::ReadAllBytes('C:\My Documents\Exported Rules.xml')

  2. Run the following command:

       PowerShell

       Import-TransportRuleCollection -FileData $Data

For detailed syntax and parameter information, see Import-TransportRuleCollection.

Need more help?
     Resources for Exchange Server:

        Mail flow rules in Exchange Server

        Mail flow rule conditions and exceptions (predicates) in Exchange Server

        Mail flow rule actions in Exchange Server

<!-- p.2549 -->

Register Filter Pack IFilters in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Mail flow rules with attachment scanning conditions perform text extraction when analyzing
the content of attachments. Exchange Server can scan most commonly used attachment types
natively. More attachment types can be included by registering IFilters in Exchange Server. This
article shows you how to register IFilters released by Microsoft and external providers.

After you register an IFilter for a specific file type, mail flow rules with attachment processing
conditions can scan these attachments. As a result, these file types no longer trigger the
AttachmentIsUnsupported condition.

  ２ Warning

  The procedures listed in this topic involve modifying the registry on your Exchange
  servers. Incorrectly editing the registry can cause serious problems that might require you
  to reinstall your operating system. Problems resulting from editing the registry incorrectly
  might not be able to be resolved. Before editing the registry, back up any valuable data.

  These procedures also require you to stop and restart the Microsoft Exchange Transport
  service on your Mailbox servers.

For more management tasks related to mail flow rules, see Procedures for mail flow rules in
Exchange Server.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes per server.

      You must be assigned permissions before you can perform this procedure or procedures.
      To see what permissions you need, see the "Exchange server configuration settings" entry
      in the Exchange infrastructure and PowerShell permissions article.

      You must do the following procedures on servers that already have Exchange Server
      Mailbox server role installed. If you add more Mailbox servers after you perform these
      procedures, you must perform them again on the newly provisioned servers.

<!-- p.2550 -->

     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Exchange admin center keyboard shortcuts.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at Exchange
  Server .

Register the Microsoft Office 2010 Filter Pack
If you are using an Exchange Server build earlier than Exchange Server 2019 CU15 (2025H1), by
default, Exchange mail flow rules do not support the following Office file types:

     Office OneNote
     Office Publisher

To support these files, you must deploy the Microsoft Office 2010 Filter Pack. This Filter Pack
isn't deployed during Exchange Server Setup and isn't a prerequisite for deployment.

Deploy the Microsoft Office 2010 Filter Pack
Deploying the Office 2010 Filter Pack consists of two main steps:

     Download and install the Filter Pack, which registers the IFilters with Windows (Search).

     Modifying the registry so the IFilters are also registered with Exchange Server. This step
     allows Exchange to support attachment scanning for the file formats.

  ） Important

  You must perform this procedure on all Mailbox servers in your organization.

   1. Download and save the Microsoft Office 2010 Filter Pack ( FilterPack64bit.exe ) from the
     Microsoft Download Center      .

   2. Run the FilterPack64bit.exe file on your Mailbox server and follow the instructions to
     complete the installation.

   3. Start Registry Editor and locate the following registry subkey:

        PowerShell

<!-- p.2551 -->

     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\HubTransportRole\CLS
     ID

4. Under CLSID, add a subkey for OneNote files as follows:

   a. Right-click CLSID, point to New, and then select Key.

  b. Change the name of the new key to {B8D12492-CE0F-40AD-83EA-099A03D493F1} .

   c. Select the key you created and set the (Default) value to where you installed the Office
     2010 Filter Pack. By default, the filter pack gets installed at C:\Program Files\Common
     Files\Microsoft Shared\Filters\ONIFilter.dll .

  d. Right select {B8D12492-CE0F-40AD-83EA-099A03D493F1}, point to New, and then
     select String Value.

   e. Name the new string value ThreadingModel and set it to Both .

5. Under CLSID, add a subkey for Publisher files as follows:

   a. Right-click CLSID, point to New, and then select Key.

  b. Change the name of the new key to {A7FD8AC9-7ABF-46FC-B70B-6A5E5EC9859A} .

   c. Select the key you created and set the (Default) value to where you installed the Office
     2010 Filter Pack. By default, the filter pack gets installed at C:\Program Files\Common
     Files\Microsoft Shared\Filters\PUBFILT.dll .

  d. Right-click {A7FD8AC9-7ABF-46FC-B70B-6A5E5EC9859A}, point to New, and then
     select String Value.

   e. Name the new string value ThreadingModel and set it to Both .

6. Locate the following registry key:

    PowerShell

     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\HubTransportRole\fil
     ters

7. Under filters, add a subkey for .one extensions as follows.

   a. Right-click filters, point to New, and then select Key.

  b. Change the name of the new key to .one .

<!-- p.2552 -->

      c. Select the key you created and set the (Default) value to {B8D12492-CE0F-40AD-83EA-
        099A03D493F1} .

   8. Under filters, add a subkey for .pub extensions as follows:

      a. Right-click filters, point to New and then select Key.

      b. Change the name of the new key to .pub .

      c. Select the key you created and set the (Default) value to {A7FD8AC9-7ABF-46FC-B70B-
        6A5E5EC9859A} .

   9. Close Registry Editor.

 10. On your Mailbox server, stop and then restart the following services in the specified
     order:

      a. Stop the Microsoft Exchange Transport service.

      b. Stop the Microsoft Filtering Management Service.

      c. Start the Microsoft Filtering Management Service.

      d. Start the Microsoft Exchange Transport service.

How do you know you successfully deployed the Microsoft
Office 2010 Filter Pack?
To verify that you successfully registered the Microsoft Office 2010 Filter Pack IFilters, do the
following steps:

   1. Create a mail flow rule with the following properties. For detailed instructions about how
     to create mail flow rules, see Procedures for mail flow rules in Exchange Server.

           The sender is your mailbox.
           Any attachment's content includes "Testing IFilters".
           Generate an incident report and send it to your mailbox.

   2. Create a OneNote file that contains the phrase "Testing IFilters", attach it to a new email
     message, and send it to yourself.

   3. Verify that you receive a mail flow rule incident report for the rule you created. This step
     confirms that the rules engine was able to analyze the contents of the OneNote file.

   4. Repeat Steps 2 and 3 with a Publisher file.

<!-- p.2553 -->

Register third-party IFilters to support other file
formats
You can extend the attachment scanning capability for other file types by registering other
third-party IFilters. You need to install and register the file type's IFilter on each of your Mailbox
servers.

  ） Important

  Microsoft hasn't tested third-party IFilters with mail flow rules, therefore we recommend
  that you deploy and test any third-party IFilters in a test environment before deploying
  into your production environment.

Deploy the Adobe PDF IFilter
This procedure shows how to deploy the Adobe PDF IFilter         to support processing of PDF
attachments in mail flow rules.

  ７ Note

  By default, Exchange Server supports the scanning of PDF files in mail flow rules. The PDF
  example here is used simply to illustrate how you can extend support for other file types
  using third-party IFilters.

   1. Download the Adobe PDF IFilter       and then follow the installation instructions.

   2. Start Registry Editor and locate the following subkey:

           Console

           HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\HubTransportRole\CLS
           ID

   3. Under CLSID, add a subkey for PDF files as follows:

      a. Right-click CLSID, point to New, and then select Key.

      b. Change the name of the new key to {E8978DA6-047F-4E3D-9C78-CDBE46041603} .

              ７ Note

<!-- p.2554 -->

           Each IFilter has a unique class ID (CLSID). You can find the CLSID in the installation
           documentation for the IFilter you're registering or by searching for the file
           extension under the HKEY_CLASSES_ROOT\CLSID key in the registry.

      c. Select the key you created and set the (Default) value to where you installed the PDF
        IFilter. By default, the PDF IFilter is installed at C:\Program Files\Adobe\Adobe PDF
        IFilter 9 for 64-bit platforms\bin\PDFFilter.dll .

   4. Locate the following registry key:

        Console

        HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\HubTransportRole\fil
        ters

   5. Under filters, add a subkey for .pdf extensions as follows:

      a. Right-click filters, point to New, and then select Key.

     b. Change the name of the new key to .pdf .

      c. Select the key you created and set the (Default) value to {E8978DA6-047F-4E3D-9C78-
        CDBE46041603} .

   6. Close Registry Editor.

   7. On your Mailbox server, stop and restart the following services in the specified order:

      a. Stop the Microsoft Exchange Transport service.

     b. Stop the Microsoft Filtering Management Service.

      c. Start the Microsoft Filtering Management Service.

     d. Start the Microsoft Exchange Transport service.

How do you know that you successfully registered third-party
IFilters to support other file formats?
Use the same procedure described earlier in this article: How do you know you successfully
deployed the Microsoft Office 2010 Filter Pack?. Substitute Publisher files with Adobe PDF files.

<!-- p.2555 -->

Use mail flow rules to inspect message
attachments
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

You can inspect email attachments in your organization by setting up mail flow rules (also
known as transport rules). Exchange offers mail flow rules that provide the ability to examine
email attachments as a part of your messaging security and compliance needs. When you
inspect attachments, you can then take action on the messages that were inspected based on
the content or characteristics of those attachments. Here are some attachment-related tasks
you can do by using mail flow rules:

      Search files in compressed attachments such as .zip and .rar files and, if there's any
      text that matches a pattern you specify, add a disclaimer to the end of the message.
      Inspect content within attachments and, if there are any keywords you specify, redirect
      the message to a moderator for approval before it's delivered.
      Check for messages with attachments that can't be inspected and then block the entire
      message from being sent.
      Check for attachments that exceed a certain size and then notify the sender of the issue, if
      you choose to prevent the message from being delivered.
      Create notifications that alert users if they send a message that has matched a mail flow
      rule.
      Block all messages containing attachments. For examples, see Common attachment
      blocking scenarios.

Exchange administrators can create mail flow rules by going to Exchange admin center > Mail
flow > Rules. You need to be assigned permissions before you can perform this procedure.
After you start to create a new rule, you can see the full list of attachment-related conditions by
clicking More options > Any attachment under Apply this rule if. The attachment-related
options are shown in the following diagram.

<!-- p.2556 -->

For more information about mail flow rules, including the full range of conditions and actions
that you can choose, see Mail flow rules (transport rules) in Exchange Server. Exchange Online
Protection (EOP) and hybrid customers can benefit from the mail flow rules best practices
provided in Best practices for configuring EOP. If you're ready to start creating rules, see
Procedures for mail flow rules in Exchange Server.

Inspect the content within attachments
You can use the mail flow rule conditions in the following table to examine the content of
attachments to messages. For these conditions, only the first 150 KB of an attachment is
inspected. In order to start using these conditions when inspecting messages, you need to add
them to a mail flow rule. Learn about creating or changing rules at Procedures for mail flow
rules in Exchange Server.

                                                                                     ﾉ   Expand table

 Condition name in       Condition name in the       Description
 EAC                     Shell

 Any attachment          AttachmentContainsWords     This condition matches messages with
 content includes any                                supported file type attachments that contain a
 of these words                                      specified string or group of characters.

<!-- p.2557 -->

 Condition name in         Condition name in the        Description
 EAC                       Shell

 Any attachment             AttachmentMatchesPatterns   This condition matches messages with
 content matches these                                  supported file type attachments that contain a
 text patterns                                          text pattern that matches a specified regular
                                                        expression.

The Exchange Management Shell names for the conditions listed here are parameters that
require the TransportRule cmdlet.

       Learn more about the cmdlet at New-TransportRule.

       Learn more about property types for these conditions at Mail flow rule conditions and
       exceptions (predicates) in Exchange Server.

Mail flow rules can inspect only the content of supported file types. If the mail flow rules agent
encounters an attachment that isn't in the list of supported file types, the
AttachmentIsUnsupported condition is triggered. The supported file types are listed in the

following section. Any file not listed will trigger the AttachmentIsUnsupported condition.

Compressed archive files
If the message contains a compressed archive file such as a .zip or .cab file, the mail flow
rules agent will inspect the files contained within that attachment. Such messages are
processed in a manner similar to messages that have multiple attachments. The properties of
compressed archive files aren't inspected. For example, if the container file type supports
comments, that field isn't inspected.

Supported file types for mail flow rule content
inspection
The following table lists the file types supported by mail flow rules. The system automatically
detects file types by inspecting file properties rather than the actual file name extension. This
behavior helps to prevent hackers from bypassing mail flow rule filtering by renaming a file
extension. A list of file types with executable code that can be checked within the context of
mail flow rules is listed later in this topic.

Starting with the Exchange Server 2019 CU15 (2025H1) release, Exchange Server uses
DocParser instead of the Oracle Outside In Technology         . This update also introduces support
for additional file types. If you are using Exchange Server 2019 CU15 or a later version, the
following file types can be inspected:

<!-- p.2558 -->

                                                                                      ﾉ   Expand table

Category           File extension                            Notes

Adobe PDF          .pdf                                      None

Compressed         .arj, .bz2, .cab, .chm, .gz, .gzip,       None
archive files      .lha, .lzh, .lzma, .mhtml, .msp, .rar,
                   .rar4, .tar, .xar, .xz, .zip, .7z

HTML               .ascx, .asp, .aspx, .css, .hta, .htm,     None
                   .html, .htw, .htx, .jhtml

JSON               .adaptivecard, .json, .messagecard        None

Mail               .eml, .msg, .nws                          None

Microsoft Office   .doc, .docb, .docm, .docx, .dot, .dotm,   The contents of any embedded parts
                   .dotx, .obd, .obt, .one, .pot, .potm,     contained within these file types are also
                   .potx, .ppa, .ppam, .pps, .ppsm, .ppsx,   inspected. However, any objects that
                   .ppt, .pptm, .pptx, .xlb, .xlc, .xlm,     aren't embedded (for example, linked
                   .xls, .xlsb, .xlsm, .xlsx, .xlt, .xltm,   documents) aren't inspected. Content
                   .xltx, .xlw                               within the custom properties is also
                                                             scanned.

Microsoft Office   .excelml, .powerpointml, .wordml          None
xml

Microsoft Visio    .vdw, .vdx, .vsd, .vsdm, .vsdx, .vss,     None
                   .vssm, .vssx, .vst, .vstm, .vstx, .vsx,
                   .vtx

OpenDocument       .odp, .ods, .odt                          No parts of .odf files are processed. For
                                                             example, if the .odf file contains an
                                                             embedded document, the contents of
                                                             that embedded document aren't
                                                             inspected.

Other              .dfx, .dxf, .encoffmetro, .fluid,         None
                   .mime, .pointpub, .pub, .rtf, .vtt,
                   .xps

Text               .asm, .bat, .c, .class, .cmd, .cpp,       Other files that are text based are also
                   .cs, .csv, .cxx, .def, .dic, .h, .hpp,    scanned. This list is representative.
                   .hxx, .ibq, .idl, .inc, .inf, .ini,
                   .inx, .java, .js, .json, .lnk, .log,
                   .m3u, messagestorage, .mpx, .php, .pl,
                   .pos, .tsv, .txt, .vcf, .vcs

XML                .infopathml, .jsp, .mspx, .xml            None

<!-- p.2559 -->

If you are using a version earlier than Exchange Server 2019 CU15 (2025H1), the following file
types can be inspected:

                                                                                        ﾉ    Expand table

 Category              File extension                     Notes

 Office 2013, Office   .docm, .docx, .pptm, .pptx,        Microsoft OneNote and Microsoft Publisher
 2010, and Office      .pub, .one, .xlsb, .xlsm, .xlsx    files aren't supported by default. You can
 2007                                                     enable support for these file types by using
                                                          IFilter integration. For more information, see
                                                          Register IFilters Filter Packs in Exchange
                                                          Server.

                                                          The contents of any embedded parts
                                                          contained within these file types are also
                                                          inspected. However, any objects that aren't
                                                          embedded (for example, linked documents)
                                                          aren't inspected.

 Office 2003           .doc, .ppt, .xls                   None

 Additional Office     .rtf, .vdw, .vsd, .vss, .vst       None
 files

 Adobe PDF             .pdf                               None

 HTML                  .html                              None

 XML                   .xml                               None

 Text                  .txt, .asm, .bat, .c, .cmd,        None
                       .cpp, .cxx, .def, .dic, .h,
                       .hpp, .hxx, .ibq, .idl, .inc,
                       inf, .ini, inx, .js, .log, .m3u,
                       .pl, .rc, .reg, .vbs, .wt

 OpenDocument          .odp, .ods, .odt                   No parts of .odf files are processed. For
                                                          example, if the .odf file contains an embedded
                                                          document, the contents of that embedded
                                                          document aren't inspected.

 AutoCAD Drawing       .dxf                               AutoCAD 2013 files aren't supported. Note:
                                                          File types can no longer be inspected after the
                                                          Exchange Server March 2024 SU was
                                                          installed.

 Image                 .jpg, .tiff                        Only the metadata text associated with these
                                                          image files is inspected. There's no optical
                                                          character recognition. Note: File types can no

<!-- p.2560 -->

 Category              File extension                     Notes

                                                          longer be inspected after the Exchange Server
                                                          March 2024 SU     was installed.

Inspect the file properties of attachments
The following mail flow rule conditions inspect the properties of a file that's attached to a
message. In order to start using these conditions when inspecting messages, you need to add
them to a mail flow rule. A list of supported file types with executable code that can be
checked within the context of mail flow rules is listed here. For more information about
creating or changing rules, see Procedures for mail flow rules in Exchange Server.

                                                                                       ﾉ     Expand table

 Condition name in      Condition name in the Shell          Description
 EAC

 Any attachment file    AttachmentNameMatchesPatterns        This condition matches messages with
 name matches these                                          supported file type attachments when
 text patterns                                               those attachments have a name that
                                                             contains the characters you specify.

 Any attachment file    AttachmentExtensionMatchesWords      This condition matches messages with
 extension includes                                          supported file type attachments when the
 these words                                                 file name extension matches what you
                                                             specify.

 Any attachment size    AttachmentSizeOver                   This condition matches messages with
 is greater than or                                          supported file type attachments when
 equal to                                                    those attachments are larger than the size
                                                             you specify.

 Any attachment         AttachmentProcessingLimitExceeded    This condition matches messages when an
 didn't complete                                             attachment isn't inspected by the mail flow
 scanning                                                    rules agent.

 Any attachment has     AttachmentHasExecutableContent       This condition matches messages that
 executable content                                          contain executable files as attachments.
                                                             The supported file types are listed here.

 Any attachment is      AttachmentIsPasswordProtected        This condition matches messages with
 password protected                                          supported file type attachments when
                                                             those attachments are protected by a
                                                             password.
