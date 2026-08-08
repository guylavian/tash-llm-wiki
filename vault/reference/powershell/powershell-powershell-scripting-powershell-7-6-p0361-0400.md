---
title: "How to use this documentation — pages 361-400"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0361-0400
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0361-0400
family: powershell
documentKind: "doc"
abstract: "They can be hard to read and that make you more prone to make mistakes. There are a few things we can do about that. Line continuation There some operators in PowerShell that let you wrap you command to the next line. The logical operators -and and -or are good operators to use"
---

# How to use this documentation — pages 361-400

<!-- p.361 -->

They can be hard to read and that make you more prone to make mistakes. There are a few
things we can do about that.

Line continuation
There some operators in PowerShell that let you wrap you command to the next line. The
logical operators -and and -or are good operators to use if you want to break your expression
into multiple lines.

 PowerShell

 if ($null -ne $user -and
     $user.Department -eq 'Finance' -and
     $user.Title -match 'Senior' -and
     $user.HomeDrive -notlike '\\server\*'
 )
 {
     # Do Something
 }

There's still a lot going on there, but placing each piece on its own line makes a big difference.
I generally use this when I get more than two comparisons or if I have to scroll to the right to
read any of the logic.

Pre-calculating results
We can take that statement out of the if statement and only check the result.

 PowerShell
 $needsSecureHomeDrive = $null -ne $user -and
     $user.Department -eq 'Finance' -and
     $user.Title -match 'Senior' -and
     $user.HomeDrive -notlike '\\server\*'

 if ( $needsSecureHomeDrive )
 {
     # Do Something
 }

This just feels much cleaner than the previous example. You also are given an opportunity to
use a variable name that explains what it's that you're really checking. This is also and example
of self-documenting code that saves unnecessary comments.

Multiple if statements

<!-- p.362 -->

We can break this up into multiple statements and check them one at a time. In this case, we
use a flag or a tracking variable to combine the results.

 PowerShell

 $skipUser = $false

 if( $null -eq $user )
 {
     $skipUser = $true
 }

 if( $user.Department -ne 'Finance' )
 {
     Write-Verbose "isn't in Finance department"
     $skipUser = $true
 }

 if( $user.Title -match 'Senior' )
 {
     Write-Verbose "Doesn't have Senior title"
     $skipUser = $true
 }

 if( $user.HomeDrive -like '\\server\*' )
 {
     Write-Verbose "Home drive already configured"
     $skipUser = $true
 }

 if ( -not $skipUser )
 {
     # do something
 }

I did have to invert the logic to make the flag logic work correctly. Each evaluation is an
individual if statement. The advantage of this is that when you're debugging, you can tell
exactly what the logic is doing. I was able to add much better verbosity at the same time.

The obvious downside is that it's so much more code to write. The code is more complex to
look at as it takes a single line of logic and explodes it into 25 or more lines.

Using functions
We can also move all that validation logic into a function. Look at how clean this looks at a
glance.

 PowerShell

<!-- p.363 -->

 if ( Test-SecureDriveConfiguration -ADUser $user )
 {
     # do something
 }

You still have to create the function to do the validation, but it makes this code much easier to
work with. It makes this code easier to test. In your tests, you can mock the call to Test-
ADDriveConfiguration and you only need two tests for this function. One where it returns $true

and one where it returns $false . Testing the other function is simpler because it's so small.

The body of that function could still be that one-liner we started with or the exploded logic
that we used in the last section. This works well for both scenarios and allows you to easily
change that implementation later.

Error handling
One important use of the if statement is to check for error conditions before you run into
errors. A good example is to check if a folder already exists before you try to create it.

 PowerShell

 if ( -not (Test-Path -Path $folder) )
 {
     New-Item -Type Directory -Path $folder
 }

I like to say that if you expect an exception to happen, then it's not really an exception. So
check your values and validate your conditions where you can.

If you want to dive a little more into actual exception handling, I have an article on everything
you ever wanted to know about exceptions.

Final words
The if statement is such a simple statement but is a fundamental piece of PowerShell. You will
find yourself using this multiple times in almost every script you write. I hope you have a better
understanding than you had before.

 Last updated on 01/18/2026

<!-- p.364 -->

Everything you ever wanted to know about
the switch statement
Like many other languages, PowerShell has commands for controlling the flow of execution
within your scripts. One of those statements is the switch statement and in PowerShell, it offers
features that aren't found in other languages. Today, we take a deep dive into working with the
PowerShell switch .

  ７ Note

  The original version      of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com        .

The if statement
One of the first statements that you learn is the if statement. It lets you execute a script block
if a statement is $true .

  PowerShell

  if ( Test-Path $Path )
  {
      Remove-Item $Path
  }

You can have much more complicated logic using elseif and else statements. Here is an
example where I have a numeric value for day of the week and I want to get the name as a
string.

  PowerShell

  $day = 3

  if ( $day -eq 0 ) { $result = 'Sunday'        }
  elseif ( $day -eq 1 ) { $result = 'Monday'    }
  elseif ( $day -eq 2 ) { $result = 'Tuesday'   }
  elseif ( $day -eq 3 ) { $result = 'Wednesday' }
  elseif ( $day -eq 4 ) { $result = 'Thursday' }
  elseif ( $day -eq 5 ) { $result = 'Friday'    }

<!-- p.365 -->

 elseif ( $day -eq 6 ) { $result = 'Saturday'        }

 $result

 Output

 Wednesday

