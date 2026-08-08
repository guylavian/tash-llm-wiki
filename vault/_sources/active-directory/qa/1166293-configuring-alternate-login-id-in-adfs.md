---
title: "Configuring Alternate Login ID in ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166293/configuring-alternate-login-id-in-adfs
question_id: 1166293
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Configuring Alternate Login ID in ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166293/configuring-alternate-login-id-in-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

I am trying to configure alternate login on my ADFS.

I have a forest with 3 domains: domain.es, domain.com and domain.net. The domain "domain.com" is public, where the user of domain.es or domain.net logs into any application integrated with the ADFS of domain.com. The domain trust relationships, name resolutions, everything is correct and the ADFS works correctly.

When executing the following command in the ADFS of the domain "domain.com" I get an error:

```
PS C:\Users\Administrator> Set-AdfsClaimsProviderTrust -TargetIdentifier "AD AUTHORITY" -AlternateLoginID mail -LookupFo
rests domain.es
Set-AdfsClaimsProviderTrust : Exception of type
'Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapServerUnavailableException' was thrown.
At line:1 char:1
+ Set-AdfsClaimsProviderTrust -TargetIdentifier "AD AUTHORITY" -AlternateLoginID m ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (Microsoft.Ident...msProviderTrust:ClaimsProviderTrust) [Set-AdfsClaimsPro
   viderTrust], LdapServerUnavailableException
    + FullyQualifiedErrorId : Exception of type 'Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.Ldap
   ServerUnavailableException' was thrown.,Microsoft.IdentityServer.Management.Commands.SetClaimsProviderTrustCommand
```

however, when I run the same thing for the domain "domain.net", it runs correctly:

```
PS C:\Users\Administrator> Set-AdfsClaimsProviderTrust -TargetIdentifier "AD AUTHORITY" -AlternateLoginID mail -LookupFo
rests domain.net
PS C:\Users\Administrator>
```

Can anyone help me with this error?

Thank you very much,

Regards.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-07*

When configured for alternate ID, AD FS allows users to sign in using the configured alternate ID value, such as email ID. Using the alternate ID enables you to adopt SaaS providers like Office 365 without modifying your on-premises UPNs. It also enables you to support line-of-business service applications with consumer-provisioned identities.

Check this MS guide for more help - https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configuring-alternate-login-id
