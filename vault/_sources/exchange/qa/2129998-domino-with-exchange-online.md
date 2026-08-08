---
title: "Domino with Exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2129998/domino-with-exchange-online
question_id: 2129998
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domino with Exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2129998/domino-with-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are using domino server in our hq. but our sub is using m365. 

To support encryption email between domino & M365, we are thinking about email with S/MIME.

Can M365 sync those info to onPrem LDAP server? Then our Domino server connect that onPrem LDAP server for those S/MIME info. Then our end user send encrypted email to M365 users.

Many Thanks.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-16*

Hi, @Jacky Lai

Yes, using S/MIME to encrypt e-mail communication between the Domino server and M365 is a viable approach. This involves the following steps:

-  Make sure that both your Domino and M365 users have a valid S/MIME certificate from a trusted certificate authority.

-  In M365, you need to publish the S/MIME certificate to a user profile in Azure Active Directory. Configure M365 to send and receive encrypted and signed email using S/MIME.

-  Use Azure AD Connect or a similar tool to synchronize the appropriate user attributes, including S/MIME certificates, from Azure Active Directory to the local Active Directory (AD). Ensure that the attributes used to map the S/MIME certificates stored in Azure AD to the correct attributes in the local AD.

-  Configure your Domino server to query your local LDAP server for S/MIME certificates. Ensure that your Domino server can access and use the S/MIME certificate from the LDAP server to encrypt and decrypt e-mail.

More information can be found Configure S/MIME in Exchange Online | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
