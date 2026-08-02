---
title: "How to stop ldap services to stop client from communicating to a DC?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/184435/how-to-stop-ldap-services-to-stop-client-from-comm
question_id: 184435
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How to stop ldap services to stop client from communicating to a DC?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/184435/how-to-stop-ldap-services-to-stop-client-from-comm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am trying to stop the communication between client and a DC. I do no want the replication to stop between DCs. I have stopped KDC and netlogon service but client still reaching to the DC.  

Is there a way to stop the LDAP services?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-10*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-07*

Hi,  

Just checking in to see if the information provided was helpful.  

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Hi,  

Thanks for post.  

According to my knowledge, we could not disable LDAP.  

You force your applications to use LDAPS instead of blocking LDAP. Would you destroy the wall if you just want to change a brick at top of it?   

Active Directory depends on LDAP and if you try to modify that in a way to clock LDAP, you introduce new problems. So the anser is no.  

More information please refer to the following similar issue:  

https://social.technet.microsoft.com/Forums/windowsserver/en-US/ff0fc815-69be-4239-8a03-27cfd444d04c/use-ldaps-636-and-disable-ldap-389?forum=winserverDS  

Thanks for your support and understanding.  

Best Regards,  

Vicky

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-03*

Ideal setup would be to put the DC in a diff site. If that's not possible, then you could increase the weight of LDAP service record for that DC and decrease the priority. However this set up is not a recommended one. You can refer https://blogs.msmvps.com/acefekay/2010/01/03/the-dc-locator-process-the-logon-process-controlling-which-dc-responds-in-an-ad-site-and-srv-records/ for more details. There is no out of the box way to control this behavior from the client side.
