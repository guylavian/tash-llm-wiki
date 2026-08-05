---
title: "Can I install AD CS on WSUS server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/278986/can-i-install-ad-cs-on-wsus-server
question_id: 278986
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Can I install AD CS on WSUS server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/278986/can-i-install-ad-cs-on-wsus-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I need to install CA in my small environment for LDAPS clients and for some certificates for intranet sites. I have only domain controller server on windows 2012 r2, and WSUS server connected to domain with Windows server 2019. As I read having AD CS on domain controller is not recommended everywhere, my question is if this is any security risk to install it on my WSUS server?  

thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-21*

If I go with one root ca server (without subordinate) can I just turn it off for security reasons after I configure it and issue all my certificates for intranet sites, ldaps servers etc, then ca server will be useless for two years (validity time of ssl certificate) am I right?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-19*

Hello @Tutek  ,    

Thank you for posting here.    

The best practice we recommend is that a server should play one role or as few roles as possible. Because this reduces possible resource conflicts and exploit vulnerabilities and minimizes patching of other applications that might cause downtime.    

If you do have limited resources, you can install ADCS on WSUS server.    

We can refer to the following similar case.    

WSUS, DC and CA on same physical machine?    

https://social.technet.microsoft.com/Forums/en-US/d9635885-3c16-49bd-b010-b2a2de9ceeaa/wsus-dc-and-ca-on-same-physical-machine?forum=winserverwsus    

References    

Step 3: Configure WSUS    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh852346(v=ws.11)?redirectedfrom=MSDN#consswsus    

How to setup Microsoft Active Directory Certificate Services    

https://www.virtuallyboring.com/setup-microsoft-active-directory-certificate-services-ad-cs/    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-02-18*

WSUS assumes IIS server, which is another potential attack vector. If server is compromissed via IIS (to be more precise, via vulnerable or miconfigured web app), then CA is compromised too. However, if you have limited license resources, then you don't have alternatives and have to use only available resources.
