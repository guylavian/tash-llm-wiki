---
title: "Installing Addiotnla Domain Controller from remote site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/176461/installing-addiotnla-domain-controller-from-remote
question_id: 176461
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Installing Addiotnla Domain Controller from remote site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/176461/installing-addiotnla-domain-controller-from-remote (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two sites and the details below.  

site A having PDC with Server 2019 and also we have additional Domain controller installed.  

Site B having server 2019 RODC installed and working fine.  

We want to install Additional Domain controller in the Site B, but after installing ADC and the server keeps rebooting continuously.  

Please advice how to resolve the issue.  

Thanks  

Krishna

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-26*

HI    

did you deploy RWDC as second DC in site B ?    

An RODC, by design, has enhanced security benefits and administrative simplicity that make it a good fit for a perimeter network or a branch office deployment. If an RODC is compromised, it expose only the resources within its site (when it has a well-configured PRP in place). The moment that an RWDC (whether it is a Windows Server 2003 or a Windows Server 2008 RWDC) is placed in a site with an RODC, the benefit is lost because, if the RWDC is compromised, the resources of the whole domain are exposed.    

Placing Several RODCs in the Same Site    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee522995(v=ws.10)?redirectedfrom=MSDN    

Planning Domain Controller Placement    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/planning-domain-controller-placement    

multiple RODC    

https://social.technet.microsoft.com/Forums/en-US/806eda3a-0195-4140-90da-6bf81c064dea/multiple-rodc?forum=winserverDS
