---
title: "Why is there so much problems with my exchange server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304050/why-is-there-so-much-problems-with-my-exchange-ser
question_id: 304050
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Why is there so much problems with my exchange server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304050/why-is-there-so-much-problems-with-my-exchange-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I don't understand why but when I made my exchange server a bunch of problems showed up and stopped me from being able to receive and send emails to external emails. The problem are:  

GLOBEEXCHANGE	4999	Error	MSExchange Common	Application	3/8/2021 10:37:03 AM  

GLOBEEXCHANGE	139	Error	MSExchange OWA	Application	3/8/2021 10:36:58 AM  

GLOBEEXCHANGE	6027	Error	Microsoft-Filtering-FIPFS	Application	3/8/2021 10:36:46 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 10:35:38 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:35:26 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 10:35:19 AM  

GLOBEEXCHANGE	6027	Error	Microsoft-Filtering-FIPFS	Application	3/8/2021 10:34:05 AM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/8/2021 10:29:29 AM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/8/2021 10:29:29 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 10:29:28 AM  

GLOBEEXCHANGE	10154	Warning	Microsoft-Windows-Windows Remote Management	System	3/8/2021 10:29:16 AM  

GLOBEEXCHANGE	1032	Error	MSExchangeDiagnostics	Application	3/8/2021 10:29:12 AM  

GLOBEEXCHANGE	6027	Error	Microsoft-Filtering-FIPFS	Application	3/8/2021 10:29:08 AM  

GLOBEEXCHANGE	6038	Warning	Microsoft-Windows-LSA	System	3/8/2021 10:28:31 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 10:28:15 AM  

GLOBEEXCHANGE	1076	Warning	User32	System	3/8/2021 10:28:01 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 10:27:59 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 10:27:59 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 10:27:31 AM  

GLOBEEXCHANGE	2001	Error	MSExchange Certificate Notification	Application	3/8/2021 10:27:14 AM  

GLOBEEXCHANGE	4002	Error	MSExchange AuditLogSearch	Application	3/8/2021 10:27:14 AM  

GLOBEEXCHANGE	12025	Warning	MSExchangeTransport	Application	3/8/2021 10:27:04 AM  

GLOBEEXCHANGE	6006	Warning	Microsoft-Windows-Winlogon	Application	3/8/2021 10:27:03 AM  

GLOBEEXCHANGE	6005	Warning	Microsoft-Windows-Winlogon	Application	3/8/2021 10:26:55 AM  

GLOBEEXCHANGE	1006	Warning	FfoSystemProbe	Application	3/8/2021 10:26:53 AM  

GLOBEEXCHANGE	1621	Warning	MSExchange Unified Messaging	Application	3/8/2021 10:26:51 AM  

GLOBEEXCHANGE	16024	Error	MSExchangeSubmission	Application	3/8/2021 10:26:50 AM  

GLOBEEXCHANGE	40034	Warning	MSExchangeIS	Application	3/8/2021 10:26:43 AM  

GLOBEEXCHANGE	2142	Error	MSExchangeADTopology	Application	3/8/2021 10:26:39 AM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/8/2021 10:26:34 AM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/8/2021 10:26:34 AM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/8/2021 10:26:33 AM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/8/2021 10:26:25 AM  

GLOBEEXCHANGE	12	Warning	Microsoft-Windows-Time-Service	System	3/8/2021 10:26:24 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 10:25:58 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 10:25:58 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:25:58 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 10:25:57 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 10:25:57 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:25:56 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:25:56 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:25:55 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 10:25:37 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:23:37 AM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/8/2021 10:23:25 AM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/8/2021 10:23:25 AM  

GLOBEEXCHANGE	10154	Warning	Microsoft-Windows-Windows Remote Management	System	3/8/2021 10:22:30 AM  

GLOBEEXCHANGE	1032	Error	MSExchangeDiagnostics	Application	3/8/2021 10:22:25 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 10:22:25 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 10:22:22 AM  

GLOBEEXCHANGE	6038	Warning	Microsoft-Windows-LSA	System	3/8/2021 10:22:18 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 10:21:13 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:21:11 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 10:21:06 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 10:20:58 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 10:20:42 AM  

GLOBEEXCHANGE	2001	Error	MSExchange Certificate Notification	Application	3/8/2021 10:20:36 AM  

GLOBEEXCHANGE	4002	Error	MSExchange AuditLogSearch	Application	3/8/2021 10:20:36 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 10:20:31 AM  

GLOBEEXCHANGE	12025	Warning	MSExchangeTransport	Application	3/8/2021 10:20:24 AM  

