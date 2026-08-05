---
title: "If we disable RC4 encryption in GPO Domain Level, it is not allowing users to login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/377020/if-we-disable-rc4-encryption-in-gpo-domain-level-i
question_id: 377020
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# If we disable RC4 encryption in GPO Domain Level, it is not allowing users to login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/377020/if-we-disable-rc4-encryption-in-gpo-domain-level-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If we disable RC4 encryption in GPO Domain Level, it is not allowing users to login.  

Issue: Old AD, RC4 encryption is there, client reported stating it is weak and to switch to AES.  

We enabled AES encryption >> tested >> all normal.  

We disabled RC4 encryption >> we couldn't connect back to environment (we use Client's Citrix for RDP), we were unable to connect. Reverted GPO settings, enabled RC4, and we were able to login.  

How to disable RC4 safely without any issue for user login.  

Please assist.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-05*

Hi,  

Before disable RC4 , you should check that all operating system and applications support AES.  

You have also enable AES on trust relationship between two domains and all service accounts with SPN  used to setup a service for kerberos authentication.  

If you have a keytab file check if it supports AES , if it's not the case you have to generate new one with AES.  

Some best practise to enable AES and Disable RC4  

Please don't forget to mark helpful reply as answer

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-30*

Hello @Dipak Shinde  ,    

Thank you for posting here.    

Before disabling RC4, please make sure to disable RC4 when it is no longer in use, otherwise it may affect the work of the environment.     

Based on the description "We disabled RC4 encryption >> we couldn't connect back to environment (we use Client's Citrix for RDP), we were unable to connect. Reverted GPO settings, enabled RC4, and we were able to login.",     

Here are my suggestions:    

There may be several aspects involved in this login process: client endpoint, remote endpoint, domain controller endpoint and Citrix endpoint. I’m not sure which endpoint or multiple endpoints only support RC4, but not support strong encryption (such as AES), so you need to check and confirm it, and then if you check it out, it is recommended to set strong encryption (such as AES) in all endpoints , in this case, even if weak encryption （RC4） is disabled, they all support strong encryption, so that you can log in successfully.     

Tips:     

-  You can capture network package or other methods to check.    

-  I am sorry, because private information and security information may be involved, the forum does not collect or analyze logs.     

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
