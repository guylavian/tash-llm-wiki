---
title: "ADFS server core 2016 Error: 'The certificate specified does not meet all the requirements of an SSL certificate."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185373/adfs-server-core-2016-error-the-certificate-specif
question_id: 1185373
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
---
# ADFS server core 2016 Error: 'The certificate specified does not meet all the requirements of an SSL certificate.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185373/adfs-server-core-2016-error-the-certificate-specif (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are having an issue with our ADFS certificate renewal, our cert has expired, and use local ADCS to generate the certs.

The new cert has been generated and is in the ADFS server, but whenever I try "Set-AdfsSslCertificate -Thumbprint 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' to set the new cert, I get the below error, I'm now kind of clueless as to what am I missing. I'm logged in via the local administrator account, and everything is on-prem. 

Thanks in advance for all the 🙂

```
Set-AdfsSslCertificate : PS0317: One or more of AD FS servers returned errors during execution of command
'Set-AdfsSslCertificate'. Error information: PS0316: AD FS Server: 'localhost', Error: 'The certificate specified does
not meet all the requirements of an SSL certificate.'.
At line:1 char:1
+ Set-AdfsSslCertificate -Thumbprint 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Set-AdfsSslCertificate], RemoteException
    + FullyQualifiedErrorId : RuntimeException,Microsoft.IdentityServer.Management.Commands.SetSslCertificateCommand
```

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-03-01*

Hi,

Did you runt the PS command in elevated ADmin mode? Try that option and also check the event logs and provide details if additional details are logged in the event viewer. There is another thread with similar issue check the solution might help - https://community.spiceworks.com/topic/2343349-unable-to-set-adfs-ssl-certificate-thumbprint

Hope this helps.

JS

==

Please accept as answer and do a Thumbs-up to upvote this response if you are satisfied with the community help. Your upvote will be beneficial for the community users facing similar issues.
