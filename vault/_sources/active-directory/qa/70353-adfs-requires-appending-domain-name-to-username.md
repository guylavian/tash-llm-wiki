---
title: "ADFS requires appending domain name to username"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/70353/adfs-requires-appending-domain-name-to-username
question_id: 70353
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS requires appending domain name to username

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/70353/adfs-requires-appending-domain-name-to-username (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently the way our ADFS 4.0 on Windows 2019 datacenter is set up, users need to add @keyman  .company.com to their username to be able to log in successfully.    

We added (what I feel is a bandaid solution) a JavaScript that appends that qualifier so that user does not have to do this.    

We have only one domain.     

-  Is there any way we can configure ADFS to eliminate the need for doing this?    

-  If it is not possible, how can we configure the JavaScript to add the @keyman   qualifier on the password expired page as well?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-19*

User can either type their username in the DOMAIN\Samaccountname format or the UPN format (the username@dnsdomainname). Or like Mark suggested, you can configure a custom attribute (although that custom attribute also need a something@something   format).    

The official way to have the user typing only one part is to go the JavaScript way. It's probably what you've done and it is described here. For the password update page, you can do the same thing. There is an example here.    

You can also achieve SSO without having to prompt the user for anything. Like using certificates. Or if you are using ADFS for Azure AD integration (to use Office 365 for example), you can have SSO thanks to having a PRT on an AAD Joined Windows 10 or Hybrid AAD Joined Windows 10. Then you won't see a form. But if you are using ADFS for Azure AD, maybe you should reconsider using ADFS all together and use Azure AD Connect Seamless Sign-On instead.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-18*

You could try alternate login Id.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configuring-alternate-login-id
