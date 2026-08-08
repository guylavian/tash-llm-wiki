---
title: "ECP cannot login when a specific Exchange server is disconnected"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187417/ecp-cannot-login-when-a-specific-exchange-server-i
question_id: 2187417
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-service"]
---
# ECP cannot login when a specific Exchange server is disconnected

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187417/ecp-cannot-login-when-a-specific-exchange-server-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My client is having below environment:

Total 5 exchange servers, all of them are 2016 standard. 

Just name them as A B C D&E

All of them installed the mailbox role

A&B act as traditional hub server, they belongs to no DAG and no user DB in it.

CDE act is DB server, belongs to the only DAG in the domain

5 DBs in the DAG (just name them DB1,2,3,4,5)

DB1 has a copy on server CE, active on C

DB2 has a copy on server CE, active on E

There is mail gateway and the smtp route only points to A&B.

—————————

Aim:

Server A&B be removed and a IP load balancer will be build and take over the IP of them.

Problem1:

After disconnecting Server A&B, and getting the IP load balancer in, mail flow (both in the out) are normal, owa normal, but problem happens to ECP.

ECP can only show the /ECP page but login fail ( no matter I am if I goes to server C or D or E the /ECP  page) 

 Further investigated and found that only when server A is disconnected, the ECP will not the able to login. When server B is disconnected, things are normal.

Shouldn’t all the ECP work on its own? It is strange that disconnect a specific Exchange will make ECP not able to login.

Is there a setting I can look into so that taking away server A and ECP can still work?

Problem2:

One day all user on DB1 cannot connect to outlook nor login OWA. After activate it on server E, things are fine.

Rebooted server C, activate it on C, not working. Activate again on E, fine again.

So, there are two possibilities,

if DB 2 can activate on C and those users are fine, DB1 having problem.

if DB 2 activate on C and those users are not fine, server C is having problem

If server C is having problem, Would you really try to solve it or just create a new Exchange, add it into DAG, remove server C?

Thanks all of you for the time

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-26*

Any ideas to the ECp login issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-26*

Hi vhim,

Thank you for posting in the Microsoft Community Forums.

Recommendation:

If database corruption is suspected, be sure to back up the database before proceeding with the repair operation.

If hardware failure is the source of the problem, consider replacing the affected hardware components.

If the problem persists and cannot be resolved, consider adding a new Exchange server to the DAG and moving the affected database copy to the new server. This can be used as a last resort to restore service, but should be used with caution to avoid the risk of data loss or inconsistency.

Best regards

Neuvi
