---
title: "How to use this documentation — pages 281-320"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0281-0320
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0281-0320
family: powershell
documentKind: "doc"
abstract: "The foreach loop works well with collections. Using the syntax: foreach ( <variable> in <collection> ) PowerShell foreach ( $node in $data ) { \"Item: [$node]\" } ForEach method I tend to forget about this one but it works well for simple operations. PowerShell allows you to call"
---

# How to use this documentation — pages 281-320

<!-- p.281 -->

The foreach loop works well with collections. Using the syntax: foreach ( <variable> in
<collection> )

 PowerShell

 foreach ( $node in $data )
 {
     "Item: [$node]"
 }

ForEach method

I tend to forget about this one but it works well for simple operations. PowerShell allows you to
call ForEach() on a collection.

 PowerShell

 PS> $data.ForEach({"Item [$PSItem]"})
 Item [Zero]
 Item [One]
 Item [Two]
 Item [Three]

The ForEach() takes a parameter that is a script block. You can drop the parentheses and just
provide the script block.

 PowerShell

 $data.ForEach{"Item [$PSItem]"}

This is a lesser known syntax but it works just the same. This ForEach method was added in
PowerShell 4.0.

For loop

The for loop is used heavily in most other languages but you don't see it much in PowerShell.
When you do see it, it's often in the context of walking an array.

 PowerShell

 for ( $index = 0; $index -lt $data.Count; $index++)
 {
     "Item: [{0}]" -f $data[$index]
 }

<!-- p.282 -->

The first thing we do is initialize an $index to 0 . Then we add the condition that $index must
be less than $data.Count . Finally, we specify that every time we loop that we must increase the
index by 1 . In this case $index++ is short for $index = $index + 1 . The format operator ( -f ) is
used to insert the value of $data[$index] in the output string.

Whenever you're using a for loop, pay special attention to the condition. I used $index -lt
$data.Count here. It's easy to get the condition slightly wrong to get an off-by-one error in

your logic. Using $index -le $data.Count or $index -lt ($data.Count - 1) are ever so slightly
wrong. That would cause your result to process too many or too few items. This is the classic
off-by-one error.

Switch loop

This is one that is easy to overlook. If you provide an array to a switch statement, it checks each
item in the array.

 PowerShell

 $data = 'Zero','One','Two','Three'
 switch( $data )
 {
     'One'
     {
         'Tock'
     }
     'Three'
     {
         'Tock'
     }
     Default
     {
         'Tick'
     }
 }

 Output

 Tick
 Tock
 Tick
 Tock

There are a lot of cool things that we can do with the switch statement. I have another article
dedicated to this.

     Everything you ever wanted to know about the switch statement

<!-- p.283 -->

Updating values

When your array is a collection of string or integers (value types), sometimes you may want to
update the values in the array as you loop over them. Most of the loops above use a variable in
the loop that holds a copy of the value. If you update that variable, the original value in the
array is not updated.

The exception to that statement is the for loop. If you want to walk an array and update
values inside it, then the for loop is what you're looking for.

 PowerShell

 for ( $index = 0; $index -lt $data.Count; $index++ )
 {
     $data[$index] = "Item: [{0}]" -f $data[$index]
 }

This example takes a value by index, makes a few changes, and then uses that same index to
assign it back.

Arrays of Objects
So far, the only thing we've placed in an array is a value type, but arrays can also contain
objects.

 PowerShell

 $data = @(
     [pscustomobject]@{FirstName='Kevin';LastName='Marquette'}
     [pscustomobject]@{FirstName='John'; LastName='Doe'}
 )

Many cmdlets return collections of objects as arrays when you assign them to a variable.

 PowerShell

 $processList = Get-Process

All of the basic features we already talked about still apply to arrays of objects with a few
details worth pointing out.

Accessing properties

<!-- p.284 -->

We can use an index to access an individual item in a collection just like with value types.

  PowerShell

  PS> $data[0]

  FirstName LastName
  -----     ----
  Kevin     Marquette

We can access and update properties directly.

  PowerShell

  PS> $data[0].FirstName

  Kevin

  PS> $data[0].FirstName = 'Jay'
  PS> $data[0]

  FirstName LastName
  -----     ----
  Jay       Marquette

Array properties

Normally you would have to enumerate the whole list like this to access all the properties:

  PowerShell

  PS> $data | ForEach-Object {$_.LastName}

  Marquette
  Doe

Or by using the Select-Object -ExpandProperty cmdlet.

  PowerShell

  PS> $data | Select-Object -ExpandProperty LastName

  Marquette
  Doe

But PowerShell offers us the ability to request LastName directly. PowerShell enumerates them
all for us and returns a clean list.

<!-- p.285 -->

 PowerShell

 PS> $data.LastName

 Marquette
 Doe

The enumeration still happens but we don't see the complexity behind it.

Where-Object filtering
This is where Where-Object comes in so we can filter and select what we want out of the array
based on the properties of the object.

 PowerShell

 PS> $data | Where-Object {$_.FirstName -eq 'Kevin'}

 FirstName LastName
 -----     ----
 Kevin     Marquette

We can write that same query to get the FirstName we are looking for.

 PowerShell

 $data | where FirstName -EQ Kevin

Where()

Arrays have a Where() method on them that allows you to specify a scriptblock for the filter.

 PowerShell

 $data.Where({$_.FirstName -eq 'Kevin'})

This feature was added in PowerShell 4.0.

Updating objects in loops
With value types, the only way to update the array is to use a for loop because we need to
know the index to replace the value. We have more options with objects because they are
reference types. Here is a quick example:

