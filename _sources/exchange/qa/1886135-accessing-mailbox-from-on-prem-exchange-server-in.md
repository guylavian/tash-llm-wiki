---
title: "Accessing Mailbox from On-prem exchange server in Recently Migrated Hybrid 0365 Environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1886135/accessing-mailbox-from-on-prem-exchange-server-in
question_id: 1886135
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Accessing Mailbox from On-prem exchange server in Recently Migrated Hybrid 0365 Environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1886135/accessing-mailbox-from-on-prem-exchange-server-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I recently migrated all my users from on-prem exchange to Exchange online although im having some trouble using the on-prem now.

Let me share some of my user's AD Attributes:

-  msExchRecipientTypeDetails: RemoteUserMailbox

-  msExchRemoteRecipientType: Migrated (UserMailbox)

Now,

Trying to use the On-premise server with EWS and that user, results in "No mailbox with such GUID".

Also, when trying to use OWA on On-premise i get the automatic redirect to o365 exchange online "for better performance please visit this link..."

Few questions:

-  Am i even suppose to be able to access the mailbox from the On-premise server according to those attributes stated above?

-  If so, What am i doing wrong?

Thank you.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-22*

Hello, @Michael Soap,

Welcome to the Microsoft Q&A platform!

Based on your description, I understand that you are experiencing some issues with local after migrating all your users from local exchange to Exchange online.

1.Reasons for not being able to access mailboxes on the local server

With regard to why you saw a ‘No mailbox with such GUID’ error and an automatic redirection to Office 365 when trying to access OWA, that is because mailboxes are located in Exchange Online, it is not possible to access their email data directly from the local EWS or OWA endpoint.

-  What you did wrong and why

Your main issue is a misunderstanding of the hybrid deployment model. When you migrate mailboxes to Exchange Online, the local server will no longer host the content of those mailboxes. Make sure that all clients and applications are configured to point to the Exchange Online endpoint, not the local Exchange server used for mailbox access.

3.My suggestions

If you need to manage users (e.g., create new mailboxes, manage existing mailboxes), you should use the Exchange Admin Center (EAC) in Office 365 or connect to Exchange Online via PowerShell. If there are specific management tasks that still need to be completed on-premises, ensure that these user objects are properly synchronized with Azure AD and that hybrid management is correctly configured.

Please feel free to contact me if you have any queries. If my reply is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

Best Wishes,

Alex Zhang

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-08-19*

Nope, now that those mailboxes are in 365, you would need to connect to Exchange Online to access them. 

EWS is going away so start looking towards Graph to access ExO mailboxes programtically instead 

https://techcommunity.microsoft.com/t5/exchange-team-blog/retirement-of-exchange-web-services-in-exchange-online/ba-p/3924440
