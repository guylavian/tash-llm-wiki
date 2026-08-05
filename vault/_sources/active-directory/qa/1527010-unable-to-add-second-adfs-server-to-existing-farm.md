---
title: "Unable to add second ADFS server to existing farm (MSSQL and gMSA)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1527010/unable-to-add-second-adfs-server-to-existing-farm
question_id: 1527010
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Unable to add second ADFS server to existing farm (MSSQL and gMSA)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1527010/unable-to-add-second-adfs-server-to-existing-farm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

My first Server 2019 ADFS server is working fine, but for HA purposes I wanted to add a second one. I already made sure that my GMSA, which is just named "ADFS-GMSA" works fine with my MSSQL server.

I was following the instructions here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/configure-a-federation-server#to-add-a-federation-server-to-an-existing-federation-server-farm-via-windows-powershell

First of all I'm immediately noticing some discrepencies - is Domain Admin required for this or not? If you look at the GUI instructions just above the powershell instructions here, you can see in step 3, "On the Connect to AD DS page, specify an account by using domain administrator permissions for the AD domain to which this computer is joined, and then click Next."

But yet in the Powershell instructions, domain admin is not mentioned at all. Why is that?

The PKI certificate is in Local Machine "my" store on both servers.

So if I use the instructions in the Powershell instructions above, here is the command string I try:

`Add-AdfsFarmNode -GroupServiceAccountIdentifier "Contoso\ADFS-GMSA`$" -SQLConnectionString "Data Source=sql1.contoso.com;Initial Catalog=ADFSConfigurationV4;Integrated Security=True;Min Pool Size=20"`

`Add-AdfsFarmNode : Access is denied.`
`At line:1 char:1`
`+ Add-AdfsFarmNode -GroupServiceAccountIdentifier "CONTOSO\ADFS-GMSA`$" - ...`
`+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
`    + CategoryInfo          : NotSpecified: (:) [Add-AdfsFarmNode], UnauthorizedAccessException`
`    + FullyQualifiedErrorId : DeploymentTask,Microsoft.IdentityServer.Deployment.Commands.JoinFarmCommand`
`Message                                                                           Context        Status`
`-------                                                                           -------        ------`
`Unable to retrieve group Managed Service Account information. Access is denied... DeploymentTask  Error`
So, we have an error of access denied, and I'm unable to retrieve the gMSA information. I have already confirmed on this server that it is in the right groups to access the gMSA information:

`PS C:\Windows\system32> Test-ADServiceAccount -Identity adfs-gmsa`

`True`
But let's see what happens if I try to use domain admin (even though the instructions don't say to do so!) to add the account. This time, I use the GUI's "view command" function to see what the GUI is trying to do:

`#`

`# Windows PowerShell script for AD FS Deployment`
`#`
`Import-Module ADFS`
`# Get the credential used for performaing installation/configuration of ADFS`
`$installationCredential = Get-Credential -Message "Enter the credential for the account used to perform the configuration."`
`Add-AdfsFarmNode ``
`-CertificateThumbprint:"2389091C27391EBCAD14D9430B7D14FCB8C28A2E" ``
`-Credential:$installationCredential ``
`-GroupServiceAccountIdentifier:"CONTOSO\ADFS-GMSA`$" ``
`-SQLConnectionString:"Data Source=sql1.contoso.com;Initial Catalog=ADFSConfigurationV4;Integrated Security=True;Min Pool Size=20"`
In this case $installationcredential is the domain admin account, DAaccount

The error in this case is different:

`Add-AdfsFarmNode : An error occurred during an attempt to connect to the AD FS configuration database. Error: Login`

`failed for user 'CONTOSO\DAaccount'.. Confirm that the database hostname and instance name are correct and that the`
`specified service account has logon access to the database.`
`At line:1 char:1`
`+ Add-AdfsFarmNode ``
`+ ~~~~~~~~~~~~~~~~~~`
`    + CategoryInfo          : NotSpecified: (:) [Add-AdfsFarmNode], SqlConfigProviderInstallException`
`    + FullyQualifiedErrorId : DeploymentTask,Microsoft.IdentityServer.Deployment.Commands.JoinFarmCommand`
`Message`
`-------`
`Unable to determine the current Farm Behavior Level. An error occurred during an attempt to connect to the AD FS con...`
Any idea what I'm doing wrong here? What is the deal with using domain admin to join a farm, versus not using domain admin to join a farm? Are the instructions on this page wrong and domain admin requirement should be mentioned in both GUI and powershell sections?

Lastly, my powershell skills are not so great that I know how to capture the full result of the "Message" line at the bottom of each error message, the ones that end in "..." in both cases. It is not captured in the automatic $error powershell variable.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-03*

```
My problem was that the Deny Logon from Access Network restriction was applied to the Domain Admins group on the SQL server with GPO. I temporarily disabled this policy and the problem was fixed.
```
