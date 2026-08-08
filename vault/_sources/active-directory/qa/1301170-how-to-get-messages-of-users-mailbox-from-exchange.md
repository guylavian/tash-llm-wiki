---
title: "How to get messages of user's mailbox from Exchange on-prem use modern authentication?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1301170/how-to-get-messages-of-users-mailbox-from-exchange
question_id: 1301170
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "microsoft-security-security-active-directory-federation-services", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to get messages of user's mailbox from Exchange on-prem use modern authentication?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1301170/how-to-get-messages-of-users-mailbox-from-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Exchange Server 2019 with enabled modern authentication. I also set up ADFS server. So when I access Outlook mailbox by the path https://example.com/oaw -> It redirects to ADFS server -> Enter credentials -> It goes to Outlook and I can see the messages on inbox.

So I implement code:

-  Get access token from ADFS server (completed).

-  Try to authenticate Exchange on-prem with the above access token using EWS Managed API but unsuccessful. The code is like this:

```
var accessToken = GetAccessTokenAsync().Result;
    ExchangeService service = new ExchangeService(ExchangeVersion.Exchange2013);
    service.Url = new Uri("https://example.com/ews/exchange.asmx");
    service.Credentials = new OAuthCredentials(accessToken);
    service.AutodiscoverUrl("user_1@example.com", RedirectionCallback);
    FindItemsResults results = service.FindItems(WellKnownFolderName.Inbox, new ItemView(int.MaxValue));
```

But it got the error 'The request failed. The remote server returned an error: (401) Unauthorized.' It seems that the OAuthCredentials(accessToken) don't work.

Do you have any solutions or ideas to get the messages from the user mailbox from Exchange on-prem by modern authentication? Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-09*

Hi @Dung Lee  ,

As far as I know, with the release of Exchange Server 2019 CU13, Exchange Server supports `OAuth 2.0` (also known as Modern authentication) for pure on-premises environments using ADFS as a security token service (STS). Initially, this feature is available only for Outlook on Windows, OWA is not supported current period.

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/enable-modern-auth-in-exchange-server-on-premises?view=exchserver-2019#overview

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
