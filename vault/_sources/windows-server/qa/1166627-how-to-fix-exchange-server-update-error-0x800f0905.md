---
title: "How to fix Exchange Server Update error 0x800f0905 from KB5022291"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166627/how-to-fix-exchange-server-update-error-0x800f0905
question_id: 1166627
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# How to fix Exchange Server Update error 0x800f0905 from KB5022291

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166627/how-to-fix-exchange-server-update-error-0x800f0905 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have trouble updating our exchange server that runs on Windows Server 2022. The update cancels with error code 0x800f0905.

Already tried sfc /scannow and dism /online /Cleanup-Image /RestoreImage.

A manual install with dism command dism.exe /online /Add-Package /PackagePath:<Path to package> with the extraced .cab from the .msu shows the following messages in C:\Windows\Logs\DISM\dism.log:

2023-02-02 14:29:26, Info DISM DISM.EXE: <----- Starting Dism.exe session ----->

2023-02-02 14:29:26, Info DISM DISM.EXE:

2023-02-02 14:29:26, Info DISM DISM.EXE: Host machine information: OS Version=10.0.20348, Running architecture=amd64, Number of processors=52

2023-02-02 14:29:26, Info DISM DISM.EXE: Dism.exe version: 10.0.20348.681

2023-02-02 14:29:26, Info DISM DISM.EXE: Executing command line: dism.exe /online /Add-Package /PackagePath:"C:\install\Windows_Updates\Windows10.0-KB5022291-x64.cab" /PreventPending

2023-02-02 14:29:26, Info DISM DISM Manager: PID=28956 TID=35396 physical location path: C:\ - CDISMManager::CreateImageSession

2023-02-02 14:29:26, Info DISM DISM Manager: PID=28956 TID=35396 Event name for current DISM session is Global{84753909-39B7-4FF3-92AF-3F45499632D2} - CDISMManager::CheckSessionAndLock

2023-02-02 14:29:26, Info DISM DISM Manager: PID=28956 TID=35396 Create session event 0x204 for current DISM session and event name is Global{84753909-39B7-4FF3-92AF-3F45499632D2} - CDISMManager::CheckSessionAndLock

2023-02-02 14:29:26, Info DISM DISM Manager: PID=28956 TID=35396 Copying DISM from "C:\Windows\System32\Dism" - CDISMManager::CreateImageSessionFromLocation

2023-02-02 14:29:26, Info DISM DISM Manager: PID=28956 TID=35396 Successfully loaded the ImageSession at "C:\Users\adtb\AppData\Local\Temp\FA9EC918-2193-4A36-A718-C42BF25840E6" - CDISMManager::LoadRemoteImageSession

2023-02-02 14:29:26, Info DISM DISM Image Session: PID=42316 TID=43476 Instantiating the Provider Store. - CDISMImageSession::get_ProviderStore

2023-02-02 14:29:26, Info DISM DISM OS Provider: PID=42316 TID=43476 Defaulting SystemPath to C:\ - CDISMOSServiceManager::Final_OnConnect

2023-02-02 14:29:26, Info DISM DISM OS Provider: PID=42316 TID=43476 Defaulting Windows folder to C:\Windows - CDISMOSServiceManager::Final_OnConnect

2023-02-02 14:29:26, Info DISM DISM Provider Store: PID=42316 TID=43476 Attempting to initialize the logger from the Image Session. - CDISMProviderStore::Final_OnConnect

2023-02-02 14:29:26, Info DISM Initialized Panther logging at C:\Windows\Logs\DISM\dism.log

2023-02-02 14:29:26, Info DISM DISM Provider Store: PID=42316 TID=43476 Found and Initialized the DISM Logger. - CDISMProviderStore::Internal_InitializeLogger

2023-02-02 14:29:26, Info DISM Initialized Panther logging at C:\Windows\Logs\DISM\dism.log

