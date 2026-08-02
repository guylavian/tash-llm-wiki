---
title: "How to  multiple url to a GPO setting listbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/107003/how-to-multiple-url-to-a-gpo-setting-listbox
question_id: 107003
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# How to  multiple url to a GPO setting listbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/107003/how-to-multiple-url-to-a-gpo-setting-listbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I created a GPO which I have to set more than 1000 urls in order to allow cookies.    

I found the policy but  I don't know how toadd all my 1000 urls. From the window  of the policy (attached file) I can add one url at time.    

Does somebody can helpme please. It's may possible by powershell or other things?    

Thank you by advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-29*

Hi,@SAKHO Mohamed (Externe)       

Dear user, thank you for posting in our forum.    

Seeing that you have consulted this question on the forum before, we can add multiple URLs through GPO, but the method is the same as yours, and you can only add them one by one.    

If you want to add in batches, you can try to use the method of deploying a boot script, but our ADDS forum does not provide a script method, you can go to the script forum to follow the help    

Links are scripted:https://social.technet.microsoft.com/Forums/Windows/en-US/home?forum=winserverpowershell    

Hope this information can help you    

Best wishes    

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-25*

I already saw this answer, but what I need is for Microsoft Edge, I already launch the LGPO.exe to know which registry to set for this setting, but on the client the key doesn't exist.    

https://learn.microsoft.com/en-us/answers/questions/107003/how-to-multiple-url-to-a-gpo-setting-listbox.html

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-25*

Hi，@SAKHO Mohamed (Externe)  

Starting from 2008R2 ADDS introduce a PowerShell module for managing GPO called “GroupPolicy”. In this module there is a cmdlet called Set-GPRegistryValue this type of policy can configure registry-based Policy.  

With the settings collected from the LGPO I’m able to use this cmdlet to set the 700 Urls:

=====================================================

Read Urls from a file on disk.

$Urls = get-Content .Urls.txt

Build a loop to add all the Urls to the specified CPO.

foreach ($Url in $Urls)  

{

```
Set-GPRegistryValue -Name ListBoxGPO -ValueName $Url -Type String -Value $Url -Key “HKLMSOFTWAREPoliciesMicrosoftWindowsCurrentVersionInternet SettingsRestrictedProtocols1”
```

}

=====================================================

Verify correct execution of the script by editing the GPO from the GPMC and check the content of the Listbox:

Hope this information can help you  

Best wishes  

Vicky
