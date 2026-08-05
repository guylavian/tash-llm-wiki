---
title: "G-Suite ADFS, on-prem AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155240/g-suite-adfs-on-prem-ad
question_id: 155240
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# G-Suite ADFS, on-prem AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155240/g-suite-adfs-on-prem-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have setup ADFS with G-Suite and it works. However, when logging in to G-Suite I have to enter my username, which detects the domain is federated so redirects me to my ADFS login page, but the username field is not pre-populated with the username I just entered in G-Suite login.  

This is really annoying and probably worse than having a separate domain/username/password in G-Suite.  

How do I fix this? And where do I fix this? In G-Suite or ADFS?  

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-08*

It's rather a question for the Google support :)  

When the Google redirects you to ADFS it could use a query string (such as login_hint) to pass the username you already typed. Then ADFS will pre-filled the username field.  

Do you see anything in the URL redirection that can be used? Even if it is not the default query string, we could use JavaScript to grab it.
