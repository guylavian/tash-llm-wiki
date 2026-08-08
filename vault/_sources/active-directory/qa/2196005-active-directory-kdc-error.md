---
title: "Active directory KDC error."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196005/active-directory-kdc-error
question_id: 2196005
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active directory KDC error.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196005/active-directory-kdc-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are getting below event in 2012 R2 domain controller, As per this article https://support.microsoft.com/en-us/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041  installed the November 9, 2021 security update and the November 14, 2021 out-of-band (OOB) updates and also a SSU, but the event is still coming. Please help to solve the error.

The Key Distribution Center (KDC) encountered a ticket that did not contain information about the account that requested the ticket while processing a request for another ticket. This prevented security checks from running and could open security vulnerabilities. See https://go.microsoft.com/fwlink/?linkid=2173051 to learn more.

Regards,

Kanishka.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-06*

Hi Ckanishka,

Thank you for posting in the Microsoft Community Forums.

Possible causes of the problem: 

The ticket may have been corrupted or expired, making it impossible for the KDC to read or verify. 

The client is incorrectly configured, resulting in the generated ticket not containing the necessary account information. 

Network issues can cause the ticket to be corrupted or some information lost during transmission. 

A configuration or operation issue with the KDC server that prevents the ticket request from being processed correctly. 

You may need to verify the issue by the following methods: 

Clear the existing Kerberos ticket cache on the client and reacquire the ticket. Use the klist command to check the currently held tickets to ensure that they are valid and have not expired. 

Make sure that the client's Kerberos configuration file (usually /etc/krb5.conf or C:Windowskrb5.ini) is configured correctly, especially for the [realms] and [domain_realm] sections. 

Ensure that the system time synchronization of the client and the KDC server is in sync. A large time difference will result in invalid tickets. You can use the NTP service to synchronize time. 

Review the logs on the KDC server for error messages or warning messages that can help locate the cause of the problem. 

Try restarting the KDC service to make sure it's working properly. 

Use network diagnostic tools (e.g., ping, traceroute) to check if the network connection between the client and the KDC server is healthy.

Best regards

Neuvi Jiang
