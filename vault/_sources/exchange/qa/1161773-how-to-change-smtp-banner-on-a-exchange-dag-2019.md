---
title: "How to change smtp banner on a Exchange DAG 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161773/how-to-change-smtp-banner-on-a-exchange-dag-2019
question_id: 1161773
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to change smtp banner on a Exchange DAG 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161773/how-to-change-smtp-banner-on-a-exchange-dag-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to change our banner so it match our MX.

I would like to preserve the original layout but only change the server name.

I have tried this but it do not translate <RegionalDay-Date-24HourTimeFormat> <RegionalTimeZoneOffset> as I hoped.

"XMAILDB01\Default Frontend XMAILDB01" –Banner "220 mail.corp.com Microsoft ESMTP MAIL service ready at <RegionalDay-Date-24HourTimeFormat> <RegionalTimeZoneOffset>"

But my other problem when I read a similary case:

https://learn.microsoft.com/en-us/answers/questions/1035819/how-to-change-smtp-banner-(exchange-2019)

It says this was not the way to do it if you have more mail servers as we have in our DAG cluster.

So how to do it?

All this because our Reverse DNS does not match SMTP Banner and spam filers are not happy about this.

Regards

Henning

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-19*

Take a reference at the similar error here: Rename the FQDN of default receive connector

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-18*

Hi Andy

Thanks I will try to make a new Receive connector.

I was just hoping to make a banner like the default but just with MX dns record. As I like it with timestamp.

Regards

Henning

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-18*

The banner is simply text, you cant insert anything but that.

For that second question, yes you create a new receive connector for port 25 for all IP remote ranges and anonymous permissions, then disable the Default Front End Receive connector which is the entry point to Exchange for external messages normally.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-18*

Hi

Thanks for replying

Yes I have read that link already, but it do not give any information about the 2 questions

No information about injecting <RegionalDay-Date-24HourTimeFormat> <RegionalTimeZoneOffset> in the banner

Also it only explanse how to set the banner. So if you follows the explanasion you end up with "220 mail.corp.com" and that was not what I was looking for.

Also when it is explaned, you cannot use the default receive connector, it is not clear what then.

Should I disable the default receive connector, and create a new , and use that insted and modify the banner for this on? And the new receive connector still use port 25/tcp.

Regards

Henning

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-18*

Hi @Henning Svane  ,

As stated in the documentation you provided, you could not directly modify the default receive connector, you need to create a new receive connector to do what you expect.

You could refer to: Modify the SMTP banner on Receive connectors

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
