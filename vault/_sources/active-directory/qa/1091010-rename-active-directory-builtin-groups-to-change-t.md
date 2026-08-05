---
title: "Rename Active Directory BuiltIn Groups to change the language"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1091010/rename-active-directory-builtin-groups-to-change-t
question_id: 1091010
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Rename Active Directory BuiltIn Groups to change the language

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1091010/rename-active-directory-builtin-groups-to-change-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

At the begenning, our first domain controller was installed in French, so all the BuiltIn group are in french.    

Now every domain controller are in Windows Server 2016 in English and I would like to rename all the BuiltIn group with the English name.    

    

I've found this thread that explained how to do that but I was a while ago with Windows server 2003.    

https://learn.microsoft.com/en-us/archive/blogs/janelewis/how-to-modify-a-system-owned-object    

Can someone tell me if it still works now, if someone did it already and if we could have some problem doing that?     

Is there a different way to do that ? (powershell ?)    

Thank you for your help !

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-16*

Hello there,    

Yes, the support article still works and many users have found it to be helpful. Additionally, this thread might shed some light on the process.    

changing language of a child domain https://social.technet.microsoft.com/Forums/en-US/7b08375a-5911-4943-8b5a-0c151c5607e2/changing-language-of-a-child-domain?forum=winserverDS#017e4d52-c736-4f6e-b96f-fef92cb5600e    

---------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-16*

Ok so I finally did it.    

It worked correctly.    

So just to explain how I did it if it helps someone :    

-   Launch LDP.exe and bind to the DS server you want to modify. Make sure you are schema admin, and admin over the partition you are modifying    

-   After connecting and binding navigate to the browse menu and select the "Modify" option.    

-   Leave the DN blank, type 'schemaUpgradeInProgress' into the Attribute field and in the values field type 1.    

    

-  Click the Add operation and then click the enter button. This will add this command to the entry list.    

-   Click the Run button. If you are successful you should see a successful modify message.    

-   Go to View -> Tree. Connect to the appropriate base DN.    

-   Find the objects (here do that for all the Builtin groups), right click and select modify    

-   In the attribute field, type "systemflags" in the Values field, leave it blank; in the operation radio options, select delete    

-   Then click Enter, then click Run to remove the system flags values    

-   Perform the modification :    

Thanks to : https://stackoverflow.com/questions/71757024/renaming-localization-of-built-in-active-directory-groups-using-sid    

Run this script (with the csv attached, you need to modify the root SID for the users that are not in the builtin OU):     

```
$orggroups=$orggroups = Import-Csv -Delimiter ';' -Path ".\AD built in groups ENGLISH.csv"  
#Loop Through Groups  
foreach ($group in $orggroups) {  
    $adgroup = $null  
    try {  
        #Check if we have a group with same SID  
        $adgroup = Get-ADGroup $group.SID -Properties DistinguishedName,Name,description,systemflags  
        $adGroupName=$adgroup.Name  
        $adGroupDesc=$adgroup.description  
        $adsysflags=$adgroup.systemflags  
        #If Name is Different, rename and update description  
  
        if ($adgroup.name -ne $group.CN) {  
            "Desc|$adGroupDesc|" + $group.description  
            Set-ADGroup $adgroup -Description $group.description   
            "Name|$adGroupName|" + $group.CN  
            Set-ADGroup $adgroup -SamAccountName $group.CN  
            Rename-ADObject $adgroup -NewName $group.CN[261011-ad-built-in-groups-english.txt][2]  
        }  
        else {  
            "Group " + $group.CN +" is named correctly"  
        }  
    }  
    catch {  
        #Didn't find group with same SID  
        "Group " + $group.CN + " does not exist"  
    }  
}
```

Then go back to the ldp.exe     

-  For each groups, set the systemflags value back to the original value (in my case "-1946157056"), to make it owned by the system again    

-  Once finished, run LDP again with the above steps (step 3), changing the schemaUpgradeInProgress value to 0 (to prevent unwantedschema/system changes)

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-16*

Hi @Sylv___  ,    

did you already came across this:    

Active Directory Language Change    

https://learn.microsoft.com/en-us/answers/questions/657959/active-directory-language-change.html    

piaudonn answered • Dec 09 2021 at 10:41 PM | piaudonn edited • Dec 09 2021 at 10:43 PM    

@Anonymous   is right for the OS language.    

For groups and users which already exist, they will not be renamed after adding a new domain controller in English.    

You can rename the objects though. They have well-known SID so renaming them will not break them. Renaming a security principal (such as a user or a group) doesn't change their security identifier (SID). When you add a user or a group into another group, or use them in a security descriptor (the security tab on an object) the system stores the SID not the display name.    

It is possible to have a custom application that is using the display name or the distinguished name of the user. And renaming a group might break these. But 1 that's bad practice on the app side and 2 that's unlikely that they use the built-in objects as a reference like these.    

Also, note that many customers are using localized names for built-in objects because the first DC was installed in French, German or Spanish. It doesn't need to be "fixed". Some rare applications are looking for name of groups as opposed as SIDs, and that's really the app that needs to be "fixed".    

Regards,    

Stoyan
