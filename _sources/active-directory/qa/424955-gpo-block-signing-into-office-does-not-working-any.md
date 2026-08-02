---
title: "GPO \"Block Signing into Office\" does not working anymore"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/424955/gpo-block-signing-into-office-does-not-working-any
question_id: 424955
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# GPO "Block Signing into Office" does not working anymore

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/424955/gpo-block-signing-into-office-does-not-working-any (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we have our own on-premise exchange infrastructure and need to prevent using o365 accounts in Office / Outlook 2016.    

Therefore we have configured the follow GPO "Block Signing into Office" with "None allowed". That had worked for the last times.    

Since view weeks, it does not works anymore and every user can add a third-party O365 account to our Office suite.     

The GPO are applied and the reg value are correct.    

    

Are there any known changes by MS in Windows, Office or GPOs that have changed the behavior?    

What can I do, to block the O365 cloud features on my devices?    

We are running Windows 10 Enterprise v1809 and Office 2016.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

Hi,  

If your GPO has been successfully applied, then the current problem should not be within the scope of AD knowledge.  

According to my understanding, you can contact the o365 team now, this seems to be a problem with o365.  

You can post in the corresponding team or change the tag.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-09*

GPO's applied successful.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-09*

Hi，  

Before answering your question, I would like to confirm some information with you  

Is your GPO application successful? You can share a screenshot of whether the application is successful or not to us.  

We specify the next solution based on the results.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

Thanks for your reply, unfortunately it does not help.  

I have also try the follow both keys with no luck.  

HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Internet\  

DWORD: UseOnlineContent  

Value: 0  

HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity\  

DWORD: EnableADAL  

Value: 0  

Are there any changes during Windows Updates or Office Updates which ignore this configurations?  

before , our members got a popup, that the feature has been disabled by sysadmin.   

The current behavior is very bad. The ignore of the gpo settings will fail our security policies.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-08*

Did the user not log in to the account or not activate Office before using the “Block Signing into Office” policy?    

I suspect if apply it to a computer that has not yet had Office activated, it causes user cannot login to activate Office.  I have also tested this policy on my computer and I have activated my Office 365. For example, I choose “None allowed” and click OK.    

    

Then OneDrive is removed from “Save As” option and Office is still active    

    

If this isn’t help, you can try disable could features through the following registry key:    

HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Internet    

DWORD: UseOnlineContent    

Value: o    

Hope it works.    

Regards,    

Vicky