It turns out that this is a common pattern and there are many ways to deal with this. One of
them is with a switch .

Switch statement
The switch statement allows you to provide a variable and a list of possible values. If the value
matches the variable, then its statement block is executed.

 PowerShell

 $day = 3

 switch ( $day )
 {
     0 { $result = 'Sunday'    }
     1 { $result = 'Monday'    }
     2 { $result = 'Tuesday'   }
     3 { $result = 'Wednesday' }
     4 { $result = 'Thursday' }
     5 { $result = 'Friday'    }
     6 { $result = 'Saturday' }
 }

 $result

 Output

 'Wednesday'

For this example, the value of $day matches one of the numeric values, then the correct name
is assigned to $result . We're only doing a variable assignment in this example, but any
PowerShell can be executed in those script blocks.

Assign to a variable
We can write that last example in another way.

<!-- p.366 -->

 PowerShell

 $result = switch ( $day )
 {
     0 { 'Sunday'    }
     1 { 'Monday'    }
     2 { 'Tuesday'   }
     3 { 'Wednesday' }
     4 { 'Thursday' }
     5 { 'Friday'    }
     6 { 'Saturday' }
 }

We're placing the value on the PowerShell pipeline and assigning it to the $result . You can do
this same thing with the if and foreach statements.

Default
We can use the default keyword to identify the what should happen if there is no match.

 PowerShell

 $result = switch ( $day )
 {
     0 { 'Sunday' }
     # ...
     6 { 'Saturday' }
     default { 'Unknown' }
 }

Here we return the value Unknown in the default case.

Strings
I was matching numbers in those last examples, but you can also match strings.

 PowerShell

 $item = 'Role'

 switch ( $item )
 {
     Component
     {
         'is a component'
     }
     Role
     {
         'is a role'

<!-- p.367 -->

      }
      Location
      {
          'is a location'
      }
 }

 Output

 is a role

I decided not to wrap the Component , Role and Location matches in quotes here to highlight
that they're optional. The switch treats those as a string in most cases.

Arrays
One of the cool features of the PowerShell switch is the way it handles arrays. If you give a
switch an array, it processes each element in that collection.

 PowerShell

 $roles = @('WEB','Database')

 switch ( $roles ) {
     'Database'   { 'Configure SQL' }
     'WEB'        { 'Configure IIS' }
     'FileServer' { 'Configure Share' }
 }

 Output

 Configure IIS
 Configure SQL

If you have repeated items in your array, then they're matched multiple times by the
appropriate section.

PSItem
You can use the $PSItem or $_ to reference the current item that was processed. When we do
a simple match, $PSItem is the value that we're matching. I'll be performing some advanced
matches in the next section where this variable is used.

Parameters

<!-- p.368 -->

A unique feature of the PowerShell switch is that it has a number of [switch] parameters that
change how it performs.

-CaseSensitive
The matches aren't case-sensitive by default. If you need to be case-sensitive, you can use -
CaseSensitive . This can be used in combination with the other [switch] parameters.

-Wildcard
We can enable wildcard support with the -Wildcard [switch] parameter. This uses the same
wildcard logic as the -like operator to do each match.

 PowerShell

 $Message = 'Warning, out of disk space'

 switch -Wildcard ( $message )
 {
     'Error*'
     {
         Write-Error -Message $Message
     }
     'Warning*'
     {
         Write-Warning -Message $Message
     }
     default
     {
         Write-Information $message
     }
 }

 Output

 WARNING: Warning, out of disk space

Here we're processing a message and then outputting it on different streams based on the
contents.

-Regex
The switch statement supports regex matches just like it does wildcards.

 PowerShell

<!-- p.369 -->

 switch -Regex ( $message )
 {
     '^Error'
     {
         Write-Error -Message $Message
     }
     '^Warning'
     {
         Write-Warning -Message $Message
     }
     default
     {
         Write-Information $message
     }
 }

I have more examples of using regex in another article I wrote: The many ways to use regex     .

-File
A little known feature of the switch statement is that it can process a file with the -File
parameter. You use -File with a path to a file instead of giving it a variable expression.

 PowerShell

 switch -Wildcard -File $path
 {
     'Error*'
     {
         Write-Error -Message $PSItem
     }
     'Warning*'
     {
         Write-Warning -Message $PSItem
     }
     default
     {
         Write-Output $PSItem
     }
 }

It works just like processing an array. In this example, I combine it with wildcard matching and
make use of the $PSItem . This would process a log file and convert it to warning and error
messages depending on the regex matches.

Advanced details

<!-- p.370 -->

Now that you're aware of all these documented features, we can use them in the context of
more advanced processing.

Expressions
The switch can be on an expression instead of a variable.

 PowerShell

 switch ( ( Get-Service | where Status -EQ 'running' ).Name ) {...}

Whatever the expression evaluates to is the value used for the match.

Multiple matches
You may have already picked up on this, but a switch can match to multiple conditions. This is
especially true when using -Wildcard or -Regex matches. You can add the same condition
multiple times and all are triggered.

 PowerShell

 switch ( 'Word' )
 {
     'word' { 'lower case word match' }
     'Word' { 'mixed case word match' }
     'WORD' { 'upper case word match' }
 }

 Output

 lower case word match
 mixed case word match
 upper case word match

All three of these statements are fired. This shows that every condition is checked (in order).
This holds true for processing arrays where each item checks each condition.

Continue
Normally, this is where I would introduce the break statement, but it's better that we learn how
to use continue first. Just like with a foreach loop, continue continues onto the next item in
the collection or exits the switch if there are no more items. We can rewrite that last example
with continue statements so that only one statement executes.

