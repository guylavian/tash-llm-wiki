---
title: "Conditional access in on-prem/ADFS enviroment for windows login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/846540/conditional-access-in-on-prem-adfs-enviroment-for
question_id: 846540
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Conditional access in on-prem/ADFS enviroment for windows login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/846540/conditional-access-in-on-prem-adfs-enviroment-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  

I've been searching for conditional access for the windows login. Could not find anything relevant to my case so far.  

AD FS relying party trust/access controll policies seems to be controlling access to applications, but I need to control windows logins.  

GPO require smart card or login but can't set a condition here.  

AAD access control seems same as AD FS controll access to applications but not to whether ask MFA for windows login.  

Is it possible to set up a conditional access where users outside of corporate network would have to use MFA (yubikey smart card PIV) to log into their windows account, while employees inside the network don't need a smart card for this?  

Not looking for conditional access into any application like o365 or the others, but plainly into their windows account managed by an op-prem AD.  

Thanks for any advice in advance!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2022-05-12*

You can force the user to use Windows Hello for Business or a smartcard to login to a system (Windows interactive sing-in). But you cannot do it based on their location (like you can in conditional access policies). You basically woud have to force it at the user level in AD (assuming you have domain joined systems).   

But with CAP, if most of applications are protected by Azure AD, then you could still enforce the MFA based on some other conditions at the application level.   

You can use multi factor unlock with Windows Hello for Business and you could have something like:  

-  If a user is connected on premises I can use just the facial recognition  

-  But if the same user on the same machine is connected from home, I will also need the PIN (called Multi Factor Unlock)

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-17*

Hi there,    

Conditional access can be achieved using Azure . Within a Conditional Access policy, an administrator can make use of signals from conditions like risk, device platform, or location to enhance their policy decisions.    

When configuring location as a condition, organizations can choose to include or exclude locations. Multiple conditions can be combined to create fine-grained and specific Conditional Access policies.    

What is Conditional Access? https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview    

Conditional Access: Conditions https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-conditions    

--------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-05-16*

Windows Hello for Business is seen as a smartcard logon in AD. So if you require a user to use a Smartcard for authentication, they can use a smartcard or Windows Hello for Business. But this doesn't take in consideration where the user is. It always applies.    

If you have Windows Hello for Business configured for your users, you can use Multi Factor Unlock feature: https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/feature-multifactor-unlock. So in that case, you can use mutliple factor to unlock the machine one of these factor is a trusted signal (which could be some network details such as the machine needs to be connected to a specific WiFi or have an IP address given by a specicic DHCP server etc...).
