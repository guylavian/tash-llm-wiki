---
title: "Open Another Mailbox from OWA to 365, receive : NegotiateSecurityContext failed with for host 'Servername.Domain.com' with status 'LogonDenied'"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1531663/open-another-mailbox-from-owa-to-365-receive-negot
question_id: 1531663
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Open Another Mailbox from OWA to 365, receive : NegotiateSecurityContext failed with for host 'Servername.Domain.com' with status 'LogonDenied'

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1531663/open-another-mailbox-from-owa-to-365-receive-negot (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Exchange Server on premises, I can open another user mailbox by clicking on Open Another Mailbox from OWA.
Some users are on Office365, when We try to Open Another Mailbox for users that are on 365, we receive this error : NegotiateSecurityContext failed with for host 'Servername.Domain.com' with status 'LogonDenied'
How to fix this

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-14*

tried your suggestion, now receiving this : 
NegotiateSecurityContext failed with for host \u0027servername.domainname.com\u0027 with status \u0027LogonDenied\u0027

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-14*

Hi @MT,

Does this issue occur after you moved the mailbox from on-premises to cloud?

If yes, please remove and re-add the full access permission on the mailbox and see if it can help with this issue.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
