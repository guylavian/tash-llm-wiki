---
title: "SSO support for edge (chromium based) with ADFS 3.0"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/100097/sso-support-for-edge-chromium-based-with-adfs-3-0
question_id: 100097
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# SSO support for edge (chromium based) with ADFS 3.0

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/100097/sso-support-for-edge-chromium-based-with-adfs-3-0 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We have upgrade ADFS FBL from 1.0 to 3.0. Still SSO with edge (chromium based) is not working if we do not add the specific version. Below is the current status  

Set-AdfsProperties -WIASupportedUserAgents @("MSAuthHost/1.0/In-Domain","MSIE 6.0", "MSIE 7.0; Windows NT", "MSIE 8.0", "MSIE 9.0", "MSIE 10.0; Windows NT 6","Windows NT 6.3; Trident/7.0", "Windows NT 6.3; Win64; x64; Trident/7.0", "Windows NT 6.3; WOW64; Trident/7.0", "Windows NT 6.2; Trident/7.0", "Windows NT 6.2; Win64; x64; Trident/7.0", "Windows NT 6.2; WOW64; Trident/7.0", "Windows NT 6.1; Trident/7.0", "Windows NT 6.1; Win64; x64; Trident/7.0", "Windows NT 6.1; WOW64; Trident/7.0", "MSIPC", "Windows Rights Management Client", “Trident/7.0”,"=~Windows\s*NT.Edge","Edg/","Edg/85.0.564.51")  

Is there a fix to work SSO with all Edge versions?  

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-06*

So you just changed the part   

=~Windows\s*NT.Edge  

to  

=~Windows\s*NT.*Edg  

Or am I missing another change?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-04*

SSO with IE & Edge (Chromium based) works with below settings  

MSAuthHost/1.0/In-Domain  

MSIE 6.0  

MSIE 7.0; Windows NT  

MSIE 8.0  

MSIE 9.0  

MSIE 10.0; Windows NT 6  

Windows NT 6.3; Trident/7.0  

Windows NT 6.3; Win64; x64; Trident/7.0  

Windows NT 6.3; WOW64; Trident/7.0  

Windows NT 6.2; Trident/7.0  

Windows NT 6.2; Win64; x64; Trident/7.0  

Windows NT 6.2; WOW64; Trident/7.0  

Windows NT 6.1; Trident/7.0  

Windows NT 6.1; Win64; x64; Trident/7.0  

Windows NT 6.1; WOW64; Trident/7.0  

MSIPC  

Windows Rights Management Client  

Trident/7.0  

=~Windows\s*NT.*Edg
