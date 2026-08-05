---
title: "ADFS understanding needed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/49526/adfs-understanding-needed
question_id: 49526
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS understanding needed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/49526/adfs-understanding-needed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I have been asked quite a few questions about our infrastructure and in particular ADFS (Active Directory Federation Services). I have no idea as I don't have anything to do with Federated Services. I don't even know if it is set up in our Domain. I basically need to find out if we have Federation Services installed. Would anyone have any advice on how to check if we even have Federation Services installed on our Domain.  

Any information would be greatly received.  

Regards.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-07-20*

If you know the FQDN of the service, you can follow DNS to see where it points to. If you don't know the FQDN of the service, but you know of an application using ADFS, you can try to sign-in to this application to be redirected to ADFS and get the name. The names of ADFS deployments are often similar, so you can also arbitrary try sts.<your domain>, federation.<your domain>, fs.<your domain> or adfs.<your domain>.  

If DNS leads you to a load balancer, then you can ask the team in charge of it to give you the endpoint for the actual service.  

You can also look in AD. Using the Users and Computer console, make sure you have enabled the Advanced Features in the View menu and navigate to: Program Data, Microsoft then ADFS. You need to be a member of the Domain Admins group to see those objects. If you have something there, it means you have (or at least used to have an ADFS farm).  

Then if you look at the Security tab of the object which as a GUID for name, you might see a GMSA account (in the list of accounts with permission on the object, you might have one that looks like a user account but has a name finishing with a $ sign). If you have one, you can list what computers have permission to retrieve the password of that account with the following command:  

```
Get-ADServiceAccount -Identity  -Properties PrincipalsAllowedToRetrieveManagedPassword
```

If you don't have a GMSA account in the list of that security tab, you are left with either enabling AD audit (not worth it if that's not already enabled) or scan the servers like Leon suggested.  

You could also try to scan the network for a host listening on port 443 and 49443 as ADFS does listen on those two ports for clients (and technically port 80 as well for other ADFS servers if that's a deployment with multiple servers using WID).
