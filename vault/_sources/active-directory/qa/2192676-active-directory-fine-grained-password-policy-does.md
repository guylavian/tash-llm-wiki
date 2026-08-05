---
title: "Active directory - Fine Grained Password policy does not work for AD users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192676/active-directory-fine-grained-password-policy-does
question_id: 2192676
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active directory - Fine Grained Password policy does not work for AD users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192676/active-directory-fine-grained-password-policy-does (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello community, I am having problems with the default policy and password configuration container. No matter how much I try to apply fine password policy, it fails to change the "password change" date. Any idea what may be happening. I attach the trunks. 

AD Version is Server 2016..

```
PS C:\Users\Administrator> Get-ADUserResultantPasswordPolicy -Identity "matías" 

Applies to: {CN=VPN_POR_DIA,OU=VPN_POR_DIA,OU=MEGAMEDIA,DC=domain,DC=cl} 

Complexity enabled: true 

Distinguished Name: CN=FGPP_21Days,CN=Password Configuration Container,CN=System,DC=domain,DC=cl 

LockDuration: 00:02:00 

Lock observation window: 00:02:00 

Locking threshold: 4 

AgePasswordMax: 21.00:00:00 

Minimum password age: 1.00:00:00 

Minimum password length: 10 

Name: FGPP_21Days 

Object class: msDS-Password Settings 

Object GUID: 60bbdc40-897f-4fb4-b017-901d31f34578 

PasswordHistoryCount: 24 

Priority: 1 

Reversible encryption enabled: false 

PS C:\Users\Administrator> 

PS C:\Users\Administrator> net user matias /domain 

Username matías 

full name matías 

Comment 

User Comment 

Country or region code 000 (Default by device) 

Active Account Yes 

The account never expires 

Last password change 07-11-2024 17:09:22 

Password expires 08-22-2024 17:09:22 

Password change 07-12-2024 17:09:22 

Password required Yes 

The user can change the password Yes 

Authorized workstations All 

Login script 

User profile 

Main directory 

Last session started Never 

Authorized login times All 

Local group members 

Members of the global group *VPN_POR_DIA 

 *Domain users 

The command completed successfully. 

PS C:\Users\Administrator> 

PS C:\Users\Administrator> Get-ADFineGrainedPasswordPolicy -Filter * | Sort-Object -Property Precedence 

Applies to: {CN=VPN_POR_DIA,OU=VPN_POR_DIA,OU=MEGAMEDIA,DC=domain,DC=cl} 

Complexity enabled: true 

Distinguished Name: CN=FGPP_21Days,CN=Password Configuration Container,CN=System,DC=domain,DC=cl 

LockDuration: 00:02:00 

Lock observation window: 00:02:00 

Locking threshold: 4 

AgePasswordMax: 21.00:00:00 

Minimum password age: 1.00:00:00 

Minimum password length: 10 

Name: FGPP_21Days 

Object class: msDS-Password Settings 

Object GUID: 60bbdc40-897f-4fb4-b017-901d31f34578 

PasswordHistoryCount: 24 

Priority: 1 

Reversible encryption enabled: false 

PS C:\Users\Administrator> Get-ADDefaultDomainPasswordPolicy 

Complexity enabled: true 

Distinguished name: DC=domain,DC=cl 

Lockout duration: 00:10:00 

Lock observation window: 00:10:00 

Locking threshold: 0 

Maximum password age: 42.00:00:00 

Minimum password age: 1.00:00:00 

Minimum password length: 7 

object class: {DNSdomain} 

objectGuid: 82d822cf-9a56-43da-b460-8f63f62705e1 

PasswordHistoryCount: 24 

Reversible encryption enabled: false
```

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-12*

Hi Neuvi, 

Thank you very much for your prompt response. The problem we are having specifically is that the password is not expiring in less than 21 days. And we assume that it is still linked to the default policy. We did the following tests: 

___________________________________________________

Test 1: from the group policy administration, the default policy is within "domain.cl". {CN=VPN_POR_DIA,OU=VPN_POR_DIA,OU=MEGAMEDIA,DC=domain,DC=cl. We apply blocking inheritance in MEGAMEDIA and VPN_POR_DIA. After that we generate a GPO within VPN_POR_DIA, we apply gpupdate /force, and it does not take this policy for users either. 

Device Settings (Enabled) 

Directives 

Windows Settings 

Security settings 

Account Policies/Password Policy 

Configuration Policy 

Require password history 15 remembered passwords 

Passwords must meet complexity requirements Enabled 

Minimum password length 10 characters 

Maximum password validity 2 days 

Minimum password validity 1 day 

```
PS C:\Users\Administrator> net user matias /domain 

Username matias

Full name matias

Comment 

User Comment 

Country or region code 000 (Default by device) 

Active account Yes 

Account expires Never 

Last password change 07-11-2024 16:52:48 

Password expires 08-22-2024 16:52:48 *************

Password change 07-12-2024 16:52:48 

Password required Yes 

The user can change the password Yes 

Authorized workstations All 

Login script 

User profile 

Main directory 

Last session started 07-11-2024 12:01:28 

Authorized login times All 

Local group members 

Members of the global group *VPN_POR_DIA 

 *Domain users 

The command completed successfully. 

PS C:\Users\Administrator> Get-ADUserResultantPasswordPolicy matias 

PS C:\Users\Administrator>   

_____________________________________
```

  Test 2: Create a Fine Grained Password policy for a specific group "VPN_POR_DIA" because we saw in some forums that it is not possible in a domain to have more than 2 GPOs with different password characteristics.  Which is an option that helps us to have a group with different key policies. We create a policy called  "FGPP_21Days" in "Password Settings Container" applied to the group "VPN_POR_DIA" with the characteristics  of 21 days. The problem and doubt at the same time is that when we apply the  following command: Get-ADUserResultantPasswordPolicy -Identity "matías", it returns that the user does  have different password parameters, BUT we really do not see that the password expires and asks us to force  it to be changed When logging in, it is clear to us when we execute  the following command: net user matias /domain which tells us "Password expires 08-22-2024 17:09:22".  As indicated 42 more days, we assume that it takes the default policy of the domain,  with the following command: Get-ADDefaultDomainPasswordPolicy 

```
PS C:\Users\Administrator> Get-ADUserResultantPasswordPolicy -Identity "matías"

Applies to: {CN=VPN_POR_DIA,OU=VPN_POR_DIA,OU=MEGAMEDIA,DC=domain,DC=cl}

Complexity enabled: true

Distinguished Name: CN=FGPP_21Days,CN=Password Configuration Container,CN=System,DC=domain,DC=cl

LockDuration: 00:02:00

Lock observation window: 00:02:00

Locking threshold: 4

AgePasswordMax: 21.00:00:00 *******************

Minimum password age: 1.00:00:00

Minimum password length: 10

Name: FGPP_21Days

Object class: msDS-Password Settings

Object GUID: 60bbdc40-897f-4fb4-b017-901d31f34578

PasswordHistoryCount: 24

Priority: 1

Reversible encryption enabled: false

PS C:\Users\Administrator> net user matias /domain 
Username matías 
full name matías 
Comment 
User Comment  
Country or region code 000 (Default by device) 
Active Account Yes 
The account never expires 
Last password change 07-11-2024 17:09:22 
Password expires 08-22-2024 17:09:22 *****************
Password change 07-12-2024 17:09:22 
Password required Yes 
The user can change the password Yes 
Authorized workstations All 
Login script 
User profile 
Main directory 
Last session started Never 
Authorized login times All 
Local group members 
Members of the global group *VPN_POR_DIA 
 *Domain users 
The command completed successfully. 

PS C:\Users\Administrador> Get-ADDefaultDomainPasswordPolicy 
ComplexityEnabled           : True 
DistinguishedName           : DC=dominio,DC=cl 
LockoutDuration             : 00:10:00 
LockoutObservationWindow    : 00:10:00 
LockoutThreshold            : 0 
MaxPasswordAge              : 42.00:00:00 ***************
MinPasswordAge              : 1.00:00:00 
MinPasswordLength           : 7 
objectClass                 : {domainDNS} 
objectGuid                  : 82d822cf-9a56-43da-b460-8f63f62705e1 
PasswordHistoryCount        : 24 
ReversibleEncryptionEnabled : False 

_____________________________

We need to force the user to change the password for a new one after 21 days. Unfortunately with the FGPP we 
don't see it happening. Currently the OU=VPN_POR_DIA has "block inheritance"

Regards
```

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-12*

Hi Matias Ignacio Catril Opazo,

Thank you for posting in the Microsoft Community Forums.

First, make sure you have changed the password policy in the correct location. In Windows Server, if a computer is joined to a domain, the password policy is usually managed through a Group Policy (GPO), not through a local security policy. What you need to check and modify are the Group Policy Objects (GPOs) associated with a specific organisational unit (OU) or the domain as a whole.

Open the Group Policy Management console.

Navigate to the OU or domain that contains the target users or computers.

Locate and edit the Default Domain Policy or other custom policy associated with those users or computers.

In the Policy Editor, expand Computer Configuration > Policies > Windows Settings > Security Settings "> Account Policies > Password Policies.

Check and change settings such as "Maximum password lifetime" to make sure they meet your requirements.

After changing the password policy, you may need to force an update to the Group Policy to ensure that the changes take effect immediately. This can be done by running the gpupdate /force command as an administrator at a command prompt.

If there are multiple Group Policy Objects (GPOs) applied to the same user or computer and there are conflicting or overlapping password policy settings between them, you may need to check the priority and inheritance settings of these GPOs.

Use the Group Policy Management Console to view the linking order and enforcement mode of the GPOs.

Make sure that no higher priority GPOs are overriding your password policy settings.

If necessary, you can adjust the linking order of the GPOs or use the "Block Inheritance" feature to prevent unnecessary policy settings from being applied.

Users may not be able to change their passwords due to limitations in the password history settings (i.e., users cannot reuse a certain number of old passwords from the recent past). Make sure that the password history setting also meets your requirements.

Best regards

Neuvi Jiang
