---
title: "Exchange Server 2019, Help on Restored Server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1480658/exchange-server-2019-help-on-restored-server
question_id: 1480658
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019, Help on Restored Server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1480658/exchange-server-2019-help-on-restored-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need Assistand om Repairing Exchange Server, See PDF on Errors IErrors.pdf Received, Accessing OWA, ECP:

When Accessing OWA: 403 - Forbidden: Access Denied

When Accessing ECP: Http Error 403.503 - Forbidden

When Accessing in-Place eDiscovery & hold, virtual directories: error The Request failed. The remote server returned an error: 403 Forbidden

When Accessing migration: The migration batcg "setimmediate$0.3936076180443564$2" can't be found

When Accessing Mailbox: The operation couldn't performed because object 'setimmediate$0.40569671329708545$2' could not be found on 'fqdn'

When Accessing Groups,Contacts,OWA Policy,in-place eDiscovery & hold, address-list, malware filter, accepted domains, email address policies, receive connectors, send connectors, servers: The operation couldn't performed because object 'setimmediate$0.xxxxxxxxxxxxxxxxxxx$2' could not be found on 'fqdn' Basically the same as 5 just the numbers changing

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-29*

The error messages you've provided indicate issues related to permissions, configuration, or possible corruption in Exchange. 

Check the pointers below.

-  Verify User Permissions

-  Check IIS Virtual Directories

-  Review IIS Logs

-  Run the Exchange Best Practices Analyzer (BPA)

-  Repair Virtual Directories

-  Check Event Viewer

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-09*

Hello @Dawie Human  

Thank you for sharing and welcome to Microsoft Q&A！

Could you confirm the following:

<<Need Assistand om Repairing Exchange Server

Are you referring to Recover Exchange servers? 

Then please check:

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-exchange-servers?view=exchserver-2019

What actions did you perform recently that caused these issues?

Regards

SF

If the answer is helpful, please click "Accept Answer" and kindly upvote it.
