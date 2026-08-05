---
title: "runspacepool - disconnect exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/278384/runspacepool-disconnect-exchange-online
question_id: 278384
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# runspacepool - disconnect exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/278384/runspacepool-disconnect-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello

I work with a large tenant (100k mailbox), so i'm trying different methods to speed up my scripts.  

Currently i'm doing a get-mailboxstatistics + get-mailboxpermission on all mailbox, and it takes a VERY long time, more than 24 hours.

All my code is ok, except one point : I'm using the new module "Exchange online v2", and i can't figure out how to call the function "disconnect-exchangeonline" when the runspacepool is closed !

Here is a sample code :

```
$curScriptPath = Split-Path -parent $MyInvocation.MyCommand.Definition

$ScriptBlock = {
Param($num)

"num=$num"

$p=Get-mailbox XXXXXXXX -erroraction stop |select primarysmtpaddress
"primarysmtpaddress=$($p.primarysmtpaddress)"

$totalitemsize=Get-o365mailboxstatistics XXXXXXXX -erroraction stop |select totalitemsize
"totalitemsize=$($totalitemsize.totalitemsize)"
}

$RunspaceCollection = @()

#Connect O365 using module Exchange Online v2 (i had to include all this in another file ".ps1", i did not figured out how to add it "dynamically")
$initialSessionState = [System.Management.Automation.Runspaces.InitialSessionState]::CreateDefault2()
$initialSessionState.Variables.Add((New-Object -TypeName System.Management.Automation.Runspaces.SessionStateVariableEntry -ArgumentList "CommandName", @("Get-Mailbox", "Get-MailboxStatistics"), $null) )
$initialSessionState.StartupScripts.Add("$curScriptPath\Connect-O365.ps1")

#Create runspace pool
$runspacepool = [runspacefactory]::CreateRunspacePool(1, 3, $initialSessionState, $Host)
$RunspacePool.Open()

0..10 | % {
    $Powershell = [PowerShell]::Create().AddScript($ScriptBlock).AddArgument($_)

    #Specify runspace to use
    $Powershell.RunspacePool = $RunspacePool

    #Create Runspace collection
    [Collections.Arraylist]$RunspaceCollection += New-Object -TypeName PSObject -Property @{
        Runspace = $PowerShell.BeginInvoke()
        PowerShell = $PowerShell  
    }
}

#Get return of each call
While($RunspaceCollection){
    Foreach($Runspace in $RunspaceCollection.ToArray()){
        If($Runspace.Runspace.IsCompleted){
            $Runspace.PowerShell.EndInvoke($Runspace.Runspace)
            $Runspace.PowerShell.Dispose()
            $RunspaceCollection.Remove($Runspace)
        }
    }
}
$RunspacePool.Close()
$RunspacePool.Dispose()
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-16*

Update : I found some sort of a "solution", but i'm not sure it's completely OK as now I don't use this code anymore, i use the "EXO" cmdlets from the module "Exchange Online Powershell v2", and it seems reliable.  

The solution I think of is to add some "fake" items to the runspacecollection to deal with the "disconnect", here is the updated pseudo-code (i could not identify my updates, the main part is the addition of a parameter "disconnect" to the scriptBlock).

```
$curScriptPath = Split-Path -parent $MyInvocation.MyCommand.Definition

$ScriptBlock = {
    Param($num,$disconnect)

    if ($disconnect) {
        Disconnect-ExchangeOnline -Confirm:$false
    }
    else {
        num=$num"

        $p=Get-mailbox XXXXXXXX -erroraction stop |select primarysmtpaddress
        "primarysmtpaddress=$($p.primarysmtpaddress)"

        $totalitemsize=Get-o365mailboxstatistics XXXXXXXX -erroraction stop |select totalitemsize
        "totalitemsize=$($totalitemsize.totalitemsize)"
    }
}

$RunspaceCollection = @()
```

Connect O365 using module Exchange Online v2 (i had to include all this in another file ".ps1", i did not figured out how to add it "dynamically")

```
$initialSessionState = [System.Management.Automation.Runspaces.InitialSessionState]::CreateDefault2()
$initialSessionState.Variables.Add((New-Object -TypeName System.Management.Automation.Runspaces.SessionStateVariableEntry -ArgumentList "CommandName", @("Get-Mailbox", "Get-MailboxStatistics"), $null) )
$initialSessionState.StartupScripts.Add("$curScriptPath\Connect-O365.ps1")
```

Create runspace pool

```
$maxThreads = 3
$runspacepool = [runspacefactory]::CreateRunspacePool(1, $maxThreads, $initialSessionState, $Host)
$RunspacePool.Open()

0..10 | % {
    $Powershell = [PowerShell]::Create().AddScript($ScriptBlock).AddArgument($_)
```

Specify runspace to use

```
$Powershell.RunspacePool = $RunspacePool
```

Create Runspace collection

```
[Collections.Arraylist]$RunspaceCollection += New-Object -TypeName PSObject -Property @{
        Runspace = $PowerShell.BeginInvoke()
        PowerShell = $PowerShell  
    }
}
```

add some "fake" items to the runspacecollection to deal with the "disconnect", 1 per thread

```
$disconnect=$true
1..$maxThreads | % {
    $Powershell = [PowerShell]::Create().AddScript($ScriptBlock).AddArgument($_).AddArgument($disconnect)
    $Powershell.RunspacePool = $RunspacePool    #Specify runspace pool to use
```

Add runspace in Runspace collection

```
[Collections.Arraylist]$RunspaceCollection += New-Object -TypeName PSObject -Property @{
        Runspace = $PowerShell.BeginInvoke()
        PowerShell = $PowerShell
    }
}
```

Get return of each call

```
While($RunspaceCollection){
    Foreach($Runspace in $RunspaceCollection.ToArray()){
        If($Runspace.Runspace.IsCompleted){
        $Runspace.PowerShell.EndInvoke($Runspace.Runspace)
        $Runspace.PowerShell.Dispose()
        $RunspaceCollection.Remove($Runspace)
        }
    }
}
$RunspacePool.Close()
$RunspacePool.Dispose()
```
