---
title: "Decryption S/MIME E-Mails on Office 365 with OWA gives me an error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1116563/decryption-s-mime-e-mails-on-office-365-with-owa-g
question_id: 1116563
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Decryption S/MIME E-Mails on Office 365 with OWA gives me an error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1116563/decryption-s-mime-e-mails-on-office-365-with-owa-g (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!    

I'm trying to setup reading / writing S/MIME encrypted e-mails at a customer who requires signed mails for certain workflows.    

They have Office 365 with Exchange on the web, and I try to setup S/MIME with a physical PKI card in Edge.    

I have installed all the necessary widgets and extensions in Edge, and I can successfully write mails.    

When I try to read an encrypted mail, though, regardless if it is from me or from someone else, in the popup window the following error message appears:    

The S/MIME message wasn't decrypted successfully. The ASN.1 package couldn't be opened.    

I can reproduce it on our Windows 10 clients. It works on Windows 11. Unfortunately, for use at the customer only Windows 10 is approved, so switching is not a possibility. This is Windows 10 Pro with all the latest updates installed.    

The same message btw. appears when I install the extension in Chrome, so it doesn't seem to be an Edge issue, more an issue with the app or the extension.    

There are several people here on Technet who had the same problem in 2019, but with no solution.    

What can we do here to make it working?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-06*

Check this similar thread - https://answers.microsoft.com/en-us/outlook_com/forum/all/smime-not-working-asn1-package/2af28f38-476c-49cb-a8f6-a7c4198ca7e8
