---
title: "How to use this documentation — pages 1041-1080"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1041-1080
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1041-1080
family: powershell
documentKind: "doc"
abstract: "Creating a list of [int] is faster than creating a list of [Object] . PowerShell $Stopwatch = [System.Diagnostics.Stopwatch]::StartNew() $ListObject = [System.Collections.Generic.List[Object]]::new() for ($i = 0; $i -lt 1mb; $i++) { $ListObject.Add($i) } $Stopwatch.Stop() Write-"
---

# How to use this documentation — pages 1041-1080

<!-- p.1041 -->

Creating a list of [int] is faster than creating a list of [Object] .

 PowerShell
 $Stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
 $ListObject = [System.Collections.Generic.List[Object]]::new()
 for ($i = 0; $i -lt 1mb; $i++) {
     $ListObject.Add($i)
 }
 $Stopwatch.Stop()
 Write-Host "Time to add 1mb integers to List[Object]:
 $($Stopwatch.Elapsed.TotalSeconds) seconds."

 Output
 Time to add 1mb integers to List[Object]: 10.5677782 seconds.

String addition
Strings are immutable. Each addition to the string actually creates a new string big enough to
hold the contents of both the left and right operands, then copies the elements of both
operands into the new string. For small strings, this overhead may not matter. For large strings,
this can affect performance and memory consumption.

There are at least two alternatives:

     The -join operator concatenates strings
     The .NET [StringBuilder] class provides a mutable string

The following example compares the performance of these three methods of building a string.

 PowerShell
 $tests = @{
     'StringBuilder' = {
         $sb = [System.Text.StringBuilder]::new()
         foreach ($i in 0..$args[0]) {
             $sb = $sb.AppendLine("Iteration $i")
         }
         $sb.ToString()
     }
     'Join operator' = {
         $string = @(
             foreach ($i in 0..$args[0]) {
                 "Iteration $i"
             }
         ) -join "`n"
         $string

<!-- p.1042 -->

     }
     'Addition Assignment +=' = {
         $string = ''
         foreach ($i in 0..$args[0]) {
             $string += "Iteration $i`n"
         }
         $string
     }
 }

 10kb, 50kb, 100kb | ForEach-Object {
     $groupResult = foreach ($test in $tests.GetEnumerator()) {
         $ms = (Measure-Command { & $test.Value $_ }).TotalMilliseconds

          [pscustomobject]@{
              Iterations        = $_
              Test              = $test.Key
              TotalMilliseconds = [Math]::Round($ms, 2)
          }

          [GC]::Collect()
          [GC]::WaitForPendingFinalizers()
     }

     $groupResult = $groupResult | Sort-Object TotalMilliseconds
     $groupResult | Select-Object *, @{
         Name        = 'RelativeSpeed'
         Expression = {
              $relativeSpeed = $_.TotalMilliseconds /
 $groupResult[0].TotalMilliseconds
              [Math]::Round($relativeSpeed, 2).ToString() + 'x'
         }
     }
 }

These tests were run on a Windows 11 machine in PowerShell 7.4.2. The output shows that the
-join operator is the fastest, followed by the [StringBuilder] class.

 Output
 Iterations Test                   TotalMilliseconds RelativeSpeed
 ---------- ----                   ----------------- -------------
      10240 Join operator                      14.75 1x
      10240 StringBuilder                      62.44 4.23x
      10240 Addition Assignment +=            619.64 42.01x
      51200 Join operator                      43.15 1x
      51200 StringBuilder                     304.32 7.05x
      51200 Addition Assignment +=          14225.13 329.67x
     102400 Join operator                      85.62 1x
     102400 StringBuilder                     499.12 5.83x
     102400 Addition Assignment +=          67640.79 790.01x

<!-- p.1043 -->

The times and relative speeds can vary depending on the hardware, the version of PowerShell,
and the current workload on the system.

Processing large files
The idiomatic way to process a file in PowerShell might look something like:

 PowerShell
 Get-Content $path | Where-Object Length -GT 10

This can be an order of magnitude slower than using .NET APIs directly. For example, you can
use the .NET [StreamReader] class:

 PowerShell
 try {
     $reader = [System.IO.StreamReader]::new($path)
     while (-not $reader.EndOfStream) {
         $line = $reader.ReadLine()
         if ($line.Length -gt 10) {
             $line
         }
     }
 }
 finally {
     if ($reader) {
         $reader.Dispose()
     }
 }

You could also use the ReadLines method of [System.IO.File] , which wraps StreamReader ,
simplifies the reading process:

 PowerShell
 foreach ($line in [System.IO.File]::ReadLines($path)) {
     if ($line.Length -gt 10) {
         $line
     }
 }

Looking up entries by property in large collections
It's common to need to use a shared property to identify the same record in different
collections, like using a name to retrieve an ID from one list and an email from another.

<!-- p.1044 -->

Iterating over the first list to find the matching record in the second collection is slow. In
particular, the repeated filtering of the second collection has a large overhead.

Given two collections, one with an Id and Name, the other with Name and Email:

 PowerShell
 $Employees = 1..10000 | ForEach-Object {
     [pscustomobject]@{
         Id   = $_
         Name = "Name$_"
     }
 }

 $Accounts = 2500..7500 | ForEach-Object {
     [pscustomobject]@{
         Name = "Name$_"
         Email = "Name$_@fabrikam.com"
     }
 }

The usual way to reconcile these collections to return a list of objects with the Id, Name, and
Email properties might look like this:

 PowerShell
 $Results = $Employees | ForEach-Object -Process {
     $Employee = $_

      $Account = $Accounts | Where-Object -FilterScript {
          $_.Name -eq $Employee.Name
      }

      [pscustomobject]@{
          Id    = $Employee.Id
          Name = $Employee.Name
          Email = $Account.Email
      }
 }

However, that implementation has to filter all 5000 items in the $Accounts collection once for
every item in the $Employee collection. That can take minutes, even for this single-value lookup.

Instead, you can make a Hash Table that uses the shared Name property as a key and the
matching account as the value.

 PowerShell
 $LookupHash = @{}
 foreach ($Account in $Accounts) {

<!-- p.1045 -->

      $LookupHash[$Account.Name] = $Account
 }

Looking up keys in a hash table is much faster than filtering a collection by property values.
Instead of checking every item in the collection, PowerShell can check if the key is defined and
use its value.

 PowerShell
 $Results = $Employees | ForEach-Object -Process {
     $Email = $LookupHash[$_.Name].Email
     [pscustomobject]@{
         Id    = $_.Id
         Name = $_.Name
         Email = $Email
     }
 }

This is much faster. While the looping filter took minutes to complete, the hash lookup takes
less than a second.

Use Write-Host carefully
The Write-Host command should only be used when you need to write formatted text to the
host console, rather than writing objects to the Success pipeline.

Write-Host can be an order of magnitude slower than [Console]::WriteLine() for specific

hosts like pwsh.exe , powershell.exe , or powershell_ise.exe . However, [Console]::WriteLine()
isn't guaranteed to work in all hosts. Also, output written using [Console]::WriteLine()
doesn't get written to transcripts started by Start-Transcript .

JIT compilation
PowerShell compiles the script code to bytecode that's interpreted. Beginning in PowerShell 3,
for code that's repeatedly executed in a loop, PowerShell can improve performance by Just-in-
time (JIT) compiling the code into native code.

