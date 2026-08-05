---
title: "ADFS service not woking externally"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/958099/adfs-service-not-woking-externally
question_id: 958099
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS service not woking externally

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/958099/adfs-service-not-woking-externally (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have setup ADFS in my lab for testing and get to know how adfs works.    

on my lan adfs works without any issue but when i try to access adfs externall it doesnt work.    

I read few articles and all of them talk about setting up external dns    

issue is that I dont have public IP address.    

I found this article which is talking about azure proxy but still this doesnt work    

https://mscloudjournal.com/2022/05/08/configure-adfs-to-work-externally-without-having-a-wap-server-configure-azure-app-    

proxy-to-publish-adfs-externally/    

Can someone please let me know how I can access the adfs externally.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-09*

The recommended way to have AD FS work for external user is to deploy a Web Application Proxy. You should not use the Azure AD Application Proxy for this. Check this: https://learn.microsoft.com/en-us/azure/active-directory/app-proxy/application-proxy-faq "Azure AD Application Proxy is designed to work with Azure AD and doesn’t fulfill the requirements to act as an AD FS proxy".    

So you deploy a WAP and you make sure the WAP is reachable from outside on a public IP address and the port TCP 443. You can also use another device on the front of the WAP but do you skip the WAP. It is an important component for remote access because it has security and policy features that AD FS wouldn't have if exposed directly. The WAP doesn't need to be domain joined, but need to be able to contact AD FS on the port TCP 443.    

Then most important part of the deployment is the split brain DNS (or split horizon DNS). Let say your ADFS URL is `https://adfs.contoso.com`.    

When an internal client is connecting to ADFS they need to resolve `adfs.contoso.com` to a private IP, the one of your internal AD DS server. So the DNS server they are using needs to have the private IP for the A record `adfs.contoso.com`.    

When an external client is connecting to ADFS, they need to resolve `adfs.contoso.com` to a public IP, the public IP of your WAP server. They are public clients so they use public DNS. You need to make sure the public DNS servers hosting the zone `contoso.com` have the public IP of the WAP server for the A host record `adfs.contoso.com`.     

Also, if your WAP server uses a public DNS server, it will think that `adfs.contoso.com` is itself. And will not be able to contact the AD FS server on the backend. So either you do not use public DNS servers on your WAP. Or you use a HOSTS file on the WAP to make sure that `adfs.contoso.com` points to the private IP of the AD FS server.
