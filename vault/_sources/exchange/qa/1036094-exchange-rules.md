---
title: "Exchange rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1036094/exchange-rules
question_id: 1036094
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1036094/exchange-rules (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Trying to block incoming empty emails at Exchange Admin Center more precise at Mail flow > Rule.    

This is the regex pattern to detect in subject or body:    

```
[\r\n]*[\r\n]*.*
[\r\n]*[\r\n]*[\r\n]*[\r\n]*
```

Tested the rule on this website https://regexr.com/ and it works against the following html code:    

    <p></p>  

    <div>  

    <div dir="ltr"><br>  

    </div>  

    </div>  

    </body>  

    </html>  

But seems not to work on the test empty emails.    

Does any one knows an effective way to block empty emails?    

Cheers,    

Gonkas

## Answers

_No answers on this thread._
