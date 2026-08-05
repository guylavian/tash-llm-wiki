---
title: "Exchange 2019 installation error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1114010/exchange-2019-installation-error
question_id: 1114010
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 installation error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1114010/exchange-2019-installation-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In order to phase out our aging Exchange 2013 system, we're opting to go for an Exchange 2019 installation. The goal is to install Exchange 2019 on-prem, next to the Exchange 2013 machine, and gradually move the local mailboxes and roles over (SMTP, communication with Exchange Online and so forth), with the endgoal of removing the Exchange 2013 machine. Exchange 2013 is currently set up in a hybrid environment where the bulk of the storage and mailing is handled by Exchange Online. However there are some mailboxes and functionality that we need on-premise to justify a server being kept.     

We created a new VM, and issued the installation of the Exchange 2019 setup after fulfilling all the pre-requisites. During the setup however (specifically step 9, Mailbox role), the installation errors out and we're just presented with an 'Exit' button to close the installation. On the next run of the installation, the incomplete installation is detected, and automatically resumed, again erroring out  at the same step.     

While the error is elaborate (included for completion sake below), it boils down to two notices (which we found have little to nothing on when searching the internet, tho other similar errors have popped up here and there):    

"Microsoft.Exchange.Management.Tasks.RecipientTaskException: Enable-Mailbox on this mail user is disallowed because the mailbox has been migrated.    

"System.Management.Automation.ParameterBindingValidationException: Cannot bind argument to parameter 'Identity' because it is null.    

The first seems to hail (according to the Exchange logs) from one of the SystemMailbox accounts, which we verified on the ECP of the old 2013 server to have been migrated to the Office365 environment. I surmise the second is (for now) a result of the first.     

The Exchange 2019 server is at present showing up in the on prem organization of mailservers, tho the installation has (as stated) not yet run to completion.     

We're unsure how to proceed.     

A possible migration of the SystemMailbox from Office365 to on-prem, would be the most obvious answer, but this doesn't seem possible to do from the GUI. Might still be possible using Powershell tho, but unsure how to exactly go about that. Also, the SystemMailbox was not manually migrated by us, so we're also unsure what might break if we start moving that thing. Also note that we're unsure if that will even fix the issue with the install.     

