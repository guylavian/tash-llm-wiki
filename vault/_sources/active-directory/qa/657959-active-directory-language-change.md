---
title: "Active Directory Language Change"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/657959/active-directory-language-change
question_id: 657959
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Active Directory Language Change

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/657959/active-directory-language-change (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am looking for some insight into the default language of Active Directory and if possible, specifically can it be changed.   

If Active Directory was originally deployed in Spanish, can it be changed to English?   

Currently 99% of Ad is in English, including all created accounts and groups, however built in accounts and security groups, such as Administrator and Domain Admins are displayed in Spanish, such as Administradores.  This was due to the first deployed AD server that created the domain was done in Spanish, however all subsequent domain controllers were added in English.  

I feel like there has to be a way to change this, if not a complete rebuild of the domain will be in order.   

Any ideas?  

Thanks,

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-12-09*

@Anonymous   is right for the OS language.    

For groups and users which already exist, they will not be renamed after adding a new domain controller in English.    

You can rename the objects though. They have well-known SID so renaming them will not break them. Renaming a security principal (such as a user or a group) doesn't change their security identifier (SID). When you add a user or a group into another group, or use them in a security descriptor (the security tab on an object) the system stores the SID not the display name.    

It is possible to have a custom application that is using the display name or the distinguished name of the user. And renaming a group might break these. But 1 that's bad practice on the app side and 2 that's unlikely that they use the built-in objects as a reference like these.     

Also, note that many customers are using localized names for built-in objects because the first DC was installed in French, German or Spanish. It doesn't need to be "fixed". Some rare applications are looking for name of groups as opposed as SIDs, and that's really the app that needs to be "fixed".

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-10*

@Pierre Audonnet - MSFT   @Anonymous        

Thank you both, first off....    

So the original Spanish DC is gone, and have been replaced with English DCs. From what you are saying, the domain is now fully English and the Spanish names are merely holdovers from the original deployment in name only (underlying SIDs are independent of this language issue) and can be renamed or ignored. In addition, for all intents and purposes, the domain is deployed and configured in English, since all domain controllers currently in place were deployed in English, and this is all really a non-issue from a Microsoft AD deployment standpoint.     

Is this correct?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-10*

Thanks for both answers. Im currently reviewing the next steps with the information you provided. I'll post a response shortly.
