---
title: "How to use this documentation — pages 1321-1360"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1321-1360
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1321-1360
family: powershell
documentKind: "doc"
abstract: "return 123 # 123 is written to the pipeline } The caller to Test gets back an unconstrained 1-dimensional array of three elements. 8.5.5 The exit statement Description: The exit statement terminates the current script and returns control and an exit code to the host environment"
---

# How to use this documentation — pages 1321-1360

<!-- p.1321 -->

      return 123 # 123 is written to the pipeline
 }

The caller to Test gets back an unconstrained 1-dimensional array of three elements.

8.5.5 The exit statement
Description:

The exit statement terminates the current script and returns control and an exit code to the
host environment or the calling script. If pipeline is provided, the value it designates is
converted to int, if necessary. If no such conversion exists, or if pipeline is omitted, the int value
zero is returned.

Examples:

 PowerShell

 exit $count # terminate the script with some accumulated count

8.6 The switch statement
Syntax:

 Syntax

 switch-statement:
     switch new-lines~opt~ switch-parameters~opt~ switch-condition switch-body

 switch-parameters:
     switch-parameter
     switch-parameters switch-parameter

 switch-parameter:
     -Regex
     -Wildcard
     -Exact
     -CaseSensitive
     -Parallel

 switch-condition:
     ( new-lines~opt~ pipeline new-lines~opt~ )
     -File new-lines~opt~ switch-filename

 switch-filename:
     command-argument
     primary-expression

<!-- p.1322 -->

 switch-body:
     new-lines~opt~ { new-lines~opt~ switch-clauses }

 switch-clauses:
     switch-clause
     switch-clauses switch-clause

 switch-clause:
     switch-clause-condition statement-block statement-terimators~opt~

 switch-clause-condition:
     command-argument
     primary-expression

Description:

If switch-condition designates a single value, control is passed to one or more matching pattern
statement blocks. If no patterns match, some default action can be taken.

A switch must contain one or more switch-clauses, each starting with a pattern (a non-default
switch clause), or the keyword default (a default switch clause). A switch must contain zero or
one default switch clauses, and zero or more non-default switch clauses. Switch clauses may
be written in any order.

Multiple patterns may have the same value. A pattern need not be a literal, and a switch may
have patterns with different types.

If the value of switch-condition matches a pattern value, that pattern's statement-block is
executed. If multiple pattern values match the value of switch-condition, each matching
pattern's statement-block is executed, in lexical order, unless any of those statement-blocks
contains a break statement (§8.5.1).

If the value of switch-condition does not match any pattern value, if a default switch clause
exists, its statement-block is executed; otherwise, pattern matching for that switch-condition is
terminated.

Switches may be nested, with each switch having its own set of switch clauses. In such
instances, a switch clause belongs to the innermost switch currently in scope.

On entry to each statement-block, $_ is automatically assigned the value of the switch-
condition that caused control to go to that statement-block. $_ is also available in that
statement-block's switch-clause-condition.

Matching of non-strings is done by testing for equality (§7.8.1).

<!-- p.1323 -->

If the matching involves strings, by default, the comparison is case-insensitive. The presence of
the switch-parameter -CaseSensitive makes the comparison case-sensitive.

A pattern may contain wildcard characters (§3.15), in which case, wildcard string comparisons
are performed, but only if the switch-parameter -Wildcard is present. By default, the
comparison is case-insensitive.

A pattern may contain a regular expression (§3.16), in which case, regular expression string
comparisons are performed, but only if the switch-parameter -Regex is present. By default, the
comparison is case-insensitive. If -Regex is present and a pattern is matched, $Matches is
defined in the switch-clause statement-block for that pattern.

A switch-parameter may be abbreviated; any distinct leading part of a parameter may be used.
For example, ‑Regex , ‑Rege , ‑Reg , ‑Re , and ‑R are equivalent.

If conflicting switch-parameters are specified, the lexically final one prevails. The presence of
‑Exact disables -Regex and -Wildcard ; it has no affect on ‑Case , however.

If the switch-parameter ‑Parallel is specified, the behavior is implementation defined.

The switch-parameter ‑Parallel is only allowed in a workflow (§8.10.2).

If a pattern is a script-block-expression, that block is evaluated and the result is converted to
bool, if necessary. If the result has the value $true , the corresponding statement-block is
executed; otherwise, it is not.

If switch-condition designates multiple values, the switch is applied to each value in lexical
order using the rules described above for a switch-condition that designates a single value.
Every switch statement has its own enumerator, $switch (§2.3.2.2, §4.5.16), which exists only
while that switch is executing.

A switch statement may have a label, and it may contain labeled and unlabeled break (§8.5.1)
and continue (§8.5.2) statements.

If switch-condition is -File switch-filename, instead of iterating over the values in an
expression, the switch iterates over the values in the file designated by switch-filename.The file
is read a line at a time with each line comprising a value. Line terminator characters are not
included in the values.

Examples:

 PowerShell

<!-- p.1324 -->

 $s = "ABC def`nghi`tjkl`fmno @#$"
 $charCount = 0; $pageCount = 0; $lineCount = 0; $otherCount = 0
 for ($i = 0; $i -lt $s.Length; ++$i) {
     ++$charCount
     switch ($s[$i]) {
         "`n" { ++$lineCount }
         "`f" { ++$pageCount }
         "`t" { }
         " " { }
         default { ++$otherCount }
     }
 }

 switch -Wildcard ("abc") {
     a* { "a*, $_" }
     ?B? { "?B? , $_" }
     default { "default, $_" }
 }

 switch -Regex -CaseSensitive ("abc") {
     ^a* { "a*" }
     ^A* { "A*" }
 }

 switch (0, 1, 19, 20, 21) {
     { $_ -lt 20 } { "-lt 20" }
     { $_ -band 1 } { "Odd" }
     { $_ -eq 19 } { "-eq 19" }
     default { "default" }
 }

8.7 The try/finally statement
Syntax:

 Syntax

 try-statement:
     try statement-block catch-clauses
     try statement-block finally-clause
     try statement-block catch-clauses finally-clause

 catch-clauses:
     catch-clause
     catch-clauses catch-clause

 catch-clause:
     new-lines~opt~ catch catch-type-list~opt~
     statement-block

 catch-type-list:

<!-- p.1325 -->

      new-lines~opt~ type-literal
      catch-type-list new-lines~opt~ , new-lines~opt~

  type-literalfinally-clause:
      new-lines~opt~ finally statement-block

Description:

The try statement provides a mechanism for catching exceptions that occur during execution
of a block. The try statement also provides the ability to specify a block of code that is always
executed when control leaves the try statement. The process of raising an exception via the
throw statement is described in §8.5.3.

A try block is the statement-block associated with the try statement. A catch block is the
statement-block associated with a catch-clause. A finally block is the statement-block associated
with a finally-clause.

