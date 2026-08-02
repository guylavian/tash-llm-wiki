---
title: "Create Drives GPO via Powershellscript"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/936325/create-drives-gpo-via-powershellscript
question_id: 936325
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
---
# Create Drives GPO via Powershellscript

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/936325/create-drives-gpo-via-powershellscript (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone I'm triing to create a GPO via Powershell as it is mentioned here: https://social.technet.microsoft.com/forums/en-US/0bfdd917-5267-45b0-bb99-bf1485bfe88c/create-gpo-map-drive-over-windows-powershell-script

i was not able to do some of the steps in the article so i worked via a GPO Template copying it and adjusting the xml file but it dowesnt work properly. Despite it is created I still have to open the GPO and click ok so that it works.  

I would like to make it step by step like in the article above.

$Klassenname = Read-Host -Prompt "Name of the Class?"  

$Bereich = Read-Host -Prompt "Area?"  

$Fileserver = "\xxxx\xxxxxx"

$Servername = 'XXXX'

OU

New-ADOrganizationalUnit -Name $Klassenname -Path "OU=$Bereich ,OU=Benutzer,DC=Ausbilden, DC=local" -Verbose  

Start-Sleep -Seconds 2

Group

New-ADGroup "GR-$Klassenname" -Path "OU=$Bereich ,OU=Benutzer,DC=xxxxx, DC=local" -GroupCategory Security -GroupScope Global -PassThru –Verbose

Start-Sleep -Seconds 2

Gruppe Membership

Add-ADGroupMember -Identity $Bereich -Members "GR-$Klassenname"

Start-Sleep -Seconds 2

GPO

Copy-GPO -SourceName "Template LW" -TargetName "$Klassenname" | New-GPLink -Target "OU=$Klassenname, OU=$Bereich, OU=Benutzer, DC=xxxxx, DC=local" -Verbose

Start-Sleep -Seconds 5

$Gpo=Get-Gpo $Klassenname -Verbose  

$Gpo = $Gpo.Id  

$Gpo

Start-Sleep -Seconds 10

$data = @"

<Drives clsid="{8FDDCC1A-0C3C-43cd-A6B4-71A6DF20DA8C}">

<Drive clsid="{935D1B74-9CB8-4e3c-9914-7DD559B7A417}" uid="{D4EBB8D8-AD3F-47B3-A76C-C172569D3C53}" changed="2020-09-07 07:25:42" image="2" status="K:" name="K:">

<Properties letter="K" useLetter="1" persistent="0" label="" path="\FSA01\$Klassenname" userName="" allDrives="NOCHANGE" thisDrive="NOCHANGE" action="U"/>

</Drive>

</Drives>

"@

$data | out-file "\dca02\sysvol\Ausbilden.local\Policies{$GPO}\User\Preferences\Drives\Drives.xml" -Verbose

Start-Sleep -Seconds 4

I know according to the article it should be done not via template but create the gpo step by step i tried this with the following steps in a seperate script  

$Klassenname = Read-Host -Prompt "Wie heißt die Klasse?"  

$Bereich = Read-Host -Prompt "Für welchen Bereich soll sie angelegt werden?"

Create the GPO

New-GPO -Name $Klassenname -Comment "This is not a test" | New-GPLink -Target "OU=$Klassenname, OU=$Bereich, OU=Benutzer, DC=xxxxx, DC=local"

Usersetting deaktivieren

$Gpo=Get-Gpo $Klassenname  

$Gpo.GpoStatus = ‘ComputerSettingsDisabled’  

$Gpo = $Gpo.Id  

$Gpo

Set-ADObject -Identity "CN={$Gpo}, CN=Policies, CN=System, DC=Ausbilden, DC=local"  

-Add @{gPCUserExtensionnames='[{00000000-0000-0000-0000-000000000000}{2EA1A81B-48E5-45E9-8BB7-A6E3AC170006}][{5794DAFD-BE60-433F-88A2-1A31939AC01F}{2EA1A81B-48E5-45E9-8BB7-A6E3AC170006}]'}

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-27*

Hello :),    

the thing is that i need to make that GPO every week several times for new classes with slightly different name. So i automated it. Thats why i need to do it with Powershell.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-26*

Hello    

Thank you for your question and reaching out.     

In my Opinion you can Simply use GPO to Map Drives for users instead of using PowerShell.    

Right-click the new Group Policy object and go to User Configuration -> Preferences -> Windows Settings -> Drive Maps.    

Right-click Drive Maps, select New and then click the Mapped Drive    

--------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
