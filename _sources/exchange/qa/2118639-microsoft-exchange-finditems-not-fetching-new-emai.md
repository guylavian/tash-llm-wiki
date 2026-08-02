---
title: "Microsoft Exchange \"findItems\" not fetching new emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118639/microsoft-exchange-finditems-not-fetching-new-emai
question_id: 2118639
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "developer-technologies-dotnet-other-l1", "office-exchange-office-exchange-server-management"]
---
# Microsoft Exchange "findItems" not fetching new emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118639/microsoft-exchange-finditems-not-fetching-new-emai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

There is some sort of a problem with an email, but I can't log error why.

I am using ExchangeVersion.Exchange2015

//Normally I am trying to get 100 emails per findItems, but if any email is "bad" I don't get any of emails...  

var itemView = new ItemView(1, 0, OffsetBasePoint.Beginning);

itemView.OrderBy.Add(ItemSchema.DateTimeReceived, SortDirection.Descending);

FindItemsResults<Item> findResults = service.FindItems(WellKnownFolderName.Inbox, filter, itemView).Result;

And I get error:  

Name cannot begin with the '<' character, hexadecimal value 0x3C. Line 1, position 23012.

I have enabled tracer:

service.TraceEnabled = true;

service.TraceFlags = TraceFlags.All;

service.TraceListener = new EwsReaderTraceListener();

public void Trace(string traceType, string traceMessage)

{

```
_log.Information("");

 _log.Information("EWS_TRACING_BEGINS");

 _log.Information(traceType);

 _log.Information(traceMessage);

 _log.Information("EWS_TRACING_ENDS");

 _log.Information("");
}

Debugger stops two times, one is with response of findItems being 200 and the other traceMessage says "System.IO.MemoryStream" and that's all.

If I call service.FindItems(WellKnownFolderName.Inbox, filter, itemView) it works

If I call service.FindItems(WellKnownFolderName.Inbox, filter, itemView) .Result it crashes

If I change sorting from "Descending" to "Ascending" then it works, which indicates that there is a problem with the newest email, but how do I catch what is the error in my tracer

Thank you all in advance :)
```

## Answers

_No answers on this thread._
