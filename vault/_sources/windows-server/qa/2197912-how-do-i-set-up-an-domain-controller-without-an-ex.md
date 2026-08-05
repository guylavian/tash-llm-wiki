---
title: "How do I set up an domain controller without an external domain?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197912/how-do-i-set-up-an-domain-controller-without-an-ex
question_id: 2197912
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# How do I set up an domain controller without an external domain?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197912/how-do-i-set-up-an-domain-controller-without-an-ex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am setting up a Windows 2022 server and want to make it a domain controller, but we do not have an external domain

How do I do this?

Thanks,

J.R.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-23*

Hello  

Please check the password policy on the server and then reset the local admin password does meet requirements.  

For domain name, you can name it like domain.com.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-22*

I used the domain name Artistic.local but I'm getting the error domain cannot be created because the local admin password does not meet requirements. 

How do I fix it?

Thanks 

J.R.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-22*

What format for a name do I use in "root domain name#?

Local.artistic.com.  or artistic.local

Artistic is the business name.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-22*

Hello JRSitman,

Thank you for posting in Microsoft Community forum.

Do you mean you want to set up the first domain controller without any existing domain? If so, please try the steps below.

1.You can set the IP and DNS server (set the IP of this server as the preferred DNS server) on this 2022 server.  

2.Then Add AD DS and DNS role on this server.  

3.Promote this server as Domain Controller.  

4.Select "add a new forest" and name the domain name during you promote it to domain controller.

5.At last, there will be one domain, and this server will be one Domain Controller in this domain.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
