---
title: "ADFS AD User Schema attribute mapping error? PolicyEvaluationException: POLICY0019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1276304/adfs-ad-user-schema-attribute-mapping-error-policy
question_id: 1276304
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS AD User Schema attribute mapping error? PolicyEvaluationException: POLICY0019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1276304/adfs-ad-user-schema-attribute-mapping-error-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,

I've deployed ADFS with success in a test environement. Now implementing the same configuration in a production environenment I get a attribute mapping error or something like that:

Microsoft.IdentityServer.RequestFailedException: MSIS7012: An error occurred while processing the request. Contact your administrator for details. ---> Microsoft.IdentityServer.ClaimsPolicy.Language.PolicyEvaluationException: POLICY0019: Query ';mail,tokenGroups(fullDomainQualifiedName);{0}' to attribute store 'Active Directory' returned an unexpected number of fields: expected '3', got '2'.

The ADFS configuration related to this issue :

```
"http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress",
"http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn",
"http://schemas.microsoft.com/ws/2008/06/identity/claims/role"), query = ";mail,tokenGroups(fullDomainQualifiedName);{0}", param = c.Value);
```

Does someone have a clue on what is wrong in this production AD? May be the User Schema that's not the "default" one?

Thank you all and best regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-09*

Hi,

this page might help debug claims :

https://adfshelp.microsoft.com/ClaimsXray/TokenRequest

Best,

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-05*

I indeed read this thread but did not understand it.

Could you recommend me a tool to make querys to the AD so I can find out what is returned in each environment. Any debbuging tool available?

Many thanks and best regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-05*

Check this similar thread for help - https://social.msdn.microsoft.com/Forums/en-US/8bcd276a-26b7-454e-8b9f-0c1d5245a25e/custom-attribute-store-multiple-claims?forum=Geneva
