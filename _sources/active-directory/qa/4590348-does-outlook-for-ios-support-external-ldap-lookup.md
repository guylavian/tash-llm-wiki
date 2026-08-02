---
title: "Does Outlook for iOS support external LDAP lookup for S/MIME?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4590348/does-outlook-for-ios-support-external-ldap-lookup
question_id: 4590348
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 4
qa_tags: []
---
# Does Outlook for iOS support external LDAP lookup for S/MIME?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4590348/does-outlook-for-ios-support-external-ldap-lookup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Does Outlook for iOS support the ability to search an external LDAP address book for S/MIME public keys or must all the public keys reside in the O365 GAL? The documentation seems to be contradictory. 

Under the "LDAP support for certificate lookup" section, it states the following: 

When Outlook for iOS and Android performs a certificate lookup for a recipient, the app will search the local device first, then query Azure Active Directory, and then evaluate any LDAP directory endpoint. When Outlook for iOS and Android connects to the LDAP directory endpoint to search for a recipient's public certificate, certificate validation is performed to ensure that the certificate is not revoked. The certificate is only considered valid by the app if certificate validation completes successfully.

Yet under the "Create S/MIME messages" section, it states:

Outlook for iOS and Android will evaluate all recipients prior to sending an encrypted message and confirm that a valid public certificate key exists for each recipient. The Global Address List (GAL) is checked first; if a certificate for the recipient does not exist in the GAL, Outlook queries the Microsoft publisher keychain in iOS or the system KeyStore in Android to locate the recipient's public certificate key. For recipients without a public certificate key (or an invalid key), Outlook will prompt for their removal. The message will not be sent without encryption to any recipient unless the encryption option is disabled by the sender during composition.

I have been told by our other admins that they've tried setting LDAP address in the Intune policy, but it did not allow them to send encrypted email to recipients in the LDAP directory.  Only when they published the contact and corresponding certificates in AD/AAD did it allow them to send encrypted email.  So, I'm curious as to what purpose the LDAP setting in Outlook for iOS serves if it cannot be used as an external repository by the client to search for public keys?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-12*

Dear jdbst56,

Good day to you and thanks for reaching out to Microsoft Community.

According to your description, we have a general understanding of your query. After searching and consulting, in this case, you may need to get in touch with our dedicated team. We understand that you have concern about LDAP services with Outlook for iOS, as Microsoft has specific community channel resources where our related most valuable professional can provide possible information for those highly technical systems, would you mind connecting and place your concern on our specific dedicated Microsoft Q&A forum community channel to get further support from our related community members? Technical services engineers over there will assist with resolving any issues or conflicts for those highly technical systems from their side. Because since we are mainly focusing Outlook client side related certain scenario on this forum community channel.

Here is URL link to place your concern: Microsoft Q&A forum channel.

I am really appreciating your kind cooperation. Thank you again for your precious time.

Sincerely,

Tammy | Microsoft Community Moderator.
