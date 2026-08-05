---
title: "Renew Microsoft Exchange Certificate in Edge Server Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664492/renew-microsoft-exchange-certificate-in-edge-serve
question_id: 1664492
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Renew Microsoft Exchange Certificate in Edge Server Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664492/renew-microsoft-exchange-certificate-in-edge-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We will be renewing Microsoft Exchange Certificate in Edge Server. 

Do we still need to resync Edge Subscription after the renewal?

There's also an existing 3rd-party SSL certificate.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-10*

Hi,

If you renew or replace a certificate that was issued by a CA on a subscribed Edge Transport server, you need to remove the old certificate, and then delete and recreate the Edge Subscription. For more information, see Renew an Exchange Server certificate  (https://learn.microsoft.com/en-us/exchange/architecture/client-access/renew-certificates?view=exchserver-2019#:%7E:text=If%20you%20renew%20or%20replace%20a%20certificate%20that%20was%20issued%20by%20a%20CA%20on%20a%20subscribed%20Edge%20Transport%20server%2C%20you%20need%20to%20remove%20the%20old%20certificate%2C%20and%20then%20delete%20and%20recreate%20the%20Edge%20Subscription.%20For%20more%20information%2C%20see%20Edge%20Subscription%20process) and Edge Subscription process(https://learn.microsoft.com/en-us/exchange/architecture/edge-transport-servers/edge-subscriptions?view=exchserver-2019#edge-subscription-process).

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-09*

Yes I believe so:

https://learn.microsoft.com/en-us/answers/questions/1165967/renew-revalidate-certificate-on-edge-server-and-ex
