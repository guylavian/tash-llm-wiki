---
title: "We patched our 2019 Domain controller and now member servers are getting The Netlogon service denied a vulnerable Netlogon secure channel connection from a machine account."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187552/we-patched-our-2019-domain-controller-and-now-memb
question_id: 2187552
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# We patched our 2019 Domain controller and now member servers are getting The Netlogon service denied a vulnerable Netlogon secure channel connection from a machine account.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187552/we-patched-our-2019-domain-controller-and-now-memb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We did security updates on the DCs (that were 7-8 months out of day, I know) and now member servers are having issues connecting. 

Event ID: 5827

The Netlogon service denied a vulnerable Netlogon secure channel connection from a machine account.  

 Machine SamAccountName: MARTIN 

 Domain: court13.local. 

 Account Type: Domain Member 

 Machine Operating System: Windows Server 2016 Standard 

 Machine Operating System Build: 10.0 (14393) 

 Machine Operating System Service Pack: N/A  

For more information about why this was denied, please visit  https://go.microsoft.com/fwlink/?linkid=2133485.

We patched one server fully yesterday and it fixed the issue. Does anyone happen to know what patch is correcting this issue?

thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-17*

Hello Michael Dupler,  

Thank you for posting in Microsoft Community forum.  

Please check all the patches on the one server you installed yesterday.  

Open PS and run get-hotfix and check the installation time via InstalledOn.  

For example:  

  

Then you can provide KBs to us and we will help to check the KBs you installed yeterday.  

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
