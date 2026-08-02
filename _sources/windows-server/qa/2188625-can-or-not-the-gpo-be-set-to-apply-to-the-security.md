---
title: "Can or not the GPO be set to apply to the security group and not to the OU path?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188625/can-or-not-the-gpo-be-set-to-apply-to-the-security
question_id: 2188625
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Can or not the GPO be set to apply to the security group and not to the OU path?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188625/can-or-not-the-gpo-be-set-to-apply-to-the-security (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can or not the GPO be set to apply to the security group and not to the OU path? Please help.. thanks you for your help

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-06*

Hello DYP_274,  

Thank you for your reply.  

1.Create an GPO.  

2.Link it to domain. Right click the domain and select Link an existing GPO.  

  

3.Edit the GPO depending on your needs, right click this GPO and select Edit.  

4.Because it is computer configuration in GPO in your case, for "Security Filtering", we can keep "Authenticated users", make Authenticated users have only "Read" permission.  

For example: select your GPO and click "Delegation" tab and click Advanced "button".  

![](https://learn-attachment.microsoft.com/api/attachments/4697ac31-3031-4002-ab6d-6c86d627ffdc?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/a98cd12e-f148-4199-a3e4-6cc59634dc66?platform=QnA" title="filestore.community.support.microsoft.com" rel="ugc nofollow">  

5.And add computer group under "Security Filtering" by clicking "Add" button.  

  

6.Make computer group have "Read" and "Apply group policy" permissions.  

For example: select your GPO and click "Delegation" tab and click Advanced "button". You will see Group or user names, check "Read" and "Apply group policy" permissions for "Your computer group".  

If you have any question or concern, please feel free to let us know.  

https://learn-attachment.microsoft.com/api/attachments/3a5da7d2-abc9-4d8e-a192-6e0d45c9b17e?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-05*

I failed and couldn't apply the GPO. Can you give me an example?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-05*

Hello DYP_274,  

Thank you for your reply.  

***We do that because the computer objects to which the policy will be applied are in different OUs. So we want to create a security group to collect computer objects in a security group account.***A: You can link the GPO to domain, and because it is computer configuration in GPO, for "Security Filtering", we can keep "Authenticated users", make Authenticated users have only "Read" permission.

And add computer group under "Security Filtering", make computer group have "Read" and "Apply group policy" permissions.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-05*

Can you set the GPO to apply to the security group instead of the OU path?  

for example on table scope is blank, and than we set on security filtering for choose Security group  ?

We do that because the computer objects to which the policy will be applied are in different OUs. So we want to create a security group to collect computer objects in a security group account.

you have a solution ?   

thanks you so much for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-05*

Hello DYP_274,  

Thank you for posting in Q&A forum.  

Can or not the GPO be set to apply to the security group and not to the OU path?  

A: We must link the GPO to domain or OUs (because the domain user objects or domain machine objects are in the domain or OU), then the user (or user group) or machine (or machine group) or Authenticated users Under "Security Filtering" has "Read" and "Apply group policy" permissions.  

This GPO will apply to user or machine.  

  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
