---
title: "Windows 11 24H2 refusing Kerberos for RDP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189553/windows-11-24h2-refusing-kerberos-for-rdp
question_id: 2189553
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 15
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Windows 11 24H2 refusing Kerberos for RDP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189553/windows-11-24h2-refusing-kerberos-for-rdp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have noticed a strange behaviour in Windows 11 24H2.

When connecting to a Server using RDP with the following message:

  

My User is a member of the "Protected Users" Group in Active directory, so NTLM Authentication is not possible.

We usually can work around this by connecting to the FQDN of the Server and using the UPN of the User Account, which

then will use Kerberos for Authentication.

Since installing Windows 11 24H2 this does not happen anymore. Instead it will fallback to NTLM as seen on the Domain Controllers Security Eventlog:

An account failed to log on. 

Subject: 

```
Security ID:		NULL SID 

Account Name:		- 

Account Domain:		- 

Logon ID:		0x0
```

Logon Type:			3 

Account For Which Logon Failed: 

```
Security ID:		NULL SID 

Account Name:		domadmin

Account Domain:		ad01
```

Failure Information: 

```
Failure Reason:		Unknown user name or bad password. 

Status:			0xC000006E 

Sub Status:		0xC000006E
```

Process Information: 

```
Caller Process ID:	0x0 

Caller Process Name:	-
```

Network Information: 

```
Workstation Name:	L01-NS-L-WN022

Source Network Address:	10.8.0.2 

Source Port:		0
```

Detailed Authentication Information: 

```
Logon Process:		NtLmSsp  

Authentication Package:	NTLM 

Transited Services:	- 

Package Name (NTLM only):	- 

Key Length:		0
```

Connecting from another Client with Windows 11 23H2 with the same Credentials works normally.

We were also able to replicate it with another Client that we upgraded to Windows 11 24H2.

Did anyone else also notice this behaviour?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-18*

We had the same issue and where still searching till we came up to this post.  

Thank you sir for your findings!

I really hope someone of Microsoft forwards this to the correct team for debugging in the Windows 11 24H2 release since using the UPN should be the default way as described in many articles.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-12*

Hi, 

Thanks for your reply and sharing. 

I'm glad your problem has been solved.

Best regards

Yanhong Liu

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-09*

Hello, 

Thank you for posting in the Microsoft Community Forums. 

Windows 11 24H2 does not support NTLMv1, and it enforces the use of NTLMv2 or Kerberos for authentication.  

For RDP connections, if the user is a member of the "Protected Users" group, NTLM authentication is not possible, and Kerberos should be used. However, if Kerberos pre-authentication fails, it could be due to issues with the encryption type or configuration settings. Ensure that the registry key for the default pre-authentication encryption type is set correctly, and consider using AES instead of RC4. 

I hope the information above is helpful. 

Best regards 

Yanhong Liu
