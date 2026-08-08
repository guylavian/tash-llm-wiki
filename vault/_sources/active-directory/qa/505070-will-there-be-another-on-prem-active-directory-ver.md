---
title: "Will there be another on-prem Active Directory version?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/505070/will-there-be-another-on-prem-active-directory-ver
question_id: 505070
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Will there be another on-prem Active Directory version?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/505070/will-there-be-another-on-prem-active-directory-ver (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

With Server 2016, the last AD FFL/DFL was released. That means the on-prem AD schema has not been upgraded for the last 5 years. I know it is a mature product that needs not much improvement yet it has room for improvement and hardening. So sysadmins wait for a new, enhanced, hardened AD and it seems like there would not be since the focus is now Azure AD. Yet, on-prem lives and will do so. So the question is still present: Will there be a new AD version?

I posted a question on Reddit ( r/activedirectory ), and added my comment if there would be some additions in the future, what would I want. And I have been told to post it here.

I'd like to make a few simple points, mostly based on "the Power of the defaults" about security and interoperability with 3rd parties:

-   All objects must be selected as "prevent accidental deletion", not just OUs. It might not be an issue after Recycle Bin, but it would help actually preventing accidents.

-   KRBTGT Account Password Reset built-in without using 3rd Party scripts. A sane and simple PowerShell module and an integrated GUI, just a window, would be great.

-   Create the emergency administrator account during the first configuration and make it obligatory.

-   LAPS by default. Schema is already extended to use and ask for configuration during AD installation. Attributes are ignored if the configuration is skipped. LAPS GPOs are ready in GPOs but not linked anywhere to help sysadmins.

-   A tiered AD structure by default. Sysadmins can start implementing basic ESAE using templates where businesses can customize later. But in greenfield installations, the default Directory Information Tree (DIT) might already fit.

-   Delegate print pruning to print servers. No print spooler on DCs. If there is a print server to publish printers, it can remove stale ones from AD too. It's just a matter of delegation by default.

-   Domain Admins group and default Administrator account is restricted within DCs only by default. Sysadmins should not work hard to harden AD but to make exceptions to it.

-   Default Domain Policy to include policies disabling and removing stale accounts. No 3rd party scheduled PowerShell tasks are needed, that DC removes them by the policy. Sysadmins should be able to make exceptions and changes when needed.

-   Default Domain Policy and Default Domain Controller Policy to include best practice audit policies by default.

-  Event log size limits: The event log size limits for DCs must be a lot higher for an actually secure environment by default. Therefore, Default Domain Controller Policy must have entries for that too.

-  Strict password policy by default. Different policies for Domain Administrators and regular users is enough for the beginning. And please, low complexity-high length is stronger, so reward longer passwords.

-  Built-in mechanism for DFS Replication issues that harm SYSVOL replications: DFS issues affect SYSVOL replication. Since AD Replication is on the AD database level, it seems healthy. But while troubleshooting, you can see the issue is about DFS. You install File Server features to manage it by GUI or Powershell. However, this is tightly coupled with AD and it must have a capability to -at least- show some warnings and alerts and manually trigger a DFS replication, etc, a mechanism is other than the Event Log.

-  This one is not so important but the LDAP standard requires that a RootDSE MUST publish information about itself and the servers. There are hybrid scenarios where the RootDSE needs to be known if it is an OpenLDAP, Red Hat Directory or AD.

-  The most googled question for AD Objects: Creator's and modifier's name. And the answer is always "check your event log". But those events are not even turned on by default. AD desperately needs creatorsName and modifiersName attributes.

-  Backlinks for AD ACLs: When a user or group is removed, the SID stays there. The ACLs can have backlinks to remove them from ACLs, and it would be great if there were a warning enumerating the ACLs.

-  A clear list of AD delegations: Since delegations are done via OUs, we can only check ACLs if there is a delegation. Or, we can use red team tools such as Bloodhound to check themç However, delegations are exceptions from the baselines and they could be easily managed via a simple interface.

-  Site-based AD performance profiles: For performance requirements, sysadmins might check some documents to tune and since they are dangerous to modify, they quit. Just like power management profiles, there might be performance profiles for different use cases: High-performance profile for data centres and higher network capabilities, and high reliability for remote sites that have low network capabilities such as oil platforms, ships and geographies where only satellite comms can help.

-  Give Domain Computers and Authenticated Users read permission by default. After MS16-072 it prevents many GPO issues.

-  Add "Domain Joiners" group by default. Allow sysadmins to delegate this permission in a fine grained-fashion. That requires changing default ACLs of DNS domains. The new group must be added for each DNS domain by default so that newly joined computers can register themselves to the DNS server.
    20. Storing PGP keys in ADUser/Person object: This was something I asked before, when user voice was still active. Adding another attribute with the ACL that enables only the owner can access would help email clients to utilize PGP.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-10*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
