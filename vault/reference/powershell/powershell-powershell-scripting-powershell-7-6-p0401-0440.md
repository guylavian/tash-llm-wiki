---
title: "How to use this documentation — pages 401-440"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0401-0440
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0401-0440
family: powershell
documentKind: "doc"
abstract: "PowerShell PS> $null -eq $undefined.Some.Fake.Property True PS> $date = Get-Date PS> $null -eq $date.Some.Fake.Property True Method on a null-valued expression Calling a method on a $null object throws a RuntimeException . PowerShell PS> $value = $null PS> $value.ToString() You"
---

# How to use this documentation — pages 401-440

<!-- p.401 -->

  PowerShell

  PS> $null -eq $undefined.Some.Fake.Property
  True

  PS> $date = Get-Date
  PS> $null -eq $date.Some.Fake.Property
  True

Method on a null-valued expression
Calling a method on a $null object throws a RuntimeException .

  PowerShell

  PS> $value = $null
  PS> $value.ToString()
  You cannot call a method on a null-valued expression.
  At line:1 char:1
  + $value.ToString()
  + ~~~~~~~~~~~~~~~~~
      + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
      + FullyQualifiedErrorId : InvokeMethodOnNull

Whenever I see the phrase You cannot call a method on a null-valued expression then the
first thing I look for are places where I am calling a method on a variable without first checking
it for $null .

Checking for $null
You may have noticed that I always place the $null on the left when checking for $null in my
examples. This is intentional and accepted as a PowerShell best practice. There are some
scenarios where placing it on the right doesn't give you the expected result.

Look at this next example and try to predict the results:

  PowerShell

  if ( $value -eq $null )
  {
      'The array is $null'
  }
  if ( $value -ne $null )
  {
      'The array is not $null'
  }

<!-- p.402 -->

If I do not define $value , the first one evaluates to $true and our message is The array is
$null . The trap here is that it's possible to create a $value that allows both of them to be

$false

 PowerShell

 $value = @( $null )

In this case, the $value is an array that contains a $null . The -eq checks every value in the
array and returns the $null that is matched. This evaluates to $false . The -ne returns
everything that doesn't match $null and in this case there are no results (This also evaluates to
$false ). Neither one is $true even though it looks like one of them should be.

Not only can we create a value that makes both of them evaluate to $false , it's possible to
create a value where they both evaluate to $true . Mathias Jessen (@IISResetMe) has a good
post     that dives into that scenario.

PSScriptAnalyzer and VS Code
The PSScriptAnalyzer      module has a rule that checks for this issue called
PSPossibleIncorrectComparisonWithNull .

 PowerShell

 PS> Invoke-ScriptAnalyzer ./myscript.ps1

 RuleName                              Message
 --------                              -------
 PSPossibleIncorrectComparisonWithNull $null should be on the left side of equality
 comparisons.

Because VS Code uses the PSScriptAnalyser rules too, it also highlights or identifies this as a
problem in your script.

Simple if check
A common way that people check for a non-$null value is to use a simple if() statement
without the comparison.

 PowerShell

 if ( $value )
 {

<!-- p.403 -->

       Do-Something
  }

If the value is $null , this evaluates to $false . This is easy to read, but be careful that it's
looking for exactly what you're expecting it to look for. I read that line of code as:

  If $value has a value.

But that's not the whole story. That line is actually saying:

  If $value is not $null or 0 or $false or an empty string or an empty array.

Here is a more complete sample of that statement.

  PowerShell

  if ( $null -ne $value -and
          $value -ne 0 -and
          $value -ne '' -and
          ($value -isnot [array] -or $value.Length -ne 0) -and
          $value -ne $false )
  {
      Do-Something
  }

It's perfectly OK to use a basic if check as long as you remember those other values count as
$false and not just that a variable has a value.

I ran into this issue when refactoring some code a few days ago. It had a basic property check
like this.

  PowerShell

  if ( $object.Property )
  {
      $object.Property = $value
  }

I wanted to assign a value to the object property only if it existed. In most cases, the original
object had a value that would evaluate to $true in the if statement. But I ran into an issue
where the value was occasionally not getting set. I debugged the code and found that the
object had the property but it was a blank string value. This prevented it from ever getting
updated with the previous logic. So I added a proper $null check and everything worked.

<!-- p.404 -->

  PowerShell

  if ( $null -ne $object.Property )
  {
      $object.Property = $value
  }

It's little bugs like these that are hard to spot and make me aggressively check values for
$null .

$null.Count
If you try to access a property on a $null value, that the property is also $null . The Count
property is the exception to this rule.

  PowerShell

  PS> $value = $null
  PS> $value.Count
  0

When you have a $null value, then the Count is 0 . This special property is added by
PowerShell.

[PSCustomObject] Count
Almost all objects in PowerShell have that Count property. One important exception is the
[pscustomobject] in Windows PowerShell 5.1 (This is fixed in PowerShell 6.0). It doesn't have a

Count property so you get a $null value if you try to use it. I call this out here so that you

don't try to use Count instead of a $null check.

Running this example on Windows PowerShell 5.1 and PowerShell 6.0 gives you different
results.

  PowerShell

  $value = [pscustomobject]@{Name='MyObject'}
  if ( $value.Count -eq 1 )
  {
      "We have a value"
  }

Enumerable null

<!-- p.405 -->

There is one special type of $null that acts differently than the others. I am going to call it the
enumerable null but it's really a System.Management.Automation.Internal.AutomationNull. This
enumerable null is the one you get as the result of a function or script block that returns
nothing (a void result).

 PowerShell

 PS> function Get-Nothing {}
 PS> $nothing = Get-Nothing
 PS> $null -eq $nothing
 True

If you compare it with $null , you get a $null value. When used in an evaluation where a value
is required, the value is always $null . But if you place it inside an array, it's treated the same as
an empty array.

 PowerShell

 PS> $containEmpty = @( @() )
 PS> $containNothing = @($nothing)
 PS> $containNull = @($null)

 PS> $containEmpty.Count
 0
 PS> $containNothing.Count
 0
 PS> $containNull.Count
 1

You can have an array that contains one $null value and its Count is 1 . But if you place an
empty array inside an array then it's not counted as an item. The count is 0 .

If you treat the enumerable null like a collection, then it's empty.

If you pass in an enumerable null to a function parameter that isn't strongly typed, PowerShell
coerces the enumerable null into a $null value by default. This means inside the function, the
value is treated as $null instead of the
System.Management.Automation.Internal.AutomationNull type.

Pipeline
The primary place you see the difference is when using the pipeline. You can pipe a $null
value but not an enumerable null value.

