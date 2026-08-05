---
title: "Migrating AD CS to an older version of Windows"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1437694/migrating-ad-cs-to-an-older-version-of-windows
question_id: 1437694
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrating AD CS to an older version of Windows

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1437694/migrating-ad-cs-to-an-older-version-of-windows (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to migrate an Enterprise CA from a Windows Server 2016 to e.g. a Windows Server 2012 R2?

Been trying to do this but starting the CA service on the older Windows fails with "Version of log file is not compatible with Jet version 0x0 (WIN32: 0)".

Apparently the ESE/Jet DB engine on 2012 R2 cannot read the newer DB format?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2023-11-27*

Hello Tommy Az,  

Thank you for posting in Q&A forum.  

We cannot migrate AD Certificate Services from Windows Server 2008 to Windows Server 2016, because the JET database engine changed so much between the two versions that if we restore the backup we get a JET version error at startup and the CA won't start. So we cannot migrate ADCS from Windows Server 2016 to Windows Server 2008.  

If you cannot migrate AD CS from 2016 to 2012 R2 in your lab or in your production environment, maybe it is.

https://social.technet.microsoft.com/wiki/contents/articles/37373.migrating-ad-certificate-services-from-windows-server-2008-to-windows-server-2016.aspx  

We all migrate AD CS from lower version to higher version, but why did you want to Migrate AD CS to an older version from higher version?  

Check if you select SHA1 (or SHA256) during migration on both lower version and higher version.

Check if you select CSP (or KSP) during migration on both lower version and higher version.

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn771627(v=ws.11)?redirectedfrom=MSDN  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
