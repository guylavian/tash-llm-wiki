---
title: "Exchange Online failing to create Endpoint to Hybrid On-Premise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1195639/exchange-online-failing-to-create-endpoint-to-hybr
question_id: 1195639
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
---
# Exchange Online failing to create Endpoint to Hybrid On-Premise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1195639/exchange-online-failing-to-create-endpoint-to-hybr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, this is an infuriating issue so we are hoping someone might be able to help us.

We operate a Full Hybrid solution that was previously running on Exchange 2013.  Due to End of Life, we built a single server to take over from the previous CA and MB servers we were running and installed Exchange 2019.

All our Virtual Directories are created and match what previously worked, Internal Migration Endpoints created without any issues (after we applied a registry fix on LSA) and internal migrations work perfectly.

When we create the Endpoint on Exchange Online, it comes back with cannot complete and f we skip verification, the migration comes back with a 403 Negotiate error.

```
IncrementalSyncs 10 -MaxConcurrentMigrations 20 -Credentials $cred -Verbose VERBOSE: Returning precomputed version info: 3.1.0 VERBOSE: HTTP/1.1 POST with 601-byte payload VERBOSE: received 634-byte response of content type text/html VERBOSE: Query 1 failed. VERBOSE: Getting message from error object New-MigrationEndpoint: |Microsoft.Exchange.Migration.MigrationServerConnectionFailedException|The connection to the server 'redacted' could not be completed.
```

```
VERBOSE: Returning precomputed version info: 3.1.0 VERBOSE: HTTP/1.1 POST with 586-byte payload VERBOSE: received 732-byte response of content type text/html VERBOSE: Query 1 failed. VERBOSE: Getting message from error object New-MoveRequest: |Microsoft.Exchange.MailboxReplicationService.MRSRemoteTransientException|The call to 'https://redacted/EWS/mrsproxy.svc' failed. Error details: The HTTP request was forbidden with client authentication scheme 'Negotiate'. --> The remote server returned an error: (403) Forbidden..
```

On the On-Premise server the HCW ran without issue and the Virtual Directory reports back that the MRSProxy is enabled.  I have disabled, performed an iisreset, re-enabled and performed another iisreset but this hasn't resolve the issue.  It seems that externally, the MRS just cannot be found and we don't know why.

DNS is fully up to date and reporting back correctly everywhere.

I can access the mailboxes externally when using EWS Editor and retrieve back everything off non-o365 migrated mailboxes.  It just seems that MRS is being weird for external connections.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-04*

Hi Jame,
Thank you, we did run through these, please see results below:

All the other settings seem correct however, we are stuck on a 401 error internally and 403 externally.  I have tried setting Windows Auth on EWS to Negotiate only and have also tried changing it to include Negotiate: Kerberos too.
Something I did miss but don't think is an issue as the problem occurs internally, the service is behind an App Gateway, Traffic Manager and Loadbalancer.