<!-- p.286 -->

 PowerShell

 foreach($person in $data)
 {
     $person.FirstName = 'Kevin'
 }

This loop is walking every object in the $data array. Because objects are reference types, the
$person variable references the exact same object that is in the array. So updates to its

properties do update the original.

You still can't replace the whole object this way. If you try to assign a new object to the
$person variable, you're updating the variable reference to something else that no longer

points to the original object in the array. This doesn't work like you would expect:

 PowerShell

 foreach($person in $data)
 {
     $person = [pscustomobject]@{
         FirstName='Kevin'
         LastName='Marquette'
     }
 }

Operators
The operators in PowerShell also work on arrays. Some of them work slightly differently.

-join
The -join operator is the most obvious one so let's look at it first. I like the -join operator
and use it often. It joins all elements in the array with the character or string that you specify.

 PowerShell

 PS> $data = @(1,2,3,4)
 PS> $data -join '-'
 1-2-3-4
 PS> $data -join ','
 1,2,3,4

One of the features that I like about the -join operator is that it handles single items.

 PowerShell

<!-- p.287 -->

 PS> 1 -join '-'
 1

I use this inside logging and verbose messages.

 PowerShell

 PS> $data = @(1,2,3,4)
 PS> "Data is $($data -join ',')."
 Data is 1,2,3,4.

-join $array

Here is a clever trick that Lee Dailey pointed out to me. If you ever want to join everything
without a delimiter, instead of doing this:

 PowerShell

 PS> $data = @(1,2,3,4)
 PS> $data -join $null
 1234

You can use -join with the array as the parameter with no prefix. Take a look at this example
to see that I'm talking about.

 PowerShell

 PS> $data = @(1,2,3,4)
 PS> -join $data
 1234

-replace and -split
The other operators like -replace and -split execute on each item in the array. I can't say
that I have ever used them this way but here is an example.

 PowerShell

 PS> $data = @('ATX-SQL-01','ATX-SQL-02','ATX-SQL-03')
 PS> $data -replace 'ATX','LAX'
 LAX-SQL-01
 LAX-SQL-02
 LAX-SQL-03

<!-- p.288 -->

-contains
The -contains operator allows you to check an array of values to see if it contains a specified
value.

 PowerShell

 PS> $data = @('red','green','blue')
 PS> $data -contains 'green'
 True

-in
When you have a single value that you would like to verify matches one of several values, you
can use the -in operator. The value would be on the left and the array on the right-hand side
of the operator.

 PowerShell

 PS> $data = @('red','green','blue')
 PS> 'green' -in $data
 True

This can get expensive if the list is large. I often use a regex pattern if I'm checking more than a
few values.

 PowerShell

 PS> $data = @('red','green','blue')
 PS> $pattern = "^({0})$" -f ($data -join '|')
 PS> $pattern
 ^(red|green|blue)$

 PS> 'green' -match $pattern
 True

-eq and -ne
Equality and arrays can get complicated. When the array is on the left side, every item gets
compared. Instead of returning True , it returns the object that matches.

 PowerShell

<!-- p.289 -->

 PS> $data = @('red','green','blue')
 PS> $data -eq 'green'
 green

When you use the -ne operator, we get all the values that are not equal to our value.

 PowerShell

 PS> $data = @('red','green','blue')
 PS> $data -ne 'green'
 red
 blue

When you use this in an if() statement, a value that is returned is a True value. If no value is
returned, then it's a False value. Both of these next statements evaluate to True .

 PowerShell

 $data = @('red','green','blue')
 if ( $data -eq 'green' )
 {
     'Green was found'
 }
 if ( $data -ne 'green' )
 {
     'And green was not found'
 }

I'll revisit this in a moment when we talk about testing for $null .

-match
The -match operator tries to match each item in the collection.

 PowerShell

 PS> $servers = @(
     'LAX-SQL-01'
     'LAX-API-01'
     'ATX-SQL-01'
     'ATX-API-01'
 )
 PS> $servers -match 'SQL'
 LAX-SQL-01
 ATX-SQL-01

<!-- p.290 -->

When you use -match with a single value, a special variable $Matches gets populated with
match info. This isn't the case when an array is processed this way.

We can take the same approach with Select-String .

 PowerShell

 $servers | Select-String SQL

I take a closer look at Select-String , -match and the $Matches variable in another post called
The many ways to use regex     .

$null or empty
Testing for $null or empty arrays can be tricky. Here are the common traps with arrays.

At a glance, this statement looks like it should work.

 PowerShell

 if ( $array -eq $null)
 {
     'Array is $null'
 }

But I just went over how -eq checks each item in the array. So we can have an array of several
items with a single $null value and it would evaluate to $true

 PowerShell

 $array = @('one',$null,'three')
 if ( $array -eq $null)
 {
     'I think Array is $null, but I would be wrong'
 }

This is why it's a best practice to place the $null on the left side of the operator. This makes
this scenario a non-issue.

 PowerShell

 if ( $null -eq $array )
 {
     'Array actually is $null'
 }

<!-- p.291 -->

A $null array isn't the same thing as an empty array. If you know you have an array, check the
count of objects in it. If the array is $null , the count is 0 .

  PowerShell

  if ( $array.Count -gt 0 )
  {
      "Array isn't empty"
  }

There is one more trap to watch out for here. You can use the Count even if you have a single
object, unless that object is a PSCustomObject . This is a bug that is fixed in PowerShell 6.1.
That's good news, but a lot of people are still on 5.1 and need to watch out for it.

  PowerShell

  PS> $object = [pscustomobject]@{Name='TestObject'}
  PS> $object.Count
  $null

