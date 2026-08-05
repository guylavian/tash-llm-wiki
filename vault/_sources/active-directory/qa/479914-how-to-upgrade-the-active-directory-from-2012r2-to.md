---
title: "How to upgrade the active directory from 2012R2 to 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/479914/how-to-upgrade-the-active-directory-from-2012r2-to
question_id: 479914
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How to upgrade the active directory from 2012R2 to 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/479914/how-to-upgrade-the-active-directory-from-2012r2-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Expert,  

I have to upgrade our AD from 2012R2 to 2016, may I know what is the steps to do this upgrade and what should I have to do avoid any issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-02*

Thanks a lot for all of you for your  comments and guidance

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-19*

Hello @Ibrahim hasan  ,    

Thank you so much for posting here.    

As mentioned, we recommend we add a new 2016 DC to the existing domain instead of upgrading the Windows Server 2012 R2 to Windows Server 2016.     

Here are the steps about how to add a new DC to existing domain. We can try the above steps.    

1, Check DC health by running Dcdiag /v and check AD replication by running repadmin/showrepl and repadmin /replsum.    

2, Join Windows Server 2016 to existing domain.    

3, Promote Windows Server 2016 to Domain Controller.    

4, Repeat step1 to check AD environment health.    

5, Transfer FSMO roles to the new DC if needed.    

6, Demote the old DC if needed.    

7, Raise domain / forest function level based on our requirement and environment, as mentioned above.    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong
