---
title: "Exchange Registry Key Missing (Outlook 2016)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/122797/exchange-registry-key-missing-outlook-2016
question_id: 122797
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Registry Key Missing (Outlook 2016)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/122797/exchange-registry-key-missing-outlook-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

I have come across and issue with Exchange Hybrid where the Outlook client prompts for credentials after migration. The fix detailed in the article below resolves the issue.    

https://learn.microsoft.com/en-us/outlook/troubleshoot/authentication/outlook-prompt-password-modern-authentication-enabled    

However, a lot of the Outlook clients seem to be missing the HKCU\Software\Microsoft\Exchange key all together and I cannot work out why some have it and others do not. There is nothing on the internet explaining why this issue occurs. Has anyone come across this before?     

Thanks,    

Mike.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-07-28*

Try opening regedit as the user not as admin.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-10-12*

Hi Mike,  

However, a lot of the Outlook clients seem to be missing the HKCU\Software\Microsoft\Exchange key all together and I cannot work out why some have it and others do not.   

I've tried to search around but cannot find a good explanation for this as well. Based on my experience, it's not uncommon that some registry keys are not existent on clients side and we need to manually add the key when need to apply certain settings. But honestly this doesn't explain why this key is only missing on some clients in your environment.   

Given this, would you please have a look at the path below on one of the affected clients and see if the "Exchange" key is located there?  

HKEY_CURRENT_USER\Software\Policies\Microsoft   

If it's not there either, I'd suggest just going ahead to manually add the registry keys required.  

Update:  

Current status:  

Manually creating the registry doesn't work. Recreating Outlook profiles works, but there are a large number of users in the org.  

Suggestion:  

Recreate Outlook profile for all users via GPO. For detailed steps, you can refer to the link below:  

How to create a new Outlook profile for all users in the domain  

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)  

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