If you're still on PowerShell 5.1, you can wrap the object in an array before checking the count
to get an accurate count.

  PowerShell

  if ( @($array).Count -gt 0 )
  {
      "Array isn't empty"
  }

To fully play it safe, check for $null , then check the count.

  PowerShell

  if ( $null -ne $array -and @($array).Count -gt 0 )
  {
      "Array isn't empty"
  }

All -eq
I recently saw someone on Reddit ask how to verify that every value in an array matches a
given value. Reddit user u/bis had this clever solution that checks for any incorrect values and
then flips the result.

<!-- p.292 -->

 PowerShell

 $results = Test-Something
 if ( -not ( $results -ne 'Passed') )
 {
     'All results a Passed'
 }

Adding to arrays
At this point, you're starting to wonder how to add items to an array. The quick answer is that
you can't. An array is a fixed size in memory. If you need to grow it or add a single item to it,
then you need to create a new array and copy all the values over from the old array. This
sounds like a lot of work, however, PowerShell hides the complexity of creating the new array.
PowerShell implements the addition operator ( + ) for arrays.

  ７ Note

  PowerShell does not implement a subtraction operation. If you want a flexible alternative
  to an array, you need to use a generic List object.

Array addition
We can use the addition operator with arrays to create a new array. So given these two arrays:

 PowerShell

 $first = @(
     'Zero'
     'One'
 )
 $second = @(
     'Two'
     'Three'
 )

We can add them together to get a new array.

 PowerShell

 PS> $first + $second

 Zero
 One

<!-- p.293 -->

 Two
 Three

Plus equals +=
We can create a new array in place and add an item to it like this:

 PowerShell

 $data = @(
     'Zero'
     'One'
     'Two'
     'Three'
 )
 $data += 'four'

Just remember that every time you use += that you're duplicating and creating a new array.
This is a not an issue for small datasets but it scales extremely poorly.

Pipeline assignment
You can assign the results of any pipeline into a variable. It's an array if it contains multiple
items.

 PowerShell

 $array = 1..5 | ForEach-Object {
     "ATX-SQL-$PSItem"
 }

Normally when we think of using the pipeline, we think of the typical PowerShell one-liners. We
can leverage the pipeline with foreach() statements and other loops. So instead of adding
items to an array in a loop, we can drop items onto the pipeline.

 PowerShell

 $array = foreach ( $node in (1..5))
 {
     "ATX-SQL-$node"
 }

Array Types

<!-- p.294 -->

By default, an array in PowerShell is created as a [psobject[]] type. This allows it to contain
any type of object or value. This works because everything is inherited from the PSObject type.

Strongly typed arrays
You can create an array of any type using a similar syntax. When you create a strongly typed
array, it can only contain values or objects the specified type.

 PowerShell

 PS> [int[]] $numbers = 1,2,3
 PS> [int[]] $numbers2 = 'one','two','three'
 ERROR: Cannot convert value "one" to type "System.Int32". Input string was not in a
 correct format."

 PS> [string[]] $strings = 'one','two','three'

ArrayList
Adding items to an array is one of its biggest limitations, but there are a few other collections
that we can turn to that solve this problem.

The ArrayList is commonly one of the first things that we think of when we need an array that
is faster to work with. It acts like an object array every place that we need it, but it handles
adding items quickly.

Here is how we create an ArrayList and add items to it.

 PowerShell

 $myarray = [System.Collections.ArrayList]::new()
 [void]$myArray.Add('Value')

We are calling into .NET to get this type. In this case, we are using the default constructor to
create it. Then we call the Add method to add an item to it.

The reason I'm using [void] at the beginning of the line is to suppress the return code. Some
.NET calls do this and can create unexpected output.

If the only data that you have in your array is strings, then also take a look at using
StringBuilder   . It's almost the same thing but has some methods that are just for dealing with
strings. The StringBuilder is specially designed for performance.

<!-- p.295 -->

It's common to see people move to ArrayList from arrays. But it comes from a time where C#
didn't have generic support. The ArrayList is deprecated in support for the generic List[]

Generic List
A generic type is a special type in C# that defines a generalized class and the user specifies the
data types it uses when created. So if you want a list of numbers or strings, you would define
that you want list of int or string types.

Here is how you create a List for strings.

 PowerShell

 $mylist = [System.Collections.Generic.List[string]]::new()

Or a list for numbers.

 PowerShell

 $mylist = [System.Collections.Generic.List[int]]::new()

We can cast an existing array to a list like this without creating the object first:

 PowerShell

 $mylist = [System.Collections.Generic.List[int]]@(1,2,3)

We can shorten the syntax with the using namespace statement in PowerShell 5 and newer. The
using statement needs to be the first line of your script. By declaring a namespace, PowerShell

lets you leave it off of the data types when you reference them.

 PowerShell

 using namespace System.Collections.Generic
 $myList = [List[int]]@(1,2,3)

This makes the List much more usable.

You have a similar Add method available to you. Unlike the ArrayList, there is no return value
on the Add method so we don't have to void it.

 PowerShell

<!-- p.296 -->

 $myList.Add(10)

And we can still access the elements like other arrays.

 PowerShell

 PS> $myList[-1]
 10

List[psobject]

You can have a list of any type, but when you don't know the type of objects, you can use
[List[psobject]] to contain them.

 PowerShell

 $list = [List[psobject]]::new()

Remove()

The ArrayList and the generic List[] both support removing items from the collection.

 PowerShell

 using namespace System.Collections.Generic
 $myList = [List[string]]@('Zero','One','Two','Three')
 [void]$myList.Remove("Two")
 Zero
 One
 Three

