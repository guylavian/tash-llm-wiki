---
title: "RE: Manage recipients in Exchange Hybrid environments using Management tools"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1363212/re-manage-recipients-in-exchange-hybrid-environmen
question_id: 1363212
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# RE: Manage recipients in Exchange Hybrid environments using Management tools

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1363212/re-manage-recipients-in-exchange-hybrid-environmen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Morning/Afternoon Folks,

We have an Exchange Hybrid environment and recently moved all of our mailboxes to Exchange online. Our old exchange server is no longer a transport server (not relaying email) and is only functioning as a management server since we plan to continue utilizing local AD and Azure AD connect sync.

I've been planning to get rid of this server and have followed along with the following article:

https://learn.microsoft.com/en-us/Exchange/manage-hybrid-exchange-recipients-with-management-tools

We have the latest version of the Exchange management tools installed (Exchange Management Tools for Exchange Server 2019 CU12) but when we shutdown the final on-premise server (only shutting it down, we haven't run any of the cleanup tasks yet) we're unable to run the "Enable-RemoteMailbox" command to provision mailboxes in the cloud connected to local accounts.

Essentially all our scripts stop working... 

What am I missing? How can I continue to provision cloud mailboxes to connect them to local AD accounts (via powershell) without the "Enable-RemoteMailbox" command? How is this supposed to work?

I'm hoping I'm missing something obvious.

After I shutdown the on-premise exchange server this is what happens when I try to run the management tools:

```
Welcome to the Exchange Management Shell!
                                                                                                                                                                Full list of cmdlets: Get-Command                                                                                                                               Only Exchange cmdlets: Get-ExCommand                                                                                                                            Cmdlets that match a specific string: Help **                                                                                                           Get general help: Help
Get help for a cmdlet: Help  or  -?
Exchange team blog: Get-ExBlog
Show full output for a command:  | Format-List

Show quick reference guide: QuickRef
VERBOSE: Connecting to [[[REDACTED]]].
New-PSSession :[[[REDACTED]]] Connecting to remote server [[[REDACTED]]] failed with the following error
message : WinRM cannot complete the operation. Verify that the specified computer name is valid, that the computer is accessible over the network, and that a
firewall exception for the WinRM service is enabled and allows access from this computer. By default, the WinRM firewall exception for public profiles limits
access to remote computers within the same local subnet. For more information, see the about_Remote_Troubleshooting Help topic.
At line:1 char:1

[PS] C:\Windows\system32>

[PS] C:\Windows\system32>Enable-RemoteMailbox
Enable-RemoteMailbox : The term 'Enable-RemoteMailbox' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ Enable-RemoteMailbox
+ ~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (Enable-RemoteMailbox:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

[PS] C:\Windows\system32>
```

## Answers

_No answers on this thread._
