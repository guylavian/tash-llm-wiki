---
title: "Exchange 2007 to Exchange 2013 MailBox Migration Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2748624/exchange-2007-to-exchange-2013-mailbox-migration-e
question_id: 2748624
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Exchange 2007 to Exchange 2013 MailBox Migration Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2748624/exchange-2007-to-exchange-2013-mailbox-migration-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When i try to migrate mailboxes from my old Exchange 2007 to Exchange 2013 it shows the following error

++++++++++++++++++++

Error: MigrationTransientException: MapiExceptionNetworkError: Unable to make connection to the server. ‎(hr=0x80040115, ec=-2147221227)‎ Diagnostic context: ...... Lid: 10648 dwParam: 0x0 Msg: EEInfo: Generating component: 2 Lid: 14744 dwParam: 0x0 Msg:
 EEInfo: Status: 1753 Lid: 9624 dwParam: 0x0 Msg: EEInfo: Detection location: 501 Lid: 13720 dwParam: 0x0 Msg: EEInfo: Flags: 0 Lid: 11672 dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 4 Lid: 8856 dwParam: 0x0 Msg: EEInfo: prm[0]: Unicode string: ncacn_ip_tcp
 Lid: 8856 dwParam: 0x0 Msg: EEInfo: prm[1]: Unicode string: MB.x.y Lid: 12952 dwParam: 0x0 Msg: EEInfo: prm[2]: Long val: 3749909585 Lid: 12952 dwParam: 0x0 Msg: EEInfo: prm[3]: Long val: 382312662 Lid: 45169 StoreEc: 0x824 Lid: 50544 ClientVersion: 15.0.1178.4
 Lid: 52080 StoreEc: 0x824 Lid: 44273 Lid: 49064 dwParam: 0x1 Lid: 37288 StoreEc: 0x6AB Lid: 49064 dwParam: 0x2 Lid: 59431 EMSMDB.EcDoConnectEx called [length=147] Lid: 51239 EMSMDB.EcDoConnectEx exception [rpc_status=0x6D9][latency=0] Lid: 62184 Lid: 16280
 dwParam: 0x0 Msg: EEInfo: ComputerName: n/a Lid: 8600 dwParam: 0x0 Msg: EEInfo: ProcessID: 8916 Lid: 12696 dwParam: 0x0 Msg: EEInfo: Generation Time: 0417-06-05T08:00:58.8330000Z Lid: 10648 dwParam: 0x0 Msg: EEInfo: Generating component: 2 Lid: 14744 dwParam:
 0x0 Msg: EEInfo: Status: 1753 Lid: 9624 dwParam: 0x0 Msg: EEInfo: Detection location: 501 Lid: 13720 dwParam: 0x0 Msg: EEInfo: Flags: 0 Lid: 11672 dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 4 Lid: 8856 dwParam: 0x0 Msg: EEInfo: prm[0]: Unicode string: ncacn_ip_tcp
 Lid: 8856 dwParam: 0x0 Msg: EEInfo: prm[1]: Unicode string: MB.x.y Lid: 12952 dwParam: 0x0 Msg: EEInfo: prm[2]: Long val: 2767313664 Lid: 12952 dwParam: 0x0 Msg: EEInfo: prm[3]: Long val: 382312662 Lid: 59505 StoreEc: 0x824 Lid: 50544 ClientVersion: 15.0.1178.4
 Lid: 52080 StoreEc: 0x824 Lid: 36081 Lid: 51152 Lid: 52465 StoreEc: 0x80040115 Lid: 60065 Lid: 33777 StoreEc: 0x80040115 Lid: 59805 Lid: 52487 StoreEc: 0x80040115 Lid: 19778 Lid: 27970 StoreEc: 0x80040115 Lid: 17730 Lid: 25922 StoreEc: 0x80040115 --> MapiExceptionNetworkError:
 Unable to make connection to the server. ‎(hr=0x80040115, ec=-2147221227)‎ Diagnostic context: ...... Lid: 10648 dwParam: 0x0 Msg: EEInfo: Generating component: 2 Lid: 14744 dwParam: 0x0 Msg: EEInfo: Status: 1753 Lid: 9624 dwParam: 0x0 Msg: EEInfo: Detection
 location: 501 Lid: 13720 dwParam: 0x0 Msg: EEInfo: Flags: 0 Lid: 11672 dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 4 Lid: 8856 dwParam: 0x0 Msg: EEInfo: prm[0]: Unicode string: ncacn_ip_tcp Lid: 8856 dwParam: 0x0 Msg: EEInfo: prm[1]: Unicode string: MB.x.y
 Lid: 12952 dwParam: 0x0 Msg: EEInfo: prm[2]: Long val: 3749909585 Lid: 12952 dwParam: 0x0 Msg: EEInfo: prm[3]: Long val: 382312662 Lid: 45169 StoreEc: 0x824 Lid: 50544 ClientVersion: 15.0.1178.4 Lid: 52080 StoreEc: 0x824 Lid: 44273 Lid: 49064 dwParam: 0x1
 Lid: 37288 StoreEc: 0x6AB Lid: 49064 dwParam: 0x2 Lid: 59431 EMSMDB.EcDoConnectEx called [length=147] Lid: 51239 EMSMDB.EcDoConnectEx exception [rpc_status=0x6D9][latency=0] Lid: 62184 Lid: 16280 dwParam: 0x0 Msg: EEInfo: ComputerName: n/a Lid: 8600 dwParam:
 0x0 Msg: EEInfo: ProcessID: 8916 Lid: 12696 dwParam: 0x0 Msg: EEInfo: Generation Time: 0417-06-05T08:00:58.8330000Z Lid: 10648 dwParam: 0x0 Msg: EEInfo: Generating component: 2 Lid: 14744 dwParam: 0x0 Msg: EEInfo: Status: 1753 Lid: 9624 dwParam: 0x0 Msg: EEInfo:
 Detection location: 501 Lid: 13720 dwParam: 0x0 Msg: EEInfo: Flags: 0 Lid: 11672 dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 4 Lid: 8856 dwParam: 0x0 Msg: EEInfo: prm[0]: Unicode string: ncacn_ip_tcp Lid: 8856 dwParam: 0x0 Msg: EEInfo: prm[1]: Unicode string:
 MB.x.y Lid: 12952 dwParam: 0x0 Msg: EEInfo: prm[2]: Long val: 2767313664 Lid: 12952 dwParam: 0x0 Msg: EEInfo: prm[3]: Long val: 382312662 Lid: 59505 StoreEc: 0x824 Lid: 50544 ClientVersion: 15.0.1178.4 Lid: 52080 StoreEc: 0x824 Lid: 36081 Lid: 51152 Lid: 52465
 StoreEc: 0x80040115 Lid: 60065 Lid: 33777 StoreEc: 0x80040115 Lid: 59805 Lid: 52487 StoreEc: 0x80040115 Lid: 19778 Lid: 27970 StoreEc: 0x80040115 Lid: 17730 Lid: 25922 StoreEc: 0x80040115

++++++++++++++++++++

What seems to be the wrong. I like to add here, both are them are in same under same series of IP.

## Answers

_No answers on this thread._
