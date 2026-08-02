---
title: "How to use this documentation — pages 161-200"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0161-0200
family: powershell
documentKind: "doc"
abstract: "HKLM Registry HKEY_LOCAL_MACHINE Variable Variable WSMan WSMan Third-party modules such as the ActiveDirectory PowerShell module and the SqlServer PowerShell module both add their own PowerShell provider and PSDrive. Import the ActiveDirectory and SqlServer PowerShell modules. P"
---

# How to use this documentation — pages 161-200

<!-- p.161 -->

 HKLM                                        Registry       HKEY_LOCAL_MACHINE
 Variable                                    Variable
 WSMan                                       WSMan

Third-party modules such as the ActiveDirectory PowerShell module and the SqlServer
PowerShell module both add their own PowerShell provider and PSDrive.

Import the ActiveDirectory and SqlServer PowerShell modules.

 PowerShell

 Import-Module -Name ActiveDirectory, SQLServer

Check to see if any additional PowerShell providers were added.

 PowerShell

 Get-PSProvider

Notice that in the following set of results, two new PowerShell providers now exist, one for
Active Directory and another one for SQL Server.

 Output

 Name                    Capabilities                       Drives
 ----                    ------------                       ------
 Registry                ShouldProcess, Transactions        {HKLM, HKCU}
 Alias                   ShouldProcess                      {Alias}
 Environment             ShouldProcess                      {Env}
 FileSystem              Filter, ShouldProcess, Credentials {C, A, D}
 Function                ShouldProcess                      {Function}
 Variable                ShouldProcess                      {Variable}
 ActiveDirectory         Include, Exclude, Filter, Shoul... {AD}
 SqlServer               Credentials                        {SQLSERVER}

A PSDrive for each of those modules was also added.

 PowerShell

 Get-PSDrive

 Output

 Name              Used (GB)      Free (GB) Provider        Root
 ----              ---------      --------- --------        ----
 A                                          FileSystem      A:\

<!-- p.162 -->

 AD                                          ActiveDire... //RootDSE/
 Alias                                       Alias
 C                     19.38          107.13 FileSystem    C:\
 Cert                                        Certificate   \
 D                                           FileSystem    D:\
 Env                                         Environment
 Function                                    Function
 HKCU                                        Registry      HKEY_CURRENT_USER
 HKLM                                        Registry      HKEY_LOCAL_MACHINE
 SQLSERVER                                   SqlServer     SQLSERVER:\
 Variable                                    Variable
 WSMan                                       WSMan

PSDrives can be accessed just like a traditional file system.

 PowerShell

 Get-ChildItem -Path Cert:\LocalMachine\CA

 Output

       PSParentPath: Microsoft.PowerShell.Security\Certificate::LocalMachine\CA

 Thumbprint                                       Subject
 ----------                                       -------
 FEE449EE0E3965A5246F000E87FDE2A065FD89D4         CN=Root Agency
 D559A586669B08F46A30A133F8A9ED3D038E2EA8         OU=www.verisign.com/CPS Incorp....
 109F1CAED645BB78B3EA2B94C0697C740733031C         CN=Microsoft Windows Hardware C...

Comparison Operators
PowerShell contains various comparison operators that are used to compare values or find
values that match certain patterns. The following table contains a list of comparison operators
in PowerShell.

All the operators listed in the table are case-insensitive. To make them case-sensitive, place a c
in front of the operator. For example, -ceq is the case-sensitive version of the equals ( -eq )
comparison operator.

                                                                                  ﾉ   Expand table

 Operator             Definition

 -eq                  Equal to

 -ne                  Not equal to

<!-- p.163 -->

 Operator            Definition

 -gt                 Greater than

 -ge                 Greater than or equal to

 -lt                 Less than

 -le                 Less than or equal to

 -like               Match using the * wildcard character

 -notlike            Doesn't match using the * wildcard character

 -match              Matches the specified regular expression

 -notmatch           Doesn't match the specified regular expression

 -contains           Determines if a collection contains a specified value

 -notcontains        Determines if a collection doesn't contain a specific value

 -in                 Determines if a specified value is in a collection

 -notin              Determines if a specified value isn't in a collection

 -replace            Replaces the specified value

Proper case "PowerShell" is equal to lower case "powershell" using the equals comparison
operator.

 PowerShell

 'PowerShell' -eq 'powershell'

 Output

 True

It's not equal using the case-sensitive version of the equals comparison operator.

 PowerShell

 'PowerShell' -ceq 'powershell'

 Output

<!-- p.164 -->

 False

The not equal comparison operator reverses the condition.

 PowerShell

 'PowerShell' -ne 'powershell'

 Output

 False

Greater than, greater than or equal to, less than, and less than or equal all work with string or
numeric values.

 PowerShell

 5 -gt 5

 Output

 False

Using greater than or equal to instead of greater than with the previous example returns the
Boolean true since five is equal to five.

 PowerShell

 5 -ge 5

 Output

 True

Based on the results from the previous two examples, you can probably guess how both less
than and less than or equal to work.

 PowerShell

 5 -lt 10

<!-- p.165 -->

 Output

 True

The -like and -match operators can be confusing, even for experienced PowerShell users. -
like is used with the wildcard characters * and ? to perform "like" matches.

 PowerShell

 'PowerShell' -like '*shell'

 Output

 True

The -match operator uses a regular expression to perform the matching.

 PowerShell

 'PowerShell' -match '^.*shell$'

 Output

 True

Use the range operator to store the numbers 1 through 10 in a variable.

 PowerShell

 $Numbers = 1..10

Determine if the $Numbers variable includes 15.

 PowerShell

 $Numbers -contains 15

 Output

 False

Determine if it includes the number 10.

<!-- p.166 -->

 PowerShell

 $Numbers -contains 10

 Output

 True

The -notcontains operator reverses the logic to see if the $Numbers variable doesn't contain a
value.

 PowerShell

 $Numbers -notcontains 15

The previous example returns the Boolean true because it's true that the $Numbers variable
doesn't contain 15.

 Output

 True

It does, however, contain the number 10, so it's false when tested.

 PowerShell

 $Numbers -notcontains 10

 Output

 False

The -in comparison operator was first introduced in PowerShell version 3.0. It's used to
determine if a value is in an array. The $Numbers variable is an array since it contains multiple
values.

 PowerShell

 15 -in $Numbers

 Output

<!-- p.167 -->

 False

In other words, -in performs the same test as the contains comparison operator except from
the opposite direction.

 PowerShell

 10 -in $Numbers

 Output

 True

Fifteen isn't in the $Numbers array, so false is returned in the following example.

 PowerShell

 15 -in $Numbers

 Output

 False

Just like the -contains operator, not reverses the logic for the -in operator.

 PowerShell

 10 -notin $Numbers

The previous example returns false because the $Numbers array does include 10 and the
condition tests to determine if it doesn't contain 10.

 Output

 False

