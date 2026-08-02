---
title: "Updating out of date, ADCS certificate revocation list"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1525349/updating-out-of-date-adcs-certificate-revocation-l
question_id: 1525349
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Updating out of date, ADCS certificate revocation list

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1525349/updating-out-of-date-adcs-certificate-revocation-l (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If the CRL on an internal Active Directory CA has been out of date for sometime.  Will there be any issues if an up to date CRL is published.  What would be the safest way to go about updating the CRL
Thanks.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-06*

Hello james gledson,  

Thank you for posting in Q&A forum.  

*  

If the CRL on an internal Active Directory CA has been out of date for sometime. Will there be any issues if an up to date CRL is published.*
A: If there is any certificate is revoked during this time, then after you update the CRL to the newest file, and if this certificate can access the newest CRL file and Delta CRL file when it is used, then this certificate may not be used (because it checks that this certificate is revoked).

If there is no any certificate is revoked during this time, then there will be no impact.
What would be the safest way to go about updating the CRL.  

A: You can right click Revoked Certificate container and select Publish\All Tasks and select New CRL\Click OK.*  

*  

And right click Revoked Certificate container and select Publish\All Tasks and select Delta CRL only\Click OK.

Or you can publish CRL with command:   

Certutil -config "CAMchineName\CAName" -CRL
Certutil -config "CAMchineName\CAName" -CRL delta  

For example:

I hope the information above is helpful.
If you have any questions or concerns, please feel free to let us know.
Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-05*

Hi
You can update CRL without any issues. It’s important to keep it up to date to let clients able to identify revoked certificates.
It is  recommended to keep CRL up to date automatically.

Please don’t forget to accept helpful answer
