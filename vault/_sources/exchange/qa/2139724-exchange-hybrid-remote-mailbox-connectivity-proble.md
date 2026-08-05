---
title: "Exchange Hybrid - Remote Mailbox connectivity problem."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2139724/exchange-hybrid-remote-mailbox-connectivity-proble
question_id: 2139724
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid - Remote Mailbox connectivity problem.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2139724/exchange-hybrid-remote-mailbox-connectivity-proble (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am facing aproblem with a mailbox/profile connectivity in outlook desktop in hybrid environment.   

The case:   

-  We created user, enabled remotemailbox, then mailbox after delta is provisioned in the cloud.   

-  User go for holidays, we convert remoteusermailobx and cloud mailbox into sharedmailbox, also remove license  

-  I believe that in this time user account was unsynced for over 30days because we moved it to unsynced OU.   

-  When user come back to work, we synced again user account, enabled remotemailbox, got exchange guid from cloud and paste it into on-prem attribute.   

-  User can use OWA Outlook but cannot connect Outlook 2016/365 with Exchange. Anyone faced with similar problem and can help me with it?   

Now, we have user with enabled remote shared mailbox, no license assigned and no cloud mailbox.   

I tried to disable-remotemailbox, then re-create it. After this user can use OWA but cannot connect with Outlook...  And i think this is main problem, OWA works, outlook on-prem does not. 

I read whole google, sadly there is no answer or i cannot ask good question.   

Thank you in advance.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-03*

Hi,@Checior200

Thanks for posting your question in the Microsoft Q&A forum.

Based on the information you provided, if OWA is working fine , only Outlook is having problems. It can be inferred that there is a problem with the Outlook configuration.

1.First you have to clear the old Outlook profile. You need to go to Control Panel > (search for) mail and find the “Mail ” option.

2.Go follow the link under Profiles > Show Profiles

3.Here you want to select your existing profile and Remove it, then Add a new one.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-02*

Hi,

Can you pass on any error messages you have?

Here are some links that might help you:

https://learn.microsoft.com/en-us/exchange/troubleshoot/user-and-shared-mailboxes/cannot-access-mailbox

https://learn.microsoft.com/en-us/exchange/troubleshoot/user-and-shared-mailboxes/cannot-access-mailbox-after-remote-mailbox-moves-to-office-365

https://learn.microsoft.com/en-us/exchange/troubleshoot/move-or-migrate-mailboxes/troubleshoot-migration-issues-in-exchange-hybrid

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/outlook-connection-issue-caused-by-rpc-encryption-requirement

Sincerely,
