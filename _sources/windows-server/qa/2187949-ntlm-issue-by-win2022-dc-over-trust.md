---
title: "NTLM issue by Win2022 DC over trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187949/ntlm-issue-by-win2022-dc-over-trust
question_id: 2187949
fetched: 2026-07-25
answer_count: 17
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# NTLM issue by Win2022 DC over trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187949/ntlm-issue-by-win2022-dc-over-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,

we have two domains DomA and DomB. We have one-way trust - DomA\User1 can log on to DomB\Server1 (Linux) via NTLM.

DomA has 3 DCs (Windows Server 2019) - DomA\DC1, DomA\DC2 and DomA\DC3. DomB has 2 DCs Windows Server 2019 DomB\DC4, DomB\DC5 and a Windows Server 2022 DomB\DC6.

If DomB\Server1 is connected to DomB\DC4 or DomB\DC5, DomA\User1 can log in successfully via NTLM.

If DomB\Server1 is connected to DomB\DC6, DomA\User1 cannot log in via NTLM and we observe EventID 4625 with status 0xC000006A - user name is correct but the password is wrong.

DomB\User2 can alwas log in DomB\Server1 successfully via NTLM.

Has anyone already observed something like this? How to fix NTLM?

Best regards

Paul

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-17*

can also be seen in the logs on DomA DCs:

The computer attempted to validate the credentials for an account. 

Authentication Package:	MICROSOFT_AUTHENTICATION_PACKAGE_V1_0 

Logon Account:	DC6$ 

Source Workstation:	DC6

Error Code:	0xC0000064

But why try DC6 Win2022 log in on DC1 over trust over NTLM?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-17*

Hello,

all users from DomA can log in on all Linux-Server from DomB successfully via NTLM, if the Linux-Server from DomB are connected to DC4 or DC5 (all are Win2019!). If Linux-Server from DomB are connected to DC6 (Windows 2022!) only Users from DomB can log in via NTLM, not from DomA

Which NTLM settings need to be checked on Linux-Server and DC6? What's different by NTLM in Win 2022 and domain trust?

We have also another Domains, where Users from DomA can log in. And always if Win2022 DC try tu make NTLM Authentification over trust it goes fail.

Regards,

Paul

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-17*

Hello   

Good day!  

*If DomB\Server1 is connected to DomB\DC6, DomA\User1 cannot log in via NTLM and we observe EventID 4625 with status 0xC000006A - user name is correct but the password is wrong.*A: If you change an account (such as DomA\User2), can DomA\User2 login DomB\Server1? Or with the same error message (EventID 4625 with status 0xC000006A - user name is correct but the password is wrong.)?  

Server1 and DC6 have no problem with NTLM. Only forward NTLM from DC6 to DC1, DC2 and DC3 have a problem.  

A: Please check the NTLM configuration on DC6 and DC1 (or DC6 and DC2 or DC6 and DC3).  

Best Regards,  

Daisy Zhou  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-16*

Hello Daisy Zhou,

thank you for answer!

DomB\User2 can alwas log in DomB\Server1 successfully via NTLM. --> Server1 and DC6 have no problem with NTLM. Only forward NTLM from DC6 to DC1, DC2 and DC3 have a problem.

TLS 1.3 on DC6 is already disabled.

Regards,

Paul

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-16*

Hello paul kotov,  

Thank you for posting in Microsoft Community forum. 

 we have two domains DomA and DomB. We have one-way trust - DomA\User1 can log on to DomB\Server1 (Linux) via NTLM.  

A: I understand Domain B trusts Domain A.

If DomB\Server1 is connected to DomB\DC6, DomA\User1 cannot log in via NTLM and we observe EventID 4625 with status 0xC000006A - user name is correct but the password is wrong.

A: It seems server1 and DC6 did not negotiate the same NTLM protocol.  

You can try to check the NTLM used on server1 and DC6.

Network security LAN Manager authentication level - Windows 10 | Microsoft Learn

I hope the information above is helpful. 

If you have any question or concern, please feel free to let us know. 

Best Regards, 

Daisy Zhou
