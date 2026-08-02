---
title: "AD GPO linking inheritance not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1294181/ad-gpo-linking-inheritance-not-working
question_id: 1294181
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# AD GPO linking inheritance not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1294181/ad-gpo-linking-inheritance-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

We need to block group policy editing (done) and also group policy linking. I am unable to understand the AD DS and inheritance why it is not working in my case please do give advice.

I am selecting any OU in group policy management and selecting the delegation tab in the right side. The default permission is link gpo selected. I add new security group. Add. Advanced settings i change the permission type to deny instead of allow. The permission is applied to this container and ALL of the child containers. If i check they do appling yet if I try to link a gpo with a restricted account i can see only the specific OU is blocked, the other child OU-s are still linkable. Why?

How can I prevent gpo linking to all the available and new OU-s?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-31*

Hello petersonal,

Thank you for posting in our Q&A forum.  

You can try set in the domain level.  

1.Right click domain name.  

2.Select the delegation tab in the right side. The default permission is link gpo selected.  

3.Add one normal domain user account.  

4.You will see the two entries after clicking Advanced button (for example, I add the domain user t2 below).  

One entry is for gplink permission (read gplink and write gplink).  

One entry is for gpoptions permission (read gpoptions and write gpoptions).  

You should set deny permission for the two entries.  

Then make AD replication complete if you have more than one DC in your domain.  

After that, you can log on DC with this normal domain user account and check if you can link gpo to domain and the OUs within Domain.  

Reference (delegate permission to link gpo):  

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789195(v=ws.11)  

Hope the information above is helpful. If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
