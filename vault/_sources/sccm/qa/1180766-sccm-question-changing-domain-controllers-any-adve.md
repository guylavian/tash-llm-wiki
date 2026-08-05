---
title: "SCCM question - changing Domain Controllers - any adverse effects?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180766/sccm-question-changing-domain-controllers-any-adve
question_id: 1180766
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM question - changing Domain Controllers - any adverse effects?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180766/sccm-question-changing-domain-controllers-any-adve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Our current main DCs are server 2012. The infrastructure team is about to replace the DCs with new server 2022. The new DCs will use the same IP addresses but different FQDNs.

Will this change affect our SCCM connections in any ways?

Thank you for your time.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-15*

Hi, @M Tran  

Thank you for posting in Microsoft Q&A forum.

We can see the support for Active Directory domains in Configuration Manager, here is the requirements and limitations:

It's not supported to change the following configurations for a computer that hosts a site system role:

-  Domain membership, including if you remove a site system from the domain, and then rejoin the same domain.

-  Domain name

-  Computer name

https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/configs/support-for-active-directory-domains#requirements-and-limitations

According to your description, the domain name is changed, so it will affect all the site system.

You may need a new SCCM and migrate the old SCCM to the new one.

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Add comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