<!-- p.371 -->

 PowerShell

 switch ( 'Word' )
 {
     'word'
     {
         'lower case word match'
         continue
     }
     'Word'
     {
         'mixed case word match'
         continue
     }
     'WORD'
     {
         'upper case word match'
         continue
     }
 }

 Output

 lower case word match

Instead of matching all three items, the first one is matched and the switch continues to the
next value. Because there are no values left to process, the switch exits. This next example is
showing how a wildcard could match multiple items.

 PowerShell

 switch -Wildcard -File $path
 {
     '*Error*'
     {
         Write-Error -Message $PSItem
         continue
     }
     '*Warning*'
     {
         Write-Warning -Message $PSItem
         continue
     }
     default
     {
         Write-Output $PSItem
     }
 }

<!-- p.372 -->

Because a line in the input file could contain both the word Error and Warning , we only want
the first one to execute and then continue processing the file.

Break
A break statement exits the switch. This is the same behavior that continue presents for single
values. The difference is shown when processing an array. break stops all processing in the
switch and continue moves onto the next item.

 PowerShell

 $Messages = @(
     'Downloading update'
     'Ran into errors downloading file'
     'Error: out of disk space'
     'Sending email'
     '...'
 )

 switch -Wildcard ($Messages)
 {
     'Error*'
     {
         Write-Error -Message $PSItem
         break
     }
     '*Error*'
     {
         Write-Warning -Message $PSItem
         continue
     }
     '*Warning*'
     {
         Write-Warning -Message $PSItem
         continue
     }
     default
     {
         Write-Output $PSItem
     }
 }

 Output

 Downloading update
 WARNING: Ran into errors downloading file
 Write-Error -Message $PSItem : Error: out of disk space
 + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
 + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException

<!-- p.373 -->

In this case, if we hit any lines that start with Error then we get an error and the switch stops.
This is what that break statement is doing for us. If we find Error inside the string and not just
at the beginning, we write it as a warning. We do the same thing for Warning . It's possible that
a line could have both the word Error and Warning , but we only need one to process. This is
what the continue statement is doing for us.

Break labels
The switch statement supports break/continue labels just like foreach .

 PowerShell

 :filelist foreach($path in $logs)
 {
     :logFile switch -Wildcard -File $path
     {
         'Error*'
         {
             Write-Error -Message $PSItem
             break filelist
         }
         'Warning*'
         {
             Write-Error -Message $PSItem
             break logFile
         }
         default
         {
             Write-Output $PSItem
         }
     }
 }

I personally don't like the use of break labels but I wanted to point them out because they're
confusing if you've never seen them before. When you have multiple switch or foreach
statements that are nested, you may want to break out of more than the inner most item. You
can place a label on a switch that can be the target of your break .

Enum
PowerShell 5.0 gave us enums and we can use them in a switch.

 PowerShell

 enum Context {
     Component

<!-- p.374 -->

      Role
      Location
 }

 $item = [Context]::Role

 switch ( $item )
 {
     Component
     {
         'is a component'
     }
     Role
     {
         'is a role'
     }
     Location
     {
         'is a location'
     }
 }

 Output

 is a role

If you want to keep everything as strongly typed enums, then you can place them in
parentheses.

 PowerShell

 switch ($item )
 {
     ([Context]::Component)
     {
         'is a component'
     }
     ([Context]::Role)
     {
         'is a role'
     }
     ([Context]::Location)
     {
         'is a location'
     }
 }

The parentheses are needed here so that the switch doesn't treat the value
[Context]::Location as a literal string.

<!-- p.375 -->

ScriptBlock
We can use a scriptblock to perform the evaluation for a match if needed.

 PowerShell

 $age = 37

 switch ( $age )
 {
     {$PSItem -le 18}
     {
         'child'
     }
     {$PSItem -gt 18}
     {
         'adult'
     }
 }

 Output

 'adult'

This adds complexity and can make your switch hard to read. In most cases where you would
use something like this it would be better to use if and elseif statements. I would consider
using this if I already had a large switch in place and I needed two items to hit the same
evaluation block.

One thing that I think helps with legibility is to place the scriptblock in parentheses.

 PowerShell

 switch ( $age )
 {
     ({$PSItem -le 18})
     {
         'child'
     }
     ({$PSItem -gt 18})
     {
         'adult'
     }
 }

It still executes the same way and gives a better visual break when quickly looking at it.

<!-- p.376 -->

Regex $Matches
We need to revisit regex to touch on something that isn't immediately obvious. The use of
regex populates the $Matches variable. I do go into the use of $Matches more when I talk
about The many ways to use regex    . Here is a quick sample to show it in action with named
matches.

 PowerShell

 $message = 'my ssn is 123-23-3456 and credit card: 1234-5678-1234-5678'

 switch -Regex ($message)
 {
     '(?<SSN>\d\d\d-\d\d-\d\d\d\d)'
     {
         Write-Warning "message contains a SSN: $($Matches.SSN)"
     }
     '(?<CC>\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d)'
     {
         Write-Warning "message contains a credit card number: $($Matches.CC)"
     }
     '(?<Phone>\d\d\d-\d\d\d-\d\d\d\d)'
     {
         Write-Warning "message contains a phone number: $($Matches.Phone)"
     }
 }

 Output

 WARNING: message may contain a SSN: 123-23-3456
 WARNING: message may contain a credit card number: 1234-5678-1234-5678