A catch-clause without a catch-type-list is called a general catch clause.

Each catch-clause is an exception handler, and a catch-clause whose catch-type-list contains the
type of the raised exception is a matching catch clause. A general catch clause matches all
exception types.

Although catch-clauses and finally-clause are optional, at least one of them must be present.

The processing of a thrown exception consists of evaluating the following steps repeatedly
until a catch clause that matches the exception is found.

     In the current scope, each try statement that encloses the throw point is examined. For
     each try statement S, starting with the innermost try statement and ending with the
     outermost try statement, the following steps are evaluated:

        If the try block of S encloses the throw point and if S has one or more catch clauses,
        the catch clauses are examined in lexical order to locate a suitable handler for the
        exception. The first catch clause that specifies the exception type or a base type of the
        exception type is considered a match. A general catch clause is considered a match for
        any exception type. If a matching catch clause is located, the exception processing is
        completed by transferring control to the block of that catch clause. Within a matching
        catch clause, the variable $_ contains a description of the current exception.

        Otherwise, if the try block or a catch block of S encloses the throw point and if S has
        a finally block, control is transferred to the finally block. If the finally block throws

<!-- p.1326 -->

        another exception, processing of the current exception is terminated. Otherwise, when
        control reaches the end of the finally block, processing of the current exception is
        continued.

     If an exception handler was not located in the current scope, the steps above are then
     repeated for the enclosing scope with a throw point corresponding to the statement from
     which the current scope was invoked.

     If the exception processing ends up terminating all scopes, indicating that no handler
     exists for the exception, then the behavior is unspecified.

To prevent unreachable catch clauses in a try block, a catch clause may not specify an
exception type that is equal to or derived from a type that was specified in an earlier catch
clause within that same try block.

The statements of a finally block are always executed when control leaves a try statement.
This is true whether the control transfer occurs as a result of normal execution, as a result of
executing a break , continue , or return statement, or as a result of an exception being thrown
out of the try statement.

If an exception is thrown during execution of a finally block, the exception is thrown out to
the next enclosing try statement. If another exception was in the process of being handled,
that exception is lost. The process of generating an exception is further discussed in the
description of the throw statement.

try statements can co-exist with trap statements; see §8.8 for details.

Examples:

 PowerShell

 $a = New-Object 'int[]' 10
 $i = 20 # out-of-bounds subscript

 while ($true) {
     try {
         $a[$i] = 10
         "Assignment completed without error"
         break
     }

      catch [IndexOutOfRangeException] {
          "Handling out-of-bounds index, >$_<`n"
          $i = 5
      }

<!-- p.1327 -->

        catch {
            "Caught unexpected exception"
        }

        finally {
            # ...
        }
  }

Each exception thrown is raised as a System.Management.Automation.RuntimeException . If there
are type-specific catch-clauses in the try block, the InnerException property of the exception
is inspected to try and find a match, such as with the type System.IndexOutOfRangeException
above.

8.8 The trap statement
Syntax:

  Syntax

  trap-statement:
      *trap* new-lines~opt~ type-literal~opt~ new-lines~opt~ statement-block

Description:

A trap statement with and without type-literal is analogous to a catch block (§8.7) with and
without catch-type-list, respectively, except that a trap statement can trap only one type at a
time.

Multiple trap statements can be defined in the same statement-block, and their order of
definition is irrelevant. If two trap statements with the same type-literal are defined in the
same scope, the lexically first one is used to process an exception of matching type.

Unlike a catch block, a trap statement matches an exception type exactly; no derived type
matching is performed.

When an exception occurs, if no matching trap statement is present in the current scope, a
matching trap statement is searched for in the enclosing scope, which may involve looking in
the calling script, function, or filter, and then in its caller, and so on. If the lookup ends up
terminating all scopes, indicating that no handler exists for the exception, then the behavior is
unspecified.

<!-- p.1328 -->

A trap statement's statement-body only executes to process the corresponding exception;
otherwise, execution passes over it.

If a trap 's statement-body exits normally, by default, an error object is written to the error
stream, the exception is considered handled, and execution continues with the statement
immediately following the one in the scope containing the trap statement that made the
exception visible. The cause of the exception might be in a command called by the command
containing the trap statement.

If the final statement executed in a trap 's statement-body is continue (§8.5.2), the writing of
the error object to the error stream is suppressed, and execution continues with the statement
immediately following the one in the scope containing the trap statement that made the
exception visible. If the final statement executed in a trap 's statement-body is break (§8.5.1),
the writing of the error object to the error stream is suppressed, and the exception is re-
thrown.

Within a trap statement the variable $_ contains a description of the current error.

Consider the case in which an exception raised from within a try block does not have a
matching catch block, but a matching trap statement exists at a higher block level. After the
try block's finally clause is executed, the trap statement gets control even if any parent scope

has a matching catch block. If a trap statement is defined within the try block itself, and that
try block has a matching catch block, the trap statement gets control.

Examples:

In the following example, the error object is written and execution continues with the
statement immediately following the one that caused the trap; that is, "Done" is written to the
pipeline.

 PowerShell

 $j = 0; $v = 10/$j; "Done"
 trap { $j = 2 }

In the following example, the writing of the error object is suppressed and execution continues
with the statement immediately following the one that caused the trap; that is, "Done" is
written to the pipeline.

 PowerShell

<!-- p.1329 -->

 $j = 0; $v = 10/$j; "Done"
 trap { $j = 2; continue }

In the following example, the writing of the error object is suppressed and the exception is re-
thrown.

 PowerShell

 $j = 0; $v = 10/$j; "Done"
 trap { $j = 2; break }

In the following example, the trap and exception-generating statements are in the same scope.
After the exception is caught and handled, execution resumes with writing 1 to the pipeline.

 PowerShell

 &{trap{}; throw '\...'; 1}

In the following example, the trap and exception-generating statements are in different scopes.
After the exception is caught and handled, execution resumes with writing 2 (not 1) to the
pipeline.

 PowerShell

 trap{} &{throw '\...'; 1}; 2

8.9 The data statement
Syntax:

 Syntax

 data-statement:
     data new-lines~opt~ data-name data-commands-allowed~opt~ statement-block

 data-name:
     simple-name

 data-commands-allowed:
     new-lines~opt~ -SupportedCommand data-commands-list

 data-commands-list:
     new-lines~opt~ data-command
     data-commands-list , new-lines~opt~ data-command

<!-- p.1330 -->

 data-command:
     command-name-expr

Description:

A data statement creates a data section, keeping that section's data separate from the code.
This separation supports facilities like separate string resource files for text, such as error
messages and Help strings. It also helps support internationalization by making it easier to
isolate, locate, and process strings that will be translated into different languages.

A script or function can have zero or more data sections.

