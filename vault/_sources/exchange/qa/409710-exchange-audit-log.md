---
title: "Exchange Audit Log"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/409710/exchange-audit-log
question_id: 409710
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Audit Log

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/409710/exchange-audit-log (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi MSFT,  

So I have enabled audit logs for actions of the mailbox owner by the cmdlet `set-mailbox -identity <> -auditowner move,create,movetodeleteditems,harddelete,softdelete -auditenabled $true`.  

However in my tests, if I move or delete some emails in the mailbox, then use cmdlet `search-mailboxauditlog -identity <> -logontypes owner -showdetails` to search the log immediately, it won't return any results. After 1 or 2 days, again, I use the cmdlet, then the log appears. So it seems the log can't be queried in a short time after the configuration.   

I'd like to know how long the log can be generated and queried.   

Thanks in advance.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-27*

Hi @67085432 ,

As AshokM said, the mailbox audit log will be kept 90 days by default,  

And also you could manually set a value of AuditLogAgeLimit to specify how long the logs could be kept:  

Set-Mailbox -Identity "Mailbox" -AuditLogAgeLimit 180

Best regards,  

Lou

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in [our documentation][10] to enable e-mail notifications if you want to receive the related email notification for this thread.

[10]: https://learn.microsoft.com/en-us/answers/articles/67444/email-notifications.html [2]: https://learn.microsoft.com/en-us/powershell/module/exchange/Get-MessageTrackingLog?view=exchange-ps

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-26*

Hi @67085432 ,    

By default, once the audit is enabled on the mailbox, any actions which has been mentioned will be logged under a folder called "Audits" in the mailbox itself. By default, mailbox audit log entries are retained in the mailbox for 90 days and then deleted.     

You can run the below command to check the statistics of Audit folder before the Search-MailboxAuditLog    

Get-MailboxFolderStatistics mailboxname | where{$_.Name -like "audit"}    

https://learn.microsoft.com/en-us/exchange/policy-and-compliance/mailbox-audit-logging/mailbox-audit-logging?view=exchserver-2019#mailbox-actions-logged-by-mailbox-audit-logging    

If the above suggestion helps, please click on "Accept answer" and upvote it.