$null
You can match a $null value that doesn't have to be the default.

 PowerShell

 $values = '', 5, $null
 switch ( $values )
 {
     $null          { "Value '$_' is `$null" }
     { '' -eq $_ } { "Value '$_' is an empty string" }
     default        { "Value [$_] isn't an empty string or `$null" }
 }

<!-- p.377 -->

 Output

 Value '' is an empty string
 Value [5] isn't an empty string or $null
 Value '' is $null

When testing for an empty string in a switch statement, it's important to use the comparison
statement as shown in this example instead of the raw value '' . In a switch statement, the
raw value '' also matches $null . For example:

 PowerShell

 $values = '', 5, $null
 switch ( $values )
 {
     $null          { "Value '$_' is `$null" }
     ''             { "Value '$_' is an empty string" }
     default        { "Value [$_] isn't an empty string or `$null" }
 }

 Output

 Value '' is an empty string
 Value [5] isn't an empty string or $null
 Value '' is $null
 Value '' is an empty string

Also, be careful with empty returns from cmdlets. Cmdlets or pipelines that have no output are
treated as an empty array that doesn't match anything, including the default case.

 PowerShell

 $file = Get-ChildItem NonExistantFile*
 switch ( $file )
 {
     $null    { '$file is $null' }
     default { "`$file is type $($file.GetType().Name)" }
 }
 # No matches

Constant expression
Lee Dailey pointed out that we can use a constant $true expression to evaluate [bool] items.
Imagine if we have several boolean checks that need to happen.

 PowerShell

<!-- p.378 -->

 $isVisible = $false
 $isEnabled = $true
 $isSecure = $true

 switch ( $true )
 {
     $isEnabled
     {
         'Do-Action'
     }
     $isVisible
     {
         'Show-Animation'
     }
     $isSecure
     {
         'Enable-AdminMenu'
     }
 }

 Output

 Do-Action
 Enabled-AdminMenu

This is a clean way to evaluate and take action on the status of several boolean fields. The cool
thing about this is that you can have one match flip the status of a value that hasn't been
evaluated yet.

 PowerShell

 $isVisible = $false
 $isEnabled = $true
 $isAdmin = $false

 switch ( $true )
 {
     $isEnabled
     {
         'Do-Action'
         $isVisible = $true
     }
     $isVisible
     {
         'Show-Animation'
     }
     $isAdmin
     {
         'Enable-AdminMenu'

<!-- p.379 -->

      }
 }

 Output

 Do-Action
 Show-Animation

Setting $isEnabled to $true in this example makes sure that $isVisible is also set to $true .
Then when $isVisible gets evaluated, its statement block is invoked. This is a bit counter-
intuitive but is a clever use of the mechanics.

$switch automatic variable
When the switch is processing its values, it creates an enumerator and calls it $switch . This is
an automatic variable created by PowerShell and you can manipulate it directly.

 PowerShell

 $a = 1, 2, 3, 4

 switch($a) {
     1 { [void]$switch.MoveNext(); $switch.Current }
     3 { [void]$switch.MoveNext(); $switch.Current }
 }

This gives you the results of:

 Output

 2
 4

By moving the enumerator forward, the next item doesn't get processed by the switch but you
can access that value directly. I would call it madness.

Other patterns
Hashtables
One of my most popular posts is the one I did on hashtables. One of the use cases for a
hashtable is to be a lookup table. That's an alternate approach to a common pattern that a

switch statement is often addressing.

<!-- p.380 -->

 PowerShell

 $day = 3

 $lookup = @{
     0 = 'Sunday'
     1 = 'Monday'
     2 = 'Tuesday'
     3 = 'Wednesday'
     4 = 'Thursday'
     5 = 'Friday'
     6 = 'Saturday'
 }

 $lookup[$day]

 Output

 Wednesday

If I'm only using a switch as a lookup, I often use a hashtable instead.

Enum
PowerShell 5.0 introduced the enum and it's also an option in this case.

 PowerShell

 $day = 3

 enum DayOfTheWeek {
     Sunday
     Monday
     Tuesday
     Wednesday
     Thursday
     Friday
     Saturday
 }

 [DayOfTheWeek]$day

 Output

 Wednesday

We could go all day looking at different ways to solve this problem. I just wanted to make sure
you knew you had options.

<!-- p.381 -->

Final words
The switch statement is simple on the surface but it offers some advanced features that most
people don't realize are available. Stringing those features together makes this a powerful
feature. I hope you learned something that you had not realized before.

 Last updated on 04/08/2026

<!-- p.382 -->

Everything you wanted to know about
exceptions
Error handling is just part of life when it comes to writing code. We can often check and
validate conditions for expected behavior. When the unexpected happens, we turn to
exception handling. You can easily handle exceptions generated by other people's code or you
can generate your own exceptions for others to handle.

  ７ Note

  The original version     of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com         .

Basic terminology
We need to cover some basic terms before we jump into this one.

Exception
An Exception is like an event that is created when normal error handling can't deal with the
issue. Trying to divide a number by zero or running out of memory are examples of something
that creates an exception. Sometimes the author of the code you're using creates exceptions
for certain issues when they happen.

Throw and Catch
When an exception happens, we say that an exception is thrown. To handle a thrown exception,
you need to catch it. If an exception is thrown and it isn't caught by something, the script stops
executing.

The call stack
The call stack is the list of functions that have called each other. When a function is called, it
gets added to the stack or the top of the list. When the function exits or returns, it is removed
from the stack.

