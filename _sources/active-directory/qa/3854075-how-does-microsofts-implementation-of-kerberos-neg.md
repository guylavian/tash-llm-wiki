---
title: "How does Microsoft's implementation of Kerberos negotiate the encryption type for service tickets?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3854075/how-does-microsofts-implementation-of-kerberos-neg
question_id: 3854075
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# How does Microsoft's implementation of Kerberos negotiate the encryption type for service tickets?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3854075/how-does-microsofts-implementation-of-kerberos-neg (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hoping not to break any service accounts for one of my clients 😅.

If I change an SPN service account's supported encryption types to both RC4 and AES (previously set to RC4 only), will that cause the KDC and service account to negotiate AES for the service ticket encryption type, even if the server hosting the service doesn't support AES (e.g., Windows Server 2003)?

I ask this because this Microsoft article states "When a service ticket is requested, the domain controller will select the ticket encryption type based on the msDS-SupportedEncryptionTypes attribute of the account associated with the requested SPN".

If that's the case, then couldn't the negotiated encryption type theoretically be one that isn't supported by the server hosting the service since it sounds like the service's server isn't involved in the encryption type negotiation?

## Answer (community) — community member

*upvotes: 0 · updated: 2025-05-07*

Hello,

Thanks for posting to Microsoft Community!

I appreciate your detailed question about Kerberos encryption negotiation in Microsoft's implementation. In Windows environments, when a service ticket is requested, the domain controller selects the ticket encryption type based on the msDS-SupportedEncryptionTypes attribute of the account associated with the requested SPN. If you change an SPN service account's supported encryption types to both RC4 and AES, the KDC will negotiate the encryption type based on the available options.

However, it's important to note that the negotiated encryption type could potentially be one that isn't supported by the server hosting the service. In such cases, it may lead to authentication failures or issues accessing the service. It's recommended to ensure that the encryption types supported by the service account align with the capabilities of the servers hosting the services to avoid any disruptions.

If you have specific concerns about compatibility with Windows Server 2003 or any other server versions, it's advisable to thoroughly test the changes in a controlled environment before implementing them in a production setting to prevent any service disruptions.

When everything is resolved, feel free to mark this thread as answer and helpful. Otherwise, please let me know if there's anything else I can help you with.

Best Regards,
Van Johnson | Microsoft Community Moderator
