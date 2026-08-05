---
title: "what is best way to compare two domain gpo to find missing setting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1603387/what-is-best-way-to-compare-two-domain-gpo-to-find
question_id: 1603387
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# what is best way to compare two domain gpo to find missing setting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1603387/what-is-best-way-to-compare-two-domain-gpo-to-find (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
we have import or export the gpo from one domain to another domain and check that some of link are missing may be not available in another domain side . Now need to validate what are linked that in scope of gpo are missing  to we can manually add  link this in new domain object.
thanks
Richa

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-01*

Hello Richa Kumari,

Thank you for posting in Q&A forum.

How did you export and import gpo from one domain to another? You can refer to the steps in the following link.

https://thomascheng.net/2018/07/11/exporting-and-importing-group-policy-object-between-domains/#:~:text=From%20the%20current%20domain%2C%20launch%20Group%20Policy%20Management,the%20exported%20GPO%20%28s%29%20to%20your%20destination%20domain.

To facilitate the migration of GPOs across domains, you may need to use the GPMC to modify certain settings to suit your environment during import or copy operations.

https://learn.microsoft.com/en-us/previous-versions/windows/desktop/gpmc/copying-and-importing-gpos-across-domains

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-29*

Hi @Richa Kumari 

You can use Policy Analyzer tools.
For more information please read this article: 
New tool: Policy Analyzer

Please don't forget to accept helpful answer
