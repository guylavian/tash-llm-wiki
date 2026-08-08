---
title: "Can CNAMEs be created for Kerberos on alternative UPN suffixes?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186464/can-cnames-be-created-for-kerberos-on-alternative
question_id: 1186464
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Can CNAMEs be created for Kerberos on alternative UPN suffixes?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186464/can-cnames-be-created-for-kerberos-on-alternative (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Troubleshooting a deployment, I found out that the server to which the SRV records points has to be match the domain of the SRV record. The mismatching domain, while isn't itself the base for the directory, it does participate in it as an alternative UPN suffix. It's actually also out email domain, used by exchange and most users UPNs, while non-user user (and machine) accounts continue to use the real AD domain name.

I figured I could just fix it by adding a CNAME (e.g; `netdom computername machine /add:altmachine`) so it gets another service principal in Kerberos like I do in machines whose Kerberos service principals have been delegated to other accounts, so PowerShell Remoting and Server Manager continue to work remotely.

Then I remembered, the Kerberos realm has never changed and from what I understand two Kerberos realms can't be just randomly linked together like AD domains in a forest. on the other hand, it is set as an alternative UPN suffix, Exchange recognizes it, and even on third party apps users can sign in with that domain, though only written in the UPN form, otherwise in the `netbiosdomainname\username`, `username@netbiosdomainname` and `domainname.tld\username` forms, it's still the original domain. It confusing.

Can CNAME be create for alternative UPN suffixes? Thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-05*

Hi @Vita

You can create CNAME or A DNS record for the alternative suffixes.

If want use the alternative suffix as DNS suffixe to authenticate via kerberos protocol on target server or service, you have to add a SPN for this alternative suffixe for each service.

Please dn't forget to mark helpful answer as accepted