Loops that have fewer than 300 instructions are eligible for JIT-compilation. Loops larger than
that are too costly to compile. When the loop has executed 16 times, the script is JIT-compiled
in the background. When the JIT-compilation completes, execution is transferred to the
compiled code.

Avoid repeated calls to a function

<!-- p.1046 -->

Calling a function can be an expensive operation. If you're calling a function in a long running
tight loop, consider moving the loop inside the function.

Consider the following examples:

 PowerShell
 $tests = @{
     'Simple for-loop'       = {
         param([int] $RepeatCount, [random] $RanGen)

          for ($i = 0; $i -lt $RepeatCount; $i++) {
              $null = $RanGen.Next()
          }
     }
     'Wrapped in a function' = {
         param([int] $RepeatCount, [random] $RanGen)

          function Get-RandomNumberCore {
              param ($Rng)

              $Rng.Next()
          }

          for ($i = 0; $i -lt $RepeatCount; $i++) {
              $null = Get-RandomNumberCore -Rng $RanGen
          }
     }
     'for-loop in a function' = {
         param([int] $RepeatCount, [random] $RanGen)

          function Get-RandomNumberAll {
              param ($Rng, $Count)

              for ($i = 0; $i -lt $Count; $i++) {
                  $null = $Rng.Next()
              }
          }

          Get-RandomNumberAll -Rng $RanGen -Count $RepeatCount
     }
 }

 5kb, 10kb, 100kb | ForEach-Object {
     $Rng = [random]::new()
     $groupResult = foreach ($test in $tests.GetEnumerator()) {
         $ms = Measure-Command { & $test.Value -RepeatCount $_ -RanGen $Rng }

          [pscustomobject]@{
              CollectionSize    = $_
              Test              = $test.Key
              TotalMilliseconds = [Math]::Round($ms.TotalMilliseconds,2)
          }

<!-- p.1047 -->

           [GC]::Collect()
           [GC]::WaitForPendingFinalizers()
      }

     $groupResult = $groupResult | Sort-Object TotalMilliseconds
     $groupResult | Select-Object *, @{
         Name        = 'RelativeSpeed'
         Expression = {
              $relativeSpeed = $_.TotalMilliseconds /
 $groupResult[0].TotalMilliseconds
              [Math]::Round($relativeSpeed, 2).ToString() + 'x'
         }
     }
 }

The Basic for-loop example is the base line for performance. The second example wraps the
random number generator in a function that's called in a tight loop. The third example moves
the loop inside the function. The function is only called once but the code still generates the
same amount of random numbers. Notice the difference in execution times for each example.

 Output
 CollectionSize Test                   TotalMilliseconds RelativeSpeed
 -------------- ----                   ----------------- -------------
           5120 for-loop in a function              9.62 1x
           5120 Simple for-loop                    10.55 1.1x
           5120 Wrapped in a function              62.39 6.49x
          10240 Simple for-loop                    17.79 1x
          10240 for-loop in a function             18.48 1.04x
          10240 Wrapped in a function             127.39 7.16x
         102400 for-loop in a function            179.19 1x
         102400 Simple for-loop                   181.58 1.01x
         102400 Wrapped in a function            1155.57 6.45x

Avoid wrapping cmdlet pipelines
Most cmdlets are implemented for the pipeline, which is a sequential syntax and process. For
example:

 PowerShell

 cmdlet1 | cmdlet2 | cmdlet3

Initializing a new pipeline can be expensive, therefore you should avoid wrapping a cmdlet
pipeline into another existing pipeline.

<!-- p.1048 -->

Consider the following example. The Input.csv file contains 2100 lines. The Export-Csv
command is wrapped inside the ForEach-Object pipeline. The Export-Csv cmdlet is invoked for
every iteration of the ForEach-Object loop.

 PowerShell
 $measure = Measure-Command -Expression {
     Import-Csv .\Input.csv | ForEach-Object -Begin { $Id = 1 } -Process {
         [pscustomobject]@{
             Id   = $Id
             Name = $_.opened_by
         } | Export-Csv .\Output1.csv -Append
     }
 }

 'Wrapped = {0:N2} ms' -f $measure.TotalMilliseconds

 Output
 Wrapped = 15,968.78 ms

For the next example, the Export-Csv command was moved outside of the ForEach-Object
pipeline. In this case, Export-Csv is invoked only once, but still processes all objects passed out
of ForEach-Object .

 PowerShell
 $measure = Measure-Command -Expression {
     Import-Csv .\Input.csv | ForEach-Object -Begin { $Id = 2 } -Process {
         [pscustomobject]@{
             Id   = $Id
             Name = $_.opened_by
         }
     } | Export-Csv .\Output2.csv
 }

 'Unwrapped = {0:N2} ms' -f $measure.TotalMilliseconds

 Output
 Unwrapped = 42.92 ms

The unwrapped example is 372 times faster. Also, notice that the first implementation requires
the Append parameter, which isn't required for the later implementation.

Avoid unnecessary collection enumeration

<!-- p.1049 -->

The PowerShell comparison operators have a convience feature when comparing collections.
When the left-hand value in the expression is a collection, the operator returns the elements of
the collection that match the right-hand value of the expression.

This feature provides a simple way to filter a collection. For example:

 PowerShell
 PS> $Collection = 1..99
 PS> ($Collection -like '*1*') -join ' '

 1 10 11 12 13 14 15 16 17 18 19 21 31 41 51 61 71 81 91

However, when you use a collection comparison in a conditional statement that only expects a
boolean result, this feature can result in poor performance.

Take for example:

 PowerShell
 if ($Collection -like '*1*') { 'Found' }

In this example, PowerShell compares the right-hand value to every value in the collection and
returns a collection of results. Since the result isn't empty, the non-null result evaluates as
$true . The condition is true when the first match is found, but PowerShell still enumerates the

entire collection. This enumeration can have a significant performance impact for large
collections.

One way to improve performance is to use the Where() method of the collection. The Where()
method stops evaluating the collection after it finds the first match.

 PowerShell
 # Create an array of 1048576 items
 $Collection = foreach ($x in 1..1MB) { $x }
 (Measure-Command { if ($Collection -like '*1*') { 'Found' } }).TotalMilliseconds
 633.3695
 (Measure-Command { if ($Collection.Where({ $_ -like '*1*' }, 'first')) { 'Found' }
 }).TotalMilliseconds
 2.607

For a million items, using the Where() method is significantly faster.

Object creation

<!-- p.1050 -->

Creating objects using the New-Object cmdlet can be slow. The following code compares the
performance of creating objects using the New-Object cmdlet to the [pscustomobject] type
accelerator.

 PowerShell
 Measure-Command {
     $test = 'PSCustomObject'
     for ($i = 0; $i -lt 100000; $i++) {
         $resultObject = [pscustomobject]@{
             Name = 'Name'
             Path = 'FullName'
         }
     }
 } | Select-Object @{n='Test';e={$test}},TotalSeconds

 Measure-Command {
     $test = 'New-Object'
     for ($i = 0; $i -lt 100000; $i++) {
         $resultObject = New-Object -TypeName psobject -Property @{
             Name = 'Name'
             Path = 'FullName'
         }
     }
 } | Select-Object @{n='Test';e={$test}},TotalSeconds

 Output
 Test           TotalSeconds
 ----           ------------
 PSCustomObject         0.48
 New-Object             3.37

