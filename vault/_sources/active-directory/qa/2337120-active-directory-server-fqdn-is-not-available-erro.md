---
title: "Active directory server <FQDN> is not available. Error message: Active directory response: A local error occurred. caused DC replication issue."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2337120/active-directory-server-fqdn-is-not-available-erro
question_id: 2337120
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active directory server <FQDN> is not available. Error message: Active directory response: A local error occurred. caused DC replication issue.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2337120/active-directory-server-fqdn-is-not-available-erro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows DC replication error

Hi, is anyone able to help me with an issue regarding DC replication?

I believe the problem started after restoring snapshots on ESXi. I was troubleshooting our on-premise Exchange mailbox and attempted to restore snapshots of both the Exchange server and the primary domain controller.

On the Exchange mailbox server, I ran the `Test-ComputerSecureChannel -Verbose` command, and it showed that the connection to my domain (domain.com) is in good condition.

However, I am now experiencing problems with domain controller replication. Could anyone assist me with this? Below are the commands/tests I ran and their outputs.

Primary:

repadmin /replsummary

Replication Summary Start Time: 2025-07-01 10:30:42

Source DSA largest delta fails/total %% error

Primary-DC 01d.04h:33m:54s 5 / 5 100 (2148074274) The target principal name is incorrect.

Secondary-DC 44m:47s 0 / 5 0

Experienced the following operational errors trying to retrieve replication information:

58 - RODC.domain.com

Destination DSA largest delta fails/total %% error

Primary-DC 44m:47s 0 / 5 0

Secondary-DC 01d.04h:33m:54s 5 / 5 100 (2148074274) The target principal name is incorrect.

test-computersecurechannel -repair -credential (get-credential)

cmdlet Get-Credential at command pipeline position 1

Supply values for the following parameters:

Credential

False

nltest /sc_reset:domain.com

I_NetLogonControl failed: Status = 1355 0x54b ERROR_NO_SUCH_DOMAIN

repadmin /showrepl

Repadmin: running command /showrepl against full DC localhost

Default-First-Site-Name\Primary-DC

DSA Options: IS_GC

Site Options: (none)

DSA object GUID: a802b3eb-2653-4e40-97d8-9273f5ec794e

DSA invocationID: 972c2929-2e82-483a-8cd1-90a062545c73

==== INBOUND NEIGHBORS ======================================

DC=domain,DC=com

Default-First-Site-Name\Secondary-DC via RPC

DSA object GUID: 1b2faa16-8476-4273-82ab-87db82db88d9

Last attempt @ 2025-06-30 22:45:53 was successful.

CN=Configuration,DC=domain,DC=com

Default-First-Site-Name\Secondary-DC via RPC

DSA object GUID: 1b2faa16-8476-4273-82ab-87db82db88d9

Last attempt @ 2025-06-30 22:45:55 was successful.

CN=Schema,CN=Configuration,DC=domain,DC=com

Default-First-Site-Name\Secondary-DC via RPC

DSA object GUID: 1b2faa16-8476-4273-82ab-87db82db88d9

Last attempt @ 2025-06-30 22:45:55 was successful.

DC=DomainDnsZones,DC=domain,DC=com

Default-First-Site-Name\Secondary-DC via RPC

DSA object GUID: 1b2faa16-8476-4273-82ab-87db82db88d9

Last attempt @ 2025-06-30 22:45:55 was successful.

DC=ForestDnsZones,DC=domain,DC=com

Default-First-Site-Name\Secondary-DC via RPC

DSA object GUID: 1b2faa16-8476-4273-82ab-87db82db88d9

Last attempt @ 2025-06-30 22:45:55 was successful.

Secondary:

repadmin /replsummary

Source DSA largest delta fails/total %% error

Primary-DC 01d.03h:21m:55s 5 / 5 100 (2148074274) The target principal name is incorrect.

Destination DSA largest delta fails/total %% error

Secondary-DC 01d.03h:21m:55s 5 / 5 100 (2148074274) The target principal name is incorrect.

Experienced the following operational errors trying to retrieve replication information:

8341 - Primary-DC.domain.com

58 - RODC.domain.com

test-computersecurechannel -repair -credential (get-credential)

cmdlet Get-Credential at command pipeline position 1

Supply values for the following parameters:

Credential

True

nltest /sc_reset:domain.com

Flags: 30 HAS_IP HAS_TIMESERV