<!-- p.406 -->

 PowerShell

 PS> $null | ForEach-Object{ Write-Output 'NULL Value' }
 'NULL Value'
 PS> $nothing | ForEach-Object{ Write-Output 'No Value' }

Depending on your code, you should account for the $null in your logic.

Either check for $null first

     Filter out null on the pipeline ( ... | where {$null -ne $_} | ... )
     Handle it in the pipeline function

foreach
One of my favorite features of foreach is that it doesn't enumerate over a $null collection.

 PowerShell

 foreach ( $node in $null )
 {
     #skipped
 }

This saves me from having to $null check the collection before I enumerate it. If you have a
collection of $null values, the $node can still be $null .

The foreach started working this way with PowerShell 3.0. If you happen to be on an older
version, then this is not the case. This is one of the important changes to be aware of when
back-porting code for 2.0 compatibility.

Value types
Technically, only reference types can be $null . But PowerShell is very generous and allows for
variables to be any type. If you decide to strongly type a value type, it cannot be $null .
PowerShell converts $null to a default value for many types.

 PowerShell

 PS> [int]$number = $null
 PS> $number
 0

 PS> [bool]$boolean = $null
 PS> $boolean

<!-- p.407 -->

  False

  PS> [string]$string = $null
  PS> $string -eq ''
  True

There are some types that do not have a valid conversion from $null . These types generate a
Cannot convert null to type error.

  PowerShell

  PS> [datetime]$date = $null
  Cannot convert null to type "System.DateTime".
  At line:1 char:1
  + [datetime]$date = $null
  + ~~~~~~~~~~~~~~~~~~~~~~~
      + CategoryInfo          : MetadataError: (:) [],
  ArgumentTransformationMetadataException
      + FullyQualifiedErrorId : RuntimeException

Function parameters
Using a strongly typed values in function parameters is very common. We generally learn to
define the types of our parameters even if we tend not to define the types of other variables in
our scripts. You may already have some strongly typed variables in your functions and not even
realize it.

  PowerShell

  function Do-Something
  {
      param(
          [string] $Value
      )
  }

As soon as you set the type of the parameter as a string , the value can never be $null . It's
common to check if a value is $null to see if the user provided a value or not.

  PowerShell

  if ( $null -ne $Value ){...}

$Value is an empty string '' when no value is provided. Use the automatic variable

$PSBoundParameters.Value instead.

<!-- p.408 -->

 PowerShell

 if ( $null -ne $PSBoundParameters.Value ){...}

$PSBoundParameters only contains the parameters that were specified when the function was

called. You can also use the ContainsKey method to check for the property.

 PowerShell

 if ( $PSBoundParameters.ContainsKey('Value') ){...}

IsNotNullOrEmpty
If the value is a string, you can use a static string function to check if the value is $null or an
empty string at the same time.

 PowerShell

 if ( -not [string]::IsNullOrEmpty( $value ) ){...}

I find myself using this often when I know the value type should be a string.

When I $null check
I am a defensive scripter. Anytime I call a function and assign it to a variable, I check it for
$null .

 PowerShell

 $userList = Get-ADUser kevmar
 if ($null -ne $userList){...}

I much prefer using if or foreach over using try/catch . Don't get me wrong, I still use
try/catch a lot. But if I can test for an error condition or an empty set of results, I can allow my

exception handling be for true exceptions.

I also tend to check for $null before I index into a value or call methods on an object. These
two actions fail for a $null object so I find it important to validate them first. I already covered
those scenarios earlier in this post.

No results scenario

<!-- p.409 -->

It's important to know that different functions and commands handle the no results scenario
differently. Many PowerShell commands return the enumerable null and an error in the error
stream. But others throw exceptions or give you a status object. It's still up to you to know how
the commands you use deal with the no results and error scenarios.

Initializing to $null
One habit that I have picked up is initializing all my variables before I use them. You are
required to do this in other languages. At the top of my function or as I enter a foreach loop, I
define all the values that I'm using.

Here is a scenario that I want you to take a close look at. It's an example of a bug I had to
chase down before.

      PowerShell

      function Do-Something
      {
          foreach ( $node in 1..6 )
          {
              try
              {
                  $result = Get-Something -Id $node
              }
              catch
              {
                  Write-Verbose "[$result] not valid"
              }

              if ( $null -ne $result )
              {
                  Update-Something $result
              }
          }
      }

The expectation here is that Get-Something returns either a result or an enumerable null. If
there's an error, we log it. Then we check to make sure we got a valid result before processing
it.

The bug hiding in this code is when Get-Something throws an exception and doesn't assign a
value to $result . It fails before the assignment so we don't even assign $null to the $result
variable. $result still contains the previous valid $result from other iterations. Update-
Something to execute multiple times on the same object in this example.

<!-- p.410 -->