PowerShell 5.0 added the new() static method for all .NET types. The following code compares
the performance of creating objects using the New-Object cmdlet to the new() method.

 PowerShell
 Measure-Command {
     $test = 'new() method'
     for ($i = 0; $i -lt 100000; $i++) {
         $sb = [System.Text.StringBuilder]::new(1000)
     }
 } | Select-Object @{n='Test';e={$test}},TotalSeconds

 Measure-Command {
     $test = 'New-Object'
     for ($i = 0; $i -lt 100000; $i++) {
         $sb = New-Object -TypeName System.Text.StringBuilder -ArgumentList 1000

<!-- p.1051 -->

     }
 } | Select-Object @{n='Test';e={$test}},TotalSeconds

 Output
 Test         TotalSeconds
 ----         ------------
 new() method         0.59
 New-Object           3.17

Use OrderedDictionary to dynamically create new
objects
There are situations where we may need to dynamically create objects based on some input,
the perhaps most commonly used way to create a new PSObject and then add new properties
using the Add-Member cmdlet. The performance cost for small collections using this technique
may be negligible however it can become very noticeable for big collections. In that case, the
recommended approach is to use an [OrderedDictionary] and then convert it to a PSObject
using the [pscustomobject] type accelerator. For more information, see the Creating ordered
dictionaries section of about_Hash_Tables.

Assume you have the following API response stored in the variable $json .

 JSON
 {
     "tables": [
       {
         "name": "PrimaryResult",
         "columns": [
           { "name": "Type", "type": "string" },
           { "name": "TenantId", "type": "string" },
           { "name": "count_", "type": "long" }
         ],
         "rows": [
           [ "Usage", "63613592-b6f7-4c3d-a390-22ba13102111", "1" ],
           [ "Usage", "d436f322-a9f4-4aad-9a7d-271fbf66001c", "1" ],
           [ "BillingFact", "63613592-b6f7-4c3d-a390-22ba13102111", "1" ],
           [ "BillingFact", "d436f322-a9f4-4aad-9a7d-271fbf66001c", "1" ],
           [ "Operation", "63613592-b6f7-4c3d-a390-22ba13102111", "7" ],
           [ "Operation", "d436f322-a9f4-4aad-9a7d-271fbf66001c", "5" ]
         ]
       }
     ]
 }

<!-- p.1052 -->

Now, suppose you want to export this data to a CSV. First you need to create new objects and
add the properties and values using the Add-Member cmdlet.

 PowerShell
 $data = $json | ConvertFrom-Json
 $columns = $data.tables.columns
 $result = foreach ($row in $data.tables.rows) {
     $obj = [psobject]::new()
     $index = 0

     foreach ($column in $columns) {
         $obj | Add-Member -MemberType NoteProperty -Name $column.name -Value
 $row[$index++]
     }

     $obj
 }

Using an OrderedDictionary , the code can be translated to:

 PowerShell
 $data = $json | ConvertFrom-Json
 $columns = $data.tables.columns
 $result = foreach ($row in $data.tables.rows) {
     $obj = [ordered]@{}
     $index = 0

     foreach ($column in $columns) {
         $obj[$column.name] = $row[$index++]
     }

     [pscustomobject] $obj
 }

In both cases the $result output would be same:

 Output
 Type        TenantId                             count_
 ----        --------                             ------
 Usage       63613592-b6f7-4c3d-a390-22ba13102111 1
 Usage       d436f322-a9f4-4aad-9a7d-271fbf66001c 1
 BillingFact 63613592-b6f7-4c3d-a390-22ba13102111 1
 BillingFact d436f322-a9f4-4aad-9a7d-271fbf66001c 1
 Operation   63613592-b6f7-4c3d-a390-22ba13102111 7
 Operation   d436f322-a9f4-4aad-9a7d-271fbf66001c 5

<!-- p.1053 -->

The latter approach becomes exponentially more efficient as the number of objects and
member properties increases.

Here is a performance comparison of three techniques for creating objects with 5 properties:

 PowerShell
 $tests = @{
     '[ordered] into [pscustomobject] cast' = {
         param([int] $Iterations, [string[]] $Props)

          foreach ($i in 1..$Iterations) {
              $obj = [ordered]@{}
              foreach ($prop in $Props) {
                  $obj[$prop] = $i
              }
              [pscustomobject] $obj
          }
     }
     'Add-Member'                           = {
         param([int] $Iterations, [string[]] $Props)

          foreach ($i in 1..$Iterations) {
              $obj = [psobject]::new()
              foreach ($prop in $Props) {
                  $obj | Add-Member -MemberType NoteProperty -Name $prop -Value $i
              }
              $obj
          }
     }
     'PSObject.Properties.Add'              = {
         param([int] $Iterations, [string[]] $Props)

          # this is how, behind the scenes, `Add-Member` attaches
          # new properties to our PSObject.
          # Worth having it here for performance comparison

          foreach ($i in 1..$Iterations) {
              $obj = [psobject]::new()
              foreach ($prop in $Props) {
                  $obj.psobject.Properties.Add(
                      [psnoteproperty]::new($prop, $i))
              }
              $obj
          }
     }
 }

 $properties = 'Prop1', 'Prop2', 'Prop3', 'Prop4', 'Prop5'

 1kb, 10kb, 100kb | ForEach-Object {
     $groupResult = foreach ($test in $tests.GetEnumerator()) {
         $ms = Measure-Command { & $test.Value -Iterations $_ -Props $properties }

<!-- p.1054 -->

          [pscustomobject]@{
              Iterations        = $_
              Test              = $test.Key
              TotalMilliseconds = [Math]::Round($ms.TotalMilliseconds, 2)
          }

          [GC]::Collect()
          [GC]::WaitForPendingFinalizers()
     }

     $groupResult = $groupResult | Sort-Object TotalMilliseconds
     $groupResult | Select-Object *, @{
         Name        = 'RelativeSpeed'
         Expression = {
              $relativeSpeed = $_.TotalMilliseconds /
 $groupResult[0].TotalMilliseconds
              [Math]::Round($relativeSpeed, 2).ToString() + 'x'
         }
     }
 }

And these are the results:

 Output
 Iterations Test                                 TotalMilliseconds RelativeSpeed
 ---------- ----                                 ----------------- -------------
       1024 [ordered] into [pscustomobject] cast             22.00 1x
       1024 PSObject.Properties.Add                         153.17 6.96x
       1024 Add-Member                                      261.96 11.91x
      10240 [ordered] into [pscustomobject] cast             65.24 1x
      10240 PSObject.Properties.Add                        1293.07 19.82x
      10240 Add-Member                                     2203.03 33.77x
     102400 [ordered] into [pscustomobject] cast            639.83 1x
     102400 PSObject.Properties.Add                       13914.67 21.75x
     102400 Add-Member                                    23496.08 36.72x

Related links
     $null
     System.Void
     Out-Null
     List<T>
     Add(T) method
     System.String
     System.Int32
     System.Object

<!-- p.1055 -->

     ToArray() method
     System.Collections.ArrayList
     System.Text.StringBuilder
     System.IO.StreamReader
     File::ReadLines() method
     Write-Host
     Add-Member

Last updated on 01/21/2026

<!-- p.1056 -->

PowerShell module authoring
considerations
This document includes some guidelines related to how a module is authored for best
performance.