Trusted DC Name \Primary-DC.domain.com

Trusted DC Connection Status Status = 0 0x0 NERR_Success

The command completed successfully

repadmin /showrepl

Repadmin: running command /showrepl against full DC localhost

Default-First-Site-Name\Secondary-DC

DSA Options: IS_GC

Site Options: (none)

DSA object GUID: 1b2faa16-8476-4273-82ab-87db82db88d9

DSA invocationID: 09befb82-b1f0-4819-b1eb-361421044ec3

==== INBOUND NEIGHBORS ======================================

DC=domain,DC=com

Default-First-Site-Name\Primary-DC via RPC

DSA object GUID: a802b3eb-2653-4e40-97d8-9273f5ec794e

Last attempt @ 2025-07-01 11:56:55 failed, result -2146893022 (0x80090322):

The target principal name is incorrect.

58 consecutive failure(s).

Last success @ 2025-06-30 06:52:53.

CN=Configuration,DC=domain,DC=com

Default-First-Site-Name\Primary-DC via RPC

DSA object GUID: a802b3eb-2653-4e40-97d8-9273f5ec794e

Last attempt @ 2025-07-01 11:56:55 failed, result -2146893022 (0x80090322):

The target principal name is incorrect.

43 consecutive failure(s).

Last success @ 2025-06-30 05:56:48.

CN=Schema,CN=Configuration,DC=domain,DC=com

Default-First-Site-Name\Primary-DC via RPC

DSA object GUID: a802b3eb-2653-4e40-97d8-9273f5ec794e

Last attempt @ 2025-07-01 11:56:55 failed, result -2146893022 (0x80090322):

The target principal name is incorrect.

34 consecutive failure(s).

Last success @ 2025-06-30 05:56:48.

DC=DomainDnsZones,DC=domain,DC=com

Default-First-Site-Name\Primary-DC via RPC

DSA object GUID: a802b3eb-2653-4e40-97d8-9273f5ec794e

Last attempt @ 2025-07-01 11:56:55 failed, result 1256 (0x4e8):

The remote system is not available. For information about network troubleshooting, see Windows Help.

106 consecutive failure(s).

Last success @ 2025-06-30 06:33:31.

DC=ForestDnsZones,DC=domain,DC=com

Default-First-Site-Name\Primary-DC via RPC

DSA object GUID: a802b3eb-2653-4e40-97d8-9273f5ec794e

Last attempt @ 2025-07-01 12:10:29 failed, result -2146893022 (0x80090322):

The target principal name is incorrect.

198 consecutive failure(s).

Last success @ 2025-06-30 06:36:48.

Source: Default-First-Site-Name\Primary-DC

******* 197 CONSECUTIVE FAILURES since 2025-06-30 06:52:53

Last error: -2146893022 (0x80090322):

The target principal name is incorrect.

repadmin /syncall /AeP Secondary-DC.domain.com

Syncing all NC's held on Secondary-DC.domain.com.

Syncing partition: DC=ForestDnsZones,DC=domain,DC=com

CALLBACK MESSAGE: Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

CALLBACK MESSAGE: SyncAll Finished.

SyncAll reported the following errors:

Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

Syncing partition: DC=DomainDnsZones,DC=domain,DC=com

CALLBACK MESSAGE: Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

CALLBACK MESSAGE: SyncAll Finished.

SyncAll reported the following errors:

Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

Syncing partition: CN=Schema,CN=Configuration,DC=domain,DC=com

CALLBACK MESSAGE: Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

CALLBACK MESSAGE: SyncAll Finished.

SyncAll reported the following errors:

Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

Syncing partition: CN=Configuration,DC=domain,DC=com

CALLBACK MESSAGE: Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

CALLBACK MESSAGE: SyncAll Finished.

SyncAll reported the following errors:

Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

Syncing partition: DC=llc,DC=domain,DC=com

CALLBACK MESSAGE: Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

CALLBACK MESSAGE: SyncAll Finished.

SyncAll reported the following errors:

Error contacting server a802b3eb-2653-4e40-97d8-9273f5ec794e._msdcs.domain.com (network error): -2146893022 (0x80090322):

The target principal name is incorrect.

kdc and netlogon are both running

connection to ports 389 and 88 are both open and accessible

Already run klist purged on both servers

already flushdns on both servers

no duplicates on setspn -X

## Answers

_No answers on this thread._
