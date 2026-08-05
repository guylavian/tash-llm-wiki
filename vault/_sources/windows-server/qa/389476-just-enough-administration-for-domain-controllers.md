---
title: "Just Enough Administration for Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/389476/just-enough-administration-for-domain-controllers
question_id: 389476
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-powershell"]
answer_author_affiliations: ["Mvp"]
---
# Just Enough Administration for Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/389476/just-enough-administration-for-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am building a JEA file for Domain Controllers, one file will be to perform read only items, the second file would be to perform certain executable/ change items like restart services or do role activities.  

I have read the various documentation out there but have not seen anything regarding domain controllers... What would be ideal to have in a DC jea file?  

If there a JEA template out there with settings ideal for Domain Controllers?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-12*

Hi,  

Glad your problem has been solved  

Best wishes  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-11*

Just checking if there's any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-11*

Hi,    

Thank you for posting in our forum.    

First of all, create a configuration file of a PowerShell session (*.pssc). To do it, run this command on your domain controller:    

New-PSSessionConfigurationFile -Path 'C:\Program Files\WindowsPowerShell\dc_manage.pssc'    

Open the PSSC file using the Notepad.    

The PSSC file sets who may connect to this JEA endpoint and under what account the commands in the JEA session will run.    

Modify the following values:    

SessionType from Default to RestrictedRemoteServer. This mode allows to use the following PowerShell cmdlets: Clear-Host, Exit-PSSession, Get-Command, Get-FormatData, Get-Help, Measure-Object, Out-Default or Select-Objectl    

Specify a folder (create it) in the TranscriptDirectory parameter. Here you will log all JEA user actions: TranscriptDirectory = C:\PS\JEA_logs    

The RunAsVirtualAccount option allows to run commands under a virtual administrator account (member of the local Administrator or Domain Administrator group): RunAsVirtualAccount = $true    

For specific steps, please refer to the link provided by Patrick. The following link can give you some information:    

https://docs.servicenow.com/bundle/quebec-it-operations-management/page/product/discovery/concept/microsoft-jea-discovery.html    

https://learn.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/session-configurations?view=powershell-7.1    

Hope this information can help you    

Best wishes    

Vicky
