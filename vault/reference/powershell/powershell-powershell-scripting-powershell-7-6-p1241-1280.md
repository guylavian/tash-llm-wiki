---
title: "How to use this documentation — pages 1241-1280"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1241-1280
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1241-1280
family: powershell
documentKind: "doc"
abstract: "5.2.3 Array elements An array can be created via a unary comma operator (§7.2.1), sub-expression (§7.1.6), array-expression (§7.1.7), binary comma operator (§7.3), range operator (§7.4), or New- Object cmdlet. Memory for creating and deleting arrays is managed by the host enviro"
---

# How to use this documentation — pages 1241-1280

<!-- p.1241 -->

5.2.3 Array elements
An array can be created via a unary comma operator (§7.2.1), sub-expression (§7.1.6),
array-expression (§7.1.7), binary comma operator (§7.3), range operator (§7.4), or New-
Object cmdlet.

Memory for creating and deleting arrays is managed by the host environment and the
garbage collection system.

Arrays and array elements are discussed in §9.

5.2.4 Hashtable key/value pairs
A Hashtable is created via a hash literal (§2.3.5.6) or the New-Object cmdlet. A new
key/value pair can be added via the [] operator (§7.1.4.3).

Memory for creating and deleting Hashtables is managed by the host environment and
the garbage collection system.

Hashtables are discussed in §10.

5.2.5 Parameters
A parameter is created when its parent command is invoked, and it is initialized with the
value of the argument provided in the invocation or by the host environment. A
parameter ceases to exist when its parent command terminates.

Parameters are discussed in §8.10.

5.2.6 Ordinary variables
An ordinary variable is defined by an assignment-expression (§7.11) or a foreach-
statement (§8.4.4). Some ordinary variables are predefined by the host environment
while others are transient, coming and going as needed at runtime.

The lifetime of an ordinary variable is that part of program execution during which
storage is guaranteed to be reserved for it. This lifetime begins at entry into the scope
with which it is associated, and ends no sooner than the end of the execution of that
scope. If the parent scope is entered recursively or iteratively, a new instance of the local
variable is created each time.

The storage referred to by an ordinary variable is reclaimed independently of the
lifetime of that variable.

<!-- p.1242 -->

An ordinary variable can be named explicitly with a Variable: namespace prefix (§5.2.7).

5.2.7 Variables on provider drives
The concept of providers and drives is introduced in §3.1, with each provider being able
to provide its own namespace drive(s). This allows resources on those drives to be
accessed as though they were ordinary variables (§5.2.6). In fact, an ordinary variable is
stored on the file system provider drive Variable: (§3.1.5) and can be accessed by its
ordinary name or its fully qualified namespace name.

Some namespace variable types are constrained implicitly (§5.3).

5.3 Constrained variables
By default, a variable may designate a value of any type. However, a variable may be
constrained to designating values of a given type by specifying that type as a type literal
before its name in an assignment or a parameter. For example,

  PowerShell

  [int]$i = 10     # constrains $i to designating ints only
  $i = "Hello"     # error, no conversion to int
  $i = "0x10"      # ok, conversion to int
  $i = $true       # ok, conversion to int

  function F ([int]$p1, [switch]$p2, [regex]$p3) { ... }

Any variable belonging to the namespace Env:, Alias:, or to the file system namespace
(§2.3.2, §3.1) is constrained implicitly to the type string . Any variable belonging to the
namespace Function: (§2.3.2, §3.1) is constrained implicitly to the type scriptblock .

<!-- p.1243 -->

6. Conversions

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

A type conversion is performed when a value of one type is used in a context that requires a
different type. If such a conversion happens automatically it is known as implicit conversion. (A
common example of this is with some operators that need to convert one or more of the
values designated by their operands.) Implicit conversion is permitted provided the sense of
the source value is preserved, such as no loss of precision of a number when it is converted.

The cast operator (§7.2.9) allows for explicit conversion.

Conversions are discussed below, with supplementary information being provided as necessary
in the description of each operator in §6.19.

Explicit conversion of a value to the type it already has causes no change to that value or its
representation.

The rules for handing conversion when the value of an expression is being bound to a
parameter are covered in §6.17.

6.1 Conversion to void
A value of any type can be discarded explicitly by casting it to type void. There is no result.

<!-- p.1244 -->

6.2 Conversion to bool
The rules for converting any value to type bool are as follows:

     A numeric or char value of zero is converted to False; a numeric or char value of non-zero
     is converted to True.
     A value of null type is converted to False.
     A string of length 0 is converted to False; a string of length > 0 is converted to True.
     A [switch] parameter with value $true is converted to True, and one with value $false
     is converted to False.
     All other non-null reference type values are converted to True.

If the type implements IList:

     If the object's Length > 2, the value is converted to True.
     If the object's Length is 1 and that first element is not itself an IList, then if that element's
     value is true, the value is converted to True.
     Otherwise, if the first element's Count >= 1, the value is converted to True.
     Otherwise, the value is converted to False.

6.3 Conversion to char
The rules for converting any value to type char are as follows:

     The conversion of a value of type bool, decimal, float, or double is in error.
     A value of null type is converted to the null (U+0000) character.
     An integer type value whose value can be represented in type char has that value;
     otherwise, the conversion is in error.
     The conversion of a string value having a length other than 1 is in error.
     A string value having a length 1 is converted to a char having that one character's value.
     A numeric type value whose value after rounding of any fractional part can be
     represented in the destination type has that rounded value; otherwise, the conversion is
     in error.
     For other reference type values, if the reference type supports such a conversion, that
     conversion is used; otherwise, the conversion is in error.

6.4 Conversion to integer
The rules for converting any value to type byte, int, or long are as follows:

<!-- p.1245 -->

     The bool value False is converted to zero; the bool value True is converted to 1.
     A char type value whose value can be represented in the destination type has that value;
     otherwise, the conversion is in error.
     A numeric type value whose value after rounding of any fractional part can be
     represented in the destination type has that rounded value; otherwise, the conversion is
     in error.
     A value of null type is converted to zero.
     A string that represents a number is converted as described in §6.16. If after truncation of
     the fractional part the result can be represented in the destination type the string is well
     formed and it has the destination type; otherwise, the conversion is in error. If the string
     does not represent a number, the conversion is in error.
     For other reference type values, if the reference type supports such a conversion, that
     conversion is used; otherwise, the conversion is in error.

6.5 Conversion to float and double
The rules for converting any value to type float or double are as follows:

     The bool value False is converted to zero; the bool value True is converted to 1.
     A char value is represented exactly.
     A numeric type value is represented exactly, if possible; however, for int, long, and
     decimal conversions to float, and for long and decimal conversions to double, some of
     the least significant bits of the integer value may be lost.
     A value of null type is converted to zero.
     A string that represents a number is converted as described in §6.16; otherwise, the
     conversion is in error.
     For other reference type values, if the reference type supports such a conversion, that
     conversion is used; otherwise, the conversion is in error.

