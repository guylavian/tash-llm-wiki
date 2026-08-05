---
title: "[Migrated from MSDN Exchange Dev] search-mailbox query not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/203186/migrated-from-msdn-exchange-dev-search-mailbox-que
question_id: 203186
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] search-mailbox query not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/203186/migrated-from-msdn-exchange-dev-search-mailbox-que (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/27a9088c-39ff-4c61-9aca-a12680f5a5e0/searchmailbox-query-not-working?forum=exchangesvrdevelopment    

I have a search query     

search-mailbox -id name -searchquery {received >'5/1/2020' and from:'pkginfo@RayHolte  .com'} -logonly -targetmailbox test    

It returned 0 result. I know there are many emails match the criteria. if i use     

search-mailbox -id name -searchquery  from:'pkginfo@RayHolte  .com' -logonly -targetmailbox test    

I got 10000 items. search-mailbox search query is tricky. What could be wrong?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Hi，    

Please try to add parentheses in searchquery:    

```
search-mailbox -id administrator  -searchquery '(from:******@contoso.com)AND (received >01/01/2020)' -logonly -targetmailbox ******@contoso.com -targetfolder test
```

Post the error information if you got any other issues again.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
