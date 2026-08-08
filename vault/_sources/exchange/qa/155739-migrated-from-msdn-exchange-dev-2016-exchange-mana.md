---
title: "[Migrated from MSDN Exchange Dev]2016 Exchange Management Shell will not load as Administrator"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155739/migrated-from-msdn-exchange-dev-2016-exchange-mana
question_id: 155739
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]2016 Exchange Management Shell will not load as Administrator

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155739/migrated-from-msdn-exchange-dev-2016-exchange-mana (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

We just noticed that all of our Exchange 2016 servers (running on Win 2012 R2) will no longer launch as administrator.  

When we right click the EMS and select "run as adminstrator", the shell window opens up as "Administrator:  Serveraname.domainname but, when the 2nd "Verbose:  Connected to Servername.domainname" appears, the shell goes to "Machine:  Servername.domainname"  

We discovered this when we tried to run a command "Get-Inboxrule" and it said the mailbox did not exist, which it does.  

We had 2 things happen this past weekend - 1st, we updated our external certificate and 2nd, we installed CU18 over the weekend.  We checked the new cert and it's assigned to SMTP, IIS, IMAP, POP on all exchange servers.  I didn't think the EMS was tied to an external cert, only the Exchange certificate (Which does not expire until late next year)  

Anyone heard of any issues with CU18 causing this issue?  We have 1 issue with CU18, users who log into OWA to access a shared mailbox can no longer download a file (it points to O365, and we are not setup for Hybrid), so we are waiting for the next CU release to fix that issue (we have a work around until then).  

Thoughts?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Hi ,    

According to my test results in a lab environment, this display is by design. You could run the following command to view who login the EMS.    

```
WhoamI
```

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