<!-- p.383 -->

When an exception is thrown, that call stack is checked in order for an exception handler to
catch it.

Terminating and non-terminating errors
PowerShell has three categories of errors.

      A non-terminating error adds an error to the error stream without stopping execution and
      doesn't trigger catch . By default, Write-Error generates non-terminating errors.
      A statement-terminating error stops the current statement but allows the script to
      continue at the next statement. Statement-terminating errors can be generated by engine
      errors, $PSCmdlet.ThrowTerminatingError() , or .NET method exceptions.
      A script-terminating error unwinds the entire call stack. Script-terminating errors can be
      generated by throw , parse errors, or -ErrorAction Stop escalation.

Both statement-terminating and script-terminating errors can be caught by try/catch . For a
comprehensive reference, see about_Error_Handling.

Swallowing an exception
This is when you catch an error just to suppress it. Do this with caution because it can make
troubleshooting issues very difficult.

Basic command syntax
Here is a quick overview of the basic exception handling syntax used in PowerShell.

Throw
To create our own exception event, we throw an exception with the throw keyword.

  PowerShell

  function Start-Something
  {
      throw "Bad thing happened"
  }

This creates a runtime exception that is a script-terminating error. It's handled by a catch in a
calling function or exits the script with a message like this.

<!-- p.384 -->

 PowerShell

 PS> Start-Something

 Bad thing happened
 At line:1 char:1
 + throw "Bad thing happened"
 + ~~~~~~~~~~~~~~~~~~~~~~~~~~
     + CategoryInfo           : OperationStopped: (Bad thing happened:String) [],
 RuntimeException
     + FullyQualifiedErrorId : Bad thing happened

Write-Error -ErrorAction Stop

I mentioned that Write-Error doesn't throw a terminating error by default. If you specify -
ErrorAction Stop , Write-Error generates a terminating error that can be handled with a

catch .

 PowerShell

 Write-Error -Message "Houston, we have a problem." -ErrorAction Stop

Thank you to Lee Dailey for reminding about using -ErrorAction Stop this way.

Cmdlet -ErrorAction Stop

If you specify -ErrorAction Stop on any advanced function or cmdlet, it turns all Write-Error
statements into terminating errors that stop execution or that can be handled by a catch .

 PowerShell

 Start-Something -ErrorAction Stop

For more information about the ErrorAction parameter, see about_CommonParameters. For
more information about the $ErrorActionPreference variable, see about_Preference_Variables.

Try/Catch
The way exception handling works in PowerShell (and many other languages) is that you first
try a section of code and if it throws an error, you can catch it. Here is a quick sample.

 PowerShell

 try
 {

<!-- p.385 -->

     Start-Something
 }
 catch
 {
     Write-Output "Something threw an exception"
     Write-Output $_
 }

 try
 {
     Start-Something -ErrorAction Stop
 }
 catch
 {
     Write-Output "Something threw an exception or used Write-Error"
     Write-Output $_
 }

The catch script only runs if there's a terminating error. If the try executes correctly, then it
skips over the catch . You can access the exception information in the catch block using the
$_ variable.

Try/Finally
Sometimes you don't need to handle an error but still need some code to execute if an
exception happens or not. A finally script does exactly that.

Take a look at this example:

 PowerShell

 $command = [System.Data.SqlClient.SqlCommand]::new(queryString, connection)
 $command.Connection.Open()
 $command.ExecuteNonQuery()
 $command.Connection.Close()

Anytime you open or connect to a resource, you should close it. If the ExecuteNonQuery()
throws an exception, the connection isn't closed. Here is the same code inside a try/finally
block.

 PowerShell

 $command = [System.Data.SqlClient.SqlCommand]::new(queryString, connection)
 try
 {
     $command.Connection.Open()
     $command.ExecuteNonQuery()
 }

<!-- p.386 -->

  finally
  {
      $command.Connection.Close()
  }

In this example, the connection is closed if there's an error. It also is closed if there's no error.
The finally script runs every time.

Because you're not catching the exception, it still gets propagated up the call stack.

Try/Catch/Finally
It's perfectly valid to use catch and finally together. Most of the time you'll use one or the
other, but you may find scenarios where you use both.

$PSItem
Now that we got the basics out of the way, we can dig a little deeper.

Inside the catch block, there's an automatic variable ( $PSItem or $_ ) of type ErrorRecord that
contains the details about the exception. Here is a quick overview of some of the key
properties.

For these examples, I used an invalid path in ReadAllText to generate this exception.

  PowerShell

  [System.IO.File]::ReadAllText( '\\test\no\filefound.log')

PSItem.ToString()
This gives you the cleanest message to use in logging and general output. ToString() is
automatically called if $PSItem is placed inside a string.

  PowerShell

  catch
  {
      Write-Output "Ran into an issue: $($PSItem.ToString())"
  }

  catch
  {

<!-- p.387 -->

      Write-Output "Ran into an issue: $PSItem"
  }

$PSItem.InvocationInfo
This property contains additional information collected by PowerShell about the function or
script where the exception was thrown. Here is the InvocationInfo from the sample exception
that I created.

  PowerShell

  PS> $PSItem.InvocationInfo | Format-List *

  MyCommand                : Get-Resource
  BoundParameters          : {}
  UnboundArguments         : {}
  ScriptLineNumber         : 5
  OffsetInLine             : 5
  ScriptName               : C:\blog\throwerror.ps1
  Line                     :     Get-Resource
  PositionMessage          : At C:\blog\throwerror.ps1:5 char:5
                             +     Get-Resource
                             +     ~~~~~~~~~~~~
  PSScriptRoot             : C:\blog
  PSCommandPath            : C:\blog\throwerror.ps1
  InvocationName           : Get-Resource