I set $result to $null right inside the foreach loop before I use it to mitigate this issue.

 PowerShell

 foreach ( $node in 1..6 )
 {
     $result = $null
     try
     {
         ...

Scope issues
This also helps mitigate scoping issues. In that example, we assign values to $result over and
over in a loop. But because PowerShell allows variable values from outside the function to
bleed into the scope of the current function, initializing them inside your function mitigates
bugs that can be introduced that way.

An uninitialized variable in your function is not $null if it's set to a value in a parent scope. The
parent scope could be another function that calls your function and uses the same variable
names.

If I take that same Do-something example and remove the loop, I would end up with something
that looks like this example:

 PowerShell

 function Invoke-Something
 {
     $result = 'ParentScope'
     Do-Something
 }

 function Do-Something
 {
     try
     {
         $result = Get-Something -Id $node
     }
     catch
     {
         Write-Verbose "[$result] not valid"
     }

      if ( $null -ne $result )
      {
          Update-Something $result

<!-- p.411 -->

        }
  }

If the call to Get-Something throws an exception, then my $null check finds the $result from
Invoke-Something . Initializing the value inside your function mitigates this issue.

Naming variables is hard and it's common for an author to use the same variable names in
multiple functions. I know I use $node , $result , $data all the time. So it would be very easy for
values from different scopes to show up in places where they should not be.

Redirect output to $null
I have been talking about $null values for this entire article but the topic is not complete if I
didn't mention redirecting output to $null . There are times when you have commands that
output information or objects that you want to suppress. Redirecting output to $null does
that.

Out-Null
The Out-Null command is the built-in way to redirect pipeline data to $null .

  PowerShell

  New-Item -Type Directory -Path $path | Out-Null

Assign to $null
You can assign the results of a command to $null for the same effect as using Out-Null .

  PowerShell

  $null = New-Item -Type Directory -Path $path

Because $null is a constant value, you can never overwrite it. I don't like the way it looks in my
code but it often performs faster than Out-Null .

Redirect to $null
You can also use the redirection operator to send output to $null .

  PowerShell

<!-- p.412 -->

  New-Item -Type Directory -Path $path > $null

If you're dealing with command-line executables that output on the different streams. You can
redirect all output streams to $null like this:

  PowerShell

  git status *> $null

Summary
I covered a lot of ground on this one and I know this article is more fragmented than most of
my deep dives. That is because $null values can pop up in many different places in PowerShell
and all the nuances are specific to where you find it. I hope you walk away from this with a
better understanding of $null and an awareness of the more obscure scenarios you may run
into.

 Last updated on 04/16/2025

<!-- p.413 -->

Everything you wanted to know about
ShouldProcess
PowerShell functions have several features that greatly improve the way users interact with
them. One important feature that is often overlooked is -WhatIf and -Confirm support and it's
easy to add to your functions. In this article, we dive deep into how to implement this feature.

  ７ Note

  The original version    of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com       .

This is a simple feature you can enable in your functions to provide a safety net for the users
that need it. There's nothing scarier than running a command that you know can be dangerous
for the first time. The option to run it with -WhatIf can make a big difference.

CommonParameters
Before we look at implementing these common parameters, I want to take a quick look at how
they're used.

Using -WhatIf
When a command supports the -WhatIf parameter, it allows you to see what the command
would have done instead of making changes. it's a good way to test out the impact of a
command, especially before you do something destructive.

 PowerShell

 PS C:\temp> Get-ChildItem
      Directory: C:\temp
 Mode                  LastWriteTime              Length Name
 ----                  -------------              ------ ----
 -a----          4/19/2021   8:59 AM                   0 importantfile.txt
 -a----          4/19/2021   8:58 AM                   0 myfile1.txt
 -a----          4/19/2021   8:59 AM                   0 myfile2.txt

<!-- p.414 -->

 PS C:\temp> Remove-Item -Path .\myfile1.txt -WhatIf
 What if: Performing the operation "Remove File" on target "C:\Temp\myfile1.txt".

If the command correctly implements ShouldProcess , it should show you all the changes that it
would have made. Here is an example using a wildcard to delete multiple files.

 PowerShell

 PS C:\temp> Remove-Item -Path * -WhatIf
 What if: Performing the operation "Remove File" on target "C:\Temp\myfile1.txt".
 What if: Performing the operation "Remove File" on target "C:\Temp\myfile2.txt".
 What if: Performing the operation "Remove File" on target
 "C:\Temp\importantfile.txt".

Using -Confirm
Commands that support -WhatIf also support -Confirm . This gives you a chance confirm an
action before performing it.

 PowerShell

 PS C:\temp> Remove-Item .\myfile1.txt -Confirm

 Confirm
 Are you sure you want to perform this action?
 Performing the operation "Remove File" on target "C:\Temp\myfile1.txt".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default is
 "Y"):

In this case, you have multiple options that allow you to continue, skip a change, or stop the
script. The help prompt describes each of those options like this.

 Output

 Y - Continue with only the next step of the operation.
 A - Continue with all the steps of the operation.
 N - Skip this operation and proceed with the next operation.
 L - Skip this operation and all subsequent operations.
 S - Pause the current pipeline and return to the command prompt. Type "exit" to
 resume the pipeline.
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default is
 "Y"):

Localization

<!-- p.415 -->

This prompt is localized in PowerShell so the language changes based on the language of your
operating system. This is one more thing that PowerShell manages for you.

[switch] parameters

Let's take a quick moment to look at ways to pass a value to a [switch] parameter. The main
reason I call this out is that you often want to pass parameter values to functions you call.

The first approach is a specific parameter syntax that can be used for all parameters but you
mostly see it used for [switch] parameters. You specify a colon to attach a value to the
parameter.

 PowerShell

 Remove-Item -Path:* -WhatIf:$true

You can do the same with a variable.

 PowerShell

 $DoWhatIf = $true
 Remove-Item -Path * -WhatIf:$DoWhatIf

The second approach is to use a hashtable to splat the value.

 PowerShell

 $RemoveSplat = @{
     Path = '*'
     WhatIf = $true
 }
 Remove-Item @RemoveSplat

If you're new to hashtables or splatting, I have another article on that covers everything you
wanted to know about hashtables.

SupportsShouldProcess
The first step to enable -WhatIf and -Confirm support is to specify SupportsShouldProcess in
the CmdletBinding of your function.

 PowerShell

<!-- p.416 -->

 function Test-ShouldProcess {
     [CmdletBinding(SupportsShouldProcess)]
     param()
     Remove-Item .\myfile1.txt
 }

By specifying SupportsShouldProcess in this way, we can now call our function with -WhatIf (or
-Confirm ).

 PowerShell

 PS> Test-ShouldProcess -WhatIf
 What if: Performing the operation "Remove File" on target "C:\Temp\myfile1.txt".

Notice that I did not create a parameter called -WhatIf . Specifying SupportsShouldProcess
automatically creates it for us. When we specify the -WhatIf parameter on Test-ShouldProcess ,
some things we call also perform -WhatIf processing.

  ７ Note

  When you use SupportsShouldProcess , PowerShell doesn't add the $WhatIf variable to the
  function. You don't need to check the value of $WhatIf because the ShouldProcess()
  method takes care of that for you.

Trust but verify
There's some danger here trusting that everything you call inherits -WhatIf values. For the rest
of the examples, I'm going to assume that it doesn't work and be very explicit when making
calls to other commands. I recommend that you do the same.

 PowerShell

 function Test-ShouldProcess {
     [CmdletBinding(SupportsShouldProcess)]
     param()
     Remove-Item .\myfile1.txt -WhatIf:$WhatIfPreference
 }

I will revisit the nuances much later once you have a better understanding of all the pieces in
play.

$PSCmdlet.ShouldProcess

<!-- p.417 -->

The method that allows you to implement SupportsShouldProcess is $PSCmdlet.ShouldProcess .
You call $PSCmdlet.ShouldProcess(...) to see if you should process some logic and PowerShell
takes care of the rest. Let's start with an example:

 PowerShell

 function Test-ShouldProcess {
     [CmdletBinding(SupportsShouldProcess)]
     param()

      $file = Get-ChildItem './myfile1.txt'
      if($PSCmdlet.ShouldProcess($file.Name)){
          $file.Delete()
      }
 }

The call to $PSCmdlet.ShouldProcess($file.Name) checks for the -WhatIf (and -Confirm
parameter) then handles it accordingly. The -WhatIf causes ShouldProcess to output a
description of the change and return $false :

 PowerShell

 PS> Test-ShouldProcess -WhatIf
 What if: Performing the operation "Test-ShouldProcess" on target "myfile1.txt".