Module Manifest Authoring
A module manifest that doesn't use the following guidelines can have a noticeable impact on
general PowerShell performance even if the module isn't used in a session.

Command auto-discovery analyzes each module to determine which commands the module
exports and this analysis can be expensive. The results of module analysis are cached per user,
but the cache isn't available on first run, which is a typical scenario with containers. During
module analysis, if the exported commands can be fully determined from the manifest, more
expensive analysis of the module can be avoided.

Guidelines
      In the module manifest, don't use wildcards in the AliasesToExport , CmdletsToExport , and
      FunctionsToExport entries.

      If the module doesn't export commands of a particular type, specify this explicitly in the
      manifest by specifying @() . A missing or $null entry is equivalent to specifying the
      wildcard * .

The following should be avoided where possible:

 PowerShell

 @{
      FunctionsToExport = '*'

      # Also avoid omitting an entry, it's equivalent to using a wildcard
      # CmdletsToExport = '*'
      # AliasesToExport = '*'
 }

Instead, use:

 PowerShell

<!-- p.1057 -->

 @{
      FunctionsToExport = 'Format-Hex', 'Format-Octal'
      CmdletsToExport = @() # Specify an empty array, not $null
      AliasesToExport = @() # Also ensure all three entries are present
 }

Avoid CDXML
When deciding how to implement your module, there are three primary choices:

      Binary (usually C#)
      Script (PowerShell)
      CDXML (an XML file wrapping CIM)

If the speed of loading your module is important, CDXML is roughly an order of magnitude
slower than a binary module.

A binary module loads the fastest because it's compiled ahead of time and can use NGen to JIT
compile once per machine.

A script module typically loads a bit more slowly than a binary module because PowerShell
must parse the script before compiling and executing it.

A CDXML module is typically much slower than a script module because it must first parse an
XML file which then generates quite a bit of PowerShell script that's then parsed and compiled.

Last updated on 12/08/2025

<!-- p.1058 -->

Optimize performance using
parallel execution
PowerShell provides several options for the creation of parallel invocations.

     Start-Job runs each job in a separate process, each with a new instance of PowerShell. In

     many cases, a linear loop is faster. Also, serialization and deserialization can limit the
     usefulness of the objects returned. This command is built in to all versions of PowerShell.
     Start-ThreadJob is a cmdlet found in the ThreadJob module. This command uses

     PowerShell runspaces to create and manage thread-based jobs. These jobs are lighter-
     weight than the jobs created by Start-Job and avoid potential loss of type fidelity required
     by cross-process serialization and deserialization. The ThreadJob module comes with
     PowerShell 7 and higher. For Windows PowerShell 5.1, you can install this module from the
     PowerShell Gallery.
     Use the System.Management.Automation.Runspaces namespace from the PowerShell SDK
     to create your own parallel logic. Both ForEach-Object -Parallel and Start-ThreadJob use
     PowerShell runspaces to execute the code in parallel.
     Workflows are a feature of Windows PowerShell 5.1. Workflows aren't available in
     PowerShell 7.0 and higher. Workflows are a special type of PowerShell script that can run in
     parallel. They're designed for long-running tasks and can be paused and resumed.
     Workflows aren't recommended for new development. For more information, see
     about_Workflows.
     ForEach-Object -Parallel is a feature of PowerShell 7.0 and higher. Like Start-ThreadJob , it

     uses PowerShell runspaces to create and manage thread-based jobs. This command is
     designed for use in a pipeline.

Limit execution concurrency
Running scripts in parallel doesn't guarantee improved performance. For example, the following
scenarios can benefit from parallel execution:

     Compute intensive scripts on multi-threaded multi-core processors
     Scripts that spend time waiting for results or doing file operations, as long as those
     operations don't block each other.

<!-- p.1059 -->

It's important to balance the overhead of parallel execution with the type of work done. Also,
there are limits to the number of invocations that can run in parallel.

The Start-ThreadJob and ForEach-Object -Parallel commands have a ThrottleLimit parameter
to limit the number of jobs running at one time. As more jobs are started, they're queued and
wait until the current number of jobs drops below the throttle limit. As of PowerShell 7.1,
ForEach-Object -Parallel reuses runspaces from a runspace pool by default. The ThrottleLimit

parameter sets the runspace pool size. The default runspace pool size is 5. You can still create a
new runspace for each iteration using the UseNewRunspace switch.

The Start-Job command doesn't have a ThrottleLimit parameter. You have to manage the
number of jobs running at one time.

Measure performance
The following function, Measure-Parallel , compares the speed of the following parallel execution
approaches:

      Start-Job - creates a child PowerShell process behind the scenes

      Start-ThreadJob - runs each job in a separate thread

      ForEach-Object -Parallel - runs each job in a separate thread

      Start-Process - invokes an external program asynchronously

        ７ Note

        This approach only makes sense if your parallel tasks only consist of a single call to an
        external program, as opposed to running a block of PowerShell code. Also, the only
        way to capture output with this approach is by redirecting to a file.

 PowerShell

 function Measure-Parallel {
     [CmdletBinding()]
     param(
         [ValidateRange(2, 2147483647)]
         [int] $BatchSize = 5,

           [ValidateSet('Job', 'ThreadJob', 'Process', 'ForEachParallel', 'All')]
           [string[]] $Approach,

<!-- p.1060 -->

        # pass a higher count to run multiple batches
        [ValidateRange(2, 2147483647)]
        [int] $JobCount = $BatchSize
    )

    $noForEachParallel = $PSVersionTable.PSVersion.Major -lt 7
    $noStartThreadJob = -not (Get-Command -ErrorAction Ignore Start-ThreadJob)

    # Translate the approach arguments into their corresponding hashtable keys (see
below).
    if ('All' -eq $Approach) { $Approach = 'Job', 'ThreadJob', 'Process',
'ForEachParallel' }
    $approaches = $Approach.ForEach({
            if ($_ -eq 'ForEachParallel') { 'ForEach-Object -Parallel' }
            else { $_ -replace '^', 'Start-' }
        })

    if ($noStartThreadJob) {
        if ($interactive -or $approaches -contains 'Start-ThreadJob') {
            Write-Warning "Start-ThreadJob is not installed, omitting its test."
            $approaches = $approaches.Where({ $_ -ne 'Start-ThreadJob' })
        }
    }
    if ($noForEachParallel) {
        if ($interactive -or $approaches -contains 'ForEach-Object -Parallel') {
            Write-Warning 'ForEach-Object -Parallel require PowerShell v7+, omitting
its test.'
            $approaches = $approaches.Where({ $_ -ne 'ForEach-Object -Parallel' })
        }
    }

    # Simulated input: Create 'f0.zip', 'f1'.zip', ... file names.
    $zipFiles = 0..($JobCount - 1) -replace '^', 'f' -replace '$', '.zip'

    # Sample executables to run - here, the native shell is called to simply
    # echo the argument given.
    $exe = if ($env:OS -eq 'Windows_NT') { 'cmd.exe' } else { 'sh' }

    # The list of its arguments *as a single string* - use '{0}' as the placeholder
    # for where the input object should go.
    $exeArgList = if ($env:OS -eq 'Windows_NT') {
         '/c "echo {0} > NUL:"'
      } else {
         '-c "echo {0} > /dev/null"'
    }

    # A hashtable with script blocks that implement the 3 approaches to parallelism.
    $approachImpl = [ordered] @{}

    # child-process-based job
    $approachImpl['Start-Job'] = {
        param([array] $batch)
        $batch |
            ForEach-Object {
                Start-Job {

<!-- p.1061 -->

                    Invoke-Expression ($using:exe + ' ' + ($using:exeArgList -f
$args[0]))
                } -ArgumentList $_
             } |
             Receive-Job -Wait -AutoRemoveJob | Out-Null
    }

    # thread-based job - requires the ThreadJob module
    if (-not $noStartThreadJob) {
        # If Start-ThreadJob is available, add an approach for it.
        $approachImpl['Start-ThreadJob'] = {
            param([array] $batch)
            $batch |
                ForEach-Object {
                    Start-ThreadJob -ThrottleLimit $BatchSize {
                        Invoke-Expression ($using:exe + ' ' + ($using:exeArgList -f
$args[0]))
                    } -ArgumentList $_
                } |
                Receive-Job -Wait -AutoRemoveJob | Out-Null
        }
    }

    # ForEach-Object -Parallel job
    if (-not $noForEachParallel) {
        $approachImpl['ForEach-Object -Parallel'] = {
            param([array] $batch)
            $batch | ForEach-Object -ThrottleLimit $BatchSize -Parallel {
                Invoke-Expression ($using:exe + ' ' + ($using:exeArgList -f $_))
            }
        }
    }

    # direct execution of an external program
    $approachImpl['Start-Process'] = {
        param([array] $batch)
        $batch |
            ForEach-Object {
                Start-Process -NoNewWindow -PassThru $exe -ArgumentList ($exeArgList
-f $_)
            } |
            Wait-Process
    }

    # Partition the array of all indices into subarrays (batches)
    $batches = @(
        0..([math]::Ceiling($zipFiles.Count / $batchSize) - 1) | ForEach-Object {
            , $zipFiles[($_ * $batchSize)..($_ * $batchSize + $batchSize - 1)]
        }
    )

    $tsTotals = foreach ($appr in $approaches) {
        $i = 0
        $tsTotal = [timespan] 0
        $batches | ForEach-Object {

<!-- p.1062 -->

               Write-Verbose "$batchSize-element '$appr' batch"
               $ts = Measure-Command { & $approachImpl[$appr] $_ | Out-Null }
               $tsTotal += $ts
               if (++$i -eq $batches.Count) {
                   # last batch processed.
                   if ($batches.Count -gt 1) {
                       Write-Verbose ("'$appr' processing $JobCount items finished in "
 +
                            "$($tsTotal.TotalSeconds.ToString('N2')) secs.")
                   }
                   $tsTotal # output the overall timing for this approach
               }
          }
      }

      # Output a result object with the overall timings.
      $oht = [ordered] @{}
      $oht['JobCount'] = $JobCount
      $oht['BatchSize'] = $BatchSize
      $oht['BatchCount'] = $batches.Count
      $i = 0
      foreach ($appr in $approaches) {
          $oht[($appr + ' (secs.)')] = $tsTotals[$i++].TotalSeconds.ToString('N2')
      }
      [pscustomobject] $oht
 }

