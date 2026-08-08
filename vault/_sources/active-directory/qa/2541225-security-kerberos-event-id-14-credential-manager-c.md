---
title: "Security-kerberos Event ID 14 . credential manager causes system to login to network with invalid password and lock the account."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2541225/security-kerberos-event-id-14-credential-manager-c
question_id: 2541225
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 57
qa_tags: []
---
# Security-kerberos Event ID 14 . credential manager causes system to login to network with invalid password and lock the account.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2541225/security-kerberos-event-id-14-credential-manager-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A number of systems on the domain keep locking a specific account. When this happens, the system logs event 14 which clearly shows the domain\account that is being used to access a server share. I have been able to clear the stored credential by logging
 in to a few systems using remote desktop and issuing the following:

-  Launch a command prompt and run "psexec -i -s -d cmd.exe"

-  From the new DOS window run "rundll32 keymgr.dll,KRShowKeyMgr"

This launches the "Stored User Names and Passwords" dialog within the System context, which allows me to manually remove the stored credentials.

Obviously, this manual process is extremely time consuming. What I'm looking for is a way to automate this procedure, maybe using ADVAPI32.dll?

Any help greatly appreciated.

Thank you.

JP

## Answer (community) — community member

*upvotes: 0 · updated: 2012-09-24*

Hi,

The issue you posted would be better suited in the TechNet Forums. I would recommend posting your query in the TechNet Forums.

**http://social.technet.microsoft.com/Forums/en/category/w7itpro**
