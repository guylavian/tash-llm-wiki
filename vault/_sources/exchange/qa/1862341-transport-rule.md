---
title: "Transport rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1862341/transport-rule
question_id: 1862341
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
---
# Transport rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1862341/transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,I have an external domain, let's say contoso.com. All emails from this domain and its subdomains should reach all my users' Focused Inbox, not the Other Inbox. This requirement applies only to this domain and its subdomains, not to any other domains. I came across this article, and I'm wondering if the following transport rule will work for me

https://learn.microsoft.com/en-us/microsoft-365/admin/setup/configure-focused-inbox?view=o365-worldwide#use-the-ui-to-create-a-transport-rule-to-direct-email-messages-to-the-focused-view-for-all-your-users

```
New-TransportRule -Name "Bypass Focused Inbox for contoso.com domain" -FromAddressMatchesPatterns "@contoso\.com$|@.*\.contoso\.com$" -SetHeaderName "X-MS-Exchange-Organization-BypassFocusedInbox" -SetHeaderValue "true"
```

## Answers

_No answers on this thread._
