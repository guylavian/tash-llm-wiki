---
title: "active directory  over site to site vpn"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/626130/active-directory-over-site-to-site-vpn
question_id: 626130
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# active directory  over site to site vpn

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/626130/active-directory-over-site-to-site-vpn (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have three dc's on-premises and another one I am planning on a private cloud, the link is  a  slow link   

The reason for the cloud is just to authenticate users who are using some web application. ( the web site  hosted  in the private cloud  and will be connected to the active directory using a ldap string )   

Do I need to create a separate site for cloud ?   

Please advise to design   

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-16*

Yes , you will need to create separate AD site , ip subnet for cloud.  

Also, You will need to configure Firewall rules and setup VPN link so that AD replication works smoothly.  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-13*

Most likely yes.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