6.6 Conversion to decimal
The rules for converting any value to type decimal are as follows:

     The bool value False is converted to zero; the bool value True is converted to 1.
     A char type value is represented exactly.
     A numeric type value is represented exactly; however, if that value is too large or too
     small to fit in the destination type, the conversion is in error.
     A value of null type is converted to zero.

<!-- p.1246 -->

     A string that represents a number is converted as described in §6.16; otherwise, the
     conversion is in error.
     For other reference type values, if the reference type supports such a conversion, that
     conversion is used; otherwise, the conversion is in error.
     The scale of the result of a successful conversion is such that the fractional part has no
     trailing zeros.

6.7 Conversion to object
The value of any type except the null type (4.1.2) can be converted to type object. The value
retains its type and representation.

6.8 Conversion to string
The rules for converting any value to type string are as follows:

     The bool value $false is converted to "False"; the bool value $true is converted to
     "True".
     A char type value is converted to a 1-character string containing that char.
     A numeric type value is converted to a string having the form of a corresponding numeric
     literal. However, the result has no leading or trailing spaces, no leading plus sign, integers
     have base 10, and there is no type suffix. For a decimal conversion, the scale is preserved.
     For values of -∞, +∞, and NaN, the resulting strings are "-Infinity", "Infinity", and "NaN",
     respectively.
     A value of null type is converted to the empty string.
     For a 1-dimensional array, the result is a string containing the value of each element in
     that array, from start to end, converted to string, with elements being separated by the
     current Output Field Separator (§2.3.2.2). For an array having elements that are
     themselves arrays, only the top-level elements are converted. The string used to represent
     the value of an element that is an array, is implementation defined. For a multi-
     dimensional array, it is flattened (§9.12) and then treated as a 1‑dimensional array.
     A value of null type is converted to the empty string.
     A scriptblock type value is converted to a string containing the text of that block without
     the delimiting { and } characters.
     For an enumeration type value, the result is a string containing the name of each
     enumeration constant encoded in that value, separated by commas.
     For other reference type values, if the reference type supports such a conversion, that
     conversion is used; otherwise, the conversion is in error.

<!-- p.1247 -->

The string used to represent the value of an element that is an array has the form
System.Type[] , System.Type[,] , and so on. For other reference types, the method ToString is

called. For other enumerable types, the source value is treated like a 1-dimensional array.

6.9 Conversion to array
The rules for converting any value to an array type are as follows:

     The target type may not be a multidimensional array.
     A value of null type is retained as is.
     For a scalar value other than $null or a value of type hashtable, a new 1-element array is
     created whose value is the scalar after conversion to the target element type.
     For a 1-dimensional array value, a new array of the target type is created, and each
     element is copied with conversion from the source array to the corresponding element in
     the target array.
     For a multi-dimensional array value, that array is first flattened (§9.12), and then treated as
     a 1-dimensional array value.
     A string value is converted to an array of char having the same length with successive
     characters from the string occupying corresponding positions in the array.

For other enumerable types, a new 1-element array is created whose value is the
corresponding element after conversion to the target element type, if such a conversion exists.
Otherwise, the conversion is in error.

6.10 Conversion to xml
The object is converted to type string and then into an XML Document object of type xml .

6.11 Conversion to regex
An expression that designates a value of type string may be converted to type regex .

6.12 Conversion to scriptblock
The rules for converting any value to type scriptblock are as follows:

     A string value is treated as the name of a command optionally following by arguments to
     a call to that command.

<!-- p.1248 -->

6.13 Conversion to enumeration types
The rules for converting any value to an enumeration type are as follows:

     A value of type string that contains one of the named values (with regard for case) for an
     enumeration type is converted to that named value.
     A value of type string that contains a comma-separated list of named values (with regard
     for case) for an enumeration type is converted to the bitwise-OR of all those named
     values.

6.14 Conversion to other reference types
The rules for converting any value to a reference type other than an array type or string are as
follows:

     A value of null type is retained as is.
     Otherwise, the behavior is implementation defined.

A number of pieces of machinery come in to play here; these include the possible use of single
argument constructors or default constructors if the value is a hashtable, implicit and explicit
conversion operators, and Parse methods for the target type; the use of Convert.ConvertTo;
and the ETS conversion mechanism.

6.15 Usual arithmetic conversions
If neither operand designates a value having numeric type, then

     If the left operand designates a value of type bool, the conversion is in error.
     Otherwise, all operands designating the value $null are converted to zero of type int and
     the process continues with the numeric conversions listed below.
     Otherwise, if the left operand designates a value of type char and the right operand
     designates a value of type bool, the conversion is in error.
     Otherwise, if the left operand designates a value of type string but does not represent a
     number (§6.16), the conversion is in error.
     Otherwise, if the right operand designates a value of type string but does not represent a
     number (§6.16), the conversion is in error.
     Otherwise, all operands designating values of type string are converted to numbers
     (§6.16), and the process continues with the numeric conversions listed below.
     Otherwise, the conversion is in error.

<!-- p.1249 -->

Numeric conversions:

      If one operand designates a value of type decimal, the value designated by the other
      operand is converted to that type, if necessary. The result has type decimal.
      Otherwise, if one operand designates a value of type double, the value designated by the
      other operand is converted to that type, if necessary. The result has type double.
      Otherwise, if one operand designates a value of type float, the values designated by both
      operands are converted to type double, if necessary. The result has type double.
      Otherwise, if one operand designates a value of type long, the value designated by the
      other operand value is converted to that type, if necessary. The result has the type first in
      the sequence long and double that can represent its value.
      Otherwise, the values designated by both operands are converted to type int, if necessary.
      The result has the first in the sequence int, long, double that can represent its value
      without truncation.

6.16 Conversion from string to numeric type
Depending on its contents, a string can be converted explicitly or implicitly to a numeric value.
Specifically,

      An empty string is converted to the value zero.
      Leading and trailing spaces are ignored; however, a string may not consist of spaces only.
      A string containing only white space and/or line terminators is converted to the value
      zero.
      One leading + or - sign is permitted.
      An integer number may have a hexadecimal prefix (0x or 0X).
      An optionally signed exponent is permitted.
      Type suffixes and multipliers are not permitted.
      The case-distinct strings "-Infinity", "Infinity", and "NaN" are recognized as the values -∞,
      +∞, and NaN, respectively.

6.17 Conversion during parameter binding
For information about parameter binding see §8.14.

When the value of an expression is being bound to a parameter, there are extra conversion
considerations, as described below:

