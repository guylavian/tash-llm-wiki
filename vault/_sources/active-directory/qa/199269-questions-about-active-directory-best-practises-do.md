---
title: "Questions About Active Directory Best Practises - Domains, Subdomains, and DNs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199269/questions-about-active-directory-best-practises-do
question_id: 199269
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Questions About Active Directory Best Practises - Domains, Subdomains, and DNs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199269/questions-about-active-directory-best-practises-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm learning active directory in a homelab environment here, so please excuse my lack of technical understanding;    

I have an active directory server "ad-01", serving as active directory + DNS server for users to authenticate into other services, such as linux based file servers, web servers, etc. The server is currently configured at the domain "ad.domain.tld", and I have created an alternate UPN suffix for just "domain.tld", as there is a webserver running on "domain.tld", and I have found from previous research that it is best practice to run the root domain as "ad.domain.tld" or similar. I've been having issues getting my third party services to authenticate against my active directory server, and I suspect it has to do with the active directory bind users I've created for these services having usernames "username@keyman  .tld" while the AD domain is "ad.domain.tld". I am also struggling a little bit with "Base Bind DN", and how exactly to select a security group using this function.    

Some guidance on working with alternate UPN Suffixes, running "domain.tld" vs "ad.domain.tld", and how to use DNs to define security groups, would be hugely appreciated.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-16*

Hello @roomwillow  ，

Thank you for posting here.

To better understand our question and help you, please confirm the following information:

1.Based on the description "I have an active directory server "ad-01", serving as active directory + DNS server for users to authenticate into other services", what is your domain name with domain controller "ad-01"?

2.Is your domain name "domain.tld" or "ad.domain.tld" ?

3.Is "ad.domain.tld" a root domain name or child domain name in "domain.tld"?

4.Based on "getting my third party services to authenticate against my active directory server", what is your third-party service/third-party app? How does your third-party authenticate against active directory server? Do you use username@keyman  .tld to logon the corresponding app but failed?

If anything is uncleal ,please feel free to let us know.

Best Regards,  

Daisy Zhou