A call using -Confirm pauses the script and prompts the user with the option to continue. It
returns $true if the user selected Y .

 PowerShell

 PS> Test-ShouldProcess -Confirm
 Confirm
 Are you sure you want to perform this action?
 Performing the operation "Test-ShouldProcess" on target "myfile1.txt".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default is
 "Y"):

An awesome feature of $PSCmdlet.ShouldProcess is that it doubles as verbose output. I depend
on this often when implementing ShouldProcess .

 PowerShell

 PS> Test-ShouldProcess -Verbose
 VERBOSE: Performing the operation "Test-ShouldProcess" on target "myfile1.txt".

<!-- p.418 -->

Overloads
There are a few different overloads for $PSCmdlet.ShouldProcess with different parameters for
customizing the messaging. We already saw the first one in the example above. Let's take a
closer look at it.

  PowerShell

  function Test-ShouldProcess {
      [CmdletBinding(SupportsShouldProcess)]
      param()

       if($PSCmdlet.ShouldProcess('TARGET')){
           # ...
       }
  }

This produces output that includes both the function name and the target (value of the
parameter).

  PowerShell

  What if: Performing the operation "Test-ShouldProcess" on target "TARGET".

Specifying a second parameter as the operation uses the operation value instead of the
function name in the message.

  PowerShell

  ## $PSCmdlet.ShouldProcess('TARGET','OPERATION')
  What if: Performing the operation "OPERATION" on target "TARGET".

The next option is to specify three parameters to fully customize the message. When three
parameters are used, the first one is the entire message. The second two parameters are still
used in the -Confirm message output.

  PowerShell

  ## $PSCmdlet.ShouldProcess('MESSAGE','TARGET','OPERATION')
  What if: MESSAGE

Quick parameter reference

<!-- p.419 -->

Just in case you came here only to figure out what parameters you should use, here is a quick
reference showing how the parameters change the message in the different -WhatIf scenarios.

 PowerShell

 ## $PSCmdlet.ShouldProcess('TARGET')
 What if: Performing the operation "FUNCTION_NAME" on target "TARGET".

 ## $PSCmdlet.ShouldProcess('TARGET','OPERATION')
 What if: Performing the operation "OPERATION" on target "TARGET".

 ## $PSCmdlet.ShouldProcess('MESSAGE','TARGET','OPERATION')
 What if: MESSAGE

I tend to use the one with two parameters.

ShouldProcessReason
We have a fourth overload that's more advanced than the others. It allows you to get the
reason ShouldProcess was executed. I'm only adding this here for completeness because we
can just check if $WhatIfPreference is $true instead.

 PowerShell

 $reason = ''
 if($PSCmdlet.ShouldProcess('MESSAGE','TARGET','OPERATION',[ref]$reason)){
     Write-Output "Some Action"
 }
 $reason

We have to pass the $reason variable into the fourth parameter as a reference variable with
[ref] . ShouldProcess populates $reason with the value None or WhatIf . I didn't say this was

useful and I have had no reason to ever use it.

Where to place it
You use ShouldProcess to make your scripts safer. So you use it when your scripts are making
changes. I like to place the $PSCmdlet.ShouldProcess call as close to the change as possible.

 PowerShell

 ## general logic and variable work
 if ($PSCmdlet.ShouldProcess('TARGET','OPERATION')){
     # Change goes here
 }

<!-- p.420 -->

If I'm processing a collection of items, I call it for each item. So the call gets placed inside the
foreach loop.

  PowerShell

  foreach ($node in $collection){
      # general logic and variable work
      if ($PSCmdlet.ShouldProcess($node,'OPERATION')){
          # Change goes here
      }
  }

The reason why I place ShouldProcess tightly around the change, is that I want as much code
to execute as possible when -WhatIf is specified. I want the setup and validation to run if
possible so the user gets to see those errors.

I also like to use this in my Pester tests that validate my projects. If I have a piece of logic that is
hard to mock in pester, I can often wrap it in ShouldProcess and call it with -WhatIf in my
tests. It's better to test some of your code than none of it.

$WhatIfPreference
The first preference variable we have is $WhatIfPreference . This is $false by default. If you set
it to $true then your function executes as if you specified -WhatIf . If you set this in your
session, all commands perform -WhatIf execution.

When you call a function with -WhatIf , the value of $WhatIfPreference gets set to $true inside
the scope of your function.

ConfirmImpact
Most of my examples are for -WhatIf but everything so far also works with -Confirm to
prompt the user. You can set the ConfirmImpact of the function to high and it prompts the user
as if it was called with -Confirm .

  PowerShell

  function Test-ShouldProcess {
      [CmdletBinding(
          SupportsShouldProcess,
          ConfirmImpact = 'High'
      )]
      param()

<!-- p.421 -->

      if ($PSCmdlet.ShouldProcess('TARGET')){
          Write-Output "Some Action"
      }
 }

This call to Test-ShouldProcess is performing the -Confirm action because of the High impact.

 PowerShell

 PS> Test-ShouldProcess

 Confirm
 Are you sure you want to perform this action?
 Performing the operation "Test-ShouldProcess" on target "TARGET".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default is
 "Y"): y
 Some Action

The obvious issue is that now it's harder to use in other scripts without prompting the user. In
this case, we can pass a $false to -Confirm to suppress the prompt.

 PowerShell

 PS> Test-ShouldProcess -Confirm:$false
 Some Action

I'll cover how to add -Force support in a later section.

$ConfirmPreference
$ConfirmPreference is an automatic variable that controls when ConfirmImpact asks you to

confirm execution. Here are the possible values for both $ConfirmPreference and
ConfirmImpact .

     High

     Medium

     Low

     None

With these values, you can specify different levels of impact for each function. If you have
$ConfirmPreference set to a value higher than ConfirmImpact , then you aren't prompted to

confirm execution.

<!-- p.422 -->

By default, $ConfirmPreference is set to High and ConfirmImpact is Medium . If you want your
function to automatically prompt the user, set your ConfirmImpact to High . Otherwise set it to
Medium if its destructive and use Low if the command is always safe run in production. If you

set it to none , it doesn't prompt even if -Confirm was specified (but it still gives you -WhatIf
support).

When calling a function with -Confirm , the value of $ConfirmPreference gets set to Low inside
the scope of your function.

Suppressing nested confirm prompts
The $ConfirmPreference can get picked up by functions that you call. This can create scenarios
where you add a confirm prompt and the function you call also prompts the user.

What I tend to do is specify -Confirm:$false on the commands that I call when I have already
handled the prompting.

 PowerShell

 function Test-ShouldProcess {
     [CmdletBinding(SupportsShouldProcess)]
     param()

      $file = Get-ChildItem './myfile1.txt'
      if($PSCmdlet.ShouldProcess($file.Name)){
          Remove-Item -Path $file.FullName -Confirm:$false
      }
 }