The following example uses Measure-Parallel to run 20 jobs in parallel, 5 at a time, using all
available approaches.

 PowerShell

 Measure-Parallel -Approach All -BatchSize 5 -JobCount 20 -Verbose

The following output comes from a Windows computer running PowerShell 7.5.1. Your timing can
vary based on many factors, but the ratios should provide a sense of relative performance.

 Output

 VERBOSE: 5-element 'Start-Job' batch
 VERBOSE: 5-element 'Start-Job' batch
 VERBOSE: 5-element 'Start-Job' batch
 VERBOSE: 5-element 'Start-Job' batch
 VERBOSE: 'Start-Job' processing 20 items finished in 7.58 secs.
 VERBOSE: 5-element 'Start-ThreadJob' batch
 VERBOSE: 5-element 'Start-ThreadJob' batch
 VERBOSE: 5-element 'Start-ThreadJob' batch
 VERBOSE: 5-element 'Start-ThreadJob' batch
 VERBOSE: 'Start-ThreadJob' processing 20 items finished in 2.37 secs.
 VERBOSE: 5-element 'Start-Process' batch
 VERBOSE: 5-element 'Start-Process' batch

<!-- p.1063 -->

  VERBOSE: 5-element 'Start-Process' batch
  VERBOSE: 5-element 'Start-Process' batch
  VERBOSE: 'Start-Process' processing 20 items finished in 0.26 secs.
  VERBOSE: 5-element 'ForEach-Object -Parallel' batch
  VERBOSE: 5-element 'ForEach-Object -Parallel' batch
  VERBOSE: 5-element 'ForEach-Object -Parallel' batch
  VERBOSE: 5-element 'ForEach-Object -Parallel' batch
  VERBOSE: 'ForEach-Object -Parallel' processing 20 items finished in 0.79 secs.

  JobCount                         : 20
  BatchSize                        : 5
  BatchCount                       : 4
  Start-Job (secs.)                : 7.58
  Start-ThreadJob (secs.)          : 2.37
  Start-Process (secs.)            : 0.26
  ForEach-Object -Parallel (secs.) : 0.79

Conclusions

      The Start-Process approach performs best because it doesn't have the overhead of job
      management. However, as previously noted, this approach has fundamental limitations.
      The ForEach-Object -Parallel adds the least overhead, followed by Start-ThreadJob .
      Start-Job has the most overhead because of the hidden PowerShell instances it creates for

      each job.

Acknowledgments
Much of the information is this article is based on the answers from Santiago Squarzon   and
mklement0       in this Stack Overflow post   .

You might also be interested in the PSParallelPipeline   module created by Santiago Squarzon.

Further reading
      Start-Job
      about_Jobs
      Start-ThreadJob
      ForEach-Object
      Start-Process

 Last updated on 04/21/2026

<!-- p.1064 -->

Troubleshoot PowerShell startup issues
Sometimes, PowerShell can have problems before it's even ready to use. Startup issues can be
difficult to troubleshoot, especially when you want to use PowerShell to help. There are three
main phases of startup:

   1. Process creation
   2. PowerShell SessionState initialization
   3. Profile processing

The most common problems include:

     Long startup time or slow performance
     Errors
     Crashes

The steps of the startup sequence
It's helpful to understand the steps PowerShell goes through during startup. This way, you can
narrow down where the issue is happening.

Step 1: Process creation
The process creation has a few steps:

   1. Create a Host window

     On Windows, the Host can be Windows Terminal, the Windows Console Host, Visual
     Studio Code, or any other hosting application. Problems that occur here are usually
     unrelated to PowerShell, but also extremely rare.

   2. Start the process host process

     Problems that occur here are usually caused by a corrupted executable or an issue in the
     operating system.

   3. Prepare .NET

     PowerShell is .NET-based and that needs to fully load. Depending on which PowerShell
     version you are trying to start, you either get the full, Windows-integrated .NET
     Framework with Windows PowerShell 5.1 or the newer .NET included in PowerShell 7.

     During first-time startup of PowerShell, PowerShell and .NET run optimization tasks. This
     optimization task is only run once, during the first startup after installation, upgrade, or if

<!-- p.1065 -->

     the cache is empty. Startup will take longer during this first-time optimization. Failure
     during optimization can create a corrupted cache. A corrupted PowerShell cache can
     cause issues with command discovery and module loading.

