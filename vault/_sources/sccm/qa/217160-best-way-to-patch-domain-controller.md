---
title: "best way to patch Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/217160/best-way-to-patch-domain-controller
question_id: 217160
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-updates"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# best way to patch Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/217160/best-way-to-patch-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we are about to enroll servers in sccm patching.  

whats the best way to patch Doman controller, what process is the best recommended. please advise as need to create design and then POC.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-04*

Hi @Karun Khanna  ,    

I would recommend to you to start with deploying the patches on servers with a separate steps, first one, you can target the TEST servers, then the PILOT then the PROD.    

For example, if you have multiple domain controllers, add one of them in the PILOT servers device collection and once all it's fine, you can start deploying the PROD.    

Regards,    

Youssef Saad | New blog: https://youssef-saad.blogspot.com    

Please remember to ** “Accept answer” ** for useful answers, thank you!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-04*

@Karun Khanna       

Thank you for posting in Microsoft Q&A forum.    

There is no such best way because it based on your actual situation.    

We can use SCCM to patch DC like other clients but we cannot restart DC at any time, so we can suppress the servers restart when we deploy updates, then we can manually restart it at a time when it can be restarted.    

    

We can also configure maintenance windows to make sure updates installed in the specified time period.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
