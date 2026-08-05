---
title: "Showstopper: Problem with EWS requests to Office365 Public Folders"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/332796/showstopper-problem-with-ews-requests-to-office365
question_id: 332796
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Showstopper: Problem with EWS requests to Office365 Public Folders

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/332796/showstopper-problem-with-ews-requests-to-office365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys,

approximately 2 days ago our customers clashed with 2 problems during access to Office 365 Public Folders via EWS API.  

One of problem is described here  

https://github.com/OfficeDev/ews-managed-api/issues/263  

when enumerating public folders:  

****An internal server error occurred. The operation failed., Unable to cast object of type 'Microsoft.Exchange.Data.Storage.PublicFolderSession' to type 'Microsoft.Exchange.Data.Storage.IMailboxSession'.****

Can someone explain what does it means? And why it happened now - because earlier all worked correctly.

2nd problem with EWS PullSubscriptionRequest on Office 365 Public Folder.  

More exactly problem happens on the next call of GetEvents - it returns ErrorNoRespondingCASInDestinationSite.

Earlier all worked perfectly and this happened 2 days ago. I started researching and found such info  

https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-maintain-affinity-between-group-of-subscriptions-and-mailbox-server?redirectedfrom=MSDN

They describe that for notification subscriptions it's necessary to use HTTP headers  

X-AnchorMailbox, X-PreferServerAffinity and X-BackEndOverrideCookie.

But we already use X-AnchorMailbox - we use it along with <ExchangeImpersonation> node and set it in the same value - <PrimarySmtpAddress>.  

But PrimarySmtpAddress for ExchangeImpersonation it's always user-mailbox address, not PublicFolder.  

Then I also found such info  

https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-route-public-folder-hierarchy-requests

So I tried to use as X-AnchorMailbox in GetEvents request the value from Autodiscover response in node  

Account/PublicFolderInformation/SmtpAddress - this value looks like AllPublicFolders?Office365?_fdbae65d@...  

After this the error ErrorNoRespondingCASInDestinationSite disappeared BUT no any notifications are returned.  

I use only X-AnchorMailbox -> so I wanted to try also X-PreferServerAffinity and X-BackEndOverrideCookie as they describe BUT <PullSubscriptionRequest> does not return any X-BackEndOverrideCookie.

So I have several questions on this 2nd problem:  

-  Do I understand correct that ErrorNoRespondingCASInDestinationSite started hapenning 2 days ago because CAS server for user-mailbox (which account we use to connect to Office 365) was changed and now is not the same as for PublicFolder ?  

-  How correctly to form EWS requests to Public Folders  

a) Is ExchangeImpersonation necessary? If yes - what address to use (we use SMTP-addr of user who connects to Office 365) ?  

b) what address to use in X-AnchorMailbox ?  

c) is X-AnchorMailbox enough (because X-BackEndOverrideCookie is not returned by PullSubscriptionRequest)  

d) if I use these 2 EWS requests correctly - PullSubscriptionRequest and GetEvents - i.e. use  

ExchangeImpersonation/ConnectingSID/PrimarySmtpAddress = admin365@...  

and  

X-AnchorMailbox = AllPublicFolders?Office365?_fdbae65d@...  

WHY I stopped to get any notifications

Any help highly appreciated.

## Answers

_No answers on this thread._
