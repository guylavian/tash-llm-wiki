---
title: "Active Directory Server Default Administrator Account is being disabled automatically"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/237797/active-directory-server-default-administrator-acco
question_id: 237797
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory Server Default Administrator Account is being disabled automatically

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/237797/active-directory-server-default-administrator-acco (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

Active Directory Server Default Administrator Account is being disabled, I recently tried to install ADRMS services after that I'm facing this issue I'm not sure if this issue is related to ADRMS... I just removed the ADRMS services but the issue is still there... There are many events by "System" and it's clear that "System" is disabling this account but I don't know the exact reason.  

Thank you in advance for your support.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-21*

Dear @Aamir Sohail  ,    

You are welcome. Thank you so much for your kindly reply.    

Okay, we are waiting for the update. For any question, please feel free to post here.    

It is hard to say. According to the below link,     

"The following conditions prevent disabling the Administrator account, even if this security setting is disabled.    

The Administrator account is currently in use    

The Administrators group has no other members    

All other members of the Administrators group are:    

Disabled    

Listed in the Deny log on locally User Rights Assignment"    

Link: https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/accounts-administrator-account-status    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Dear Hannah,    

Thank you so much for your reply. This policy was set on default I didn't change this policy. But the default set saying "Disabled" which might be the cause of this problem. I enabled this policy and set it to "Enabled"    

!    

    

Now I believe it will resolve the problem I'll update you tomorrow about it.    

But I'm still confused: I was working as it is for more than 3 months. I don't know why I show up just a few days ago. Is it because of windows update? or what?    

Thank you again for your help :-)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Hello,    

Thank you so much for posting here.    

Since it is being disabled automatically, we could see if the group policies takes effect.     

Press Windows key + R. This will open Run. Alternatively, you can go to Start and search for ‘Run’    

In Run dialog box, type gpedit.msc and hit Enter.    

Navigate to the location: Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options.    

Now on the right hand pane double-click on Accounts: Administrator account status.    

We could check the status. If it is Disabled, please select Enabled and click on Apply.    

    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
