---
title: "Active Directory Cross-forest authentication & EventID 4776 \"The specified account does not exist\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1662295/active-directory-cross-forest-authentication-event
question_id: 1662295
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Cross-forest authentication & EventID 4776 "The specified account does not exist"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1662295/active-directory-cross-forest-authentication-event (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Let's say we have forestA and forestB. There is 2-way transitive trust between these forests.

A service tries to authenticate a user residing in forestB against a DC in forestA. This results in an authentication failure: EventID 4776 "The specified account does not exist" on the DC in forestA and (at the same time) a successful authentication on the DC in forestB. The service is successfully authenticated. 

Is this normal behavior? The end result is a lot of unnecessary failed authentication events on the DC in forestA.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-02*

Hello Tim-1789,  

Thank you for posting in Q&A forum.

authentication failure: EventID 4776 "The specified account does not exist" on the DC in forestA

A1: Event ID 4776 means NTLM authentication. This event generates every time that a credential validation occurs using NTLM authentication.

*  

(at the same time) a successful authentication on the DC in forestB. The service is successfully authenticated.*  

A2: Please check if the related successful event ID is 4771 (Kerberos authentication).

A service tries to authenticate a user residing in forestB against a DC in forestA

A3: I understand only Domain Controller in Forest B can authenticate the account in forest B.

4771(F): Kerberos pre-authentication failed.

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4771

4776(S, F): The computer attempted to validate the credentials for an account.

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4776

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
