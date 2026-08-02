---
title: "ADFS 2019 multiple mfa provider selection on RP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/18531/adfs-2019-multiple-mfa-provider-selection-on-rp
question_id: 18531
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 2019 multiple mfa provider selection on RP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/18531/adfs-2019-multiple-mfa-provider-selection-on-rp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Microsoft community    

Would we be able with ADFS 2019 to select in claim rules (at relying party level) the preferred MFA if you have multiple providers registered.    

Is this really possible and how ?    

The idea would be to use a claim rule like this    

Set-AdfsRelyingPartyTrust -TargetName test –AdditionalAuthenticationRules 'exists([Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid", Value == "S-1-5-21-2462332226-1795882094-2017209951-xxxxx"]) =>issue(Type = "http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod", Value = "http://schemas.microsoft.com/claims/multipleauthn") && (Type = "http://schemas.microsoft.com/claims/authnmethodsproviders", Value = "mfaprovider");    

here we would select the mfa provider based on a group    

I also understood this was stated here     

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/overview/whats-new-active-directory-federation-services-windows-server    

in "Specify auth method for additional auth per RP" section    

Any input would be appreciated, thx

## Answers

_No answers on this thread._
