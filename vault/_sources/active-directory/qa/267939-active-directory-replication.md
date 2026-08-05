---
title: "Active Directory Replication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/267939/active-directory-replication
question_id: 267939
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active Directory Replication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/267939/active-directory-replication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to speed up AD replication by going off this article  

https://social.technet.microsoft.com/wiki/contents/articles/16929.set-active-directory-to-use-notify-replication.aspx  

I have changed the Inter-Site Transports > IP option to 1, but the actual connection shows 0x5 = ( IS_GENERATED | OVERRIDE_NOTIFY_DEFAULT ) and the "instant" replication is not happening. Is there something I'm missing?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-11*

Hi,  

Before going further , i would like to confirm that if all your sites are in the same site link?  

If all the sites are in the same site link (DEFAULTIPSITELINK), you can just configure it as the way in the link you provided.  

If you have several sites links, you will have to configure each site link.  

For manually created sitelinks:  

Open ADSIEDIT  

Connect to Configuration Naming Context  

Expand Sites –> (The site name) –> Servers –> (Servername) –> NTDS Settings  

Right-click the relevant sitelink and select properties  

Change the value of “options” to 8  

Repeat for every manually configured sitelink (if desired)  

https://pertorben.wordpress.com/2016/01/12/enable-immediate-replication-between-ad-sites/(Third-party link)  

Wait for all the changes replicate to all the DCs, you can do that by command:repadmin /syncall /AdeP  

This response contains a third-party link. We provide this link for easy reference. Microsoft cannot guarantee the validity of any information and content in this link.  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-10*

Something here may help.    

https://learn.microsoft.com/en-US/troubleshoot/windows-server/identity/modify-default-intra-site-dc-replication-interval    

--please don't forget to Accept as answer if the reply is helpful--
