---
title: "Azure MFA with Exchange Server On-Premises"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/352695/azure-mfa-with-exchange-server-on-premises
question_id: 352695
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Azure MFA with Exchange Server On-Premises

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/352695/azure-mfa-with-exchange-server-on-premises (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings All,  

I have Exchange On-Premises, and I am planning to introduce ActiveSync to allow mobile users access to their mailboxes (emails, calendar, etc..).  

To Secure ActiveSync, it is recommended by Microsoft to enable MFA, where I have Azure E3 Subscription that includes MFA. my question is, does this subscription's MFA support my setup? or I need other solutions?  

Thanking you  

Jamils

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

Hi @Joyce Shen - MSFT      

Thank you very much for your reply.    

But, there is some confusion, at least for me, when I got theses two Microsoft articles about the subject:    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/configure-exchange-server-for-hybrid-modern-authentication?view=o365-worldwide    

https://learn.microsoft.com/en-us/Exchange/clients/outlook-for-ios-and-android/use-hybrid-modern-auth?view=exchserver-2019    

any clarifications on that?    

Thanking you    

Jamils

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

Hi @Jamil Saif      

Please refer to the discussion in below thread about MFA for on-premise Exchange activesync    

Exchange Server 2016 On-Premise and 2FA/MFA    

Exchange ActiveSync with Azure AD Application Proxy    

For more information about Tutorial: Secure user sign-in events with Azure AD Multi-Factor Authentication    

I also see a workaround using Activesync Device Quarantine. All new ActiveSync devices go into a quarantined state until approved by IT. The IT department has to get confirmation from the user that they added the device, and if they had an old device, what was done with it to properly wipe the email off.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