2023-02-02 14:29:26, Info DISM Initialized Panther logging at C:\Windows\Logs\DISM\dism.log

2023-02-02 14:29:26, Info DISM DISM Manager: PID=28956 TID=35396 Image session successfully loaded from the temporary location: C:\Users\adtb\AppData\Local\Temp\FA9EC918-2193-4A36-A718-C42BF25840E6 - CDISMManager::CreateImageSession

2023-02-02 14:29:26, Info DISM DISM.EXE: Target image information: OS Version=10.0.20348.1129, Image architecture=amd64

2023-02-02 14:29:26, Info DISM DISM.EXE: Image session version: 10.0.20348.1

2023-02-02 14:29:26, Info DISM DISM Transmog Provider: PID=42316 TID=43476 Current image session is [ONLINE] - CTransmogManager::GetMode

2023-02-02 14:29:26, Info DISM DISM Transmog Provider: PID=42316 TID=43476 Audit Mode: [No] - CTransmogManager::Initialize

2023-02-02 14:29:26, Info DISM DISM Transmog Provider: PID=42316 TID=43476 GetProductType: ProductType = [ServerNT] - CTransmogManager::GetProductType

2023-02-02 14:29:26, Info DISM DISM Transmog Provider: PID=42316 TID=43476 Product Type: [ServerNT] - CTransmogManager::Initialize

2023-02-02 14:29:26, Info DISM DISM Transmog Provider: PID=42316 TID=43476 Product Type ServerNT : [Yes] - CTransmogManager::Initialize

2023-02-02 14:29:27, Info CSI 00000001 Shim considered [l:126]'??\C:\Windows\Servicing\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_10.0.20348.1300_none_b1d41586f9830306\wcp.dll' : got STATUS_OBJECT_PATH_NOT_FOUND

2023-02-02 14:29:27, Info CSI 00000002 Shim considered [l:123]'??\C:\Windows\WinSxS\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_10.0.20348.1300_none_b1d41586f9830306\wcp.dll' : got STATUS_SUCCESS

2023-02-02 14:29:27, Info DISM DISM Driver Manager: PID=42316 TID=43476 Further logs for driver related operations can be found in the target operating system at %WINDIR%\inf\setupapi.offline.log - CDriverManager::Initialize

2023-02-02 14:29:27, Info CSI 00000001 Shim considered [l:126]'??\C:\Windows\Servicing\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_10.0.20348.1300_none_b1d41586f9830306\wcp.dll' : got STATUS_OBJECT_PATH_NOT_FOUND

2023-02-02 14:29:27, Info CSI 00000002 Shim considered [l:123]'??\C:\Windows\WinSxS\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_10.0.20348.1300_none_b1d41586f9830306\wcp.dll' : got STATUS_SUCCESS

2023-02-02 14:29:27, Info DISM DISM OS Provider: PID=42316 TID=43476 Determined System directory to be C:\Windows\System32 - CDISMOSServiceManager::get_SystemDirectory

2023-02-02 14:29:27, Info DISM DISM Package Manager: PID=42316 TID=43476 Finished initializing the CbsConUI Handler. - CCbsConUIHandler::Initialize

2023-02-02 14:29:27, Info CSI 00000001 Shim considered [l:126]'??\C:\Windows\Servicing\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_10.0.20348.1300_none_b1d41586f9830306\wcp.dll' : got STATUS_OBJECT_PATH_NOT_FOUND

2023-02-02 14:29:27, Info CSI 00000002 Shim considered [l:123]'??\C:\Windows\WinSxS\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_10.0.20348.1300_none_b1d41586f9830306\wcp.dll' : got STATUS_SUCCESS

2023-02-02 14:29:27, Info DISM DISM Package Manager: PID=42316 TID=43476 CBS is being initialized for online use. More information about CBS actions can be located at: %windir%\logs\cbs\cbs.log - CDISMPackageManager::Initialize