Step 2: PowerShell SessionState initialization
Loading the PowerShell binaries and initializing the engine involves processing the PowerShell
configuration and some cached data.

   1. Process configuration files: powershell.config.json and PSSession configuration files
     used by JEA and other remoting scenarios. These files may contain settings that can affect
     the language mode, available commands and modules, and some policy settings.
   2. Check Group Policies and Windows Security policies. Windows Group Policies can
     override settings in the powershell.config.json . Security Policies can enable features like
     WDAC (Windows Defender Application Control), which can also constrain the language
     mode available.
   3. Load the default modules (Microsoft.PowerShell.Core and PSReadLine) and any modules
     and assemblies defined in the PSSession configuration.

For more information about PowerShell security features, see the following articles:

     PowerShell security features
     about_Language_Modes

Step 3: Profile processing
Finally, PowerShell runs the available profile files. Profile scripts are run in the following order:

   1. All Hosts All Users
   2. Current Host All Users
   3. All Hosts Current User
   4. Current Host Current User

  ７ Note

  Profile scripts aren't run for remote sessions.

For more information about profiles, see about_Profiles.

Narrow the scope of the issue

<!-- p.1066 -->

It's helpful to remove variables and narrow down the specific scope of where the issue
happens. The easiest variable to eliminate is the profile. The profile often contains custom
code, especially in the user-specific profile scripts.

Try running PowerShell with the profile disabled:

 PowerShell
 # PS 5.1:
 powershell -NoProfile

 # PS 7.*:
 pwsh -NoProfile

Next you should see if the problem is version-specific. Try running your profile in both
Windows PowerShell 5.1 and PowerShell 7. Windows PowerShell and PowerShell 7 store the
profile in different locations. Your profile may not be the same for both versions. Compare the
files to understand the differences. You can try installing your PowerShell profile in Windows
PowerShell 5.1. However, be aware that some PowerShell 7 commands and modules aren't
compatible with Windows PowerShell 5.1.

You can test your PowerShell 7 profile in Windows PowerShell 5.1 without overwriting your
existing profile.

   1. Start Windows PowerShell 5.1 with the profile disabled.

   2. Manually dot-source your PowerShell 7 profile file into the Windows PowerShell 5.1
      session.

       PowerShell
       . $env:USERPROFILE\Documents\PowerShell\Microsoft.PowerShell_profile.ps1

   3. Observe whether the issue occurs.

If the issue persists, then you know problem is an environmental issue outside of the profile.

Try running the profile on a different device. If the profile works correctly on another device,
then you know the issue is specific to your original device.

Troubleshoot common environmental problems

Crashes during startup

<!-- p.1067 -->

If the PowerShell console crashes during startup, especially early and with no feedback, you
could have a corrupted process cache. This is a rare condition that you can resolve by clearing
the cache. There are two cache locations that can be cleared:

     User Cache: $env:LOCALAPPDATA\Microsoft\Windows\Caches
     System Cache:
      $env:windir\System32\Config\SystemProfile\AppData\Local\Microsoft\Windows\Caches

Delete the contents of the user cache folder first, then try starting PowerShell again. If the
problem persists, delete the contents of the system cache and try again.

You may also need to delete the PowerShell analysis cache. You can find the cache files in the
following locations:

     Windows PowerShell:
      $env:windir\System32\Config\SystemProfile\AppData\Local\Microsoft\Windows\PowerShell

     PowerShell 7: $env:LOCALAPPDATA\Microsoft\PowerShell

Delete only the following file patterns:

      ModuleAnalysisCache-*

      StartupProfileData-*

The cached data is recreated the next time you start PowerShell.

If the problem persists in Windows PowerShell 5.1, you may need to repair the .NET Framework
installation. For more information, see Repair the .NET Framework.

Troubleshoot common profile problems
This section describes some common problems that can occur during PowerShell startup, and
how to troubleshoot them.

Profile takes too long to run
First you must define what's "too long." PowerShell is only doing what the scripts tell it to do.
Check all profile paths. There may be multiple profile scripts being run. Review the code to
understand it's trying to do.

     Determine where the delay occurs

     If there are profile scripts for the AllUsers scope, you might not be able to edit those files.
     Work with your system administrator to review those files. For the CurrentUser scope

<!-- p.1068 -->

   profile scripts, edit those files to add timing messages to help you find where the delay
   occurs. For example, you can add the following line at various points in your profile script.

    PowerShell

    Write-Host "$(Get-Date -Format 'HH:mm:ss.fff') | Profile: Step X"

   Reduce dependencies

   Reduce the number of modules that need to be loaded to execute your profile. Run Get-
   Module after profile runs to see the modules that were loaded during startup. By default,

   PowerShell loads the Microsoft.PowerShell.Core and PSReadLine modules. Any additional
   modules were loaded by your profile scripts.

   Modules can be loaded explicitly by using Import-Module or implicitly by using
   commands defined in those modules. Consider whether you need a command or a
   module loaded during startup.

   Avoid installing modules in a redirected folder

   In many situations on Windows, your Documents folder can be redirected to a network file
   share or to OneDrive. Network file access can be slow, especially if the network is
   congested or the server is under heavy load. Depending on how OneDrive is configured,
   it can also introduce delays or cause errors during profile exectution.

   You have a few options to mitigate this problem:
     Don't redirect your Documents folder, but that might not be desired
     Configure your Modules folder in OneDrive to always be kept on disk. This prevents
     errors and delayed load times.
     Install modules in the AllUsers scope, which is outside of the user profile folder.

   Measure the actual performance

   If you don't know how long your profile takes to run, you can't determine whether it's too
   long. The Measure-Command cmdlet can show how long a command or script block takes to
   run.

   Steve Lee, the PowerShell Dev Manager, has a blog post that describes how to measure
   the performance of your profile. It includes instructions for establishing a baseline for
   performance, how to get detailed timing information, and ways to optimize your profile.
   See Optimizing your $Profile    .

PowerShell 7 starts slowly in an isolated network

<!-- p.1069 -->

In this scenario, your Windows computer is on a network that's not connected to the internet.
For interactive PowerShell sessions, PowerShell loads the PSReadLine module automatically.
PSReadLine is a signed module. PowerShell must verify the digital signature of the module. This
verification can cause delays in a disconnected environment. To test this theory, start
PowerShell 7 in non-interactive mode:

 PowerShell
 pwsh.exe -noninteractive

If PowerShell starts quickly in non-interactive mode, then the problem is likely caused by
Certificate Revocation List (CRL) checks. As part of the process of verifying a digital signature,
The .NET runtime checks the CRL to ensure that the signing certificate is still valid. In a
disconnected environment, you computer can't access the CRL on internet. The default timeout
for CRL checks is 15 seconds. This means that every time PowerShell loads a signed module, it
can take up to 15 seconds to timeout.

There are three possible workarounds for this problem:

     Firewall or proxy exemption

     Allowing direct internet access for CRL checking prevents the problem. In an environment
     where you can control access to the internet access, you can configure your firewall or
     proxy to allow access to the CRL Urls. This is the easiest solution with the least impact.
     The firewall logs should show the Url that PowerShell attempted to reach.

     Reduce CRL Timeout

     Reducing the CRL lookup timeout is possible, but doing so risks other lookups to fail, that
     can't complete in the time specified. For details about how to change the timeout, see
     Manage Network Retrieval and Path Validation.

     Remove CRL checking

     The CRL checking settings are managed by Group Policy. For more information, see
     Manage Trusted Publishers.

        ２ Warning

        It's possible to disable the CRL check however, it's not recommended. Disabling CRL
        checking prevents you from actually revoking compromised certificates.

