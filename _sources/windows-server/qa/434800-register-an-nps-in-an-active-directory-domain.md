---
title: "Register an NPS in an Active Directory Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/434800/register-an-nps-in-an-active-directory-domain
question_id: 434800
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Register an NPS in an Active Directory Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/434800/register-an-nps-in-an-active-directory-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,  

I have been using NPS server for user based wireless authentication and it has been working fine on Windows 2008 R2 Server. Now I have migrated my NPS to Windows 2016 server as a member of a domain and it is working fine however I have never done anything with "Register an NPS in an Active Directory Domain" and that option is active in NPS. I am not sure if I need to register NPS server in an Active Directory Domain but wanted to understand if I really need to register NPS in AD.  

I have read on MS forum that "The dial-in tab of the user properties in AD is available" if NPS is registered in AD but that tab is already available in  my AD.  

Your advise is appreciated.  

Regards  

Justice Bali

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-15*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-15*

Hi,    

NPS must be registered in Active Directory so that they have permission to read the dial-in properties of user accounts during the authorization process.     

And registering an NPS will add the server to the RAS and IAS Servers group in Active Directory. As picture below:    

    

For more details, you can refer to the following article:    

Register an NPS in an Active Directory Domain    

Best Regards,    

Candy    

--------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-14*

Something here may help.    

https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-manage-register    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
