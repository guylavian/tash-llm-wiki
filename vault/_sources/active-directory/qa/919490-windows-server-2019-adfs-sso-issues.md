---
title: "Windows Server 2019 ADFS SSO issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/919490/windows-server-2019-adfs-sso-issues
question_id: 919490
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Windows Server 2019 ADFS SSO issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/919490/windows-server-2019-adfs-sso-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We try to access SSO moodle with miniOrange plugin via ADFS Server 2019. I think there is the issue with ADFS server configuration, because:    

-  If I login to moodle with Firefox (46 version) SSO works fine. (https://help.hcltechsw.com/domino/10.0.1/secu_enabling_iwa_in_firefox.html)    

-  If I login with Chrome (92 version) ADFS prompt for credential and if I entered it login successful. But SSO no working. Try add Chrome GPO called 'authentication server whitelisting' with ADFS server name, no result. Also try the same with Edge GPO.    

-  If I login wth Edge (version 101) then ADFS prompt for login then enter the credential and it re-prompted for credential, and it become the infinity cycle.    

-  If I try login with IE11, then prompt for credential enter it and get HTTP 400 Bad request.    

WIASupportedUserAgents added mozilla/5.0. Also try add „Chrome“ but no work.     

Set-ADFSProperties –ExtendedProtectionTokenCheck try to „none“ and „allow“    

I think if SSO work with Firefox, then miniorange plugin configuration is correct and the problem is with ADFS?     

Also SPN is correct HTTP://<federationservice domain> on one Federation service account    

Also set Set-AdfsProperties -EnableIdpInitiatedSignonPage $true    

Can you advise where to troubleshoot problem? Can it be workstation or server GPO? I need SSO login for MS Egde.

## Answers

_No answers on this thread._
