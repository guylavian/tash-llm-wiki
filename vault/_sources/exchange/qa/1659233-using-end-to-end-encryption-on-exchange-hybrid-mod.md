---
title: "Using End to end Encryption on Exchange Hybrid mode."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1659233/using-end-to-end-encryption-on-exchange-hybrid-mod
question_id: 1659233
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Using End to end Encryption on Exchange Hybrid mode.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1659233/using-end-to-end-encryption-on-exchange-hybrid-mod (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,

I just create a rule on exchange online to encrypt any sending email (working fine as testing), we have hybrid configuration on our environment, the weird thing  when I send email from O365 email to any on premise email it shown as external 

can anyone help me with this?

Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-23*

Hi @Waleed Waleed,

To help you better, I want to confirm that if all that emails from O365 send to on-premises shown as external. If no, this issue may be related to this rule. If yes, you can do the following to check:

-  You can use EAC navigate to Mail flow > Accepted domains, check hybrid routing domain (tenant.mail.onmicrosoft.com), this domain should be configured as “Internal Relay” as opposed to “Authoritative”. 

-  Use the following command to check the value of the send connector you use to send to on-premises from O365:   Get-SendConnector "XXXX" | Format-List.    Make sure the CloudServicesMailEnabled set to true.

-  If needed, you can re-run Hybrid Configuration wizard to see if messages from O365 can be treated as internal messages.

If you have any questions, please feel free to contact me.
