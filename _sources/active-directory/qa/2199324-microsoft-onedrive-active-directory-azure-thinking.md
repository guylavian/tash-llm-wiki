---
title: "Microsoft/OneDrive/Active directory/Azure thinking im part of organization"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199324/microsoft-onedrive-active-directory-azure-thinking
question_id: 2199324
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Microsoft/OneDrive/Active directory/Azure thinking im part of organization

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199324/microsoft-onedrive-active-directory-azure-thinking (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

For a long time now Ive had problems. I dont know what it is, but my leads keep getting me back to Azure and my Outlook-mail.  

On all sites I go Im getting redirected to wrong country and to the company/commercial/developer/enterprise homepages. An example is if I try to enter the Norwegian site www.komplett.no I get redirected to www.komplett.no/bedrift (bedrift means company). Or if I go to asus and want to visit the norwegian site I get redirected to the US site. I also have sort of access to log-in to Azure but then I get kicked out right away. I cant find anything or anywhere on my account saying Im in an organization and Im out of options for places to look.  

The reason I think it has something to do with my Outlook is because the problem dosent happent until I log in to my outlook. Ive had so many clean installs on my PC, and no problems are showing until I log in. It might be connected to something else but I dont know.  

I also got a new PC and router during this time and the same problem keeps happening and it makes my system corrupt.  

Things I can come up with now that I have tested many times;  

My second guess is it has something to do with Active Directory and some admin priviligies. The reason for this is the folders and files showing up on my PC.  

Its so many files from Group Policy and they are all dated 07. may 2022. I thought it was my old PC corrupt system but when i bought my new one and same files showed up with exact same date 07. may 2022 I thought I was gonna lose my mind. This is not files stored in my OneDrive  

Clean install  

Sfc /scannow  

DISM  

DHSCK  

Resetting network  

Removing all connections from my account. 3rd partys and Microsoft  

The typical malware removal tips when you google

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-27*

Hello,

From your description, it sounds like you're experiencing a complex issue involving persistent redirects, access restrictions, and unexpected system changes possibly tied . Here's a step-by-step approach to troubleshoot further: 

-  Sign out of all Microsoft accounts on your computer and browsers. Clear cache and cookies in your browsers,Temporarily disable browser extensions, as they can sometimes interfere with site redirections or logins. 

-  Continue troubleshooting network-related issues. Check your DNS resolver settings to ensure you're not being redirected due to a misconfigured DNS server. Try changing Public DNS. 

-  Ensure you performed a clean installation of Windows on your new PC, avoiding restoring data or settings from backups that might carry over the issue.Create a new local user account (non-Microsoft) on the new PC and test the behavior to see if the issue persists.

I hope the above information can help you!

Best regards

Zunhui