When working with value types, it removes the first one from the list. You can call it over and
over again to keep removing that value. If you have reference types, you have to provide the
object that you want removed.

 PowerShell

 [List[System.Management.Automation.PSDriveInfo]]$drives = Get-PSDrive
 $drives.Remove($drives[2])

 PowerShell

 $delete = $drives[2]

<!-- p.297 -->

  $drives.Remove($delete)

The remove method returns true if it was able to find and remove the item from the
collection.

More collections
There are many other collections that can be used but these are the good generic array
replacements. If you're interested in learning about more of these options, take a look at this
Gist   that Mark Kraus     put together.

Other nuances
Now that I have covered all the major functionality, here are a few more things that I wanted to
mention before I wrap this up.

Pre-sized arrays
I mentioned that you can't change the size of an array once it's created. We can create an array
of a pre-determined size by calling it with the new($size) constructor.

  PowerShell

  $data = [Object[]]::new(4)
  $data.Count
  4

Multiplying arrays
An interesting little trick is that you can multiply an array by an integer.

  PowerShell

  PS> $data = @('red','green','blue')
  PS> $data * 3
  red
  green
  blue
  red
  green
  blue
  red
  green
  blue

<!-- p.298 -->

Initialize with 0
A common scenario is that you want to create an array with all zeros. If you're only going to
have integers, a strongly typed array of integers defaults to all zeros.

  PowerShell

  PS> [int[]]::new(4)
  0
  0
  0
  0

We can use the multiplying trick to do this too.

  PowerShell

  PS> $data = @(0) * 4
  PS> $data
  0
  0
  0
  0

The nice thing about the multiplying trick is that you can use any value. So if you would rather
have 255 as your default value, this would be a good way to do it.

  PowerShell

  PS> $data = @(255) * 4
  PS> $data
  255
  255
  255
  255

Nested arrays
An array inside an array is called a nested array. I don't use these much in PowerShell but I have
used them more in other languages. Consider using an array of arrays when your data fits in a
grid like pattern.

Here are two ways we can create a two-dimensional array.

  PowerShell

<!-- p.299 -->

  $data = @(@(1,2,3),@(4,5,6),@(7,8,9))

  $data2 = @(
      @(1,2,3),
      @(4,5,6),
      @(7,8,9)
  )

The comma is very important in those examples. I gave an earlier example of a normal array on
multiple lines where the comma was optional. That isn't the case with a multi-dimensional
array.

The way we use the index notation changes slightly now that we've a nested array. Using the
$data above, this is how we would access the value 3.

  PowerShell

  PS> $outside = 0
  PS> $inside = 2
  PS> $data[$outside][$inside]
  3

Add a set of bracket for each level of array nesting. The first set of brackets is for the outer
most array and then you work your way in from there.

Write-Output -NoEnumerate
PowerShell likes to unwrap or enumerate arrays. This is a core aspect of the way PowerShell
uses the pipeline but there are times that you don't want that to happen.

I commonly pipe objects to Get-Member to learn more about them. When I pipe an array to it, it
gets unwrapped and Get-Member sees the members of the array and not the actual array.

  PowerShell

  PS> $data = @('red','green','blue')
  PS> $data | Get-Member
  TypeName: System.String
  ...

To prevent that unwrap of the array, you can use Write-Output -NoEnumerate .

  PowerShell

<!-- p.300 -->

  PS> Write-Output -NoEnumerate $data | Get-Member
  TypeName: System.Object[]
  ...

I have a second way that's more of a hack (and I try to avoid hacks like this). You can place a
comma in front of the array before you pipe it. This wraps $data into another array where it is
the only element, so after the unwrapping the outer array we get back $data unwrapped.

  PowerShell

  PS> ,$data | Get-Member
  TypeName: System.Object[]
  ...

Return an array
This unwrapping of arrays also happens when you output or return values from a function. You
can still get an array if you assign the output to a variable so this isn't commonly an issue.

The catch is that you have a new array. If that is ever a problem, you can use Write-Output -
NoEnumerate $array or return ,$array to work around it.

Anything else?
I know this is all a lot to take in. My hope is that you learn something from this article every
time you read it and that it turns out to be a good reference for you for a long time to come. If
you found this to be helpful, please share it with others you think may get value out of it.

From here, I would recommend you check out a similar post that I wrote about hashtables.

 Last updated on 03/24/2025

<!-- p.301 -->

Everything you wanted to know
about hashtables
I want to take a step back and talk about hashtables. I use them all the time now. I was teaching
someone about them after our user group meeting last night and I realized I had the same
confusion about them as he had. Hashtables are really important in PowerShell so it's good to
have a solid understanding of them.

  ７ Note

  The original version     of this article appeared on the blog written by @KevinMarquette .
  The PowerShell team thanks Kevin for sharing this content with us. Please check out his blog
  at PowerShellExplained.com        .

Hashtable as a collection of things
I want you to first see a Hashtable as a collection in the traditional definition of a hashtable. This
definition gives you a fundamental understanding of how they work when they get used for more
advanced stuff later. Skipping this understanding is often a source of confusion.

What is an array?
Before I jump into what a Hashtable is, I need to mention arrays first. For the purpose of this
discussion, an array is a list or collection of values or objects.

  PowerShell

  $array = @(1,2,3,5,7,11)

Once you have your items into an array, you can either use foreach to iterate over the list or use
an index to access individual elements in the array.

  PowerShell

  foreach($item in $array)
  {
      Write-Output $item
  }

