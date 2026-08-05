---
title: "Active Directory blocks Store"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/343198/active-directory-blocks-store
question_id: 343198
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active Directory blocks Store

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/343198/active-directory-blocks-store (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have followed guide after guide but I am getting nowhere. I am using active directory to teach myself how corporate's environments work. This issue has just came up and I cannot seem to get anywhere to solve it. While on my active directory account with admin privileges' I cannot access the Microsoft store nor any of the applications that will get installed through it such as the xbox gamepass app. I have my main GPO set to allow the Microsoft store but that did not solve it. This is the error code I get "0x80131500" and I have lookup the error code and followed the guide that comes up and that did not help. Is it possible that there is a hidden permission in windows server 2019 that would allow this to work?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-05*

I am stumped I have no idea what to do.    

You can add your domain account to the local administrators group.    

    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-05*

Hi，  

Based on the information you provided, the local administrator can open the store ,the error just for the domain users.  

I would suggest you check :  

1,Check if it fix the issue if you add the domain user to the local administrator.  

2,Check the gpresult for the user, run the command :gpresult /h filename.html. Confirm if any related policies was set for the STORE.  

If there are any progress , welcome to share here!  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-04*

Something here might help.  

Store error 0x80131500  

--please don't forget to Accept as answer if the reply is helpful--
