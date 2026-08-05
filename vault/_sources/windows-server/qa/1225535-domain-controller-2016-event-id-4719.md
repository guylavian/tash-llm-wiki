---
title: "Domain Controller 2016, event ID 4719"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1225535/domain-controller-2016-event-id-4719
question_id: 1225535
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain Controller 2016, event ID 4719

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1225535/domain-controller-2016-event-id-4719 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello team,
I have another "spicy" and very similar issue as had last one (details below):
https://learn.microsoft.com/en-us/answers/questions/1189485/windows-2019-audit-policy-being-overwritten-by-som?comment=answer-1187942&page=1#comment-1232881  

I have problem on domain controllers 2016. When GPOs are applied, there are event IDs
4719 - auditing added (there are several security auditing configured), but then immediatelly
there again events 4719 auditing removed.  

We are using BASIC auditing, NOT advanced, that means settings
Audit: Force audit policy subcategory settings (Windows Vita or later) to override audit policy category settings" - DISABLED  

when you run command "auditpol /get /category:*" the result on all audits is "NO AUDITING"  

Can someoen help me on this please?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-14*

Hello Jan Kratochvil,  

Thank you for your reply.  

We must be very careful in production environment.  

I think you have can try two options below:  

Option 1. You can use advanced audit policy.  

Option 2. If you do not want to use advanced audit policy. You want to roll back to legacy auditing.   

1.You can try to do a similar test in your lab based on the link below and check   

If it works.  

https://serverfault.com/questions/631530/mistakenly-configured-advanced-audit-policies-return-to-basic  

2.If so, please back up all DCs and all audit policy GPO.  

3.Then roll back to legacy auditing in your production environment.  

4.In case，finally, if there is a problem with the audit policy, we can also restore or manually reconfigure.  

Hope the information above is helpful. If you have any question or concern, please feel free to let us know.   

Best Regards,   

Daisy Zhou

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-13*

Hello Daisy,
        I have read your posted link, but to be honest link is not related to this problem?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-13*

Hello Jan Kratochvil,  

Thank you for posting in our Q&A forum.  

You can try to check why the event appear and disappear again based on this similar thread.  

https://learn.microsoft.com/en-us/answers/questions/1000078/security-event-log-id4740-4767-appear-and-then-dis  

Hope the information above is helpful. 
If you have any question or concern, please feel free to let us know. 
Best Regards, 
Daisy Zhou