Determine if fifteen isn't in the $Numbers array.

 PowerShell

 15 -notin $Numbers

<!-- p.168 -->

15 is "not in" the $Numbers array so it returns the Boolean true.

 Output

 True

The -replace operator does just what you would think. It's used to replace something.
Specifying one value replaces that value with nothing. In the following example, you replace
"Shell" with nothing.

 PowerShell

 'PowerShell' -replace 'Shell'

 Output

 Power

If you want to replace a value with a different one, specify the new one after the pattern you
want to replace. SQL Saturday in Baton Rouge is an event I try to speak at every year. In the
following example, the word "Saturday" is replaced with the abbreviation "Sat".

 PowerShell

 'SQL Saturday - Baton Rouge' -replace 'saturday','Sat'

 Output

 SQL Sat - Baton Rouge

There are also methods like Replace() that can be used to replace things similar to how the
replace operator works. However, the -replace operator is case-insensitive by default, and the
Replace() method is case-sensitive.

 PowerShell

 'SQL Saturday - Baton Rouge'.Replace('saturday','Sat')

Notice that the word "Saturday" isn't replaced. This is because it's specified in a different case
than the original.

<!-- p.169 -->

 Output

 SQL Saturday - Baton Rouge

When the word "Saturday" is specified in the same case as the original, the Replace() method
performs the replacement as expected.

 PowerShell

 'SQL Saturday - Baton Rouge'.Replace('Saturday','Sat')

 Output

 SQL Sat - Baton Rouge

Be careful when using methods to transform data because you can encounter unforeseen
problems, such as failing the Turkey Test. For an example, see my blog article, Using Pester to
Test PowerShell Code with Other Cultures     . I recommend using operators instead of methods
whenever possible to avoid these types of problems.

While the comparison operators can be used, as shown in the previous examples, I typically use
them with the Where-Object cmdlet to perform filtering.

Summary
You learned several topics in this chapter, including Formatting Right, Aliases, Providers, and
Comparison Operators.

Review
   1. Why is it necessary to perform formatting as far to the right as possible?
   2. How do you determine what the actual cmdlet is for the % alias?
   3. Why shouldn't you use aliases in scripts you save or code you share with others?
   4. Perform a directory listing on the drives that are associated with the Registry provider.
   5. What's one of the main benefits of using the replace operator instead of the replace
     method?

References
     Format-Table

<!-- p.170 -->

      Format-List
      Format-Wide
      about_Aliases
      about_Providers
      about_Comparison_Operators
      about_Arrays

Next steps
In Chapter 6, you'll learn about flow control, scripting, loops, and conditional logic.

 Last updated on 02/06/2026

<!-- p.171 -->

Chapter 6 - Flow control

Scripting
When you move from writing PowerShell one-liners to writing scripts, it sounds more
complicated than it is. A script is nothing more than the same or similar commands you run
interactively in the PowerShell console, except you save them as a .ps1 file. There are some
scripting constructs that you might use, such as a foreach loop instead of the ForEach-Object
cmdlet. The differences can be confusing for beginners when considering that foreach is both
a language keyword and an alias for the ForEach-Object cmdlet.

Looping
One of the best aspects of PowerShell is its scalability. Once you learn how to perform a task
for a single item, applying the same action to hundreds of items is almost as straightforward.
Loop through the items using one of the different types of loops in PowerShell.

ForEach-Object
ForEach-Object is a cmdlet for iterating through items in a pipeline, such as with PowerShell

one-liners. ForEach-Object streams the objects through the pipeline.

Although the Module parameter of Get-Command accepts multiple string values, it only accepts
them via pipeline input by property name. In the following scenario, if you want to pipe two
string values to Get-Command for use with the Module parameter, you need to use the ForEach-
Object cmdlet.

 PowerShell

 'ActiveDirectory', 'SQLServer' |
     ForEach-Object {Get-Command -Module $_} |
     Group-Object -Property ModuleName -NoElement |
     Sort-Object -Property Count -Descending

 Output

 Count Name
 ----- ----

<!-- p.172 -->

    147 ActiveDirectory
     82 SqlServer

In the previous example, $_ is the current object. Beginning with PowerShell version 3.0,
$PSItem can be used instead of $_ . Most experienced PowerShell users prefer using $_ since

it's backward compatible and less to type.

When using the foreach keyword, you must store the items in memory before iterating
through them, which could be difficult if you don't know how many items you're working with.

 PowerShell

 $ComputerName = 'DC01', 'WEB01'
 foreach ($Computer in $ComputerName) {
     Get-ADComputer -Identity $Computer
 }

 Output

 DistinguishedName : CN=DC01,OU=Domain Controllers,DC=mikefrobbins,DC=com
 DNSHostName       : dc01.mikefrobbins.com
 Enabled           : True
 Name              : DC01
 ObjectClass       : computer
 ObjectGUID        : c38da20c-a484-469d-ba4c-bab3fb71ae8e
 SamAccountName    : DC01$
 SID               : S-1-5-21-2989741381-570885089-3319121794-1001
 UserPrincipalName :

 DistinguishedName : CN=WEB01,CN=Computers,DC=mikefrobbins,DC=com
 DNSHostName       : web01.mikefrobbins.com
 Enabled           : True
 Name              : WEB01
 ObjectClass       : computer
 ObjectGUID        : 33aa530e-1e31-40d8-8c78-76a18b673c33
 SamAccountName    : WEB01$
 SID               : S-1-5-21-2989741381-570885089-3319121794-1107
 UserPrincipalName :

Many times a loop such as foreach or ForEach-Object is necessary. Otherwise you receive an
error message.

 PowerShell

 Get-ADComputer -Identity 'DC01', 'WEB01'

 Output

<!-- p.173 -->

 Get-ADComputer : Cannot convert 'System.Object[]' to the type
 'Microsoft.ActiveDirectory.Management.ADComputer' required by parameter
 'Identity'. Specified method is not supported.
 At line:1 char:26
 + Get-ADComputer -Identity 'DC01', 'WEB01'
 +                          ~~~~~~~~~~~~~~~
     + CategoryInfo          : InvalidArgument: (:) [Get-ADComputer], Parame
    terBindingException
     + FullyQualifiedErrorId : CannotConvertArgument,Microsoft.ActiveDirecto
    ry.Management.Commands.GetADComputer

Other times, you can get the same results while eliminating the loop. Consult the cmdlet help
to understand your options.

 PowerShell

 'DC01', 'WEB01' | Get-ADComputer

 Output

 DistinguishedName : CN=DC01,OU=Domain Controllers,DC=mikefrobbins,DC=com
 DNSHostName       : dc01.mikefrobbins.com
 Enabled           : True
 Name              : DC01
 ObjectClass       : computer
 ObjectGUID        : c38da20c-a484-469d-ba4c-bab3fb71ae8e
 SamAccountName    : DC01$
 SID               : S-1-5-21-2989741381-570885089-3319121794-1001
 UserPrincipalName :

 DistinguishedName : CN=WEB01,CN=Computers,DC=mikefrobbins,DC=com
 DNSHostName       : web01.mikefrobbins.com
 Enabled           : True
 Name              : WEB01
 ObjectClass       : computer
 ObjectGUID        : 33aa530e-1e31-40d8-8c78-76a18b673c33
 SamAccountName    : WEB01$
 SID               : S-1-5-21-2989741381-570885089-3319121794-1107
 UserPrincipalName :

