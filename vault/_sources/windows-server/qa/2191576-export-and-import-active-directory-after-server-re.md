---
title: "Export and Import Active Directory After Server Restore"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191576/export-and-import-active-directory-after-server-re
question_id: 2191576
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Export and Import Active Directory After Server Restore

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191576/export-and-import-active-directory-after-server-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a server, running Microsoft Server 2022 21H2, that has experienced operating system file corruption after a recent Windows update (or hardware failure, or solar flares during the solar eclipse - who knows?). The corruption also destroyed accesses to any backups that were currently run every day. After Dell engineers tried to fix the problem using SFC and DISM (something that I had already tried), they gave up and told me to reinstall the operating system. Of course, this would destroy the Domain Controller and Active Directory configurations. 

I do have a backup that I created when the server was first deployed, so I could restore to that instance and retain the Domain Controller configuration. However, the Active Directory has changed. 

I am looking for a method to export the current Active Directory configuration (users, OU, computers, etc.) and then import it back to the system after restoring to the virgin deployment state.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-23*

Well,

I finally got the XML file to create with all of the objects using:

PS> $ADOObjects =  Get-ADObject -Filter * -Properties * 

PS> $doc = $ADOObjects | ConvertTo-Xml 

PS> $doc.Save("C:\AD_Config.xml")

Now, to figure out if the import PS script will work. We'll see what happens. I think I can also run some PS scripts in the what if mode to see what will happen if I actually run the script for real.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-23*

However, if I run just: Get-ADObject -Filter * -Properties *, all of the object and their properties are printed to screen.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-23*

I tried the export script and got this error. Any thoughts?

Copy-Item : A parameter cannot be found that matches parameter name 'InputObject'. 

At line:1 char:49 

-  Copy codeExport-Clixml -Path "C:\AD_Config.xml" -InputObject (Get-ADO ... 

- 

```
~~~~~~~~~~~~
```

-  CategoryInfo          : InvalidArgument: (:) [Copy-Item], ParameterBindingException 

-  FullyQualifiedErrorId : NamedParameterNotFound,Microsoft.PowerShell.Commands.CopyItemCommand

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-23*

Thank you for the quick response. This is what I was looking for. 

Yes, the AD is still functioning properly. I will be traveling back to the server's location either this weekend or the next to restore from the deployed state backup. I will let you know in a couple of weeks if this was successful. 

JS

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-23*

Hi Jeff Swain1,

Thank you for posting in the Microsoft Community Forums.

Can I ask if AD is still logged in and working properly in your current work environment. If the AD environment is corrupted, then you may not be able to use backup restore. If you can still log in and use it, you need to export the current configuration for backup, then do a system reinstall of the server and import the configuration, that is possible to do. 

This operation requires a power shell script, but I'm not familiar with it, so it's for reference only, and you need to be careful with it.

-  Using PowerShell for Export:    Open PowerShell and execute the following command to export the Active Directory configuration to a file:

```
powershellCopy codeExport-Clixml -Path "C:\AD_Config.xml" -InputObject (Get-ADObject -Filter * -Properties *)
```

    This will export all objects and properties from Active Directory and save them to a file named `AD_Config.xml`.

-  Restore the Server to Original State:    Before restoring to the original deployment state, ensure that any unnecessary data has been backed up and removed. You may need to reinstall the Windows Server operating system or perform a system restore to revert the system to its original state.

-  Import Active Directory Configuration:    After the server has been restored to its original state, open PowerShell and execute the following command to import the previously exported Active Directory configuration:

```
powershellCopy code$AD_Config = Import-Clixml -Path "C:\AD_Config.xml"
 foreach ($object in $AD_Config) {
     New-ADObject -Name $object.Name -Type $object.Type -Path $object.Path -OtherAttributes $object.OtherAttributes
 }
```

    This will recreate all objects and attributes in Active Directory based on the exported configuration file.

Please note that this is a basic method, and specifics may vary depending on the environment, configuration, and requirements. Before performing this operation, ensure that you understand and test these steps and have taken appropriate backup and recovery measures in a production environment.

Best regards

Neuvi Jiang
