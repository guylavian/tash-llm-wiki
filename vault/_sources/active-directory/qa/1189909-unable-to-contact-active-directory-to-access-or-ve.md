---
title: "Unable to contact Active Directory to access or verify claim types"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189909/unable-to-contact-active-directory-to-access-or-ve
question_id: 1189909
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Unable to contact Active Directory to access or verify claim types

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189909/unable-to-contact-active-directory-to-access-or-ve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey Guys,

In the AD domain environment. I want to update a user's "Special Permissions" for a folder on a server.

The advanced permissions are however grey. I see the error at the bottom "Unable to contact Active Directory to access or verify claim types"

I have investigated and troubleshooted the error message and noticed this error across most servers on our network (on-prem and cloud) - I have checked the DNS, Firewall etc...all working fine and couldn't spot any issues. In the end I rejoined one of the server back to the domain that solved the issue but surely I can't do this to all servers - I am pretty sure there's option, I appreciate in advance any assistance in this matter.

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-31*

Set primary DNS to your DC server.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-15*

Sounds good, might also work through this one.  

https://learn.microsoft.com/en-us/windows-server/identity/solution-guides/deploy-a-central-access-policy--demonstration-steps-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-15*

You could check  

```
Test-ComputerSecureChannel
```

and if needed 

```
Test-ComputerSecureChannel -Repair
```

- 

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
