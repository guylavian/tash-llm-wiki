---
title: "FAQ for March 2021 Exchange Server Security Updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/298536/faq-for-march-2021-exchange-server-security-update
question_id: 298536
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# FAQ for March 2021 Exchange Server Security Updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/298536/faq-for-march-2021-exchange-server-security-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are publishing a content to help you install the Exchange security updates smoothly.

The content contains:

-FAQ  

-Setup Notice and Best Practices  

-Troubleshooting Tips

FAQ

-   My server is exchange 2016 CU16. The article says CU18 and CU19. Is my server in risk?  

    -YES. It applied to All exchange 2013 to 2019 CU versions. Not just the CU which listed below    • Exchange Server 2010 (update requires Service Pack 3 – this is a Defense in Depth update)  

    • Exchange Server 2013 (update requires CU 23, CU 22, CU 21 or SP1)  

    • Exchange Server 2016 (update requires CU 19, CU 18, CU 17, CU 16, CU 15, CU 14, CU13, CU 12, CU 11, CU 10, CU 9 or CU 8)  

    • Exchange Server 2019 (update requires CU 8, CU 7, CU 6, CU 5, CU 4, CU 3, CU 2, CU 1 or RTM)    You need to patch CU to latest first and then apply security patch.

-   My servers do not publish to internet. Am I in risk?  

    -If the exchange service is completely blocked from internet, it’s basically safe. Microsoft still suggest patching ASAP.

-   I’m in hybrid. I can block internet access. But I need to remain hybrid slow. Is it safe?  

    -If the firewall configured to allow o365 EXO IP address to access exchange server, it is basically safe. Microsoft still suggest patching ASAP.

-   Are there workarounds for these vulnerabilities?  

    -If installing security updates will be delayed, the only viable workaround would be to remove Exchange Servers from direct Internet access until the March security updates can be installed.

-   I don’t know the status of my exchange setup. What shall I Do  

    -You can use the Exchange Server Health Checker script, which can be downloaded from GitHub (use the latest release). Running this script will tell you if you are behind on your on-premises Exchange Server updates (note that the script does not support Exchange Server 2010).

-   Will the installation of the Security Updates take as long as installing an RU/CU?  

    -Installation of Security Updates does not take as long as installing a CU or RU, but you will need to plan for some downtime.  

    Plan 2-3 hours for CU upgrade at least.  

    Plan 1 hour for SU upgrade at least.

-   How can I tell if my servers have already been compromised?  

    -Information on Indicators of Compromise (IOCs) – such as what to search for, and how to find evidence of successful exploitation (if it happened), can be found in HAFNIUM Targeting Exchange Servers.  

    HAFNIUM targeting Exchange Servers with 0-day exploits - Microsoft Security  

    Scan Exchange log files for indicators of compromise

-   There are a lot of CVEs. Shall I apply them all?  

    -All the CVEs fixed by one security update. You don’t need to patch individually.  

    Patch can be downloaded here.    • Description of the security update for Microsoft Exchange Server 2019, 2016, and 2013: March 2, 2021 (KB5000871)  

    • Description of the security update for Microsoft Exchange Server 2010 Service Pack 3: March 2, 2021 (KB5000978)  

    Note: We are still on schedule to release Exchange Server 2016 CU 20 and Exchange Server 2019 CU 9 later in March 2021 and those CUs will contain the Security Updates mentioned here (along with other fixes). Our strong recommendation is for customers to not wait and to install these security updates immediately.

-   Any impact to the exchange service for the CU and SU upgrade?  

    -Nothing different from the previous CU and SU. Follow the best practice.  

    Upgrade Exchange to the latest Cumulative Update | Microsoft Learn

-  Any known issue for the setup?  

    -Listed in the kb.  

    Description of the security update for Microsoft Exchange Server 2019, 2016, and 2013: March 2, 2021 (KB5000871)

Setup notice and best practices

-   .net framework.  

    Latest build of exchange CU need .net framework 4.8. It needs to be installed first.  

    In case you need to prepare schema/AD on DC directly, .net framework 4.8 is needed on DC as well.

