---
title: "Exchange hybrid mailuser"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/279032/exchange-hybrid-mailuser
question_id: 279032
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange hybrid mailuser

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/279032/exchange-hybrid-mailuser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Exchange 2016 hybrid with Exchange Online.  I have migrated about 200 mailboxes so far.  

I am noticing something that I don't understand and that seems to be affecting the performance of a third-party application.  When I run "Get-MailUser" on the on-premises Exchange Server, it returns 3 special accounts created for specific applications.  When I run "Get-Recipient ******@mycorp.com" (where jdoe is a mailbox that has been migrated to O365), the results list the RecipientType as "MailUser".  This is true of any migrated mailbox.  

If I run Get-MailUser in Exchange Online, it returns a list of all the mailboxes still on premises.  

From the perspective of on premises Exchange Server, it appears that even though a migrated mailbox is listed as a MailUser when listing recipients, it is not really seen as an actual MailUser.  

Is this normal, or do I have something configured wrong?  

Thank you very much for your help.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-18*

Thank you very much!  That clears it up for me.  

The application in question was written to run against Exchange Server, and it seems to check for the existence of a mailbox or a mailuser.  That's why my questions.  

Thanks again for the explanation.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-18*

Thank you very much.  Forgive me, but I am still a little unclear.  You said that "The remote mailboxes in 365 will shows on-prem will show as mail users..."  

In my case, the Exchange Online mailboxes do show as MailUser in response to a Get-Recipient cmdlet, but if I run Get-Mail-User from Exchange Server, I do not see any of the Exchange Online mailboxes.  All I see are 3 MailUsers that were created long ago on premises.  

Should I see the Exchange Online mailboxes when I run Get-MailUser on the on premises Exchange Server?  

Thank you for your help.
