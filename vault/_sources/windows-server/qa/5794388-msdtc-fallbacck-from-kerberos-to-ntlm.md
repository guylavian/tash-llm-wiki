---
title: "MSDTC fallbacck from Kerberos to NTLM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5794388/msdtc-fallbacck-from-kerberos-to-ntlm
question_id: 5794388
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# MSDTC fallbacck from Kerberos to NTLM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5794388/msdtc-fallbacck-from-kerberos-to-ntlm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we have several SQL servers and we are using DTC (Distributed Transaction Coordinator) with linked server.

We have configured the required SPN for SQL and we have noticed that if we disable the incoming NTLM traffic from the GPO "Network security: Restrict NTLM: Incoming NTLM traffic", the calls that are using DTC are using Kerberos but failed and then try NTLM but fail again because of the GPO.

From SSMS, if we run this command, the output is KERBEROS  

select auth_scheme from sys.dm_exec_connections where session_id=@@spid

We are having this error in the Windows application log of the calling server

Source: MSDTC Client 2

ID: 4879

MS DTC encountered an error (HR=0x80004005) while establishing a secure connection with the [SQL_ServerName] system.

Any idea what could cause the DTC to fail using Kerberos ?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-02*

Hello Charles Thivierge,

The error you’re seeing with MSDTC when NTLM is disabled is a classic Kerberos delegation problem. Even though sys.dm_exec_connections shows KERBEROS for the SQL session itself, MSDTC requires Kerberos at the RPC layer between the DTC service on the calling server and the DTC service on the target SQL server. If delegation is not properly configured, the Kerberos handshake fails, and with NTLM disabled, there is no fallback, resulting in Event ID 4879 and HR=0x80004005.

The key here is that Kerberos for DTC is not just about having SPNs registered for SQL. You must also have SPNs registered for the MSDTC service itself, and the accounts involved must be trusted for delegation. Specifically, the machine accounts of the SQL servers and the calling servers need to be configured in Active Directory with “Trust this computer for delegation to any service (Kerberos only)” or constrained delegation to the MSSQLSvc and MSDTC SPNs. Without this, the DTC handshake will fail even though the SQL connection reports Kerberos.

Check that the following SPNs exist and are registered against the correct service accounts or machine accounts:

-  MSDTC/<hostname>

-  MSDTC/<hostname.domain>

Also confirm that the Distributed Transaction Coordinator service is running under NT AUTHORITY\NetworkService or a domain account with proper delegation rights. If it’s running under NetworkService, the SPNs must be registered against the machine account in AD.

Finally, ensure that the firewall allows RPC dynamic ports between the servers, and that the DTC security settings (dcomcnfg > Component Services > Computers > My Computer > Distributed Transaction Coordinator > Local DTC > Security) are aligned. For Kerberos, “Mutual Authentication Required” must be enabled, and “Allow Inbound/Outbound” must be checked.

I hope you've found something useful here. If it helps you get more insight into the issue, it's appreciated to accept the answer. Should you have more questions, feel free to leave a message. Have a nice day!

Domic Vo.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-02*

MSDTC uses its own security negotiation; seeing `KERBEROS` for the SQL connection in `sys.dm_exec_connections` only proves that the SQL client–server TDS session is using Kerberos, not that the MSDTC RPC security context is also using Kerberos successfully.

If Kerberos for MSDTC fails, it will fall back to NTLM. Because the GPO blocks incoming NTLM, the fallback also fails and you see event 4879 (`HR=0x80004005`) from `MSDTC Client 2`.

From the provided context, the main Kerberos-related causes to check are:

-  Malformed or missing SPNs for the DTC/SQL services  

   Kerberos will fail if the SPN used as the target for authentication is malformed or not registered on the correct account. Common issues:

-  SPN format is incorrect (for example, wrong host, port, or service class).

-  SPN not registered at all on the service account.

-  SPN registered on the wrong account.

   Actions:

-  Use `setspn -Q` or `setspn -L` to verify SPNs on the relevant service accounts and confirm that the SPNs used by MSDTC are present and correctly formed.

-  If the SPN is malformed, either correct the SPN used by the application or register the malformed SPN on the correct service account, as described in the SPN guidance.

-  Client cannot reach a domain controller / KDC  

   Kerberos requires line-of-sight to a DC. If the MSDTC client cannot contact a DC when it tries to get a Kerberos ticket for the remote service, Kerberos fails and MSDTC falls back to NTLM.   Actions:

-  Verify that the calling SQL Server can resolve and reach domain controllers (DNS, ports for Kerberos/KDC).

-  Check for Kerberos errors in the System event log on the MSDTC client and on the DCs around the time of the failure.

-  Network DTC security configuration  

   If DTC transactions fail because of network connectivity or security configuration, MSDTC may not be able to establish the secure RPC channel even if Kerberos is available.   Actions on both SQL servers involved in the distributed transaction:

-  Open Component Services → Computers → My Computer → Distributed Transaction Coordinator → Local DTC → Properties → Security.

-  Ensure Network DTC Access is enabled.

-  Under Transaction Manager Communication, enable Allow Inbound and Allow Outbound as required.

-  Restart the MSDTC service after changes.

-  Cloned/duplicate identities affecting MSDTC  

   If servers were cloned or imaged, MSDTC can have duplicate CIDs, which can break DTC communication.   Actions:

-  Use DTCPing or `Test-Dtc` to verify MSDTC functionality between the two servers.

-  If DTCPing warns that the CID values are the same, reinstall MSDTC on one server to generate a unique CID.

-  LSASS / security subsystem issues  

   If LSASS is unresponsive or misconfigured, Kerberos/NTLM operations can fail, causing SSPI/AcceptSecurityContext failures for services including MSDTC.   Actions:

-  Check for LSASS-related errors and Kerberos errors in the event logs.

-  Confirm SPNs and DC reachability as above.

In summary, the DTC Kerberos failure is typically due to SPN issues, DC reachability, or MSDTC security/network configuration. Once Kerberos for MSDTC is working end-to-end (validated with DTCPing or `Test-Dtc`), blocking NTLM via GPO will no longer break the distributed transactions.

References:

-  KB5011233: Protections in CVE-2022-21920 may block NTLM authentication if Kerberos authentication is not successful

-  Troubleshooting Problems with MSDTC

-  New functionality in the Distributed Transaction Coordinator service in Windows

-  Local security subsystem errors in SQL Server
