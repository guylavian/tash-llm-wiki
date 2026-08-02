---
title: "Create an audience for SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-create-an-audience-for-sharepoint-server
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/create-an-audience-for-sharepoint-server
family: administration
documentKind: "how-to"
abstract: "Learn how to use a Microsoft PowerShell script to create an audience."
---

# Create an audience for SharePoint Server - SharePoint Server

Note

Create an audience for SharePoint Server

# Create an audience for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn how to use a Microsoft PowerShell script to create an audience.

Create an audience by using a Microsoft PowerShell script

## Create an audience by using a Microsoft PowerShell script

- Verify that you meet the following minimum requirements:

See Add-SPShellAdmin.

You must read about_Execution_Policies.

- Copy the following variable declarations, and paste them into a text editor such as Notepad. Set input values specific to your organization. You'll use these values in step 3. Save the file, and name it Audiences.ps1.

```
## Settings you may want to change for Audience Name and Description ## 
$mySiteHostUrl = https://www.my.contoso.com
$audienceName = "<Input name of audience>"
$audienceDescription = "<Input description for audience>"
$audienceRules = @()
$audienceRules += New-Object Microsoft.Office.Server.Audience.AudienceRuleComponent("AccountName", "Contains", "jdoe")
#Create an OR group operator between the two audience rules.
$audienceRules += New-Object Microsoft.Office.Server.Audience.AudienceRuleComponent("", "OR", "")
$audienceRules += New-Object Microsoft.Office.Server.Audience.AudienceRuleComponent("AccountName", "Contains", "jlew")
```

- Copy the following code, and paste it into Audiences.ps1 beneath the variable declarations from step 2.

```
#Get the My Site Host's SPSite object
$site = Get-SPSite $mySiteHostUrl
$ctx = [Microsoft.Office.Server.ServerContext]::GetContext($site)
$audMan = New-Object Microsoft.Office.Server.Audience.AudienceManager($ctx)
#Create a new audience object for the given Audience Manager
$aud = $audMan.Audiences.Create($audienceName, $audienceDescription)
$aud.AudienceRules = New-Object System.Collections.ArrayList
$audienceRules | ForEach-Object { $aud.AudienceRules.Add($_) }
#Save the new Audience
$aud.Commit()
#Compile the new Audience
$upa = Get-SPServiceApplication | Where-Object {$_.DisplayName -eq "User Profile Service Application"}
$audJob = [Microsoft.Office.Server.Audience.AudienceJob]::RunAudienceJob(($upa.Id.Guid.ToString(), "1", "1", $aud.AudienceName))
```

Note

You can use a different file name, but you must save the file as an ANSI-encoded text file with the extension .ps1.

Click SharePoint Management Shell.

Change to the directory to which you saved the file.

At the PowerShell command prompt, type the following command:

```
./Audiences.ps1 
```

For additional information about PowerShell scripts and .ps1 files see Running Windows PowerShell Scripts.

For more information about how to create audiences, see AudienceRuleComponent class.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
