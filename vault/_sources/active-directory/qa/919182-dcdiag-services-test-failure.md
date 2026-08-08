---
title: "Dcdiag services test failure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/919182/dcdiag-services-test-failure
question_id: 919182
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Dcdiag services test failure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/919182/dcdiag-services-test-failure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I am executing Dcdiag /test:services /s:servername but it fails due to COM+system startup failure error.    

I set the startup type to Automatic, then it passes but after few hours it is failing again , when checked it is found that this COM+system startup changed to Manual automatically    

Also I am getting Invalid service type: DnsCache on servername , current value WIN32_OWN_PROCESS, expected value    

WIN32_SHARE_PROCESS.    

Anybody help is greatly appreciated

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-07-22*

Hello All,    

Finally found the issue, this startup type is flipping back due to an assigned GPO to the Domain Controllers OU , this GPO contains one setting for COM+ Event System service in which startup type is set as manual.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-07-08*

COM+ Event System is found as running but the startup type is manual .    

When I set the startup type for COM+ Event System service to Automatic , it passes but after some time it reverts back startup type to manual

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-12*

When I set the startup type for COM+ Event System service to Automatic , it passes but after some time it reverts back startup type to manual     

How to fix this ?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-11*

Hi there,     

Can you disable the anti-virus and do another test ??    

-  Make sure that your Domain Controller(s) are the only listed DNS servers on all of your Network Adapters    

-  Try and ping your domainainname.local and see if it correctly resolves your domain controller    

-  Run DCDiag from the Domain Controller rather than a remote workstation    

-  Run the Server 2012 Best Practices analyzers, starting with the DNS role    

I hope this information helps. If you have any questions please let me know and I will be glad to help you out.    

----------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