<!-- p.302 -->

  Write-Output $array[3]

You can also update values using an index in the same way.

  PowerShell

  $array[2] = 13

I just scratched the surface on arrays but that should put them into the right context as I move
onto hashtables.

What is a hashtable?
I'm going to start with a basic technical description of what hashtables are, in the general sense,
before I shift into the other ways PowerShell uses them.

A hashtable is a data structure, much like an array, except you store each value (object) using a
key. It's a basic key/value store. First, we create an empty hashtable.

  PowerShell

  $ageList = @{}

Notice that braces, instead of parentheses, are used to define a hashtable. Then we add an item
using a key like this:

  PowerShell

  $key = 'Kevin'
  $value = 36
  $ageList.Add( $key, $value )

  $ageList.Add( 'Alex', 9 )

The person's name is the key and their age is the value that I want to save.

Using the brackets for access
Once you add your values to the hashtable, you can pull them back out using that same key
(instead of using a numeric index like you would have for an array).

  PowerShell

<!-- p.303 -->

 $ageList['Kevin']
 $ageList['Alex']

When I want Kevin's age, I use his name to access it. We can use this approach to add or update
values into the hashtable too. This is just like using the Add() method above.

 PowerShell

 $ageList = @{}

 $key = 'Kevin'
 $value = 36
 $ageList[$key] = $value

 $ageList['Alex'] = 9

There's another syntax you can use for accessing and updating values that I'll cover in a later
section. If you're coming to PowerShell from another language, these examples should fit in with
how you may have used hashtables before.

Creating hashtables with values
So far I've created an empty hashtable for these examples. You can pre-populate the keys and
values when you create them.

 PowerShell

 $ageList = @{
     Kevin = 36
     Alex = 9
 }

As a lookup table
The real value of this type of a hashtable is that you can use them as a lookup table. Here is a
simple example.

 PowerShell

 $environments = @{
     Prod = 'SrvProd05'
     QA   = 'SrvQA02'
     Dev = 'SrvDev12'
 }

<!-- p.304 -->

  $server = $environments[$env]

In this example, you specify an environment for the $env variable and it will pick the correct
server. You could use a switch($env){...} for a selection like this but a hashtable is a nice option.

This gets even better when you dynamically build the lookup table to use it later. So think about
using this approach when you need to cross reference something. I think we would see this even
more if PowerShell wasn't so good at filtering on the pipe with Where-Object . If you're ever in a
situation where performance matters, this approach needs to be considered.

I won't say that it's faster, but it does fit into the rule of If performance matters, test it .

Multiselection

Generally, you think of a hashtable as a key/value pair, where you provide one key and get one
value. PowerShell allows you to provide an array of keys to get multiple values.

  PowerShell

  $environments[@('QA','DEV')]
  $environments[('QA','DEV')]
  $environments['QA','DEV']

In this example, I use the same lookup hashtable from above and provide three different array
styles to get the matches. This is a hidden gem in PowerShell that most people aren't aware of.

Iterating hashtables
Because a hashtable is a collection of key/value pairs, you iterate over it differently than you do
for an array or a normal list of items.

The first thing to notice is that if you pipe your hashtable, the pipe treats it like one object.

  PowerShell

  PS> $ageList | Measure-Object
  count : 1

Even though the Count property tells you how many values it contains.

  PowerShell

<!-- p.305 -->

 PS> $ageList.Count
 2

You get around this issue by using the Values property if all you need is just the values.

 PowerShell

 PS> $ageList.Values | Measure-Object -Average
 Count   : 2
 Average : 22.5

It's often more useful to enumerate the keys and use them to access the values.

 PowerShell

 PS> $ageList.Keys | ForEach-Object{
     $message = '{0} is {1} years old!' -f $_, $ageList[$_]
     Write-Output $message
 }
 Kevin is 36 years old
 Alex is 9 years old

Here is the same example with a foreach(){...} loop.

 PowerShell

 foreach($key in $ageList.Keys)
 {
     $message = '{0} is {1} years old' -f $key, $ageList[$key]
     Write-Output $message
 }

We are walking each key in the hashtable and then using it to access the value. This is a common
pattern when working with hashtables as a collection.

GetEnumerator()
That brings us to GetEnumerator() for iterating over our hashtable.

 PowerShell

 $ageList.GetEnumerator() | ForEach-Object{
     $message = '{0} is {1} years old!' -f $_.Key, $_.Value
     Write-Output $message
 }

<!-- p.306 -->

The enumerator gives you each key/value pair one after another. It was designed specifically for
this use case. Thank you to Mark Kraus       for reminding me of this one.

BadEnumeration
One important detail is that you can't modify a hashtable while it's being enumerated. If we start
with our basic $environments example:

  PowerShell

  $environments = @{
      Prod = 'SrvProd05'
      QA   = 'SrvQA02'
      Dev = 'SrvDev12'
  }

And trying to set every key to the same server value fails.

  PowerShell

  $environments.Keys | ForEach-Object {
      $environments[$_] = 'SrvDev03'
  }

  An error occurred while enumerating through a collection: Collection was modified;
  enumeration operation may not execute.
  + CategoryInfo          : InvalidOperation: tableEnumerator:HashtableEnumerator) [],
   RuntimeException
  + FullyQualifiedErrorId : BadEnumeration

This will also fail even though it looks like it should also be fine:

  PowerShell

  foreach($key in $environments.Keys) {
      $environments[$key] = 'SrvDev03'
  }

  Collection was modified; enumeration operation may not execute.
      + CategoryInfo          : OperationStopped: (:) [], InvalidOperationException
      + FullyQualifiedErrorId : System.InvalidOperationException

