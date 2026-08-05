---
title: "Transport Rule Agent placing messages in Poison queue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/269329/transport-rule-agent-placing-messages-in-poison-qu
question_id: 269329
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Transport Rule Agent placing messages in Poison queue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/269329/transport-rule-agent-placing-messages-in-poison-qu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Having a weird problem. It seems the Transport Rule Agent on an Exchange 2019 server is causing messages to sporadically be placed in the Poison queue. It is not nearly every message going through this one server. This DAG of 2019 servers is very new in an Exchange 2013 environment. Things that I’ve tried:  

-  Disabling the Transport Rule Agent gets the messages out of the queue and on to their destination, but when I re-enable it, the behavior continues.  

-  Found this link that mentions files missing from the %ExchangeInstallPath%FIP-FS\Data\Engines\amd64 folder. I saw that it was different from servers in the same DAG. Made them the same and restarted a couple of services, to include MSExchangeTransport. Also restarted server. This did not work.  

-  Tried changing permissions on registry key mentioned below, to no avail.  

-  Disabled the specific transport rule mentioned in Event 4010 and no change.  

I’m trying to figure out which Exchange log I should be looking at. I assume it should be under the TransportRoles\Logs\Hub folder since messages get put in the Poison queue and they get put there after going through the transport agents. When I run “Set-TransportService,” which logs should I make sure are enabled and set to the highest level of logging? When I look through the Application log in the Event Viewer, I see a couple of different events that look like they could be relevant information, which is as follows:  

First event once a message gets put in the poison queue as far as I can tell: “Event 10001 – Source: MSExchangeTransport – Task Category: PoisonMessage – Message: X messages have reached or exceeded the configured poison threshold of 2. After the Microsoft Exchange Transport service restarted, these messages were moved to the poison message queue.”  

Event 4010 – Source: MSExchange Messaging Policies – Task Category: Rules – Message: Transport engine failed to evaluate condition due to Filtering Service error. The rule is configured to ignore errors. Details: Message ID [message ID]. Rule ID: [rule ID]. Predicate [predicate] Action Filtering Service Failure Exception Error: FIPS test Extraction failed with error: ‘Scanning Process caught exception: … Unknown Error 2214608899. Unable to reserve MSAM for file parsing – the engine is permanently offline’. See inner exception for details -- [big long inner exception text]  

Event 4007 – Source: MSExchange Messaging Policies – Task Category: Rules – Message: Transport engine failed to evaluate condition or apply action. [message ID][Rule ID][Predicate]. UnautheroizedAccessException Error: Access to the registry ‘HKLM\SOFTWARE\Microsoft\ExchangeServer\v15\WorkerTaskFramework\IdStore\ProbeDefinitionIDConflicts’ is denied. [long inner exception trace]  

Event 1051 – Source: MSExchange Extensibility – Task Category: MExRuntime – Message: Agent ‘Transport Rule Agent’ caused an unhandled exception ‘UnauthorizedAccessException: Access to the registry key [same key as above] is denied while handling event OnResolvedMessage.  

Event 17025 – Source: Transport – Task Category: Storage – Message: The following messages were loaded at startup before Transport crashed. To avoid further crashes, it is recommended that a New-InterceptorRule is deployed matching the values for the message that caused the Transport to crash. [message info like from, to, and subject]  

Event 4999 – Source: MSExchange Common – Task Category: General – Message: Watson report about to be sent for process id: [process id], with parameters: E12II, c-RTL-AMD64, 15.02.0792.003, edgetransport, mscorlib, M.W.RegistryKey.CreateSubKeyInternal, System.UnauthorizedAccessException, a293-dempidset, 04.08.4300.000, ErrorReportingEnabled: False  

Event 2203 – Source: FIPFS – Message: A FIP-FS Scan process returned error 0x84004003 PID: [PID] Msg: Scanning Process caught exception “Unable to reserve MSAM for file parsing – the engine is permanently offline ID: {[hex guid looking data]}”

## Answers

_No answers on this thread._
