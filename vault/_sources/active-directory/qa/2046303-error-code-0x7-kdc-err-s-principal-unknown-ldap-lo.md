---
title: "Error Code: 0x7  KDC_ERR_S_PRINCIPAL_UNKNOWN LDAP/Localhost"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2046303/error-code-0x7-kdc-err-s-principal-unknown-ldap-lo
question_id: 2046303
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error Code: 0x7  KDC_ERR_S_PRINCIPAL_UNKNOWN LDAP/Localhost

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2046303/error-code-0x7-kdc-err-s-principal-unknown-ldap-lo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

"In the event log, an entry like this appears every 5 minutes. How do I fix it?"

A Kerberos error message was received:

 on logon session 

 Client Time: 

 Server Time: 13:55:10.0000 9/10/2024 Z

 Error Code: 0x7  KDC_ERR_S_PRINCIPAL_UNKNOWN

 Extended Error: 

 Client Realm: 

 Client Name: 

 Server Realm: Contoso.com

 Server Name: LDAP/localhost

 Target Name: LDAP/****@Contoso.com**

 Error Text: 

 File: onecore\ds\security\protocols\kerberos\client2\kerbtick.cxx

 Line: 1286

 Error Data is in record data.

By entering this, I received another error message:

setspn -A LDAP/localhost Contoso.com\administrator."

A Kerberos error message was received:

 on logon session 

 Client Time: 

 Server Time: 13:45:10.0000 9/10/2024 Z

 Error Code: 0x29 KRB_AP_ERR_MODIFIED

 Extended Error: 

 Client Realm: 

 Client Name: 

 Server Realm: Contoso.com

 Server Name: dc01$

 Target Name: 

 Error Text: 

 File: onecore\ds\security\protocols\kerberos\client2\ctxtapi.cxx

 Line: 5a1

 Error Data is in record data.

"So this is not the solution, but what should I enter to make it work?"

"Of course, I replaced the domain name with contoso.com."

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-10*

Hello,

Thank you for posting in Q&A forum.

KDC_ERR_C_PRINCIPAL_UNKNOWN means the domain controller does not know which client principal it should use to encrypt the ticket.To resolve this, determine if the requestor has the correct UPN.

For more details, I suggest you refer to the following link：

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/kerberos-errors-in-network-captures/ba-p/400066

I hope the information above is helpful.

Best regards

Zunhui

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