The important details here show the ScriptName , the Line of code and the ScriptLineNumber
where the invocation started.

$PSItem.ScriptStackTrace
This property shows the order of function calls that got you to the code where the exception
was generated.

  PowerShell

  PS> $PSItem.ScriptStackTrace
  at Get-Resource, C:\blog\throwerror.ps1: line 13
  at Start-Something, C:\blog\throwerror.ps1: line 5
  at <ScriptBlock>, C:\blog\throwerror.ps1: line 18

I'm only making calls to functions in the same script but this would track the calls if multiple
scripts were involved.

<!-- p.388 -->

$PSItem.Exception
This is the actual exception that was thrown.

$PSItem.Exception.Message

This is the general message that describes the exception and is a good starting point when
troubleshooting. Most exceptions have a default message but can also be set to something
custom when the exception is thrown.

 PowerShell

 PS> $PSItem.Exception.Message

 Exception calling "ReadAllText" with "1" argument(s): "The network path was not
 found."

This is also the message returned when calling $PSItem.ToString() if there was not one set on
the ErrorRecord .

$PSItem.Exception.InnerException

Exceptions can contain inner exceptions. This is often the case when the code you're calling
catches an exception and throws a different exception. The original exception is placed inside
the new exception.

 PowerShell

 PS> $PSItem.Exception.InnerExceptionMessage
 The network path was not found.

I will revisit this later when I talk about re-throwing exceptions.

$PSItem.Exception.StackTrace

This is the StackTrace for the exception. I showed a ScriptStackTrace above, but this one is for
the calls to managed code.

 Output

 at System.IO.FileStream.Init(String path, FileMode mode, FileAccess access, Int32
 rights, Boolean
  useRights, FileShare share, Int32 bufferSize, FileOptions options,
 SECURITY_ATTRIBUTES secAttrs,

<!-- p.389 -->

  String msgPath, Boolean bFromProxy, Boolean useLongPath, Boolean checkHost)
 at System.IO.FileStream..ctor(String path, FileMode mode, FileAccess access,
 FileShare share, Int32
  bufferSize, FileOptions options, String msgPath, Boolean bFromProxy, Boolean
 useLongPath, Boolean
  checkHost)
 at System.IO.StreamReader..ctor(String path, Encoding encoding, Boolean
 detectEncodingFromByteOrderMarks,
  Int32 bufferSize, Boolean checkHost)
 at System.IO.File.InternalReadAllText(String path, Encoding encoding, Boolean
 checkHost)
 at CallSite.Target(Closure , CallSite , Type , String )

You only get this stack trace when the event is thrown from managed code. I'm calling a .NET
Framework function directly so that is all we can see in this example. Generally when you're
looking at a stack trace, you're looking for where your code stops and the system calls begin.

Working with exceptions
There is more to exceptions than the basic syntax and exception properties.

Catching typed exceptions
You can be selective with the exceptions that you catch. Exceptions have a type and you can
specify the type of exception you want to catch.

 PowerShell

 try
 {
       Start-Something -Path $path
 }
 catch [System.IO.FileNotFoundException]
 {
     Write-Output "Could not find $path"
 }
 catch [System.IO.IOException]
 {
         Write-Output "IO error with the file: $path"
 }

The exception type is checked for each catch block until one is found that matches your
exception. It's important to realize that exceptions can inherit from other exceptions. In the
example above, FileNotFoundException inherits from IOException . So if the IOException was
first, then it would get called instead. Only one catch block is invoked even if there are multiple
matches.

<!-- p.390 -->

If we had a System.IO.PathTooLongException , the IOException would match but if we had an
InsufficientMemoryException then nothing would catch it and it would propagate up the stack.

Catch multiple types at once
It's possible to catch multiple exception types with the same catch statement.

 PowerShell

 try
 {
     Start-Something -Path $path -ErrorAction Stop
 }
 catch [System.IO.DirectoryNotFoundException],[System.IO.FileNotFoundException]
 {
     Write-Output "The path or file was not found: [$path]"
 }
 catch [System.IO.IOException]
 {
     Write-Output "IO error with the file: [$path]"
 }

Thank you Redditor u/Sheppard_Ra for suggesting this addition.

Throwing typed exceptions
You can throw typed exceptions in PowerShell. Instead of calling throw with a string:

 PowerShell

 throw "Could not find: $path"

Use an exception accelerator like this:

 PowerShell

 throw [System.IO.FileNotFoundException] "Could not find: $path"

But you have to specify a message when you do it that way.

You can also create a new instance of an exception to be thrown. The message is optional
when you do this because the system has default messages for all built-in exceptions.

 PowerShell

<!-- p.391 -->

 throw [System.IO.FileNotFoundException]::new()
 throw [System.IO.FileNotFoundException]::new("Could not find path: $path")

