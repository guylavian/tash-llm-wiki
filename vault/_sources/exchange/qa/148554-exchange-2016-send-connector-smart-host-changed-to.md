---
title: "Exchange 2016 send connector smart host changed to MX records"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/148554/exchange-2016-send-connector-smart-host-changed-to
question_id: 148554
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 send connector smart host changed to MX records

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/148554/exchange-2016-send-connector-smart-host-changed-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 send connector configured to send through smart host at ISP. In an effort to troubleshoot some delivery problems to a specific domain, we want to bypass the ISP replays and change the send connector to send via MX records. An nslookup on exchange seems to be returning the correct data so i expect the mail should flow out fine.   

When i make the change on the send connector, will the existing smart host settings be retained by exchange? Should i document the settings first in case i have to reconfigure it from scratch?   

That said, once i have made changes to the send connctor do i need to restart the transport service?

## Answers

_No answers on this thread._
