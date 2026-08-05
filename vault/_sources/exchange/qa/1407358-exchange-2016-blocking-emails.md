---
title: "Exchange 2016 blocking emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1407358/exchange-2016-blocking-emails
question_id: 1407358
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 blocking emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1407358/exchange-2016-blocking-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi there,

I am running Exchange 2016 and went to the Microsoft site to fill out a contact form.  Microsoft attempted to email be back saying thank you from email@microsoft.com but our Exchange server blocked the email.  This is the message I am seeing.  Why was the email blocked?

28/10/2023 20:18:34    FAIL             SMTP          email@microsoft.com       {******@yyy.com}                                        Thanks for your request

RunspaceId              : 8da772ca-1784-4b02-a831-55867685f81c

Timestamp               : 28/10/2023 20:18:34

ClientIp                : 199.15.214.202

ClientHostname          : xxx

ServerIp                : x.x.x.x

ServerHostname          :

SourceContext           : Sender Id Agent

ConnectorId             : xxx\Default xxx

Source                  : SMTP

EventId                 : FAIL

InternalMessageId       : 190838281863168

MessageId               : ******@sjmktmail-trigger1d.marketo.org

NetworkMessageId        : 196b3170-6f7d-4763-484d-08dbd7eaadff

Recipients              : {******@xxx.com}

RecipientStatus         : {[{LED=550 5.7.1 Sender ID (PRA) Not Permitted};{MSG=};{FQDN=};{IP=x.x.x.x};{LRT=}]}

TotalBytes              : 0

RecipientCount          : 1

RelatedRecipientAddress :

Reference               :

MessageSubject          : Thanks for your request

Sender                  : email@microsoft.com

ReturnPath              : ******@bounce4.email.microsoft.com

Directionality          : Incoming

TenantId                :

OriginalClientIp        :

MessageInfo             :

MessageLatency          :

MessageLatencyType      : None

EventData               : {[ToEntity, Unknown], [FromEntity, Internet], [DeliveryPriority, Normal], [OriginalFromAddress, ******@bounce4.email.microsoft.com], [AccountForest, xxxcom]}

TransportTrafficType    : Email

SchemaVersion           : 15.01.2507.034

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-30*

Hello @JD ,

Welcome to our Q&A forum.

Based on the error message you provided, it seems that your Exchange server blocked the email from Microsoft due to a Sender ID (PRA) Not Permitted error. This error occurs when the sender’s domain does not have a valid Sender Policy Framework (SPF) record or if the SPF record is not configured correctly.

To resolve this issue, you can check if the SPF record for Microsoft’s domain is configured correctly. You can use the Microsoft Remote Connectivity Analyzer to check if the SPF record is valid. If the SPF record is not valid, you can add it to your list of allowed domains.

Please feel free to let us know if you have any updates.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