2023-02-02 14:29:27, Info DISM DISM Package Manager: PID=42316 TID=43476 Loaded servicing stack for online use only. - CDISMPackageManager::CreateCbsSession

2023-02-02 14:29:27, Info DISM DISM Package Manager: PID=42316 TID=43476 Processing the top level command token(add-package). - CPackageManagerCLIHandler::Private_ValidateCmdLine

2023-02-02 14:29:27, Info DISM DISM Package Manager: PID=42316 TID=43476 Attempting to route to appropriate command handler. - CPackageManagerCLIHandler::ExecuteCmdLine

2023-02-02 14:29:27, Info DISM DISM Package Manager: PID=42316 TID=43476 Routing the command... - CPackageManagerCLIHandler::ExecuteCmdLine

2023-02-02 14:29:27, Info DISM DISM Package Manager: PID=42316 TID=43476 Encountered the option "packagepath" with value "C:\install\Windows_Updates\Windows10.0-KB5022291-x64.cab" - CPackageManagerCLIHandler::Private_GetPackagesFromCommandLine

2023-02-02 14:29:28, Info DISM DISM Package Manager: PID=42316 TID=43476 Package Multiple_Packages~~~~0.0.0.0 with CBS state 0(CbsInstallStateAbsent) being mapped to dism state 1(DISM_INSTALL_STATE_NOTPRESENT) - CDISMPackage::LogInstallStateMapping

2023-02-02 14:29:28, Info DISM DISM Package Manager: PID=42316 TID=43476 Initiating Changes on Package with values: 4, 7 - CDISMPackage::Internal_ChangePackageState

2023-02-02 14:29:28, Info DISM DISM Package Manager: PID=42316 TID=43476 CBS session options=0x10100! - CDISMPackageManager::Internal_Finalize

2023-02-02 14:31:29, Info DISM DISM Package Manager: PID=42316 TID=34280 Error in operation: (null) (CBS HRESULT=0x800f0905) - CCbsConUIHandler::Error

2023-02-02 14:31:29, Error DISM DISM Package Manager: PID=42316 TID=43476 Failed finalizing changes. - CDISMPackageManager::Internal_Finalize(hr:0x800f0905)

2023-02-02 14:31:29, Error DISM DISM Package Manager: PID=42316 TID=43476 Failed processing package changes with session options - CDISMPackageManager::ProcessChangesWithOptions(hr:0x800f0905)

2023-02-02 14:31:29, Info DISM DISM Package Manager: PID=42316 TID=43476 Loaded servicing stack for online use only. - CDISMPackageManager::CreateCbsSession

2023-02-02 14:31:29, Error DISM DISM Package Manager: PID=42316 TID=43476 Failed while processing command add-package. - CPackageManagerCLIHandler::ExecuteCmdLine(hr:0x800f0905)

2023-02-02 14:31:29, Info DISM DISM Package Manager: PID=42316 TID=43476 Further logs for online package and feature related operations can be found at %WINDIR%\logs\CBS\cbs.log - CPackageManagerCLIHandler::ExecuteCmdLine

2023-02-02 14:31:29, Error DISM DISM.EXE: DISM Package Manager processed the command line but failed. HRESULT=800F0905

2023-02-02 14:31:29, Info DISM DISM Package Manager: PID=42316 TID=43476 Finalizing CBS core. - CDISMPackageManager::Finalize

2023-02-02 14:32:05, Info DISM DISM Manager: PID=28956 TID=35396 Closing session event handle 0x204 - CDISMManager::CleanupImageSessionEntry

2023-02-02 14:32:05, Info DISM DISM.EXE: Image session has been closed. Reboot required=no.

2023-02-02 14:32:05, Info DISM DISM.EXE:

2023-02-02 14:32:05, Info DISM DISM.EXE: <----- Ending Dism.exe session ----->

I do not want to start an in-place upgrade repair, because that always seems to destroy Exchange.

Do you guys have any other ideas?

## Answers

_No answers on this thread._
