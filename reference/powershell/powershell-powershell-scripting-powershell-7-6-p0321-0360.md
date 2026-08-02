---
title: "How to use this documentation — pages 321-360"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0321-0360
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0321-0360
family: powershell
documentKind: "doc"
abstract: "$key = $ht.Keys[0] $ht.$($key) a $ht[$key] a When the key is an array, you must wrap the $key variable in a subexpression so that it can be used with member access ( . ) notation. Or, you can use array index ( [] ) notation. Use in automatic variables $PSBoundParameters $PSBound"
---

# How to use this documentation — pages 321-360

<!-- p.321 -->

 $key = $ht.Keys[0]
 $ht.$($key)
 a
 $ht[$key]
 a

When the key is an array, you must wrap the $key variable in a subexpression so that it can be
used with member access ( . ) notation. Or, you can use array index ( [] ) notation.

Use in automatic variables
$PSBoundParameters
$PSBoundParameters is an automatic variable that only exists inside the context of a function. It

contains all the parameters that the function was called with. This isn't exactly a hashtable but
close enough that you can treat it like one.

That includes removing keys and splatting it to other functions. If you find yourself writing proxy
functions, take a closer look at this one.

See about_Automatic_Variables for more details.

PSBoundParameters gotcha
One important thing to remember is that this only includes the values that are passed in as
parameters. If you also have parameters with default values but aren't passed in by the caller,
$PSBoundParameters doesn't contain those values. This is commonly overlooked.

$PSDefaultParameterValues
This automatic variable lets you assign default values to any cmdlet without changing the cmdlet.
Take a look at this example.

 PowerShell

 $PSDefaultParameterValues["Out-File:Encoding"] = "UTF8"

This adds an entry to the $PSDefaultParameterValues hashtable that sets UTF8 as the default
value for the Out-File -Encoding parameter. This is session-specific so you should place it in your
$PROFILE .

I use this often to pre-assign values that I type quite often.

<!-- p.322 -->

  PowerShell

  $PSDefaultParameterValues[ "Connect-VIServer:Server" ] = 'VCENTER01.contoso.local'

This also accepts wildcards so you can set values in bulk. Here are some ways you can use that:

  PowerShell

  $PSDefaultParameterValues[ "Get-*:Verbose" ] = $true
  $PSDefaultParameterValues[ "*:Credential" ] = Get-Credential

For a more in-depth breakdown, see this great article on Automatic Defaults    by Michael
Sorens    .

Regex $Matches
When you use the -match operator, an automatic variable called $Matches is created with the
results of the match. If you have any sub expressions in your regex, those sub matches are also
listed.

  PowerShell

  $message = 'My SSN is 123-45-6789.'

  $message -match 'My SSN is (.+)\.'
  $Matches[0]
  $Matches[1]

Named matches
This is one of my favorite features that most people don't know about. If you use a named regex
match, then you can access that match by name on the matches.

  PowerShell

  $message = 'My Name is Kevin and my SSN is 123-45-6789.'

  if($message -match 'My Name is (?<Name>.+) and my SSN is (?<SSN>.+)\.')
  {
      $Matches.Name
      $Matches.SSN
  }

<!-- p.323 -->

In the example above, the (?<Name>.*) is a named sub expression. This value is then placed in
the $Matches.Name property.

Group-Object -AsHashtable
One little known feature of Group-Object is that it can turn some datasets into a hashtable for
you.

 PowerShell

 Import-Csv $Path | Group-Object -AsHashtable -Property Email

This will add each row into a hashtable and use the specified property as the key to access it.

Copying Hashtables
One important thing to know is that hashtables are objects. And each variable is just a reference
to an object. This means that it takes more work to make a valid copy of a hashtable.

Assigning reference types
When you have one hashtable and assign it to a second variable, both variables point to the
same hashtable.

 PowerShell

 PS> $orig = @{name='orig'}
 PS> $copy = $orig
 PS> $copy.name = 'copy'
 PS> 'Copy: [{0}]' -f $copy.name
 PS> 'Orig: [{0}]' -f $orig.name

 Copy: [copy]
 Orig: [copy]

This highlights that they're the same because altering the values in one will also alter the values
in the other. This also applies when passing hashtables into other functions. If those functions
make changes to that hashtable, your original is also altered.

Shallow copies, single level
If we have a simple hashtable like our example above, we can use Clone() to make a shallow
copy.

<!-- p.324 -->

 PowerShell

 PS> $orig = @{name='orig'}
 PS> $copy = $orig.Clone()
 PS> $copy.name = 'copy'
 PS> 'Copy: [{0}]' -f $copy.name
 PS> 'Orig: [{0}]' -f $orig.name

 Copy: [copy]
 Orig: [orig]

This will allow us to make some basic changes to one that don't impact the other.

Shallow copies, nested
The reason why it's called a shallow copy is because it only copies the base level properties. If one
of those properties is a reference type (like another hashtable), then those nested objects will still
point to each other.

 PowerShell

 PS> $orig = @{
         person=@{
             name='orig'
         }
     }
 PS> $copy = $orig.Clone()
 PS> $copy.person.name = 'copy'
 PS> 'Copy: [{0}]' -f $copy.person.name
 PS> 'Orig: [{0}]' -f $orig.person.name

 Copy: [copy]
 Orig: [copy]

So you can see that even though I cloned the hashtable, the reference to person wasn't cloned.
We need to make a deep copy to truly have a second hashtable that isn't linked to the first.

