---
title: "LDAP operation logging for Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1427642/ldap-operation-logging-for-active-directory
question_id: 1427642
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# LDAP operation logging for Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1427642/ldap-operation-logging-for-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there any mechanism to log all LDAP operation details for Active Directory on the domain controllers (preferably in one place)?  I know you can turn on diagnostic logging for queries, but I want to see things like modify operations and what attributes are being modified along with the return codes back to the clients as well as bind calls with the actual DN string being sent by the client.  AD Insight (the SysInternals tool) did some of that, but it was meant to be run at the client end, not the domain controller.  I've tried turning on various options in the NTDS Diagnostics registry key, but I don't get anything that seems useful.  Google searches haven't turned up much other than the query logging.  Even if it's a third party tool, I'm just looking for anything that can give me the data.  I'd use Wireshark, but it can be hard to grab the data on a busy server and there's no way to use it when the client is using LDAPS with an encryption cipher that can't be decrypted with the private key alone.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-17*

On domain controllers, several techniques exist to log all LDAP activity information for Active Directory. Here are several possibilities:

-  Enable LDAP auditing

-  Use a third-party tool

-  Use Wireshark

-  Use a dedicated LDAP capture tool

-  Use a SIEM (Security Information and Event Management) tool

Let me know if you have any queries.
