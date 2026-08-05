---
title: "LDAP Signing on Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1130584/ldap-signing-on-domain-controllers
question_id: 1130584
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# LDAP Signing on Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1130584/ldap-signing-on-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We   enforced LDAP Signing Required on our clients about a month ago using a GPO.  We are still testing to see if anything breaks.  Now I want to enforce LDAP signing on the Domain Controllers. I want to do this manually through the Local Security Policy. I will set Domain controller: LDAP server signing and Domain controller: LDAP server channel binding.    

My question is, will I have to restart the domain controllers?  I know I will have to restart if I configured channel binding through the registry.     

Thanks for your help.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-12-16*

Domain controller: LDAP server signing    

This setting doesn't require restart, changes are applied immediately: https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/domain-controller-ldap-server-signing-requirements#restart-requirement    

Domain controller: LDAP server channel binding    

This setting doesn't require restart, changes are applied immediately: https://support.microsoft.com/en-us/topic/kb4034879-use-the-ldapenforcechannelbinding-registry-entry-to-make-ldap-authentication-over-ssl-tls-more-secure-e9ecfa27-5e57-8519-6ba3-d2c06b21812e
