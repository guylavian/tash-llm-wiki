---
title: "Replication (SYSVOL) EventID's 4612 and 5012"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/680218/replication-sysvol-eventids-4612-and-5012
question_id: 680218
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Replication (SYSVOL) EventID's 4612 and 5012

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/680218/replication-sysvol-eventids-4612-and-5012 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 Server 2019 Domain controllers. AD01 and AD02. AD01 has all FSMO roles.  

Have been in the process of eliminating 2 Server 2012 DC's  

In Event ID 5012, Error 9026 on AD01 I see the following  

//////////////////////////////  

The DFS Replication service failed to communicate with partner AD01 for replication group Domain System Volume. The partner did not recognize the connection or the replication group configuration.  

Partner DNS Address: AD01.domain.org  

Optional data if available:  

Partner WINS Address: AD01  

Partner IP Address: ::1  

/////////////////////////////////  

I believe that the ip address being shown is incorrect and that it should be 10.5.5.4.  

It seems like that the incorrect " Partner IP Address: ::1 " is IPV6 related. So while I mention that, I do want to say that IPV6 has been disabled. I don't understand how or where " ::1 " is being picked up from.  

AD02 DFS Replication logs look clean without errors.  

In DNS and was resolving the correct IP address 10.5.5.4  along with  with the " ::1 "  address and saw this and didn't think anything of this. After i started to see EVENT ID 5012 with the  " ::1 "  addressing for AD01, I when back through DNS and eliminated all the " ::1 "  instances leaving just 10.5.5.4 for AD01. The hope was that " Partner IP Address: ::1 " would change to Partner IP Address: 10.5.5.4  

Does anyone have any ideas where " ::1 " is coming from?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-31*

Another simple resolution may be to move roles off, demote, reboot, promo it again. While it is demoted it wouldn't hurt to confirm domain health was 100% before next steps.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-31*

@Anonymous       

I tried the non-authoritative sync as you suggested. That did not resolve the replication problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-31*

@Anonymous       

This happened after removing the old Server 2012 instance. DFS Replication was working fine prior to the removal.     

So I verified the IPV4  IP address and loopback 127.0.0.1 as you suggested.     

How do I stop the IPv6 loopback address? IPv6 is not enabled on these DC's

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-31*

Does anyone have any ideas where " ::1 " is coming from?  

IPv6 loopback address  

I'd check that each domain controller has own static ip address plus loopback (127.0.0.1) listed for DNS and no others such as router or public DNS. Its also very important to verify domain health is 100% before adding new ones into the mix.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