<!-- p.1250 -->

     If the parameter type is switch (§4.2.5, §8.10.5) and the parameter has no argument, the
     value of the parameter in the called command is set to $true . If the parameter type is
     other than switch, a parameter having no argument is in error.
     If the parameter type is switch and the argument value is $null , the parameter value is
     set to $false .
     If the parameter type is object or is the same as the type of the argument, the argument's
     value is passed without conversion.
     If the parameter type is not object or scriptblock, an argument having type scriptblock is
     evaluated and its result is passed as the argument's value. (This is known as delayed script
     block binding.) If the parameter type is object or scriptblock, an argument having type
     scriptblock is passed as is.
     If the parameter type is a collection of type T2, and the argument is a scalar of type T1,
     that scalar is converted to a collection of type T2 containing one element. If necessary,
     the scalar value is converted to type T2 using the conversion rules of this section.
     If the parameter type is a scalar type other than object and the argument is a collection,
     the argument is in error.
     If the expected parameter type is a collection of type T2, and the argument is a collection
     of type T1, the argument is converted to a collection of type T2 having the same length as
     the argument collection. If necessary, the argument collection element values are
     converted to type T2 using the conversion rules of this section.
     If the steps above and the conversions specified earlier in this chapter do not suffice, the
     rules in §6.18 are applied. If those fail, the parameter binding fails.

6.18 .NET Conversion
For an implicit conversion, PowerShell's built-in conversions are tried first. If they cannot
resolve the conversion, the .NET custom converters below are tried, in order, from top to
bottom. If a conversion is found, but it throws an exception, the conversion has failed.

     PSTypeConverter: There are two ways of associating the implementation of the
     PSTypeConverter class with its target class: through the type configuration file
     (types.ps1xml) or by applying the System.ComponentModel.TypeConverterAttribute
     attribute to the target class. Refer to the PowerShell SDK documentation for more
     information.

     TypeConverter: This CLR type provides a unified way of converting types of values to
     other types, as well as for accessing standard values and sub-properties. The most
     common type of converter is one that converts to and from a text representation. The

<!-- p.1251 -->

     type converter for a class is bound to the class with a
      System.ComponentModel.TypeConverterAttribute . Unless this attribute is overridden, all

     classes that inherit from this class use the same type converter as the base class. Refer to
     the PowerShell SDK and the Microsoft .NET framework documentation for more
     information.

     Parse Method: If the source type is string and the destination type has a method called
      Parse , that method is called to perform the conversion.

     Constructors: If the destination type has a constructor taking a single argument whose
     type is that of the source type, that constructor is called to perform the conversion.

     Implicit Cast Operator: If the source type has an implicit cast operator that converts to
     the destination type, that operator is called to perform the conversion.

     Explicit Cast Operator: If the source type has an explicit cast operator that converts to the
     destination type, that operator is called to perform the conversion. If the destination type
     has an explicit cast operator that converts from the source type, that operator is called to
     perform the conversion.

     IConvertable: System.Convert.ChangeType is called to perform the conversion.

6.19 Conversion to ordered
The rules for converting any value to the pseudo-type ordered are as follows:

     If the value is a hash literal (§2.3.5.6), the result is an object with an implementation
     defined type that behaves like a hashtable and the order of the keys matches the order
     specified in the hash literal.
     Otherwise, the behavior is implementation defined.

Only hash literals (§2.3.5.6) can be converted to ordered. The result is an instance of
System.Collections.Specialized.OrderedDictionary .

6.20 Conversion to pscustomobject
The rules for converting any value to the pseudo-type pscustomobject are as follows:

     A value of type hashtable is converted to a PowerShell object. Each key in the hashtable
     becomes a NoteProperty with the corresponding value.
     Otherwise, the behavior is implementation defined.

<!-- p.1252 -->

The conversion is always allowed but does not change the type of the value.

Last updated on 04/08/2026

<!-- p.1253 -->

7. Expressions
Article • 04/25/2024

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December
  2012 and is based on Windows PowerShell 3.0. This specification does not reflect
  the current state of PowerShell. There is no plan to update this documentation to
  reflect the current state. This documentation is presented here for historical
  reference.

  The specification document is available as a Microsoft Word document from the
  Microsoft Download Center at:
  https://www.microsoft.com/download/details.aspx?id=36389            That Word
  document has been converted for presentation here on Microsoft Learn. During
  conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

Syntax:

  Syntax

  expression:
      primary-expression
      bitwise-expression
      logical-expression
      comparison-expression
      additive-expression
      multiplicative-expression

  dash: one of
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

  dashdash:
      dash dash

Description:

<!-- p.1254 -->

An expression is a sequence of operators and operands that designates a method, a
function, a writable location, or a value; specifies the computation of a value; produces
one or more side effects; or performs some combination thereof. For example,

     The literal 123 is an expression that designates the int value 123.
     The expression 1,2,3,4 designates the 4-element array object having the values
     shown.
     The expression 10.4 * $a specifies a computation.
     The expression $a++ produces a side effect.
     The expression $a[$i--] = $b[++$j] performs a combination of these things.

Except as specified for some operators, the order of evaluation of terms in an expression
and the order in which side effects take place are both unspecified. Examples of
unspecified behavior include the following: $i++ + $i , $i + --$i , and $w[$j++] =
$v[$j] .

An implementation of PowerShell may provide support for user-defined types, and
those types may have operations defined on them. All details of such types and
operations are implementation defined.

A top-level expression is one that is not part of some larger expression. If a top-level
expression contains a side-effect operator the value of that expression is not written to
the pipeline; otherwise, it is. See §7.1.1 for a detailed discussion of this.

Ordinarily, an expression that designates a collection ([§4§4]) is enumerated into its
constituent elements when the value of that expression is used. However, this is not the
case when the expression is a cmdlet invocation. For example,

  PowerShell

  $x = 10,20,30
  $a = $($x; 99)                            # $a.Length is 4

  $x = New-Object 'int[]' 3
  $a = $($x; 99)                            # equivalent, $a.Length is 4

  $a = $(New-Object 'int[]' 3; 99)          # $a.Length is 2

In the first two uses of the $(...) operator, the expression designating the collection is
the variable $x , which is enumerated resulting in three int values, plus the int 99.
However, in the third case, the expression is a direct call to a cmdlet, so the result is not
enumerated, and $a is an array of two elements, int[3] and int .

<!-- p.1255 -->

If an operation is not defined by PowerShell, the type of the value designated by the left
operand is inspected to see if it has a corresponding op_<operation> method.

7.1 Primary expressions
Syntax:

  Syntax

  primary-expression:
      value
      member-access
      element-access
      invocation-expression
      post-increment-expression
      post-decrement-expression

  value:
      parenthesized-expression
      sub-expression
      array-expression
      script-block-expression
      hash-literal-expression
      literal
      type-literal
      variable