The statement-block of a data section is limited to containing the following PowerShell features
only:

        All operators except -match
        The if statement
        The following automatic variables: $PSCulture , $PSUICulture , $true , $false , and $null .
        Comments
        Pipelines
        Statements separated by semicolons ( ; )
        Literals
        Calls to the ConvertFrom-StringData cmdlet
        Any other cmdlets identified via the SupportedCommand parameter

If the ConvertFrom-StringData cmdlet is used, the key/value pairs can be expressed using any
form of string literal. However, expandable-string-literals and expandable-here-string-literals
must not contain any variable substitutions or sub-expression expansions.

Examples:

The SupportedCommand parameter indicates that the given cmdlets or functions generate
data only. For example, the following data section includes a user-written cmdlet, ConvertTo-
Xml , which formats data in an XML file:

 PowerShell

 data -SupportedCommand ConvertTo-Xml {
     Format-Xml -Strings string1, string2, string3
 }

<!-- p.1331 -->

Consider the following example, in which the data section contains a ConvertFrom-StringData
command that converts the strings into a hash table, whose value is assigned to $messages .

 PowerShell

 $messages = data {
     ConvertFrom-StringData -StringData @'
     Greeting = Hello
     Yes = yes
     No = no
 '@
 }

The keys and values of the hash table are accessed using $messages.Greeting , $messages.Yes ,
and $messages.No , respectively.

Now, this can be saved as an English-language resource. German- and Spanish-language
resources can be created in separate files, with the following data sections:

 PowerShell

 $messages = data {
     ConvertFrom-StringData -StringData @"
     Greeting = Guten Tag
     Yes = ja
     No = nein
 "@
 }

 $messagesS = data {
     ConvertFrom-StringData -StringData @"
     Greeting = Buenos días
     Yes = sí
     No = no
 "@
 }

If dataname is present, it names the variable (without using a leading $ ) into which the value
of the data statement is to be stored. Specifically, $name = data { ... } is equivalent to data
name { ... } .

8.10 Function definitions
Syntax:

 Syntax

<!-- p.1332 -->

function-statement:
    function new-lines~opt~ function-name function-parameter-declaration~opt~ {
script-block }
    filter new-lines~opt~ function-name function-parameter-declaration~opt~ {
script-block }
    workflow new-lines~opt~ function-name function-parameter-declaration~opt~ {
script-block }

function-name:
    command-argument

command-argument:
    command-name-expr

function-parameter-declaration:
    new-lines~opt~ ( parameter-list new-lines~opt~ )

parameter-list:
    script-parameter
    parameter-list new-lines~opt~ , script-parameter

script-parameter:
    new-lines~opt~ attribute-list~opt~ new-lines~opt~ variable script-parameter-
default~opt~

script-block:
    param-block~opt~ statement-terminators~opt~ script-block-body~opt~

param-block:
    new-lines~opt~ attribute-list~opt~ new-lines~opt~ param new-lines~opt~
        ( parameter-list~opt~ new-lines~opt~ )

parameter-list:
    script-parameter
    parameter-list new-lines~opt~ , script-parameter

script-parameter-default:
    new-lines~opt~ = new-lines~opt~ expression

script-block-body:
    named-block-list
    statement-list

named-block-list:
    named-block
    named-block-list named-block

named-block:
    block-name statement-block statement-terminators~opt~

block-name: one of
    dynamicparam   begin   process   end

<!-- p.1333 -->

Description:

A function definition specifies the name of the function, filter, or workflow being defined and
the names of its parameters, if any. It also contains zero or more statements that are executed
to achieve that function's purpose.

Each function is an instance of the class System.Management.Automation.FunctionInfo .

8.10.1 Filter functions
Whereas an ordinary function runs once in a pipeline and accesses the input collection via
$input , a filter is a special kind of function that executes once for each object in the input

collection. The object currently being processed is available via the variable $_ .

A filter with no named blocks (§8.10.7) is equivalent to a function with a process block, but
without any begin block or end block.

Consider the following filter function definition and calls:

 PowerShell

 filter Get-Square2 { # make the function a filter
     $_ * $_ # access current object from the collection
 }

 -3..3 | Get-Square2 # collection has 7 elements
 6, 10, -3 | Get-Square2 # collection has 3 elements

Each filter is an instance of the class System.Management.Automation.FilterInfo (§4.5.11).

8.10.2 Workflow functions
A workflow function is like an ordinary function with implementation defined semantics. A
workflow function is translated to a sequence of Windows Workflow Foundation activities and
executed in the Windows Workflow Foundation engine.

8.10.3 Argument processing
Consider the following definition for a function called Get-Power :

 PowerShell

 function Get-Power ([long]$Base, [int]$Exponent) {
     $result = 1

<!-- p.1334 -->

         for ($i = 1; $i -le $Exponent; ++$i) {
             $result *= $Base
         }
         return $result
  }

This function has two parameters, $Base and $Exponent . It also contains a set of statements
that, for non-negative exponent values, computes $Base^$Exponent^ and returns the result to
Get-Power 's caller.

When a script, function, or filter begins execution, each parameter is initialized to its
corresponding argument's value. If there is no corresponding argument and a default value
(§8.10.4) is supplied, that value is used; otherwise, the value $null is used. As such, each
parameter is a new variable just as if it was initialized by assignment at the start of the script-
block.

If a script-parameter contains a type constraint (such as [long] and [int] above), the value of
the corresponding argument is converted to that type, if necessary; otherwise, no conversion
occurs.

When a script, function, or filter begins execution, variable $args is defined inside it as an
unconstrained 1-dimensional array, which contains all arguments not bound by name or
position, in lexical order.

Consider the following function definition and calls:

  PowerShell

  function F ($a, $b, $c, $d) { ... }

  F -b 3 -d 5 2 4             # $a is 2, $b is 3, $c is 4, $d is 5, $args Length 0
  F -a 2 -d 3 4 5             # $a is 2, $b is 4, $c is 5, $d is 3, $args Length 0
  F 2 3 4 5 -c 7 -a 1         # $a is 1, $b is 2, $c is 7, $d is 3, $args Length 2

For more information about parameter binding see §8.14.

8.10.4 Parameter initializers
The declaration of a parameter p may contain an initializer, in which case, that initializer's value
is used to initialize p provided p is not bound to any arguments in the call.

Consider the following function definition and calls:

<!-- p.1335 -->

  PowerShell

  function Find-Str ([string]$Str, [int]$StartPos = 0) { ... }

  Find-Str "abcabc" # 2nd argument omitted, 0 used for $StartPos
  Find-Str "abcabc" 2 # 2nd argument present, so it is used for $StartPos

8.10.5 The [switch] type constraint
When a [switch] parameter is passed, the corresponding parameter in the command must be
constrained by the type switch. Type switch has two values, True and False.

