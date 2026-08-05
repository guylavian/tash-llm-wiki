---
title: "ADFS/WAP publish application using CBA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/185153/adfs-wap-publish-application-using-cba
question_id: 185153
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS/WAP publish application using CBA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/185153/adfs-wap-publish-application-using-cba (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have the following configuration (On Prem only)  

ForestA (Windows 2016 FFL).  This Domain has an ADFS farm with a WAP (all in 2016)  

ForestB (Windows 2016 FFL), This Domain has a Web server (IIS 2016) and configured with Windows Authentication.  

There is an internal CA in forestA that is added into the NTAuthCA of both Forests  

There is a 2-way trust between ForestA and ForestB (Forest-Wide Auth.)  

I have a client that is a stand alone (not member of any domain) and has a client certificate issued by the internal CA in ForestA.  Does this client should be able to access the Web server in ForestB through the ADFS/WAP using Certificate Authentication ?  

ADFS is configured with Certificate Authentication (external and Internal).  

I have added a claim rule to map the user principal name with the UPN  

WAP is publishing the web site using Preauth ADFS (Web and MSOFBA).  It has to be this because the WAP in pass-through cannot forward the client certificate to the web site.  

Even after this, when i try to connect using Certificate Auth. i receive a IIS error 500.  From the network traces on the WAP, i can see the Kerberos error KDC_ERR_POLICY.  

This should point to a Constrained delegation between domains which is not supported but i have configured using Resource-based constrained delegation...  

Am i missing something ?  

Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-04*

Thanks @Pierre Audonnet - MSFT    i do have the same understanding of the WAP and actually, it makes sense    

By the way, i do have the same issue if i configure using Forms Authentication.  So it's not an issue with the Certificate authentication but more related to a double hop authentication between 2 domains.    

I will try to configure the RBCD with the IIS server and we will see ;)    

Thanks!
