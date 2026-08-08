---
title: "ADFS  Non-Claims-Aware Relaying Party Trust cannot logout"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/24067/adfs-non-claims-aware-relaying-party-trust-cannot
question_id: 24067
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS  Non-Claims-Aware Relaying Party Trust cannot logout

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/24067/adfs-non-claims-aware-relaying-party-trust-cannot (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I set for my non-claims-aware Party Trust the logout url to adfs/ls/?wa=wsignout1.0. But if I close the Browser and open the application Url it automatically logins cause the EdgeAccessCookie is still existing.  

How can I fix my logout.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-11-04*

I searched myself crazy to find a solution for this problem. And there is a simple infrastructural solution I want to share with you.  

When you publish the non-claims-aware application on WAP you need to enable for that published application on WAP the setting: EnableSignout  

Example: The name of your published application is TEST. On the WAP server run the command:  

Get-WebApplicationProxyApplication TEST | Format List  

There you get some hidden settings that you can't find in the WAP GUI. Default the 'EnableSignOut' setting is "False"  

In the result you need to copy the ID of the published application. (Example ID for TEST = b20e2sq4-01ce-e674-5fe7-0709a1e94d63)  

Run the command to enable the signout option:  

Set-WebApplicationProxyApplication -ID b20e2sq4-01ce-e674-5fe7-0709a1e94d63 -EnableSignout  

To cleanup the EdgeAccessCookie (after log on) for the application, use the URL:  

https://<FQDN relying Party>/?wa=wsignoutcleanup1.0&wreply=https://<FQDN WAP>/adfs/ls/?wa-wsignout1.0
