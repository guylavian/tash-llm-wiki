---
title: "Powershell scriptlogon GPO- It runs only for domain admin, but not domain users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/352366/powershell-scriptlogon-gpo-it-runs-only-for-domain
question_id: 352366
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Powershell scriptlogon GPO- It runs only for domain admin, but not domain users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/352366/powershell-scriptlogon-gpo-it-runs-only-for-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

I have a Powershell script runs as users login. I have tested , It runs if the user is domain admin, but does not run for domain users.

Set-ExecutionPolicy Bypass

$username=$env:username

$date=Get-Date -format M-d-yy-HHmm

$Source= "\FServer\Sharefolder\$username"

$Destination="\Fserver2\Sharefolder2\$username"

$Log="\Fileserver2\Sharefolder3\Temp\Log-$username-$date.txt"

If ($Source-and $Destination) {

ROBOCOPY $Source $Destination "/E" "/S" "/SEC" "/XD" "AppData" /LOG+:log

}

any help is appreciated.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-12*

Hello @Akiyo Hiroshi  ,    

Thank you for your posting here.    

If you logon one domain PC using one domain account, can you run the script successfully with this domain user?    

Best Regards,    

Daisy Zhou

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-11*

How do you know that it's not running? Have the script create a transcript into a local temp folder and see if you are just getting some error.   

```
Start-Transcript -path c:\Windows\temp\RemoveSig.log
... the script code goes here 
Stop-Transcript
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-10*

another important question,  

The parameter section: -executionpolicy Bypass, is that correct ?