Other than that we might try to uninstall Exchange (where I'm assuming it would remove the server from the on-prem Exchange environment, and just completely clean up it's installation. Which we may follow-up with a reinstallation from scratch. But prior to possibly causing issues with the environment we're holding off on that in waiting for possible further insights from the community.     

I'm hoping someone in the community may have some insight in what is going on here, and how we can resolve the issue at hand.     

Below the full error presented:    

```
Error:  
The following error was generated when "$error.Clear();   
            if (!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated)  
            {  
                $mailboxId = "SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}";  
                $displayName = "E4E Encryption Store - Active";  
  
                $existingArbitrationMailboxes = @(Get-Mailbox -Arbitration -Filter {Name -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);  
                if ($existingArbitrationMailboxes.Length -eq 0)  
                {  
                    $mailboxDatabase = @(get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);  
                    if ($mailboxDatabase.Length -ne 0)  
                    {  
                        $mailboxUsers = @(Get-User -Filter {LastName -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);  
                        if ($mailboxUsers.Length -ne 0)  
                        {  
                            $orgMailbox = Enable-Mailbox -Arbitration -Identity $mailboxUsers[0] -Database $mailboxDatabase[0].Identity;  
                            Set-Mailbox -Arbitration `  
                                -Identity $orgMailbox `  
                                -RequireSenderAuthenticationEnabled $false `  
                                -UseDatabaseQuotaDefaults $false `  
                                -SCLDeleteEnabled $false `  
                                -SCLJunkEnabled $false `  
                                -SCLQuarantineEnabled $false `  
                                -SCLRejectEnabled $false `  
                                -HiddenFromAddressListsEnabled $true `  
                                -DisplayName $displayName `  
                                -Force;  
                        }  
                    }  
                }  
            }  
        " was run: "Microsoft.Exchange.Management.Tasks.RecipientTaskException: Enable-Mailbox on this mail user is disallowed because the mailbox has been migrated.  
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  
   at Microsoft.Exchange.Management.RecipientTasks.EnableMailbox.PrepareRecipientObject(ADUser& user)  
   at Microsoft.Exchange.Management.RecipientTasks.EnableRecipientObjectTask`2.PrepareDataObject()  
   at Microsoft.Exchange.Configuration.Tasks.SetTaskBase`1.InternalValidate()  
   at Microsoft.Exchange.Configuration.Tasks.RecipientObjectActionTask`2.InternalValidate()  
   at Microsoft.Exchange.Management.RecipientTasks.EnableMailbox.InternalValidate()  
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()  
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".  
  
Error:  
The following error was generated when "$error.Clear();   
            if (!$RoleIsDatacenter -and !$RoleIsDatacenterDedicated)  
            {  
                $mailboxId = "SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}";  
                $displayName = "E4E Encryption Store - Active";  
  
                $existingArbitrationMailboxes = @(Get-Mailbox -Arbitration -Filter {Name -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);  
                if ($existingArbitrationMailboxes.Length -eq 0)  
                {  
                    $mailboxDatabase = @(get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);  
                    if ($mailboxDatabase.Length -ne 0)  
                    {  
                        $mailboxUsers = @(Get-User -Filter {LastName -eq $mailboxId} -IgnoreDefaultScope -ResultSize 1);  
                        if ($mailboxUsers.Length -ne 0)  
                        {  
                            $orgMailbox = Enable-Mailbox -Arbitration -Identity $mailboxUsers[0] -Database $mailboxDatabase[0].Identity;  
                            Set-Mailbox -Arbitration `  
                                -Identity $orgMailbox `  
                                -RequireSenderAuthenticationEnabled $false `  
                                -UseDatabaseQuotaDefaults $false `  
                                -SCLDeleteEnabled $false `  
                                -SCLJunkEnabled $false `  
                                -SCLQuarantineEnabled $false `  
                                -SCLRejectEnabled $false `  
                                -HiddenFromAddressListsEnabled $true `  
                                -DisplayName $displayName `  
                                -Force;  
                        }  
                    }  
                }  
            }  
        " was run: "System.Management.Automation.ParameterBindingValidationException: Cannot bind argument to parameter 'Identity' because it is null.  
   at System.Management.Automation.ParameterBinderBase.ValidateNullOrEmptyArgument(CommandParameterInternal parameter, CompiledCommandParameter parameterMetadata, Type argumentType, Object parameterValue, Boolean recurseIntoCollections)  
   at System.Management.Automation.ParameterBinderBase.BindParameter(CommandParameterInternal parameter, CompiledCommandParameter parameterMetadata, ParameterBindingFlags flags)  
   at System.Management.Automation.CmdletParameterBinderController.BindParameter(CommandParameterInternal argument, MergedCompiledCommandParameter parameter, ParameterBindingFlags flags)  
   at System.Management.Automation.CmdletParameterBinderController.BindParameter(UInt32 parameterSets, CommandParameterInternal argument, MergedCompiledCommandParameter parameter, ParameterBindingFlags flags)  
   at System.Management.Automation.CmdletParameterBinderController.BindParameters(UInt32 parameterSets, Collection`1 arguments)  
   at System.Management.Automation.CmdletParameterBinderController.BindCommandLineParametersNoValidation(Collection`1 arguments)  
   at System.Management.Automation.CmdletParameterBinderController.BindCommandLineParameters(Collection`1 arguments)  
   at System.Management.Automation.CommandProcessor.BindCommandLineParameters()  
   at System.Management.Automation.CommandProcessor.Prepare(IDictionary psDefaultParameterValues)  
   at System.Management.Automation.CommandProcessorBase.DoPrepare(IDictionary psDefaultParameterValues)  
   at System.Management.Automation.Internal.PipelineProcessor.Start(Boolean incomingStream)  
   at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)  
--- End of stack trace from previous location where exception was thrown ---  
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  
   at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)  
   at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)  
   at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)  
   at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)".
```

## Answer (community) — community member

*upvotes: 1 · updated: 2022-12-22*

Surmised answer accepted :) This way atleast someone running into the same issue has some means to possibly proceed with their problem :)     

Thanks to all who supplied insight and support :) It's appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-07*

No, there is no pre-existing 2019 Exchange server.     

We have a 2013 Exchange server, running on Windows 2012R2 in a hybrid config with Exchange Online. That's it.     

Our goal is to create a new Exchange 2019 in the same organization and then take our time in migrating everything off of the 2013 machine to the 2019 machine. (so mailboxes, connectors, the Hybrid connection, certificates, and whatever I'm not mentioning). In the end the 2013 should be decomissioned.     

However with this error it seems the 2019 setup isn't running to completion, and thus I'm not trusting that server (in whatever capacity the install has completed - seeing I can see it in the ECP o the 2013 machine) to handle anything yet.     

And the mailbox isn't missing. It's there. It's shown as being migrated to ExchangeOnline for whatever reason.     

The -Arbitration switch seems to be one that Exchange 2013 doesn't know, so running that from the 2019 machine:    

```
[PS] C:\Windows\system32>Get-Mailbox -Arbitration | format-table -autosize  
  
Name                                                Alias                                               ServerName ProhibitSendQuota  
----                                                -----                                               ---------- -----------------  
SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c} SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c} EX2013     Unlimited  
SystemMailbox{1f05a927-6b8f-4441-91d1-167030fdc771} SystemMailbox{1f05a927-6b8f-4441-91d1-167030fdc771} EX2013     Unlimited  
SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9} SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9} EX2013     Unlimited  
FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042 FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042 EX2013     Unlimited  
Migration.8f3e7716-2011-43e4-96b1-aba62d229136      Migration.8f3e7716-2011-43e4-96b1-aba62d229136      EX2013     Unlimited
```

The offending mailbox that causes the error (SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}) isn't shown in this list. Which makes sense, as Exchange 2019 isn't fully installed yet, and thus that mailbox shouldn't really exist. But then why is the installer complaining that the mailbox has been migrated?     