Consider the following function definition and calls:

  PowerShell

  function Process ([switch]$Trace, $P1, $P2) { ... }

  Process 10 20                     # $Trace is False, $P1 is 10, $P2 is 20
  Process 10 -Trace 20              # $Trace is True, $P1 is 10, $P2 is 20
  Process 10 20 -Trace              # $Trace is True, $P1 is 10, $P2 is 20
  Process 10 20 -Trace:$false       # $Trace is False, $P1 is 10, $P2 is 20
  Process 10 20 -Trace:$true        # $Trace is True, $P1 is 10, $P2 is 20

8.10.6 Pipelines and functions
When a script, function, or filter is used in a pipeline, a collection of values is delivered to that
script or function. The script, function, or filter gets access to that collection via the enumerator
$input (§2.3.2.2, §4.5.16), which is defined on entry to that script, function, or filter.

Consider the following function definition and calls:

  PowerShell

  function Get-Square1 {
      foreach ($i in $input) {         # iterate over the collection
          $i * $i
      }
  }

  -3..3 | Get-Square1                  # collection has 7 elements
  6, 10, -3 | Get-Square1              # collection has 3 elements

8.10.7 Named blocks

<!-- p.1336 -->

The statements within a script-block can belong to one large unnamed block, or they can be
distributed into one or more named blocks. Named blocks allow custom processing of
collections coming from pipelines; named blocks can be defined in any order.

The statements in a begin block (i.e.; one marked with the keyword begin) are executed once,
before the first pipeline object is delivered.

The statements in a process block (i.e.; one marked with the keyword process) are executed for
each pipeline object delivered. ( $_ provides access to the current object being processed from
the input collection coming from the pipeline.) This means that if a collection of zero elements
is sent via the pipeline, the process block is not executed at all. However, if the script or
function is called outside a pipeline context, this block is executed exactly once, and $_ is set
to $null , as there is no current collection object.

The statements in an end block (i.e.; one marked with the keyword end) are executed once,
after the last pipeline object has been delivered.

8.10.8 dynamicparam block
The subsections of §8.10 thus far deal with static parameters, which are defined as part of the
source code. It is also possible to define dynamic parameters via a dynamicparam block,
another form of named block (§8.10.7), which is marked with the keyword dynamicparam . Much
of this machinery is implementation defined.

Dynamic parameters are parameters of a cmdlet, function, filter, or script that are available
under certain conditions only. One such case is the Encoding parameter of the Set-Item
cmdlet.

In the statement-block, use an if statement to specify the conditions under which the parameter
is available in the function. Use the New-Object cmdlet to create an object of an
implementation-defined type to represent the parameter, and specify its name. Also, use New-
Object to create an object of a different implementation-defined type to represent the

implementation-defined attributes of the parameter.

The following example shows a function with standard parameters called Name and Path, and
an optional dynamic parameter named DP1. The DP1 parameter is in the PSet1 parameter set
and has a type of Int32 . The DP1 parameter is available in the Sample function only when the
value of the Path parameter contains "HKLM:", indicating that it is being used in the
HKEY_LOCAL_MACHINE registry drive.

<!-- p.1337 -->

 PowerShell

 function Sample {
     param ([string]$Name, [string]$Path)
     dynamicparam {
         if ($Path -match "*HKLM*:") {
             $dynParam1 = New-Object
 System.Management.Automation.RuntimeDefinedParameter("dp1", [int32],
 $attributeCollection)

             $attributes = New-Object
 System.Management.Automation.ParameterAttribute
             $attributes.ParameterSetName = 'pset1'
             $attributes.Mandatory = $false

             $attributeCollection = New-Object -Type
 System.Collections.ObjectModel.Collection``1[System.Attribute]
             $attributeCollection.Add($attributes)

             $paramDictionary = New-Object
 System.Management.Automation.RuntimeDefinedParameterDictionary
             $paramDictionary.Add("dp1", $dynParam1)
             return $paramDictionary
         }
     }
 }

The type used to create an object to represent a dynamic parameter is
System.Management.Automation.RuntimeDefinedParameter .

The type used to create an object to represent the attributes of the parameter is
System.Management.Automation.ParameterAttribute .

The implementation-defined attributes of the parameter include Mandatory, Position, and
ValueFromPipeline.

8.10.9 param block
A param-block provides an alternate way of declaring parameters. For example, the following
sets of parameter declarations are equivalent:

 PowerShell

 function FindStr1 ([string]$Str, [int]$StartPos = 0) { ... }
 function FindStr2 {
     param ([string]$Str, [int]$StartPos = 0) ...
 }

<!-- p.1338 -->

A param-block allows an attribute-list on the param-block whereas a function-parameter-
declaration does not.

A script may have a param-block but not a function-parameter-declaration. A function or filter
definition may have a function-parameter-declaration or a param-block, but not both.

Consider the following example:

 PowerShell

 param ( [Parameter(Mandatory = $true, ValueFromPipeline=$true)]
         [string[]] $ComputerName )

The one parameter, $ComputerName , has type string[] , it is required, and it takes input from
the pipeline.

See §12.3.7 for a discussion of the Parameter attribute and for more examples.

8.11 The parallel statement
Syntax:

 Syntax

 parallel-statement:
     *parallel* statement-block

The parallel statement contains zero or more statements that are executed in an
implementation defined manner.

A parallel statement is only allowed in a workflow (§8.10.2).

8.12 The sequence statement
Syntax:

 Syntax

 sequence-statement:
     *sequence* statement-block

The sequence statement contains zero or more statements that are executed in an
implementation defined manner.

<!-- p.1339 -->

A sequence statement is only allowed in a workflow (§8.10.2).

8.13 The inlinescript statement
Syntax:

 Syntax

 inlinescript-statement:
     inlinescript statement-block

The inlinescript statement contains zero or more statements that are executed in an
implementation defined manner.

An inlinescript statement is only allowed in a workflow (§8.10.2).

8.14 Parameter binding
When a script, function, filter, or cmdlet is invoked, each argument can be bound to the
corresponding parameter by position, with the first parameter having position zero.

Consider the following definition fragment for a function called Get-Power , and the calls to it:

 PowerShell

 function Get-Power ([long]$Base, [int]$Exponent) { ... }

 Get-Power 5 3          # argument 5 is bound to parameter $Base in position 0
                        # argument 3 is bound to parameter $Exponent in position 1
                        # no conversion is needed, and the result is 5 to the power 3

 Get-Power 4.7 3.2      # double argument 4.7 is rounded to int 5, double argument
                        # 3.2 is rounded to int 3, and result is 5 to the power 3

 Get-Power 5            # $Exponent has value $null, which is converted to int 0

 Get-Power              # both parameters have value $null, which is converted to int 0