-   Schema upgrade.  

    Depends on the current CU version your server running, you may or may not need to upgrade schema.  

    Exchange 2019  

    https://learn.microsoft.com/en-us/exchange/plan-and-deploy/active-directory/ad-schema-changes?view=exchserver-2019  

    Exchange 2016  

    https://learn.microsoft.com/en-us/exchange/plan-and-deploy/active-directory/ad-schema-changes?view=exchserver-2016  

    Exchange 2013  

    https://learn.microsoft.com/en-us/exchange/exchange-2013-active-directory-schema-changes-exchange-2013-help

-   Further update.  

    If the server is 2019 CU7, and you apply the security update and then later go to CU8, you must apply the security update again.  

    If the server is 2016 CU18, and you apply the security update and then later go to CU19, you must apply the security update again.  

    Any newer version released in future. The patch will be included.

-   Backup the customized configuration  

    Any customized Exchange or Internet Information Server (IIS) settings that you made in Exchange XML application configuration files on the Exchange server (for example, web.config files or the EdgeTransport.exe.config file) will be overwritten when you install an Exchange CU. Be sure save this information so you can easily re-apply the settings after the install. After you install the Exchange CU, you need to re-configure these settings.

-   Best practice for CU /SU update.  

    • There is no need to install the RTM build or previous builds and then upgrade to the latest Cumulative Update. This is because each Cumulative Update is a full build of the product.  

    • Reboot the server beforehand and afterward.  

    • Test the new update in a non-production environment first to avoid any problems in the new update affecting the running production environment.  

    • Have a tested and working backup of both the Active Directory and your Exchange Server. (we don’t restore the backup usually. It is used as last option only)  

    • Temporarily disable any anti-virus software and third-party programs prior to the update process. Additionally, ensure all antivirus exclusions are correct .  

    Note: in some cases, you may find that services will not stop, or the install fails. Please disable A/V and all third-party programs and restart the server to unlock the files.  

    • Use an elevated command prompt to install the Cumulative Update and security update.  

    • Before performing any type of software or hardware maintenance on a DAG member, you should first put the DAG member in maintenance mode  

    Manage database availability groups | Microsoft Learn

Troubleshooting tips:

-   See error below.  

      

    It means the CU version didn’t meet the requirements. You need to upgrade server CU first.

-   Ecp error ( We see this issue 4 time already)  

      

    The SU was not installed properly.  

    Follow the best practice to run cmd as administrator and run MSP from there.  

    If the installation has already done. Uninstall and reinstall.

-   Installation failed due to previous IU or SU.  

    You need to uninstall the previous installed IU or SU before applying this SU. Sample log below.  

    Installation cannot continue. The Setup Wizard has determined that this Interim Update is incompatible with the current Microsoft Exchange Server 2013 Cumulative Update 23 configuration.

-   Missing group or AD problem.  

    Sample log like below.  

    This user account isn't a member of the 'Schema Admins' and/or 'Enterprise Admins' groups.  

    Make sure group membership. For schema and AD prepare, run it directly on DC server if possible.

-   xxx    Can't Perform Later Version of Exchange Installation in a mixed existing Hybrid Environment  

    a.Connect to Exchange Online PowerShell,  

    b.Output EXO Org Configuration file    Get-OrganizationConfig |Export-Clixml X:\EXO_OrgConfig.xml    c.Before install later version of Exchange, use the command to prepare AD with additional parameter as below.    Setup.exe /PrepareAD /TenantOrganizationConfig "X:\EXO_OrgConfig.xml" /IAcceptExchangeServerLicenseTerms  

    Note, you must specify the path location, directly point to the file name under the current CMD path, no use.

-   You must be a member of the 'Organization Management' role group or a member of the 'Enterprise Admins' group to continue.  

    The error may not always accurate. You may see this error even you do have the group membership.  

    The common cause is because the server run the command is not in the same site, same domain as schema master.  

    Two options:  

    a. Move schema master into same site, dc domain as the server you run setup.  

    b. Copy the exchange installation pack to DC which own schema master and prepare Schema/AD locally on DC.

-   Installation failed because service cannot stop properly.  

    Try the best practice to reboot server first before installing the CU/SU.

-   Installation failure caused by AV.  

      

    Follow the best practice , temporarily disable AV before apply the CU and SU.

-   SU installation failure with error below.  

      

    Try to follow the best practices to reboot server before installation of SU.  

    Verify if all exchange services can be stopped in time.

Author: Paolo Lin (Escalation Engineer at Microsoft)

## Answers

_No answers on this thread._
