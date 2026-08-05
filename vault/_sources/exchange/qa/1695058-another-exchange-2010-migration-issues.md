---
title: "Another Exchange 2010 migration issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1695058/another-exchange-2010-migration-issues
question_id: 1695058
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Another Exchange 2010 migration issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1695058/another-exchange-2010-migration-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

More issues trying to migrate mailboxes from Exchange 2010 over a slow link. Previously managed to migrate a few mailboxes off this server, but now the remaining few are problematic. This is the cmd I run and the error received. The mailboxes are still sending and receiving emails, so no issues with the server itself, so don’t understand the error with regards not being able to connect to the source mailbox. No firewall issues either? Any ideas on what to try?

CMD

Get-MoveRequestStatistics ******@domain.com -IncludeReport | Export-Clixml c:\temp\SPS.xml

stats = Import-Clixml c:\temp\SPS.xml

stats.report.failures[-1]

 

ERROR

Timestamp         : 6/12/2024 6:51:30 AM

FailureType       : SourceMailboxConnectionStalePermanentException

FailureCode       : -2146233088

MapiLowLevelError : 0

FailureSide       : Source

FailureSideInt    : 1

ExceptionTypes    : {Exchange, MRS, MRSPermanent}

ExceptionTypesInt : {1, 10, 12}

Message           : Couldn't connect to the source mailbox. --> MapiExceptionNetworkError: Unable to make connection to the server.

                    (hr=0x80004005, ec=2423)

                    Diagnostic context:

                        ......

                        Lid: 14744   dwParam: 0x0 Msg: EEInfo: Status: 1722

                        Lid: 9624    dwParam: 0x0 Msg: EEInfo: Detection location: 323

                        Lid: 13720   dwParam: 0x0 Msg: EEInfo: Flags: 0

                        Lid: 11672   dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 0

                        Lid: 62184

                        Lid: 16280   dwParam: 0x0 Msg: EEInfo: ComputerName: n/a

                        Lid: 8600    dwParam: 0x0 Msg: EEInfo: ProcessID: 29760

                        Lid: 12696   dwParam: 0x0 Msg: EEInfo: Generation Time: 0424-06-12T06:51:30.1800000Z

                        Lid: 10648   dwParam: 0x0 Msg: EEInfo: Generating component: 18

                        Lid: 14744   dwParam: 0x0 Msg: EEInfo: Status: 1237

                        Lid: 9624    dwParam: 0x0 Msg: EEInfo: Detection location: 313

                        Lid: 13720   dwParam: 0x0 Msg: EEInfo: Flags: 0

                        Lid: 11672   dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 0

                        Lid: 62184

                        Lid: 16280   dwParam: 0x0 Msg: EEInfo: ComputerName: n/a

                        Lid: 8600    dwParam: 0x0 Msg: EEInfo: ProcessID: 29760

                        Lid: 12696   dwParam: 0x0 Msg: EEInfo: Generation Time: 0424-06-12T06:51:30.1800000Z

                        Lid: 10648   dwParam: 0x0 Msg: EEInfo: Generating component: 18

                        Lid: 14744   dwParam: 0x0 Msg: EEInfo: Status: 10060

                        Lid: 9624    dwParam: 0x0 Msg: EEInfo: Detection location: 311

                        Lid: 13720   dwParam: 0x0 Msg: EEInfo: Flags: 0

                        Lid: 11672   dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 3

                        Lid: 12952   dwParam: 0x0 Msg: EEInfo: prm[0]: Long val: 24489

                        Lid: 15000   dwParam: 0x0 Msg: EEInfo: prm[1]: Pointer val: 0x0

                        Lid: 15000   dwParam: 0x0 Msg: EEInfo: prm[2]: Pointer val: 0x1703D80A00000000

                        Lid: 62184

                        Lid: 16280   dwParam: 0x0 Msg: EEInfo: ComputerName: n/a

                        Lid: 8600    dwParam: 0x0 Msg: EEInfo: ProcessID: 29760

                        Lid: 12696   dwParam: 0x0 Msg: EEInfo: Generation Time: 0424-06-12T06:51:30.1800000Z

                        Lid: 10648   dwParam: 0x0 Msg: EEInfo: Generating component: 18

                        Lid: 14744   dwParam: 0x0 Msg: EEInfo: Status: 10060

                        Lid: 9624    dwParam: 0x0 Msg: EEInfo: Detection location: 318

                        Lid: 13720   dwParam: 0x0 Msg: EEInfo: Flags: 0

                        Lid: 11672   dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 0

                        Lid: 53361   StoreEc: 0x977

                        Lid: 51859

                        Lid: 33649   StoreEc: 0x977

                        Lid: 43315

                        Lid: 58225   StoreEc: 0x977

                        Lid: 39912   StoreEc: 0x977

                        Lid: 54129   StoreEc: 0x977

                        Lid: 50519

                        Lid: 59735   StoreEc: 0x977

                        Lid: 59199

                        Lid: 27356   StoreEc: 0x977

                        Lid: 65279

                        Lid: 52465   StoreEc: 0x977

                        Lid: 60065

                        Lid: 33777   StoreEc: 0x977

                        Lid: 59805

                        Lid: 52487   StoreEc: 0x977

                        Lid: 19778

                        Lid: 27970   StoreEc: 0x977

                        Lid: 17730

                        Lid: 25922   StoreEc: 0x977

