---
title: "ADFS Authentication Issue in .Net 8"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1662585/adfs-authentication-issue-in-net-8
question_id: 1662585
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-aspnet-core-other-l1", "developer-technologies-dotnet-other-l1", "microsoft-security-security-active-directory-federation-services"]
---
# ADFS Authentication Issue in .Net 8

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1662585/adfs-authentication-issue-in-net-8 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an existing ASP.NET MVC application that relies on ADFS authentication. I'm currently upgrading it to .NET 8. As part of the upgrade process, I prioritized implementing the authentication functionality first. However, I'm encountering an issue where the `IsAuthenticated` property consistently returns `false`.

`builder.Services.AddAuthentication(sharedOptions =>`

`    {`

`        sharedOptions.DefaultScheme = CookieAuthenticationDefaults.AuthenticationScheme;`

`        sharedOptions.DefaultChallengeScheme = WsFederationDefaults.AuthenticationScheme;`

`    })`

`    .AddCookie()`

`    .AddWsFederation(options =>`

`    {`

`        options.MetadataAddress = "https://example.com/FederationMetadata/2007-06/FederationMetadata.xml"; // Replace with your metadata URL`

`        options.Wtrealm = "urn:DevDotNet"; // Replace with your URN`

`        options.Wreply = "https://xyz.com/Home/Index";`

`}`

Can you please help to identify the issue?

## Answers

_No answers on this thread._