If you're not using PowerShell 5.0 or higher, you must use the older New-Object approach.

 PowerShell

 throw (New-Object -TypeName System.IO.FileNotFoundException )
 throw (New-Object -TypeName System.IO.FileNotFoundException -ArgumentList "Could
 not find path: $path")

By using a typed exception, you (or others) can catch the exception by the type as mentioned
in the previous section.

Write-Error -Exception

We can add these typed exceptions to Write-Error and we can still catch the errors by
exception type. Use Write-Error like in these examples:

 PowerShell

 # with normal message
 Write-Error -Message "Could not find path: $path" -Exception
 ([System.IO.FileNotFoundException]::new()) -ErrorAction Stop

 # With message inside new exception
 Write-Error -Exception ([System.IO.FileNotFoundException]::new("Could not find
 path: $path")) -ErrorAction Stop

 # Pre PS 5.0
 Write-Error -Exception ([System.IO.FileNotFoundException]"Could not find path:
 $path") -ErrorAction Stop

 Write-Error -Message "Could not find path: $path" -Exception (New-Object -TypeName
 System.IO.FileNotFoundException) -ErrorAction Stop

Then we can catch it like this:

 PowerShell

 catch [System.IO.FileNotFoundException]
 {
     Write-Log $PSItem.ToString()
 }

The big list of .NET exceptions

<!-- p.392 -->

I compiled a master list with the help of the Reddit r/PowerShell community that contains
hundreds of .NET exceptions to complement this post.

     The big list of .NET exceptions

I start by searching that list for exceptions that feel like they would be a good fit for my
situation. You should try to use exceptions in the base System namespace.

Exceptions are objects
If you start using a lot of typed exceptions, remember that they are objects. Different
exceptions have different constructors and properties. If we look at the FileNotFoundException
documentation for System.IO.FileNotFoundException , we see that we can pass in a message
and a file path.

 PowerShell

 [System.IO.FileNotFoundException]::new("Could not find file", $path)

And it has a FileName property that exposes that file path.

 PowerShell

 catch [System.IO.FileNotFoundException]
 {
     Write-Output $PSItem.Exception.FileName
 }

You should consult the .NET documentation for other constructors and object properties.

Re-throwing an exception
If all you're going to do in your catch block is throw the same exception, then don't catch it.
You should only catch an exception that you plan to handle or perform some action when it
happens.

There are times where you want to perform an action on an exception but re-throw the
exception so something downstream can deal with it. We could write a message or log the
problem close to where we discover it but handle the issue further up the stack.

 PowerShell

<!-- p.393 -->

 catch
 {
     Write-Log $PSItem.ToString()
     throw $PSItem
 }

Interestingly enough, we can call throw from within the catch and it re-throws the current
exception.

 PowerShell

 catch
 {
     Write-Log $PSItem.ToString()
     throw
 }

We want to re-throw the exception to preserve the original execution information like source
script and line number. If we throw a new exception at this point, it hides where the exception
started.

Re-throwing a new exception

If you catch an exception but you want to throw a different one, then you should nest the
original exception inside the new one. This allows someone down the stack to access it as the
$PSItem.Exception.InnerException .

 PowerShell

 catch
 {
     throw [System.MissingFieldException]::new('Could not access
 field',$PSItem.Exception)
 }

$PSCmdlet.ThrowTerminatingError()

The one thing that I don't like about using throw for raw exceptions is that the error message
points at the throw statement and indicates that line is where the problem is.

 Output

 Unable to find the specified file.
 At line:31 char:9
 +         throw [System.IO.FileNotFoundException]::new()

<!-- p.394 -->

 +          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      + CategoryInfo          : OperationStopped: (:) [], FileNotFoundException
      + FullyQualifiedErrorId : Unable to find the specified file.

Having the error message tell me that my script is broken because I called throw on line 31 is a
bad message for users of your script to see. It doesn't tell them anything useful.

Dexter Dhami pointed out that I can use ThrowTerminatingError() to correct that.

 PowerShell

 $PSCmdlet.ThrowTerminatingError(
     [System.Management.Automation.ErrorRecord]::new(
         ([System.IO.FileNotFoundException]"Could not find $Path"),
         'My.ID',
         [System.Management.Automation.ErrorCategory]::OpenError,
         $MyObject
     )
 )

If we assume that ThrowTerminatingError() was called inside a function called Get-Resource ,
then this is the error that we would see.

 Output

 Get-Resource : Could not find C:\Program Files (x86)\Reference
 Assemblies\Microsoft\Framework\.NETPortable\v4.6\System.IO.xml
 At line:6 char:5
 +     Get-Resource -Path $Path
 +     ~~~~~~~~~~~~
     + CategoryInfo          : OpenError: (:) [Get-Resource], FileNotFoundException
     + FullyQualifiedErrorId : My.ID,Get-Resource

Do you see how it points to the Get-Resource function as the source of the problem? That tells
the user something useful.

Because $PSItem is an ErrorRecord , we can also use ThrowTerminatingError this way to re-
throw.

 PowerShell

 catch
 {
     $PSCmdlet.ThrowTerminatingError($PSItem)
 }

<!-- p.395 -->

This changes the source of the error to the Cmdlet and hide the internals of your function from
the users of your Cmdlet.

How try/catch changes error propagation
Inside a try block, PowerShell sets an internal flag that causes all statement-terminating errors
to propagate to the catch block. This is by design, not a corner case. The following example
demonstrates this behavior.

 PowerShell

 function Start-Something { 1/(1-1) }

Outside try/catch , a statement-terminating error from a child scope doesn't stop the parent
scope. Here is a function that generates a divide by zero runtime exception.

Invoke it like this to see the error reported while the script continues.

 PowerShell

 &{ Start-Something; Write-Output "We did it. Send Email" }

But placing that same code inside a try/catch , the error propagates to the catch block.

 PowerShell

 try {
     &{ Start-Something; Write-Output "We did it. Send Email" }
 } catch {
     Write-Output "Notify Admin to fix error and send email"
 }

The error is caught and the subsequent Write-Output inside the script block doesn't run. This is
standard try/catch behavior — all terminating errors within the try block are caught, whether
they originate in the current scope or in a child scope.

$PSCmdlet.ThrowTerminatingError() inside try/catch
$PSCmdlet.ThrowTerminatingError() creates a statement-terminating error within the cmdlet.

After the error leaves the cmdlet, the caller treats it as a non-terminating error by default. The
caller can escalate it back to a terminating error by using -ErrorAction Stop or calling it from
within a try/catch block.

<!-- p.396 -->

Public function templates
One last takeaway I had with my conversation with Kirk Munro was that he places a try/catch
block inside every begin , process and end block in all his advanced functions. In those generic
catch blocks, he has a single line using $PSCmdlet.ThrowTerminatingError($PSItem) to deal with
all exceptions leaving his functions.

 PowerShell

 function Start-Something
 {
     [CmdletBinding()]
     param()

        process
        {
            try {
                ...
            } catch {
                $PSCmdlet.ThrowTerminatingError($PSItem)
            }
        }
 }

Because everything is in a try statement within his functions, everything acts consistently. This
also gives clean errors to the end user that hides the internal code from the generated error.

Trap
I focused on the try/catch aspect of exceptions. But there's one legacy feature I need to
mention before we wrap this up.

A trap is placed in a script or function to catch all exceptions that happen in that scope. When
an exception happens, the code in the trap is executed and then the normal code continues. If
multiple exceptions happen, then the trap is called over and over.

 PowerShell

 trap
 {
        Write-Log $PSItem.ToString()
 }

 throw [System.Exception]::new('first')
 throw [System.Exception]::new('second')
 throw [System.Exception]::new('third')

<!-- p.397 -->

I personally never adopted this approach but I can see the value in admin or controller scripts
that log any and all exceptions, then still continue to execute.

Closing remarks
Adding proper exception handling to your scripts not only make them more stable, but also
makes it easier for you to troubleshoot those exceptions.

I spent a lot of time talking throw because it is a core concept when talking about exception
handling. PowerShell also gave us Write-Error that handles all the situations where you would
use throw . So don't think that you need to be using throw after reading this.

Now that I have taken the time to write about exception handling in this detail, I'm going to
switch over to using Write-Error -Stop to generate errors in my code. I'm also going to take
Kirk's advice and make ThrowTerminatingError my goto exception handler for every function.

 Last updated on 04/02/2026

<!-- p.398 -->

Everything you wanted to know about
$null
The PowerShell $null often appears to be simple but it has a lot of nuances. Let's take a close
look at $null so you know what happens when you unexpectedly run into a $null value.

  ７ Note

  The original version    of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com        .

What is NULL?
You can think of NULL as an unknown or empty value. A variable is NULL until you assign a
value or an object to it. This can be important because there are some commands that require
a value and generate errors if the value is NULL.

PowerShell $null
$null is an automatic variable in PowerShell used to represent NULL. You can assign it to

variables, use it in comparisons and use it as a place holder for NULL in a collection.

PowerShell treats $null as an object with a value of NULL. This is different than what you may
expect if you come from another language.

Examples of $null
Anytime you try to use a variable that you have not initialized, the value is $null . This is one of
the most common ways that $null values sneak into your code.

 PowerShell

 PS> $null -eq $undefinedVariable
 True

<!-- p.399 -->

If you happen to mistype a variable name then PowerShell sees it as a different variable and
the value is $null .

The other way you find $null values is when they come from other commands that don't give
you any results.

 PowerShell

 PS> function Get-Nothing {}
 PS> $value = Get-Nothing
 PS> $null -eq $value
 True

Impact of $null
$null values impact your code differently depending on where they show up.

In strings
If you use $null in a string, then it's a blank value (or empty string).

 PowerShell

 PS> $value = $null
 PS> Write-Output "'The value is $value'"
 'The value is '

This is one of the reasons that I like to place brackets around variables when using them in log
messages. It's even more important to identify the edges of your variable values when the
value is at the end of the string.

 PowerShell

 PS> $value = $null
 PS> Write-Output "The value is [$value]"
 The value is []

This makes empty strings and $null values easy to spot.

In numeric equation
When a $null value is used in a numeric equation then your results are invalid if they don't
give an error. Sometimes the $null evaluates to 0 and other times it makes the whole result

<!-- p.400 -->

$null . Here is an example with multiplication that gives 0 or $null depending on the order of

the values.

 PowerShell

 PS> $null * 5
 PS> $null -eq ( $null * 5 )
 True

 PS> 5 * $null
 0
 PS> $null -eq ( 5 * $null )
 False

In place of a collection
A collection allows you use an index to access values. If you try to index into a collection that is
actually null , you get this error: Cannot index into a null array .

 PowerShell

 PS> $value = $null
 PS> $value[10]
 Cannot index into a null array.
 At line:1 char:1
 + $value[10]
 + ~~~~~~~~~~
     + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
     + FullyQualifiedErrorId : NullArray

If you have a collection but try to access an element that is not in the collection, you get a
$null result.

 PowerShell

 $array = @( 'one','two','three' )
 $null -eq $array[100]
 True

In place of an object
If you try to access a property or sub property of an object that doesn't have the specified
property, you get a $null value like you would for an undefined variable. It doesn't matter if
the variable is $null or an actual object in this case.
