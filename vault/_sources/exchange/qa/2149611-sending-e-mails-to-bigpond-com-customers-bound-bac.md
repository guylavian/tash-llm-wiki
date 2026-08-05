---
title: "Sending e-mails to Bigpond.com customers bound backs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2149611/sending-e-mails-to-bigpond-com-customers-bound-bac
question_id: 2149611
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Sending e-mails to Bigpond.com customers bound backs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2149611/sending-e-mails-to-bigpond-com-customers-bound-bac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,

Under the doamin: chromaderm.com.au

All the emails to @bigpond.com email has been bound backs. Other domain or gmail working in order.

Defer:Reason: [{LED=451-4.7.23 Message deferred - unable to verify SPF policy for 451 4.7.23 chromaderm.com.au. IB305 i{2b0c499b-c839-43d2-9c76-dda19649fe67}};{MSG=};{FQDN=extmail.bigpond.com};{IP=203.42.22.10};{LRT=1/21/2025 3:45:12 AM}]. OutboundProxyTargetIP: 203.42.22.10. OutboundProxyTargetHostName: extmail.bigpond.com

Checked the SPF working in order:

```
Test	Result
```

Status Ok	SPF Record Published	SPF Record found

Status Ok	SPF Record Deprecated	No deprecated records found

Status Ok	SPF Multiple Records	Less than two records found

Status Ok	SPF Contains characters after ALL	No items after 'ALL'.

Status Ok	SPF Syntax Check	The record is valid

Status Ok	SPF Included Lookups	Number of included lookups is OK

Status Ok	SPF Recursive Loop	Nor Recursive Loops on Includes

Status Ok	SPF Duplicate Include	No Duplicate Includes Found

Status Ok	SPF Type PTR Check	No type PTR found

Status Ok	SPF Void Lookups	Number of void lookups is OK

Status Ok	SPF MX Resource Records	Number of MX Resource Records is OK

Status Ok	SPF Record Null Value	No Null DNS Lookups found

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-22*

Hi Alex,

Thanks for the quick response.

STILL bound backs

Here is some results of the attachments.

Maybe the problem is DKIM at MS portal???

DKMI.jpg

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-21*

Hello, @PETER LAI,

Welcome to the Microsoft Q&A platform!

Based on your description, although you've verified that your SPF record is correctly configured and valid, the Bigpond mail server is still unable to verify your SPF policy.

Here are a few steps you can take to troubleshoot and resolve this issue:

1.Check SPF Record: Ensure that your SPF record includes all the necessary IP addresses and domains that send emails on behalf of chromaderm.com.au. You can use tools like MXToolbox to verify your SPF record. Please refer to Set up SPF identify valid email sources for your Microsoft 365 domain - Microsoft Defender for Office 365 | Microsoft Learn.

2.Check DNS Propagation: DNS changes sometimes can take time to propagate. Ensure that your SPF record changes have fully propagated across the internet.

3.Check for DNS Issues: Use DNS diagnostics tools to ensure there are no other issues with your DNS setup. Sometimes, unrelated DNS issues can cause problems with email delivery.

4.Review Email Sending Practices: Make sure that your emails comply with best practices, such as not sending bulk emails from a consumer internet connection, limiting the number of recipients per email, and including appropriate headers.

5.Email Authentication: Ensure that you are also using other email authentication methods like DKIM (DomainKeys Identified Mail) and DMARC (Domain-based Message Authentication, Reporting, and Conformance) to further authenticate your emails. These additional layers of security can help improve email deliverability.

Official documents for instruction：

How to use DKIM for email in your custom domain - Microsoft Defender for Office 365 | Microsoft Learn

Use DMARC to validate email, setup steps - Microsoft Defender for Office 365 | Microsoft Learn

If after checking all these steps the problem persists, it may help to examine server logs or further monitor email traffic for any unusual patterns or additional error messages that could give more clues to the root cause. 

Moreover, since your SPF record appears to be valid, the issue might be on Bigpond’s end. Reach out to Bigpond’s support team with the bounce-back message and detailed information regarding the issue. They might be able to provide more insights or whitelist your domain.

Should you need more help on this, you can feel free to post back. 

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
