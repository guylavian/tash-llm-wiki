---
title: "Troubles with kerberos on DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5740880/troubles-with-kerberos-on-dc
question_id: 5740880
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# Troubles with kerberos on DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5740880/troubles-with-kerberos-on-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have troubles on somes computers since i upgraded my DC from windows 2016 to windows 2025. Finally i found this errors on one of my two DC. I pasted directly commands on the DC :

Test-ComputerSecureChannel -Verbose

VERBOSE: Performing the operation "Test-ComputerSecureChannel" on target "N".

Test-ComputerSecureChannel : Cannot verify the secure channel for the local computer. Operation failed with the following exception: The specified domain either does not exist or could not be contacted.

nltest /sc_verify:mydomaine-name

I_NetLogonControl failed: Status = 1355 0x54b ERROR_NO_SUCH_DOMAIN

From one computer member, if i try :  

nltest /sc_verify:mydomaine-name /server:DC1 (DC before)  

I_NetLogonControl failed: Status = 1355 0x54b ERROR_NO_SUCH_DOMAIN

and on the second DC :  

nltest /sc_verify:mydomaine-name /server:DC2 -> success ! **

On the second DC, this commands works very well, no problem. That mean kerberos is broken on this DC ? this DC as all FSMO roles.  

thanks a lot

## Answer (community) — Independent Advisor

*upvotes: 1 · updated: 2026-01-28*

Hello Eric,

Since replication, DNS, and Netlogon logs are all clean, that rules out the usual causes of a broken secure channel. The Dell article you referenced is correct: in certain scenarios, `nltest /sc_verify` or `Test-ComputerSecureChannel` can return ERROR_NO_SUCH_DOMAIN (1355) when run directly on a domain controller. This is expected behavior because a DC does not maintain a secure channel to itself in the same way a member server does.

In other words, the error on DC1 is not necessarily an indication of a fault, but rather a quirk of how secure channel verification works on domain controllers. The fact that replication, DNS, and Netlogon are all healthy strongly suggests that DC1 is functioning correctly after the upgrade.

To be thorough, I recommend:

Continuing to monitor replication with `repadmin /replsummary` and `repadmin /showrepl`.

Watching Netlogon and Directory Services logs for any new warnings or errors.

Validating FSMO role operations from DC2 to ensure DC1 is serving them correctly.

If all of these remain healthy, you can safely consider the 1355 return code on DC1 as benign and not a sign of Kerberos or trust failure.

Domic Vo.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-01-27*

Hello,

No erros with commands

repadmin /replsummary

repadmin /showrepl

dcdiag  

All records in DNS are OK  

No errors in **Event Viewer > Applications and Services Logs > Microsoft > Windows > Netlogon  

**i also found this, this article say it is normal : https://www.dell.com/support/kbdoc/en-us/000226052/domain

what do you think ?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-01-26*

Hello Eric LE CORRE,

The errors you are seeing point to a broken secure channel between your upgraded domain controller (DC1) and the domain. The ERROR_NO_SUCH_DOMAIN (1355) returned by both Test-ComputerSecureChannel and nltest /sc_verify means that Netlogon on DC1 cannot locate or validate the domain trust. Since DC2 responds correctly and validates the secure channel, the issue is isolated to DC1 and not the domain as a whole.

This is not strictly “Kerberos broken,” but rather that DC1’s Netlogon service is failing to establish or advertise itself correctly after the upgrade from Windows Server 2016 to Windows Server 2025. When a DC is upgraded in place, the machine account password and secure channel must remain intact. If that state is corrupted, the DC can appear domain‑joined but fail to authenticate.

The first step is to check the Netlogon service on DC1. Ensure it is running and review the logs under Event Viewer > Applications and Services Logs > Microsoft > Windows > Netlogon. Look for Event IDs 5719, 5781, or 5805, which indicate secure channel or replication failures.

Next, verify replication health. Run:

repadmin /replsummary

repadmin /showrepl

If DC1 is failing inbound or outbound replication, that confirms the domain trust is broken at the directory level.

Also check DNS registration. DC1 must have its SRV records correctly registered in the domain DNS zone (_ldap._tcp.dc._msdcs.<domain>). Run dcdiag /test:dns /v on DC1. If the SRV records are missing or stale, clients and other DCs will not locate DC1, which can produce the 1355 error.

If DNS and replication are healthy but the secure channel still fails, you may need to reset the machine account password for DC1. On a domain controller, this is done with:

netdom reset DC1 /domain:mydomain-name /userd:domainadmin /passwordd:*

This forces the DC to re‑establish its secure channel with the domain. Be cautious: if replication is already broken, you may need to demote and re‑promote DC1 instead of resetting, to avoid lingering objects.

Since DC1 holds all FSMO roles, you should also confirm that those roles are functioning. Run netdom query fsmo from DC2. If DC2 can query FSMO roles but DC1 cannot validate its secure channel, you may be in a split‑brain situation where DC1 is not trusted by the domain. In that case, transferring FSMO roles to DC2 temporarily and then repairing or rebuilding DC1 is the safer path.

In summary, the error is not Kerberos itself but a broken secure channel and likely DNS/Netlogon registration issue on DC1 after the upgrade. Check Netlogon logs, replication health, and DNS SRV records. If those are corrupted, reset the secure channel or demote/re‑promote DC1 to restore domain trust.

I hope you've found something useful here. If it helps you get more insight into the issue, it's appreciated to accept the answer. Should you have more questions, feel free to leave a message. Have a nice day!

Domic Vo.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-01-26*

It appears that you are experiencing issues with Kerberos authentication on one of your Domain Controllers (DC) after upgrading to Windows Server 2025. The errors you are encountering, such as "Cannot verify the secure channel for the local computer" and "ERROR_NO_SUCH_DOMAIN," suggest that the DC is having trouble communicating with the domain, which could be due to several factors.

Here are some troubleshooting steps you can take:

-  Check Network Connectivity: Ensure that the problematic DC can communicate with the other DC and that there are no network issues or firewalls blocking the necessary ports.

-  DNS Configuration: Verify that the DNS settings on the DC are correct. The DC should point to itself as the primary DNS server and to another DC as the secondary DNS server if applicable. Incorrect DNS settings can lead to domain discovery issues.

-  Event Logs: Check the Event Viewer on the problematic DC for any additional error messages that may provide more context about the issue.

-  Run `nltest`: Since you mentioned that `nltest /sc_verify` failed, you might want to run `nltest /dclist:<domain>` to see if the DC can list other domain controllers.

-  FSMO Roles: Since this DC holds all FSMO roles, ensure that it is functioning correctly and that the roles are not causing any issues. You may consider transferring the roles to another DC temporarily to see if that resolves the issue.

-  Kerberos Configuration: Verify that the Kerberos Key Distribution Center (KDC) service is running on the problematic DC. You can check this in the Services management console.

-  Review Security Policies: Check if there are any security policies that might be affecting Kerberos authentication on the DC.

If the issue persists after these checks, you may need to investigate further for potential Active Directory replication issues or consider restoring the DC from backup if it continues to malfunction.

References:

-  Event ID 5719, Error 1311, or Error 1355 - Domain controller or domain not found

-  Domain controller is not functioning correctly
