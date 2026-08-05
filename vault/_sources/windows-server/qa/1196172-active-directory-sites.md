---
title: "Active Directory Sites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1196172/active-directory-sites
question_id: 1196172
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory Sites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1196172/active-directory-sites (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Everybody,
Our company has two office. We configured a Site2Site VPN between the two location, but in the secondary office has slow bandwidth.
We installed there a DC and DHCP server, but if I login in the HQ we feel the slow conection. 
I want to configured two site (HQ, Secondary). In the HQ has lots of subnets (50), but in the secondary office has just 6 subnets.
If i configured a sites with 6 subnets (Secondary site), then it will work, or i need to configured the HQ sites and all subnets too?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-05*

Hello Thank you for your question and reaching out. 
I can understand you are having query\issues related to AD sites. The sites' and subnets' layout should make it easier for users to use the dc locator process to locate the closest domain controller for authentication. If its is small site then there is no need to introduce many subnets as it will create more confusions. 
On Both Client computers make sure preferred DNS ip should be of your Respective location's DC's ip. Reference: https://social.technet.microsoft.com/wiki/contents/articles/52587.active-directory-design-considerations-and-best-practices.aspx 
--If the reply is helpful, please Upvote and Accept as answer--