This brings us back to an earlier warning: There are nuances as to when -WhatIf is not passed
to a function and when -Confirm passes to a function. I promise I'll get back to this later.

$PSCmdlet.ShouldContinue
If you need more control than ShouldProcess provides, you can trigger the prompt directly
with ShouldContinue . ShouldContinue ignores $ConfirmPreference , ConfirmImpact , -Confirm ,
$WhatIfPreference , and -WhatIf because it prompts every time it's executed.

At a quick glance, it's easy to confuse ShouldProcess and ShouldContinue . I tend to remember
to use ShouldProcess because the parameter is called SupportsShouldProcess in the
CmdletBinding . You should use ShouldProcess in almost every scenario. That is why I covered

that method first.

<!-- p.423 -->

Let's take a look at ShouldContinue in action.

 PowerShell

 function Test-ShouldContinue {
     [CmdletBinding()]
     param()

      if($PSCmdlet.ShouldContinue('TARGET','OPERATION')){
          Write-Output "Some Action"
      }
 }

This provides us a simpler prompt with fewer options.

 PowerShell

 Test-ShouldContinue

 Second
 TARGET
 [Y] Yes    [N] No    [S] Suspend    [?] Help (default is "Y"):

The biggest issue with ShouldContinue is that it requires the user to run it interactively because
it always prompts the user. You should always be building tools that can be used by other
scripts. The way you do this is by implementing -Force . I'll revisit this idea later.

Yes to all
This is automatically handled with ShouldProcess but we have to do a little more work for
ShouldContinue . There's a second method overload where we have to pass in a few values by

reference to control the logic.

 PowerShell

 function Test-ShouldContinue {
     [CmdletBinding()]
     param()

      $collection = 1..5
      $yesToAll = $false
      $noToAll = $false

      foreach($target in $collection) {

           $continue = $PSCmdlet.ShouldContinue(
                   "TARGET_$target",

<!-- p.424 -->

                     'OPERATION',
                     [ref]$yesToAll,
                     [ref]$noToAll
                )

           if ($continue){
               Write-Output "Some Action [$target]"
           }
      }
  }

I added a foreach loop and a collection to show it in action. I pulled the ShouldContinue call
out of the if statement to make it easier to read. Calling a method with four parameters starts
to get a little ugly, but I tried to make it look as clean as I could.

Implementing -Force
ShouldProcess and ShouldContinue need to implement -Force in different ways. The trick to

these implementations is that ShouldProcess should always get executed, but ShouldContinue
should not get executed if -Force is specified.

ShouldProcess -Force
If you set your ConfirmImpact to high , the first thing your users are going to try is to suppress
it with -Force . That's the first thing I do anyway.

  PowerShell

  Test-ShouldProcess -Force
  Error: Test-ShouldProcess: A parameter cannot be found that matches parameter name
  'force'.

If you recall from the ConfirmImpact section, they actually need to call it like this:

  PowerShell

  Test-ShouldProcess -Confirm:$false

Not everyone realizes they need to do that and -Force doesn't suppress ShouldContinue . So
we should implement -Force for the sanity of our users. Take a look at this full example here:

  PowerShell

<!-- p.425 -->

 function Test-ShouldProcess {
     [CmdletBinding(
         SupportsShouldProcess,
         ConfirmImpact = 'High'
     )]
     param(
         [switch]$Force
     )

      if ($Force -and -not $PSBoundParameters.ContainsKey('Confirm')) {
          $ConfirmPreference = 'None'
      }

      if ($PSCmdlet.ShouldProcess('TARGET')) {
          Write-Output "Some Action"
      }
 }

We add our own -Force switch as a parameter. The -Confirm parameter is automatically
added when using SupportsShouldProcess in the CmdletBinding . However, when you use
SupportsShouldProcess , PowerShell doesn't add the $Confirm variable to the function. If you

are running in Strict Mode and try to use the $Confirm variable before it has been defined, you
get an error. To avoid the error you can use $PSBoundParameters to test if the parameter was
passed by the user.

 PowerShell

 if ($Force -and -not $PSBoundParameters.ContainsKey('Confirm')) {
     $ConfirmPreference = 'None'
 }

If the user specifies -Force we set $ConfirmPreference to None in the local scope. If the user
also specifies -Confirm then ShoudProcess() honors the values of the -Confirm parameter.

 PowerShell

 if ($PSCmdlet.ShouldProcess('TARGET')){
     Write-Output "Some Action"
 }

If someone specifies both -Force and -WhatIf , then -WhatIf needs to take priority. This
approach preserves -WhatIf processing because ShouldProcess always gets executed.

Don't add a test for the $Force value inside the if statement with the ShouldProcess . That is
an anti-pattern for this specific scenario even though that's what I show you in the next section

<!-- p.426 -->

for ShouldContinue .

ShouldContinue -Force
This is the correct way to implement -Force with ShouldContinue .

 PowerShell

 function Test-ShouldContinue {
     [CmdletBinding()]
     param(
         [switch]$Force
     )

      if($Force -or $PSCmdlet.ShouldContinue('TARGET','OPERATION')){
          Write-Output "Some Action"
      }
 }

By placing the $Force to the left of the -or operator, it gets evaluated first. Writing it this way
short circuits the execution of the if statement. If $Force is $true , then the ShouldContinue is
not executed.

 PowerShell

 PS> Test-ShouldContinue -Force
 Some Action

We don't have to worry about -Confirm or -WhatIf in this scenario because they're not
supported by ShouldContinue . This is why it needs to be handled differently than
ShouldProcess .

Scope issues
Using -WhatIf and -Confirm are supposed to apply to everything inside your functions and
everything they call. They do this by setting $WhatIfPreference to $true or setting
$ConfirmPreference to Low in the local scope of the function. When you call another function,

calls to ShouldProcess use those values.

This actually works correctly most of the time. Anytime you call built-in cmdlet or a function in
your same scope, it works. It also works when you call a script or a function in a script module
from the console.

<!-- p.427 -->

The one specific place where it doesn't work is when a script or a script module calls a function
in another script module. This may not sound like a big problem, but most of the modules you
create or pull from the PSGallery are script modules.

The core issue is that script modules do not inherit the values for $WhatIfPreference or
$ConfirmPreference (and several others) when called from functions in other script modules.

The best way to summarize this as a general rule is that this works correctly for binary modules
and never trust it to work for script modules. If you aren't sure, either test it or just assume it
doesn't work correctly.

I personally feel this is very dangerous because it creates scenarios where you add -WhatIf
support to multiple modules that work correctly in isolation, but fail to work correctly when
they call each other.

