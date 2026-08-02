---
title: "Connect-exchangeonline will not load due to unsigned files in temp directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/285595/connect-exchangeonline-will-not-load-due-to-unsign
question_id: 285595
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Connect-exchangeonline will not load due to unsigned files in temp directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/285595/connect-exchangeonline-will-not-load-due-to-unsign (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Powershell 5.1, Exchangeonlinemanagement installed from psgallery with install-module exchangeonlinemanagement.  

Module v 2.0.4 installed to C:\Program Files\WindowsPowerShell\Modules

After running "connect-exchangeonline", successfully authenticating with 2FA, the session is generated and then the screen errors with

Import-Module : Errors occurred while loading the format data file:  

C:\temp\temp\tmp_vexfwmg2.gol\tmp_vexfwmg2.gol.format.ps1xml, , C:\temp\temp\tmp_vexfwmg2.gol\tmp_vexfwmg2.gol.format.ps1xml: The file was skipped because of the following validation exception: File C:\temp\temp\tmp_vexfwmg2.gol\tmp_vexfwmg2.gol.format.ps1xml cannot be loaded. The file C:\temp\temp\tmp_vexfwmg2.gol\tmp_vexfwmg2.gol.format.ps1xml is not digitally signed. You cannot run this script on the current system. For more information about running scripts and setting execution policy, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.. At line:3 char:17  

-  ... Import-Module -Name $name -Alias * -Function * -Prefix $p ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : InvalidOperation: (:) [Import-Module], RuntimeException  

-  FullyQualifiedErrorId : FormatXmlUpdateException,Microsoft.PowerShell.Commands.ImportModuleCommand

get-executionpolicy shows remotesigned (as expected).  

Set-executionpolicy unrestricted allows the install to continue and connect to exchange but obviously that's a bad idea.

Why is the module generating local files in my temp directory (that change everytime so I can't unblock them) ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-24*

@absoblogginlutely      

Here is the configuration on my computer:    

    

I could install ExchangeOnlineManagement module and connect successfully:    

    

I would suggest you uninstall and install this module again. After uninstalling this module, you need to close and open a new PowerShell windows.    

If you still cannot use this module successfully, I think there may exist some issue with your PowerShell 5.1, you can try to install PS 7.0 on your computer and install this module in it.    

If you cannot connect to Exchange online with PS7.0, you could post this issue in PowerShell github, that project mainly collect and solve issue with PowerShell to improve the experience of using PowerShell.     

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
