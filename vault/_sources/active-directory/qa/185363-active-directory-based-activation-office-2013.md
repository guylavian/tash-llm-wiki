---
title: "Active Directory Based Activation - Office 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/185363/active-directory-based-activation-office-2013
question_id: 185363
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory Based Activation - Office 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/185363/active-directory-based-activation-office-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning, we are in the process of setting up a new Citrix XenApp environment and am coming up with activation issues for our office 2013 program on the cloned virtual machines. In researching this, due to the nature of the golden image setup for Citrix XenApp, it appears I need to do either a KMS setup or ADBA setup. My preference would be the ADBA setup.  

My question for all of you is, we have a volume license key for office 2013 and have it in use for our current older production Citrix environment. If I install/setup ADBA with this key, because I need it for the new environment, will this affect my current production Citrix environment that are all stand-alone windows 2008r2 Citrix servers? Will they be attempting to constantly reactivate themselves or will they recognize that they are already activated and won't cause issues?   

I appreciate the information in advance. It will be most helpful in ensuring I don't cause issues to my current live Citrix environment.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

@jkoelker       

Based on my research, you may use KMS and ADBA at the same time and ADBA uses the same host key that are used by KMS.     

KMS and ADBA not mutually exclusive.    

Does "stand-alone" just mean out of the domain but those KMS clients could connect to KMS host?    

For those previous KMS clients , they will still connect to the KMS host regularly (For example, once every 180 days) as before to resume activation process. So, you need to maintain the connection between the host and the clients.    

More informtaion please refer to "Active Directory-based activation of Office 2013" and "Active Directory-Based Activation Overview".    

Any updates please let me know.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
