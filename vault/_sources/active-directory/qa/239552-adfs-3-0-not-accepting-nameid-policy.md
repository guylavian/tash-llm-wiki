---
title: "ADFS 3.0 not accepting NameID Policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/239552/adfs-3-0-not-accepting-nameid-policy
question_id: 239552
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 3.0 not accepting NameID Policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/239552/adfs-3-0-not-accepting-nameid-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in the process of configuring SAML 2.0 federation to an ADFS 3.0 (Windows Server 2012 R2) instance, and wanting to set the NameID Policy to "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress" for the Relying Party Trust.  

This works perfectly fine on another ADFS 3.0 instance by configuring two custom claim policies:  

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", 
Issuer == "AD AUTHORITY"] => issue(store = "Active Directory", 
types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"), 
query = ";mail;{0}", param = c.Value);

c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"]
 => issue(
Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", 
Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, 
Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
);
```

However, on the to-be-configured ADFS instance, the SAML response for a login request returns:   

```

  

```

and the ADFS error logs says:  

"Microsoft.IdentityServer.Protocols.Saml.InvalidNameIdPolicyException: MSIS7070: The SAML request contained a NameIDPolicy that was not satisfied by the issued token. Requested NameIDPolicy: AllowCreate: True Format: urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress SPNameQualifier: . Actual NameID properties: null."  

I have googled for the error but could not find a solution that addressed the issue for me. Has anybody seen this issue before and can explain why the NameID policy is not applied? Any hints would be much appreciated.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-01-21*

Are you sure your test user has an email in the AD where the authentication takes place?
