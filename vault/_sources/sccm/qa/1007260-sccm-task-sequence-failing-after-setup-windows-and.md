---
title: "SCCM Task Sequence failing after Setup Windows and Configuration Manager Task for Surface GO Lte"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1007260/sccm-task-sequence-failing-after-setup-windows-and
question_id: 1007260
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-updates"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM Task Sequence failing after Setup Windows and Configuration Manager Task for Surface GO Lte

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1007260/sccm-task-sequence-failing-after-setup-windows-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I hope you can help?     

SCCM Task Sequence failing after Setup Windows and Configuration Manager Task, It restarts try to install then just boots into Windows    

See SMSTS Log file below    

<![LOG[The action (Setup Windows and Configuration Manager) initiated a reboot request]LOG]!><time="10:35:33.039-60" date="09-07-2022" component="TSManager" context="" type="1" thread="2000" file="engine.cxx:1022">  

<![LOG[MP server https:/SERVERNAME. Ports 80,443. CRL=false.]LOG]!><time="10:35:33.039-60" date="09-07-2022" component="TSManager" context="" type="1" thread="2000" file="utils.cpp:7348">  

<![LOG[Setting authenticator]LOG]!><time="10:35:33.070-60" date="09-07-2022" component="TSManager" context="" type="1" thread="2000" file="utils.cpp:7370">  

<![LOG[Sending StatusMessage]LOG]!><time="10:35:33.086-60" date="09-07-2022" component="TSManager" context="" type="1" thread="2000" file="libsmsmessaging.cpp:4570">  

<![LOG[Setting the authenticator.]LOG]!><time="10:35:33.117-60" date="09-07-2022" component="TSManager" context="" type="0" thread="2000" file="libsmsmessaging.cpp:1617">  

<![LOG[CLibSMSMessageWinHttpTransport::Send: WinHttpOpenRequest - URL: SERVER:443 CCM_POST /ccm_system_AltAuth/request]LOG]!><time="10:35:33.120-60" date="09-07-2022" component="TSManager" context="" type="1" thread="2000" file="libsmsmessaging.cpp:9728">  

<![LOG[SSL, using authenticator in request.]LOG]!><time="10:35:33.120-60" date="09-07-2022" component="TSManager" context="" type="1" thread="2000" file="libsmsmessaging.cpp:9863">  

<![LOG[In SSL, but with no client cert.]LOG]!><time="10:35:33.120-60" date="09-07-2022" component="TSManager" context="" type="1" thread="2000" file="libsmsmessaging.cpp:9884">  

<![LOG[Request was successful.]LOG]!><time="10:35:33.183-60" date="09-07-2022" component="TSManager" context="" type="0" thread="2000" file="libsmsmessaging.cpp:10090">  

<![LOG[Server is no longer in use. Shutting down.]LOG]!><time="10:35:33.198-60" date="09-07-2022" component="TSProgressUI.exe" context="" type="1" thread="1076" file="winmain.cpp:154">  

<![LOG[****************************************************************************]LOG]!><time="10:35:33.198-60" date="09-07-2022" component="TSManager" context="" type="1" thread="2000" file="tsmanager.cpp:1287">  

5:33.198-60" date="09-07-2022" component="TSProgressUI.exe" context="" type="1" thread="1076" file="winmain.cpp:498">  

<![LOG[Execution engine result code: Reboot (2)]LOG]!><time="10:35:33.198-60" date="09-07-2022" component="TSManager" context="" type="2" thread="2000" file="tsmanager.cpp:1293">  

<![LOG[Shutdown complete.]LOG]!><time="10:35:33.198-60" date="09-07-2022" component="TSProgressUI.exe" context="" type="1" thread="1076" file="winmain.cpp:515">  

<![LOG[Process completed with exit code 2147945410]LOG]!><time="10:35:33.230-60" date="09-07-2022" component="TSMBootstrap" context="" type="0" thread="1988" file="CommandLine.cpp:1136">  

<![LOG[Task Sequence Manager returned code 0x80070BC2]LOG]!><time="10:35:33.230-60" date="09-07-2022" component="TSMBootstrap" context="" type="1" thread="1988" file="tsmediawizardcontrol.cpp:2264">  

