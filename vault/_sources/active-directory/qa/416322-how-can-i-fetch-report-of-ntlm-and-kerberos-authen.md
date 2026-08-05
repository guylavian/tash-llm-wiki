---
title: "How can I fetch report of NTLM and Kerberos Authentication details in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/416322/how-can-i-fetch-report-of-ntlm-and-kerberos-authen
question_id: 416322
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How can I fetch report of NTLM and Kerberos Authentication details in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/416322/how-can-i-fetch-report-of-ntlm-and-kerberos-authen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm looking to export a report of NTLM and Kerberos Authentication success and failure  in Active Directory.  

Is there any way or via powerhsell script.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-07*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-04*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-01*

Event Description:    

This event generates every time the Key Distribution Center fails to issue a Kerberos Ticket Granting Ticket (TGT). This problem can occur when a domain controller doesn’t have a certificate installed for smart card authentication (for example, with a “Domain Controller” or “Domain Controller Authentication” template), the user’s password has expired, or the wrong password was provided.    

This event generates only on domain controllers.    

This event is not generated if “Do not require Kerberos preauthentication” option is set for the account.    

    

Event Description:    

This event generates every time that a credential validation occurs using NTLM authentication.    

This event occurs only on the computer that is authoritative for the provided credentials. For domain accounts, the domain controller is authoritative. For local accounts, the local computer is authoritative.    

It shows successful and unsuccessful credential validation attempts.    

    

reference：https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4771    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4776