Deep copies
There are a couple of ways to make a deep copy of a hashtable (and keep it as a hashtable).
Here's a function using PowerShell to recursively create a deep copy:

 PowerShell

 function Get-DeepClone
 {
     [CmdletBinding()]

<!-- p.325 -->

      param(
          $InputObject
      )
      process
      {
          if($InputObject -is [hashtable]) {
              $clone = @{}
              foreach($key in $InputObject.Keys)
              {
                  $clone[$key] = Get-DeepClone $InputObject[$key]
              }
              return $clone
          } else {
              return $InputObject
          }
      }
 }

It doesn't handle any other reference types or arrays, but it's a good starting point.

Another way is to use .NET to deserialize it using CliXml like in this function:

 PowerShell

 function Get-DeepClone
 {
     param(
         $InputObject
     )
     $TempCliXmlString = [System.Management.Automation.PSSerializer]::Serialize(
         $InputObject, [int32]::MaxValue)
     return [System.Management.Automation.PSSerializer]::Deserialize($TempCliXmlString)
 }

For extremely large hashtables, the deserializing function is faster as it scales out. However, there
are some things to consider when using this method. Since it uses CliXml, it's memory intensive
and if you are cloning huge hashtables, that might be a problem. Another limitation of the CliXml
is there is a depth limitation of 48. Meaning, if you have a hashtable with 48 layers of nested
hashtables, the cloning will fail and no hashtable will be output at all.

Anything else?
I covered a lot of ground quickly. My hope is that you walk away leaning something new or
understanding it better every time you read this. Because I covered the full spectrum of this
feature, there are aspects that just may not apply to you right now. That is perfectly OK and is
kind of expected depending on how much you work with PowerShell.

<!-- p.326 -->

Last updated on 07/13/2026

<!-- p.327 -->

Everything you wanted to know about
PSCustomObject
PSCustomObject is a great tool to add into your PowerShell tool belt. Let's start with the basics

and work our way into the more advanced features. The idea behind using a PSCustomObject is
to have a simple way to create structured data. Take a look at the first example and you'll have
a better idea of what that means.

  ７ Note

  The original version     of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com       .

Creating a PSCustomObject
I love using [pscustomobject] in PowerShell. Creating a usable object has never been easier.
Because of that, I'm going to skip over all the other ways you can create an object but I need to
mention that most of these examples are PowerShell v3.0 and newer.

 PowerShell

 $myObject = [pscustomobject]@{
     Name     = 'Kevin'
     Language = 'PowerShell'
     State    = 'Texas'
 }

This method works well for me because I use hashtables for just about everything. But there
are times when I would like PowerShell to treat hashtables more like an object. The first place
you notice the difference is when you want to use Format-Table or Export-Csv and you realize
that a hashtable is just a collection of key/value pairs.

You can then access and use the values like you would a normal object.

 PowerShell

 $myObject.Name

<!-- p.328 -->

Converting a hashtable
While I am on the topic, did you know you could do this:

 PowerShell

 $myHashtable = @{
     Name     = 'Kevin'
     Language = 'PowerShell'
     State    = 'Texas'
 }
 $myObject = [pscustomobject]$myHashtable

I do prefer to create the object from the start but there are times you have to work with a
hashtable first. This example works because the constructor takes a hashtable for the object
properties. One important note is that while this method works, it isn't an exact equivalent. The
biggest difference is that the order of the properties isn't preserved.

If you want to preserve the order, see Ordered hashtables.

Legacy approach
You may have seen people use New-Object to create custom objects.

 PowerShell

 $myHashtable = @{
     Name     = 'Kevin'
     Language = 'PowerShell'
     State    = 'Texas'
 }

 $myObject = New-Object -TypeName psobject -Property $myHashtable

This way is quite a bit slower but it may be your best option on early versions of PowerShell.

Saving to a file
I find the best way to save a hashtable to a file is to save it as JSON. You can import it back into
a [pscustomobject]

 PowerShell

 $myObject | ConvertTo-Json -Depth 1 | Set-Content -Path $Path
 $myObject = Get-Content -Path $Path | ConvertFrom-Json

<!-- p.329 -->

I cover more ways to save objects to a file in my article on The many ways to read and write to
files   .

Working with properties
Adding properties
You can still add new properties to your PSCustomObject with Add-Member .

  PowerShell

  $myObject | Add-Member -MemberType NoteProperty -Name 'ID' -Value 'KevinMarquette'

  $myObject.ID

Remove properties
You can also remove properties off of an object.

  PowerShell

  $myObject.psobject.Properties.Remove('ID')

The .psobject is an intrinsic member that gives you access to base object metadata. For more
information about intrinsic members, see about_Intrinsic_Members.

Enumerating property names
Sometimes you need a list of all the property names on an object.

  PowerShell

  $myObject | Get-Member -MemberType NoteProperty | select -ExpandProperty Name

We can get this same list off of the psobject property too.

  PowerShell

  $myobject.psobject.Properties.Name

   ７ Note

<!-- p.330 -->

  Get-Member returns the properties in alphabetical order. Using the member-access

  operator to enumerate the property names returns the properties in the order they were
  defined on the object.

Dynamically accessing properties
I already mentioned that you can access property values directly.

 PowerShell

 $myObject.Name

You can use a string for the property name and it will still work.

 PowerShell

 $myObject.'Name'

We can take this one more step and use a variable for the property name.

 PowerShell

 $property = 'Name'
 $myObject.$property