<![LOG[Setting reboot required flag.]LOG]!><time="10:35:33.230-60" date="09-07-2022" component="TSMBootstrap" context="" type="0" thread="1988" file="tsmediawizardcontrol.cpp:2269">  

<![LOG[ThreadToResolveAndExecuteTaskSequence returned code 0x00000000]LOG]!><time="10:35:33.230-60" date="09-07-2022" component="TSMBootstrap" context="" type="1" thread="1668" file="tsmediaresolveprogresspage.cpp:221">  

<![LOG[ResolveProgressPage::OnWizardNext()]LOG]!><time="10:35:33.230-60" date="09-07-2022" component="TSMBootstrap" context="" type="0" thread="1668" file="tsmediaresolveprogresspage.cpp:113">  

<![LOG[Activating Finish Page.]LOG]!><time="10:35:33.230-60" date="09-07-2022" component="TSMBootstrap" context="" type="0" thread="1668" file="tsmediafinishpage.cpp:107">  

<![LOG[Execution complete.]LOG]!><time="10:35:34.528-60" date="09-07-2022" component="TSBootShell" context="" type="1" thread="632" file="bootshell.cpp:845">  

<![LOG[hMap != 0, HRESULT=80070002 (..\environmentscope.cpp,493)]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="0" thread="632" file="environmentscope.cpp:493">  

<![LOG[m_pGlobalScope->open(), HRESULT=80070002 (..\environmentlib.cpp,335)]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="0" thread="632" file="environmentlib.cpp:335">  

<![LOG[this->open(), HRESULT=80070002 (..\environmentlib.cpp,561)]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="0" thread="632" file="environmentlib.cpp:561">  

<![LOG[::RegQueryValueExW(hSubKey, szReg, NULL, NULL, NULL, &dwSize), HRESULT=80070002 (..\utils.cpp,1110)]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="0" thread="632" file="utils.cpp:1110">  

<![LOG[RegQueryValueExW is unsuccessful for Software\Microsoft\SMS\Task Sequence, SMSTSEndProgram]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="2" thread="632" file="utils.cpp:1110">  

<![LOG[GetTsRegValue() is unsuccessful. 0x80070002.]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="2" thread="632" file="utils.cpp:1141">  

<![LOG[End program: ]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="1" thread="632" file="bootshell.cpp:877">  

<![LOG[Finalizing logging from process 588]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="1" thread="632" file="tslogging.cpp:2110">  

<![LOG[Finalizing logs to root of first available drive]LOG]!><time="10:35:34.543-60" date="09-07-2022" component="TSBootShell" context="" type="1" thread="632" file="tslogging.cpp:1952">  

<![LOG[Successfully finalized logs to C:\SMSTSLog]LOG]!><time="10:35:34.555-60" date="09-07-2022" component="TSBootShell" context="" type="1" thread="632" file="tslogging.cpp:2009">  

<![LOG[Cleaning up task sequencing logging configuration.]LOG]!><time="10:35:34.555-60" date="09-07-2022" component="TSBootShell" context="" type="0" thread="632" file="tslogging.cpp:907">  

<![LOG[TS::Environment::SharedEnvironment.isInitialized() == true, HRESULT=80004005 (..\tslogging.cpp,694)]LOG]!><time="10:35:34.571-60" date="09-07-2022" component="TSBootShell" context="" type="0" thread="632" file="tslogging.cpp:694">  

<![LOG[TS environment is not initialized]LOG]!><time="10:35:34.571-60" date="09-07-2022" component="TSBootShell" context="" type="3" thread="632" file="tslogging.cpp:694">

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-15*

Hi ,

1,Could you please share the screenshot of your task sequence? Also look in the hidden folder C:\$WINDOWS.~BT\Sources\Panther to view the setuperr.log and setupact.log to see if there is any useful information.

2.Please add the correct NIC driver to have a try.

3,If possible, it's also recommended to create a new OSD task sequence with a new OS image to have a try.

Thanks for your time.

Best regards,  

Simon

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
