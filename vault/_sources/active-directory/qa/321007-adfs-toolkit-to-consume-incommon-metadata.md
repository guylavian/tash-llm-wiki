---
title: "ADFS Toolkit to consume incommon metadata"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/321007/adfs-toolkit-to-consume-incommon-metadata
question_id: 321007
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Toolkit to consume incommon metadata

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/321007/adfs-toolkit-to-consume-incommon-metadata (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there any document on how to pull InCommon metadata in ADFS? Has anyone used adfs toolkit or any other 3rd party tool to consume incommon metadata?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-05*

Have you tried     

```
Add-AdfsClaimsProviderTrustsGroup -MetadataUrl https:///InCommon-metadata.xml
```

Ref: https://learn.microsoft.com/en-us/powershell/module/adfs/add-adfsclaimsprovidertrustsgroup?view=windowsserver2019-ps