GLOBEEXCHANGE	1621	Warning	MSExchange Unified Messaging	Application	3/8/2021 10:20:06 AM  

GLOBEEXCHANGE	6006	Warning	Microsoft-Windows-Winlogon	Application	3/8/2021 10:20:06 AM  

GLOBEEXCHANGE	6005	Warning	Microsoft-Windows-Winlogon	Application	3/8/2021 10:20:03 AM  

GLOBEEXCHANGE	1006	Warning	FfoSystemProbe	Application	3/8/2021 10:20:02 AM  

GLOBEEXCHANGE	1007	Warning	MSExchange Mailbox Replication	Application	3/8/2021 10:20:00 AM  

GLOBEEXCHANGE	16024	Error	MSExchangeSubmission	Application	3/8/2021 10:20:00 AM  

GLOBEEXCHANGE	40034	Warning	MSExchangeIS	Application	3/8/2021 10:19:58 AM  

GLOBEEXCHANGE	2142	Error	MSExchangeADTopology	Application	3/8/2021 10:19:44 AM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/8/2021 10:19:32 AM  

GLOBEEXCHANGE	12	Warning	Microsoft-Windows-Time-Service	System	3/8/2021 10:19:31 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 10:19:04 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 10:19:04 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:19:03 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:19:03 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:19:02 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 10:19:02 AM  

GLOBEEXCHANGE	6008	Error	EventLog	System	3/8/2021 10:19:02 AM  

GLOBEEXCHANGE	41	Critical	Microsoft-Windows-Kernel-Power	System	3/8/2021 10:18:58 AM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/8/2021 8:26:40 AM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/8/2021 8:26:40 AM  

GLOBEEXCHANGE	10154	Warning	Microsoft-Windows-Windows Remote Management	System	3/8/2021 8:26:32 AM  

GLOBEEXCHANGE	1032	Error	MSExchangeDiagnostics	Application	3/8/2021 8:26:00 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 8:25:57 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 8:25:21 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 8:25:17 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 8:25:15 AM  

GLOBEEXCHANGE	6038	Warning	Microsoft-Windows-LSA	System	3/8/2021 8:25:15 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 8:25:13 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 8:24:59 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 8:24:50 AM  

GLOBEEXCHANGE	4002	Error	MSExchange AuditLogSearch	Application	3/8/2021 8:24:43 AM  

GLOBEEXCHANGE	2001	Error	MSExchange Certificate Notification	Application	3/8/2021 8:24:43 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 8:24:38 AM  

GLOBEEXCHANGE	12025	Warning	MSExchangeTransport	Application	3/8/2021 8:24:29 AM  

GLOBEEXCHANGE	6006	Warning	Microsoft-Windows-Winlogon	Application	3/8/2021 8:24:13 AM  

GLOBEEXCHANGE	1006	Warning	FfoSystemProbe	Application	3/8/2021 8:24:10 AM  

GLOBEEXCHANGE	6005	Warning	Microsoft-Windows-Winlogon	Application	3/8/2021 8:24:09 AM  

GLOBEEXCHANGE	16024	Error	MSExchangeSubmission	Application	3/8/2021 8:24:07 AM  

GLOBEEXCHANGE	40034	Warning	MSExchangeIS	Application	3/8/2021 8:24:06 AM  

GLOBEEXCHANGE	1621	Warning	MSExchange Unified Messaging	Application	3/8/2021 8:24:06 AM  

GLOBEEXCHANGE	2142	Error	MSExchangeADTopology	Application	3/8/2021 8:23:52 AM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/8/2021 8:23:38 AM  

GLOBEEXCHANGE	12	Warning	Microsoft-Windows-Time-Service	System	3/8/2021 8:23:38 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 8:23:10 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 8:23:10 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 8:23:10 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 8:23:10 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 8:23:09 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 8:23:09 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 8:21:53 AM  

GLOBEEXCHANGE	12025	Warning	MSExchangeTransport	Application	3/8/2021 8:13:54 AM  

GLOBEEXCHANGE	1008	Error	Microsoft-Windows-Perflib	Application	3/8/2021 8:13:52 AM  

GLOBEEXCHANGE	2004	Error	Microsoft-Windows-PerfNet	Application	3/8/2021 8:13:52 AM  

GLOBEEXCHANGE	1008	Error	Microsoft-Windows-Perflib	Application	3/8/2021 8:13:52 AM  

GLOBEEXCHANGE	1008	Error	Microsoft-Windows-Perflib	Application	3/8/2021 8:13:52 AM  