When a script, function, filter, or cmdlet is invoked, an argument can be bound to the
corresponding parameter by name. This is done by using a parameter with argument, which is
an argument that is the parameter's name with a leading dash (-), followed by the associated
value for that argument. The parameter name used can have any case-insensitive spelling and
can use any prefix that uniquely designates the corresponding parameter. When choosing
parameter names, avoid using the names of the common parameters.

<!-- p.1340 -->

Consider the following calls to function Get-Power :

 PowerShell

 Get-Power -Base 5 -Exponent 3       # -Base designates $Base, so 5 is
                                     # bound to that, -Exponent designates
                                     # $Exponent, so 3 is bound to that

 Get-Power -Exp 3 -Bas 5             # $Base takes on 5 and $Exponent takes on 3

 Get-Power -E 3 -B 5                 # $Base takes on 5 and $Exponent takes on 3

On the other hand, calls to the following function

 PowerShell

 function Get-Hypot ([double]$Side1, [double]$Side2) {
     return [Math]::Sqrt($Side1 * $Side1 + $Side2 * $Side2)
 }

must use parameters -Side1 and -Side2 , as there is no prefix that uniquely designates the
parameter.

The same parameter name cannot be used multiple times with or without different associated
argument values.

Parameters can have attributes (§12). For information about the individual attributes see the
sections within §12.3. For information about parameter sets see §12.3.7.

A script, function, filter, or cmdlet can receive arguments via the invocation command line,
from the pipeline, or from both. Here are the steps, in order, for resolving parameter binding:

   1. Bind all named parameters, then
   2. Bind positional parameters, then
   3. Bind from the pipeline by value (§12.3.7) with exact match, then
   4. Bind from the pipeline by value (§12.3.7) with conversion, then
   5. Bind from the pipeline by name (§12.3.7) with exact match, then
   6. Bind from the pipeline by name (§12.3.7) with conversion

Several of these steps involve conversion, as described in §6. However, the set of conversions
used in binding is not exactly the same as that used in language conversions. Specifically,

     Although the value $null can be cast to bool, $null cannot be bound to bool .

<!-- p.1341 -->

      When the value $null is passed to a [switch] parameter for a cmdlet, it is treated as if
      $true was passed. However, when passed to a [switch] parameter for a function, it is

      treated as if $false was passed.
      Parameters of type bool or switch can only bind to numeric or bool arguments.
      If the parameter type is not a collection, but the argument is some sort of collection, no
      conversion is attempted unless the parameter type is object or PsObject. (The main point
      of this restriction is to disallow converting a collection to a string parameter.) Otherwise,
      the usual conversions are attempted.

If the parameter type is IList or ICollection<T> , only those conversions via Constructor,
op_Implicit, and op_Explicit are attempted. If no such conversions exist, a special conversion for
parameters of "collection" type is used, which includes IList , ICollection<T> , and arrays.

Positional parameters prefer to be bound without type conversion, if possible. For example,

  PowerShell

  function Test {
      [CmdletBinding(DefaultParameterSetName = "SetB")]
      param([Parameter(Position = 0, ParameterSetName = "SetA")]
          [decimal]$Dec,
          [Parameter(Position = 0, ParameterSetName = "SetB")]
          [int]$In
      )
      $PSCmdlet.ParameterSetName
  }

  Test 42d      # outputs "SetA"
  Test 42       # outputs "SetB"

 Last updated on 04/08/2026

<!-- p.1342 -->

9. Arrays

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December 2012 and
  is based on Windows PowerShell 3.0. This specification does not reflect the current state
  of PowerShell. There is no plan to update this documentation to reflect the current state.
  This documentation is presented here for historical reference.

  The specification document is available as a Microsoft Word document from the Microsoft
  Download Center at: https://www.microsoft.com/download/details.aspx?id=36389
  That Word document has been converted for presentation here on Microsoft Learn.
  During conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

9.1 Introduction
PowerShell supports arrays of one or more dimensions with each dimension having zero or
more elements. Within a dimension, elements are numbered in ascending integer order starting
at zero. Any individual element can be accessed via the array subscript operator [] (§7.1.4).
The number of dimensions in an array is called its rank.

An element can contain a value of any type including an array type. An array having one or
more elements whose values are of any array type is called a jagged array. A multidimensional
array has multiple dimensions, in which case, the number of elements in each row of a
dimension is the same. An element of a jagged array may contain a multidimensional array,
and vice versa.

Multidimensional arrays are stored in row-major order. The number of elements in an array is
called that array's length, which is fixed when the array is created. As such, the elements in a 1-
dimensional array A having length N can be accessed (i.e., subscripted) using the expressions
A[0], A[1], ..., A[N-1] . The elements in a 2-dimensional array B having M rows, with each

row having N columns, can be accessed using the expressions B[0,0], B[0,1], ..., B[0,N-1],

<!-- p.1343 -->

B[1,0], B[1,1], ..., B[1,N-1], ..., B[M-1,0], B[M-1,1], ..., B[M-1,N-1] . And so on for

arrays with three or more dimensions.

By default, an array is polymorphic; i.e., its elements do not need to all have the same type. For
example,

 PowerShell

 $items = 10,"blue",12.54e3,16.30D # 1-D array of length 4
 $items[1] = -2.345
 $items[2] = "green"

 $a = New-Object 'object[,]' 2,2 # 2-D array of length 4
 $a[0,0] = 10
 $a[0,1] = $false
 $a[1,0] = "red"
 $a[1,1] = $null

A 1-dimensional array has type type[] , a 2-dimensional array has type type[,] , a 3-
dimensional array has type type[,,] , and so on, where type is object for an unconstrained type
array, or the constrained type for a constrained array (§9.4).

All array types are derived from the type Array (§4.3.2).

9.2 Array creation
An array is created via an array creation expression, which has the following forms: unary
comma operator (§7.2.1) ,array-expression (§7.1.7), binary comma operator (§7.3), range
operator (§7.4), or New-Object cmdlet.

Here are some examples of array creation and usage:

 PowerShell

 $values = 10, 20, 30
 for ($i = 0; $i -lt $values.Length; ++$i) {
     "`$values[$i] = $($values[$i])"
 }

 $x = , 10                               # x refers to an array of length 1
 $x = @(10)                              # x refers to an array of length 1
 $x = @()                                # x refers to an array of length 0

 $a = New-Object 'object[,]' 2, 2        # create a 2x2 array of anything
 $a[0, 0] = 10                           # set to an int value
 $a[0, 1] = $false                       # set to a boolean value
 $a[1, 0] = "red"                        # set to a string value

<!-- p.1344 -->

  $a[1, 1] = 10.50D                       # set to a decimal value
  foreach ($e in $a) {                    # enumerate over the whole array
      $e
  }

The following is written to the pipeline:

  Output

  $values[0] = 10
  $values[1] = 20
  $values[2] = 30

  10
  False
  red
  10.50