The trick to this situation is to clone the keys before doing the enumeration.

  PowerShell

<!-- p.307 -->

 $environments.Keys.Clone() | ForEach-Object {
     $environments[$_] = 'SrvDev03'
 }

  ７ Note

  You can't clone a hashtable containing a single key. PowerShell throws an error. Instead, you
  convert the Keys property to an array, then iterate over the array.

 PowerShell

 @($environments.Keys) | ForEach-Object {
     $environments[$_] = 'SrvDev03'
 }

Hashtable as a collection of properties
So far the type of objects we placed in our hashtable were all the same type of object. I used ages
in all those examples and the key was the person's name. This is a great way to look at it when
your collection of objects each have a name. Another common way to use hashtables in
PowerShell is to hold a collection of properties where the key is the name of the property. I'll step
into that idea in this next example.

Property-based access
The use of property-based access changes the dynamics of hashtables and how you can use
them in PowerShell. Here is our usual example from above treating the keys as properties.

 PowerShell

 $ageList = @{}
 $ageList.Kevin = 35
 $ageList.Alex = 9

Just like the examples above, this example adds those keys if they don't exist in the hashtable
already. Depending on how you defined your keys and what your values are, this is either a little
strange or a perfect fit. The age list example has worked great up until this point. We need a new
example for this to feel right going forward.

 PowerShell

<!-- p.308 -->

  $person = @{
      name = 'Kevin'
      age = 36
  }

And we can add and access attributes on the $person like this.

  PowerShell

  $person.city = 'Austin'
  $person.state = 'TX'

All of a sudden this hashtable starts to feel and act like an object. It's still a collection of things, so
all the examples above still apply. We just approach it from a different point of view.

Checking for keys and values
In most cases, you can just test for the value with something like this:

  PowerShell

  if( $person.age ){...}

It's simple but has been the source of many bugs for me because I was overlooking one
important detail in my logic. I started to use it to test if a key was present. When the value was
$false or zero, that statement would return $false unexpectedly.

  PowerShell

  if( $null -ne $person.age ){...}

This works around that issue for zero values but not $null vs non-existent keys. Most of the time
you don't need to make that distinction but there are methods for when you do.

  PowerShell

  if( $person.ContainsKey('age') ){...}

We also have a ContainsValue() for the situation where you need to test for a value without
knowing the key or iterating the whole collection.

Removing and clearing keys

<!-- p.309 -->

You can remove keys with the Remove() method.

 PowerShell

 $person.Remove('age')

Assigning them a $null value just leaves you with a key that has a $null value.

A common way to clear a hashtable is to just initialize it to an empty hashtable.

 PowerShell

 $person = @{}

While that does work, try to use the Clear() method instead.

 PowerShell

 $person.Clear()

This is one of those instances where using the method creates self-documenting code and it
makes the intentions of the code very clean.

All the fun stuff
Ordered hashtables
By default, hashtables aren't ordered (or sorted). In the traditional context, the order doesn't
matter when you always use a key to access values. You may find that you want the properties to
stay in the order that you define them. Thankfully, there's a way to do that with the ordered
keyword.

 PowerShell

 $person = [ordered]@{
     name = 'Kevin'
     age = 36
 }

Now when you enumerate the keys and values, they stay in that order.

Inline hashtables

<!-- p.310 -->

When you're defining a hashtable on one line, you can separate the key/value pairs with a
semicolon.

 PowerShell

 $person = @{ name = 'kevin'; age = 36; }

This will come in handy if you're creating them on the pipe.

Custom expressions in common pipeline commands
There are a few cmdlets that support the use of hashtables to create custom or calculated
properties. You commonly see this with Select-Object and Format-Table . The hashtables have a
special syntax that looks like this when fully expanded.

 PowerShell

 $property = @{
     Name = 'TotalSpaceGB'
     Expression = { ($_.Used + $_.Free) / 1GB }
 }

The Name is what the cmdlet would label that column. The Expression is a script block that is
executed where $_ is the value of the object on the pipe. Here is that script in action:

 PowerShell

 $drives = Get-PSDrive | where Used
 $drives | Select-Object -Property Name, $property

 Name     TotalSpaceGB
 ----     ------------
 C    238.472652435303

I placed that in a variable but it could easily be defined inline and you can shorten Name to n and
Expression to e while you're at it.

 PowerShell

 $drives | Select-Object -Property Name, @{n='TotalSpaceGB';e={($_.Used + $_.Free) /
 1GB}}

I personally don't like how long that makes commands and it often promotes some bad
behaviors that I won't get into. I'm more likely to create a new hashtable or pscustomobject with

<!-- p.311 -->

all the fields and properties that I want instead of using this approach in scripts. But there's a lot
of code out there that does this so I wanted you to be aware of it. I talk about creating a
pscustomobject later on.

Custom sort expression
It's easy to sort a collection if the objects have the data that you want to sort on. You can either
add the data to the object before you sort it or create a custom expression for Sort-Object .

 PowerShell

 Get-ADUser | Sort-Object -Property @{ e={ Get-TotalSales $_.Name } }

In this example I'm taking a list of users and using some custom cmdlet to get additional
information just for the sort.

Sort a list of Hashtables

If you have a list of hashtables that you want to sort, you'll find that the Sort-Object doesn't treat
your keys as properties. We can get a round that by using a custom sort expression.

 PowerShell

 $data = @(
     @{name='a'}
     @{name='c'}
     @{name='e'}
     @{name='f'}
     @{name='d'}
     @{name='b'}
 )

 $data | Sort-Object -Property @{e={$_.name}}

