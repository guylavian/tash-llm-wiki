---
title: "Test LDAPS Connection using Powershell [ADSI] and alternate credentials"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163878/test-ldaps-connection-using-powershell-adsi-and-al
question_id: 1163878
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Test LDAPS Connection using Powershell [ADSI] and alternate credentials

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163878/test-ldaps-connection-using-powershell-adsi-and-al (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a web server in a DMZ, and want to test a secure LDAP connection to the non-DMZ domain using alternate credentials. Is there a way to get Powershell to prompt for credentials with the [adsi] command?

I would like to be able to run [adsi]"LDAP://myadserver.mydomain.local:636" and have it prompt for user credentials. So far I am not having any luck.

Thanks for any help

## Answer (community) — community member

*upvotes: 1 · updated: 2023-01-25*

```
Hello there,

You can use Test-LDAP to verify whether LDAP and LDAPS are available on one or more Domain Controllers.

Function Test-LDAPConnection {
    [CmdletBinding()]
               
    # Parameters used in this function
    Param
    (
        [Parameter(Position=0, Mandatory = $True, HelpMessage="Provide domain controllers names, example DC01", ValueFromPipeline = $true)] 
        $DCs,
  
        [Parameter(Position=1, Mandatory = $False, HelpMessage="Provide port number for LDAP", ValueFromPipeline = $true)] 
        $Port = "636"
    ) 
  
    $ErrorActionPreference = "Stop"
    $Results = @()
    Try{ 
        Import-Module ActiveDirectory -ErrorAction Stop
    }
    Catch{
        $_.Exception.Message
        Break
    } 
         
    ForEach($DC in $DCs){
        $DC =$DC.trim()
        Write-Verbose "Processing $DC"
        Try{
            $DCName = (Get-ADDomainController -Identity $DC).hostname
        }
        Catch{
            $_.Exception.Message
            Continue
        }
  
        If($DCName -ne $Null){  
            Try{
                $Connection = [adsi]"LDAP://$($DCName):$Port"
            }
            Catch{
                $ExcMessage = $_.Exception.Message
                throw "Error: Failed to make LDAP connection. Exception: $ExcMessage"
            }
  
            If ($Connection.Path) {
                $Object = New-Object PSObject -Property ([ordered]@{ 
                       
                    DC                = $DC
                    Port              = $Port
                    Path              = $Connection.Path
                })
  
                $Results += $Object
            }         
        }
    }
  
    If($Results){
        Return $Results
    }

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--
```

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-01-24*

Try either of these:

```
$user = Read-Host "User: "
$password = Read-Host "Password: "
$ADSI = New-Object System.DirectoryServices.DirectoryEntry("LDAP://$OUPath", $username, $password)
```

```
$cred     = Get-Credential

$ADSI = New-Object System.DirectoryServices.DirectoryEntry("LDAP://$OUPath", $cred.UserName, $cred.GetNetworkCredential().Password
            )
```