I know that looks strange, but it works.

Convert PSCustomObject into a hashtable
To continue on from the last section, you can dynamically walk the properties and create a
hashtable from them.

 PowerShell

 $hashtable = @{}
 foreach( $property in $myobject.psobject.Properties.Name )
 {
     $hashtable[$property] = $myObject.$property
 }

Testing for properties

<!-- p.331 -->

If you need to know if a property exists, you could just check for that property to have a value.

 PowerShell

 if( $null -ne $myObject.ID )

But if the value could be $null you can check to see if it exists by checking the
psobject.Properties for it.

 PowerShell

 if( $myobject.psobject.Properties.Match('ID').Count )

Adding object methods
If you need to add a script method to an object, you can do it with Add-Member and a
ScriptBlock . You have to use the this automatic variable reference the current object. Here is

a scriptblock to turn an object into a hashtable. (same code form the last example)

 PowerShell

 $ScriptBlock = {
     $hashtable = @{}
     foreach( $property in $this.psobject.Properties.Name )
     {
         $hashtable[$property] = $this.$property
     }
     return $hashtable
 }

Then we add it to our object as a script property.

 PowerShell

 $memberParam = @{
     MemberType = "ScriptMethod"
     InputObject = $myobject
     Name = "ToHashtable"
     Value = $scriptBlock
 }
 Add-Member @memberParam

Then we can call our function like this:

 PowerShell

<!-- p.332 -->

 $myObject.ToHashtable()

Objects vs Value types
Objects and value types don't handle variable assignments the same way. If you assign value
types to each other, only the value get copied to the new variable.

 PowerShell

 $first = 1
 $second = $first
 $second = 2

In this case, $first is 1 and $second is 2.

Object variables hold a reference to the actual object. When you assign one object to a new
variable, they still reference the same object.

 PowerShell

 $third = [pscustomobject]@{Key=3}
 $fourth = $third
 $fourth.Key = 4

Because $third and $fourth reference the same instance of an object, both $third.key and
$fourth.Key are 4.

psobject.Copy()
If you need a true copy of an object, you can clone it.

 PowerShell

 $third = [pscustomobject]@{Key=3}
 $fourth = $third.psobject.Copy()
 $fourth.Key = 4

Clone creates a shallow copy of the object. They have different instances now and $third.key
is 3 and $fourth.Key is 4 in this example.

I call this a shallow copy because if you have nested objects (objects with properties contain
other objects), only the top-level values are copied. The child objects will reference each other.

<!-- p.333 -->

PSTypeName for custom object types
Now that we have an object, there are a few more things we can do with it that may not be
nearly as obvious. First thing we need to do is give it a PSTypeName . This is the most common
way I see people do it:

 PowerShell

 $myObject.psobject.TypeNames.Insert(0,"My.Object")

I recently discovered another way to do this from Redditor u/markekraus . He talks about this
approach that allows you to define it inline.

 PowerShell

 $myObject = [pscustomobject]@{
     PSTypeName = 'My.Object'
     Name       = 'Kevin'
     Language   = 'PowerShell'
     State      = 'Texas'
 }

I love how nicely this just fits into the language. Now that we have an object with a proper type
name, we can do some more things.

  ７ Note

  You can also create custom PowerShell types using PowerShell classes. For more
  information, see PowerShell Class Overview.

Using DefaultPropertySet (the long way)
PowerShell decides for us what properties to display by default. A lot of the native commands
have a .ps1xml formatting file    that does all the heavy lifting. From this post by Boe Prox   ,
there's another way for us to do this on our custom object using just PowerShell. We can give it
a MemberSet for it to use.

 PowerShell

 $defaultDisplaySet = 'Name','Language'
 $defaultDisplayPropertySet = New-Object
 System.Management.Automation.PSPropertySet('DefaultDisplayPropertySet',

<!-- p.334 -->

  [string[]]$defaultDisplaySet)
  $PSStandardMembers =
  [System.Management.Automation.PSMemberInfo[]]@($defaultDisplayPropertySet)
  $MyObject | Add-Member MemberSet PSStandardMembers $PSStandardMembers

Now when my object just falls to the shell, it will only show those properties by default.

Update-TypeData with DefaultPropertySet
This is nice but I recently saw a better way using Update-TypeData to specify the default
properties.

  PowerShell

  $TypeData = @{
      TypeName = 'My.Object'
      DefaultDisplayPropertySet = 'Name','Language'
  }
  Update-TypeData @TypeData

That is simple enough that I could almost remember it if I didn't have this post as a quick
reference. Now I can easily create objects with lots of properties and still give it a nice clean
view when looking at it from the shell. If I need to access or see those other properties, they're
still there.

  PowerShell

  $myObject | Format-List *

Update-TypeData with ScriptProperty
Something else I got out of that video was creating script properties for your objects. This
would be a good time to point out that this works for existing objects too.

  PowerShell

  $TypeData = @{
      TypeName = 'My.Object'
      MemberType = 'ScriptProperty'
      MemberName = 'UpperCaseName'
      Value = {$this.Name.ToUpper()}
  }
  Update-TypeData @TypeData

<!-- p.335 -->

You can do this before your object is created or after and it will still work. This is what makes
this different than using Add-Member with a script property. When you use Add-Member the way I
referenced earlier, it only exists on that specific instance of the object. This one applies to all
objects with this TypeName .

