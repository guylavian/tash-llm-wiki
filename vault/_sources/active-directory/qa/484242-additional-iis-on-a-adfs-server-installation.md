---
title: "Additional IIS on a ADFS-Server installation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/484242/additional-iis-on-a-adfs-server-installation
question_id: 484242
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other", "windows-development-iis"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Additional IIS on a ADFS-Server installation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/484242/additional-iis-on-a-adfs-server-installation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to install the IIS server role on a system, which host already the ADFS-Service?  

We need an additional IIS installation to provide some web-apps on the same Windows-Server 2016 which hosts the ADFS-Service for our infrastructure.  

Does someone know if I can install the IIS component?  

ADFS use by default port 80 and 443, our Webapps can use different ports - but the main question is if the installation / configuration of the IIS will be stop because the default ports of IIS are already in use.  

Thanks for any help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-22*

Hi @Andy   ,    

As far as I know, ADFS server is also based on windows server. So it can work with IIS if both of them install on windows server.    

However. As piaudonn said, it may has some issues about security and others. ADFS server and IIS both use 80 and 443 port as default port, this may cause conflicts.    

If the answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our  documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.    

Best regards,    

Bruce Zhang

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-21*

In theory you could. In practice you shouldn't.  

ADFS is a very sensitive service. Should be considered as secured as a domain controller (and you don't install IIS on domain controllers).   

It also increases the likelihood of an administrative mistake impacting the other component (TLS bindings, user right assignments modifications, certificate enrollment...).  

I'd stay away from this configuration.