The default initial value of any element not explicitly initialized is the default value for that
element's type (that is, $false , zero, or $null ).

9.3 Array concatenation
Arrays of arbitrary type and length can be concatenated via the + and += operators, both of
which result in the creation of a new unconstrained 1-dimensional array. The existing arrays are
unchanged. See §7.7.3 for more information, and §9.4 for a discussion of adding to an array of
constrained type.

9.4 Constraining element types
A 1-dimensional array can be created so that it is type-constrained by prefixing the array-
creation expression with an array type cast. For example,

  PowerShell

  $a = [int[]](1,2,3,4)       # constrained to int
  $a[1] = "abc"               # implementation-defined behavior
  $a += 1.23                  # new array is unconstrained

The syntax for creating a multidimensional array requires the specification of a type, and that
type becomes the constraint type for that array. However, by specifying type object[] , there
really is no constraint as a value of any type can be assigned to an element of an array of that
type.

<!-- p.1345 -->

Concatenating two arrays (§7.7.3) always results in a new array that is unconstrained even if
both arrays are constrained by the same type. For example,

 PowerShell

 $a = [int[]](1,2,3)        # constrained to int
 $b = [int[]](10,20)        # constrained to int
 $c = $a + $b               # constraint not preserved
 $c = [int[]]($a + $b)      # result explicitly constrained to int

9.5 Arrays as reference types
As array types are reference types, a variable designating an array can be made to refer to any
array of any rank, length, and element type. For example,

 PowerShell

 $a = 10,20                          # $a refers to an array of length 2
 $a = 10,20,30                       # $a refers to a different array, of length 3
 $a = "red",10.6                     # $a refers to a different array, of length 2
 $a = New-Object 'int[,]' 2,3        # $a refers to an array of rank 2

Assignment of an array involves a shallow copy; that is, the variable assigned to refers to the
same array, no copy of the array is made. For example,

 PowerShell

 $a = 10,20,30
 ">$a<"
 $b = $a            # make $b refer to the same array as $a
 ">$b<"

 $a[0] = 6          # change value of [0] via $a
 ">$a<"
 ">$b<"             # change is reflected in $b

 $b += 40           # make $b refer to a new array
 $a[0] = 8          # change value of [0] via $a
 ">$a<"
 ">$b<"             # change is not reflected in $b

The following is written to the pipeline:

 Output

<!-- p.1346 -->

 >10 20 30<
 >10 20 30<
 >6 20 30<
 >6 20 30<
 >8 20 30<
 >6 20 30 40<

9.6 Arrays as array elements
Any element of an array can itself be an array. For example,

 PowerShell

 $colors = "red", "blue", "green"
 $list = $colors, (,7), (1.2, "yes") # parens in (,7) are redundant; they
                                     # are intended to aid readability
 "`$list refers to an array of length $($list.Length)"
 ">$($list[1][0])<"
 ">$($list[2][1])<"

The following is written to the pipeline:

 Output

 $list refers to an array of length 3
 >7<
 >yes<

$list[1] refers to an array of 1 element, the integer 7, which is accessed via $list[1][0] , as

shown. Compare this with the following subtly different case:

 PowerShell

 $list = $colors, 7, (1.2, "yes") # 7 has no prefix comma
 ">$($list[1])<"

Here, $list[1] refers to a scalar, the integer 7, which is accessed via $list[1] .

Consider the following example,

 PowerShell

 $x = [string[]]("red","green")
 $y = 12.5, $true, "blue"
 $a = New-Object 'object[,]' 2,2
 $a[0,0] = $x               # element is an array of 2 strings

<!-- p.1347 -->

  $a[0,1] = 20                   # element is an int
  $a[1,0] = $y                   # element is an array of 3 objects
  $a[1,1] = [int[]](92,93)       # element is an array of 2 ints

9.7 Negative subscripting
This is discussed in §7.1.4.1.

9.8 Bounds checking
This is discussed in §7.1.4.1.

9.9 Array slices
An array slice is an unconstrained 1-dimensional array whose elements are copies of zero or
more elements from a collection. An array slice is created via the subscript operator []
(§7.1.4.5).

9.10 Copying an array
A contiguous set of elements can be copied from one array to another using the method
[array]::Copy . For example,

  PowerShell

  $a = [int[]](10,20,30)
  $b = [int[]](0,1,2,3,4,5)
  [array]::Copy($a, $b, 2)           # $a[0]->$b[0],
  $a[1]->$b[1]
  [array]::Copy($a, 1, $b, 3, 2)      # $a[1]->$b[3],
  $a[2]->$b[4]

9.11 Enumerating over an array
Although it is possible to loop through an array accessing each of its elements via the subscript
operator, we can enumerate over that array's elements using the foreach statement. For a
multidimensional array, the elements are processed in row-major order. For example,

  PowerShell

  $a = 10, 53, 16, -43
  foreach ($elem in $a) {

<!-- p.1348 -->

       # do something with element via $elem
  }

  foreach ($elem in -5..5) {
      # do something with element via $elem
  }

  $a = New-Object 'int[,]' 3, 2
  foreach ($elem in $a) {
      # do something with element via $elem
  }

9.12 Multidimensional array flattening
Some operations on a multidimensional array (such as replication (§7.6.3) and concatenation
(§7.7.3)) require that array to be flattened; that is, to be turned into a 1-dimensional array of
unconstrained type. The resulting array takes on all the elements in row-major order.

Consider the following example:

  PowerShell

  $a = "red",$true
  $b = (New-Object 'int[,]' 2,2)
  $b[0,0] = 10
  $b[0,1] = 20
  $b[1,0] = 30
  $b[1,1] = 40
  $c = $a + $b

The array designated by $c contains the elements "red", $true , 10, 20, 30, and 40.

 Last updated on 03/24/2025

<!-- p.1349 -->

10. Hashtables
Article • 01/08/2025

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December
  2012 and is based on Windows PowerShell 3.0. This specification does not reflect
  the current state of PowerShell. There is no plan to update this documentation to
  reflect the current state. This documentation is presented here for historical
  reference.

  The specification document is available as a Microsoft Word document from the
  Microsoft Download Center at:
  https://www.microsoft.com/download/details.aspx?id=36389             That Word
  document has been converted for presentation here on Microsoft Learn. During
  conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

Syntax:

   Tip

  The ~opt~ notation in the syntax definitions indicates that the lexical entity is
  optional in the syntax.

  Syntax

  hash-literal-expression:
      @{ new-lines~opt~ hash-literal-body~opt~ new-lines~opt~ }

  hash-literal-body:
      hash-entry
      hash-literal-body statement-terminators hash-entry

  hash-entry:
      key-expression = new-lines~opt~ statement

  key-expression:
      simple-name
      unary-expression

<!-- p.1350 -->

  statement-terminator:
      ;
      new-line-character

