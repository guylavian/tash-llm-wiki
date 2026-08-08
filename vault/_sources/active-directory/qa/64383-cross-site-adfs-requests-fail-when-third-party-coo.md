---
title: "Cross Site ADFS Requests fail when Third Party Cookie Disabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/64383/cross-site-adfs-requests-fail-when-third-party-coo
question_id: 64383
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Cross Site ADFS Requests fail when Third Party Cookie Disabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/64383/cross-site-adfs-requests-fail-when-third-party-coo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Chrome 83 have disabled Third Party Cookie in Incognito, and are looking to implement in the standard browser in Jan 2022. I'm looking for options around handling these requests which currently fail with Third Party Cookies disabled (In Firefox as well).  

We have a website abcd.com that redirects to adfs.xyz.com and authenticates users on ADFS 4.0 and then takes the user back to abdc.com. This works successfully, but when we request content from content.xyz.com (Cross Site) it fails at adfs.xyz.com ADFS page with an "Refused to display https://adfs.xyz.com/adfs/ls/'in a frame because it set 'X-Frame-Options' to 'deny'"  

Some of my thoughts where to do a URL Transform (rewrite) on the ADFS server and or Content Server, but I feel the requests from abcd.com to xyz.com would not be rewritten.  

Is there a way to have multiple domains in the header of ADFS?  

Or does the website need to be re-written without iFrames?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-11*

iFrames are blocked by default for authentication endpoints. It is so for security reasons.    

That said, you can modify the headers that ADFS will return (even on ADFS for Windows Server 2016 as long you have the installed KB4493473 and KB4507459). See here for documentation.    

Example:    

```
Set-AdfsResponseHeaders -SetHeaderName "X-Frame-Options" -SetHeaderValue "allow-from https://www.example.com"
```
