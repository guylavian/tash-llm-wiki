---
title: "ADFS 3 and TLS 1.2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297246/adfs-3-and-tls-1-2
question_id: 297246
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 3 and TLS 1.2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297246/adfs-3-and-tls-1-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have an environment of 2 WAP behind load balancer and 2 adfs 3 servers. Each wap has local host file pointing to one of the adfs servers.     

Been seeing red X on some relying party for monitoring errors when the update automatically option is selected. Came across the following articles.     

https://learn.microsoft.com/en-US/troubleshoot/windows-server/identity/disable-and-replace-tls-1dot0    

https://social.technet.microsoft.com/Forums/lync/en-US/b0aefc22-0b4b-43ae-89d1-fad3b8a6c630/federation-metadata-url-the-request-was-aborted-could-not-create-ssltls-secure-channel?forum=ADFS    

The second link references the first one. It would be nice to actually have a readable article or How to for doing this in wap and adfs. The servers are 2012 r2 and have the default cipher suites (that is no registry settings for any so far).     

If we create the "enable" registry settings for ssl 3, tls 1.1, and tls 1.2 then will that work in updating the relying party? Or, do we need to exclusively disable the lower ones and have tls 1.2 enabled for tls 1.2 to take over? Wouldn't adfs first resort to the tls 1.2?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-03*

Thank you. I had come across that article as well. So in essence, one would need to create all those registry key/values and disable the lower protocols on all adfs and wap servers. Then, enable SchUseStrongCrypto. For 2012 r2 it says to create using "	New-ItemProperty -path 'HKLM:\SOFTWARE\Microsoft.NetFramework\v4.0.30319' -name 'SchUseStrongCrypto' -value '1' -PropertyType 'DWord' -Force | Out-Null",  that is, for .net v 4.0.   

Is that all there is? If a relying party has issues connecting after changing to tls 1.2 then will enabling tls 1.1 (or whichever lower protocol that does the job) work for that relying party since adfs will default to tls 1.2 through SchUseStrongCrypto?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-03-03*

There is an article about management SSL/TLS on ADFS/WAP servers: Managing SSL/TLS Protocols and Cipher Suites for AD FS     

Anyhow, you should disable the lower ones, regardless of the server's role or type. They are not considered secured anymore.    

And you should enable SchUseStrongCrypto on all your ADFS and WAP servers. Without SchUseStrongCrypto enabled the metadata lookup will fail if the file is hosted on a TLS1.1 or TLS1.2 server.
