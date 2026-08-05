---
title: "Implement domain controller as HA version"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/76527/implement-domain-controller-as-ha-version
question_id: 76527
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Implement domain controller as HA version

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/76527/implement-domain-controller-as-ha-version (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi recently we plan to purchase 2 server 2016 (server A and server B) and implement a standalone Domain controller to run some failover features (server C,server D). Could someone guide me when installing a domain controller and it will automatic install DNS as well, my question is server A we set as a primary zove (transfer zone) and server B set a secondary zone if the server A is down will server A transfer to server B and keep the Domain controller running, thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-26*

Hi,  

If you promote multiple domain controller you can install DNS zone during the DC promotion.  

It's recommended to set DNS zone as integrated active directory DNS zone on all domain controller , in this case the DNS zone will be replicated automatically during active directory replication process.  

Don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-26*

Hi,  

Multiple domain controllers is for fault tolerance.They will sync the Active Directory information and can provide services if the other is unavailable.So we should always have at least 2 DC's .Since the replication is automatically, we don't need to do additional configuration.  

Following links for your reference:  

https://social.technet.microsoft.com/wiki/contents/articles/12370.windows-server-2012-set-up-your-first-domain-controller-step-by-step.aspx  

https://social.technet.microsoft.com/wiki/contents/articles/20098.setting-up-additional-active-directory-domain-controller-with-windows-server-2012.aspx  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-25*

If you have more than one domain controller, then any change made to one domain controller is automatically replicated to other domain controllers to ensure all domain controllers have the information. This happens automatically, you don't have to do anything special.
