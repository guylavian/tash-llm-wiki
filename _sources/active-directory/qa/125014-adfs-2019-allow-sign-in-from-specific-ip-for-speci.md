---
title: "ADFS 2019 allow sign in from specific IP for specific users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/125014/adfs-2019-allow-sign-in-from-specific-ip-for-speci
question_id: 125014
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# ADFS 2019 allow sign in from specific IP for specific users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/125014/adfs-2019-allow-sign-in-from-specific-ip-for-speci (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have an ADFS 2019 and ADFS 2019 Proxy servers to have SSO with Office 365.  

For a specific group in our AD we only want to allow the signin from a specific IP or a computer that is joined in our domain.   

All other users can sign in from everywhere.  

When I search on internet I can only find documentation about ADFS 2012 and I need to create Issuance Authorization Rules.  

But in ADFS 2019 I don't have Issuance Authorization Rules.  

How can I achieve my goal?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-15*

Like @Vasil Michev   says you can use Access Control Policies.    

Let say you want to allow all users but if the user is a member of the group TESTG then you allow the connection only if the IP is 1.2.3.4. You will have the following policy:    

    

The first part allow all users as long as they are not member of the group.    

If they are member of the group then we allow them as long as the IP is not between 0.0.0.0 and 1.2.3.3 and not between 1.2.3.6 and 255.255.255.255. In other word we allow only if the if IP is 1.2.3.4.    

Also, you can still use the "old school" issuance authorization rules in Windows Server 2019 ADFS. To do so, set the policy of your relying party to $null, example:    

```
Set-AdfsRelyingPartyTrust -TargetName ClaimsXray -AccessControlPolicyName:$null
```

Then check the GUI and you'll see your policy has been converted into an old school one :)

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-13*

Of course you do, they're simply packaged as Access Control Policies: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/access-control-policies-in-ad-fs
