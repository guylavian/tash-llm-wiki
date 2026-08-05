---
title: "Exit Module ADCS Configuration issue on Windows 2019 - Using Variables in BodyArg"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/439242/exit-module-adcs-configuration-issue-on-windows-20
question_id: 439242
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exit Module ADCS Configuration issue on Windows 2019 - Using Variables in BodyArg

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/439242/exit-module-adcs-configuration-issue-on-windows-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This might be a stupid question but I am beating my head against the wall.  I have tried removing whitespace, trying single %.. etc and I am following the microsoft 2008 doc on how to set it up.  

Templates\Default\Pending  

BodyArg -   

Request.RequestID  

UPN  

Request.RequesterName  

Request.SubmittedWhen  

Request.DistinguishedName  

CertificateTemplate  

Request.DispositionMessage  

BodyFormat -   

Request ID: %%1  

UPN: %%2  

Requester Name: %%3  

Request Submission Date (GMT): %%4  

Distinguished Name: %%5  

Certificate Template used: %%6  

Request Disposition Message: %%7  

E-mail comes like this -   

Title - A certificate is pending on %1  

Body -   

Request ID: %1  

UPN: %2  

Requester Name: %3  

Request Submission Date (GMT): %4  

Distinguished Name: %5  

Certificate Template used: %6  

Request Disposition Message: %7  

I feel like this should be easy and I am just missing something.  Why aren't the %Variables subbing in the bodyarg values? Thank you For ANY help!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-17*

Hello @Spatz, Jason W  ，

Thank you for posting here.

1.Based on the description "I am following the microsoft 2008 doc on how to set it up", what microsoft 2008 doc did you follow? Would you please provide the article link?

2.What are you doing now?

3.And what issue do you have now?

4.What is BodyArg? Is it a microsoft product or non-Microsoft product?

Maybe the following links is helpful to you.  

Active Directory Certificate Services SMTP Exit Module for Windows Server 2008 R2 Example  

https://social.technet.microsoft.com/wiki/contents/articles/2004.active-directory-certificate-services-smtp-exit-module-for-windows-server-2008-r2-example.aspx

Operating a PKI: SMTP Exit Module  

https://sysadmins.lv/retired-msft-blogs/xdot509/operating-a-pki-smtp-exit-module.aspx

Hope the information above is also helpful.

Should you have any question or concern, please feel free to let us know.

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
