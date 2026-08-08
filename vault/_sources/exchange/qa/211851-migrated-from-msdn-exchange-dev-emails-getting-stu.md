---
title: "[Migrated from MSDN Exchange Dev] Emails Getting Stuck In Outlook (Outlook Connectivity Test Failed), OWA is working fine"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/211851/migrated-from-msdn-exchange-dev-emails-getting-stu
question_id: 211851
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Emails Getting Stuck In Outlook (Outlook Connectivity Test Failed), OWA is working fine

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/211851/migrated-from-msdn-exchange-dev-emails-getting-stu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/e462e857-3174-460c-b100-5c7821a79304/emails-getting-stuck-in-outlook-outlook-connectivity-test-failed-owa-is-working-fine?forum=exchangesvrdevelopment  

We have Exchange 2016 and outlook is very slow, like emails are getting stuck in outbox. Some time the new emails delivered but old emails keep stuck in outbox and not getting delivered at all.  

I am getting below mentioned error in outlook connectivity test.  

Testing the MAPI Mail Store endpoint on the Exchange server.An error occurred while testing the Mail Store.  

Test Steps  

Attempting to log on to the Mailbox.An error occurred while logging on to the Mailbox.  

Additional Details  

Mailbox logon returned EcLoginFailure -2147221231. Possible causes are: 1. The user doesn't have any access to a private mailbox or public folder messaging data. 2. There are no private mailboxes or public folders on the server. 3. The server is exiting or is about to exit. Status Code: -2147221231

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-28*

Create a new mailbox and test if the newly created mailboxes works on that, if they are working, migrate some old users to the new mailbox database and test Outlook Connectivity Test again.    

If still now work, you might need to start a mailbox repair:https://learn.microsoft.com/en-us/powershell/module/exchange/new-mailboxrepairrequest?view=exchange-ps    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
