---
title: "exchange 2016 cu20 fail to instal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/343369/exchange-2016-cu20-fail-to-instal
question_id: 343369
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange 2016 cu20 fail to instal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/343369/exchange-2016-cu20-fail-to-instal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi dear expert

we trying install cu20 on exchange 2016 but we get below error

please give me hand ti fix my issue

I'm new to exchange

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LocalService /t REG_SZ /d `"wsbexchange`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LaunchPermission /t REG_BINARY /d `"010004806000000070000000000000001400000002004c0003000000000014001f000000010100000000000512000000000018001f000000010200000000000520000000200200000000180003000000010200000000000520000000270200000102000000000005200000002002000001020000000000052000000020020000`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\wsbexchange.exe`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`"  /v `"Application Identifier`" /t REG_SZ /d Exchange /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`" /v CLSID /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMarkDbRecoverable /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMountOnPITRecovery /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$servicecmd" -Args:"create wsbexchange binpath= `"$WsbBinPath`" type= own start= demand error= ignore obj= LocalSystem DisplayName= `"Microsoft Exchange Server Extension for Windows Server Backup`"";
          Start-SetupProcess -Name:"$servicecmd" -Args:"description wsbexchange `"Enables Windows Server Backup users to back up and recover application data for Microsoft Exchange Server.`"";
     }
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1.
```

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LocalService /t REG_SZ /d `"wsbexchange`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LaunchPermission /t REG_BINARY /d `"010004806000000070000000000000001400000002004c0003000000000014001f000000010100000000000512000000000018001f000000010200000000000520000000200200000000180003000000010200000000000520000000270200000102000000000005200000002002000001020000000000052000000020020000`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\wsbexchange.exe`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`"  /v `"Application Identifier`" /t REG_SZ /d Exchange /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`" /v CLSID /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMarkDbRecoverable /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMountOnPITRecovery /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$servicecmd" -Args:"create wsbexchange binpath= `"$WsbBinPath`" type= own start= demand error= ignore obj= LocalSystem DisplayName= `"Microsoft Exchange Server Extension for Windows Server Backup`"";
          Start-SetupProcess -Name:"$servicecmd" -Args:"description wsbexchange `"Enables Windows Server Backup users to back up and recover application data for Microsoft Exchange Server.`"";
     }
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1.
```

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LocalService /t REG_SZ /d `"wsbexchange`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LaunchPermission /t REG_BINARY /d `"010004806000000070000000000000001400000002004c0003000000000014001f000000010100000000000512000000000018001f000000010200000000000520000000200200000000180003000000010200000000000520000000270200000102000000000005200000002002000001020000000000052000000020020000`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\wsbexchange.exe`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`"  /v `"Application Identifier`" /t REG_SZ /d Exchange /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`" /v CLSID /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMarkDbRecoverable /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMountOnPITRecovery /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$servicecmd" -Args:"create wsbexchange binpath= `"$WsbBinPath`" type= own start= demand error= ignore obj= LocalSystem DisplayName= `"Microsoft Exchange Server Extension for Windows Server Backup`"";
          Start-SetupProcess -Name:"$servicecmd" -Args:"description wsbexchange `"Enables Windows Server Backup users to back up and recover application data for Microsoft Exchange Server.`"";
     }
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1.
```

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LocalService /t REG_SZ /d `"wsbexchange`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LaunchPermission /t REG_BINARY /d `"010004806000000070000000000000001400000002004c0003000000000014001f000000010100000000000512000000000018001f000000010200000000000520000000200200000000180003000000010200000000000520000000270200000102000000000005200000002002000001020000000000052000000020020000`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\wsbexchange.exe`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`"  /v `"Application Identifier`" /t REG_SZ /d Exchange /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`" /v CLSID /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMarkDbRecoverable /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMountOnPITRecovery /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$servicecmd" -Args:"create wsbexchange binpath= `"$WsbBinPath`" type= own start= demand error= ignore obj= LocalSystem DisplayName= `"Microsoft Exchange Server Extension for Windows Server Backup`"";
          Start-SetupProcess -Name:"$servicecmd" -Args:"description wsbexchange `"Enables Windows Server Backup users to back up and recover application data for Microsoft Exchange Server.`"";
     }
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1.
```

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LocalService /t REG_SZ /d `"wsbexchange`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LaunchPermission /t REG_BINARY /d `"010004806000000070000000000000001400000002004c0003000000000014001f000000010100000000000512000000000018001f000000010200000000000520000000200200000000180003000000010200000000000520000000270200000102000000000005200000002002000001020000000000052000000020020000`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\wsbexchange.exe`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`"  /v `"Application Identifier`" /t REG_SZ /d Exchange /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`" /v CLSID /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMarkDbRecoverable /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMountOnPITRecovery /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$servicecmd" -Args:"create wsbexchange binpath= `"$WsbBinPath`" type= own start= demand error= ignore obj= LocalSystem DisplayName= `"Microsoft Exchange Server Extension for Windows Server Backup`"";
          Start-SetupProcess -Name:"$servicecmd" -Args:"description wsbexchange `"Enables Windows Server Backup users to back up and recover application data for Microsoft Exchange Server.`"";
     }
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1.
```

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LocalService /t REG_SZ /d `"wsbexchange`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LaunchPermission /t REG_BINARY /d `"010004806000000070000000000000001400000002004c0003000000000014001f000000010100000000000512000000000018001f000000010200000000000520000000200200000000180003000000010200000000000520000000270200000102000000000005200000002002000001020000000000052000000020020000`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\wsbexchange.exe`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`"  /v `"Application Identifier`" /t REG_SZ /d Exchange /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`" /v CLSID /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMarkDbRecoverable /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMountOnPITRecovery /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$servicecmd" -Args:"create wsbexchange binpath= `"$WsbBinPath`" type= own start= demand error= ignore obj= LocalSystem DisplayName= `"Microsoft Exchange Server Extension for Windows Server Backup`"";
          Start-SetupProcess -Name:"$servicecmd" -Args:"description wsbexchange `"Enables Windows Server Backup users to back up and recover application data for Microsoft Exchange Server.`"";
     }
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1.
```

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LocalService /t REG_SZ /d `"wsbexchange`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LaunchPermission /t REG_BINARY /d `"010004806000000070000000000000001400000002004c0003000000000014001f000000010100000000000512000000000018001f000000010200000000000520000000200200000000180003000000010200000000000520000000270200000102000000000005200000002002000001020000000000052000000020020000`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\wsbexchange.exe`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`"  /v `"Application Identifier`" /t REG_SZ /d Exchange /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`" /v CLSID /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMarkDbRecoverable /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMountOnPITRecovery /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$servicecmd" -Args:"create wsbexchange binpath= `"$WsbBinPath`" type= own start= demand error= ignore obj= LocalSystem DisplayName= `"Microsoft Exchange Server Extension for Windows Server Backup`"";
          Start-SetupProcess -Name:"$servicecmd" -Args:"description wsbexchange `"Enables Windows Server Backup users to back up and recover application data for Microsoft Exchange Server.`"";
     }
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1.
```

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LocalService /t REG_SZ /d `"wsbexchange`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v LaunchPermission /t REG_BINARY /d `"010004806000000070000000000000001400000002004c0003000000000014001f000000010100000000000512000000000018001f000000010200000000000520000000200200000000180003000000010200000000000520000000270200000102000000000005200000002002000001020000000000052000000020020000`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\wsbexchange.exe`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`"  /v `"Application Identifier`" /t REG_SZ /d Exchange /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WindowsServerBackup\Application Support\{76fe1ac4-15f7-4bcd-987e-8e1acb462fb7}`" /v CLSID /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMarkDbRecoverable /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKLM\Software\Microsoft\windows nt\currentversion\WSBAppExchangeHelper`" /v AutoMountOnPITRecovery /t REG_DWORD /d 1 /f";
          Start-SetupProcess -Name:"$servicecmd" -Args:"create wsbexchange binpath= `"$WsbBinPath`" type= own start= demand error= ignore obj= LocalSystem DisplayName= `"Microsoft Exchange Server Extension for Windows Server Backup`"";
          Start-SetupProcess -Name:"$servicecmd" -Args:"description wsbexchange `"Enables Windows Server Backup users to back up and recover application data for Microsoft Exchange Server.`"";
     }
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1.
```

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))
          {
                if ((get-service wsbexchange).Status -eq "Running")
                {
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";
                }
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";
          }

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\APPID\{D8A2E312-3B17-4293-B71E-
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-05*

we resolve our issue   

the problem cause all services stopped and no run automatically

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-05*

Hi @ramin sa      

Is this a newly installed Exchange server or you are upgrading it?    

Have you checked that you have meet all Exchange Server prerequisites list in the official document?    

You could also refer to the below step-by-step guide to perform the installation    

Installing Exchange 2016 on Windows Server 2016 Step by Step    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-04*

The error message indicates that there are certain pre-requisites verification failed. Most probably, the Visual C++ version installation need to be checked. Check, if the correct version of Visual C++ version is installed. After fixing that, try the installation again.
