---
title: "Exchange Server 2019 Default Frontend Connector Received huge Spam request to authentication."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2169416/exchange-server-2019-default-frontend-connector-re
question_id: 2169416
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019 Default Frontend Connector Received huge Spam request to authentication.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2169416/exchange-server-2019-default-frontend-connector-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Default Frontend Connector received the Message like that "Hello [106.219.68.200 - random ip address] SIZE 37748736 PIPELINING DSN ENHANCEDSTATUSCODES AUTH NTLM LOGIN X-EXPS GSSAPI NTLM 8BITMIME BINARYMIME CHUNKING SMTPUTF8 XRDST

Is it mean that through the NTLM Protocol to authentication ? if yes, Can we block the NTLM protocol ? 

Or we can apply other setting in the server to limited the authentication type ?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-20*

Hi @IT301    

Welcome to the Microsoft Q&A platform!  

Yes, it means authentication by NTLM protocol. You can disable the NTLM protocol by means of Group Policy, which is much simpler:

1.Open the Group Policy Management Console (gpedit.msc).

2.Navigate to Computer Configuration -> Windows Settings -> Security Settings -> Local Policies -> Security Options.

3.Locate and configure Network Security: LAN Manager Authentication Level to Send NTLMv2 response to deny LM and NTLM only  

  

If you need stronger security, consider registry settings: Exchange Server support for Windows Extended Protection | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
