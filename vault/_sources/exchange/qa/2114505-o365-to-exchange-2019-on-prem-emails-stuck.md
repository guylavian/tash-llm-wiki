---
title: "O365 to Exchange 2019 on prem emails stuck"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2114505/o365-to-exchange-2019-on-prem-emails-stuck
question_id: 2114505
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# O365 to Exchange 2019 on prem emails stuck

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2114505/o365-to-exchange-2019-on-prem-emails-stuck (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Have an office 2019 and Office365 hybrid environment. Emails from O365 to exchange on prem getting stuck on O365 side with error Reason: [{LED=450 4.4.317 Cannot connect to remote server [Message=451 4.4.0 Security status IllegalMessage].

Has been working okay just suddenly stopped. what could be issue?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-04*

Hi, @JohnMark Mulli  

According to the error information you provided, this issue usually occurs during the TLS handshake between Exchange Online and the remote email server.

To fix this, you can try:

-  Check out the articles provided by Andy.

-  Check your firewall and security software to make sure they're not blocking connections to remote servers.

-  Check whether the message content or headers comply with the remote server's security policy.

-  Make sure that the SSL certificate on the server you're trying to connect to matches the domain name and update SSL certificate.

-  Make sure that the required ports are open and that the protocol is set up correctly to allow connections.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-11-02*

See:

https://learn.microsoft.com/en-us/answers/questions/715125/office-365-hybrid-connector-error-450-4-4-317-cann