We do have a GitHub RFC working to get this issue fixed. See Propagate execution preferences
beyond script module scope       for more details.

In closing
I have to look up how to use ShouldProcess every time I need to use it. It took me a long time
to distinguish ShouldProcess from ShouldContinue . I almost always need to look up what
parameters to use. So don't worry if you still get confused from time to time. This article will be
here when you need it. I'm sure I will reference it often myself.

If you liked this post, please share your thoughts with me on Twitter using the link below. I
always like hearing from people that get value from my content.

 Last updated on 04/08/2026

<!-- p.428 -->

Visualize parameter binding
Article • 05/20/2024

Parameter binding is the process that PowerShell uses to determine which parameter set
is being used and to associate (bind) values to the parameters of a command. These
values can come from the command line and the pipeline.

The parameter binding process starts by binding named and positional command-line
arguments. After binding command-line arguments, PowerShell tries to bind any
pipeline input. There are two ways that values are bound from the pipeline. Parameters
that accept pipeline input have one or both of the following attributes:

      ValueFromPipeline - The value from the pipeline is bound to the parameter based
      on its type. The type of the argument must match the type of the parameter.
      ValueFromPipelineByPropertyName - The value from the pipeline is bound to the
      parameter based on its name. The object in the pipeline must have a property that
      matches the name of the parameter or one of its aliases. The type of the property
      must match or be convertible to the type of the parameter.

For more information about parameter binding, see about_Parameter_Binding.

Use Trace-Command to visualize parameter
binding
Troubleshooting parameter binding issues can be challenging. You can use the Trace-
Command cmdlet to visualize the parameter binding process.

Consider the following scenario. You have a directory with two text files, file1.txt and
[file2].txt .

  PowerShell

  PS> Get-ChildItem

       Directory: D:\temp\test\binding

  Mode                      LastWriteTime         Length Name
  ----                      -------------         ------ ----
  -a---                5/17/2024 12:59 PM              0 [file2].txt
  -a---                5/17/2024 12:59 PM              0 file1.txt

<!-- p.429 -->

You want to delete the files by passing the filenames, through the pipeline, to the
Remove-Item cmdlet.

  PowerShell

  PS> 'file1.txt', '[file2].txt' | Remove-Item
  PS> Get-ChildItem

         Directory: D:\temp\test\binding

  Mode                    LastWriteTime           Length Name
  ----                    -------------           ------ ----
  -a---              5/17/2024 12:59 PM                0 [file2].txt

Notice that Remove-Item only deleted file1.txt and not [file2].txt . The filename
includes square brackets, which is treated as a wildcard expression. Using Trace-
Command , you can see that the filename is being bound to the Path parameter of Remove-
Item .

  PowerShell

  Trace-Command -PSHost -Name ParameterBinding -Expression {
      '[file2].txt' | Remove-Item
  }

The output from Trace-Command can be verbose. Each line of output is prefixed with a
timestamp and trace provider information. For the output of this example, the prefix
information has been removed to make it easier to read.

  Output

  BIND NAMED cmd line args [Remove-Item]
  BIND POSITIONAL cmd line args [Remove-Item]
  BIND cmd line args to DYNAMIC parameters.
      DYNAMIC parameter object:
  [Microsoft.PowerShell.Commands.FileSystemProviderRemoveItemDynamicParameters
  ]
  MANDATORY PARAMETER CHECK on cmdlet [Remove-Item]
  CALLING BeginProcessing
  BIND PIPELINE object to parameters: [Remove-Item]
      PIPELINE object TYPE = [System.String]
      RESTORING pipeline parameter's original values
      Parameter [Path] PIPELINE INPUT ValueFromPipeline NO COERCION
      BIND arg [[file2].txt] to parameter [Path]
          Binding collection parameter Path: argument type [String], parameter
  type [System.String[]],
              collection type Array, element type [System.String], no
  coerceElementType

<!-- p.430 -->

          Creating array with element type [System.String] and 1 elements
          Argument type String is not IList, treating this as scalar
          Adding scalar element of type String to array position 0
          BIND arg [System.String[]] to param [Path] SUCCESSFUL
      Parameter [Credential] PIPELINE INPUT ValueFromPipelineByPropertyName NO
  COERCION
      Parameter [Credential] PIPELINE INPUT ValueFromPipelineByPropertyName NO
  COERCION
      Parameter [Credential] PIPELINE INPUT ValueFromPipelineByPropertyName
  WITH COERCION
      Parameter [Credential] PIPELINE INPUT ValueFromPipelineByPropertyName
  WITH COERCION
  MANDATORY PARAMETER CHECK on cmdlet [Remove-Item]
  CALLING ProcessRecord
  CALLING EndProcessing

Using Get-Help , you can see that the Path parameter of Remove-Item accepts string
objects from the pipeline ByValue or ByPropertyName . LiteralPath accepts string objects
from the pipeline ByPropertyName .

  PowerShell

  PS> Get-Help Remove-Item -Parameter Path, LiteralPath

  -Path <System.String[]>
      Specifies a path of the items being removed. Wildcard characters are
  permitted.

       Required?                      true
       Position?                      0
       Default value                  None
       Accept pipeline input?         True (ByPropertyName, ByValue)
       Accept wildcard characters?    true

  -LiteralPath <System.String[]>
      Specifies a path to one or more locations. The value of LiteralPath is
  used exactly as it's
      typed. No characters are interpreted as wildcards. If the path includes
  escape characters,
      enclose it in single quotation marks. Single quotation marks tell
  PowerShell not to interpret
      any characters as escape sequences.

       Required?                      true
       Position?                      named
       Default value                  None
       Accept pipeline input?         True (ByPropertyName)
       Accept wildcard characters?    false

<!-- p.431 -->

The output of Trace-Command shows that parameter binding starts by binding command-
line parameters followed by the pipeline input. You can see that Remove-Item receives a
string object from the pipeline. That string object is bound to the Path parameter.

  BIND PIPELINE object to parameters: [Remove-Item]
      PIPELINE object TYPE = [System.String]
      RESTORING pipeline parameter's original values
      Parameter [Path] PIPELINE INPUT ValueFromPipeline NO COERCION
      BIND arg [[file2].txt] to parameter [Path]
      ...
          BIND arg [System.String[]] to param [Path] SUCCESSFUL

Since the Path parameter accepts wildcard characters, the square brackets represent a
wildcard expression. However, that expression doesn't match any files in the directory.
You need to use the LiteralPath parameter to specify the exact path to the file.

Get-Command shows that the LiteralPath parameter accepts input from the pipeline

