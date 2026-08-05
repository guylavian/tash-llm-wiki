---
title: "Kerberos Authentication Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5855562/kerberos-authentication-error
question_id: 5855562
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Kerberos Authentication Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5855562/kerberos-authentication-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are having Kerberos Error and it is not allowing users to connect to an SQL Server on a server. I have checked Klist, time sync, as well as clearing the klist, resync the time. This is a domain account. I am at a lost.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-04-08*

Use a focused Kerberos/SQL checklist to narrow down the cause, since time sync and ticket cache have already been checked.

-  Confirm whether tickets are expired or missing

-  On an affected client, run:

-  `klist` to confirm there is a valid TGT and a service ticket for the SQL SPN.

-  If you see `KRB_AP_ERR_TKT_EXPIRED` in KDC logs or traces, purge and reacquire tickets:

-  `klist purge`

-  Sign out/in or restart the client, then try to connect again.

-  If tickets are still expiring quickly or not renewing, investigate domain controller health and time sync across all DCs and SQL servers.

-  Verify the SQL Server SPN and uniqueness

-  Kerberos to SQL requires a correct and unique SPN for the SQL service account.

-  On a domain controller (or admin workstation with RSAT), run:

-  `setspn -Q MSSQLSvc/<SQLServerFQDN>:<port>`

-  `setspn -Q MSSQLSvc/<SQLServerNetBIOS>:<port>`

-  Confirm:

-  The SPN exists.

-  It is registered on the correct SQL Server service account (not on multiple accounts).

-  There are no duplicates. If `KDC_ERR_PRINCIPAL_NOT_UNIQUE` or `KDC_ERR_S_PRINCIPAL_UNKNOWN` appear in logs or traces, fix SPN registration as described in Kerberos generates KDC_ERR_S_PRINCIPAL_UNKNOWN or KDC_ERR_PRINCIPAL_NOT_UNIQUE error.

-  Check for KRB_AP_ERR_MODIFIED and related errors

-  On the SQL Server and domain controllers, review System/Security logs for:

-  `KRB_AP_ERR_MODIFIED`

-  `KDC_ERR_PRINCIPAL_NOT_UNIQUE` / `KDC_ERR_S_PRINCIPAL_UNKNOWN`

-  `KRB_AP_ERR_SKEW`

-  If `KRB_AP_ERR_MODIFIED` appears:

-  It usually indicates SPN or account mismatch (ticket encrypted for a different account than the one running SQL).

-  Correct the SPN and ensure SQL is running under the account that owns the SPN.

-  If `KRB_AP_ERR_SKEW` appears:

-  Reconfirm time sync using `w32tm /resync /computer:<Target> /rediscover` on clients, SQL Server, and DCs.

-  Validate infrastructure and domain reachability

-  Ensure the client and SQL Server can contact domain controllers:

-  Check that required ports are open between client ↔ DC and SQL ↔ DC, especially:

-  Kerberos: 88/TCP, 88/UDP, 464/TCP/UDP, and dynamic RPC ports 49152–65535.

-  DNS: 53/TCP/UDP.

-  If domain controller discovery fails, errors like Event ID 5719, 1311, or 1355 may appear, indicating domain or DC not found.

-  Confirm both client and SQL Server are joined to appropriate domains (same forest or trusted forests).

-  Check LSASS / SSPI handshake errors on SQL Server

-  In the SQL Server error log, look for entries such as:

-  `SSPI handshake failed with error code 0x80090311` or `0x80090304`.

-  These indicate issues with LSASS or contacting an authority for authentication.

-  Reconfirm SPN registration and DC reachability.

-  If LSASS is unresponsive, restart the server during a maintenance window.

-  Use Network Monitor for deeper Kerberos tracing

-  If the issue persists and logs show Kerberos errors but the cause is unclear:

-  Install Network Monitor on both client and SQL Server.

-  Capture simultaneous traces while reproducing the failed connection.

-  Inspect Kerberos messages for:

-  Missing tickets in HTTP/TDS requests.

-  Specific KDC error codes (KDC_ERR_ETYPE_NOTSUPP, KRB_AP_ERR_MODIFIED, etc.).

-  Use the error codes from the trace together with the troubleshooting checklist to pinpoint the misconfiguration.

-  Restart after changes

-  After fixing SPNs, time, or infrastructure issues:

-  Restart SQL Server service (so it re-reads SPNs and credentials).

-  If necessary, restart affected clients and/or domain controllers.

-  Test Kerberos connections again.

If a specific Kerberos error code (for example, `KRB_AP_ERR_TKT_EXPIRED`, `KRB_AP_ERR_MODIFIED`, `KDC_ERR_PRINCIPAL_NOT_UNIQUE`) is identified in event logs or traces, focus on the corresponding row in the Kerberos troubleshooting checklist and remediate that condition before re-testing.

References:

-  KRB_AP_ERR_TKT_EXPIRED error in Kerberos tickets

-  Kerberos authentication troubleshooting guidance

-  Event ID 5719, Error 1311, or Error 1355 - Domain controller or domain not found

-  Local security subsystem errors in SQL Server

-  A Kerberos authentication fails together with the error code 0X80090302 or 0x8009030f on a computer that is running Windows Server 2008 or Windows Vista when the AES algorithm is used

-  Consistent authentication issues in SQL Server
