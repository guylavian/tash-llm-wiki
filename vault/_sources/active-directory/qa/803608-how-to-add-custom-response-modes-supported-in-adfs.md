---
title: "How to add custom \"response_modes_supported\" in ADFS 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/803608/how-to-add-custom-response-modes-supported-in-adfs
question_id: 803608
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How to add custom "response_modes_supported" in ADFS 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/803608/how-to-add-custom-response-modes-supported-in-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi MS Team,  

Is there any way to add extra "response_modes_supported" in ADFS 2019, as of now I can see only below pattern:  

"response_modes_supported":["query","fragment","form_post"]  

I want to add one of my custom response mode support something like "post_message"  

Thanks,  

Amit Kumar

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-14*

Thanks @Pierre Audonnet - MSFT   for response.     

Look like we cannot do this? lets wait for few more week and if some have any idea.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-04-12*

The `OAuthAuthorizationResponseModeConstants` class seems to have only three possible values in the `Microsoft.IdentityServer.Web.Protocols.OAuth.Messages`:  

-  query  

-  fragment  

-  form_post  

 We can see that with apps such as JustDecompile. Anyhow, I don't see a space for a customization in here. But maybe someone has more info.
