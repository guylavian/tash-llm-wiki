---
title: "Active Directory Azure VM login issue for network jump systems."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5947333/active-directory-azure-vm-login-issue-for-network
question_id: 5947333
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Active Directory Azure VM login issue for network jump systems.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5947333/active-directory-azure-vm-login-issue-for-network (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Domain login on jump systems hangs/times out when only internal AD/DNS communication (10.0.0.12 and 10.0.0.13, over the existing IPsec tunnel) is allowed. Login only completes smoothly when a broad Microsoft-Azure address object (~25,000 IP ranges covering all of Azure's public IP space) is also permitted through the firewall.

-  Basic connectivity (ping, traceroute) to the AD server succeeds  the network path itself is fine.

-  The problem shows up specifically during the logon process, as a delay/hang rather than a clean failure.

-  A secondary DNS entry pointing to a public IP (11.5.112.18.21) was initially suspected, but this was ruled out  that IP is confirmed to belong to an ISP, not Microsoft/Azure.

-  Since the fix requires a broad Azure IP range (not one specific address), the likely cause is a Windows OS-level dependency that piggybacks on login most probably certificate revocation checking (CRL/OCSP) or automatic root certificate updates, both of which are served off Microsoft's large, distributed CDN/Azure infrastructure. This is not yet confirmed with hard evidence  it's the leading hypothesis pending log data.

Now the question is   

"Does Active Directory login on the jump systems have a genuine dependency on Microsoft Azure or Entra ID / other Microsoft services  or not?"

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-07-15*

Hi Shwetha, a standard on-premises Active Directory domain logon does not have an inherent dependency on Microsoft Azure, Microsoft Entra ID, or the full Azure public IP range. The required traffic is normally limited to the domain infrastructure, including DNS, Kerberos, LDAP/LDAPS, SMB, RPC, and related domain-controller communications; therefore, the fact that logon succeeds only when the broad Microsoft Azure address object is allowed indicates that another component invoked during sign-in is making an outbound connection.

The most likely candidates are certificate revocation checks through CRL or OCSP, automatic root certificate updates, smart-card or credential-provider certificate validation, Defender, or another security component involved in the logon path. I would not recommend permanently allowing all Azure public IP ranges, because that is unnecessarily broad and does not identify the actual dependency.

Please capture a trace during a delayed logon using `netsh trace start scenario=NetConnection capture=yes report=yes`, reproduce the issue, and then stop it with `netsh trace stop`. At the same time, review `Microsoft-Windows-CAPI2/Operational`, `Microsoft-Windows-GroupPolicy/Operational`, Netlogon, Schannel, and System logs to identify the exact hostname or URL causing the timeout. Once the destination is confirmed, allow only the required endpoint or correct the certificate-validation path rather than opening the entire Azure address space.