As you can see in the previous examples, the Identity parameter for Get-ADComputer only
accepts a single value when provided via parameter input. However, by using the pipeline, you
can send multiple values to the command because the values are processed one at a time.

For

<!-- p.174 -->

A for loop iterates while a specified condition is true. I don't use the for loop often, but it has
uses.

 PowerShell

 for ($i = 1; $i -lt 5; $i++) {
     Write-Output "Sleeping for $i seconds"
     Start-Sleep -Seconds $i
 }

 Output

 Sleeping for 1 seconds
 Sleeping for 2 seconds
 Sleeping for 3 seconds
 Sleeping for 4 seconds

In the previous example, the loop iterates four times by starting with the number one and
continuing as long as the counter variable $i is less than 5. It sleeps for a total of 10 seconds.

Do
There are two different do loops in PowerShell: do until and do while . do until runs while
the specified condition is false.

The following example is a numbers game that continues until the value you guess equals the
same number that the Get-Random cmdlet generated.

 PowerShell

 $number = Get-Random -Minimum 1 -Maximum 10
 do {
     $guess = Read-Host -Prompt "What's your guess?"
     if ($guess -lt $number) {
         Write-Output 'Too low!'
     } elseif ($guess -gt $number) {
         Write-Output 'Too high!'
     }
 }
 until ($guess -eq $number)

 Output

 What's your guess?: 1
 Too low!
 What's your guess?: 2

<!-- p.175 -->

 Too low!
 What's your guess?: 3

Do While is the opposite. It runs as long as the specified condition is evaluated as true.

 PowerShell

 $number = Get-Random -Minimum 1 -Maximum 10
 do {
     $guess = Read-Host -Prompt "What's your guess?"
     if ($guess -lt $number) {
         Write-Output 'Too low!'
     } elseif ($guess -gt $number) {
         Write-Output 'Too high!'
     }
 }
 while ($guess -ne $number)

 Output

 What's your guess?: 1
 Too low!
 What's your guess?: 2
 Too low!
 What's your guess?: 3
 Too low!
 What's your guess?: 4

The same results are achieved with a Do While loop by reversing the test condition to not
equals.

do loops always run at least once because the condition is evaluated at the end of the loop.

While
Like the do while loop, a while loop runs as long as the specified condition is true. The
difference, however, is that a while loop evaluates the condition at the top of the loop before
any code is run. So, it doesn't run if the condition is evaluated as false.

The following example calculates what day Thanksgiving Day is on in the United States. It's
always on the fourth Thursday of November. The loop starts with the 22nd day of November
and adds a day, while the day of the week isn't equal to Thursday. If the 22nd is a Thursday, the
loop doesn't run at all.

 PowerShell

<!-- p.176 -->

 $date = Get-Date -Date 'November 22'
 while ($date.DayOfWeek -ne 'Thursday') {
     $date = $date.AddDays(1)
 }
 Write-Output $date

 Output

 Thursday, November 23, 2017 12:00:00 AM

break, continue, and return
The break keyword is designed to exit a loop and is often used with the switch statement. In
the following example, break causes the loop to end after the first iteration.

 PowerShell

 for ($i = 1; $i -lt 5; $i++) {
     Write-Output "Sleeping for $i seconds"
     Start-Sleep -Seconds $i
     break
 }

 Output

 Sleeping for 1 seconds

The continue keyword is designed to skip to the next iteration of a loop.

The following example outputs the numbers 1, 2, 4, and 5. It skips number 3 and continues
with the next iteration of the loop. Like break , continue breaks out of the loop except only for
the current iteration. Execution continues with the next iteration instead of breaking out of the
loop altogether and stopping.

 PowerShell

 while ($i -lt 5) {
     $i += 1
     if ($i -eq 3) {
         continue
     }
     Write-Output $i
 }

<!-- p.177 -->

 Output

 1
 2
 4
 5

The return keyword is designed to exit out of the existing scope.

Notice in the following example that return outputs the first result and then exits out of the
loop.

 PowerShell

 $number = 1..10
 foreach ($n in $number) {
     if ($n -ge 4) {
         return $n
     }
 }

 Output

 4

A more thorough explanation of the result statement can be found in one of my blog articles:
The PowerShell return keyword     .

Summary
In this chapter, you learned about the different types of loops that exist in PowerShell.

Review
     1. What's the difference between the ForEach-Object cmdlet and the foreach statement?
     2. What's the primary advantage of using a while loop instead of a do while or do until
        loop?
     3. How do the break and continue statements differ?

References
        ForEach-Object
        about_Foreach

<!-- p.178 -->

     about_For
     about_Do
     about_While
     about_Break
     about_Continue
     about_Return

Next steps
In Chapter 7, you'll learn how to retrieve and work with system information using Windows
Management Instrumentation (WMI) and the Common Information Model (CIM). You'll explore
modern CIM-based cmdlets, understand how they differ from legacy WMI commands, and use
them to query local and remote systems efficiently.

Last updated on 03/30/2026

<!-- p.179 -->

Chapter 7 - Working with WMI

WMI and CIM
Windows PowerShell ships by default with cmdlets for working with other technologies, such as
Windows Management Instrumentation (WMI). The WMI cmdlets are deprecated and aren't
available in PowerShell 6+, but are covered here as you might encounter them in older scripts
running on Windows PowerShell. For new development, use the CIM cmdlets instead.

Several native WMI cmdlets exist in PowerShell without you having to install any other software
or modules. Get-Command can be used to determine what WMI cmdlets exist in Windows
PowerShell. The following results are from a Windows 11 system running PowerShell version
5.1. Your results might differ depending on the PowerShell version you're running.

 PowerShell
 Get-Command -Noun WMI*

 Output
 CommandType      Name                                                    Version
 -----------      ----                                                    -------
 Cmdlet           Get-WmiObject                                           3.1.0.0
 Cmdlet           Invoke-WmiMethod                                        3.1.0.0
 Cmdlet           Register-WmiEvent                                       3.1.0.0
 Cmdlet           Remove-WmiObject                                        3.1.0.0
 Cmdlet           Set-WmiInstance                                         3.1.0.0

