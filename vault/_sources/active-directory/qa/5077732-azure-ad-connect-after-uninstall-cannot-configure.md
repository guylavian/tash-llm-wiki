---
title: "Azure AD Connect - after uninstall cannot configure and install again"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5077732/azure-ad-connect-after-uninstall-cannot-configure
question_id: 5077732
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 11
qa_tags: []
---
# Azure AD Connect - after uninstall cannot configure and install again

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5077732/azure-ad-connect-after-uninstall-cannot-configure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Halo,

I had "successfully" running AD Connect (password hash sync) with my on-premise AD (1500 accounts). Last week my passwords stopped to sync. I used recommended solution (from forum) to uninstall AD Connect and make full install again (all directories, databases,
 sync user, etc. was deleted too).

But I cannot configure and install AD Connect again. After adding forest and before selecting synced OU I am getting error "ArgumentOutOfRangeException". I have founded some recommendations, but I am still in troubles...

Thank you for hints and recommendation. Screenshot and log are below.

[10:50:05.604] [ 25] [INFO ] Page transition from "Connect Directories" [ConfigSyncDirectoriesPageViewModel] to "Azure AD sign-in" [UserSignInConfigPageViewModel]  

[10:50:05.604] [ 25] [ERROR] RootWizardPageViewModel: An unhandled exception occurred during a page load.  

Exception Data (Raw): System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.  

Parameter name: index  

   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)  

   at Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.UserSignInConfigPageViewModel.OnLoad(NavigateDirection direction)  

   at Microsoft.Online.Deployment.Framework.UI.WizardPages.RootWizardPageViewModel.ActivatePage(IWizardPage page, NavigateDirection direction)  

[10:50:05.651] [ 25] [ERROR] A terminating unhandled exception occurred.  

Exception Data (Raw): System.AggregateException: One or more errors occurred. ---> System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.  

Parameter name: index  

   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)  

   at Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.UserSignInConfigPageViewModel.OnLoad(NavigateDirection direction)  

   at Microsoft.Online.Deployment.Framework.UI.WizardPages.RootWizardPageViewModel.ActivatePage(IWizardPage page, NavigateDirection direction)  

   at Microsoft.Online.Deployment.Framework.UI.WizardPages.RootWizardPageViewModel.MoveNext()  

   at Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.ConfigSyncDirectoriesPageViewModel.WaitForTaskCompletion(Task task)  

   at System.Threading.Tasks.Task.Execute()  

   --- End of inner exception stack trace ---  

---> (Inner Exception #0) System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.  

Parameter name: index  

   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)  

   at Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.UserSignInConfigPageViewModel.OnLoad(NavigateDirection direction)  

   at Microsoft.Online.Deployment.Framework.UI.WizardPages.RootWizardPageViewModel.ActivatePage(IWizardPage page, NavigateDirection direction)  

   at Microsoft.Online.Deployment.Framework.UI.WizardPages.RootWizardPageViewModel.MoveNext()  

   at Microsoft.Online.Deployment.OneADWizard.UI.WizardPages.ConfigSyncDirectoriesPageViewModel.WaitForTaskCompletion(Task task)  

   at System.Threading.Tasks.Task.Execute()<---  

[10:50:05.697] [  1] [INFO ] Page transition from "Azure AD sign-in" [UserSignInConfigPageViewModel] to "Error" [ErrorPageViewModel]  

[10:50:05.713] [  1] [INFO ] UserSignInConfigPageViewModel : UPN attribute:   

[11:11:52.847] [  1] [INFO ] Opened log file at path C:\ProgramData\AADConnect\trace-20200414-104617.log

## Answer (community) — community member

*upvotes: 0 · updated: 2020-04-14*

Thank you so much for your answer, I have put question on the right forum:

https://docs.microsoft.com/answers/questions/22648/azure-ad-connect-after-uninstall-cannot-configure.html

But when I disable Directory Sync, error still exist...

directory sync was disabled, checked with:

`(Get-MSOLCompanyInformation).DirectorySynchronizationEnabled`

Next I uninstalled Ad Connect and then install again but I still cannot configure AD Connect with the same error.....

But thank you so much.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-04-14*

Hello PavelObar,

Based on the error information you provided, it is more likely that the Azure AD connect tool has problems with connection from Azure AD, it cannot retreve data from the Azure AD.  First please temporarily disable the AAD connect sync from your Azure AD
 via powershell command ***Set-MsolDirSyncEnabled –EnableDirSync $false,***after that please uninstall the AAD connect tool and then re-install it.  In this case please try to run the AAD connect tool again with the correct AAD gloabl
 admin sign in credentail to see if it make any difference, thanks.

On another hand, as we are focusing on Office 365 Exchange Online Support, we are not experts for Azure AD related problems and we have limited resource regarding to Azure AD.  If the issue persists, since Microsoft has a dedicated Azure AD support forum,
 it is recommended that please post a new thread to Azure AD forum and provide your generated information
 there. The dedicated support engineers there are focusing on Azure AD related problems, and they would give you more professional assistance regarding your problem, thanks.   By the way, if you need any other help from Our Office 365 for Business Exchange
 Online side, please feel free to share with me, and I am willing to help you. thanks.

Your understanding and patience will be highly appreciated.

Best Regards,

Oliver