7.1.1 Grouping parentheses
Syntax:

   Tip

  The ~opt~ notation in the syntax definitions indicates that the lexical entity is
  optional in the syntax.

  Syntax

  parenthesized-expression:
      ( new-lines~opt~ pipeline new-lines~opt~ )

Description:

A parenthesized expression is a primary-expression whose type and value are the same
as those of the expression without the parentheses. If the expression designates a

<!-- p.1256 -->

variable then the parenthesized expression designates that same variable. For example,
$x.m and ($x).m are equivalent.

Grouping parentheses may be used in an expression to document the default
precedence and associativity within that expression. They can also be used to override
that default precedence and associativity. For example,

  PowerShell

  4 + 6 * 2       # 16
  4 + (6 * 2)     # 16 document default precedence
  (4 + 6) * 2     # 20 override default precedence

Ordinarily, grouping parentheses at the top-most level are redundant. However, that is
not always the case. Consider the following example:

  PowerShell

  2,4,6          # Length 3; values 2,4,6
  (2,4),6        # Length 2; values [Object[]],int

In the second case, the parentheses change the semantics, resulting in an array whose
two elements are an array of 2 ints and the scalar int 6.

Here's another exception:

  PowerShell

  23.5/2.4              # pipeline gets 9.79166666666667
  $a = 1234 * 3.5       # value not written to pipeline
  $a                    # pipeline gets 4319

In the first and third cases, the value of the result is written to the pipeline. However,
although the expression in the second case is evaluated, the result is not written to the
pipeline due to the presence of the side-effect operator = at the top level. (Removal of
the $a = part allows the value to be written, as * is not a side-effect operator.)

To stop a value of any expression not containing top-level side effects from being
written to the pipeline, discard it explicitly, as follows:

  PowerShell

  # None of these value are written to pipeline
  [void](23.5/2.4)
  [void]$a

<!-- p.1257 -->

   $null = $a
   $a > $null

To write to the pipeline the value of any expression containing top-level side effects,
enclose that expression in parentheses, as follows:

   PowerShell

   ($a = 1234 * 3.5) # pipeline gets 4319

As such, the grouping parentheses in this case are not redundant.

In the following example, we have variable substitution (§2.3.5.2) taking place in a string
literal:

   PowerShell

   ">$($a = -23)<"      # value not written to pipeline, get ><
   ">$(($a = -23))<"    # pipeline gets >-23<

In the first case, the parentheses represent a sub-expression's delimiters not grouping
parentheses, and as the top-level expression contains a side-effect operator, the
expression's value is not written to the pipeline. Of course, the > and < characters are
still written.) If grouping parenthesis are added -- as shown in the second case -- writing
is enabled.

The following examples each contain top-level side-effect operators:

   PowerShell

   $a = $b = 0         # value not written to pipeline
   $a = ($b = 0)       # value not written to pipeline
   ($a = ($b = 0))     # pipeline gets 0

   ++$a              # value not written to pipeline
   (++$b)            # pipeline gets 1

   $a--              # value not written to pipeline
   ($b--)            # pipeline gets 1

The use of grouping parentheses around an expression containing no top-level side
effects makes those parentheses redundant. For example;

   PowerShell

<!-- p.1258 -->

   $a          # pipeline gets 0
   ($a)        # no side effect, so () redundant

Consider the following example that has two side effects, neither of which is at the top
level:

  PowerShell

   12.6 + ($a = 10 - ++$b) # pipeline gets 21.6.

The result is written to the pipeline, as the top-level expression has no side effects.

7.1.2 Member access
Syntax:

  Syntax

   member-access:
       primary-expression . new-line~opt~ member-name
       primary-expression :: new-line~opt~ member-name

Note that no whitespace is allowed after primary-expression.

Description:

The operator . is used to select an instance member from an object, or a key from a
Hashtable . The left operand must designate an object, and the right operand must

designate an accessible instance member.

Either the right operand designates an accessible instance member within the type of
the object designated by the left operand or, if the left operand designates an array, the
right operand designates accessible instance members within each element of the array.

Whitespace is not permitted before the . operator.

This operator is left associative.

The operator :: is used to select a static member from a given type. The left operand
must designate a type, and the right-hand operand must designate an accessible static
member within that type.

Whitespace is not permitted before the :: operator.

<!-- p.1259 -->

This operator is left associative.

If the right-hand operand designates a writable location within the type of the object
designated by the left operand, then the whole expression designates a writable
location.

Examples:

  PowerShell

  $a = 10, 20, 30
  $a.Length                          # get instance property

  (10, 20, 30).Length

  $property = "Length"
  $a.$property                       # property name is a variable

  $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123
  }
  $h1.FirstName                # designates the key FirstName
  $h1.Keys                     # gets the collection of keys

  [int]::MinValue                    # get static property
  [double]::PositiveInfinity         # get static property
  $property = "MinValue"
  [long]::$property                  # property name is a variable

  foreach ($t in [byte], [int], [long]) {
      $t::MaxValue             # get static property
  }

  $a = @{ID = 1 }, @{ID = 2 }, @{ID = 3 }
  $a.ID                        # get ID from each element in the array

7.1.3 Invocation expressions
Syntax:

  Syntax

  invocation-expression:
      primary-expression . new-line~opt~ member-name argument-list
      primary-expression :: new-line~opt~ member-name argument-list

  argument-list:
      ( argument-expression-list~opt~ new-lines~opt~ )

Note that no whitespace is allowed after primary-expression.

<!-- p.1260 -->

Description:

An invocation-expression calls the method designated by primary-expression.member-
name or primary-expression::member-name . The parentheses in argument-list contain a

possibly empty, comma-separated list of expressions that designate the arguments
whose values are passed to the method. Before the method is called, the arguments are
evaluated and converted according to the rules of §6, if necessary, to match the types
expected by the method. The order of evaluation of primary-expression.member-name ,
primary-expression::member-name , and the arguments is unspecified.

This operator is left associative.

The type of the result of an invocation-expression is a method-designator (§4.5.24).

Examples:

  PowerShell

  [Math]::Sqrt(2.0)                  # call method with argument 2.0
  [char]::IsUpper("a")               # call method
  $b = "abc#$%XYZabc"
  $b.ToUpper()                       # call instance method

  [Math]::Sqrt(2)                    # convert 2 to 2.0 and call method
  [Math]::Sqrt(2D)                   # convert 2D to 2.0 and call method
  [Math]::Sqrt($true)                # convert $true to 1.0 and call method
  [Math]::Sqrt("20")                 # convert "20" to 20 and call method

  $a = [Math]::Sqrt                  # get method descriptor for Sqrt
  $a.Invoke(2.0)                     # call Sqrt via the descriptor
  $a = [Math]::("Sq"+"rt")           # get method descriptor for Sqrt
  $a.Invoke(2.0)                     # call Sqrt via the descriptor
  $a = [char]::ToLower               # get method descriptor for ToLower
  $a.Invoke("X")                     # call ToLower via the descriptor

