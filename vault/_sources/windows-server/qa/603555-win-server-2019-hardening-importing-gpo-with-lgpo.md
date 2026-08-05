---
title: "Win server 2019 hardening, importing GPO with LGPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/603555/win-server-2019-hardening-importing-gpo-with-lgpo
question_id: 603555
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Win server 2019 hardening, importing GPO with LGPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/603555/win-server-2019-hardening-importing-gpo-with-lgpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have a stand-alone win server 2019 that after running the LGPO.exe to import the previous GPO from another machine, our nessus scanner reflecting over 100 non-compliance.  

However, if we were to run the baseline script on top of the above, the findings falls to the level that we first saw in the nessus scanner.  

The compliance we selected are CIS Microsoft Windows Server 2019 MS, L1 and L2 together.   

Wonder if anyone encounter such issue before and was resolve it. Where only 1 full GPO is been exported.  

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-28*

Hi @dan den  ,    

I found some similar threads that might be helpful for you , you can try out the steps shared in these forums     

https://learn.microsoft.com/en-us/answers/questions/44252/hardening-group-policy-template-adn-importing-it-t.html    

https://social.technet.microsoft.com/Forums/en-US/ce8d4e22-2e14-4ec9-b5b0-3368664813bf/hardening-group-policy-template-and-importing-it-to-windows-server-2016-group-policy?forum=winserversecurity    

----------    

--If the reply is helpful, please Upvote and Accept it as an answer--
