---
title: "Need guidance on Inherited Environment with ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/921560/need-guidance-on-inherited-environment-with-adfs
question_id: 921560
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Need guidance on Inherited Environment with ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/921560/need-guidance-on-inherited-environment-with-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I have an environment that had Azure AD sync setup before I started working here. It is already syncing all the users. The computers are being added to the Devices list because SCP is setup but none of the OU's with the computers are being AAD Synced. We have an ADFS server for SSO capabilities for O365 and several other services. I will admit, my ADFS knowledge is quite limited though I am well versed in AD DS. Also ADFS works in tandem with DUO.    

I would say my Azure AD Sync experience is as a novice or intermediate. So don't be afraid to dumb it down.    

Password Hash Sync and Enable single sign on are the effective config at this time in Azure AD Connect Sign In options.    

I was hoping to get some help understanding with a few things and what my options are. I have tried to figure it out but with so much documentation and not being involved in the initial setup I'm struggling a bit. I had begun setup of a test lab but that is proving to cost more than I can afford right now.    

Am I required to use ADFS to get a fully functional Hybrid Azure AD situation working? Or is the current config enough?    

It is looking like it is not required because I added an OU to sync and put a single pc in there and it successfully changed from Azure AD Registered to Azure AD Joined. It has a timestamp under the Registered column. If ADFS is required I may have follow up questions later.    

The reason I question it is because once joined and the dsregcmd (can post if needed) shows all green (I think), with the pc off network, I cannot login as a user that wasn't logged in once initially so the profile exists.     

Is this expected behavior?    

I was sort of tasked with working on these with the end result in mind being, giving the ability for people off-prem end users to join the domain without a VPN. I read way to late that the computer must be able to talk to the domain computer until the entire registration process is complete.    

I wanted to confirm if this is an absolute?    

I appreciate any guidance that can be provided.    

P.S. If there is time, a question about my lab. Can I get a fully functional Hybrid Azure AD setup with a single ADFS server with a cert issued from a CA I spun up for a .local domain? Or would I have to use a WAP with a cert from a public authority with a FQDN?    

Thanks again.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

You don't need to use ADFS if you dont want to for Hybrid AADJ. You can just sync the devices. [https://learn.microsoft.com/en-us/azure/active-directory/devices/howto-hybrid-azure-ad-join#federated-domains. If that's all you are using ADFS for I would recommend removing ADFS, [https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480, and [https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