ByPropertyName or ByValue . And, that it has two aliases, PSPath and LP .

  PowerShell

  PS> (Get-Command Remove-Item).Parameters.LiteralPath.Attributes |
  >> Select-Object ValueFrom*, Alias* | Format-List

  ValueFromPipeline               : False
  ValueFromPipelineByPropertyName : True
  ValueFromRemainingArguments     : False

  AliasNames : {PSPath, LP}

In this next example, Get-Item is used to retrieve a FileInfo object. That object has a
property named PSPath.

  PowerShell

  PS> Get-Item *.txt | Select-Object PSPath

  PSPath
  ------
  Microsoft.PowerShell.Core\FileSystem::D:\temp\test\binding\[file2].txt

The FileInfo object is then passed to Remove-Item .

  PowerShell

<!-- p.432 -->

  Trace-Command -PSHost -Name ParameterBinding -Expression {
      Get-Item *.txt | Remove-Item
  }

For the output of this example, the prefix information has been removed and separated
to show parameter binding for both commands.

In this output, you can see that Get-Item binds the positional parameter value *.txt to
the Path parameter.

  Output

  BIND NAMED cmd line args [Get-Item]
  BIND POSITIONAL cmd line args [Get-Item]
      BIND arg [*.txt] to parameter [Path]
          Binding collection parameter Path: argument type [String], parameter
  type [System.String[]],
              collection type Array, element type [System.String], no
  coerceElementType
          Creating array with element type [System.String] and 1 elements
          Argument type String is not IList, treating this as scalar
          Adding scalar element of type String to array position 0
          BIND arg [System.String[]] to param [Path] SUCCESSFUL
  BIND cmd line args to DYNAMIC parameters.
      DYNAMIC parameter object:
  [Microsoft.PowerShell.Commands.FileSystemProviderGetItemDynamicParameters]
  MANDATORY PARAMETER CHECK on cmdlet [Get-Item]

In the trace output for parameter binding, you can see that Remove-Item receives a
FileInfo object from the pipeline. Since a FileInfo object isn't a String object, it can't be
bound to the Path parameter.

The PSPath property of the FileInfo object matches an alias for the LiteralPath
parameter. PSPath is also a String object, so it can be bound to the LiteralPath
parameter without type coercion.

  Output

  BIND NAMED cmd line args [Remove-Item]
  BIND POSITIONAL cmd line args [Remove-Item]
  BIND cmd line args to DYNAMIC parameters.
      DYNAMIC parameter object:
  [Microsoft.PowerShell.Commands.FileSystemProviderRemoveItemDynamicParameters
  ]
  MANDATORY PARAMETER CHECK on cmdlet [Remove-Item]
  CALLING BeginProcessing
  CALLING BeginProcessing
  CALLING ProcessRecord

<!-- p.433 -->

    BIND PIPELINE object to parameters: [Remove-Item]
        PIPELINE object TYPE = [System.IO.FileInfo]
        RESTORING pipeline parameter's original values
        Parameter [Path] PIPELINE INPUT ValueFromPipeline NO COERCION
        BIND arg [D:\temp\test\binding\[file2].txt] to parameter [Path]
            Binding collection parameter Path: argument type [FileInfo],
parameter type [System.String[]],
                collection type Array, element type [System.String], no
coerceElementType
            Creating array with element type [System.String] and 1 elements
            Argument type FileInfo is not IList, treating this as scalar
            BIND arg [D:\temp\test\binding\[file2].txt] to param [Path]
SKIPPED
        Parameter [Credential] PIPELINE INPUT
ValueFromPipelineByPropertyName NO COERCION
        Parameter [Path] PIPELINE INPUT ValueFromPipelineByPropertyName NO
COERCION
        Parameter [Credential] PIPELINE INPUT
ValueFromPipelineByPropertyName NO COERCION
        Parameter [LiteralPath] PIPELINE INPUT
ValueFromPipelineByPropertyName NO COERCION
        BIND arg
[Microsoft.PowerShell.Core\FileSystem::D:\temp\test\binding\[file2].txt] to
parameter [LiteralPath]
            Binding collection parameter LiteralPath: argument type
[String], parameter type [System.String[]],
                collection type Array, element type [System.String], no
coerceElementType
            Creating array with element type [System.String] and 1 elements
            Argument type String is not IList, treating this as scalar
            Adding scalar element of type String to array position 0
            BIND arg [System.String[]] to param [LiteralPath] SUCCESSFUL
        Parameter [Credential] PIPELINE INPUT
ValueFromPipelineByPropertyName WITH COERCION
    MANDATORY PARAMETER CHECK on cmdlet [Remove-Item]
    CALLING ProcessRecord
CALLING EndProcessing
CALLING EndProcessing

<!-- p.434 -->

Writing Progress across multiple threads
with ForEach-Object -Parallel
Starting in PowerShell 7.0, the ability to work in multiple threads simultaneously is possible
using the Parallel parameter in the ForEach-Object cmdlet. Monitoring the progress of these
threads can be a challenge though. Normally, you can monitor the progress of a process using
Write-Progress. However, since PowerShell uses a separate runspace for each thread when
using Parallel, reporting the progress back to the host isn't as straight forward as normal use of
Write-Progress .

Using a synced hashtable to track progress
When writing the progress from multiple threads, tracking becomes difficult because when
running parallel processes in PowerShell, each process has it's own runspace. To get around
this, you can use a synchronized hashtable. A synced hashtable is a thread safe data structure
that can be modified by multiple threads simultaneously without throwing an error.

Set up
One of the downsides to this approach is it takes a, somewhat, complex set up to ensure
everything runs without error.

 PowerShell

 $dataset = @(
     @{
         Id    = 1
         Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
     }
     @{
         Id    = 2
         Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
     }
     @{
         Id    = 3
         Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
     }
     @{
         Id    = 4
         Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
     }
     @{

<!-- p.435 -->

            Id   = 5
            Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
      }
 )

 # Create a hashtable for process.
 # Keys should be ID's of the processes
 $origin = @{}
 $dataset | ForEach-Object {$origin.($_.Id) = @{}}

 # Create synced hashtable
 $sync = [System.Collections.Hashtable]::Synchronized($origin)

This section creates three different data structures, for three different purposes.

The $dataSet variable stores an array of hashtables that is used to coordinate the next steps
without the risk of being modified. If an object collection is modified while iterating through
the collection, PowerShell throws an error. You must keep the object collection in the loop
separate from the objects being modified. The Id key in each hashtable is the identifier for a
mock process. The Wait key simulates the workload of each mock process being tracked.

The $origin variable stores a nested hashtable with each key being one of the mock process
id's. Then, it is used to hydrate the synchronized hashtable stored in the $sync variable. The
$sync variable is responsible for reporting the progress back to the parent runspace, which

displays the progress.