The Common Information Model (CIM) cmdlets were introduced in PowerShell 3.0 and are
grouped within a dedicated module. To list all available CIM cmdlets, use the Get-Command
cmdlet with the Module parameter, as shown in the following example.

 PowerShell
 Get-Command -Module CimCmdlets

 Output
 CommandType      Name                                                    Version
 -----------      ----                                                    -------
 Cmdlet           Export-BinaryMiLog                                      1.0.0.0
 Cmdlet           Get-CimAssociatedInstance                               1.0.0.0
 Cmdlet           Get-CimClass                                            1.0.0.0
 Cmdlet           Get-CimInstance                                         1.0.0.0
 Cmdlet           Get-CimSession                                          1.0.0.0

<!-- p.180 -->

 Cmdlet           Import-BinaryMiLog                                    1.0.0.0
 Cmdlet           Invoke-CimMethod                                      1.0.0.0
 Cmdlet           New-CimInstance                                       1.0.0.0
 Cmdlet           New-CimSession                                        1.0.0.0
 Cmdlet           New-CimSessionOption                                  1.0.0.0
 Cmdlet           Register-CimIndicationEvent                           1.0.0.0
 Cmdlet           Remove-CimInstance                                    1.0.0.0
 Cmdlet           Remove-CimSession                                     1.0.0.0
 Cmdlet           Set-CimInstance                                       1.0.0.0

The CIM cmdlets still allow you to work with WMI, so don't be confused when someone states:
"When I query WMI with the PowerShell CIM cmdlets".

