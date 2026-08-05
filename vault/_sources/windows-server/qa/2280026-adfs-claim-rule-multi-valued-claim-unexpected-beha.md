---
title: "ADFS Claim Rule: Multi-valued Claim Unexpected Behavior UPN (Web API + Application Group) — Possible Bug"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2280026/adfs-claim-rule-multi-valued-claim-unexpected-beha
question_id: 2280026
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# ADFS Claim Rule: Multi-valued Claim Unexpected Behavior UPN (Web API + Application Group) — Possible Bug

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2280026/adfs-claim-rule-multi-valued-claim-unexpected-beha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I’m seeing a very odd behavior in ADFS Claim Issuance, and after a lot of testing I suspect this could be a bug in the way ADFS merges claims across Web API Applications and Application Groups.

✅ Environment

-  ADFS Version: (example: ADFS 2019 / ADFS 2022)

ADFS Role: Active Directory Federation Services (on-premises)

Application Type: Web API + Server Application inside same Application Group

Client: APEX app using OIDC flow

🎯 Scenario

I’m trying to issue a single-valued claim extracted from UPN, to provide the username in the JWT token.

My rule is:

```
@RuleName = "ExtractUsername" c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"]  => issue(Type = "sacousername", Value = regexreplace(c.Value, "@.*$", ""));
```

🔍 Observed behavior

Despite having only ONE rule issuing ExtractUsername, the resulting JWT always contains:

```
sacousername
```

An array of two values:

1️⃣ The original casing (ex: `"usernameUPPERCASE"`) 2️⃣ The lowercased version (ex: `"usernameLOWERCASE"`)

✅ Tests performed

1️⃣ Checked Web API Application `IssuanceTransformRules`: → Only ONE rule emits ExtractUsername.

2️⃣ Checked Application Group:

Server application → no IssuanceTransformRules.

Web API → same rule as above.

3️⃣ Checked ClaimsProviderTrust → No ClaimRules emitting ExtractUsername.

4️⃣ Checked AdditionalClientClaims and `RequestedClaims` → Nothing defined.

🚩 Still the token contains ExtractUsername as array.

🧐 Conclusion

I suspect this is a known bug / design issue:

ADFS merges claims from multiple sources (Web API App + Application Group + ClaimsProvider).

If at any point in the past, a claim was emitted as multi-valued, ADFS caches that behavior.

-  Even after cleanup, it keeps issuing the claim as an array.

-  I completely removed the `ExtractUsername` rule from the Web API Application, issued a new token, and the claim still appears in the token as an array — even though there is no active rule emitting it.

🎯 Question

Is this a known issue in ADFS?

Is there an official workaround or hotfix?

Is this addressed in newer versions?

Thanks in advance! Any insights would be greatly appreciated.

🚀 Tags to add

✅ `adfs` ✅ `adfs-claims` ✅ `adfs-2019` or `adfs-2022` ✅ `openid-connect` ✅ `jwt`

## Answers

_No answers on this thread._