10.1 Introduction
The type Hashtable represents a collection of key/value pair objects that supports
efficient retrieval of a value when indexed by the key. Each key/value pair is an element,
which is stored in some implementation-defined object type.

An element's key cannot be the null value. There are no restrictions on the type of a key
or value. Duplicate keys are not supported.

Given a key/value pair object, the key and associated value can be obtained by using the
instance properties Key and Value, respectively.

Given one or more keys, the corresponding value(s) can be accessed via the Hashtable
subscript operator [] (§7.1.4.3).

All Hashtables have type Hashtable (§4.3.3).

The order of the keys in the collection returned by Keys is unspecified; however, it is the
same order as the associated values in the collection returned by Values.

Here are some examples involving Hashtables:

  PowerShell

  $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123 }
  $h1.FirstName # designates the key FirstName
  $h1["LastName"] # designates the associated value for key LastName
  $h1.Keys # gets the collection of keys

Hashtable elements are stored in an object of type DictionaryEntry, and the collections

returned by Keys and Values have type ICollection.

10.2 Hashtable creation
A Hashtable is created via a hash literal (§7.1.9) or the New-Object cmdlet. It can be
created with zero or more elements. The Count property returns the current element
count.

<!-- p.1351 -->

10.3 Adding and removing Hashtable elements
An element can be added to a Hashtable by assigning (§7.11.1) a value to a non-existent
key name or to a subscript (§7.1.4.3) that uses a non-existent key name. Removal of an
element requires the use of the Remove method. For example,

  PowerShell

  $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123 }
  $h1.Dept = "Finance" # adds element Finance
  $h1["Salaried"] = $false # adds element Salaried
  $h1.Remove("Salaried") # removes element Salaried

10.4 Hashtable concatenation
Hashtables can be concatenated via the + and += operators, both of which result in the
creation of a new Hashtable . The existing Hashtables are unchanged. See §7.7.4 for
more information.

10.5 Hashtables as reference types
As Hashtable is a reference type, assignment of a Hashtable involves a shallow copy;
that is, the variable assigned to refers to the same Hashtable ; no copy of the Hashtable
is made. For example,

  PowerShell

  $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123 }
  $h2 = $h1
  $h1.FirstName = "John" # change key's value in $h1
  $h2.FirstName # change is reflected in $h2

10.6 Enumerating over a Hashtable
To process every pair in a Hashtable , use the Keys property to retrieve the list of keys as
an array, and then enumerate over the elements of that array getting the associated
value via the Value property or a subscript, as follows

  PowerShell

<!-- p.1352 -->

$h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123}
foreach ($e in $h1.Keys) {
   "Key is " + $e + ", Value is " + $h1[$e]
}

<!-- p.1353 -->

11. Modules

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December 2012 and
  is based on Windows PowerShell 3.0. This specification does not reflect the current state
  of PowerShell. There is no plan to update this documentation to reflect the current state.
  This documentation is presented here for historical reference.

  The specification document is available as a Microsoft Word document from the Microsoft
  Download Center at: https://www.microsoft.com/download/details.aspx?id=36389
  That Word document has been converted for presentation here on Microsoft Learn.
  During conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

11.1 Introduction
As stated in §3.14, a module is a self-contained reusable unit that allows PowerShell code to be
partitioned, organized, and abstracted. A module can contain one or more module members,
which are commands (such as cmdlets and functions) and items (such as variables and aliases).
The names of these members can be kept private to the module or they may be exported to
the session into which the module is imported.

There are three different module types: manifest, script, and binary. A manifest module is a file
that contains information about a module, and controls certain aspects of that module's use. A
script module is a PowerShell script file with a file extension of .psm1 instead of .ps1 . A binary
module contains class types that define cmdlets and providers. Unlike script modules, binary
modules are written in compiled languages. Binary modules are not covered by this
specification.

A binary module is a .NET assembly (i.e.; a DLL) that was compiled against the PowerShell
libraries.

<!-- p.1354 -->

Modules may nest; that is, one module may import another module. A module that has
associated nested modules is a root module.

When a PowerShell session is created, by default, no modules are imported.

When modules are imported, the search path used to locate them is defined by the
environment variable PSModulePath.

The following cmdlets deal with modules:

     Get-Module: Identifies the modules that have been, or can be imported
     Import-Module: Adds one or more modules to the current session (see §11.4)
     Export-ModuleMember: Identifies the module members that are to be exported
     Remove-Module: Removes one or more modules from the current session (see §11.5)
     New-Module: Creates a dynamic module (see §11.7)

11.2 Writing a script module
A script module is a script file. Consider the following script module:

 PowerShell

 function Convert-CentigradeToFahrenheit ([double]$tempC) {
     return ($tempC * (9.0 / 5.0)) + 32.0
 }
 New-Alias c2f Convert-CentigradeToFahrenheit

 function Convert-FahrenheitToCentigrade ([double]$tempF) {
     return ($tempF - 32.0) * (5.0 / 9.0)
 }
 New-Alias f2c Convert-FahrenheitToCentigrade

 Export-ModuleMember -Function Convert-CentigradeToFahrenheit
 Export-ModuleMember -Function Convert-FahrenheitToCentigrade
 Export-ModuleMember -Alias c2f, f2c

This module contains two functions, each of which has an alias. By default, all function names,
and only function names are exported. However, once the cmdlet Export-ModuleMember has
been used to export anything, then only those things exported explicitly will be exported. A
series of commands and items can be exported in one call or a number of calls to this cmdlet;
such calls are cumulative for the current session.

11.3 Installing a script module

<!-- p.1355 -->

A script module is defined in a script file, and modules can be stored in any directory. The
environment variable PSModulePath points to a set of directories to be searched when
module-related cmdlets look for modules whose names do not include a fully qualified path.
Additional lookup paths can be provided; for example,

$Env:PSModulePath = $Env:PSModulePath + ";<additional-path>"

Any additional paths added affect the current session only.

Alternatively, a fully qualified path can be specified when a module is imported.

11.4 Importing a script module
Before the resources in a module can be used, that module must be imported into the current
session, using the cmdlet Import-Module . Import-Module can restrict the resources that it
actually imports.

When a module is imported, its script file is executed. That process can be configured by
defining one or more parameters in the script file, and passing in corresponding arguments via
the ArgumentList parameter of Import-Module .

Consider the following script that uses these functions and aliases defined in §11.2:

Import-Module "E:\Scripts\Modules\PSTest_Temperature" -Verbose

 PowerShell

 "0 degrees C is " + (Convert-CentigradeToFahrenheit 0) + " degrees F"
 "100 degrees C is " + (c2f 100) + " degrees F"
 "32 degrees F is " + (Convert-FahrenheitToCentigrade 32) + " degrees C"
 "212 degrees F is " + (f2c 212) + " degrees C"

