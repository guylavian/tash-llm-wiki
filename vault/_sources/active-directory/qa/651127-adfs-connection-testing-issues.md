---
title: "ADFS connection testing issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/651127/adfs-connection-testing-issues
question_id: 651127
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS connection testing issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/651127/adfs-connection-testing-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,   

I am working on setting up a pretty simple (at least it should be) single ADFS server to create SSO for our cloud CRM.  I have the feature installed and services are running.  I have my public cert installed and the cert from my CRM provider installed.  We are running 2012 R2 so I imagine this would be ADFS 3.0 which means there is no IIS involvement per the website.  Right now this is where I am.    

From the ADFS server I can use the URL https://localhost/adfs/ls/idpinitiatedlogin and reach the blue login screen.  But that is the only way.  I cannot use the FQDN or the IP address to reach the same screen.  The server is obviously available as it is an active app server in our environment.  I cannot hit this screen from any other computer in my environment.  Also when I do hit the URL it says that my certificate is invalid, but since this is 3.0 and does not use IIS I don't know where to correctly bind the certificate, and since its already installed, I'm not sure what else needs to be done.    

Any help would be greatly appreciated.   

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-06*

My provider that we are trying to create the SSO with says that the message states that ADFS is only available to the local host but to no other client.  What configuration should I look for to figure out why this is?  I can telnet to the HTTPS port on the server from another PC but cannot access the ADFS link.  Any thoughts?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-03*

Ok my hostname and the server name are different.  I tried to hit the URL you sent with my farm name and same result "site can't be reached".  I can ping the DNS name without issue.  Are there any possible issues with the certificate?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-03*

So you mean the identifier correct?  I still can't connect to that name either.  Neither HTTP or HTTPS, they both bring up Site Can't Be Reached.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-03*

You can only connect to the ADFS server by calling the name of the farm. That's the name you can see in the admin console or in the output of `Get-ADFSProperties`.    

This is because the TLS/SNI implementation. The FQDN of the address you type in the browser has to match the certificate AND the name of the farm.    

You can create a fallback SNI configuration for clients not compatible with SNI. The reco is to use the right name as opposed as create the fallback. It is essentially what is discussed here: https://learn.microsoft.com/en-us/answers/questions/645614/adfs-endpoint-configurations.html
