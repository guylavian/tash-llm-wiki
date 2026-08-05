---
title: "Uninstall Trend Micro Agend with GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/997158/uninstall-trend-micro-agend-with-gpo
question_id: 997158
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Uninstall Trend Micro Agend with GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/997158/uninstall-trend-micro-agend-with-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to make a script to  uninstall trend micro agent with GPO so I can apply this action to all computers to my organization.    

But it asks for a password to uninstall it.    

Do you have an ideas how to do it ?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-09*

Hello there,    

Was this application installed using GPO ?    

You can Uninstall using the application using GPO editor -> Edit- > Software Settings -> All Tasks, and then click Remove -> Click Immediately uninstall the software from users and computers, and then click OK.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software#remove-a-package    

Alternatively you can use below PowerShell script and run it from Server to Uninstall it Remotely.    

 $computerNames = @("ComputerName1", "rName2", "rName3")    

 $appName = "AnyDesk"    

 $yourAccount = Get-Credential    

 ForEach ($computerName in $computerNames) {    

     Invoke-Command -ComputerName $computerName -Credential $yourAccount -ScriptBlock {  

         Get-WmiObject Win32_product | Where {$.name -eq $appName} | ForEach {  

             $.Uninstall()  

         }  

     }  

 }    

--------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-09-07*

Might try asking them here in dedicated forums.    

https://success.trendmicro.com/forum/s/    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
