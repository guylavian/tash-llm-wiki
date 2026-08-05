---
title: "Unable to change the ADFS authentication policies rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/603438/unable-to-change-the-adfs-authentication-policies
question_id: 603438
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Unable to change the ADFS authentication policies rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/603438/unable-to-change-the-adfs-authentication-policies (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Unable to execute the Microsoft PowerShell which is presented in Microsoft Learn (refer below). However, I am getting error while executing. Request to execute this script in ADFS environment and provide the alternative which will change the group name per relying party trust    

$MfaClaimRule = "c:[Type == '"https://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid'", Value =~ '"^(?i) <group_SID>$'"] => issue(Type = '"https://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod'", Value '"https://schemas.microsoft.com/claims/multipleauthn'");"    

Set-AdfsRelyingPartyTrust –TargetRelyingParty $rp –AdditionalAuthenticationRules $MfaClaimRule

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-04*

Assuming you are using ADFS on Windows Server 2016, you should not use this command but use Access Policies instead.    

The scenario you are looking for is available in the built-in templates: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/access-control-policies-in-ad-fs