Running the processes
This section runs the multi-threaded processes and creates some of the output used to display
progress.

 PowerShell

 $job = $dataset | ForEach-Object -ThrottleLimit 3 -AsJob -Parallel {
     $syncCopy = $Using:sync
     $process = $syncCopy.$($PSItem.Id)

      $process.Id = $PSItem.Id
      $process.Activity = "Id $($PSItem.Id) starting"
      $process.Status = "Processing"

      # Fake workload start up that takes x amount of time to complete
      Start-Sleep -Milliseconds ($PSItem.Wait*5)

      # Process. update activity
      $process.Activity = "Id $($PSItem.Id) processing"
      foreach ($percent in 1..100)
      {

<!-- p.436 -->

           # Update process on status
           $process.Status = "Handling $percent/100"
           $process.PercentComplete = (($percent / 100) * 100)

           # Fake workload that takes x amount of time to complete
           Start-Sleep -Milliseconds $PSItem.Wait
      }

      # Mark process as completed
      $process.Completed = $true
 }

The mock processes are sent to ForEach-Object and started as jobs. The ThrottleLimit is set to
3 to highlight running multiple processes in a queue. The jobs are stored in the $job variable
and allows us to know when all the processes have finished later on.

When using the Using: statement to reference a parent scope variable in PowerShell, you can't
use expressions to make it dynamic. For example, if you tried to create the $process variable
like this, $process = $Using:sync.$($PSItem.Id) , you would get an error stating you can't use
expressions there. So, we create the $syncCopy variable to be able to reference and modify the
$sync variable without the risk of it failing.

Next, we build out a hashtable to represent the progress of the process currently in the loop
using the $process variable by referencing the synchronized hashtable keys. The Activity and
the Status keys are used as parameter values for Write-Progress to display the status of a
given mock process in the next section.

The foreach loop is just a way to simulate the process working and is randomized based on
the $dataSet Wait attribute to set Start-Sleep using milliseconds. How you calculate the
progress of your process may vary.

Displaying the progress of multiple processes
Now that the mock processes are running as jobs, we can start to write the processes progress
to the PowerShell window.

 PowerShell

 while($job.State -eq 'Running')
 {
     $sync.Keys | ForEach-Object {
         # If key is not defined, ignore
         if(![string]::IsNullOrEmpty($sync.$_.Keys))
         {
             # Create parameter hashtable to splat

<!-- p.437 -->

               $param = $sync.$_

               # Execute Write-Progress
               Write-Progress @param
           }
      }

      # Wait to refresh to not overload gui
      Start-Sleep -Seconds 0.1
  }

The $job variable contains the parent job and has a child job for each of the mock processes.
While any of the child jobs are still running, the parent job State will remain "Running". This
allows us to use the while loop to continually update the progress of every process until all
processes are finished.

Within the while loop, we loop through each of the keys in the $sync variable. Since this is a
synchronized hashtable, it is constantly updated but can still be accessed without throwing any
errors.

There is a check to ensure that the process being reported is actually running using the
IsNullOrEmpty() method. If the process hasn't been started, the loop won't report on it and

move on to the next until it gets to a process that has been started. If the process is started, the
hashtable from the current key is used to splat the parameters to Write-Progress .

Full example

  PowerShell

  # Example workload
  $dataset = @(
      @{
          Id    = 1
          Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
      }
      @{
          Id    = 2
          Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
      }
      @{
          Id    = 3
          Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
      }
      @{
          Id    = 4
          Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
      }
      @{

<!-- p.438 -->

        Id   = 5
        Wait = 3..10 | Get-Random | ForEach-Object {$_*100}
    }
)

# Create a hashtable for process.
# Keys should be ID's of the processes
$origin = @{}
$dataset | ForEach-Object {$origin.($_.Id) = @{}}

# Create synced hashtable
$sync = [System.Collections.Hashtable]::Synchronized($origin)

$job = $dataset | ForEach-Object -ThrottleLimit 3 -AsJob -Parallel {
    $syncCopy = $Using:sync
    $process = $syncCopy.$($PSItem.Id)

    $process.Id = $PSItem.Id
    $process.Activity = "Id $($PSItem.Id) starting"
    $process.Status = "Processing"

    # Fake workload start up that takes x amount of time to complete
    Start-Sleep -Milliseconds ($PSItem.Wait*5)

    # Process. update activity
    $process.Activity = "Id $($PSItem.Id) processing"
    foreach ($percent in 1..100)
    {
        # Update process on status
        $process.Status = "Handling $percent/100"
        $process.PercentComplete = (($percent / 100) * 100)

        # Fake workload that takes x amount of time to complete
        Start-Sleep -Milliseconds $PSItem.Wait
    }

    # Mark process as completed
    $process.Completed = $true
}

while($job.State -eq 'Running')
{
    $sync.Keys | ForEach-Object {
        # If key is not defined, ignore
        if(![string]::IsNullOrEmpty($sync.$_.Keys))
        {
            # Create parameter hashtable to splat
            $param = $sync.$_

            # Execute Write-Progress
            Write-Progress @param
        }
    }

    # Wait to refresh to not overload gui

<!-- p.439 -->

      Start-Sleep -Seconds 0.1
 }

Related Links
     about_Jobs
     about_Scopes
     about_Splatting

Last updated on 03/24/2025

<!-- p.440 -->

Add Credential support to PowerShell
functions

  ７ Note

  The original version    of this article appeared on the blog written by @joshduffney      .
  This article has been edited for inclusion on this site. The PowerShell team thanks Josh for
  sharing this content with us. Please check out his blog at duffney.io .

This article shows you how to add credential parameters to PowerShell functions and why
you'd want to. A credential parameter is to allow you to run the function or cmdlet as a
different user. The most common use is to run the function or cmdlet as an elevated user
account.

For example, the cmdlet New-ADUser has a Credential parameter, which you could provide
domain admin credentials to create an account in a domain. Assuming your normal account
running the PowerShell session doesn't have that access already.

Creating credential object
The PSCredential object represents a set of security credentials such as a user name and
password. The object can be passed as a parameter to a function that runs as the user account
in that credential object. There are a few ways that you can create a credential object. The first
way to create a credential object is to use the PowerShell cmdlet Get-Credential . When you
run without parameters, it prompts you for a username and password. Or you can call the
cmdlet with some optional parameters.

To specify the domain name and username ahead of time you can use either the Credential or
UserName parameters. When you use the UserName parameter, you're also required to
provide a Message value. The code below demonstrates using the cmdlet. You can also store
the credential object in a variable so that you can use the credential multiple times. In the
example below, the credential object is stored in the variable $Cred .

 PowerShell

 $Cred = Get-Credential
 $Cred = Get-Credential -Credential domain\user