Importing a module causes a name conflict when commands or items in the module have the
same names as commands or items in the session. A name conflict results in a name being
hidden or replaced. The Prefix parameter of Import-Module can be used to avoid naming
conflicts. Also, the Alias, Cmdlet, Function, and Variable parameters can limit the selection of
commands to be imported, thereby reducing the chances of name conflict.

Even if a command is hidden, it can be run by qualifying its name with the name of the module
in which it originated. For example, & M\F 100 invokes the function F in module M, and passes
it the argument 100.

<!-- p.1356 -->

When the session includes commands of the same kind with the same name, such as two
cmdlets with the same name, by default it runs the most recently added command.

See §3.5.6 for a discussion of scope as it relates to modules.

11.5 Removing a script module
One or more modules can be removed from a session via the cmdlet Remove-Module .

Removing a module does not uninstall the module.

In a script module, it is possible to specify code that is to be executed prior to that module's
removal, as follows:

$MyInvocation.MyCommand.ScriptBlock.Module.OnRemove = { *on-removal-code* }

11.6 Module manifests
As stated in §11.1, a manifest module is a file that contains information about a module, and
controls certain aspects of that module's use.

A module need not have a corresponding manifest, but if it does, that manifest has the same
name as the module it describes, but with a .psd1 file extension.

A manifest contains a limited subset of PowerShell script, which returns a Hashtable containing
a set of keys. These keys and their values specify the manifest elements for that module. That is,
they describe the contents and attributes of the module, define any prerequisites, and
determine how the components are processed.

Essentially, a manifest is a data file; however, it can contain references to data types, the if
statement, and the arithmetic and comparison operators. (Assignments, function definitions
and loops are not permitted.) A manifest also has read access to environment variables and it
can contain calls to the cmdlet Join-Path , so paths can be constructed.

  ７ Note

  Editor's Note: The original document contains a list of keys allowed in a module manifest
  file. That list is outdated and incomplete. For a complete list of keys in a module manifest,
  see New-ModuleManifest.

The only key that is required is ModuleVersion.

<!-- p.1357 -->

Here is an example of a simple manifest:

 PowerShell

 @{
 ModuleVersion = '1.0'
 Author = 'John Doe'
 RequiredModules = @()
 FunctionsToExport = 'Set*','Get*','Process*'
 }

The key GUID has a string value. This specifies a Globally Unique IDentifier (GUID) for the
module. The GUID can be used to distinguish among modules having the same name. To
create a new GUID, call the method [guid]::NewGuid() .

11.7 Dynamic modules
A dynamic module is a module that is created in memory at runtime by the cmdlet New-Module ;
it is not loaded from disk. Consider the following example:

 PowerShell

 $sb = {
     function Convert-CentigradeToFahrenheit ([double]$tempC) {
         return ($tempC * (9.0 / 5.0)) + 32.0
     }

      New-Alias c2f Convert-CentigradeToFahrenheit

      function Convert-FahrenheitToCentigrade ([double]$tempF) {
          return ($tempF - 32.0) * (5.0 / 9.0)
      }

      New-Alias f2c Convert-FahrenheitToCentigrade

      Export-ModuleMember -Function Convert-CentigradeToFahrenheit
      Export-ModuleMember -Function Convert-FahrenheitToCentigrade
      Export-ModuleMember -Alias c2f, f2c
 }

 New-Module -Name MyDynMod -ScriptBlock $sb
 Convert-CentigradeToFahrenheit 100
 c2f 100

The script block $sb defines the contents of the module, in this case, two functions and two
aliases to those functions. As with an on-disk module, only functions are exported by default,
so Export-ModuleMember cmdlets calls exist to export both the functions and the aliases.

<!-- p.1358 -->

Once New-Module runs, the four names exported are available for use in the session, as is shown
by the calls to the Convert-CentigradeToFahrenheit and c2f.

Like all modules, the members of dynamic modules run in a private module scope that is a
child of the global scope. Get-Module cannot get a dynamic module, but Get-Command can get
the exported members.

To make a dynamic module available to Get-Module , pipe a New-Module command to Import-
Module , or pipe the module object that New-Module returns, to Import-Module . This action adds

the dynamic module to the Get-Module list, but it does not save the module to disk or make it
persistent.

11.8 Closures
A dynamic module can be used to create a closure, a function with attached data. Consider the
following example:

  PowerShell

  function Get-NextID ([int]$StartValue = 1) {
      $nextID = $StartValue
      {
          ($Script:nextID++)
      }.GetNewClosure()
  }

  $v1 = Get-NextID         # get a scriptblock with $StartValue of 0
  & $v1                    # invoke Get-NextID getting back 1
  & $v1                    # invoke Get-NextID getting back 2

  $v2 = Get-NextID 100     # get a scriptblock with $StartValue of 100
  & $v2                    # invoke Get-NextID getting back 100
  & $v2                    # invoke Get-NextID getting back 101

The intent here is that Get-NextID return the next ID in a sequence whose start value can be
specified. However, multiple sequences must be supported, each with its own $StartValue and
$nextID context. This is achieved by the call to the method [scriptblock]::GetNewClosure

(§4.3.7).

Each time a new closure is created by GetNewClosure , a new dynamic module is created, and
the variables in the caller's scope (in this case, the script block containing the increment) are
copied into this new module. To ensure that the nextId defined inside the parent function (but
outside the script block) is incremented, the explicit Script: scope prefix is needed.

<!-- p.1359 -->

Of course, the script block need not be a named function; for example:

 PowerShell

 $v3 = & {      # get a scriptblock with $StartValue of 200
     param ([int]$StartValue = 1)
     $nextID = $StartValue
     {
         ($Script:nextID++)
     }.GetNewClosure()
 } 200

 & $v3              # invoke script getting back 200
 & $v3              # invoke script getting back 201

Last updated on 03/24/2025

<!-- p.1360 -->

12. Attributes
Article • 03/24/2025

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December
  2012 and is based on Windows PowerShell 3.0. This specification does not reflect
  the current state of PowerShell. There is no plan to update this documentation to
  reflect the current state. This documentation is presented here for historical
  reference.

  The specification document is available as a Microsoft Word document from the
  Microsoft Download Center at:
  https://www.microsoft.com/download/details.aspx?id=36389             That Word
  document has been converted for presentation here on Microsoft Learn. During
  conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

An attribute object associates predefined system information with a target element,
which can be a param block or a parameter (§8.10). Each attribute object has an attribute
type.

Information provided by an attribute is also known as metadata. Metadata can be
examined by the command or the execution environment to control how the command
processes data or before run time by external tools to control how the command itself is
processed or maintained.

Multiple attributes can be applied to the same target element.

12.1 Attribute specification

   Tip

  The ~opt~ notation in the syntax definitions indicates that the lexical entity is
  optional in the syntax.
