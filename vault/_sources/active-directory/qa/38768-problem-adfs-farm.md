---
title: "Problem adfs farm"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/38768/problem-adfs-farm
question_id: 38768
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Problem adfs farm

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/38768/problem-adfs-farm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

They could help me, I have a problem in farm adfs, I have a primary and a secondary adfs and they are in a Microsoft NLB, when I restart my primary adfs the entire authentication environment falls, I validated all certificates in the adfs and WAPs , would this compartment be normal?  

Would any procedure work around this problem?  

Thanks  

Alan F Maia

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-06-24*

I will perform updates on the server, since it is out of date, I should do it in a few weeks.  

I will follow this line before I continue troubleshooting  

Thanks  

Alan Ferreira Maia

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-06-23*

Microsoft NLB doesn't provide a full proof fault tolerance. A node will be considered up as soon as the TCP-IP stack of the machine is up and running whereas the ADFS service might not be running yet.  

That said, if you turn off complete one node, you should expect the authentication to work on the second node... I would start by creating an entry in your HOSTS file to make your ADFS FQDN point to the secondary node in a normal operation mode (2 nodes are up). And see if authentication works. If it does work, you have a NLB issue. If it doesn't work, you have an ADFS issue and we'll need to check if the database sync works properly and what not. For that second part, you can use these tool: Diagnostics Analyzer.
