---
title: "ADFS 3 : Adding Multiple Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/125399/adfs-3-adding-multiple-domain
question_id: 125399
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 3 : Adding Multiple Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/125399/adfs-3-adding-multiple-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently we have ADFS running on server 2012r2 ... with DNS as adfs.firstdomain.com  

Now we have a requirement to add  second domain/DNS to our existing ADFS federation for one application.  

For eg:   

App 1 : https://adfs.firstdomain.com/adfs/ls/IdpInitiatedSignOn  

App2 2 : https://adfs.Seconddomain.com/adfs/ls/IdpInitiatedSignOn  

Please let me know how to achieve this.  

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-15*

So in theory yes we can set up something that does the trick from a DNS perspective. But there is a lot of caveats...  

You will need to make sure that you have the proper DNS record in company-b.com. An A record pointing to the same IP as the ADFS A record in company-a.com.  

You will need to ensure that the TLS (aka Service Communication Certificate) has the proper alternative subject name to reference either *.company-b.com or login.company-b.com on the top of the existing ones.  

You will need to add the SPN HOST/login.company-b.com to the ADFS service account in AD.  

You will need to make sure that the URL login.company-b.com is trusted in your browser to do Windows Integrated Authentication (else no single sign-on).  

On the ADFS server, you will need to configure the new SNI binding like:   

netsh http add sslcert hostnameport=login.company-b.com:443 certhash=<the thumbrint of your TLS cert>  appid={5d89a20c-beab-4389-9447-324788eb944a} certstorename=MY  

Now, that's the theory, because in practice, this will not work all the time and is not officially tested. In other words, that's an unsupported configuration. The metadata of the ADFS farm will also not contain those URI/URL either and this will likely not work through a WAP.  Better to work through those "restriction" IMO.
