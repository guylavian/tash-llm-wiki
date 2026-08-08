---
title: "Unable to Assign MSI with MST to GPO Computer Configuration Using PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2153998/unable-to-assign-msi-with-mst-to-gpo-computer-conf
question_id: 2153998
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["community-center-not-monitored", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to Assign MSI with MST to GPO Computer Configuration Using PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2153998/unable-to-assign-msi-with-mst-to-gpo-computer-conf (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

-  Is there a PowerShell method to properly assign an MST along with an MSI to GPO Computer Configuration?

-  Does `SoftwareInstallation.CreatePackage()` support MST assignments via PowerShell?

-  Is there an alternative way (like modifying registry or using COM objects) to force MST association?

Any guidance or working PowerShell scripts would be highly appreciated! 🚀

 This question is related to the following Learning Module

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-06*

Hi dipeeka pise, 

Thank you for reaching out to Microsoft Q & A forum. 

Yes, you can assign an MST (Transform) file along with an MSI in Group Policy Software Installation, but the SoftwareInstallation.CreatePackage() method in PowerShell does not directly support MST assignments. However, you can modify the package properties after creation to include the MST file  

PowerShell Method: 

You can use the IGroupPolicyObject COM interface to configure the MST file alongside the MSI. Below is a step-by-step approach: 

1.Create the GPO and Assign the MSI 

2.Modify the GPO to Include the MST File 

Here’s a PowerShell script to achieve this: 

```
# Load the Group Policy Management COM Object
$gpm = New-Object -ComObject 'GPMgmt.GPM'
# Open the Group Policy Object (GPO)
$gpo = $gpm.GetGPO("{GPO-GUID-HERE}")  # Replace with actual GPO GUID or retrieve by name
# Get the Software Installation Policy
$si = $gpo.GetSoftwareInstallation("Computer")  # Target Computer Configuration
# Define MSI and MST Paths
$msiPath = "\\server\share\software.msi"
$mstPath = "\\server\share\transform.mst"
# Assign the MSI Package
$package = $si.CreatePackage($msiPath, 1)  # 1 = Assigned Installation
# Modify the Package Properties to Include the MST File
$package.Modify(2, "TRANSFORMS=$mstPath")  # 2 = Modify existing package
# Save and Apply Changes
$gpo.Save()
```

Alternative Methods: 

If PowerShell does not fully support this, consider these options: 

1.Using Group Policy Management Console (GPMC) Manually 

Open Group Policy Management Editor 

Navigate to Computer Configuration > Software Settings > Software Installation 

Create a new software installation package and assign the MSI 

Right-click the package, go to Properties > Modifications, and add the MST file 

2.Using a Startup Script 

If the MST file needs to be applied post-installation, use a batch or PowerShell script in Computer Configuration > Windows Settings > Scripts (Startup/Shutdown) to apply the MST file after MSI installation. 

Please feel free to contact us if you have any additional questions.     

If you have found the answer provided to be helpful, please click on the "Accept answer/Upvote" button so that it is useful for other members in the Microsoft Q&A community.