<!-- p.1070 -->

ERROR: Cannot dot-source this command because it was
defined in a different language mode
PowerShell works with application control systems, such as AppLocker and Windows Defender
Application Control (WDAC), by automatically running in ConstrainedLanguage mode.
ConstrainedLanguage mode restricts some features that are potentially dangerous. However,
there are times when you need FullLanguage mode to use certain commands or features.
Scripts can run in FullLanguage mode when they're trusted by the policy. Trust can be
indicated through file signing or other policy mechanisms configured in AppLocker or WDAC.

When you start a PowerShell session that's managed under application control, you get the
following error:

 Cannot dot-source this command because it was defined in a different language mode.
 To invoke this
 command without importing its contents, omit the '.' operator.

Under application control, PowerShell is running in ConstrainedLanguage mode. This error
occurs when and your profile script is exempted or is signed to run in FullLanguage mode.
When PowerShell is running in ConstrainedLanguage mode, it can't dot-source code trusted to
run in FullLanguage mode.

To resolve the problem, you must remove the exemption or signature from the profile script. If
you need code that must run in FullLanguage mode during your profile, move it into another
script file that's exempted or signed. Call (don't dot-source) that script file from within your
profile.

For more information on this issue, see PowerShell Constrained Language mode and the Dot-
Source Operator       .

Further reading
      about_Language_Modes
      Measure-Command

 Last updated on 01/14/2026

<!-- p.1071 -->

Portable Modules
Windows PowerShell is written for .NET Framework while PowerShell Core is written for .NET
Core. Portable modules are modules that work in both Windows PowerShell and PowerShell
Core. While .NET Framework and .NET Core are highly compatible, there are differences in the
available APIs between the two. There are also differences in the APIs available in Windows
PowerShell and PowerShell Core. Modules intended to be used in both environments need to
be aware of these differences.

Porting an existing module

Porting a PSSnapIn
PowerShell SnapIns aren't supported in PowerShell Core. However, it's trivial to convert a
PSSnapIn to a PowerShell module. Typically, the PSSnapIn registration code is in a single source
file of a class that derives from PSSnapIn. Remove this source file from the build; it's no longer
needed.

Use New-ModuleManifest to create a new module manifest that replaces the need for the
PSSnapIn registration code. Some values from the PSSnapIn (such as Description) can be
reused within the module manifest.

The RootModule property in the module manifest should be set to the name of the assembly
( .dll ) implementing the cmdlets.

The .NET Portability Analyzer (aka APIPort)
To port modules written for Windows PowerShell to work with PowerShell Core, start with the
.NET Portability Analyzer   . Run this tool against your compiled assembly to determine if the
.NET APIs used in the module are compatible with .NET Framework, .NET Core, and other .NET
runtimes. The tool suggests alternate APIs if they exist. Otherwise, you may need to add
runtime checks and restrict capabilities not available in specific runtimes.

Creating a new module
If creating a new module, the recommendation is to use the .NET CLI.

Installing the PowerShell Standard module template

<!-- p.1072 -->

Once the .NET CLI is installed, install a template library to generate a simple PowerShell
module. The module will be compatible with Windows PowerShell, PowerShell Core, Windows,
Linux, and macOS.

The following example shows how to install the template:

 PowerShell
 dotnet new install Microsoft.PowerShell.Standard.Module.Template

 Output
 The following template packages will be installed:
    Microsoft.PowerShell.Standard.Module.Template

 Success: Microsoft.PowerShell.Standard.Module.Template::0.1.3 installed the
 following templates:
 Template Name               Short Name Language Tags
 -------------------------- ---------- -------- -------------------------
 PowerShell Standard Module psmodule     [C#]      Library/PowerShell/Module

Creating a new module project
After the template is installed, you can create a new PowerShell module project using that
template. In this example, the sample module is called 'myModule'.

 PS> mkdir myModule

     Directory: C:\Users\Steve

 Mode LastWriteTime Length Name
 ---- ------------- ------ ----
 d----- 8/3/2018 2:41 PM myModule

 PS> cd myModule
 PS C:\Users\Steve\myModule> dotnet new psmodule
 The template "PowerShell Standard Module" was created successfully.

 Processing post-creation actions...
 Restoring C:\Users\Steve\myModule\myModule.csproj:
   Determining projects to restore...
   Restored C:\Users\Steve\myModule\myModule.csproj (in 184 ms).
 Restore succeeded.

Building the module

<!-- p.1073 -->

Use standard .NET CLI commands to build the project.

 PowerShell

 dotnet build

 Output
 PS C:\Users\Steve\myModule> dotnet build
 MSBuild version 17.6.3+07e294721 for .NET
   Determining projects to restore...
   All projects are up-to-date for restore.
   PowerShellPG -> C:\Users\Steve\myModule\bin\Debug\netstandard2.0\myModule.dll

 Build succeeded.
     0 Warning(s)
     0 Error(s)

 Time Elapsed 00:00:02.36

Testing the module
After building the module, you can import it and execute the sample cmdlet.

 PowerShell

 Import-Module .\bin\Debug\netstandard2.0\myModule.dll
 Test-SampleCmdlet -?
 Test-SampleCmdlet -FavoriteNumber 7 -FavoritePet Cat

 Output
 NAME
        Test-SampleCmdlet

 SYNTAX
     Test-SampleCmdlet [-FavoriteNumber] <int> [[-FavoritePet] {Cat | Dog | Horse}]
 [<CommonParameters>]

 ALIASES
     None

 REMARKS
     None

 FavoriteNumber FavoritePet

<!-- p.1074 -->

 -------------- -----------
              7 Cat

Debugging the module
For a guide on setting up Visual Studio Code to debug the module, see Using Visual Studio
Code for debugging compiled cmdlets.

Supporting technologies
The following sections describe in detail some of the technologies used by this template.

.NET Standard Library
.NET Standard is a formal specification of .NET APIs that are available in all .NET
implementations. Managed code targeting .NET Standard works with the .NET Framework and
.NET Core versions that are compatible with that version of the .NET Standard.

  ７ Note

  Although an API may exist in .NET Standard, the API implementation in .NET Core may
  throw a PlatformNotSupportedException at runtime, so to verify compatibility with
  Windows PowerShell and PowerShell Core, the best practice is to run tests for your
  module within both environments. Also run tests on Linux and macOS if your module is
  intended to be cross-platform.

Targeting .NET Standard helps ensure that, as the module evolves, incompatible APIs don't
accidentally get introduced into the module. Incompatibilities are discovered at compile time
instead of runtime.

However, it isn't required to target .NET Standard for a module to work with both Windows
PowerShell and PowerShell Core, as long as you use compatible APIs. The Intermediate
Language (IL) is compatible between the two runtimes. You can target .NET Framework 4.6.1,
which is compatible with .NET Standard 2.0. If you don't use APIs outside of .NET Standard 2.0,
then your module works with PowerShell Core 6 without recompilation.

PowerShell Standard Library
The PowerShell Standard      library is a formal specification of PowerShell APIs available in all
PowerShell versions greater than or equal to the version of that standard.

<!-- p.1075 -->

For example, PowerShell Standard 5.1    is compatible with both Windows PowerShell 5.1 and
PowerShell Core 6.0 or newer.

We recommend you compile your module using PowerShell Standard Library. The library
ensures the APIs are available and implemented in both Windows PowerShell and PowerShell
Core 6. PowerShell Standard is intended to always be forwards-compatible. A module built
using PowerShell Standard Library 5.1 will always be compatible with future versions of
PowerShell.

Module Manifest

Indicating Compatibility With Windows PowerShell and PowerShell Core

After validating that your module works with both Windows PowerShell and PowerShell Core,
the module manifest should explicitly indicate compatibility by using the CompatiblePSEditions
property. A value of Desktop means that the module is compatible with Windows PowerShell,
while a value of Core means that the module is compatible with PowerShell Core. Including
both Desktop and Core means that the module is compatible with both Windows PowerShell
and PowerShell Core.

  ７ Note

  Core doesn't automatically mean that the module is compatible with Windows, Linux, and

  macOS. The CompatiblePSEditions property was introduced in PowerShell v5. Module
  manifests that use the CompatiblePSEditions property fail to load in versions prior to
  PowerShell v5.

Indicating OS Compatibility
First, validate that your module works on Linux and macOS. Next, indicate compatibility with
those operating systems in the module manifest. This makes it easier for users to find your
module for their operating system when published to the PowerShell Gallery     .

Within the module manifest, the PrivateData property has a PSData sub-property. The
optional Tags property of PSData takes an array of values that show up in PowerShell Gallery.
The PowerShell Gallery supports the following compatibility values:

                                                                               ﾉ   Expand table

<!-- p.1076 -->

 Tag                           Description

 PSEdition_Core                Compatible with PowerShell Core 6

 PSEdition_Desktop             Compatible with Windows PowerShell

 Windows                       Compatible with Windows

 Linux                         Compatible with Linux (no specific distro)

 macOS                         Compatible with macOS

Example:

 PowerShell
 @{
     GUID = "4ae9fd46-338a-459c-8186-07f910774cb8"
     Author = "Microsoft Corporation"
     CompanyName = "Microsoft Corporation"
     Copyright = "(C) Microsoft Corporation. All rights reserved."
     HelpInfoUri = "https://go.microsoft.com/fwlink/?linkid=855962"
     ModuleVersion = "1.2.4"
     PowerShellVersion = "3.0"
     ClrVersion = "4.0"
     RootModule = "PackageManagement.psm1"
     Description = 'PackageManagement (a.k.a. OneGet) is a new way to discover and
 install software packages from around the web.
  it's a manager or multiplexer of existing package managers (also called package
 providers) that unifies Windows package management with a single Windows PowerShell
 interface. With PackageManagement, you can do the following.
   - Manage a list of software repositories in which packages can be searched,
 acquired and installed
   - Discover software packages
   - Seamlessly install, uninstall, and inventory packages from one or more software
 repositories'

       CmdletsToExport = @(
           'Find-Package',
           'Get-Package',
           'Get-PackageProvider',
           'Get-PackageSource',
           'Install-Package',
           'Import-PackageProvider'
           'Find-PackageProvider'
           'Install-PackageProvider'
           'Register-PackageSource',
           'Set-PackageSource',
           'Unregister-PackageSource',
           'Uninstall-Package'
           'Save-Package'
       )

<!-- p.1077 -->

      FormatsToProcess    = @('PackageManagement.format.ps1xml')

     PrivateData = @{
         PSData = @{
             Tags = @('PackageManagement', 'PSEdition_Core', 'PSEdition_Desktop',
 'Windows', 'Linux', 'macOS')
             ProjectUri = 'https://oneget.org'
         }
     }
 }