As previously mentioned, WMI is a separate technology from PowerShell, and you're just using
the CIM cmdlets to access WMI. You might find an old VBScript that uses WMI Query Language
(WQL) to query WMI, such as in the following example.

 VB
 strComputer = "."
 Set objWMIService = GetObject("winmgmts:" _
     & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\CIMV2")

 Set colBIOS = objWMIService.ExecQuery _
     ("Select * from Win32_BIOS")

 For each objBIOS in colBIOS
      Wscript.Echo "Manufacturer: " & objBIOS.Manufacturer
      Wscript.Echo "Name: " & objBIOS.Name
      Wscript.Echo "Serial Number: " & objBIOS.SerialNumber
      Wscript.Echo "SMBIOS Version: " & objBIOS.SMBIOSBIOSVersion
      Wscript.Echo "Version: " & objBIOS.Version
 Next

You can take the WQL query from the VBScript and use it with the Get-CimInstance cmdlet
without any modifications.

 PowerShell

 Get-CimInstance -Query 'Select * from Win32_BIOS'

 Output
 SMBIOSBIOSVersion : 090006
 Manufacturer      : American Megatrends Inc.
 Name              : Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80GHz
 SerialNumber      : 3810-1995-1654-4615-2295-2755-89
 Version           : VRTUAL - 4001628

<!-- p.181 -->

The previous example isn't how I typically query WMI with PowerShell. But it works and allows
you to easily migrate existing Visual Basic scripts to PowerShell. When writing a one-liner to
query WMI, I use the following syntax.

 PowerShell
 Get-CimInstance -ClassName Win32_BIOS

 Output

 SMBIOSBIOSVersion : 090006
 Manufacturer      : American Megatrends Inc.
 Name              : Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80GHz
 SerialNumber      : 3810-1995-1654-4615-2295-2755-89
 Version           : VRTUAL - 4001628

If you only want the serial number, pipe the output to Select-Object and specify only the
SerialNumber property.

 PowerShell

 Get-CimInstance -ClassName Win32_BIOS |
     Select-Object -Property SerialNumber

 Output

 SerialNumber
 ------------
 3810-1995-1654-4615-2295-2755-89

By default, when querying WMI, several properties that are never used are retrieved behind the
scenes. It doesn't matter much when querying WMI on the local computer. But once you start
querying remote computers, it's not only extra processing time to return that information but
also more unnecessary information to send across the network. Get-CimInstance has a
Property parameter that limits the information retrieved, making the WMI query more efficient.

 PowerShell
 Get-CimInstance -ClassName Win32_BIOS -Property SerialNumber |
     Select-Object -Property SerialNumber

 Output

 SerialNumber
 ------------

<!-- p.182 -->

 3810-1995-1654-4615-2295-2755-89

The previous results returned an object. To return a string, use the ExpandProperty parameter.

 PowerShell
 Get-CimInstance -ClassName Win32_BIOS -Property SerialNumber |
     Select-Object -ExpandProperty SerialNumber

 Output

 3810-1995-1654-4615-2295-2755-89

You could also use the dotted syntax style to return a string, eliminating the need to pipe to
Select-Object .

 PowerShell

 (Get-CimInstance -ClassName Win32_BIOS -Property SerialNumber).SerialNumber

 Output
 3810-1995-1654-4615-2295-2755-89

Query Remote Computers with the CIM cmdlets
You should still be running PowerShell as a local admin and domain user. When you try to
query information from a remote computer using the Get-CimInstance cmdlet, you receive an
access denied error message.

 PowerShell

 Get-CimInstance -ComputerName dc01 -ClassName Win32_BIOS

 Output
 Get-CimInstance : Access is denied.
 At line:1 char:1
 + Get-CimInstance -ComputerName dc01 -ClassName Win32_BIOS
 + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     + CategoryInfo          : PermissionDenied: (root\cimv2:Win32_BIOS:Stri
    ng) [Get-CimInstance], CimException
     + FullyQualifiedErrorId : HRESULT 0x80070005,Microsoft.Management.Infra
    structure.CimCmdlets.GetCimInstanceCommand
     + PSComputerName        : dc01

<!-- p.183 -->

Many people have security concerns regarding PowerShell, but you have the same permissions
in PowerShell as in the GUI. No more and no less. The problem in the previous example is that
the user running PowerShell doesn't have rights to query WMI information from the DC01
server. You could relaunch PowerShell as a domain administrator since Get-CimInstance
doesn't have a Credential parameter. But that isn't a good idea because anything you run from
PowerShell would run as a domain admin. Depending on the situation, that scenario could be
dangerous from a security standpoint.

Using the principle of least privilege, elevate to your domain admin account on a per-
command basis using the Credential parameter if a command has one. Get-CimInstance
doesn't have a Credential parameter, so the solution in this scenario is to create a CimSession
first. Then, use the CimSession instead of a computer name to query WMI on the remote
computer.

 PowerShell
 $CimSession = New-CimSession -ComputerName dc01 -Credential (Get-Credential)

 Output
 cmdlet Get-Credential at command pipeline position 1
 Supply values for the following parameters:
 Credential

The CIM session was stored in a variable named $CimSession . Notice that you also specify the
Get-Credential cmdlet in parentheses so that it executes first, prompting for alternate

credentials, before creating the new session. I show you another more efficient way to specify
alternate credentials later in this chapter, but it's important to understand this basic concept
before making it more complicated.

You can now use the CIM session created in the previous example with the Get-CimInstance
cmdlet to query the BIOS information from WMI on the remote computer.

 PowerShell
 Get-CimInstance -CimSession $CimSession -ClassName Win32_BIOS

 Output
 SMBIOSBIOSVersion : 090006
 Manufacturer      : American Megatrends Inc.
 Name              : Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80GHz
 SerialNumber      : 0986-6980-3916-0512-6608-8243-13

<!-- p.184 -->

 Version             : VRTUAL - 4001628
 PSComputerName      : dc01

There are several other benefits to using CIM sessions instead of just specifying a computer
name. When you run multiple queries to the same computer, using a CIM session is more
efficient than using the computer name for each query. Creating a CIM session only sets up the
connection once. Then, multiple queries use that same session to retrieve information. Using
the computer name requires the cmdlets to set up and tear down the connection with each
query.

The Get-CimInstance cmdlet uses the WSMan protocol by default, which means the remote
computer needs PowerShell version 3.0 or higher to connect. It's actually not the PowerShell
version that matters, it's the stack version. The stack version can be determined using the Test-
WSMan cmdlet. It needs to be version 3.0, which you find with PowerShell version 3.0 and higher.

 PowerShell
 Test-WSMan -ComputerName dc01

 Output
 wsmid           : http://schemas.dmtf.org/wbem/wsman/identity/1/wsmanidentit
                   y.xsd
 ProtocolVersion : http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd
 ProductVendor   : Microsoft Corporation
 ProductVersion : OS: 0.0.0 SP: 0.0 Stack: 3.0

The older WMI cmdlets use the DCOM protocol, which is compatible with older versions of
Windows. However, the firewall typically blocks DCOM on newer versions of Windows. The
New-CimSessionOption cmdlet allows you to create a DCOM protocol connection for use with
New-CimSession . This option allows the Get-CimInstance cmdlet to communicate with versions

of Windows as old as Windows Server 2000. This ability also means that PowerShell isn't
required on the remote computer when using the Get-CimInstance cmdlet with a CimSession
configured to use the DCOM protocol.

Create the DCOM protocol option using the New-CimSessionOption cmdlet and store it in a
variable.

 PowerShell
 $DCOM = New-CimSessionOption -Protocol Dcom

For efficiency, you can store your domain administrator or elevated credentials in a variable so
you don't have to constantly enter them for each command.

<!-- p.185 -->

 PowerShell
 $Cred = Get-Credential

 Output
 cmdlet Get-Credential at command pipeline position 1
 Supply values for the following parameters:
 Credential

I have a server named SQL03 that runs Windows Server 2008 (non-R2). It's the newest
Windows Server operating system that doesn't have PowerShell installed by default.

Create a CimSession to SQL03 using the DCOM protocol.

 PowerShell
 $CimSession = New-CimSession -ComputerName sql03 -SessionOption $DCOM -Credential
 $Cred

Notice in the previous command that you specify the variable named $Cred as the value for
the Credential parameter instead of manually entering your credentials again.

The output of the query is the same regardless of the underlying protocol.

 PowerShell
 Get-CimInstance -CimSession $CimSession -ClassName Win32_BIOS

 Output
 SMBIOSBIOSVersion : 090006
 Manufacturer      : American Megatrends Inc.
 Name              : Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80GHz
 SerialNumber      : 7237-7483-8873-8926-7271-5004-86
 Version           : VRTUAL - 4001628
 PSComputerName    : sql03

The Get-CimSession cmdlet is used to see what CimSessions are currently connected and what
protocols they use.

 PowerShell
 Get-CimSession

 Output

<!-- p.186 -->

 Id           : 1
 Name         : CimSession1
 InstanceId   : 80742787-e38e-41b1-a7d7-fa1369cf1402
 ComputerName : dc01
 Protocol     : WSMAN

 Id           : 2
 Name         : CimSession2
 InstanceId   : 8fcabd81-43cf-4682-bd53-ccce1e24aecb
 ComputerName : sql03
 Protocol     : DCOM

Retrieve and store the previously created CimSessions in a variable named $CimSession .

 PowerShell
 $CimSession = Get-CimSession

Query both computers with one command, one using the WSMan protocol and the other with
DCOM.

 PowerShell
 Get-CimInstance -CimSession $CimSession -ClassName Win32_BIOS

 Output
 SMBIOSBIOSVersion : 090006
 Manufacturer      : American Megatrends Inc.
 Name              : Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80GHz
 SerialNumber      : 0986-6980-3916-0512-6608-8243-13
 Version           : VRTUAL - 4001628
 PSComputerName    : dc01

 SMBIOSBIOSVersion : 090006
 Manufacturer      : American Megatrends Inc.
 Name              : Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80GHz
 SerialNumber      : 7237-7483-8873-8926-7271-5004-86
 Version           : VRTUAL - 4001628
 PSComputerName    : sql03

One of my blog articles on WMI and CIM cmdlets features a PowerShell function that
automatically detects whether to use WSMan or DCOM and then sets up the appropriate CIM
session for you. For more information, see PowerShell Function to Create CimSessions to
Remote Computers with Fallback to Dcom .

When you finish with the CIM sessions, remove them with the Remove-CimSession cmdlet. To
remove all CIM sessions, pipe Get-CimSession to Remove-CimSession .

<!-- p.187 -->

 PowerShell
 Get-CimSession | Remove-CimSession

Summary
In this chapter, you learned about using PowerShell to work with WMI on local and remote
computers. You also learned how to use the CIM cmdlets to work with remote computers using
the WSMan and DCOM protocols.

Review
  1. What's the difference in the WMI and CIM cmdlets?
  2. By default, what protocol does the Get-CimInstance cmdlet use?
  3. What are some benefits of using a CIM session instead of specifying a computer name
     with Get-CimInstance ?
  4. How do you specify an alternate protocol other than the default one for use with Get-
     CimInstance ?

  5. How do you close or remove CIM sessions?

References
     about_WMI
     about_WMI_Cmdlets
     about_WQL
     CimCmdlets Module
     Video: Using CIM Cmdlets and CIM Sessions

Next steps
In Chapter 8, you'll learn about PowerShell remoting. You'll explore how to run commands on
remote systems, understand one-to-one and one-to-many remoting scenarios, and learn how
remoting enables scalable automation across multiple computers.

Last updated on 02/06/2026

<!-- p.188 -->

Chapter 8 - PowerShell remoting
PowerShell offers several ways to run commands against remote computers. In the last chapter,
you explored how to remotely query WMI using the CIM cmdlets. PowerShell also includes
several cmdlets that feature a built-in ComputerName parameter.

As shown in the following example, you can use Get-Command with the ParameterName
parameter to identify cmdlets that include a ComputerName parameter.

 PowerShell
 Get-Command -ParameterName ComputerName

 Output
 CommandType Name              Version Source
 ----------- ----              ------- ------
 Cmdlet      Add-Computer      3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Clear-EventLog    3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Connect-PSSession 3.0.0.0 Microsoft.PowerShell.Core
 Cmdlet      Enter-PSSession   3.0.0.0 Microsoft.PowerShell.Core
 Cmdlet      Get-EventLog      3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Get-HotFix        3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Get-Process       3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Get-PSSession     3.0.0.0 Microsoft.PowerShell.Core
 Cmdlet      Get-Service       3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Get-WmiObject     3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Invoke-Command    3.0.0.0 Microsoft.PowerShell.Core
 Cmdlet      Invoke-WmiMethod 3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Limit-EventLog    3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      New-EventLog      3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      New-PSSession     3.0.0.0 Microsoft.PowerShell.Core
 Cmdlet      Receive-Job       3.0.0.0 Microsoft.PowerShell.Core
 Cmdlet      Receive-PSSession 3.0.0.0 Microsoft.PowerShell.Core
 Cmdlet      Register-WmiEvent 3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Remove-Computer   3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Remove-EventLog   3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Remove-PSSession 3.0.0.0 Microsoft.PowerShell.Core
 Cmdlet      Remove-WmiObject 3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Rename-Computer   3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Restart-Computer 3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Send-MailMessage 3.1.0.0 Microsoft.PowerShell.Utility
 Cmdlet      Set-Service       3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Set-WmiInstance   3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Show-EventLog     3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Stop-Computer     3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Test-Connection   3.1.0.0 Microsoft.PowerShell.Management
 Cmdlet      Write-EventLog    3.1.0.0 Microsoft.PowerShell.Management

<!-- p.189 -->

Commands such as Get-Process and Get-HotFix include a ComputerName parameter, but this
approach isn't the long-term direction Microsoft recommends for running commands against
remote systems. Even when you find a command with a ComputerName parameter, it often
lacks a Credential parameter, making it difficult to specify alternate credentials. Running
PowerShell from an elevated session doesn't guarantee success, as a network firewall can block
the request between your system and the remote computer.

To use the PowerShell remoting commands demonstrated in this chapter, PowerShell remoting
must be enabled on the remote computer. You can enable it by running the Enable-PSRemoting
cmdlet.

 PowerShell
 Enable-PSRemoting

 Output
 WinRM has been updated to receive requests.
 WinRM service type changed successfully.
 WinRM service started.

 WinRM has been updated for remote management.
 WinRM firewall exception enabled.

One-to-one remoting
If you want an interactive remote session, one-to-one remoting is what you want. This type of
remoting is provided via the Enter-PSSession cmdlet.

Store your domain admin credentials in the $Cred variable. This approach allows you to enter
your credentials once and reuse them on a per-command basis as long as your current
PowerShell session remains active.

 PowerShell
 $Cred = Get-Credential

Establish a one-to-one PowerShell remoting session to the domain controller named dc01.

 PowerShell
 Enter-PSSession -ComputerName dc01 -Credential $Cred

<!-- p.190 -->

Notice the PowerShell prompt is preceded by [dc01] . This prefix indicates you're in an
interactive session with the remote computer named dc01. Any commands you run now
execute on dc01, not your local machine.

 Output

 [dc01]: PS C:\Users\Administrator\Documents>

Remember that you can only access the PowerShell commands and modules installed on the
remote computer. If you installed other modules locally, they aren't available in the remote
session.

When connected via a one-to-one interactive remoting session, it's as if you're sitting directly
at the remote machine.

 PowerShell

 [dc01]: Get-Process | Get-Member

 Output

    TypeName: System.Diagnostics.Process

 Name                          MemberType       Definition
 ----                          ----------       ----------
 Handles                       AliasProperty    Handles = Handlecount
 Name                          AliasProperty    Name = ProcessName
 NPM                           AliasProperty    NPM = NonpagedSystemMemorySize64
 PM                            AliasProperty    PM = PagedMemorySize64
 SI                            AliasProperty    SI = SessionId
 VM                            AliasProperty    VM = VirtualMemorySize64
 WS                            AliasProperty    WS = WorkingSet64
 Disposed                      Event            System.EventHandler Disposed(Sy...
 ErrorDataReceived             Event            System.Diagnostics.DataReceived...
 Exited                        Event            System.EventHandler Exited(Syst...
 OutputDataReceived            Event            System.Diagnostics.DataReceived...
 BeginErrorReadLine            Method           void BeginErrorReadLine()
 BeginOutputReadLine           Method           void BeginOutputReadLine()
 CancelErrorRead               Method           void CancelErrorRead()
 CancelOutputRead              Method           void CancelOutputRead()
 Close                         Method           void Close()
 CloseMainWindow               Method           bool CloseMainWindow()
 CreateObjRef                  Method           System.Runtime.Remoting.ObjRef ...
 Dispose                       Method           void Dispose(), void IDisposabl...
 Equals                        Method           bool Equals(System.Object obj)
 GetHashCode                   Method           int GetHashCode()
 GetLifetimeService            Method           System.Object GetLifetimeService()
 GetType                       Method           type GetType()
 InitializeLifetimeService     Method           System.Object InitializeLifetim...
 Kill                          Method           void Kill()

<!-- p.191 -->

Refresh                    Method         void Refresh()
Start                      Method         bool Start()
ToString                   Method         string ToString()
WaitForExit                Method         bool WaitForExit(int millisecon...
WaitForInputIdle           Method         bool WaitForInputIdle(int milli...
__NounName                 NoteProperty   string __NounName=Process
BasePriority               Property       int BasePriority {get;}
Container                  Property       System.ComponentModel.IContaine...
EnableRaisingEvents        Property       bool EnableRaisingEvents {get;s...
ExitCode                   Property       int ExitCode {get;}
ExitTime                   Property       datetime ExitTime {get;}
Handle                     Property       System.IntPtr Handle {get;}
HandleCount                Property       int HandleCount {get;}
HasExited                  Property       bool HasExited {get;}
Id                         Property       int Id {get;}
MachineName                Property       string MachineName {get;}
MainModule                 Property       System.Diagnostics.ProcessModul...
MainWindowHandle           Property       System.IntPtr MainWindowHandle ...
MainWindowTitle            Property       string MainWindowTitle {get;}
MaxWorkingSet              Property       System.IntPtr MaxWorkingSet {ge...
MinWorkingSet              Property       System.IntPtr MinWorkingSet {ge...
Modules                    Property       System.Diagnostics.ProcessModul...
NonpagedSystemMemorySize   Property       int NonpagedSystemMemorySize {g...
NonpagedSystemMemorySize64 Property       long NonpagedSystemMemorySize64...
PagedMemorySize            Property       int PagedMemorySize {get;}
PagedMemorySize64          Property       long PagedMemorySize64 {get;}
PagedSystemMemorySize      Property       int PagedSystemMemorySize {get;}
PagedSystemMemorySize64    Property       long PagedSystemMemorySize64 {g...
PeakPagedMemorySize        Property       int PeakPagedMemorySize {get;}
PeakPagedMemorySize64      Property       long PeakPagedMemorySize64 {get;}
PeakVirtualMemorySize      Property       int PeakVirtualMemorySize {get;}
PeakVirtualMemorySize64    Property       long PeakVirtualMemorySize64 {g...
PeakWorkingSet             Property       int PeakWorkingSet {get;}
PeakWorkingSet64           Property       long PeakWorkingSet64 {get;}
PriorityBoostEnabled       Property       bool PriorityBoostEnabled {get;...
PriorityClass              Property       System.Diagnostics.ProcessPrior...
PrivateMemorySize          Property       int PrivateMemorySize {get;}
PrivateMemorySize64        Property       long PrivateMemorySize64 {get;}
PrivilegedProcessorTime    Property       timespan PrivilegedProcessorTim...
ProcessName                Property       string ProcessName {get;}
ProcessorAffinity          Property       System.IntPtr ProcessorAffinity...
Responding                 Property       bool Responding {get;}
SafeHandle                 Property       Microsoft.Win32.SafeHandles.Saf...
SessionId                  Property       int SessionId {get;}
Site                       Property       System.ComponentModel.ISite Sit...
StandardError              Property       System.IO.StreamReader Standard...
StandardInput              Property       System.IO.StreamWriter Standard...
StandardOutput             Property       System.IO.StreamReader Standard...
StartInfo                  Property       System.Diagnostics.ProcessStart...
StartTime                  Property       datetime StartTime {get;}
SynchronizingObject        Property       System.ComponentModel.ISynchron...
Threads                    Property       System.Diagnostics.ProcessThrea...
TotalProcessorTime         Property       timespan TotalProcessorTime {get;}
UserProcessorTime          Property       timespan UserProcessorTime {get;}
VirtualMemorySize          Property       int VirtualMemorySize {get;}

<!-- p.192 -->

 VirtualMemorySize64            Property       long VirtualMemorySize64 {get;}
 WorkingSet                     Property       int WorkingSet {get;}
 WorkingSet64                   Property       long WorkingSet64 {get;}
 PSConfiguration                PropertySet    PSConfiguration {Name, Id, Prio...
 PSResources                    PropertySet    PSResources {Name, Id, Handleco...
 Company                        ScriptProperty System.Object Company {get=$thi...
 CPU                            ScriptProperty System.Object CPU {get=$this.To...
 Description                    ScriptProperty System.Object Description {get=...
 FileVersion                    ScriptProperty System.Object FileVersion {get=...
 Path                           ScriptProperty System.Object Path {get=$this.M...
 Product                        ScriptProperty System.Object Product {get=$thi...
 ProductVersion                 ScriptProperty System.Object ProductVersion {g...

When you finish working with the remote computer, run the Exit-PSSession cmdlet to end the
remote session.

 PowerShell
 [dc01]:   Exit-PSSession

One-to-many remoting
While you might occasionally need to perform tasks interactively on a remote computer,
PowerShell remoting becomes more powerful when you simultaneously execute commands
across multiple remote systems. Use the Invoke-Command cmdlet to run commands on one or
more remote computers at the same time.

In the following example, you query three servers for the status of the Windows Time service.
The Get-Service cmdlet is placed inside the script block of Invoke-Command , meaning it
executes on each remote computer.

 PowerShell
 Invoke-Command -ComputerName dc01, sql02, web01 {
     Get-Service -Name W32time
 } -Credential $Cred

The results are returned to your local session as deserialized objects.

 Output
 Status   Name           DisplayName         PSComputerName
 ------   ----           -----------         --------------
 Running W32time         Windows Time        web01
 Start... W32time        Windows Time        dc01
 Running W32time         Windows Time        sql02

<!-- p.193 -->

To confirm the returned objects are deserialized, pipe the output to Get-Member .

 PowerShell
 Invoke-Command -ComputerName dc01, sql02, web01 {
     Get-Service -Name W32time
 } -Credential $Cred | Get-Member

 Output
    TypeName: Deserialized.System.ServiceProcess.ServiceController

 Name                MemberType   Definition
 ----                ----------   ----------
 GetType             Method       type GetType()
 ToString            Method       string ToString(), string ToString(strin...
 Name                NoteProperty string Name=W32time
 PSComputerName      NoteProperty string PSComputerName=dc01
 PSShowComputerName NoteProperty bool PSShowComputerName=True
 RequiredServices    NoteProperty Deserialized.System.ServiceProcess.Servi...
 RunspaceId          NoteProperty guid RunspaceId=5ed06925-8037-43ef-9072-...
 CanPauseAndContinue Property     System.Boolean {get;set;}
 CanShutdown         Property     System.Boolean {get;set;}
 CanStop             Property     System.Boolean {get;set;}
 Container           Property      {get;set;}
 DependentServices   Property     Deserialized.System.ServiceProcess.Servi...
 DisplayName         Property     System.String {get;set;}
 MachineName         Property     System.String {get;set;}
 ServiceHandle       Property     System.String {get;set;}
 ServiceName         Property     System.String {get;set;}
 ServicesDependedOn Property      Deserialized.System.ServiceProcess.Servi...
 ServiceType         Property     System.String {get;set;}
 Site                Property      {get;set;}
 StartType           Property     System.String {get;set;}
 Status              Property     System.String {get;set;}

Notice that most methods are missing from deserialized objects. The methods are missing
because these objects aren't live. They're inert snapshots of the object's state when you
execute the command against the remote computer. For example, you can't start or stop a
service using a deserialized object since it no longer has access to the required methods.

However, this doesn't mean you can't use methods like Stop() with Invoke-Command . The key is
that you must call the method within the remote session.

To demonstrate, stop the Windows Time service on all three remote servers by invoking the
Stop() method remotely.

 PowerShell

<!-- p.194 -->

 Invoke-Command -ComputerName dc01, sql02, web01 {
     (Get-Service -Name W32time).Stop()
 } -Credential $Cred

 Invoke-Command -ComputerName dc01, sql02, web01 {
     Get-Service -Name W32time
 } -Credential $Cred

 Output

 Status     Name          DisplayName         PSComputerName
 ------     ----          -----------         --------------
 Stopped    W32time       Windows Time        web01
 Stopped    W32time       Windows Time        dc01
 Stopped    W32time       Windows Time        sql02

As mentioned in an earlier chapter, if there's a cmdlet available to accomplish a task, it's
preferable to use it rather than calling a method directly. For example, use the Stop-Service
cmdlet instead of the Stop() method to stop a service.

In the previous example, the Stop() method is used to make a point. Some people mistakenly
believe that you can't use methods with PowerShell remoting. While it's true that you can't call
methods on deserialized objects returned to your local session, you can, however, invoke them
within the remote session.

PowerShell sessions
In the final example from the previous section, you ran two commands using the Invoke-
Command cmdlet. This scenario resulted in two separate sessions being established and torn

down. One for each command.

Like CIM sessions, a persistent PowerShell session allows you to run multiple commands
against a remote computer without the overhead of creating a new session for each command.

Create a PowerShell session to each of the three computers you're working with in this chapter,
DC01, SQL02, and WEB01.

 PowerShell
 $Session = New-PSSession -ComputerName dc01, sql02, web01 -Credential $Cred

Now, use the $Session variable to start the Windows Time service by calling its method and
then verify the service status.

<!-- p.195 -->

 PowerShell
 Invoke-Command -Session $Session {(Get-Service -Name W32time).Start()}
 Invoke-Command -Session $Session {Get-Service -Name W32time}

 Output
 Status   Name          DisplayName         PSComputerName
 ------   ----          -----------         --------------
 Running W32time        Windows Time        web01
 Start... W32time       Windows Time        dc01
 Running W32time        Windows Time        sql02

Once you create the session with alternate credentials, you don't need to specify those
credentials again for each command.

Be sure to remove the sessions when you finish using them.

 PowerShell

 Get-PSSession | Remove-PSSession

Summary
In this chapter, you learned the fundamentals of PowerShell remoting, including running
commands interactively on a single remote computer and executing commands across
multiple systems using one-to-many remoting. You also explored the advantages of using
persistent PowerShell sessions when running multiple commands against the same remote
computer.

Review
   1. How do you enable PowerShell remoting?
   2. What PowerShell command do you use to start an interactive session with a remote
     computer?
   3. What's one benefit of using a PowerShell remoting session instead of specifying the
     computer name with each command?
   4. Can you use a PowerShell session in a one-to-one interactive remoting scenario?
   5. What's the difference between the objects returned by cmdlets run locally and objects
     returned when the same cmdlets are executed on remote computers using Invoke-
     Command ?

<!-- p.196 -->

References
      about_Remote
      about_Remote_Output
      about_Remote_Requirements
      about_Remote_Troubleshooting
      about_Remote_Variables
      PowerShell Remoting FAQ

Next steps
In Chapter 9, you'll learn how to write reusable PowerShell functions. You'll explore function
design, parameters, pipeline input, error handling, and best practices for turning one-liners and
scripts into reliable tools.

 Last updated on 02/06/2026

<!-- p.197 -->

Chapter 9 - Functions
PowerShell one-liners and scripts that have to be modified often are good candidates to turn
into reusable functions.

Write functions whenever possible because they're more tool-oriented. You can add the
functions to a script module, put that module in a location defined in the $env:PSModulePath ,
and call the functions without needing to locate where you saved the functions. Using the
PowerShellGet module, it's easy to share your PowerShell modules in a NuGet repository.
PowerShellGet ships with PowerShell version 5.0 and higher. It's also available as a separate
download for PowerShell version 3.0 and higher.

Don't overcomplicate things. Keep it simple and use the most straightforward way to
accomplish a task. Avoid aliases and positional parameters in any code that you reuse. Format
your code for readability. Don't hardcode values; use parameters and variables. Don't write
unnecessary code even if it doesn't hurt anything. It adds unnecessary complexity. Attention to
detail goes a long way when writing any PowerShell code.

Naming
When naming your functions in PowerShell, use a Pascal case name with an approved verb and
a singular noun. To obtain a list of approved verbs in PowerShell, run Get-Verb . The following
example sorts the results of Get-Verb by the Verb property.

 PowerShell

 Get-Verb | Sort-Object -Property Verb

The Group property gives you an idea of how the verbs are meant to be used.

 Output

 Verb          Group
 ----          -----
 Add           Common
 Approve       Lifecycle
 Assert        Lifecycle
 Backup        Data
 Block         Security
 Checkpoint    Data
 Clear         Common

<!-- p.198 -->

Close       Common
Compare     Data
Complete    Lifecycle
Compress    Data
Confirm     Lifecycle
Connect     Communications
Convert     Data
ConvertFrom Data
ConvertTo   Data
Copy        Common
Debug       Diagnostic
Deny        Lifecycle
Disable     Lifecycle
Disconnect Communications
Dismount    Data
Edit        Data
Enable      Lifecycle
Enter       Common
Exit        Common
Expand      Data
Export      Data
Find        Common
Format      Common
Get         Common
Grant       Security
Group       Data
Hide        Common
Import      Data
Initialize Data
Install     Lifecycle
Invoke      Lifecycle
Join        Common
Limit       Data
Lock        Common
Measure     Diagnostic
Merge       Data
Mount       Data
Move        Common
New         Common
Open        Common
Optimize    Common
Out         Data
Ping        Diagnostic
Pop         Common
Protect     Security
Publish     Data
Push        Common
Read        Communications
Receive     Communications
Redo        Common
Register    Lifecycle
Remove      Common
Rename      Common
Repair      Diagnostic
Request     Lifecycle

<!-- p.199 -->

 Reset         Common
 Resize        Common
 Resolve       Diagnostic
 Restart       Lifecycle
 Restore       Data
 Resume        Lifecycle
 Revoke        Security
 Save          Data
 Search        Common
 Select        Common
 Send          Communications
 Set           Common
 Show          Common
 Skip          Common
 Split         Common
 Start         Lifecycle
 Step          Common
 Stop          Lifecycle
 Submit        Lifecycle
 Suspend       Lifecycle
 Switch        Common
 Sync          Data
 Test          Diagnostic
 Trace         Diagnostic
 Unblock       Security
 Undo          Common
 Uninstall     Lifecycle
 Unlock        Common
 Unprotect     Security
 Unpublish     Data
 Unregister    Lifecycle
 Update        Data
 Use           Other
 Wait          Lifecycle
 Watch         Common
 Write         Communications

It's important to use an approved verb for your PowerShell functions. Modules that contain
functions with unapproved verbs generate a warning message when they're imported into a
PowerShell session. That warning message makes your functions look unprofessional.
Unapproved verbs also limit the discoverability of your functions.

A simple function
A function in PowerShell is declared with the function keyword followed by the function name
and then an opening and closing curly brace ( { } ). The code executed by the function is
contained within those curly braces.

 PowerShell

<!-- p.200 -->

 function Get-Version {
     $PSVersionTable.PSVersion
 }

The function shown in the following example is a simple example that returns the version of
PowerShell.

 PowerShell

 Get-Version

 Output

 Major    Minor   Build   Revision
 -----    -----   -----   --------
 5        1       14393   693

When you use a generic name for your functions, such as Get-Version , it could cause naming
conflicts. Default commands added in the future or commands that others might write could
conflict with them. Prefix the noun portion of your function names to help prevent naming
conflicts. For example: <ApprovedVerb>-<Prefix><SingularNoun> .

The following example uses the prefix PS .

 PowerShell

 function Get-PSVersion {
     $PSVersionTable.PSVersion
 }

Other than the name, this function is identical to the previous one.

 PowerShell

 Get-PSVersion

 Output

 Major    Minor   Build   Revision
 -----    -----   -----   --------
 5        1       14393   693
