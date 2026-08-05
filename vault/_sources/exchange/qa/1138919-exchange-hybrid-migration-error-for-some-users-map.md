---
title: "Exchange Hybrid - Migration error for some users : MapiExceptionNamedPropsQuotaExceeded"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1138919/exchange-hybrid-migration-error-for-some-users-map
question_id: 1138919
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid - Migration error for some users : MapiExceptionNamedPropsQuotaExceeded

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1138919/exchange-hybrid-migration-error-for-some-users-map (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

everything is in the title, I'm migrating our mailboxes to M365, we are in a hybrid scenario with Exchange 2016/Exchange Online.    

95% of our users are ok, but for 5 % batch migration is failing in the middle of the sync (sync start and run then fail) and  I have the following error :    

Error: QuotaExceededException: Cannot get ID from name. --> MapiExceptionNamedPropsQuotaExceeded: Unable to get IDs from property names.    

I checked all around quotas On prem, mailboxes are good for Exchange online quotas.    

I migrated concerned mailboxes to a new db tocheck if it could be related to a corrupt db same issue.    

If someone can help troubleshooting this, thanks in advance.    

Best regards

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-10*

Hi,
I tried the 2007 workaround with no luck.
Error is on Exchange Online NamedProperties limitation, it seems that my concerned mailboxes exceed the 30 000 Named Properties.
Ho can I  count/decrease/delete/remove some Named Properties for a particular mailbox ?

I tried  to see Named properties with the following
$Mailbox = Get-Mailbox -Identity "john.doe@ssss  .com"
$MailboxItems = (Get-MailboxFolderStatistics -Identity $Mailbox.Identity -FolderScope "All").Items
$NamedProperties = (Get-ItemProperty -Path $MailboxItems).NamedProperties | Measure-Object

but the NamedProperties is empty...

These 7 mailboxes are stucking our migration.... and support case we opened didn't help....  Actually the support guy asked me to remove a user from the failed batch and to test his mailbox only... It fails with a "primary mailbox already exist" error message and the support guy is focusing on it instead of our original issue....
I managed to workaround the primary mailbox issue, and the migration fail again with same message

Error: QuotaExceededException: Cannot get ID from name. --> MapiExceptionNamedPropsQuotaExceeded: Unable to get IDs from property names.

Any help will be appreciated.
Thanks in advance,
Best regards

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-22*

Hi,    

Thanks for the answer,    

Yes I spotted this KB but thought I wasn't concerned as we are in 2013 CU 23, and just some users are concerned.    

I already open a case with 365 support, but no useful answer so far.    

Regarding your question, there is a plugin that is archiving mails to a folder ina  file server but I don't know if it set a xHeader or other property.    

Thanks for the help,    

Best regards

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-22*

This is an old issue that used to plague Exchange 2007 and 2010:    

https://learn.microsoft.com/en-us/previous-versions/office/exchange-server-2007/bb851493(v=exchg.80)?redirectedfrom=MSDN    

Are you using some third party software that is updating messages with x headers or custom properties?    

I would open a case with 365 support and ask for guidance on how to handle.