Splatting hashtables at cmdlets
This is one of my favorite things about hashtables that many people don't discover early on. The
idea is that instead of providing all the properties to a cmdlet on one line, you can instead pack
them into a hashtable first. Then you can give the hashtable to the function in a special way. Here
is an example of creating a DHCP scope the normal way.

 PowerShell

<!-- p.312 -->

  Add-DhcpServerV4Scope -Name 'TestNetwork' -StartRange '10.0.0.2' -EndRange
  '10.0.0.254' -SubnetMask '255.255.255.0' -Description 'Network for testlab A' -
  LeaseDuration (New-TimeSpan -Days 8) -Type "Both"

Without using splatting, all those things need to be defined on a single line. It either scrolls off
the screen or will wrap where ever it feels like. Now compare that to a command that uses
splatting.

  PowerShell

  $DHCPScope = @{
      Name          = 'TestNetwork'
      StartRange    = '10.0.0.2'
      EndRange      = '10.0.0.254'
      SubnetMask    = '255.255.255.0'
      Description   = 'Network for testlab A'
      LeaseDuration = (New-TimeSpan -Days 8)
      Type          = "Both"
  }
  Add-DhcpServerV4Scope @DHCPScope

The use of the @ sign instead of the $ is what invokes the splat operation.

Just take a moment to appreciate how easy that example is to read. They are the exact same
command with all the same values. The second one is easier to understand and maintain going
forward.

I use splatting anytime the command gets too long. I define too long as causing my window to
scroll right. If I hit three properties for a function, odds are that I'll rewrite it using a splatted
hashtable.

Splatting for optional parameters
One of the most common ways I use splatting is to deal with optional parameters that come from
some place else in my script. Let's say I have a function that wraps a Get-CimInstance call that has
an optional $Credential argument.

  PowerShell

  $CIMParams = @{
      ClassName = 'Win32_BIOS'
      ComputerName = $ComputerName
  }

  if($Credential)

<!-- p.313 -->

 {
      $CIMParams.Credential = $Credential
 }

 Get-CimInstance @CIMParams

I start by creating my hashtable with common parameters. Then I add the $Credential if it exists.
Because I'm using splatting here, I only need to have the call to Get-CimInstance in my code
once. This design pattern is very clean and can handle lots of optional parameters easily.

To be fair, you could write your commands to allow $null values for parameters. You just don't
always have control over the other commands you're calling.

Multiple splats
You can splat multiple hashtables to the same cmdlet. If we revisit our original splatting example:

 PowerShell

 $Common = @{
     SubnetMask = '255.255.255.0'
     LeaseDuration = (New-TimeSpan -Days 8)
     Type = "Both"
 }

 $DHCPScope = @{
     Name        = 'TestNetwork'
     StartRange = '10.0.0.2'
     EndRange    = '10.0.0.254'
     Description = 'Network for testlab A'
 }

 Add-DhcpServerv4Scope @DHCPScope @Common

I'll use this method when I have a common set of parameters that I'm passing to lots of
commands.

Splatting for clean code
There's nothing wrong with splatting a single parameter if makes you code cleaner.

 PowerShell

 $log = @{Path = '.\logfile.log'}
 Add-Content "logging this command" @log

<!-- p.314 -->

Splatting executables
Splatting also works on some executables that use a /param:value syntax. Robocopy.exe , for
example, has some parameters like this.

  PowerShell

  $robo = @{R=1;W=1;MT=8}
  robocopy source destination @robo

I don't know that this is all that useful, but I found it interesting.

Adding hashtables
Hashtables support the addition operator to combine two hashtables.

  PowerShell

  $person += @{Zip = '78701'}

This only works if the two hashtables don't share a key.

Nested hashtables
We can use hashtables as values inside a hashtable.

  PowerShell

  $person = @{
      name = 'Kevin'
      age = 36
  }
  $person.location = @{}
  $person.location.city = 'Austin'
  $person.location.state = 'TX'

I started with a basic hashtable containing two keys. I added a key called location with an empty
hashtable. Then I added the last two items to that location hashtable. We can do this all inline
too.

  PowerShell

  $person = @{
      name = 'Kevin'

<!-- p.315 -->

      age = 36
      location = @{
          city = 'Austin'
          state = 'TX'
      }
 }

This creates the same hashtable that we saw above and can access the properties the same way.

 PowerShell

 $person.location.city
 Austin

There are many ways to approach the structure of your objects. Here is a second way to look at a
nested hashtable.

 PowerShell

 $people = @{
     Kevin = @{
         age = 36
         city = 'Austin'
     }
     Alex = @{
         age = 9
         city = 'Austin'
     }
 }

This mixes the concept of using hashtables as a collection of objects and a collection of
properties. The values are still easy to access even when they're nested using whatever approach
you prefer.

 PowerShell

 PS> $people.kevin.age
 36
 PS> $people.kevin['city']
 Austin
 PS> $people['Alex'].age
 9
 PS> $people['Alex']['City']
 Austin

I tend to use the dot property when I'm treating it like a property. Those are generally things I've
defined statically in my code and I know them off the top of my head. If I need to walk the list or

<!-- p.316 -->

programmatically access the keys, I use the brackets to provide the key name.

 PowerShell

 foreach($name in $people.Keys)
 {
     $person = $people[$name]
     '{0}, age {1}, is in {2}' -f $name, $person.age, $person.city
 }

Having the ability to nest hashtables gives you a lot of flexibility and options.

