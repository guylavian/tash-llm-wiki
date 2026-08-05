---
title: "Unable to connect to Exchange Online PowerShell Module"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1287748/unable-to-connect-to-exchange-online-powershell-mo
question_id: 1287748
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Unable to connect to Exchange Online PowerShell Module

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1287748/unable-to-connect-to-exchange-online-powershell-mo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Community!

I'm trying to connect to Security & Compliance PowerShell using the Exchange Online PowerShell module and tried to follow the following guide, but I'm receiving an error when I reach the Check Connection part.

Any help would be greatly appreciated!  

Before we start, please ensure you have PowerShell installed and access to your Exchange Online credentials. You also need to install the Exchange Online PowerShell Module which you can download from Microsoft.

Here's the step-by-step guide:

Open PowerShell: Look for PowerShell in the start menu and open it. You might need to run it as administrator depending on your system's settings.

Load the Exchange Online PowerShell Module: If you've installed the Exchange Online PowerShell Module, we need to load it into your session. This gives PowerShell the ability to understand and use commands related to Exchange Online. To do this, type the following command into PowerShell:

```
Import-Module ExchangeOnlineManagement
```

Then press Enter.

Connect to the Security & Compliance PowerShell: Now we're going to connect to the Security & Compliance PowerShell. This is where you'll need your Exchange Online credentials. The command to use depends on the type of your organization. Here are examples for different types of organizations:

If your organization is a regular Microsoft 365 organization, type the following command, replacing `******@contoso.onmicrosoft.com` with your own user principal name (that's usually your email address):

```
Connect-IPPSSession -UserPrincipalName ******@contoso.onmicrosoft.com
```

If your organization is a Microsoft GCC High organization, use this command (again, replace the user principal name with your own):

```
Connect-IPPSSession -UserPrincipalName ******@govt.us -ConnectionUri https://ps.compliance.protection.office365.us/powershell-liveid/ -AzureADAuthorizationEndpointUri https://login.microsoftonline.us/common
```

After typing the relevant command, press Enter.

Authenticate: You will be prompted to enter your password in the pop-up window that appears. Type your password and then click Sign in.

If you're using multi-factor authentication (MFA), you'll also be asked for a verification code. You should receive this code by text message or through the Microsoft Authenticator app on your device, depending on how your account is set up. Enter the code in the verification window and then click Verify.

-  Check the connection: To make sure you've connected successfully, you can run a command. For example, you can type:

```
Get-RetentionCompliancePolicy
```

Then press Enter. If the command runs without any errors, you've connected successfully!  

But, alas, I'm unable to run the aforementioned command which gives out this error:

```
PS C:\Windows\system32> Get-RetentionCompliancePolicy
Get-RetentionCompliancePolicy : The term 'Get-RetentionCompliancePolicy' is not recognized as the name of a cmdlet,
function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the
path is correct and try again.
At line:1 char:1
+ Get-RetentionCompliancePolicy
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (Get-RetentionCompliancePolicy:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

For which I received and tried out all of these suggestions:  

Your PowerShell version (5.1) is compatible with the Exchange Online PowerShell module and should be able to run the commands. Therefore, your issue might not be the PowerShell version.

Here are the next steps you can take:

Check if the Exchange Online PowerShell module is correctly installed: Run `Get-Module -ListAvailable -Name ExchangeOnlineManagement`. If the module is not listed, then you need to install it using `Install-Module -Name ExchangeOnlineManagement`.

If the module is installed, try importing it again: Run `Import-Module ExchangeOnlineManagement`. This will load the module into your PowerShell session.

Confirm that you are connected to Exchange Online: Try running a different command like `Get-Mailbox`. If you don't get any results or if you get an error, you might have been disconnected. In that case, run the `Connect-IPPSSession -UserPrincipalName <YourUserName>` command again, replacing `<YourUserName>` with your user name.

Verify permissions: Make sure that the account you're using to run these commands has the appropriate permissions in your Exchange Online organization. You might need to consult with your organization's IT department or administrator to confirm this.

Try running `Get-Command *RetentionCompliancePolicy*`. If this command returns no output, it means that the `Get-RetentionCompliancePolicy` cmdlet is not available in your PowerShell session, and the problem might be with your installation or connection.

I've tried these steps, except for number 4, which I'm not sure how to (and I don't have admin access to this server) and I'm getting the same error, and so I decided to reach out to Microsoft Support for more assistance, and so I here I am!  

Is it the permissions?  

I'm getting the following when running the command stated on the first step:

```
Directory: C:\Program Files\WindowsPowerShell\Modules

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     3.1.0      ExchangeOnlineManagement            {Get-ConnectionInformation, Get-EXOCasMailbox, Get-EXOMailbox, Get-EXOMailboxFolderPermission...}
```

Thank you advance!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-05-19*

Yes, permissions most likely :)

https://office365itpros.com/2018/12/07/retention-policies-sharepoint-site/
