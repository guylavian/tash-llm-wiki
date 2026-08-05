---
title: "Exchange Server — pages 2481-2520"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2481-2520
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2481-2520
family: exchange
documentKind: "doc"
abstract: "Set-IRMConfiguration -JournalReportDecryptionEnabled $true For more information, see Enable or Disable Journal Report Decryption. Mail flow rules in Exchange Server Article • 04/30/2025 APPLIES TO: 2016 2019 Subscription Edition You can use mail flow rules (also known as transpo"
---

# Exchange Server — pages 2481-2520

<!-- p.2481 -->

       Set-IRMConfiguration -JournalReportDecryptionEnabled $true

For more information, see Enable or Disable Journal Report Decryption.

<!-- p.2482 -->

Mail flow rules in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

You can use mail flow rules (also known as transport rules) to identify and take action on
messages that flow through the transport pipeline in your Exchange 2016 and Exchange 2019
organization. Mail flow rules are similar to the Inbox rules that are available in Outlook and
Outlook on the web (formerly known as Outlook Web App). The main difference is mail flow
rules take action on messages while they're in transit, and not after the message is delivered to
the mailbox. Mail flow rules contain a richer set of conditions, exceptions, and actions, which
provides you with the flexibility to implement many types of messaging policies.

This article explains the components of mail flow rules, and how they work.

You can use the Exchange admin center (EAC) or the Exchange Management Shell to manage
mail flow rules. For instructions on how to manage mail flow rules, see Procedures for mail flow
rules in Exchange Server.

For each rule, you have the option of enforcing it, testing it, or testing it and notifying the
sender. To learn more about the testing options, see Test a mail flow rule and Policy Tips.

For steps to implement specific messaging policies, see the following topics:

      Organization-wide disclaimers, signatures, footers, or headers in Exchange Server

      Common message approval scenarios

      Using mail flow rules to inspect message attachments