Looking at nested hashtables
As soon as you start nesting hashtables, you're going to need an easy way to look at them from
the console. If I take that last hashtable, I get an output that looks like this and it only goes so
deep:

 PowerShell

 PS> $people
 Name                                 Value
 ----                                 -----
 Kevin                                {age, city}
 Alex                                 {age, city}

My go to command for looking at these things is ConvertTo-Json because it's very clean and I
frequently use JSON on other things.

 PowerShell

 PS> $people | ConvertTo-Json
 {
     "Kevin": {
                 "age": 36,
                 "city": "Austin"
             },
     "Alex": {
                 "age": 9,
                 "city": "Austin"
             }
 }

Even if you don't know JSON, you should be able to see what you're looking for. There's a
Format-Custom command for structured data like this but I still like the JSON view better.

<!-- p.317 -->

Creating objects
Sometimes you just need to have an object and using a hashtable to hold properties just isn't
getting the job done. Most commonly you want to see the keys as column names. A
pscustomobject makes that easy.

 PowerShell

 $person = [pscustomobject]@{
     name = 'Kevin'
     age = 36
 }

 $person

 name age
 ---- ---
 Kevin 36

Even if you don't create it as a pscustomobject initially, you can always cast it later when needed.

 PowerShell

 $person = @{
     name = 'Kevin'
     age = 36
 }

 [pscustomobject]$person

 name age
 ---- ---
 Kevin 36

I already have detailed write-up for pscustomobject that you should go read after this one. It
builds on a lot of the things learned here.

Reading and writing hashtables to file
Saving to CSV
Struggling with getting a hashtable to save to a CSV is one of the difficulties that I was referring
to above. Convert your hashtable to a pscustomobject and it will save correctly to CSV. It helps if
you start with a pscustomobject so the column order is preserved. But you can cast it to a
pscustomobject inline if needed.

<!-- p.318 -->

  PowerShell

  $person | ForEach-Object{ [pscustomobject]$_ } | Export-Csv -Path $path

Again, check out my write-up on using a pscustomobject.

Saving a nested hashtable to file
If I need to save a nested hashtable to a file and then read it back in again, I use the JSON
cmdlets to do it.

  PowerShell

  $people | ConvertTo-Json | Set-Content -Path $path
  $people = Get-Content -Path $path -Raw | ConvertFrom-Json

There are two important points about this method. First is that the JSON is written out multiline
so I need to use the -Raw option to read it back into a single string. The Second is that the
imported object is no longer a [hashtable] . It's now a [pscustomobject] and that can cause
issues if you don't expect it.

Watch for deeply-nested hashtables. When you convert it to JSON you might not get the results
you expect.

  PowerShell

  @{ a = @{ b = @{ c = @{ d = "e" }}}} | ConvertTo-Json

  {
      "a": {
        "b": {
          "c": "System.Collections.Hashtable"
        }
      }
  }

Use Depth parameter to ensure that you have expanded all the nested hashtables.

  PowerShell

  @{ a = @{ b = @{ c = @{ d = "e" }}}} | ConvertTo-Json -Depth 3

  {
      "a": {
        "b": {
          "c": {

<!-- p.319 -->

                  "d": "e"
              }
          }
      }
  }

If you need it to be a [hashtable] on import, then you need to use the Export-CliXml and
Import-CliXml commands.

Converting JSON to Hashtable
If you need to convert JSON to a [hashtable] , there's one way that I know of to do it with the
JavaScriptSerializer in .NET.

  PowerShell

  [Reflection.Assembly]::LoadWithPartialName("System.Web.Script.Serialization")
  $JSSerializer = [System.Web.Script.Serialization.JavaScriptSerializer]::new()
  $JSSerializer.Deserialize($json,'Hashtable')

Beginning in PowerShell v6, JSON support uses the NewtonSoft JSON.NET and adds hashtable
support.

  PowerShell

  '{ "a": "b" }' | ConvertFrom-Json -AsHashtable

  Name             Value
  ----             -----
  a                b

PowerShell 6.2 added the Depth parameter to ConvertFrom-Json . The default Depth is 1024.

Reading directly from a file
If you have a file that contains a hashtable using PowerShell syntax, there's a way to import it
directly.

  PowerShell

  $content = Get-Content -Path $Path -Raw -ErrorAction Stop
  $scriptBlock = [scriptblock]::Create( $content )
  $scriptBlock.CheckRestrictedLanguage( $allowedCommands, $allowedVariables, $true )
  $hashtable = ( & $scriptBlock )

<!-- p.320 -->

It imports the contents of the file into a scriptblock , then checks to make sure it doesn't have
any other PowerShell commands in it before it executes it.

On that note, did you know that a module manifest (the .psd1 file) is just a hashtable?

Keys can be any object
Most of the time, the keys are just strings. So we can put quotes around anything and make it a
key.

 PowerShell

 $person = @{
     'full name' = 'Kevin Marquette'
     '#' = 3978
 }
 $person['full name']

You can do some odd things that you may not have realized you could do.

 PowerShell

 $person.'full name'

 $key = 'full name'
 $person.$key

Just because you can do something, it doesn't mean that you should. That last one just looks like
a bug waiting to happen and would be easily misunderstood by anyone reading your code.

Technically your key doesn't have to be a string but they're easier to think about if you only use
strings. However, indexing doesn't work well with the complex keys.

 PowerShell

 $ht = @{ @(1,2,3) = "a" }
 $ht

 Name                               Value
 ----                               -----
 {1, 2, 3}                          a

Accessing a value in the hashtable by its key doesn't always work. For example:

 PowerShell
