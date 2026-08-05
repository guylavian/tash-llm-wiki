---
title: "Active Directory Groups"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2276600/active-directory-groups
question_id: 2276600
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Groups

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2276600/active-directory-groups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The syntax below works fine for me for one user, but I have a list of AD groups in a text file with the following format:

```
group1
group2
group3
```

I want to import this text file (e.g., `C:\Temp\grouplist.txt`) and assign user1 access to all the listed groups. Could you please guide me with the correct syntax? It works fine for a single group, but I would like to know how to import the entire list from the text file and assign access accordingly.

```
# Define the $owner that will be able to manage the members of $group
 $owner = "user1";
 $group = "group1";
     
 # Try to get objects from AD            
 try {
     
   
     $ownerobject = get-adgroup $owner;
     $groupobject = get-adgroup $group;
     
 # If AD could not be read
 } catch {
     
     write-host "Could not get user/group information from Active Directory";
     break;
 }
     
 # Try to set "write members" rights on the group 
 try {
     $ldapstring = "LDAP://" + $groupobject.distinguishedname;
     $ldapgroup = [ADSI]$ldapstring;
     
     [System.DirectoryServices.DirectoryEntryConfiguration]$secoptions = $ldapgroup.get_Options();
     $secoptions.SecurityMasks = [System.DirectoryServices.SecurityMasks]'Dacl';
        
     # Get SID
     $identityref = $ownerobject.sid.value;
     $sid = new-object System.Security.Principal.SecurityIdentifier ($identityref);
     
     # Define rights to be applied
     $adrights = [System.DirectoryServices.ActiveDirectoryRights]::WriteProperty;
     $type = [System.Security.AccessControl.AccessControlType]::Allow;
     
     # Define permission attribute to modify (writeMembers)
     $objectguid = [Guid]"bf9679c0-0de6-11d0-a285-00aa003049e2";
     
     $adrule = new-object System.DirectoryServices.ActiveDirectoryAccessRule ($sid, $adrights, $type, $objectguid);
     
     # Apply new ACL
     $ldapgroup.get_ObjectSecurity().AddAccessRule($adrule); 
     $ldapgroup.CommitChanges();
     
     write-host ("ACLs updated for group: " + $group);
     
     
 # If permissions could not be set
 } catch {
     
     write-host ("Could not set new ACLs on group: " + $group);
     break;
 }
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-17*

I have modified the script to grant user1 and user2 access to the groups listed in the attached text file. Could someone please review and validate the script?

```
# Define the users that will be granted permission
$owners = "user1", "user2"

# Loop through each group in the list
foreach ($group in Get-Content C:\Temp\grouplist.txt) {
    if ($group.Trim() -eq "") {
        continue  # Skip blank lines
    }

    Write-Host "Processing group: $group"

    try {
        # Get the group object from AD
        $groupObject = Get-ADGroup -Identity $group -ErrorAction Stop
    } catch {
        Write-Host "Could not retrieve group object for '$group'. Skipping..."
        continue
    }

    try {
        # Bind to the group via ADSI
        $ldapString = "LDAP://" + $groupObject.DistinguishedName
        $ldapGroup = [ADSI]$ldapString

        $secOptions = $ldapGroup.get_Options()
        $secOptions.SecurityMasks = [System.DirectoryServices.SecurityMasks]'Dacl'

        # Loop through each owner and apply ACL
        foreach ($owner in $owners) {
            try {
                $ownerObject = Get-ADUser -Identity $owner -ErrorAction Stop
            } catch {
                Write-Host "Could not retrieve user object for '$owner'. Skipping..."
                continue
            }

            $sid = New-Object System.Security.Principal.SecurityIdentifier($ownerObject.SID.Value)
            $adRights = [System.DirectoryServices.ActiveDirectoryRights]::WriteProperty
            $accessType = [System.Security.AccessControl.AccessControlType]::Allow
            $writeMembersGuid = [Guid]"bf9679c0-0de6-11d0-a285-00aa003049e2"

            $adRule = New-Object System.DirectoryServices.ActiveDirectoryAccessRule($sid, $adRights, $accessType, $writeMembersGuid)

            $acl = $ldapGroup.ObjectSecurity
            $acl.AddAccessRule($adRule)
            $ldapGroup.ObjectSecurity = $acl

            Write-Host "Granted '$owner' WriteMembers rights on group '$group'"
        }

        # Commit all changes
        $ldapGroup.CommitChanges()
    } catch {
        Write-Host "Failed to apply ACLs on group '$group'. Error: $_"
        continue
    }
}
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-17*

A foreach loop should do the trick.

```
# Define the $owner that will be able to manage the members of $group
$owner = "user1";
foreach ($group in (Get-Content C:\Temp\grouplist.txt)) {
	if ($group.trim() -eq "") {
		continue                      # skip over blank lines
	}
	
	write-host "Granting $owner access to group $group"
 
	# The rest of your script goes here.

}
```
