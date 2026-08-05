---
title: "Active Directory Users and Computers, dsa.msc"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/465679/active-directory-users-and-computers-dsa-msc
question_id: 465679
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Users and Computers, dsa.msc

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/465679/active-directory-users-and-computers-dsa-msc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

What could cause dsa.msc, the Active Directory Users and Computers snap-in, to start after 5-10 minutes? It cannot be opened. Windows Server 2019 fixes?  

I request information.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-06*

Hello,    

This issue is likely due to the way that DNS is being handled by the application, and can likely be resolved by running dsa.msc while specifying the DC you are connecting to via IP as below:    

runas /profile /env /user:domain\username "mmc %windir%\system32\dsa.msc /server=yourDomainControllersIPaddress"    

This will launch ADUC without needing to resolve your DC's hostname through DNS and should resolve the latency issues.    

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-14*

The problem is that I don't know which KB it is: - (((  

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-13*

Hello  

Thank you for your response.  

yes only one DC,  

yes, only the Active Directory Users and Computers snap-in and Active Directory sites and services open badly. Very long. DNS, DHCP, etc. open well.  

I did a clean boot. The problem is the same. The starters take a long time to run.  

Updates broke it. Was well. What to do? Help? It is impossible to work.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-09*

Thank you for your response  

-  The Active Directory Users and Computers snap-in takes a long time to start. It takes more than 5 minutes. It opens up. Reading account properties takes a long time, etc. You can work on it, but it takes a long time to perform tasks on it.   

-  It shows no error. It opens but after a while.   

-  Everything worked fine. The domain controller was working fine. I don't know if this happened after system updates.   

-  Working at AD   

-  Yes I can open other entrees. They work normally.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-08*

Hello @Andrzej Wysocki  ,

Thank you for posting here.

To better understand the question, please confirm the following information at your convenience.

1.Based on "What could cause dsa.msc, the Active Directory Users and Computers snap-in, to start after 5-10 minutes?", did you mean you can open ADUC, but every 5-10 minutes, ADUC will be automatically start again?

2.Based on "It cannot be opened.", what error message did you receive when you open ADUC?

3.Does this issue appear as soon as the new domain control is promoted? Or is the domain controller able to work normally after being promoted, but this problem suddenly appeared one day?

4.Have you made any change before the issue occurs?

5.Can you open other AD tools(such as AD site and services or AD domains and trusts) on this DC?

Meanwhile, please check if any third-app/third-service caused the issue. You can perform a clean boot on this DC, then check if the issue persists.

How to perform a clean boot in Windows  

https://support.microsoft.com/en-us/topic/how-to-perform-a-clean-boot-in-windows-da2f9573-6eec-00ad-2f8a-a97a1807f3dd

Hope the information above is also helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