If I connect to the Exchange Online environment in Azure, the -Arbitration switch isn't known at all.    

If I follow the commands in the error as depicted in the PowerShell windows on the Exchange 2019 machine:    

Get-Mailbox -Arbitration -Filter {Name -eq "SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}"}    

doesn't yield any results.     

Which ends up the the 'Enable-Mailbox' error thrown... The mailbox needs to be enabled locally, but doesn't seem to exist, while at the same time the installer of Exchange 2019 is telling me it does exist, and it's been migrated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-05*

Thanks for your response.     

In order to answer your questions:    

1. Please verify that all Exchange server 2013 has been upgraded to the latest CU(CU23).    

Going by https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019#exchange-server-2013    

Initiated command on the 2013 server:    

```
Get-ExchangeServer | Format-List Name,Edition,AdminDisplayVersion  
  
Name                : **EX2013**  
Edition             : Standard  
AdminDisplayVersion : Version 15.0 (Build 1497.2)  
  
Name                : **EX2019**  
Edition             : StandardEvaluation  
AdminDisplayVersion : Version 15.2 (Build 1118.7)
```

Build 1497.2 for Exchange 2013 refers to the November 2022 update for CU23 according to the link above. So that's definitly the last CU23 version.     

Build 1118.7 for Exchange 2019 is based off the CU12 ISO install, and comes back as the update for April 2022. So While that one hasn't been updated to the last standard (which is to be expected as we're only installing it right now), that also seems to be the last version available.     

2. Are the active Directory Servers hosted on Windows 2012 R2 Standard or Datacenter and higher with Windows Server 2012 R2 or higher Active Directory Forest functionality?    

I'd have expected the pre-requisites in updating the schema and AD settings to already flag this one if it wasn't the case, but to verify:    

The Exchange 2013 is installed on an Exchange 2012 R2 VM, while the Exchange 2019 is run on a Windows Server 2019 VM.     

The lowest available domain controller (which is slated to be removed from the AD once we get the time for it), is a 2012 R2 Standard machine    

When checking the ADUC on the domain controller, both the Domain and Forest functional level are shown as Windows Server 2012 R2.     

> 3. Whether you successfully prepareAD before installing Exchange2019?    

As to this (glad I asked my colleague to specifically copy this stuff to a note):    

```
D:\>Setup.exe /PrepareSchema /IAcceptExchangeServerLicenseTerms_DiagnosticDataON  
  
Microsoft Exchange Server 2019 Cumulative Update 12 Unattended Setup  
  
Copying Files...  
File copy complete. Setup will now collect additional information needed for installation.  
  
  
Performing Microsoft Exchange Server Prerequisite Check  
  
    Prerequisite Analysis                                                                                                                                                   COMPLETED  
  
Configuring Microsoft Exchange Server  
  
    Extending Active Directory schema                                                                                                                                       COMPLETED  
  
The Exchange Server setup operation completed successfully.
```

----    

```
D:\>Setup.exe /PrepareAD /OrganizationName:"**name**" /IAcceptExchangeServerLicenseTerms_DiagnosticDataON  
  
Microsoft Exchange Server 2019 Cumulative Update 12 Unattended Setup  
  
Copying Files...  
File copy complete. Setup will now collect additional information needed for installation.  
  
  
Performing Microsoft Exchange Server Prerequisite Check  
  
    Prerequisite Analysis                                                                                                                                                   100%  
  
Setup will prepare the organization for Exchange Server 2019 by using 'Setup /PrepareAD'. No Exchange Server 2016 roles have been detected in this topology. After this operation, you will  
not be able to install any Exchange Server 2016 roles.  
For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2019  
  
  
Configuring Microsoft Exchange Server  
  
    Organization Preparation                                                                                                                                                COMPLETED  
  
The Exchange Server setup operation completed successfully.
```

I did anonymize the names and organization (bolded in the above outputs), so those changes are expected in the posted output :) So yes, that also seems to have completed as expected.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-05*

Hi @Jurriaan van Doornik   ,    

As far as I know, the mailbox (SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}) is a system mailbox that was added in Exchange 2016 CU8 and later.    

When you install a new Exchange 2019 in your Exchange 2013 environment , this system mailbox will be created in Exchange 2019.    

Here are more details about arbitration mailboxes:    

Create user mailboxes in Exchange Server, create Exchange mailbox, Exchange Server create mailbox | Microsoft Learn    

Check Exchange arbitration mailboxes - ALI TAJRAN    

(Kindly note: Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.)    

In order to better narrow down the issue, I need to confirm the following points with you:    

- 	Please verify that all Exchange server 2013 has been upgraded to the latest CU(CU23).    

- 	Are the active Directory Servers hosted on Windows 2012 R2 Standard or Datacenter and higher with Windows Server 2012 R2 or higher Active Directory Forest functionality?    

- 	Whether you successfully prepareAD before installing Exchange2019？    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