Function parameters
You can now use these custom types for parameters in your functions and scripts. You can have
one function create these custom objects and then pass them into other functions.

 PowerShell

 param( [PSTypeName('My.Object')]$Data )

PowerShell requires that the object is the type you specified. It throws a validation error if the
type doesn't match automatically to save you the step of testing for it in your code. A great
example of letting PowerShell do what it does best.

Function OutputType
You can also define an OutputType for your advanced functions.

 PowerShell

 function Get-MyObject
 {
     [OutputType('My.Object')]
     [CmdletBinding()]
         param
         (
             ...

The OutputType attribute value is only a documentation note. It isn't derived from the function
code or compared to the actual function output.

The main reason you would use an output type is so that meta information about your
function reflects your intentions. Things like Get-Command and Get-Help that your development
environment can take advantage of. If you want more information, then take a look at the help
for it: about_Functions_OutputTypeAttribute.

With that said, if you're using Pester to unit test your functions then it would be a good idea to
validate the output objects match your OutputType. This could catch variables that just fall to

<!-- p.336 -->

the pipe when they shouldn't.

Closing thoughts
The context of this was all about [pscustomobject] , but a lot of this information applies to
objects in general.

I have seen most of these features in passing before but never saw them presented as a
collection of information on PSCustomObject . Just this last week I stumbled upon another one
and was surprised that I had not seen it before. I wanted to pull all these ideas together so you
can hopefully see the bigger picture and be aware of them when you have an opportunity to
use them. I hope you learned something and can find a way to work this into your scripts.

 Last updated on 03/24/2025

<!-- p.337 -->

Everything you wanted to know about
variable substitution in strings
There are many ways to use variables in strings. I'm calling this variable substitution but I'm
referring to any time you want to format a string to include values from variables. This is
something that I often find myself explaining to new scripters.

  ７ Note

  The original version    of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com       .

Concatenation
The first class of methods can be referred to as concatenation. It's basically taking several
strings and joining them together. There's a long history of using concatenation to build
formatted strings.

 PowerShell

 $name = 'Kevin Marquette'
 $message = 'Hello, ' + $name

Concatenation works out OK when there are only a few values to add. But this can get
complicated quickly.

 PowerShell

 $first = 'Kevin'
 $last = 'Marquette'

 PowerShell

 $message = 'Hello, ' + $first + ' ' + $last + '.'

This simple example is already getting harder to read.

<!-- p.338 -->

Variable substitution
PowerShell has another option that is easier. You can specify your variables directly in the
strings.

  PowerShell

  $message = "Hello, $first $last."

The type of quotes you use around the string makes a difference. A double quoted string
allows the substitution but a single quoted string doesn't. There are times you want one or the
other so you have an option.

Command substitution
Things get a little tricky when you start trying to get the values of properties into a string. This
is where many new people get tripped up. First let me show you what they think should work
(and at face value almost looks like it should).

  PowerShell

  $directory = Get-Item 'C:\windows'
  $message = "Time: $directory.CreationTime"

You would be expecting to get the CreationTime off of the $directory , but instead you get this
Time: C:\windows.CreationTime as your value. The reason is that this type of substitution only

sees the base variable. It considers the period as part of the string so it stops resolving the
value any deeper.

It just so happens that this object gives a string as a default value when placed into a string.
Some objects give you the type name instead like System.Collections.Hashtable . Just
something to watch for.

PowerShell allows you to do command execution inside the string with a special syntax. This
allows us to get the properties of these objects and run any other command to get a value.

  PowerShell

  $message = "Time: $($directory.CreationTime)"

<!-- p.339 -->

This works great for some situations but it can get just as crazy as concatenation if you have
just a few variables.

Command execution
You can run commands inside a string. Even though I have this option, I don't like it. It gets
cluttered quickly and hard to debug. I either run the command and save to a variable or use a
format string.

 PowerShell

 $message = "Date: $(Get-Date)"

Format string
.NET has a way to format strings that I find fairly easy to work with. First let me show you the
static method for it before I show you the PowerShell shortcut to do the same thing.

 PowerShell

 # .NET string format string
 [string]::Format('Hello, {0} {1}.',$first,$last)

 # PowerShell format string
 'Hello, {0} {1}.' -f $first, $last

What is happening here is that the string is parsed for the tokens {0} and {1} , then it uses
that number to pick from the values provided. If you want to repeat one value some place in
the string, you can reuse that values number.

The more complicated the string gets, the more value you get out of this approach.

Format values as arrays
If your format line gets too long, you can place your values into an array first.

 PowerShell

 $values = @(
     "Kevin"
     "Marquette"
 )
 'Hello, {0} {1}.' -f $values

<!-- p.340 -->

This is not splatting because I'm passing the whole array in, but the idea is similar.

Advanced formatting
I intentionally called these out as coming from .NET because there are lots of formatting
options already well documented on it. There are built-in ways to format various data types.

  PowerShell

  "{0:yyyyMMdd}" -f (Get-Date)
  "Population {0:N0}" -f 8175133

  Output

  20211110
  Population 8,175,133

I'm not going to go into them but I just wanted to let you know that this is a very powerful
formatting engine if you need it.

Joining strings
Sometimes you actually do want to concatenate a list of values together. There's a -join
operator that can do that for you. It even lets you specify a character to join between the
strings.

  PowerShell

  $servers = @(
      'server1'
      'server2'
      'server3'
  )

  $servers     -join ','

If you want to -join some strings without a separator, you need to specify an empty string '' .
But if that is all you need, there's a faster option.

  PowerShell

  [string]::Concat('server1','server2','server3')
  [string]::Concat($servers)

<!-- p.341 -->

It's also worth pointing out that you can also -split strings too.

Join-Path
This is often overlooked but a great cmdlet for building a file path.

 PowerShell

 $folder = 'Temp'
 Join-Path -Path 'C:\windows' -ChildPath $folder

The great thing about this is it works out the backslashes correctly when it puts the values
together. This is especially important if you are taking values from users or config files.

This also goes well with Split-Path and Test-Path . I also cover these in my post about reading
and saving to files .

Strings are arrays
I do need to mention adding strings here before I go on. Remember that a string is just an
array of characters. When you add multiple strings together, a new array is created each time.

Look at this example:

 PowerShell

 $message = "Numbers: "
 foreach($number in 1..10000)
 {
     $message += " $number"
 }

It looks very basic but what you don't see is that each time a string is added to $message that a
whole new string is created. Memory gets allocated, data gets copied and the old one is
discarded. Not a big deal when it's only done a few times, but a loop like this would really
expose the issue.

StringBuilder
StringBuilder is also very popular for building large strings from lots of smaller strings. The
reason why is because it just collects all the strings you add to it and only concatenates all of
them at the end when you retrieve the value.

<!-- p.342 -->

 PowerShell

 $stringBuilder = New-Object -TypeName "System.Text.StringBuilder"

 [void]$stringBuilder.Append("Numbers: ")
 foreach($number in 1..10000)
 {
     [void]$stringBuilder.Append(" $number")
 }
 $message = $stringBuilder.ToString()

Again, this is something that I'm reaching out to .NET for. I don't use it often anymore but it's
good to know it's there.

Delineation with braces
This is used for suffix concatenation within the string. Sometimes your variable doesn't have a
clean word boundary.

 PowerShell

 $test = "Bet"
 $tester = "Better"
 Write-Host "$test $tester ${test}ter"

Thank you Redditor u/real_parbold for that one.

Here is an alternate to this approach:

 PowerShell

 Write-Host "$test $tester $($test)ter"
 Write-Host "{0} {1} {0}ter" -f $test, $tester

I personally use format string for this, but this is good to know in case you see it in the wild.

Find and replace tokens
While most of these features limit your need to roll your own solution, there are times where
you may have large template files where you want to replace strings inside.

Let us assume you pulled in a template from a file that has a lot of text.

 PowerShell

<!-- p.343 -->

 $letter = Get-Content -Path TemplateLetter.txt -RAW
 $letter = $letter -replace '#FULL_NAME#', 'Kevin Marquette'

You may have lots of tokens to replace. The trick is to use a very distinct token that is easy to
find and replace. I tend to use a special character at both ends to help distinguish it.

I recently found a new way to approach this. I decided to leave this section in here because this
is a pattern that is commonly used.

Replace multiple tokens
When I have a list of tokens that I need to replace, I take a more generic approach. I would
place them in a hashtable and iterate over them to do the replace.

 PowerShell

 $tokenList = @{
     Full_Name = 'Kevin Marquette'
     Location = 'Orange County'
     State = 'CA'
 }

 $letter = Get-Content -Path TemplateLetter.txt -RAW
 foreach( $token in $tokenList.GetEnumerator() )
 {
     $pattern = '#{0}#' -f $token.key
     $letter = $letter -replace $pattern, $token.Value
 }

Those tokens could be loaded from JSON or CSV if needed.

ExecutionContext ExpandString
There's a clever way to define a substitution string with single quotes and expand the variables
later. Look at this example:

 PowerShell

 $message = 'Hello, $Name!'
 $name = 'Kevin Marquette'
 $string = $ExecutionContext.InvokeCommand.ExpandString($message)

The call to InvokeCommand.ExpandString on the current execution context uses the variables in
the current scope for substitution. The key thing here is that the $message can be defined very

<!-- p.344 -->

early before the variables even exist.

If we expand on that just a little bit, we can perform this substitution over and over with
different values.

 PowerShell

 $message = 'Hello, $Name!'
 $nameList = 'Mark Kraus','Kevin Marquette','Lee Dailey'
 foreach($name in $nameList){
     $ExecutionContext.InvokeCommand.ExpandString($message)
 }

To keep going on this idea; you could be importing a large email template from a text file to do
this. I have to thank Mark Kraus    for this suggestion.

Whatever works the best for you
I'm a fan of the format string approach. I definitely do this with the more complicated strings
or if there are multiple variables. On anything that is very short, I may use any one of these.

Anything else?
I covered a lot of ground on this one. My hope is that you walk away learning something new.

Links
If you'd like to learn more about the methods and features that make string interpolation
possible, see the following list for the reference documentation.

     Concatenation uses the addition operator
     Variable and command substitution follow the quoting rules
     Formatting uses the format operator
     Joining strings uses the join operator and references Join-Path, but you could also read
     about Join-String
     Arrays are documented in About arrays
     StringBuilder is a .NET class, with its own documentation
     Braces in strings is also covered in the quoting rules
     Token replacement uses the replace operator
     The $ExecutionContext.InvokeCommand.ExpandString() method has .NET API reference
     documentation

<!-- p.345 -->

Last updated on 08/06/2025

<!-- p.346 -->

Everything you wanted to know about the
if statement
Like many other languages, PowerShell has statements for conditionally executing code in your
scripts. One of those statements is the If statement. Today we will take a deep dive into one of
the most fundamental commands in PowerShell.

  ７ Note

  The original version    of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com       .

Conditional execution
Your scripts often need to make decisions and perform different logic based on those
decisions. This is what I mean by conditional execution. You have one statement or value to
evaluate, then execute a different section of code based on that evaluation. This is exactly what
the if statement does.

The if statement
Here is a basic example of the if statement:

 PowerShell
 $condition = $true
 if ( $condition )
 {
     Write-Output "The condition was true"
 }

The first thing the if statement does is evaluate the expression in parentheses. If it evaluates
to $true , then it executes the statements in the braces. If the value was $false , then it would
skip over that statement block.

In the previous example, the if statement was just evaluating the $condition variable. It was
$true and would have executed the Write-Output command inside the statement block.

<!-- p.347 -->

In some languages, you can place a single line of code after the if statement and it gets
executed. That isn't the case in PowerShell. You must provide a full statement block with
braces for it to work correctly.

Comparison operators
The most common use of the if statement for is comparing two items with each other.
PowerShell has special operators for different comparison scenarios. When you use a
comparison operator, the value on the left-hand side is compared to the value on the right-
hand side.

-eq for equality
The -eq does an equality check between two values to make sure they're equal to each other.

 PowerShell

 $value = Get-MysteryValue
 if ( 5 -eq $value )
 {
     # do something
 }

In this example, I'm taking a known value of 5 and comparing it to my $value to see if they
match.

One possible use case is to check the status of a value before you take an action on it. You
could get a service and check that the status was running before you called Restart-Service
on it.

It's common in other languages like C# to use == for equality (ex: 5 == $value ) but that
doesn't work with PowerShell. Another common mistake that people make is to use the equals
sign (ex: 5 = $value ) that is reserved for assigning values to variables. By placing your known
value on the left, it makes that mistake more awkward to make.

This operator (and others) has a few variations.

         -eq case-insensitive equality
         -ieq case-insensitive equality

         -ceq case-sensitive equality

-ne not equal

<!-- p.348 -->

Many operators have a related operator that is checking for the opposite result. -ne verifies
that the values don't equal each other.

 PowerShell

 if ( 5 -ne $value )
 {
     # do something
 }

Use this to make sure that the action only executes if the value isn't 5 . A good use-cases where
would be to check if a service was in the running state before you try to start it.

Variations:

      -ne case-insensitive not equal
      -ine case-insensitive not equal

      -cne case-sensitive not equal

These are inverse variations of -eq . I'll group these types together when I list variations for
other operators.

-gt -ge -lt -le for greater than or less than
These operators are used when checking to see if a value is larger or smaller than another
value. The -gt -ge -lt -le stand for GreaterThan, GreaterThanOrEqual, LessThan, and
LessThanOrEqual.

 PowerShell

 if ( $value -gt 5 )
 {
     # do something
 }

Variations:

      -gt greater than
      -igt greater than, case-insensitive

      -cgt greater than, case-sensitive

      -ge greater than or equal
      -ige greater than or equal, case-insensitive

      -cge greater than or equal, case-sensitive
      -lt less than

<!-- p.349 -->

     -ilt less than, case-insensitive
     -clt less than, case-sensitive

     -le less than or equal
     -ile less than or equal, case-insensitive

     -cle less than or equal, case-sensitive

I don't know why you would use case-sensitive and insensitive options for these operators.

-like wildcard matches
PowerShell has its own wildcard-based pattern matching syntax and you can use it with the -
like operator. These wildcard patterns are fairly basic.

     ? matches any single character

     * matches any number of characters

 PowerShell

 $value = 'S-ATX-SQL01'
 if ( $value -like 'S-*-SQL??')
 {
     # do something
 }

It's important to point out that the pattern matches the whole string. If you need to match
something in the middle of the string, you need to place the * on both ends of the string.

 PowerShell
 $value = 'S-ATX-SQL02'
 if ( $value -like '*SQL*')
 {
     # do something
 }

Variations:

     -like case-insensitive wildcard

     -ilike case-insensitive wildcard
     -clike case-sensitive wildcard

     -notlike case-insensitive wildcard not matched
     -inotlike case-insensitive wildcard not matched

     -cnotlike case-sensitive wildcard not matched

<!-- p.350 -->

-match regular expression
The -match operator allows you to check a string for a regular-expression-based match. Use
this when the wildcard patterns aren't flexible enough for you.

 PowerShell
 $value = 'S-ATX-SQL01'
 if ( $value -match 'S-\w\w\w-SQL\d\d')
 {
     # do something
 }

A regex pattern matches anywhere in the string by default. So you can specify a substring that
you want matched like this:

 PowerShell
 $value = 'S-ATX-SQL01'
 if ( $value -match 'SQL')
 {
     # do something
 }

Regex is a complex language of its own and worth looking into. I talk more about -match and
the many ways to use regex     in another article.

Variations:

     -match case-insensitive regex
     -imatch case-insensitive regex

     -cmatch case-sensitive regex
     -notmatch case-insensitive regex not matched

     -inotmatch case-insensitive regex not matched

     -cnotmatch case-sensitive regex not matched

-is of type
You can check a value's type with the -is operator.

 PowerShell

 if ( $value -is [string] )
 {

<!-- p.351 -->

     # do something
 }

You may use this if you're working with classes or accepting various objects over the pipeline.
You could have either a service or a service name as your input. Then check to see if you have a
service and fetch the service if you only have the name.

 PowerShell
 if ( $Service -isnot [System.ServiceProcess.ServiceController] )
 {
     $Service = Get-Service -Name $Service
 }

Variations:

     -is of type

     -isnot not of type

Collection operators
When you use the previous operators with a single value, the result is $true or $false . This is
handled slightly differently when working with a collection. Each item in the collection gets
evaluated and the operator returns every value that evaluates to $true .

 PowerShell

 PS> 1,2,3,4 -eq 3
 3

This still works correctly in an if statement. So a value is returned by your operator, then the
whole statement is $true .

 PowerShell
 $array = 1..6
 if ( $array -gt 3 )
 {
     # do something
 }

There's one small trap hiding in the details here that I need to point out. When using the -ne
operator this way, it's easy to mistakenly look at the logic backwards. Using -ne with a
collection returns $true if any item in the collection doesn't match your value.

<!-- p.352 -->

 PowerShell
 PS> 1,2,3 -ne 4
 1
 2
 3

This may look like a clever trick, but we have operators -contains and -in that handle this
more efficiently. And -notcontains does what you expect.

-contains
The -contains operator checks the collection for your value. As soon as it finds a match, it
returns $true .

 PowerShell
 $array = 1..6
 if ( $array -contains 3 )
 {
     # do something
 }

This is the preferred way to see if a collection contains your value. Using Where-Object (or -eq )
walks the entire list every time and is significantly slower.

Variations:

        -contains case-insensitive match
        -icontains case-insensitive match

        -ccontains case-sensitive match
        -notcontains case-insensitive not matched

        -inotcontains case-insensitive not matched

        -cnotcontains case-sensitive not matched

-in
The -in operator is just like the -contains operator except the collection is on the right-hand
side.

 PowerShell
 $array = 1..6
 if ( 3 -in $array )

<!-- p.353 -->

 {
      # do something
 }

Variations:

      -in case-insensitive match

      -iin case-insensitive match
      -cin case-sensitive match

      -notin case-insensitive not matched

      -inotin case-insensitive not matched
      -cnotin case-sensitive not matched

Logical operators
Logical operators are used to invert or combine other expressions.

-not
The -not operator flips an expression from $false to $true or from $true to $false . Here is
an example where we want to perform an action when Test-Path is $false .

 PowerShell
 if ( -not ( Test-Path -Path $path ) )

Most of the operators we talked about do have a variation where you do not need to use the -
not operator. But there are still times it is useful.

! operator
You can use ! as an alias for -not .

 PowerShell
 if ( -not $value ){}
 if ( !$value ){}

You may see ! used more by people that come from another languages like C#. I prefer to
type it out because I find it hard to see when quickly looking at my scripts.

<!-- p.354 -->

-and
You can combine expressions with the -and operator. When you do that, both sides need to be
$true for the whole expression to be $true .

 PowerShell
 if ( ($age -gt 13) -and ($age -lt 55) )

In that example, $age must be 13 or older for the left side and less than 55 for the right side. I
added extra parentheses to make it clearer in that example but they're optional as long as the
expression is simple. Here is the same example without them.

 PowerShell
 if ( $age -gt 13 -and $age -lt 55 )

Evaluation happens from left to right. If the first item evaluates to $false , it exits early and
doesn't perform the right comparison. This is handy when you need to make sure a value exists
before you use it. For example, Test-Path throws an error if you give it a $null path.

 PowerShell
 if ( $null -ne $path -and (Test-Path -Path $path) )

-or
The -or allows for you to specify two expressions and returns $true if either one of them is
$true .

 PowerShell
 if ( $age -le 13 -or $age -ge 55 )

Just like with the -and operator, the evaluation happens from left to right. Except that if the
first part is $true , then the whole statement is $true and it doesn't process the rest of the
expression.

Also make note of how the syntax works for these operators. You need two separate
expressions. I have seen users try to do something like this $value -eq 5 -or 6 without
realizing their mistake.

<!-- p.355 -->

-xor exclusive or
This one is a little unusual. -xor allows only one expression to evaluate to $true . So if both
items are $false or both items are $true , then the whole expression is $false . Another way to
look at this is the expression is only $true when the results of the expression are different.

It's rare that anyone would ever use this logical operator and I can't think up a good example
as to why I would ever use it.

Bitwise operators
Bitwise operators perform calculations on the bits within the values and produce a new value
as the result. Teaching bitwise operators is beyond the scope of this article, but here is the list
of them.

      -band binary AND
      -bor binary OR

      -bxor binary exclusive OR

      -bnot binary NOT
      -shl shift left

      -shr shift right

PowerShell expressions
We can use normal PowerShell inside the condition statement.

 PowerShell
 if ( Test-Path -Path $Path )

Test-Path returns $true or $false when it executes. This also applies to commands that

return other values.

 PowerShell
 if ( Get-Process Notepad* )

It evaluates to $true if there's a returned process and $false if there isn't. It's perfectly valid to
use pipeline expressions or other PowerShell statements like this:

 PowerShell

<!-- p.356 -->

 if ( Get-Process | where Name -EQ Notepad )

These expressions can be combined with each other with the -and and -or operators, but you
may have to use parenthesis to break them into subexpressions.

 PowerShell
 if ( (Get-Process) -and (Get-Service) )

Checking for $null
Having a no result or a $null value evaluates to $false in the if statement. When checking
specifically for $null , it's a best practice to place the $null on the left-hand side.

 PowerShell

 if ( $null -eq $value )

There are quite a few nuances when dealing with $null values in PowerShell. If you're
interested in diving deeper, I have an article about everything you wanted to know about $null.

Variable assignment within the condition
I almost forgot to add this one until Prasoon Karunan V       reminded me of it.

 PowerShell
 if ($process=Get-Process notepad -ErrorAction Ignore) {$process} else {$false}

Normally when you assign a value to a variable, the value isn't passed onto the pipeline or
console. When you do a variable assignment in a sub expression, it does get passed on to the
pipeline.

 PowerShell
 PS> $first = 1
 PS> ($second = 2)
 2

See how the $first assignment has no output and the $second assignment does? When an
assignment is done in an if statement, it executes just like the $second assignment above.
Here is a clean example on how you could use it:

<!-- p.357 -->

 PowerShell
 if ( $process = Get-Process Notepad* )
 {
     $process | Stop-Process
 }

If $process gets assigned a value, then the statement is $true and $process gets stopped.

Make sure you don't confuse this with -eq because this isn't an equality check. This is a more
obscure feature that most people don't realize works this way.

Variable assignment from the statement block
You can also use the if statement statement block to assign a value to a variable.

 PowerShell

 $discount = if ( $age -ge 55 )
 {
      Get-SeniorDiscount
 }
 elseif ( $age -le 13 )
 {
      Get-ChildDiscount
 }
 else
 {
      0.00
 }

Each script block is writing the results of the commands, or the value, as output. We can assign
the result of the if statement to the $discount variable. That example could have just as easily
assigned those values to the $discount variable directly in each statement block. I can't say
that I use this with the if statement often, but I do have an example where I used this recently.

Alternate execution path
The if statement allows you to specify an action for not only when the statement is $true , but
also for when it's $false . This is where the else statement comes into play.

else
The else statement is always the last part of the if statement when used.

<!-- p.358 -->

 PowerShell
 if ( Test-Path -Path $Path -PathType Leaf )
 {
      Move-Item -Path $Path -Destination $archivePath
 }
 else
 {
      Write-Warning "$path doesn't exist or isn't a file."
 }

In this example, we check the $path to make sure it's a file. If we find the file, we move it. If not,
we write a warning. This type of branching logic is very common.

Nested if
The if and else statements take a script block, so we can place any PowerShell command
inside them, including another if statement. This allows you to make use of much more
complicated logic.

 PowerShell
 if ( Test-Path -Path $Path -PathType Leaf )
 {
      Move-Item -Path $Path -Destination $archivePath
 }
 else
 {
      if ( Test-Path -Path $Path )
      {
          Write-Warning "A file was required but a directory was found instead."
      }
      else
      {
          Write-Warning "$path could not be found."
      }
 }

In this example, we test the happy path first and then take action on it. If that fails, we do
another check and to provide more detailed information to the user.

elseif
We aren't limited to just a single conditional check. We can chain if and else statements
together instead of nesting them by using the elseif statement.

 PowerShell

<!-- p.359 -->

 if ( Test-Path -Path $Path -PathType Leaf )
 {
      Move-Item -Path $Path -Destination $archivePath
 }
 elseif ( Test-Path -Path $Path )
 {
      Write-Warning "A file was required but a directory was found instead."
 }
 else
 {
      Write-Warning "$path could not be found."
 }

The execution happens from the top to the bottom. The top if statement is evaluated first. If
that is $false , then it moves down to the next elseif or else in the list. That last else is the
default action to take if none of the others return $true .

switch
At this point, I need to mention the switch statement. It provides an alternate syntax for doing
multiple comparisons with a value. With the switch , you specify an expression and that result
gets compared with several different values. If one of those values match, the matching code
block is executed. Take a look at this example:

 PowerShell
 $itemType = 'Role'
 switch ( $itemType )
 {
     'Component'
     {
         'is a component'
     }
     'Role'
     {
         'is a role'
     }
     'Location'
     {
         'is a location'
     }
 }

There three possible values that can match the $itemType . In this case, it matches with Role . I
used a simple example just to give you some exposure to the switch operator. I talk more
about everything you ever wanted to know about the switch statement in another article.

<!-- p.360 -->

Array inline
I have a function called Invoke-SnowSql      that launches an executable with several command-
line arguments. Here is a clip from that function where I build the array of arguments.

 PowerShell
 $snowSqlParam = @(
     '--accountname', $Endpoint
     '--username', $Credential.UserName
     '--option', 'exit_on_error=true'
     '--option', 'output_format=csv'
     '--option', 'friendly=false'
     '--option', 'timing=false'
     if ($Debug)
     {
         '--option', 'log_level=DEBUG'
     }
     if ($Path)
     {
         '--filename', $Path
     }
     else
     {
         '--query', $singleLineQuery
     }
 )

The $Debug and $Path variables are parameters on the function that are provided by the end
user. I evaluate them inline inside the initialization of my array. If $Debug is true, then those
values fall into the $snowSqlParam in the correct place. Same holds true for the $Path variable.

Simplify complex operations
It's inevitable that you run into a situation that has way too many comparisons to check and
your if statement scrolls way off the right side of the screen.

 PowerShell
 $user = Get-ADUser -Identity $UserName
 if ( $null -ne $user -and $user.Department -eq 'Finance' -and $user.Title -match
 'Senior' -and $user.HomeDrive -notlike '\\server\*' )
 {
     # Do Something
 }