7.1.4 Element access
Syntax:

  Syntax

  element-access:
      primary-expression [ new-lines~opt~ expression new-lines~opt~ ]

Description:

<!-- p.1261 -->

There must not be any whitespace between primary-expression and the left square
bracket ( [ ).

7.1.4.1 Subscripting an array

Description:

Arrays are discussed in detail in §9. If expression is a 1-dimensional array, see §7.1.4.5.

When primary-expression designates a 1-dimensional array A, the operator [] returns
the element located at A[0 + expression] after the value of expression has been
converted to int . The result has the element type of the array being subscripted. If
expression is negative, A[expression] designates the element located at A[A.Length +
expression] .

When primary-expression designates a 2-dimensional array B, the operator [] returns
the element located at B[0 + row,0 + column] after the value of the row and column
components of expression (which are specified as a comma-separated list) have been
converted to int . The result has the element type of the array being subscripted. Unlike
for a 1-dimensional array, negative positions have no special meaning.

When primary-expression designates an array of three or more dimensions, the rules for
2-dimensional arrays apply and the dimension positions are specified as a comma-
separated list of values.

If a read access on a non-existing element is attempted, the result is $null . It is an error
to write to a non-existing element.

For a multidimensional-array subscript expression, the order of evaluation of the
dimension position expressions is unspecified. For example, given a 3-dimensional array
$a , the behavior of $a[$i++,$i,++$i] is unspecified.

If expression is an array, see §7.1.4.5.

This operator is left associative.

Examples:

  PowerShell

   $a = [int[]](10,20,30) # [int[]], Length 3
   $a[1] # returns int 20
   $a[20] # no such position, returns $null
   $a[-1] # returns int 30, i.e., $a[$a.Length-1]
   $a[2] = 5 # changes int 30 to int 5

<!-- p.1262 -->

  $a[20] = 5 # implementation-defined behavior

  $a = New-Object 'double[,]' 3,2
  $a[0,0] = 10.5 # changes 0.0 to 10.5
  $a[0,0]++ # changes 10.5 to 10.6

  $list = ("red",$true,10),20,(1.2, "yes")
  $list[2][1] # returns string "yes"

  $a = @{ A = 10 },@{ B = $true },@{ C = 123.45 }
  $a[1]["B"] # $a[1] is a Hashtable, where B is a key

  $a = "red","green"
  $a[1][4] # returns string "n" from string in $a[1]

If a write access to a non-existing element is attempted, an IndexOutOfRange exception
is raised.

7.1.4.2 Subscripting a string
Description:

When primary-expression designates a string S, the operator [] returns the character
located in the zero-based position indicated by expression, as a char. If expression is
greater than or equal to that string's length, the result is $null . If expression is negative,
S[expression] designates the element located at S[S.Length + expression] .

Examples:

  PowerShell

  $s = "Hello"      # string, Length 5, positions 0-4
  $c = $s[1]        # returns "e" as a string
  $c = $s[20]       # no such position, returns $null
  $c = $s[-1]       # returns "o", i.e., $s[$s.Length-1]

7.1.4.3 Subscripting a Hashtable
Description:

When primary-expression designates a Hashtable, the operator [] returns the value(s)
associated with the key(s) designated by expression. The type of expression is not
restricted.

When expression is a single key name, the result is the associated value and has that
type, unless no such key exists, in which case, the result is $null . If $null is used as the

<!-- p.1263 -->

key the behavior is implementation defined. If expression is an array of key names, see
§7.1.4.5.

If expression is an array, see §7.1.4.5.

Examples:

  PowerShell

  $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123 }
  $h1['FirstName']     # the value associated with key FirstName
  $h1['BirthDate']     # no such key, returns $null

  $h1 = @{ 10 = "James"; 20.5 = "Anderson"; $true = 123 }
  $h1[10]              # returns value "James" using key 10
  $h1[20.5]            # returns value "Anderson" using key 20.5
  $h1[$true]           # returns value 123 using key $true

When expression is a single key name, if $null is used as the only value to subscript a
Hashtable, a NullArrayIndex exception is raised.

7.1.4.4 Subscripting an XML document

Description:

When primary-expression designates an object of type xml, expression is converted to
string, if necessary, and the operator [] returns the first child element having the name
specified by expression. The type of expression must be string. The type of the result is
implementation defined. The result can be subscripted to return its first child element. If
no child element exists with the name specified by expression, the result is $null . The
result does not designate a writable location.

Examples:

  PowerShell

  $x = [xml]@"
  <Name>
  <FirstName>Mary</FirstName>
  <LastName>King</LastName>
  </Name>
  "@

  $x['Name']                      # refers to the element Name
  $x['Name']['FirstName']         # refers to the element FirstName within Name
  $x['FirstName']                 # No such child element at the top level, result
  is $null

<!-- p.1264 -->

The type of the result is System.Xml.XmlElement or System.String .

7.1.4.5 Generating array slices
When primary-expression designates an object of a type that is enumerable (§4) or a
Hashtable, and expression is a 1-dimensional array, the result is an array slice (§9.9)
containing the elements of primary-expression designated by the elements of
expression.

In the case of a Hashtable, the array slice contains the associated values to the keys
provided, unless no such key exists, in which case, the corresponding element is $null .
If $null is used as any key name the behavior is implementation defined.

Examples:

  PowerShell

  $a = [int[]](30,40,50,60,70,80,90)
  $a[1,3,5]                 # slice has Length 3, value 40,60,80
  $a[,5]                    # slice with Length 1
  $a[@()]                   # slice with Length 0
  $a[-1..-3]                # slice with Length 3, value 90,80,70
  $a = New-Object 'int[,]' 3,2
  $a[0,0] = 10; $a[0,1] = 20; $a[1,0] = 30
  $a[1,1] = 40; $a[2,0] = 50; $a[2,1] = 60
  $a[(0,1),(1,0)]           # slice with Length 2, value 20,30, parens needed
  $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123 }
  $h1['FirstName']          # the value associated with key FirstName
  $h1['BirthDate']          # no such key, returns $null
  $h1['FirstName','IDNum'] # returns [Object[]], Length 2 (James/123)
  $h1['FirstName','xxx']    # returns [Object[]], Length 2 (James/$null)
  $h1[$null,'IDNum']        # returns [Object[]], Length 2 ($null/123)