GLOBEEXCHANGE	1009	Warning	MSExchangeFastSearch	Application	3/8/2021 7:43:18 AM  

GLOBEEXCHANGE	10154	Warning	Microsoft-Windows-Windows Remote Management	System	3/8/2021 7:41:14 AM  

GLOBEEXCHANGE	1032	Error	MSExchangeDiagnostics	Application	3/8/2021 7:41:09 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 7:41:08 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 7:40:47 AM  

GLOBEEXCHANGE	6038	Warning	Microsoft-Windows-LSA	System	3/8/2021 7:40:43 AM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/8/2021 7:40:20 AM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/8/2021 7:40:20 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 7:40:00 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 7:40:00 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 7:39:59 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 7:39:50 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 7:39:47 AM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/8/2021 7:39:41 AM  

GLOBEEXCHANGE	12025	Warning	MSExchangeTransport	Application	3/8/2021 7:38:59 AM  

GLOBEEXCHANGE	1006	Warning	FfoSystemProbe	Application	3/8/2021 7:38:44 AM  

GLOBEEXCHANGE	16024	Error	MSExchangeSubmission	Application	3/8/2021 7:38:38 AM  

GLOBEEXCHANGE	1621	Warning	MSExchange Unified Messaging	Application	3/8/2021 7:38:38 AM  

GLOBEEXCHANGE	40034	Warning	MSExchangeIS	Application	3/8/2021 7:38:37 AM  

GLOBEEXCHANGE	2142	Error	MSExchangeADTopology	Application	3/8/2021 7:38:26 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 7:38:16 AM  

GLOBEEXCHANGE	12	Warning	Microsoft-Windows-Time-Service	System	3/8/2021 7:38:11 AM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/8/2021 7:38:11 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 7:38:05 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 7:38:05 AM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/8/2021 7:37:54 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 7:37:52 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 7:37:43 AM  

GLOBEEXCHANGE	10149	Warning	Microsoft-Windows-Windows Remote Management	System	3/8/2021 7:37:26 AM  

GLOBEEXCHANGE	1003	Error	MSExchange Front End HTTP Proxy	Application	3/8/2021 7:37:26 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 7:37:24 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 7:16:20 AM  

GLOBEEXCHANGE	4	Error	MSExchange Control Panel	Application	3/8/2021 7:12:28 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 7:12:16 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 7:12:16 AM  

GLOBEEXCHANGE	4	Error	MSExchange Control Panel	Application	3/8/2021 7:11:58 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 7:11:55 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 7:11:55 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 7:11:49 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 7:11:49 AM  

GLOBEEXCHANGE	4999	Error	MSExchange Common	Application	3/8/2021 7:11:44 AM  

GLOBEEXCHANGE	74	Error	MSExchange RBAC	Application	3/8/2021 6:54:10 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:40:26 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:40:26 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:40:26 AM  

GLOBEEXCHANGE	906	Warning	ESE	Application	3/8/2021 6:37:18 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:36:26 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:36:26 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:36:26 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:34:26 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:34:26 AM  

GLOBEEXCHANGE	9009	Warning	Microsoft-Windows-IIS-APPHOSTSVC	System	3/8/2021 6:32:26 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 6:20:13 AM  

GLOBEEXCHANGE	7031	Error	Microsoft-Windows-Service Control Manager	System	3/8/2021 6:20:10 AM  

GLOBEEXCHANGE	7031	Error	Microsoft-Windows-Service Control Manager	System	3/8/2021 6:20:10 AM  

GLOBEEXCHANGE	1000	Error	Application Error	Application	3/8/2021 6:19:56 AM  

GLOBEEXCHANGE	4999	Error	MSExchange Common	Application	3/8/2021 6:19:04 AM  

GLOBEEXCHANGE	1039	Warning	MSExchangeHMHost	Application	3/8/2021 6:18:33 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 6:18:13 AM  

GLOBEEXCHANGE	3008	Warning	MSExchange Front End HTTP Proxy	Application	3/8/2021 6:17:48 AM  

GLOBEEXCHANGE	4404	Error	MSExchangeRepl	Application	3/8/2021 6:17:48 AM  

GLOBEEXCHANGE	3008	Warning	MSExchange Front End HTTP Proxy	Application	3/8/2021 6:17:48 AM  

GLOBEEXCHANGE	3008	Warning	MSExchange Front End HTTP Proxy	Application	3/8/2021 6:17:48 AM  

