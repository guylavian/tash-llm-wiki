---
title: "DKIM fails when sending with Exchange Hybrid SMTP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1501192/dkim-fails-when-sending-with-exchange-hybrid-smtp
question_id: 1501192
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# DKIM fails when sending with Exchange Hybrid SMTP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1501192/dkim-fails-when-sending-with-exchange-hybrid-smtp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
We have an exchange hybrid environment with a receive connector for SMTP. The settings for the receive connector looks like this:

With following send connector:

We are sending emails to external domains automatically via SMTP without authentication. If we enable DKIM it fails although we see the DKIM-Signature in the header.

Authentication-Results:

mx.google.com; dkim=fail header.i=@ourdomain.com header.s=selector2 header.b=aRRIv5Z9; dkim=fail header.i=@ourdomain.com header.s=selector2 header.b=aRRIv5Z9; arc=fail (signature failed); spf=pass (google.com: domain of @ourdomain.com designates as permitted sender) smtp.mailfrom=@ourdomain.com

X-MS-Exchange-Authentication-Results:

spf=pass (sender IP is xxx.xxx.xxx.xxx) smtp.mailfrom=ourdomain.com; dkim=fail (signature did not verify) header.d=ourdomain.com;dmarc=bestguesspass action=none header.from=Ourdomain.com;

Sending emails via Outlook or Outlook OWA doesn't have any DKIM problems.

How do I fix the DKIM failure when sending with Exchange Hybrid SMTP?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-22*

If all your outbound mail goes through 365, enable DKIM there and turn off anything else - https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dkim-configure?view=o365-worldwide#steps-you-need-to-do-to-manually-set-up-dkim

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-19*

Hi @Safak,

Did you mean you enabled DKIM in Exchange Online?

If yes, do the messages go to external recipients directly from Exchange Online? (on-premises to online to external, no other third-party gateways)

If yes, does this issue only occur to certain recipients?

Please also post the DKIM-Signature part of the message header.

(Don't forget to hide your personal information)
Example:

```
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=contoso.com; s=selector1-contoso-com; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-SenderADCheck; bh=KEs42OsNdsrmiPfcVLwpIUZVT+vEuqqygMUN9vA+M2Y=; b=O8/rYT/jYym6TfYubf7UAvHIgqxqbd/RYnWn3KNV9Vc2yLrOOwEUtizwh1pwylLxJYIUKOdkrIEG7DOgqLG+xWLbURRsOTvt24yb1SlHBdTzzUcPHHVNaLFMWtGd3odEuGdjVXBmLdWsyR0s+8PUvqvqINoKrEqBAJm4VRts5ykZtD9RgcKndhQ0aWcWUTIbqagmFWmWkzDlvtW50T82C+KpLIW/SAPtzV/Vkss33HXqEOs05op/Xkca6IeJW1L5uNpv1jNceqnShZt8hIUWP5cjhYfwc9erFnjRjYQIndWVQ0wdoVpLN8GcCRp+Q92VgD09SZJwMuJlRI9kJo9kPw==
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