Windows PowerShell: When expression is a collection of two or more key names, if
$null is used as any key name that key is ignored and has no corresponding element in

the resulting array.

7.1.5 Postfix increment and decrement operators
Syntax:

  Syntax

  post-increment-expression:
      primary-expression ++

<!-- p.1265 -->

  post-decrement-expression:
      primary-expression dashdash

Description:

The primary-expression must designate a writable location having a value of numeric
type (§4) or the value $null . If the value designated by the operand is $null , that value
is converted to type int and value zero before the operator is evaluated. The type of the
value designated by primary-expression may change when the result is stored. See §7.11
for a discussion of type change via assignment.

The result produced by the postfix ++ operator is the value designated by the operand.
After that result is obtained, the value designated by the operand is incremented by 1 of
the appropriate type. The type of the result of expression E++ is the same as for the
result of the expression E + 1 (§7.7).

The result produced by the postfix -- operator is the value designated by the operand.
After that result is obtained, the value designated by the operand is decremented by 1
of the appropriate type. The type of the result of expression E-- is the same as for the
result of the expression E - 1 (§7.7).

These operators are left associative.

Examples:

  PowerShell

  $i = 0                   # $i = 0
  $i++                     # $i is incremented by 1
  $j = $i--                # $j takes on the value of $i before the decrement

  $a = 1,2,3
  $b = 9,8,7
  $i = 0
  $j = 1
  $b[$j--] = $a[$i++]      # $b[1] takes on the value of $a[0], then $j is
                           # decremented, $i incremented

  $i = 2147483647          # $i holds a value of type int
  $i++                     # $i now holds a value of type double because
                           # 2147483648 is too big to fit in type int

  [int]$k = 0              # $k is constrained to int
  $k = [int]::MaxValue     # $k is set to 2147483647
  $k++                     # 2147483648 is too big to fit, imp-def behavior

<!-- p.1266 -->

  $x = $null                # target is unconstrained, $null goes to [int]0
  $x++                      # value treated as int, 0->1

7.1.6 $(...) operator
Syntax:

  Syntax

  sub-expression:
      $( new-lines~opt~ statement-list~opt~ new-lines~opt~ )

Description:

If statement-list is omitted, the result is $null . Otherwise, statement-list is evaluated.
Any objects written to the pipeline as part of the evaluation are collected in an
unconstrained 1-dimensional array, in order. If the array of collected objects is empty,
the result is $null . If the array of collected objects contains a single element, the result
is that element; otherwise, the result is the unconstrained 1-dimensional array of
collected results.

Examples:

  PowerShell

  $j = 20
  $($i = 10) # pipeline gets nothing
  $(($i = 10)) # pipeline gets int 10
  $($i = 10; $j) # pipeline gets int 20
  $(($i = 10); $j) # pipeline gets [Object[]](10,20)
  $(($i = 10); ++$j) # pipeline gets int 10
  $(($i = 10); (++$j)) # pipeline gets [Object[]](10,22)
  $($i = 10; ++$j) # pipeline gets nothing
  $(2,4,6) # pipeline gets [Object[]](2,4,6)

7.1.7 @(...) operator
Syntax:

  Syntax

  array-expression:
      @( new-lines~opt~ statement-list~opt~ new-lines~opt~ )

<!-- p.1267 -->

Description:

If statement-list is omitted, the result is an unconstrained 1-dimensional array of length
zero. Otherwise, statement-list is evaluated, and any objects written to the pipeline as
part of the evaluation are collected in an unconstrained 1-dimensional array, in order.
The result is the (possibly empty) unconstrained 1-dimensional array.

Examples:

  PowerShell

  $j = 20
  @($i = 10)                # 10 not written to pipeline, result is array of 0
  @(($i = 10))              # pipeline gets 10, result is array of 1
  @($i = 10; $j)            # 10 not written to pipeline, result is array of 1
  @(($i = 10); $j)          # pipeline gets 10, result is array of 2
  @(($i = 10); ++$j)        # pipeline gets 10, result is array of 1
  @(($i = 10); (++$j))      # pipeline gets both values, result is array of 2
  @($i = 10; ++$j)          # pipeline gets nothing, result is array of 0

  $a = @(2,4,6)             # result is array of 3
  @($a)                     # result is the same array of 3
  @(@($a))                  # result is the same array of 3

7.1.8 Script block expression
Syntax:

  Syntax

  script-block-expression:
      { new-lines~opt~ script-block new-lines~opt~ }

  script-block:
      param-block~opt~ statement-terminators~opt~ script-block-body~opt~

  script-block-body:
      named-block-list
      statement-list

Description:

param-block is described in §8.10.9. named-block-list is described in §8.10.7.

A script block is an unnamed block of statements that can be used as a single unit.
Script blocks can be used to invoke a block of code as if it was a single command, or
they can be assigned to variables that can be executed.

<!-- p.1268 -->

The named-block-list or statement-list is executed and the type and value(s) of the result
are the type and value(s) of the results of those statement sets.

A script-block-expression has type scriptblock (§4.3.7).

If param-block is omitted, any arguments passed to the script block are available via
$args (§8.10.1).

During parameter binding, a script block can be passed either as a script block object or
as the result after the script block has been evaluated. See §6.17 for further information.

7.1.9 Hash literal expression
Syntax:

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

  statement-terminators:
      statement-terminator
      statement-terminators statement-terminator

  statement-terminator:
      ;
      new-line-character

Description:

A hash-literal-expression is used to create a Hashtable (§10) of zero or more elements
each of which is a key/value pair.

The key may have any type except the null type. The associated values may have any
type, including the null type, and each of those values may be any expression that
designates the desired value, including $null .

<!-- p.1269 -->

The ordering of the key/value pairs is not significant.

Examples:

  PowerShell

  $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123 }
  $last = "Anderson"; $IDNum = 120
  $h2 = @{ FirstName = "James"; LastName = $last; IDNum = $IDNum + 3 }
  $h3 = @{ }
  $h4 = @{ 10 = "James"; 20.5 = "Anderson"; $true = 123 }

which creates two Hashtables, $h1 and $h2 , each containing three key/value pairs, and
a third, $h3 , that is empty. Hashtable $h4 has keys of various types.