GLOBEEXCHANGE	3008	Warning	MSExchange Front End HTTP Proxy	Application	3/8/2021 6:17:48 AM  

GLOBEEXCHANGE	6027	Error	Microsoft-Filtering-FIPFS	Application	3/8/2021 6:17:47 AM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/8/2021 1:38:10 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 1:34:34 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 1:34:34 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 1:34:13 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 1:34:13 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 1:34:06 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 1:34:06 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/8/2021 12:55:26 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 12:34:34 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 12:34:34 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 12:34:13 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 12:34:13 AM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/8/2021 12:34:07 AM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/8/2021 12:34:07 AM  

GLOBEEXCHANGE	4999	Error	MSExchange Common	Application	3/8/2021 12:28:56 AM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/7/2021 11:36:50 PM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/7/2021 11:34:34 PM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/7/2021 11:34:34 PM  

GLOBEEXCHANGE	3042	Warning	MSExchangeApplicationLogic	Application	3/7/2021 11:34:34 PM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/7/2021 11:34:15 PM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/7/2021 11:34:15 PM  

GLOBEEXCHANGE	3025	Error	MSExchangeApplicationLogic	Application	3/7/2021 11:34:15 PM  

GLOBEEXCHANGE	3018	Error	MSExchangeApplicationLogic	Application	3/7/2021 11:34:15 PM  

GLOBEEXCHANGE	3042	Warning	MSExchangeApplicationLogic	Application	3/7/2021 11:34:13 PM  

GLOBEEXCHANGE	3042	Warning	MSExchangeApplicationLogic	Application	3/7/2021 11:34:07 PM  

GLOBEEXCHANGE	906	Warning	ESE	Application	3/7/2021 10:59:33 PM  

GLOBEEXCHANGE	1008	Error	Microsoft-Windows-Perflib	Application	3/7/2021 10:57:56 PM  

GLOBEEXCHANGE	7023	Error	Microsoft-Windows-Service Control Manager	System	3/7/2021 10:57:34 PM  

GLOBEEXCHANGE	7023	Error	Microsoft-Windows-Service Control Manager	System	3/7/2021 10:57:34 PM  

GLOBEEXCHANGE	7023	Error	Microsoft-Windows-Service Control Manager	System	3/7/2021 10:57:34 PM  

GLOBEEXCHANGE	7023	Error	Microsoft-Windows-Service Control Manager	System	3/7/2021 10:52:34 PM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/7/2021 10:47:43 PM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/7/2021 10:47:43 PM  

GLOBEEXCHANGE	5009	Warning	Microsoft-Windows-WAS	System	3/7/2021 10:46:37 PM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/7/2021 10:39:43 PM  

GLOBEEXCHANGE	1033	Warning	MSExchange ActiveSync	Application	3/7/2021 10:39:43 PM  

GLOBEEXCHANGE	6038	Warning	Microsoft-Windows-LSA	System	3/7/2021 10:39:04 PM  

GLOBEEXCHANGE	10016	Error	Microsoft-Windows-DistributedCOM	System	3/7/2021 10:37:41 PM  

GLOBEEXCHANGE	6003	Error	MSExchange Common	Application	3/7/2021 10:36:15 PM  

GLOBEEXCHANGE	10154	Warning	Microsoft-Windows-Windows Remote Management	System	3/7/2021 10:36:13 PM  

GLOBEEXCHANGE	1032	Error	MSExchangeDiagnostics	Application	3/7/2021 10:36:06 PM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/7/2021 10:35:46 PM  

GLOBEEXCHANGE	4999	Error	MSExchange Common	Application	3/7/2021 10:35:40 PM  

GLOBEEXCHANGE	139	Error	MSExchange OWA	Application	3/7/2021 10:35:37 PM  

GLOBEEXCHANGE	7031	Error	Microsoft-Windows-Service Control Manager	System	3/7/2021 10:35:06 PM  

GLOBEEXCHANGE	1000	Error	Application Error	Application	3/7/2021 10:35:02 PM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/7/2021 10:35:00 PM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/7/2021 10:34:50 PM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/7/2021 10:34:34 PM  

GLOBEEXCHANGE	1014	Warning	Microsoft-Windows-DNS Client Events	System	3/7/2021 10:34:33 PM  

GLOBEEXCHANGE	1022	Warning	MSExchangeFrontEndTransport	Application	3/7/2021 10:34:32 PM  

GLOBEEXCHANGE	8198	Error	Microsoft-Windows-Security-SPP	Application	3/7/2021 10:34:29 PM  

GLOBEEXCHANGE	12025	Warning	MSExchangeTransport	Application	3/7/2021 10:34:28 PM  