Mail flow rule components
A rule is made of conditions, exceptions, actions, and properties:

      Conditions: Identify the messages that you want to apply the actions to. Some conditions
      examine message header fields (for example, the To, From, or Cc fields). Other conditions
      examine message properties (for example, the message subject, body, attachments,
      message size, or message classification). Most conditions require you to specify a
      comparison operator (for example, equals, doesn't equal, or contains) and a value to
      match. If there are no conditions or exceptions, the rule is applied to all messages.

      For a complete list of mail flow rule conditions, see Mail flow rule conditions and
      exceptions (predicates) in Exchange Server.

<!-- p.2483 -->

     Exceptions: Optionally identify the messages that the actions shouldn't apply to. The
     same message identifiers that are available in conditions are also available in exceptions.
     Exceptions override conditions and prevent the rule actions from being applied to a
     message, even if the message matches all of the configured conditions.

     Actions: Specify what to do to messages that match the conditions in the rule, and don't
     match any of the exceptions. There are many actions available, such as rejecting, deleting,
     or redirecting messages, adding additional recipients, adding prefixes in the message
     subject, or inserting disclaimers in the message body.

     For a complete list of mail flow rule actions available, see Mail flow rule actions in
     Exchange Server.

     Properties: Specify other rules settings that aren't conditions, exceptions or actions. For
     example, when the rule should be applied, whether to enforce or test the rule, and the
     time period when the rule is active. For more information, see the Mail flow rule
     properties section in this topic.

Multiple conditions, exceptions, and actions
The following table shows how multiple conditions, condition values, exceptions, and actions
are handled in a rule.

                                                                                           ﾉ   Expand table

 Component          Logic   Comments

 Multiple           AND     A message must match all the conditions in the rule. If you need to match one
 conditions                 condition or another, use separate rules for each condition. For example, if you
                            want to add the same disclaimer to messages with attachments and messages
                            that contain specific text, create one rule for each condition. In the EAC, you
                            can easily copy a rule.

 One condition      OR      Some conditions allow you to specify more than one value. The message must
 with multiple              match any one (not all) of the specified values. For example, if an email
 values                     message has the subject Stock price information, and the The subject includes
                            any of these words condition is configured to match the words Contoso or
                            stock, the condition is satisfied because the subject contains at least one of the
                            specified values.

 Multiple           OR      If a message matches any one of the exceptions, the actions are not applied to
 exceptions                 the message. The message doesn't have to match all the exceptions.

 Multiple actions   AND     Messages that match a rule's conditions get all the actions that are specified in
                            the rule. For example, if the actions Prepend the subject of the message with
                            and Add recipients to the Bcc box are selected, both actions are applied to

<!-- p.2484 -->

 Component         Logic      Comments

                              the message.
                              Keep in mind that some actions, such as the Delete the message without
                              notifying anyone action, prevent subsequent rules from being applied to a
                              message. Other actions such as Forward the message do not allow additional
                              actions.
                              You can also set an action on a rule so that when that rule is applied,
                              subsequent rules are not applied to the message.

Mail flow rule properties
The following table describes the rule properties that are available in mail flow rules.

                                                                                             ﾉ   Expand table

 Property name     Parameter name in the               Description
 in the EAC        Exchange Management
                   Shell

 Priority          Priority                            Indicates the order that the rules are applied to
                                                       messages. The default priority is based on when the
                                                       rule is created (older rules have a higher priority than
                                                       newer rules), and higher priority rules are processed
                                                       before lower priority rules.
                                                       You change the rule priority in the EAC by moving the
                                                       rule up or down in the list of rules. In the Exchange
                                                       Management Shell, you set the priority number (0 is
                                                       the highest priority).
                                                       For example, if you have one rule to reject messages
                                                       that include a credit card number, and another one
                                                       requiring approval, you'll want the reject rule to
                                                       happen first, and stop applying other rules.
                                                       For more information, see Set the priority of mail flow
                                                       rules.

 Audit this rule   SetAuditSeverity                    Sets the severity level of the incident report and the
 with severity                                         corresponding entry that's written to the message
 level                                                 tracking log when messages violate DLP policies.
                                                       Valid values are DoNotAudit, Low, Medium, and High.

 Mode              Mode                                You can specify whether you want the rule to start
                                                       processing messages immediately, or whether you
                                                       want to test rules without affecting the delivery of the
                                                       message (with or without Data Loss Prevention or
                                                       DLP Policy Tips).
                                                       Policy Tips are similar to MailTips, and can be
                                                       configured to present a brief note in Outlook or

<!-- p.2485 -->

Property name     Parameter name in the           Description
in the EAC        Exchange Management
                  Shell

                                                  Outlook on the web that provides information about
                                                  possible policy violations to the person that's creating
                                                  the message. For more information, see Policy
                                                  Tips.For more information about the modes, see Test
                                                  a mail flow rule.

Activate this     ActivationDate                  Specifies the date range when the rule is active.
rule on the       ExpiryDate
following date
Deactivate this
rule on the
following date

On check box      New rules: Enabled parameter    You can create a disabled rule, and enable it when
selected or not   on the New-TransportRule        you're ready to test it. Or, you can disable a rule
selected          cmdlet.                         without deleting it to preserve the settings. For
                  Existing rules: Use the         instructions, see Enable or disable mail flow rules.
                  Enable-TransportRule or
                  Disable-TransportRule
                  cmdlets.
                  The value is displayed in the
                  State property of the rule.

Defer the         RuleErrorAction                 You can specify how the message should be handled
message if rule                                   if the rule processing can't be completed. By default,
processing                                        the rule will be ignored, but you can choose to
doesn't                                           resubmit the message for processing.
complete

Match sender      SenderAddressLocation           If the rule uses conditions or exceptions that examine
address in                                        the sender's email address, you can look for the value
message                                           in the message header, the message envelope, or
                                                  both. For more information, see Senders.

Stop processing   SenderAddressLocation           This is an action for the rule, but it looks like a
more rules                                        property in the EAC. You can choose to stop applying
                                                  additional rules to a message after a rule processes a
                                                  message.

Comments          Comments                        Comments You can enter descriptive comments
                                                  about the rule.

How mail flow rules are applied

<!-- p.2486 -->

Mail flow rules are applied by a transport agent on Mailbox servers and Edge Transport servers.
On Mailbox servers, rules are applied by the Transport Rule agent. On Edge Transport servers,
rules are applied by Edge Rule agent. Although similar in functionality, the agents have some
differences. The important differences are summarized in the following table:

                                                                                        ﾉ    Expand table

 Transport         SMTP or categorizer event where rules are           Where rules are stored
 agent             invoked

 Transport Rule    The OnResolvedMessage categorizer event.            In Active Directory. Rules are
 agent on          In Exchange 2010, the Transport Rule agent was      available to all Mailbox servers in
 Mailbox           invoked on the OnRoutedMessage categorizer          the Active Directory forest.
 servers           event. The change to OnResolvedMessage allowed
                   new rule actions that can change how a message is
                   routed (for example, require TLS).

 Edge Rule         The OnEndOfData SMTP event                          In the local instance of Active
 agent on Edge                                                         Directory Lightweight Directory
 Transport                                                             Services (AD LDS) on the server.
 servers                                                               Rules are only applied to
                                                                       messages that flow through the
                                                                       local server.

For more information about transport agents, see Transport Agents in Exchange Server.

Differences in processing based on message type
There are several types of messages that flow through an organization. The following table
shows which messages types can be processed by mail flow rules.

                                                                                        ﾉ    Expand table

 Type of message                                               Can a rule be applied?

 Regular messages Messages that contain a single rich text     Yes
 format (RTF), HTML, or plain text message body or a
 multipart or alternative set of message bodies.

 S/MIME encrypted messages                                     Rules can only access envelope headers
                                                               and process messages based on
                                                               conditions that inspect those headers.
                                                               Rules with conditions that require
                                                               inspection of the message's content, or
                                                               actions that modify the message's
                                                               content can't be processed.

<!-- p.2487 -->

 Type of message                                                Can a rule be applied?

 RMS Protected messages: Messages that are protected by         Rules can always access envelope headers
 applying an Active Directory Rights Management Services        and process messages based on
 (AD RMS) rights policy template.                               conditions that inspect those headers.For
                                                                a rule to inspect or modify a protected
                                                                message's content, your need to:
                                                                     Have transport decryption set to
                                                                     Mandatory or Optional. By default,
                                                                      Transport decryption is set to
                                                                      Optional.
                                                                      Have the encryption key

                                                                .

 Clear-signed messages: Messages that have been signed but      Yes
 not encrypted.

 UM messages: Messages that are created or processed by         Yes
 the Unified Messaging service in Exchange 2016, such as
 voice mail, fax, missed call notifications, and messages
 created or forwarded by using Microsoft Outlook Voice
 Access. (Note: Unified Messaging is not available in
 Exchange 2019.)

 Anonymous messages: Messages that were sent by                 Yes
 anonymous senders.

 Read reports: Reports that are generated in response to read   Yes
 receipt requests by senders. Read reports have a message
 class of IPM.Note*.MdnRead or IPM.Note*.MdnNotRead .

Rule storage and replication
Mail flow rules that you create and configure on Mailbox servers are stored in Active Directory,
and they're read and applied by the Transport service on all Mailbox servers in the
organization. When you create, modify, or remove a mail flow rule, the change is replicated
between the domain controllers in your organization. This allows Exchange to provide a
consistent set of mail flow rules across the organization.

Notes:

     Replication between domain controllers depends on factors that aren't controlled by
     Exchange (for example, the number of Active Directory sites, and the speed of network
     links). Therefore, you need to consider replication delays when you implement mail flow
     rules in your organization. For more information about Active Directory replication, see

<!-- p.2488 -->

     Introduction to Active Directory Replication and Topology Management Using Windows
     PowerShell.

     Each Mailbox server caches expanded distribution groups to avoid repeated Active
     Directory queries to determine a group's membership. By default, entries in the expanded
     groups cache expire every four hours. Therefore, changes to the group's membership
     aren't detected by mail flow rules until the expanded groups cache is updated. To force
     an immediate update of the cache on a Mailbox server, restart the Microsoft Exchange
     Transport service. You need to restart the service on each Mailbox server where you want
     to forcibly update the cache.

Mail flow rules that you create and configure on Edge Transport servers are stored in the local
instance of AD LDS on the server. No automated replication of mail flow rules occurs on Edge
Transport servers. Rules on the Edge Transport server apply only to messages that flow through
the local server. If you need to apply the same set of mail flow rules on multiple Edge Transport
servers, you can clone the Edge Transport server configuration, or export and import the mail
flow rules. For more information, see Edge Transport Server Cloned Configuration and Import
or export mail flow rule collections.

Whenever the Transport service on a Mailbox server or Edge Transport server detects a
modified mail flow rule, an event is logged in the Application log in the Event Viewer (Event ID
4002 on Mailbox servers, and Event ID 16028 on Edge Transport servers).

Rule replication and storage in mixed environments

There are two mixed environment scenarios that are common:

     Hybrid deployments where part of your organization resides in Microsoft 365 or Office
     365

     In a hybrid environment, there's no replication of rules between your on-premises
     Exchange organization and Microsoft 365 or Office 365. Therefore, when you create a rule
     in Exchange, you need to create a matching rule in Microsoft 365 or Office 365. Rules you
     create in Microsoft 365 or Office 365 are stored in the cloud, whereas the rules you create
     in your on-premises organization are stored locally in Active Directory. When you manage
     rules in a hybrid environment, you need to keep the two sets of rules synchronized by
     making the change in both places, or making the change in one environment and then
     exporting the rules and importing them in the other environment.

     Important: Even though there is a substantial overlap between the conditions and actions
     that are available in Microsoft 365 or Office 365 and Exchange Server, there are
     differences. If you plan on creating the same rule in both locations, make sure that all

<!-- p.2489 -->

conditions and actions you plan to use are available. To see the list of available conditions
and actions that are available in Microsoft 365 or Office 365, see the following topics:

Mail flow rule conditions and exceptions (predicates) in Exchange Online

Mail flow rule actions in Exchange Online

Coexistence with Exchange 2010

  ７ Note

  This section applies to Exchange 2016 only.

When you coexist with Exchange 2010, all mail flow rules are stored in Active Directory
and replicated across your organization regardless of the Exchange Server version you
used to create the rules. However, all mail flow rules are associated with the Exchange
server version that was used to create them and are stored in a version-specific container
in Active Directory. When you first deploy Exchange 2016 in your organization, any
existing rules are imported to Exchange 2016 as part of the setup process. However, any
changes afterwards would need to be made with both versions. For example, if you
change an existing rule in Exchange 2016 (Exchange Management Shell or the EAC), you
need to make the same change in Exchange 2010 (Exchange Management Shell or the
Exchange Management Console).

Exchange 2010 can't process rules that have the Version or RuleVersion value 15.n.n.n. To
be sure all your rules can be processed, only use rules that have the value 14.n.n.n.

<!-- p.2490 -->

Mail flow rule conditions and exceptions
(predicates) in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Conditions and exceptions in mail flow rules (also known as transport rules) identify the messages that the rule is
applied to or not applied to. For example, if the rule adds a disclaimer to messages, you can configure the rule to
only apply to messages that contain specific words, messages sent by specific users, or to all messages except
those sent by the members of a specific group. Collectively, the conditions and exceptions in mail flow rules are
also known as predicates, because for every condition, there's a corresponding exception that uses the exact
same settings and syntax. The only difference is conditions specify messages to include, while exceptions specify
messages to exclude.

Most conditions and exceptions have one property that requires one or more values. For example, the The
sender is condition requires the sender of the message. Some conditions have two properties. For example, the
A message header includes any of these words condition requires one property to specify the message header
field, and a second property to specify the text to look for in the header field. Some conditions or exceptions
don't have any properties. For example, the Any attachment has executable content condition simply looks for
attachments in messages that have executable content.

For more information about mail flow rules in Exchange Server, including how multiple conditions/exceptions or
multi-valued conditions/exceptions are handled, see Mail flow rules in Exchange Server.

For more information about conditions and exceptions in mail flow rules in Exchange Online Protection or
Exchange Online, see Mail flow rule conditions and exceptions (predicates) in Exchange Online.

Conditions and exceptions for mail flow rules on Mailbox
servers
The tables in the following sections describe the conditions and exceptions that are available in mail flow rules
on Mailbox servers. The properties types are described in the Property types section.

Senders

Recipients

Message subject or body

Attachments

Any recipients

Message sensitive information types, To and Cc values, size, and character sets

Sender and recipient

Message properties

Message headers

<!-- p.2491 -->

  ７ Note

       After you select a condition or exception in the Exchange admin center (EAC), the value that's
       ultimately shown in the Apply this rule if or Except if field is often different (shorter) than the click
       path value you selected. Also, when you create new rules based on a template (a filtered list of
       scenarios), you can often select a short condition name instead of following the complete click path.
       The short names and full click path values are shown in the EAC column in the tables.

       If you select [Apply to all messages] in the EAC, you can't specify any other conditions. The equivalent
       in the Exchange Management Shell is to create a rule without specifying any condition parameters.

       The settings and properties are the same in conditions and exceptions, so the output of the Get-
       TransportRulePredicate cmdlet doesn't list exceptions separately. Also, the names of some of the
       predicates that are returned by this cmdlet are different than the corresponding parameter names, and
       a predicate might require multiple parameters.

Senders
For conditions and exceptions that examine the sender's address, you can specify where rule looks for the
sender's address.

In the EAC, in the Properties of this rule section, select Match sender address in message. You might need to
select More options to see this setting. In the Exchange Management Shell, the parameter is
SenderAddressLocation. The available values are:

     Header: Only examine senders in the message headers (for example, the From, Sender, or Reply-To fields).
     This is the default value, and is the way mail flow rules worked before Exchange 2013 Cumulative Update 1
     (CU1).

     Envelope: Only examine senders from the message envelope (the MAIL FROM value that was used in the
     SMTP transmission, which is typically stored in the Return-Path field). Message envelope searching is
     available only for the following conditions (and the corresponding exceptions):
        The sender is (From)
        The sender is a member of (FromMemberOf)
        The sender address includes (FromAddressContainsWords)
        The sender address matches (FromAddressMatchesPatterns)
        The sender's domain is (SenderDomainIs)

     Header or envelope ( HeaderOrEnvelope ): Examine senders in the message header and the message
     envelope.

                                                                                                     ﾉ   Expand table

<!-- p.2492 -->

Condition or        Condition and exception parameters in      Property type     Description                      Available
exception in        the Exchange Management Shell                                                                 in
the EAC

The sender is       From                                       Addresses         Messages that are sent by the    Exchange
                    ExceptIfFrom                                                 specified mailboxes, mail        2010 or
The sender > is                                                                  users, or mail contacts in the   later
this person                                                                      Exchange organization.

The sender is       FromScope                                  UserScopeFrom     Messages that are sent by        Exchange
located             ExceptIfFromScope                                            either internal senders or       2010 or
                                                                                 external senders.                later
The sender > is
external/internal

The sender is a     FromMemberOf                               Addresses         Messages that are sent by a      Exchange
member of           ExceptIfFromMemberOf                                         member of the specified          2010 or
                                                                                 group.                           later
The sender > is
a member of
this group

The sender          FromAddressContainsWords                   Words             Messages that contain the        Exchange
address includes    ExceptIfFromAddressContainsWords                             specified words in the           2010 or
                                                                                 sender's email address.          later
The sender >
address includes
any of these
words

The sender          FromAddressMatchesPatterns                 Patterns          Messages where the sender's      Exchange
address matches     ExceptIfFromAddressMatchesPatterns                           email address contains text      2010 or
                                                                                 patterns that match the          later
The sender >                                                                     specified regular expressions.
address matches
any of these text
patterns

The sender's        SenderADAttributeContainsWords             First property:   Messages where the specified     Exchange
specified           ExceptIfSenderADAttributeContainsWords     ADAttribute       Active Directory attribute of    2010 or
properties                                                                       the sender contains any of the   later
include any of                                                 Second            specified words.
these words                                                    property: Words
                                                                                 The Country attribute
The sender >                                                                     requires the two-letter
has specific                                                                     country code value (for
properties                                                                       example, DE for Germany).
including any of
these words

The sender's        SenderADAttributeMatchesPatterns           First property:   Messages where the specified     Exchange
specified           ExceptIfSenderADAttributeMatchesPatterns   ADAttribute       Active Directory attribute of    2010 or
properties                                                                       the sender contains text         later
match these text                                               Second            patterns that match the
patterns                                                       property:         specified regular expressions.
                                                               Patterns
The sender >
has specific
properties

<!-- p.2493 -->

Condition or        Condition and exception parameters in   Property type     Description                         Available
exception in        the Exchange Management Shell                                                                 in
the EAC

matching these
text patterns

The sender has      HasSenderOverride                       n/a               Messages where the sender           Exchange
overridden the      ExceptIfHasSenderOverride                                 has chosen to override a data       2013 or
Policy Tip                                                                    loss prevention (DLP) policy.       later
                                                                              For more information about
The sender >                                                                  DLP policies, see Data loss
has overridden                                                                prevention in Exchange
the Policy Tip                                                                Server.

Sender's IP         SenderIPRanges                          IPAddressRanges   Messages where the sender's         Exchange
address is in the   ExceptIfSenderIPRanges                                    IP address matches the              2013 or
range                                                                         specified IP address, or falls      later
                                                                              within the specified IP address
The sender > IP                                                               range.
address is in any
of these ranges
or exactly
matches

The sender's        SenderDomainIs                          DomainName        Messages where the domain           Exchange
domain is           ExceptIfSenderDomainIs                                    of the sender's email address       2013 or
                                                                              matches the specified value.        later
The sender >                                                                  This predicate will match
domain is                                                                     domains and subdomains
                                                                              with domain provided. For
                                                                              example:

                                                                              For the value "domain.com",
                                                                              both domain "domain.com"
                                                                              and subdomain
                                                                              "subdomain.domain.com" will
                                                                              be matched.

                                                                              If you need to find sender
                                                                              domains that contain the
                                                                              specified domain (for
                                                                              example, any subdomain of a
                                                                              domain), use The sender
                                                                              address matches
                                                                              (FromAddressMatchesPatterns)
                                                                              condition and specify the
                                                                              domain by using the syntax:
                                                                              '\.domain\.com$' .

Recipients

                                                                                                          ﾉ    Expand table

<!-- p.2494 -->

Condition or         Condition and exception parameters in     Property      Description                          Available
exception in the     the Exchange Management Shell             type                                               in
EAC

The recipient is     SentTo                                    Addresses     Messages where one of the            Exchange
                     ExceptIfSentTo                                          recipients is the specified          2010 or
The recipient >                                                              mailbox, mail user, or mail          later
is this person                                                               contact in the Exchange
                                                                             organization. The recipients can
                                                                             be in the To, Cc, or Bcc fields of
                                                                             the message.

                                                                             Note: You can't specify
                                                                             distribution groups or mail-
                                                                             enabled security groups. If you
                                                                             need to take action on messages
                                                                             that are sent to a group, use the
                                                                             To box contains (AnyOfToHeader)
                                                                             condition instead.

The recipient is     SentToScope                               UserScopeTo   Messages that are sent to internal   Exchange
located              ExceptIfSentToScope                                     recipients, external recipients,     2010 or
                                                                             external recipients in partner       later
The recipient >                                                              organizations, or external
is                                                                           recipients in non-partner
external/external                                                            organizations.

The recipient is a   SentToMemberOf                            Addresses     Messages that contain recipients     Exchange
member of            ExceptIfSentToMemberOf                                  who are members of the               2010 or
                                                                             specified group. The group can       later
The recipient >                                                              be in the To, Cc, or Bcc fields of
is a member of                                                               the message.
this group

The recipient        RecipientAddressContainsWords             Words         Messages that contain the            Exchange
address includes     ExceptIfRecipientAddressContainsWords                   specified words in the recipient's   2010 or
                                                                             email address.                       later
The recipient >
address includes                                                             Note: This condition or exception
any of these                                                                 doesn't consider messages that
words                                                                        are sent to recipient proxy
                                                                             addresses. It only matches
                                                                             messages that are sent to the
                                                                             recipient's primary email address.

The recipient        RecipientAddressMatchesPatterns           Patterns      Messages where a recipient's         Exchange
address matches      ExceptIfRecipientAddressMatchesPatterns                 email address contains text          2010 or
                                                                             patterns that match the specified    later
The recipient >                                                              regular expressions.
address matches
any of these text                                                            Note: This condition or exception
patterns                                                                     doesn't consider messages that
                                                                             are sent to recipient proxy
                                                                             addresses. It only matches
                                                                             messages that are sent to the
                                                                             recipient's primary email address.

<!-- p.2495 -->

Condition or       Condition and exception parameters in         Property      Description                            Available
exception in the   the Exchange Management Shell                 type                                                 in
EAC

The recipient's    RecipientADAttributeContainsWords             First         Messages where the specified           Exchange
specified          ExceptIfRecipientADAttributeContainsWords     property:     Active Directory attribute of a        2010 or
properties                                                       ADAttribute   recipient contains any of the          later
include any of                                                                 specified words.
these words                                                      Second
                                                                 property:     The Country attribute requires
The recipient >                                                  Words         the two-letter country code value
has specific                                                                   (for example, DE for Germany).
properties
including any of
these words

The recipient's    RecipientADAttributeMatchesPatterns           First         Messages where the specified           Exchange
specified          ExceptIfRecipientADAttributeMatchesPatterns   property:     Active Directory attribute of a        2010 or
properties                                                       ADAttribute   recipient contains text patterns       later
match these text                                                               that match the specified regular
patterns                                                         Second        expressions.
                                                                 property:
The recipient >                                                  Patterns
has specific
properties
matching these
text patterns

A recipient's      RecipientDomainIs                             DomainName    Messages where the domain of a         Exchange
domain is          ExceptIfRecipientDomainIs                                   recipient's email address matches      2013 or
                                                                               the specified value.                   later
The recipient >
domain is                                                                      If you need to find recipient
                                                                               domains that contain the
                                                                               specified domain (for example,
                                                                               any subdomain of a domain), use
                                                                               The recipient address matches
                                                                               (RecipientAddressMatchesPatterns)
                                                                               condition, and specify the domain
                                                                               by using the syntax
                                                                               '\.domain\.com$' .

Message subject or body

 ７ Note

 The search for words or text patterns in the subject or other header fields in the message occurs after the
 message has been decoded from the MIME content transfer encoding method that was used to transmit
 the binary message between SMTP servers in ASCII text. You can't use conditions or exceptions to search for
 the raw (typically, Base64) encoded values of the subject or other header fields in messages.

                                                                                                          ﾉ      Expand table

<!-- p.2496 -->

 Condition or           Condition and exception parameters in      Property     Description                       Available
 exception in the       the Exchange Management Shell              type                                           in
 EAC

 The subject or         SubjectOrBodyContainsWords                 Words        Messages that have the            Exchange
 body includes          ExceptIfSubjectOrBodyContainsWords                      specified words in the            2010 or
                                                                                Subject field or message          later
 The subject or                                                                 body.
 body > subject or
 body includes any
 of these words

 The subject or         SubjectOrBodyMatchesPatterns               Patterns     Messages where the Subject        Exchange
 body matches           ExceptIfSubjectOrBodyMatchesPatterns                    field or message body             2010 or
                                                                                contain text patterns that        later
 The subject or                                                                 match the specified regular
 body > subject or                                                              expressions.
 body matches
 these text patterns

 The subject            SubjectContainsWords                       Words        Messages that have the            Exchange
 includes               ExceptIfSubjectContainsWords                            specified words in the            2010 or
                                                                                Subject field.                    later
 The subject or
 body > subject
 includes any of
 these words

 The subject            SubjectMatchesPatterns                     Patterns     Messages where the Subject        Exchange
 matches                ExceptIfSubjectMatchesPatterns                          field contains text patterns      2010 or
                                                                                that match the specified          later
 The subject or                                                                 regular expressions.
 body > subject
 matches these text
 patterns

Attachments
For more information about how mail flow rules inspect message attachments, see Using mail flow rules to
inspect message attachments.

                                                                                                            ﾉ   Expand table

 Condition or        Condition and exception parameters in      Property type           Description                Available
 exception in        the Exchange Management Shell                                                                 in
 the EAC

 Any                 AttachmentContainsWords                    Words                   Messages where an          Exchange
 attachment's        ExceptIfAttachmentContainsWords                                    attachment contains the    2010 or
 content                                                                                specified words.           later
 includes

 Any
 attachment >
 content

<!-- p.2497 -->

Condition or      Condition and exception parameters in     Property type   Description                 Available
exception in      the Exchange Management Shell                                                         in
the EAC

includes any of
these words

Any               AttachmentMatchesPatterns                 Patterns        Messages where an           Exchange
attachments       ExceptIfAttachmentMatchesPatterns                         attachment contains text    2010 or
content                                                                     patterns that match the     later
matches                                                                     specified regular
                                                                            expressions.
Any
attachment >                                                                Note: Only the first 150
content                                                                     kilobytes (KB) of the
matches these                                                               attachments are
text patterns                                                               scanned.

Any               AttachmentIsUnsupported                   n/a             Messages where an           Exchange
attachment's      ExceptIfAttachmentIsUnsupported                           attachment isn't natively   2010 or
content can't                                                               recognized by Exchange,     later
be inspected                                                                and the required IFilter
                                                                            isn't installed on the
Any                                                                         Mailbox server. For more
attachment >                                                                information, see Register
content can't                                                               Filter Pack IFilters with
be inspected                                                                Exchange Server.

Any               AttachmentNameMatchesPatterns             Patterns        Messages where an           Exchange
attachment's      ExceptIfAttachmentNameMatchesPatterns                     attachment's file name      2010 or
file name                                                                   contains text patterns      later
matches                                                                     that match the specified
                                                                            regular expressions.
Any
attachment >
file name
matches these
text patterns

Any               AttachmentExtensionMatchesWords           Words           Messages where an           Exchange
attachment's      ExceptIfAttachmentExtensionMatchesWords                   attachment's file           2013 or
file extension                                                              extension matches any       later
matches                                                                     of the specified words.

Any
attachment >
file extension
includes these
words

Any               AttachmentSizeOver                        Size            Messages where any          Exchange
attachment is     ExceptIfAttachmentSizeOver                                attachment is greater       2010 or
greater than or                                                             than or equal to the        later
equal to                                                                    specified value.

Any                                                                         In the EAC, you can only
attachment >                                                                specify the size in
size is greater                                                             kilobytes (KB).

<!-- p.2498 -->

Condition or     Condition and exception parameters in       Property type        Description                  Available
exception in     the Exchange Management Shell                                                                 in
the EAC

than or equal
to

The message      AttachmentProcessingLimitExceeded           n/a                  Messages where the           Exchange
didn't           ExceptIfAttachmentProcessingLimitExceeded                        rules engine couldn't        2013 or
complete                                                                          complete the scanning        later
scanning                                                                          of the attachments. You
                                                                                  can use this condition to
Any                                                                               create rules that work
attachment >                                                                      together to identify and
didn't                                                                            process messages where
complete                                                                          the content couldn't be
scanning                                                                          fully scanned.

Any              AttachmentHasExecutableContent              n/a                  Messages where an            Exchange
attachment       ExceptIfAttachmentHasExecutableContent                           attachment is an             2013 or
has executable                                                                    executable file. The         later
content                                                                           system inspects the file's
                                                                                  properties rather than
Any                                                                               relying on the file's
attachment >                                                                      extension.
has executable
content

Any              AttachmentIsPasswordProtected               n/a                  Messages where an            Exchange
attachment is    ExceptIfAttachmentIsPasswordProtected                            attachment is password       2013 or
password                                                                          protected (and therefore     later
protected                                                                         can't be scanned).
                                                                                  Password detection only
Any                                                                               works for Office
attachment >                                                                      documents, .zip files,
is password                                                                       and .7z files.
protected

has these        AttachmentPropertyContainsWords             First property:      Messages where the           Exchange
properties,      ExceptIfAttachmentPropertyContainsWords     DocumentProperties   specified property of an     2016 or
including any                                                                     attached Office              later
of these words                                               Second property:     document contains the
                                                             Words                specified words. This
Any                                                                               condition helps you
attachment >                                                                      integrate mail flow rules
has these                                                                         with SharePoint, File
properties,                                                                       Classification
including any                                                                     Infrastructure (FCI) in
of these words                                                                    Windows Server 2012 R2
                                                                                  or later, or a third-party
                                                                                  classification system.

                                                                                  You can select from a list
                                                                                  of built-in properties, or
                                                                                  specify a custom
                                                                                  property.

Any recipients

<!-- p.2499 -->

The conditions and exceptions in this section provide a unique capability that affects all recipients when the
message contains at least one of the specified recipients. For example, let's say you have a rule that rejects
messages. If you use a recipient condition from the Recipients section, the message is only rejected for those
specified recipients. For example, if the rule finds the specified recipient in a message, but the message contains
five other recipients. The message is rejected for that one recipient, and is delivered to the five other recipients.

If you add a recipient condition from this section, that same message is rejected for the detected recipient and
the five other recipients.

Conversely, a recipient exception from this section prevents the rule action from being applied to all recipients of
the message, not just for the detected recipients.

  ７ Note

  This condition or exception doesn't consider messages that are sent to recipient proxy addresses. It only
  matches messages that are sent to the recipient's primary email address.

                                                                                                        ﾉ      Expand table

 Condition or        Condition and exception parameters in the       Property   Description                     Available
 exception in the    Exchange Management Shell                       type                                       in
 EAC

 Any recipient       AnyOfRecipientAddressContainsWords              Words      Messages that contain           Exchange
 address includes    ExceptIfAnyOfRecipientAddressContainsWords                 the specified words in the      2013 or
                                                                                To, Cc, or Bcc fields of the    later
 Any recipient >                                                                message.
 address includes
 any of these
 words

 Any recipient       AnyOfRecipientAddressMatchesPatterns            Patterns   Messages where the To,          Exchange
 address matches     ExceptIfAnyOfRecipientAddressMatchesPatterns               Cc, or Bcc fields contain       2013 or
                                                                                text patterns that match        later
 Any recipient >                                                                the specified regular
 address matches                                                                expressions.
 any of these text
 patterns

Message sensitive information types, To and Cc values, size, and
character sets
The conditions in this section that look for values in the To and Cc fields behave like the conditions in the Any
recipients section (all recipients of the message are affected by the rule, not just the detected recipients).

  ７ Note

  The recipient conditions in this section do not consider messages that are sent to recipient proxy addresses.
  They only match messages that are sent to the recipient's primary email address.

<!-- p.2500 -->

                                                                                                         ﾉ     Expand table

Condition or    Condition and exception parameters in        Property type               Description              Available
exception in    the Exchange Management Shell                                                                     in
the EAC

The message     MessageContainsDataClassifications           SensitiveInformationTypes   Messages that            Exchange
contains        ExceptIfMessageContainsDataClassifications                               contain sensitive        2013 or
sensitive                                                                                information as           later
information                                                                              defined by data loss
                                                                                         prevention (DLP)
The message                                                                              policies.
> contains
any of these                                                                             This condition is
types of                                                                                 required for rules
sensitive                                                                                that use the Notify
information                                                                              the sender with a
                                                                                         Policy Tip
                                                                                         (NotifySender)
                                                                                         action.

The To box      AnyOfToHeader                                Addresses                   Messages where           Exchange
contains        ExceptIfAnyOfToHeader                                                    the To field includes    2010 or
                                                                                         any of the specified     later
The message                                                                              recipients.
> To box
contains this
person

The To box      AnyOfToHeaderMemberOf                        Addresses                   Messages where           Exchange
contains a      ExceptIfAnyOfToHeaderMemberOf                                            the To field             2010 or
member of                                                                                contains a recipient     later
                                                                                         who is a member of
The message                                                                              the specified group.
> To box
contains a
member of
this group

The Cc box      AnyOfCcHeader                                Addresses                   Messages where           Exchange
contains        ExceptIfAnyOfCcHeader                                                    the Cc field             2010 or
                                                                                         includes any of the      later
The message                                                                              specified recipients.
> Cc box
contains this
person

The Cc box      AnyOfCcHeaderMemberOf                        Addresses                   Messages where           Exchange
contains a      ExceptIfAnyOfCcHeaderMemberOf                                            the Cc field             2010 or
member of                                                                                contains a recipient     later
                                                                                         who is a member of
The message                                                                              the specified group.
> contains a
member of
this group

The To or Cc    AnyOfToCcHeader                              Addresses                   Messages where           Exchange
box contains    ExceptIfAnyOfToCcHeader                                                  the To or Cc fields      2010 or
                                                                                                                  later

<!-- p.2501 -->

Condition or      Condition and exception parameters in      Property type   Description             Available
exception in      the Exchange Management Shell                                                      in
the EAC

The message                                                                  contain any of the
> To or Cc                                                                   specified recipients.
box contains
this person

The To or Cc      AnyOfToCcHeaderMemberOf                    Addresses       Messages where          Exchange
box contains      ExceptIfAnyOfToCcHeaderMemberOf                            the To or Cc fields     2010 or
a member of                                                                  contain a recipient     later
                                                                             who is a member of
The message                                                                  the specified group.
> To or Cc
box contains
a member of
this group

The message       MessageSizeOver                            Size            Messages where          Exchange
size is greater   ExceptIfMessageSizeOver                                    the total size          2013 or
than or equal                                                                (message plus           later
to                                                                           attachments) is
                                                                             greater than or
The message                                                                  equal to the
> size is                                                                    specified value.
greater than
or equal to                                                                  In the EAC, you can
                                                                             only specify the size
                                                                             in kilobytes (KB).

                                                                             Note: Message size
                                                                             limits on mailboxes
                                                                             are evaluated
                                                                             before mail flow
                                                                             rules. A message
                                                                             that's too large for
                                                                             a mailbox is
                                                                             rejected before a
                                                                             rule with this
                                                                             condition is able to
                                                                             act on the message.

The message       ContentCharacterSetContainsWords           CharacterSets   Messages that have      Exchange
character set     ExceptIfContentCharacterSetContainsWords                   any of the specified    2013 or
name                                                                         character set           later
includes any                                                                 names.
of these
words

The message
> character
set name
includes any
of these
words

<!-- p.2502 -->

Sender and recipient

                                                                                                       ﾉ      Expand table

Condition or        Condition and exception parameters in    Property type            Description               Available
exception in the    the Exchange Management Shell                                                               in
EAC

The sender is       SenderManagementRelationship             ManagementRelationship   Messages where            Exchange
one of the          ExceptIfSenderManagementRelationship                              either sender is the      2010 or
recipient's                                                                           manager of a              later
                                                                                      recipient, or the
The sender and                                                                        sender is managed
the recipient >                                                                       by a recipient.
the sender's
relationship to a
recipient is

The message is      BetweenMemberOf1 and                     Addresses                Messages that are         Exchange
between             BetweenMemberOf2                                                  sent between              2010 or
members of          ExceptIfBetweenMemberOf1 and                                      members of the            later
these groups        ExceptIfBetweenMemberOf2                                          specified groups.

The sender and
the recipient >
the message is
between
members of
these groups

The manager of      ManagerForEvaluatedUser and              First property:          Messages where            Exchange
the sender or       ManagerAddress                           EvaluatedUser            either a specified        2010 or
recipient is        ExceptIfManagerForEvaluatedUser and                               user is the manager       later
                    ExceptIfManagerAddress                   Second property:         of the sender, or a
The sender and                                               Addresses                specified user is the
the recipient >                                                                       manager of a
the manager of                                                                        recipient.
the sender or
recipient is this
person

The sender's and    ADAttributeComparisonAttribute and       First property:          Messages where            Exchange
any recipient's     ADComparisonOperator                     ADAttribute              the specified Active      2010 or
property            ExceptIfADAttributeComparisonAttribute                            Directory attribute       later
compares as         and ExceptIfADComparisonOperator         Second property:         for the sender and
                                                             Evaluation               recipient either
The sender and                                                                        match or don't
the recipient >                                                                       match.
the sender and
recipient
property
compares as

Message properties

<!-- p.2503 -->

                                                                                                      ﾉ     Expand table

Condition or      Condition and exception       Property type           Description                           Available
exception in      parameters in the Exchange                                                                  in
the EAC           Management Shell

The message       MessageTypeMatches            MessageType             Messages of the specified type.       Exchange
type is           ExceptIfMessageTypeMatches                                                                  2010 or
                                                                        Note: When Outlook or Outlook         later
The message                                                             on the web is configured to
properties >                                                            forward a message, the
include the                                                             ForwardingSmtpAddress
message type                                                            property is added to the message.
                                                                        The message type isn't changed
                                                                        to AutoForward .

The message is    HasClassification             MessageClassification   Messages that have the specified      Exchange
classified as     ExceptIfHasClassification                             message classification. This is a     2010 or
                                                                        custom message classification         later
The message                                                             that you can create in your
properties >                                                            organization by using the New-
include this                                                            MessageClassification cmdlet.
classification

The message       HasNoClassification           n/a                     Messages that don't have a            Exchange
isn't marked      ExceptIfHasNoClassification                           message classification.               2010 or
with any                                                                                                      later
classifications

The message
properties >
don't include
any
classification

The message       SCLOver                       SCLValue                Messages that are assigned a          Exchange
has an SCL        ExceptIfSCLOver                                       spam confidence level (SCL) that's    2010 or
greater than or                                                         greater than or equal to the          later
equal to                                                                specified value.

The message
properties >
include an SCL
greater than or
equal to

The message       WithImportance                Importance              Messages that are marked with         Exchange
importance is     ExceptIfWithImportance                                the specified Importance level.       2010 or
set to                                                                                                        later

The message
properties >
include the
importance
level

Message headers

<!-- p.2504 -->

  ７ Note

  The search for words or text patterns in the subject or other header fields in the message occurs after the
  message has been decoded from the MIME content transfer encoding method that was used to transmit
  the binary message between SMTP servers in ASCII text. You can't use conditions or exceptions to search for
  the raw (typically, Base64) encoded values of the subject or other header fields in messages.

                                                                                                        ﾉ      Expand table

 Condition or    Condition and exception parameters in    Property type           Description                    Available
 exception in    the Exchange Management Shell                                                                   in
 the EAC

 A message       HeaderContainsMessageHeader and          First property:         Messages that contain          Exchange
 header          HeaderContainsWords                      MessageHeaderField      the specified header           2010 or
 includes        ExceptIfHeaderContainsMessageHeader                              field, and the value of        later
                 and ExceptIfHeaderContainsWords          Second property:        that header field
 A message                                                Words                   contains the specified
 header >                                                                         words.
 includes any
 of these                                                                         The name of the header
 words                                                                            field and the value of the
                                                                                  header field are always
                                                                                  used together.

 A message       HeaderMatchesMessageHeader and           First property:         Messages that contain          Exchange
 header          HeaderMatchesPatterns                    MessageHeaderField      the specified header           2010 or
 matches         ExceptIfHeaderMatchesMessageHeader and                           field, and the value of        later
                 ExceptIfHeaderMatchesPatterns            Second property:        that header field
 A message                                                Patterns                contains the specified
 header >                                                                         regular expressions.
 matches these
 text patterns                                                                    The name of the header
                                                                                  field and the value of the
                                                                                  header field are always
                                                                                  used together.

Conditions and exceptions for mail flow rules on Edge
Transport servers
The conditions and exceptions that are available in mail flow rules on Edge Transport servers are a small subset
of what's available on Mailbox servers. There's no EAC on Edge Transport servers, so you can only manage mail
flow rules in the Exchange Management Shell on the local Edge Transport server. The conditions and exceptions
are described in the following table. The properties types are described in the Property types section.

                                                                                                        ﾉ      Expand table

 Condition and exception parameters in the      Property type           Description                              Available
 Exchange Management Shell                                                                                       in

 AnyOfRecipientAddressContainsWords             Words                   Messages that contain the specified      Exchange
 ExceptIfAnyOfRecipientAddressContainsWords                             words in the To, Cc, or Bcc fields.      2013 or

<!-- p.2505 -->

Condition and exception parameters in the      Property type        Description                               Available
Exchange Management Shell                                                                                     in

                                                                                                              later
                                                                    When a message contains the
                                                                    specified recipient, the rule action is
                                                                    applied (or not applied) to all
                                                                    recipients of the message. For
                                                                    example, the message is rejected
                                                                    for all recipients of the message,
                                                                    not just for the specified recipient.

AnyOfRecipientAddressMatchesPatterns           Patterns             Messages where the To, Cc, or Bcc         Exchange
ExceptIfAnyOfRecipientAddressMatchesPatterns                        fields contain text patterns that         2013 or
                                                                    match the specified regular               later
                                                                    expressions.

                                                                    When a message contains the
                                                                    specified recipient, the rule action is
                                                                    applied (or not applied) to all
                                                                    recipients of the message. For
                                                                    example, the message is rejected
                                                                    for all recipients of the message,
                                                                    not just for the specified recipient.

AttachmentSizeOver                             Size                 Messages with attachments where           Exchange
ExceptIfAttachmentSizeOver                                          any attachment is greater than or         2010 or
                                                                    equal to the specified value.             later

FromAddressContainsWords                       Words                Messages that contain the specified       Exchange
ExceptIfFromAddressContainsWords                                    words in the sender's email address.      2010 or
                                                                                                              later

FromAddressMatchesPatterns                     Patterns             Messages where the sender's email         Exchange
ExceptIfFromAddressMatchesPatterns                                  address contains text patterns that       2010 or
                                                                    match the specified regular               later
                                                                    expressions.

FromScope                                      UserScopeFrom        Messages that are sent by either          Exchange
ExceptIfFromScope                                                   internal senders or external senders.     2010 or
                                                                                                              later

HeaderContainsMessageHeader and                First property:      Messages that contain the specified       Exchange
HeaderContainsWords                            MessageHeaderField   header field, and the value of that       2010 or
ExceptIfHeaderContainsMessageHeader and                             header field contains the specified       later
ExceptIfHeaderContainsWords                    Second property:     words.
                                               Words
                                                                    The name of the header field and
                                                                    the value of the header field are
                                                                    always used together.

HeaderMatchesMessageHeader and                 First property:      Messages that contain the specified       Exchange
HeaderMatchesPatterns                          MessageHeaderField   header field, and the value of that       2010 or
ExceptIfHeaderMatchesMessageHeader and                              header field contains the specified       later
ExceptIfHeaderMatchesPatterns                  Second property:     regular expressions.
                                               Patterns
                                                                    The name of the header field and
                                                                    the value of the header field are
                                                                    always used together.

<!-- p.2506 -->

 Condition and exception parameters in the           Property type            Description                             Available
 Exchange Management Shell                                                                                            in

 MessageSizeOver                                      Size                    Messages where the total size           Exchange
 ExceptIfMessageSizeOver                                                      (message plus attachments) is           2013 or
                                                                              greater than or equal to the            later
                                                                              specified value.

 SCLOver                                              SCLValue                Messages that are assigned an SCL       Exchange
 ExceptIfSCLOver                                                              that's greater than or equal to the     2010 or
                                                                              specified value.                        later

 SubjectContainsWords                                 Words                   Messages that contain the specified     Exchange
 ExceptIfSubjectContainsWords                                                 words in the Subject field.             2010 or
                                                                                                                      later

 SubjectMatchesPatterns                               Patterns                Messages where the Subject field        Exchange
 ExceptIfSubjectMatchesPatterns                                               contains text patterns that match       2010 or
                                                                              the specified regular expressions.      later

 SubjectOrBodyContainsWords                           Words                   Messages that contain the specified     Exchange
 ExceptIfSubjectOrBodyContainsWords                                           words in the Subject field or           2010 or
                                                                              message body.                           later

 SubjectOrBodyMatchesPatterns                         Patterns                Messages where the Subject field or     Exchange
 ExceptIfSubjectOrBodyMatchesPatterns                                         message body contain text patterns      2010 or
                                                                              that match the specified regular        later
                                                                              expressions.

Property types
The property types that are used in conditions and exceptions are described in the following table.

  ７ Note

  If the property is a string, trailing spaces are not allowed.

                                                                                                               ﾉ    Expand table

 Property type                  Valid values                  Description

 ADAttribute                    Select from a predefined      You can check against any of the following Active Directory attributes:
                                list of Active Directory            City
                                attributes                          Company
                                                                    Country
                                                                    CustomAttribute1 - CustomAttribute15
                                                                    Department
                                                                    DisplayName
                                                                    Email
                                                                    FaxNumber
                                                                    FirstName
                                                                    HomePhoneNumber
                                                                    Initials
                                                                    LastName
                                                                    Manager

<!-- p.2507 -->

Property type   Valid values             Description

                                               MobileNumber
                                               Notes
                                               Office
                                               OtherFaxNumber
                                               OtherHomePhoneNumber
                                               OtherPhoneNumber
                                               PagerNumber
                                               PhoneNumber
                                               POBox
                                               State
                                               Street
                                               Title
                                               UserLogonName
                                               ZipCode

                                         In the EAC, to specify multiple words or text patterns for the same
                                         attribute, separate the values with commas. For example, the value
                                          San Francisco,Palo Alto for the City attribute looks for "City equals
                                         San Francisco" or City equals Palo Alto".

                                         In the Exchange Management Shell, use the syntax
                                         "AttributeName1:Value1,Value 2 with
                                         spaces,Value3...","AttributeName2:Word4,Value 5 with
                                         spaces,Value6..." , where Value is the word or text pattern that you
                                         want to match.

                                         For example, "City:San Francisco,Palo Alto" or "City:San
                                         Francisco,Palo Alto" , "Department:Sales,Finance" .

                                         When you specify multiple attributes, or multiple values for the same
                                         attribute, the or operator is used. Don't use values with leading or
                                         trailing spaces.

                                         The Country attribute requires the ISO 3166-1 two-letter country
                                         code value (for example, DE for Germany). For more information, see
                                         Country Codes - ISO 3166     .

Addresses       Exchange recipients      Depending on the nature of the condition or exception, you might be
                                         able to specify any mail-enabled object in the organization (for
                                         example, recipient-related conditions), or you might be limited to a
                                         specific object type (for example, groups for group membership
                                         conditions). And, the condition or exception might require one value,
                                         or allow multiple values.

                                         In the Exchange Management Shell, separate multiple values by
                                         commas.

                                         Note: This condition or exception doesn't consider messages that are
                                         sent to recipient proxy addresses. It only matches messages that are
                                         sent to the recipient's primary email address.

CharacterSets   Array of character set   One or more content character sets that exist in a message. For
                names                    example:
                                               Arabic/iso-8859-6
                                               Chinese/big5

<!-- p.2508 -->

Property type        Valid values          Description

                                                 Chinese/euc-cn
                                                 Chinese/euc-tw
                                                 Chinese/gb2312
                                                 Chinese/iso-2022-cn
                                                 Cyrillic/iso-8859-5
                                                 Cyrillic/koi8-r
                                                 Cyrillic/windows-1251
                                                 Greek/iso-8859-7
                                                 Hebrew/iso-8859-8
                                                 Japanese/euc-jp
                                                 Japanese/iso-022-jp
                                                 Japanese/shift-jis
                                                 Korean/euc-kr
                                                 Korean/johab
                                                 Korean/ks_c_5601-1987
                                                 Turkish/windows-1254
                                                 Turkish/iso-8859-9
                                                 Vietnamese/tcvn

DocumentProperties   Array of custom or    Specifies a built-in or custom document property. The built-in
                     predefined document   document properties are:
                     properties                  Business Impact
                                                 Compliancy
                                                 Confidentiality
                                                 Department
                                                 Impact
                                                 Intellectual Property
                                                 Personally Identifiable Information
                                                 Personal Information
                                                 Personal Use
                                                 Required Clearance
                                                 PHI
                                                 PII
                                                 Project
                                                 Protected Health Information

                                           Each property contains a single value. When you specify multiple
                                           properties, the or operator is used.

                                           Exchange Management Shell uses the syntax: "<PropertyName1>:
                                           <PropertyValue1>","<PropertyName2>:<PropertyValue2>" , where
                                           <PropertyValue> is the word that you want to match.

                                           The syntax for this parameter is "PropertyName:Word" . To specify
                                           multiple properties, or multiple words for the same property, use the
                                           following syntax: "PropertyName1:Word1,Phrase with
                                           spaces,word2...","PropertyName2:Word3,Phrase with spaces,word4... .
                                           Don't use leading or trailing spaces.

                                           When you specify multiple properties, or multiple values for the same
                                           property, the or operator is used.

<!-- p.2509 -->

Property type            Valid values                 Description

DomainName               Array of SMTP domains        For example, contoso.com or eu.contoso.com .

                                                      In the Exchange Management Shell, you can specify multiple domains
                                                      separated by commas.

EvaluatedUser            Single value of Sender or    Specifies whether the rule is looking for the manager of the sender or
                         Recipient                    the manager of the recipient.

Evaluation               Single value of Equal or     When comparing the Active Directory attribute of the sender and
                         Not equal ( NotEqual )       recipients, this operator specifies whether the values should match, or
                                                      not match.

Importance               Single value of Low,         The Importance level that was assigned to the message by the sender
                         Normal, or High              in Outlook or Outlook on the web.

IPAddressRanges          Array of IP addresses or     You enter the IPv4 addresses using the following syntax:
                         address ranges                     Single IP address: For example, 192.168.1.1 .
                                                            IP address range: For example, 192.168.0.1-192.168.0.254 .
                                                            Classless InterDomain Routing (CIDR) IP address range: For
                                                            example, 192.168.0.1/25 .

                                                      In the Exchange Management Shell, you can specify multiple IP
                                                      addresses or ranges separated by commas.

ManagementRelationship   Single value of Manager or   Specifies the relationship between the sender and any of the
                         Direct                       recipients. The rule checks the Manager attribute in Active Directory
                         report( DirectReport )       to see if the sender is the manager of a recipient, or if the sender is
                                                      managed by a recipient.

MessageClassification    Single message               In the EAC, you select from the list of message classifications that
                         classification               you've created.

                                                      In the Exchange Management Shell, you use the Get-
                                                      MessageClassification cmdlet to identify the message classification.
                                                      For example, use the following command to search for messages with
                                                      the Company Internal classification and prepend the message subject
                                                      with the value CompanyInternal : New-TransportRule "Rule Name" -
                                                      HasClassification @(Get-MessageClassification "Company
                                                      Internal").Identity -PrependSubject "CompanyInternal"

MessageHeaderField       Single string                Specifies the name of the header field. The name of the header field is
                                                      always paired with the value in the header field (word or text pattern
                                                      match).

                                                      The message header is a collection of required and optional header
                                                      fields in the message. Examples of header fields are To, From,
                                                      Received, and Content-Type. Official header fields are defined in RFC
                                                      5322. Unofficial header fields start with X- and are known as X-
                                                      headers.

MessageType              Single message type value    Specifies one of the following message types:
                                                            Automatic reply ( OOF )
                                                            Auto-forward ( AutoForward )
                                                            Encrypted
                                                            Calendaring

<!-- p.2510 -->

Property type               Valid values                 Description

                                                               Permission controlled ( PermissionControlled )
                                                               Voicemail
                                                               Signed
                                                               Approval request ( ApprovalRequest )
                                                               Read receipt ( ReadReceipt )

                                                         Note: When Outlook or Outlook on the web is configured to forward
                                                         a message, the ForwardingSmtpAddress property is added to the
                                                         message. The message type isn't changed to AutoForward .

Patterns                    Array of regular             Specifies one or more regular expressions that are used to identify
                            expressions                  text patterns in values. For more information, see Regular Expression
                                                         Syntax.

                                                         In the Exchange Management Shell, you specify multiple regular
                                                         expressions separated by commas, and you enclose each regular
                                                         expression in quotation marks (").

SCLValue                    One of the following         Specifies the spam confidence level (SCL) that's assigned to a
                            values:                      message. A higher SCL value indicates that a message is more likely to
                                  Bypass spam            be spam.
                                  filtering ( -1 )
                                  Integers 0 through 9

SensitiveInformationTypes   Array of sensitive           Specifies one or more sensitive information types that are defined in
                            information types            your organization. For a list of built-in sensitive information types, see
                                                         Sensitive information types in Exchange Server.

                                                         In the Exchange Management Shell, use the syntax
                                                         @{<SensitiveInformationType1>},@{<SensitiveInformationType2>},... .
                                                         For example, to look for content that contains at least two credit card
                                                         numbers, and at least one ABA routing number, use the value
                                                         @{Name="Credit Card Number"; minCount="2"},@{Name="ABA Routing
                                                         Number"; minCount="1"} .

Size                        Single size value            Specifies the size of an attachment or the whole message.

                                                         In the EAC, you can only specify the size in kilobytes (KB).

                                                         In the Exchange Management Shell, when you enter a value, qualify
                                                         the value with one of the following units:

                                                               B (bytes)
                                                               KB (kilobytes)
                                                               MB (megabytes)
                                                               GB (gigabytes)

                                                         For example, 20MB . Unqualified values are typically treated as bytes,
                                                         but small values may be rounded up to the nearest kilobyte.

UserScopeFrom               Single value of Inside the   A sender is considered to be inside the organization if either of the
                            organization                 following conditions is true:
                            ( InOrganization ) or

<!-- p.2511 -->

Property type   Valid values                   Description

                Outside the organization             The sender is a mailbox, mail user, group, or mail-enabled
                ( NotInOrganization )                public folder that exists in the organization's Active Directory.
                                                     The sender's email address is in an accepted domain that's
                                                     configured as an authoritative domain or an internal relay
                                                     domain and the message was sent or received over an
                                                     authenticated connection. For more information about
                                                     accepted domains, see Accepted domains in Exchange Server.

                                               A sender is considered to be outside the organization if either of the
                                               following conditions is true:

                                                     The sender's email address isn't in an accepted domain.
                                                     The sender's email address is in an accepted domain that's
                                                     configured as an external relay domain.

                                               Note: To determine whether mail contacts are considered to be inside
                                               or outside the organization, the sender's address is compared with
                                               the organization's accepted domains.

UserScopeTo     One of the following           A recipient is considered to be inside the organization if either of the
                values:                        following conditions is true:
                      Inside the                     The recipient is a mailbox, mail user, group, or mail-enabled
                      organization                   public folder that exists in the organization's Active Directory.
                      ( InOrganization )             The recipient's email address is in an accepted domain that's
                      Outside the                    not configured as an external relay domain and the message
                      organization                   was sent or received over an authenticated connection.
                      ( NotInOrganization )
                      In an external
                      partner organization
                      ( ExternalPartner )      A recipient is considered to be outside the organization if either of

                      In an external non-      the following conditions is true:
                      partner organization
                                                     The recipient's email address isn't in an accepted domain and,
                      ( ExternalNonPartner )
                                                     at the same time, the recipient's email address isn't in a remote
                                                     domain for which the property IsInternal is set to true.
                                                     The recipient's email address is in an accepted domain that's
                                                     configured as an external relay domain.

                                               External partner organizations are external domains where you've
                                               configured Domain Security (mutual TLS authentication) to send mail.

                                               External non-partner organizations are all other external domains that
                                               aren't considered partner domains.

Words           Array of strings               Specifies one or more words to look for. The words aren't case-
                                               sensitive, and can be surrounded by spaces and punctuation marks.
                                               Wildcards and partial matches aren't supported.

                                               For example, "contoso" matches " Contoso.". However, if the text is
                                               surrounded by other characters, it isn't considered a match. For
                                               example, "contoso" doesn't match the following values:

<!-- p.2512 -->

 Property type             Valid values              Description

                                                           Acontoso
                                                           Contosoa
                                                           Acontosob

                                                     The asterisk (*) is treated as a literal character, and isn't used as a
                                                     wildcard character.

For more information
Mail flow rule actions in Exchange Server

Mail flow rule conditions and exceptions (predicates) in Exchange Online

<!-- p.2513 -->

Mail flow rule actions in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019        Subscription Edition

Actions in mail flow rules (also known as transport rules) specify what you want to do to messages that match
conditions of the rule. For example, you can create a rule that forwards message from specific senders to a
moderator, or adds a disclaimer or personalized signature to all outbound messages.

Actions typically require additional properties. For example, when the rule redirects a message, you need to
specify where to redirect the message. Some actions have multiple properties that are available or required. For
example, when the rule adds a header field to the message header, you need to specify both the name and value
of the header. When the rule adds a disclaimer to messages, you need to specify the disclaimer text, but you can
also specify where to insert the text, or what to do if the disclaimer can't be added to the message. Typically, you
can configure multiple actions in a rule, but some actions are exclusive. For example, one rule can't reject and
redirect the same message.

For more information about mail flow rules in Exchange Server, including how multiple actions are handled, see
Mail flow rules in Exchange Server.

For more information about conditions and exceptions in mail flow rules, see Mail flow rule conditions and
exceptions (predicates) in Exchange Server.

Actions for mail flow rules on Mailbox servers
The actions that are available in mail flow rules on Mailbox servers are described in the following table. Valid
values for each property are described in Property values[Property values] section.

Notes:

      After you select an action in the Exchange admin center (EAC), the value that's ultimately shown in the Do
      the following field is often different from the click path you selected. Also, when you create new rules, you
      can sometimes (depending on the selections you make) select a short action name from a template (a
      filtered list of actions) instead of following the complete click path. The short names and full click path
      values are shown in the EAC column in the table.

      The names of some of the actions that are returned by the Get-TransportRuleAction cmdlet are different
      than the corresponding parameter names, and multiple parameters might be required for an action.

                                                                                                       ﾉ    Expand table

 Action in      Action parameter in the            Property                  Description                           Available
 the EAC        Exchange Management Shell                                                                          in

 Forward the    ModerateMessageByUser              Addresses                 Forwards the message to the           Exchange
 message for                                                                 specified moderators as an            2010 or
 approval to                                                                 attachment wrapped in an              later
 these                                                                       approval request. For more
 people                                                                      information, see Common
                                                                             message approval scenarios. You
 Forward the                                                                 can't use a distribution group as a
 message for                                                                 moderator.

<!-- p.2514 -->

Action in      Action parameter in the           Property                Description                           Available
the EAC        Exchange Management Shell                                                                       in

approval >
to these
people

Forward the    ModerateMessageByManager          n/a                     Forwards the message to the           Exchange
message for                                                              sender's manager for approval.        2010 or
approval to                                                                                                    later
the sender's                                                             This action only works if the
manager                                                                  sender's Manager attribute is
                                                                         defined in Active Directory.
Forward the                                                              Otherwise, the message is
message for                                                              delivered to the recipients without
approval >                                                               moderation.
to the
sender's
manager

Redirect the   RedirectMessageTo                 Addresses               Redirects the message to the          Exchange
message to                                                               specified recipients. The message     2010 or
these                                                                    isn't delivered to the original       later
recipients                                                               recipients, and no notification is
                                                                         sent to the sender or the original
Redirect the                                                             recipients.
message to
> these
recipients

Reject the     RejectMessageReasonText           String                  Returns the message to the sender     Exchange
message                                                                  in a non-delivery report (also        2010 or
with the                                                                 known as an NDR or bounce             later
explanation                                                              message) with the specified text as
                                                                         the rejection reason. The recipient
Block the                                                                doesn't receive the original
message >                                                                message or notification.
reject the
message                                                                  The default enhanced status code
and include                                                              that's used is 5.7.1 .
an
explanation                                                              When you create or modify the
                                                                         rule in the Exchange Management
                                                                         Shell, you can specify the DSN
                                                                         code by using the
                                                                         RejectMessageEnhancedStatusCode
                                                                         parameter.

Reject the     RejectMessageEnhancedStatusCode   DSNEnhancedStatusCode   Returns the message to the sender     Exchange
message                                                                  in an NDR with the specified          2010 or
with the                                                                 enhanced delivery status              later
enhanced                                                                 notification (DSN) code. The
status code                                                              recipient doesn't receive the
                                                                         original message or notification.
Block the
message >                                                                Valid DSN codes are 5.7.1 or
reject the                                                               5.7.900 through 5.7.999 .
message
with the                                                                 The default reason text that's used

<!-- p.2515 -->

Action in       Action parameter in the     Property             Description                            Available
the EAC         Exchange Management Shell                                                               in

enhanced                                                         is Delivery not authorized,
status code                                                      message refused .
of
                                                                 When you create or modify the
                                                                 rule in the Exchange Management
                                                                 Shell, you can specify the rejection
                                                                 reason text by using the
                                                                 RejectMessageReasonText
                                                                 parameter.

Delete the      DeleteMessage               n/a                  Silently drops the message without     Exchange
message                                                          sending a notification to the          2010 or
without                                                          recipient or the sender.               later
notifying
anyone

Block the
message >
delete the
message
without
notifying
anyone

Add             BlindCopyTo                 Addresses            Adds one or more recipients to the     Exchange
recipients to                                                    Bcc field of the message. The          2010 or
the Bcc box                                                      original recipients aren't notified,   later
                                                                 and they can't see the additional
Add                                                              addresses.
recipients >
to the Bcc
box

Add             AddToRecipients             Addresses            Adds one or more recipients to the     Exchange
recipients to                                                    To field of the message. The           2010 or
the To box                                                       original recipients can see the        later
                                                                 additional addresses.
Add
recipients >
to the To
box

Add             CopyTo                      Addresses            Adds one or more recipients to the     Exchange
recipients to                                                    Cc field of the message. The           2010 or
the Cc box                                                       original recipients can see the        later
                                                                 additional address.
Add
recipients >
to the Cc
box

Add the         AddManagerAsRecipientType   AddedManagerAction   Adds the sender's manager to the       Exchange
sender's                                                         message as the specified recipient     2010 or
manager as                                                       type (To, Cc, Bcc), or redirects the   later
a recipient                                                      message to the sender's manager
                                                                 without notifying the sender or the

<!-- p.2516 -->

Action in        Action parameter in the             Property                   Description                          Available
the EAC          Exchange Management Shell                                                                           in

Add                                                                             recipient.
recipients >
add the                                                                         This action only works if the
sender's                                                                        sender's Manager attribute is
manager as                                                                      defined in Active Directory.
a recipient

Append the       ApplyHtmlDisclaimerText             First property:            Applies the specified HTML           Exchange
disclaimer                                           DisclaimerText             disclaimer to the end of the         2010 or
                 ApplyHtmlDisclaimerFallbackAction                              message.                             later
Apply a                                              Second property:
disclaimer       ApplyHtmlDisclaimerTextLocation     DisclaimerFallbackAction   When you create or modify the
to the                                                                          rule in the Exchange Management
message >                                            Third property (Exchange   Shell, use the
append a                                             Management Shell only):    ApplyHtmlDisclaimerTextLocation
disclaimer                                           DisclaimerTextLocation     parameter with the value Append .

Prepend the      ApplyHtmlDisclaimerText             First property:            Applies the specified HTML           Exchange
disclaimer                                           DisclaimerText             disclaimer to the beginning of the   2010 or
                 ApplyHtmlDisclaimerFallbackAction                              message.                             later
Apply a                                              Second property:
disclaimer       ApplyHtmlDisclaimerTextLocation     DisclaimerFallbackAction   When you create or modify the
to the                                                                          rule in the Exchange Management
message >                                            Third property (Exchange   Shell, use the
prepend a                                            Management Shell only):    ApplyHtmlDisclaimerTextLocation
disclaimer                                           DisclaimerTextLocation     parameter with the value Prepend .

Remove this      RemoveHeader                        MessageHeaderField         Removes the specified header field   Exchange
header                                                                          from the message header.             2010 or
                                                                                                                     later
Modify the
message
properties >
remove a
message
header

Set the          SetHeaderName                       First property:            Adds or modifies the specified       Exchange
message                                              MessageHeaderField         header field in the message          2010 or
header to        SetHeaderValue                                                 header, and sets the header field    later
this value                                           Second property: String    to the specified value.

Modify the
message
properties >
set a
message
header

Apply a          ApplyClassification                 MessageClassification      Applies the specified message        Exchange
message                                                                         classification to the message.       2010 or
classification                                                                                                       later

Modify the
message
properties >

<!-- p.2517 -->

Action in        Action parameter in the          Property           Description                           Available
the EAC          Exchange Management Shell                                                                 in

apply a
message
classification

Set the          SetSCL                           SCLValue           Sets the spam confidence level        Exchange
spam                                                                 (SCL) of the message to the           2010 or
confidence                                                           specified value.                      later
level (SCL)
to

Modify the
message
properties >
set the spam
confidence
level (SCL)

Apply rights     ApplyRightsProtectionTemplate    RMSTemplate        Applies the specified Rights          Exchange
protection                                                           Management Services (RMS)             2010 or
to the                                                               template to the message.              later
message
with                                                                 RMS requires Exchange Enterprise
                                                                     client access licenses (CALs) for
Modify the                                                           each mailbox. For more
message                                                              information about CALs, see
security >                                                           Exchange licensing FAQs      .
apply rights
protection

Require TLS      RouteMessageOutboundRequireTls   n/a                Forces the outbound messages to       Exchange
encryption                                                           be routed over a TLS encrypted        2013 or
                                                                     connection.                           later
Modify the
message
security >
require TLS
encryption

Prepend the      PrependSubject                   String             Adds the specified text to the        Exchange
subject of                                                           beginning of the Subject field of     2010 or
the message                                                          the message. Consider using a         later
with                                                                 space or a colon (:) as the last
                                                                     character of the specified text to
                                                                     differentiate it from the original
                                                                     subject text.

                                                                     To prevent the same string from
                                                                     being added to messages that
                                                                     already contain the text in the
                                                                     subject (for example, replies), add
                                                                     the The subject includes
                                                                     (ExceptIfSubjectContainsWords)
                                                                     exception to the rule.

Notify the       NotifySender                     First property:    Notifies the sender or blocks the     Exchange
sender with                                       NotifySenderType   message when the message              2013 or

<!-- p.2518 -->

Action in      Action parameter in the           Property                    Description                            Available
the EAC        Exchange Management Shell                                                                            in

a Policy Tip   RejectMessageReasonText                                       matches a DLP policy.                  later
                                                 Second property: String
               RejectMessageEnhancedStatusCode                               When you use this action, you
               (Exchange Management Shell        Third property (Exchange    need to use the The message
               only)                             Management Shell only):     contains sensitive information
                                                 DSNEnhancedStatusCode       (MessageContainsDataClassification
                                                                             condition.

                                                                             When you create or modify the
                                                                             rule in the Exchange Management
                                                                             Shell, the RejectMessageReasonText
                                                                             parameter is optional. If you don't
                                                                             use this parameter, the default text
                                                                             Delivery not authorized, message
                                                                             refused is used.

                                                                             In the Exchange Management
                                                                             Shell, you can also use the
                                                                             RejectMessageEnhancedStatusCode
                                                                             parameter to specify the enhanced
                                                                             status code. If you don't use this
                                                                             parameter, the default enhanced
                                                                             status code 5.7.1 is used.

                                                                             This action limits the other
                                                                             conditions, exceptions, and actions
                                                                             that you can configure in the rule.

Generate       GenerateIncidentReport            First property: Addresses   Sends an incident report that          Exchange
incident                                                                     contains the specified content to      2013 or
report and     IncidentReportContent             Second property:            the specified recipients.              later
send it to                                       IncidentReportContent
                                                                             An incident report is generated for
                                                                             messages that match data loss
                                                                             prevention (DLP) policies in your
                                                                             organization.

Notify the     GenerateNotification              NotificationMessageText     Specifies the text, HTML tags, and     Exchange
recipient                                                                    message keywords to include in         2016 or
with a                                                                       the notification message that's        later
message                                                                      sent to the message's recipients.
                                                                             For example, you can notify
                                                                             recipients that the message was
                                                                             rejected by the rule, or marked as
                                                                             spam and delivered to their Junk
                                                                             Email folder.

Properties     SetAuditSeverity                  AuditSeverityLevel          Specifies whether to:                  Exchange
of this rule                                                                       Prevent the generation of an     2013 or
section >                                                                          incident report and the          later
Audit this                                                                         corresponding entry in the
rule with                                                                          message tracking log.
severity                                                                           Generate an incident report
level                                                                              and the corresponding entry
                                                                                   in the message tracking log

<!-- p.2519 -->

 Action in       Action parameter in the           Property                       Description                                    Available
 the EAC         Exchange Management Shell                                                                                       in

                                                                                           with the specified severity
                                                                                           level (low, medium, or high).

 Properties      StopRuleProcessing                n/a                            Specifies that after the message is            Exchange
 of this rule                                                                     affected by the rule, the message is           2013 or
 section >                                                                        exempt from processing by other                later
 Stop                                                                             rules.
 processing
 more rules

 More
 options >
 Properties
 of this rule
 section >
 Stop
 processing
 more rules

Actions for mail flow rules on Edge Transport servers
A small subset of actions that are available on Mailbox servers are also available on Edge Transport servers, but
there are also some actions that are only available on Edge Transport servers. There's no EAC on Edge Transport
servers, so you can only manage mail flow rules in the Exchange Management Shell on the local Edge Transport
server. The actions are described in the following table. The properties types are described in the Property values
section.

                                                                                                                 ﾉ   Expand table

 Action parameter in the Exchange      Property               Description                              Available         Available
 Management Shell                                                                                      on                in

 AddToRecipients                       Addresses              Adds one or more recipients to           Mailbox           Exchange
                                                              the To field of the message. The         servers and       2010 or
                                                              original recipients can see the          Edge              later
                                                              additional addresses.                    Transport
                                                                                                       servers

 BlindCopyTo                           Addresses              Adds one or more recipients to           Mailbox           Exchange
                                                              the Bcc field of the message. The        servers and       2010 or
                                                              original recipients aren't notified,     Edge              later
                                                              and they can't see the additional        Transport
                                                              addresses.                               servers

 CopyTo                                Addresses              Adds one or more recipients to           Mailbox           Exchange
                                                              the Cc field of the message. The         servers and       2010 or
                                                              original recipients can see the          Edge              later
                                                              additional address.                      Transport
                                                                                                       servers

 DeleteMessage                         n/a                    Silently drops the message               Mailbox           Exchange
                                                              without sending a notification to        servers and       2010 or

<!-- p.2520 -->

Action parameter in the Exchange   Property             Description                          Available      Available
Management Shell                                                                             on             in

                                                        the recipient or the sender.         Edge           later
                                                                                             Transport
                                                                                             servers

Disconnect                         n/a                  Ends the SMTP connection             Edge           Exchange
                                                        between the sending server and       Transport      2010 or
                                                        the Edge Transport server without    servers only   later
                                                        generating an NDR.

LogEventText                       String               Generates an event with the          Edge           Exchange
                                                        specified text in the Application    Transport      2010 or
                                                        log of the local Edge Transport      servers only   later
                                                        server. The entry contains the
                                                        following information:
                                                              Level: Information
                                                              Source: MSExchange
                                                              Messaging Policies
                                                              Event ID: 4000
                                                              Task Category: Rules
                                                              EventData: The following
                                                              message is logged by an
                                                              action in the rules: <text
                                                              you specify>.

PrependSubject                     String               Adds the specified text to the       Mailbox        Exchange
                                                        beginning of the Subject field of    servers and    2010 or
                                                        the message. Consider using a        Edge           later
                                                        space or a colon (:) as the last     Transport
                                                        character of the specified text to   servers
                                                        differentiate it from the original
                                                        subject.

Quarantine                         n/a                  Delivers the message to the          Edge           Exchange
                                                        quarantine mailbox that's defined    Transport      2010 or
                                                        in the content filtering             servers only   later
                                                        configuration on the Edge
                                                        Transport server. For more
                                                        information, see Configure a
                                                        spam quarantine mailbox.

                                                        If the quarantine mailbox isn't
                                                        configured, the message is
                                                        returned to the sender in an NDR.

RedirectMessageTo                  Addresses            Redirects the message to the         Mailbox        Exchange
                                                        specified recipients. The message    servers and    2010 or
                                                        isn't delivered to the original      Edge           later
                                                        recipients, and no notification is   Transport
                                                        sent to the sender or the original   servers
                                                        recipients.

RemoveHeader                       MessageHeaderField   Removes the specified header         Mailbox        Exchange
                                                        field from the message header.       servers and    2010 or
                                                                                             Edge           later