Dependency on Native Libraries
Modules intended for use across different operating systems or processor architectures may
depend on a managed library that itself depends on some native libraries.

Prior to PowerShell 7, one would have to have custom code to load the appropriate native dll
so that the managed library can find it correctly.

With PowerShell 7, native binaries to load are searched in sub-folders within the managed
library's location following a subset of the .NET RID Catalog notation.

 managed.dll folder
     |
     |--- 'win-x64' folder
     |       |--- native.dll
     |
     |--- 'win-x86' folder
     |       |--- native.dll
     |
     |--- 'win-arm' folder
     |       |--- native.dll
     |
     |--- 'win-arm64' folder
     |       |--- native.dll
     |
     |--- 'linux-x64' folder
     |       |--- native.so
     |
     |--- 'linux-x86' folder
     |       |--- native.so
     |
     |--- 'linux-arm' folder
     |       |--- native.so
     |
     |--- 'linux-arm64' folder
     |       |--- native.so
     |

<!-- p.1078 -->

     |--- 'osx-x64' folder
     |       |--- native.dylib

Last updated on 12/08/2025

<!-- p.1079 -->

How to create a Standard Library binary
module
I recently had an idea for module that I wanted to implement as a binary module. I have yet to
create one using the PowerShell Standard Library    so this felt like a good opportunity. I used
the Creating a cross-platform binary module     guide to create this module without any
roadblocks. We're going to walk that same process and I'll add a little extra commentary along
the way.

  ７ Note

  The original version    of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com      .

What's the PowerShell Standard Library?
The PowerShell Standard Library allows us to create cross platform modules that work in both
PowerShell and Windows PowerShell 5.1.

Why binary modules?
When you are writing a module in C# you give up easy access to PowerShell cmdlets and
functions. But if you are creating a module that doesn't depend on a lot of other PowerShell
commands, the performance benefit can be significant. PowerShell was optimized for the
administrator, not the computer. By switching to C#, you get to shed the overhead added by
PowerShell.

For example, we have a critical process that does a lot of work with JSON and hashtables. We
optimized the PowerShell as much as we could but the process still takes 12 minutes to
complete. The module already contained a lot of C# style PowerShell. This makes conversion to
a binary module clean and simple. By converting to a binary module, we reduced the process
time from over 12 minutes to under four minutes.

Hybrid modules
You can mix binary cmdlets with PowerShell advanced functions. Everything you know about
script modules applies the same way. The empty psm1 file is included so you can add other
PowerShell functions later.

<!-- p.1080 -->

Almost all of the compiled cmdlets that I have created started out as PowerShell functions first.
All of our binary modules are really hybrid modules.

Build scripts
I kept the build script simple here. I generally use a large Invoke-Build script as part of my
CI/CD pipeline. It does more magic like running Pester tests, running PSScriptAnalyzer,
managing versioning, and publishing to the PSGallery. Once I started using a build script for
my modules, I was able to find lots of things to add to it.

Planning the module
The plan for this module is to create a src folder for the C# code and structure the rest like I
would for a script module. This includes using a build script to compile everything into an
Output folder. The folder structure looks like this:

 MyModule
 ├───src
 ├───Output
 │   └───MyModule
 ├───MyModule
 │   ├───Data
 │   ├───Private
 │   └───Public
 └───Tests

Getting Started
First I need to create the folder and create the git repo. I'm using $module as a placeholder for
the module name. This should make it easier for you to reuse these examples if needed.

 PowerShell
 $module = 'MyModule'
 New-Item -Path $module -Type Directory
 Set-Location $module
 git init

Then create the root level folders.

 PowerShell