MessageData       :

DataContext       : --------

                    Operation: IMailbox.Connect

                    Operation: [Connect] IMailbox.Connect

                    OperationSide: Source

                    f9523820-e7a7-438a-bb1f-a7a15459f5a3 (Primary)

                    Flags: None

DataContextData   :

StackTrace        :

InnerException    : MapiExceptionNetworkError: MapiExceptionNetworkError: Unable to make connection to the server. (hr=0x80004005, ec=2423)

                    Diagnostic context:

                        ......

                        Lid: 14744   dwParam: 0x0 Msg: EEInfo: Status: 1722

                        Lid: 9624    dwParam: 0x0 Msg: EEInfo: Detection location: 323

                        Lid: 13720   dwParam: 0x0 Msg: EEInfo: Flags: 0

                        Lid: 11672   dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 0

                        Lid: 62184

                        Lid: 16280   dwParam: 0x0 Msg: EEInfo: ComputerName: n/a

                        Lid: 8600    dwParam: 0x0 Msg: EEInfo: ProcessID: 29760

                        Lid: 12696   dwParam: 0x0 Msg: EEInfo: Generation Time: 0424-06-12T06:51:30.1800000Z

                        Lid: 10648   dwParam: 0x0 Msg: EEInfo: Generating component: 18

                        Lid: 14744   dwParam: 0x0 Msg: EEInfo: Status: 1237

                        Lid: 9624    dwParam: 0x0 Msg: EEInfo: Detection location: 313

                        Lid: 13720   dwParam: 0x0 Msg: EEInfo: Flags: 0

                        Lid: 11672   dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 0

                        Lid: 62184

                        Lid: 16280   dwParam: 0x0 Msg: EEInfo: ComputerName: n/a

                        Lid: 8600    dwParam: 0x0 Msg: EEInfo: ProcessID: 29760

                        Lid: 12696   dwParam: 0x0 Msg: EEInfo: Generation Time: 0424-06-12T06:51:30.1800000Z

                        Lid: 10648   dwParam: 0x0 Msg: EEInfo: Generating component: 18

                        Lid: 14744   dwParam: 0x0 Msg: EEInfo: Status: 10060

                        Lid: 9624    dwParam: 0x0 Msg: EEInfo: Detection location: 311

                        Lid: 13720   dwParam: 0x0 Msg: EEInfo: Flags: 0

                        Lid: 11672   dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 3

                        Lid: 12952   dwParam: 0x0 Msg: EEInfo: prm[0]: Long val: 24489

                        Lid: 15000   dwParam: 0x0 Msg: EEInfo: prm[1]: Pointer val: 0x0

                        Lid: 15000   dwParam: 0x0 Msg: EEInfo: prm[2]: Pointer val: 0x1703D80A00000000

                        Lid: 62184

                        Lid: 16280   dwParam: 0x0 Msg: EEInfo: ComputerName: n/a

                        Lid: 8600    dwParam: 0x0 Msg: EEInfo: ProcessID: 29760

                        Lid: 12696   dwParam: 0x0 Msg: EEInfo: Generation Time: 0424-06-12T06:51:30.1800000Z

                        Lid: 10648   dwParam: 0x0 Msg: EEInfo: Generating component: 18

                        Lid: 14744   dwParam: 0x0 Msg: EEInfo: Status: 10060

                        Lid: 9624    dwParam: 0x0 Msg: EEInfo: Detection location: 318

                        Lid: 13720   dwParam: 0x0 Msg: EEInfo: Flags: 0

                        Lid: 11672   dwParam: 0x0 Msg: EEInfo: NumberOfParameters: 0

                        Lid: 53361   StoreEc: 0x977

                        Lid: 51859

                        Lid: 33649   StoreEc: 0x977

                        Lid: 43315

                        Lid: 58225   StoreEc: 0x977

                        Lid: 39912   StoreEc: 0x977

                        Lid: 54129   StoreEc: 0x977

                        Lid: 50519

                        Lid: 59735   StoreEc: 0x977

                        Lid: 59199

                        Lid: 27356   StoreEc: 0x977

                        Lid: 65279

                        Lid: 52465   StoreEc: 0x977

                        Lid: 60065

                        Lid: 33777   StoreEc: 0x977

                        Lid: 59805

                        Lid: 52487   StoreEc: 0x977

                        Lid: 19778

                        Lid: 27970   StoreEc: 0x977

                        Lid: 17730

                        Lid: 25922   StoreEc: 0x977

UnknownElements   :

UnknownAttributes :

## Answers

_No answers on this thread._
