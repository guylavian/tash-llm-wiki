---
title: "ADFS 2016 ESL lockout"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/728994/adfs-2016-esl-lockout
question_id: 728994
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 2016 ESL lockout

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/728994/adfs-2016-esl-lockout (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello   

I am running ADFS 2016, in a two node farm. If a user is coming from a familiar ip, but the failed authentication attempts go past the value set on "Extranet Lockout Threshold" , will this lock the user account out at ADFS ? My assumption is that the account will not get locked out because the source ip is from a familiar location

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-14*

The smart lockout feature (not the default setting, so make sure you check the current configuration with `Get-ADFSProperties` (and make the adjustment if necessary https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ad-fs-extranet-smart-lockout-protection) is essentially managing two counters. One for familiar IPs (IPs from which we saw succesfull logons in the past) and another for unfamilliar IPs (IPs from which we never saw any succesfull logon in the past).     

When a user failed to logon from a unfamilliar IP address, then it increases the counter for unfamilliar IPs.    

If a user is faling to authenticate from a familliar IP address, then it increases the counter for familliar IPs.    

The account can be locked in both situation. The idea of that feature is that the failed logon due to password based attacks (such as password spray or brute force from attackers and botnet) will not lock out the user (unless the user is conencting from a machine which is a part of a botnet attacking your AD FS farm... but eh, that's kind of a corner case).
