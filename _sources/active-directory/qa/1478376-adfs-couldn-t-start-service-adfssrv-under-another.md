---
title: "ADFS couldn’t start service adfssrv under another gMSA error 1064, 220"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1478376/adfs-couldn-t-start-service-adfssrv-under-another
question_id: 1478376
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# ADFS couldn’t start service adfssrv under another gMSA error 1064, 220

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1478376/adfs-couldn-t-start-service-adfssrv-under-another (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to start the ADFS service under a new gMSA and at about 10 seconds I get a 1064 error, unless I make a mistake while reading the internal WID database. I had this problem in a production environment, I get the same error in a lab environment. I just deployed DC01 (WS2022) and ADFS server (WS2022), there is nothing else. I deployed the ADFS role under the adfs_gmsa service account in the classic way. Everything is working. The goal is to get the ADFS server running under adfs_gmsa2 (in my case adfs_gmsa3, it doesn’t matter).

-  I create adfs_gmsa3 and bind to ADFS server

```
Add-KdsRootKey –EffectiveTime ((get-date).addhours(-10))
New-ADServiceAccount -Name adfs_gmsa3 –RestrictToSingleComputer
$Identity = Get-ADComputer -identity ADFS
Add-ADComputerServiceAccount -Identity $identity -ServiceAccount adfs_gmsa3

Install-ADServiceAccount -Identity adfs_gmsa3
```

-  Next I assign adfs_gmsa3 to the adfssrv service

-  I give the same rights in the database to adfs_gmsa3 as for adfs_gmsa

-  Granted more rights to the certificate 

Didn't do anything else. I'm trying to start the ADFS service and the error is like in the screenshots. I suspect that I can't read the database. But there are still the same rights for adfs_gmsa3. What's wrong?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-12*

Hi @OZ •
Thank you for your feedback.
I will add you answer as a comment to let you accept  it as helpful and help other forum visitor facing the same issue to identify helpful answer.

---Please don't forget to accept helpful answer

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-05*

Hi @OZ

I think you forgot to specify the list of server allowed to retrieve the GMSA password when you create the service account.

You can specify adfs server to retrieve password by following command:

`Set-ADServiceAccount -Identity adfs-gmsa1 -PrincipalsAllowedToRetrieveManagedPassword "ADFS-SRV-Name$"`

Please don't forget to accept helpful answer