GLOBEEXCHANGE	1009	Warning	MSExchangeFastSearch	Application	3/7/2021 10:34:10 PM  

GLOBEEXCHANGE	1006	Warning	MSExchangeFastSearch	Application	3/7/2021 10:34:10 PM  

GLOBEEXCHANGE	7004	Warning	MSExchangeFrontEndTransport	Application	3/7/2021 10:33:55 PM  

GLOBEEXCHANGE	6006	Warning	Microsoft-Windows-Winlogon	Application	3/7/2021 10:33:47 PM  

GLOBEEXCHANGE	1010	Warning	MSExchangeFastSearch	Application	3/7/2021 10:33:47 PM  

GLOBEEXCHANGE	1006	Warning	FfoSystemProbe	Application	3/7/2021 10:33:45 PM  

GLOBEEXCHANGE	7004	Warning	MSExchangeTransportSubmission	Application	3/7/2021 10:33:44 PM  

GLOBEEXCHANGE	1621	Warning	MSExchange Unified Messaging	Application	3/7/2021 10:33:44 PM  

GLOBEEXCHANGE	7010	Warning	MSExchangeTransportSubmission	Application	3/7/2021 10:33:44 PM  

GLOBEEXCHANGE	7004	Warning	MSExchangeTransportDelivery	Application	3/7/2021 10:33:36 PM  

GLOBEEXCHANGE	7010	Warning	MSExchangeFrontEndTransport	Application	3/7/2021 10:33:36 PM  

GLOBEEXCHANGE	1007	Warning	MSExchange Mailbox Replication	Application	3/7/2021 10:33:35 PM  

GLOBEEXCHANGE	1007	Warning	MSExchange Mailbox Replication	Application	3/7/2021 10:33:35 PM  

GLOBEEXCHANGE	16024	Error	MSExchangeSubmission	Application	3/7/2021 10:33:35 PM  

GLOBEEXCHANGE	1007	Warning	MSExchange Mailbox Replication	Application	3/7/2021 10:33:35 PM  

GLOBEEXCHANGE	7010	Warning	MSExchangeTransportDelivery	Application	3/7/2021 10:33:33 PM  

GLOBEEXCHANGE	40034	Warning	MSExchangeIS	Application	3/7/2021 10:33:32 PM  

GLOBEEXCHANGE	6005	Warning	Microsoft-Windows-Winlogon	Application	3/7/2021 10:33:28 PM  

GLOBEEXCHANGE	2142	Error	MSExchangeADTopology	Application	3/7/2021 10:33:16 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:06 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:05 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:05 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:05 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:05 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:05 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:05 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:05 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:04 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:02 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:02 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:02 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:02 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:02 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:02 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:02 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:33:01 PM  

GLOBEEXCHANGE	4027	Error	MSExchange ADAccess	Application	3/7/2021 10:32:59 PM  

GLOBEEXCHANGE	12	Warning	Microsoft-Windows-Time-Service	System	3/7/2021 10:32:58 PM  

GLOBEEXCHANGE	1023	Error	Microsoft-Windows-Perflib	Application	3/7/2021 3:34:38 PM  

GLOBEEXCHANGE	1023	Error	Microsoft-Windows-Perflib	Application	3/7/2021 3:34:38 PM  

GLOBEEXCHANGE	1023	Error	Microsoft-Windows-Perflib	Application	3/7/2021 3:34:38 PM  

GLOBEEXCHANGE	3008	Warning	MSExchange Front End HTTP Proxy	Application	3/7/2021 3:34:36 PM  

Please help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-09*

Hi,    

Which CU are you using?     

Do you have a send connector created as this doc suggests? Are the default receive connectors correctly configured? You can view the default settings here: Receive connectors    

You said it can't receive and send mails externally, does the mail sender get any NDR message? Track the message in powershell and post the results with personal information covered: Search message tracking logs    

Let's start with error 4027:    

-  Initially, check if any Windows firewall rule is blocking a certain port.    

-  Secondly, make sure that you don’t have any kind of trouble in allowing other computers to communicate with your computer through Windows Firewall. You can try using the Incoming Connections troubleshooter to automatically find and fix some common problems.    

-  Check if any Exchange-related services are not working. The reason behind it can be the Net.tcp port sharing service. If this service is stopped or having any issue then Exchange will not install. Then you would need to start this service to continue with Exchange setup.    

-  Make sure to enable the IPv6. Also, ensure that the AD Subnet configuration is as per the Exchange environment.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