7.1.10 Type literal expression
Syntax:

  Syntax

  type-literal:
      [ type-spec ]

  type-spec:
      array-type-name new-lines~opt~ dimension~opt~ ]
      generic-type-name new-lines~opt~ generic-type-arguments ]
      type-name

  dimension:
      ,
      dimension ,

  generic-type-arguments:
      type-spec new-lines~opt~
      generic-type-arguments , new-lines~opt~ type-spec

  array-type-name:
      type-name [

  generic-type-name:
      type-name [

Description:

A type-literal is represented in an implementation by some unspecified underlying type.
As a result, a type name is a synonym for its underlying type.

<!-- p.1270 -->

Type literals are used in a number of contexts:

     Specifying an explicit conversion (§6, §7.2.9)
     Creating a type-constrained array (§9.4)
     Accessing the static members of an object (§7.1.2)
     Specifying a type constraint on a variable (§5.3) or a function parameter (§8.10.2)

Examples:

  PowerShell

  [int].IsPrimitive        # $true
  [Object[]].FullName      # "System.Object[]"
  [int[,,]].GetArrayRank() # 3

A generic stack type (§4.4) that is specialized to hold strings might be written as
[Stack[string]] , and a generic dictionary type that is specialized to hold int keys with

associated string values might be written as [Dictionary[int,string]] .

The type of a type-literal is System.Type . The complete name for the type Stack[string]
suggested above is System.Collections.Generic.Stack[int] . The complete name for the
type Dictionary[int,string] suggested above is
System.Collections.Generic.Dictionary[int,string] .

7.2 Unary operators
Syntax:

  Syntax

  unary-expression:
      primary-expression
      expression-with-unary-operator

  expression-with-unary-operator:
      , new-lines~opt~ unary-expression
      -not new-lines~opt~ unary-expression
      ! new-lines~opt~ unary-expression
      -bnot new-lines~opt~ unary-expression
      + new-lines~opt~ unary-expression
      dash new-lines~opt~ unary-expression
      pre-increment-expression
      pre-decrement-expression
      cast-expression
      -split new-lines~opt~ unary-expression
      -join new-lines~opt~ unary-expression

<!-- p.1271 -->

  pre-increment-expression:
      ++ new-lines~opt~ unary-expression

  pre-decrement-expression:
      dashdash new-lines~opt~ unary-expression

  dash: one of
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

  cast-expression:
      type-literal unary-expression

  dashdash:
      dash dash

7.2.1 Unary comma operator
Description:

The comma operator ( , ) creates an unconstrained 1-dimensional array having one
element, whose type and value are that of unary-expression.

This operator is right associative.

Examples:

  PowerShell

  $a = ,10            # create an unconstrained array of 1 element, $a[0],
                      # which has type int

  $a = ,(10,"red") # create an unconstrained array of 1 element,
  $a[0],
                   # which is an unconstrained array of 2 elements,
                   # $a[0][0] an int, and $a[0][1] a string

  $a = ,,10           # create an unconstrained array of 1 element, which is
                      # an unconstrained array of 1 element, which is an int
                      # $a[0][0] is the int. Contrast this with @(@(10))

7.2.2 Logical NOT
Syntax:

  Syntax

<!-- p.1272 -->

  logical-not-operator:
      dash not

  dash: one of
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The operator -not converts the value designated by unary-expression to type bool
(§6.2), if necessary, and produces a result of that type. If unary-expression's value is True,
the result is False, and vice versa. The operator ! is an alternate spelling for -not .

This operator is right associative.

Examples:

  PowerShell

  -not $true            # False
  -not -not $false      # False
  -not 0                # True
  -not 1.23             # False
  !"xyz"                # False

7.2.3 Bitwise NOT
Syntax:

  Syntax

  bitwise-not-operator:
      dash bnot

  dash: one of
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The operator -bnot converts the value designated by unary-expression to an integer
type (§6.4), if necessary. If the converted value can be represented in type int then that is

<!-- p.1273 -->

the result type. Else, if the converted value can be represented in type long then that is
the result type. Otherwise, the expression is ill-formed. The resulting value is the ones-
complement of the converted value.

This operator is right associative.

Examples:

  PowerShell

  -bnot $true             # int with value 0xFFFFFFFE
  -bnot 10                # int with value 0xFFFFFFF5
  -bnot 2147483648.1      # long with value 0xFFFFFFFF7FFFFFFF
  -bnot $null             # int with value 0xFFFFFFFF
  -bnot "0xabc"           # int with value 0xFFFFF543

7.2.4 Unary plus
Description:

An expression of the form + unary-expression is treated as if it were written as 0 +
unary-expression (§7.7). The integer literal 0 has type int .

This operator is right associative.

Examples:

  PowerShell

  +123L            # type long, value 123
  +0.12340D        # type decimal, value 0.12340
  +"0xabc"         # type int, value 2748

7.2.5 Unary minus
Description:

An expression of the form - unary-expression is treated as if it were written as 0 -
unary-expression (§7.7). The integer literal 0 has type int . The minus operator can be

any one of the dash characters listed in §7.2.

This operator is right associative.

Examples:

<!-- p.1274 -->

  PowerShell

  -$true       # type int, value -1
  -123L        # type long, value -123
  -0.12340D    # type decimal, value -0.12340

7.2.6 Prefix increment and decrement operators
Description:

The unary-expression must designate a writable location having a value of numeric type
(§4) or the value $null . If the value designated by its unary-expression is $null , unary-
expression's value is converted to type int and value zero before the operator is
evaluated.

  ７ Note

  The type of the value designated by unary-expression may change when the result
  is stored. See §7.11 for a discussion of type change via assignment.

For the prefix increment operator ++ , the value of unary-expression is incremented by
1 of the appropriate type. The result is the new value after incrementing has taken

place. The expression ++E is equivalent to E += 1 (§7.11.2).

For the prefix decrement operator -- , the value of unary-expression is decremented by
1 of the appropriate type. The result is the new value after decrementing has taken

place. The expression --E is equivalent to E -= 1 (§7.11.2). The prefix decrement
operator can be any of the patterns matching the dashdash pattern in §7.2.

These operators are right associative.

Examples:

  PowerShell

  $i = 0                   # $i = 0
  ++$i                     # $i is incremented by 1
  $j = --$i                # $i is decremented then $j takes on the value of $i

  $a = 1,2,3
  $b = 9,8,7
  $i = 0;
  $j = 1
  $b[--$j] = $a[++$i]      # $j is # decremented, $i incremented, then $b[0]
                           # takes on the value of $a[1]

<!-- p.1275 -->

  $i = 2147483647           # $i holds a value of type int
  ++$i                      # $i now holds a value of type double because
                            # 2147483648 is too big to fit in type int

  [int]$k = 0               # $k is constrained to int
  $k = [int]::MinValue      # $k is set to -2147483648
  --$k                      # -2147483649 is too small to fit, imp-def behavior

  $x = $null                # target is unconstrained, $null goes to [int]0
  --$x                      # value treated as int, 0 becomes -1

7.2.7 The unary -join operator
Syntax:

  Syntax

  join-operator:
      dash join

  dash: one of
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The unary -join operator produces a string that is the concatenation of the value of
one or more objects designated by unary-expression. (A separator can be inserted by
using the binary version of this operator (§7.8.4.4).)

unary-expression can be a scalar value or a collection.

Examples:

  PowerShell

  -join (10, 20, 30)                  # result is "102030"
  -join (123, $false, 19.34e17)       # result is "123False1.934E+18"
  -join 12345                         # result is "12345"
  -join $null                         # result is ""

7.2.8 The unary -split operator
Syntax:

<!-- p.1276 -->

  Syntax

  split-operator:
      dash split

  dash: one of
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The unary -split operator splits one or more strings designated by unary-expression,
returning their subparts in a constrained 1-dimensional array of string. It treats any
contiguous group of whitespace characters as the delimiter between successive
subparts. An explicit delimiter string can be specified by using the binary version of this
operator (§7.8.4.5) or its two variants (§7.8).

The delimiter text is not included in the resulting strings. Leading and trailing
whitespace in the input string is ignored. An input string that is empty or contains
whitespace only results in an array of one string, which is empty.

unary-expression can designate a scalar value or an array of strings.

Examples:

  PowerShell

  -split " red`tblue`ngreen " # 3 strings: "red", "blue", "green"
  -split ("yes no", "up down") # 4 strings: "yes", "no", "up", "down"
  -split " " # 1 (empty) string

7.2.9 Cast operator
Description:

This operator converts explicitly (§6) the value designated by unary-expression to the
type designated by type-literal (§7.1.10). If type-literal is other than void, the type of the
result is the named type, and the value is the value after conversion. If type-literal is
void, no object is written to the pipeline and there is no result.

When an expression of any type is cast to that same type, the resulting type and value is
the unary-expression's type and value.

<!-- p.1277 -->

This operator is right associative.

Examples:

  PowerShell

  [bool]-10           # a bool with value True
  [int]-10.70D        # a decimal with value -10
  [int]10.7           # an int with value 11
  [long]"+2.3e+3"     # a long with value 2300
  [char[]]"Hello"     # an array of 5 char with values H, e, l, l, and o.

7.3 Binary comma operator
Syntax:

  Syntax

  array-literal-expression:
      unary-expression , new-lines~opt~ array-literal-expression

Description:

The binary comma operator creates a 1-dimensional array whose elements are the
values designated by its operands, in lexical order. The array has unconstrained type.

Examples:

  PowerShell

  2,4,6                         # Length 3; values 2,4,6
  (2,4),6                       # Length 2; values [Object[]],int
  (2,4,6),12,(2..4)             # Length 3; [Object[]],int,[Object[]]
  2,4,6,"red",$null,$true       # Length 6

The addition of grouping parentheses to certain binary comma expressions does not
document the default precedence; instead, it changes the result.

7.4 Range operator
Syntax:

  Syntax

<!-- p.1278 -->

  range-expression:
      unary-expression .. new-lines~opt~ unary-expression

Description:

A range-expression creates an unconstrained 1-dimensional array whose elements are
the values of the int sequence specified by the range bounds. The values designated by
the operands are converted to int, if necessary (§6.4). The operand designating the lower
value after conversion is the lower bound, while the operand designating the higher
value after conversion is the upper bound. Both bounds may be the same, in which case,
the resulting array has length 1 . If the left operand designates the lower bound, the
sequence is in ascending order. If the left operand designates the upper bound, the
sequence is in descending order.

Conceptually, this operator is a shortcut for the corresponding binary comma operator
sequence. For example, the range 5..8 can also be generated using 5,6,7,8 . However,
if an ascending or descending sequence is needed without having an array, an
implementation may avoid generating an actual array. For example, in foreach ($i in
1..5) { ... } , no array need be created.

A range-expression can be used to specify an array slice (§9.9).

Examples:

  PowerShell

  1..10          # ascending range 1..10
  -495..-500     # descending range -495..-500
  16..16         # sequence of 1

  $x = 1.5
  $x..5.40D      # ascending range 2..5

  $true..3       # ascending range 1..3
  -2..$null      # ascending range -2..0
  0xf..0xa       # descending range 15..10

7.5 Format operator
Syntax:

  Syntax

<!-- p.1279 -->

  format-expression:
      format-specification-string format-operator new-lines~opt~ range-
  expression

  format-operator:
      dash f

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

A format-expression formats one or more values designated by range-expression
according to a format-specification-string designated by format-expression. The
positions of the values designated by range-expression are numbered starting at zero
and increasing in lexical order. The result has type string .

A format specification string may contain zero or more format specifications each
having the following form:

{N [ ,M ][ : FormatString ]}

N represents a (required) range-expression value position, M represents the (optional)
minimum display width, and FormatString indicates the (optional) format. If the width of
a formatted value exceeds the specified width, the width is increased accordingly. Values
whose positions are not referenced in FormatString are ignored after being evaluated
for any side effects. If N refers to a non-existent position, the behavior is
implementation defined. Value of type $null and void are formatted as empty strings.
Arrays are formatted as for sub-expression (§7.1.6). To include the characters { and } in
a format specification without their being interpreted as format delimiters, write them as
{{ and }} , respectively.

For a complete definition of format specifications, see the type System.IFormattable in
Ecma Technical Report TR/84      .

Examples:

  PowerShell

  "__{0,3}__" -f 5                                # __ 5__
  "__{0,-3}__" -f 5                               # __5 __
  "__{0,3:000}__" -f 5                            # __005__
  "__{0,5:0.00}__" -f 5.0                         # __ 5.00__

<!-- p.1280 -->

  "__{0:C}__" -f 1234567.888                      # __$1,234,567.89__
  "__{0:C}__" -f -1234.56                         # __($1,234.56)__
  "__{0,12:e2}__" -f 123.456e2                    # __ 1.23e+004__
  "__{0,-12:p}__" -f -0.252                       # __-25.20 % __

  $i = 5; $j = 3
  "__{0} + {1} <= {2}__" -f $i,$j,($i+$j)         # __5 + 3 <= 8__

  $format = "__0x{0:X8}__"
  $format -f 65535                                # __0x0000FFFF__

In a format specification, if N refers to a non-existent position, a FormatError is raised.

7.6 Multiplicative operators
Syntax:

  Syntax

  multiplicative-expression:
      multiplicative-expression * new-lines~opt~ format-expression
      multiplicative-expression / new-lines~opt~ format-expression
      multiplicative-expression % new-lines~opt~ format-expression

7.6.1 Multiplication
Description:

The result of the multiplication operator * is the product of the values designated by
the two operands after the usual arithmetic conversions (§6.15) have been applied.

This operator is left associative.

Examples:

  PowerShell

  12 * -10L         # long result -120
  -10.300D * 12     # decimal result -123.600
  10.6 * 12         # double result 127.2
  12 * "0xabc"      # int result 32976

7.6.2 String replication
Description:
