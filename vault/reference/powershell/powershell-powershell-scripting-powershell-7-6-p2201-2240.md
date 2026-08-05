---
title: "How to use this documentation — pages 2201-2240"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2201-2240
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2201-2240
family: powershell
documentKind: "doc"
abstract: "/// NotImplementException exception. /// </summary> /// <returns>Throws a NotImplemented exception.</returns> public override System.Security.SecureString ReadLineAsSecureString() { throw new NotImplementedException(\"The method or operation is not implemented.\"); } /// <summary>"
---

# How to use this documentation — pages 2201-2240

<!-- p.2201 -->

    /// NotImplementException exception.
    /// </summary>
    /// <returns>Throws a NotImplemented exception.</returns>
    public override System.Security.SecureString ReadLineAsSecureString()
    {
      throw new NotImplementedException("The method or operation is not
implemented.");
    }

    /// <summary>
    /// Writes characters to the output display of the host.
    /// </summary>
    /// <param name="value">The characters to be written.</param>
    public override void Write(string value)
    {
      Console.Write(value);
    }

    /// <summary>
    /// Writes characters to the output display of the host with possible
    /// foreground and background colors.
    /// </summary>
    /// <param name="foregroundColor">The color of the characters.</param>
    /// <param name="backgroundColor">The background color to use.</param>
    /// <param name="value">The characters to be written.</param>
    public override void Write(
                               ConsoleColor foregroundColor,
                               ConsoleColor backgroundColor,
                               string value)
    {
      ConsoleColor oldFg = Console.ForegroundColor;
      ConsoleColor oldBg = Console.BackgroundColor;
      Console.ForegroundColor = foregroundColor;
      Console.BackgroundColor = backgroundColor;
      Console.Write(value);
      Console.ForegroundColor = oldFg;
      Console.BackgroundColor = oldBg;
    }

    /// <summary>
    /// Writes a line of characters to the output display of the host
    /// with foreground and background colors and appends a newline (carriage
return).
    /// </summary>
    /// <param name="foregroundColor">The foreground color of the display. </param>
    /// <param name="backgroundColor">The background color of the display. </param>
    /// <param name="value">The line to be written.</param>
    public override void WriteLine(
                                   ConsoleColor foregroundColor,
                                   ConsoleColor backgroundColor,
                                   string value)
    {
      ConsoleColor oldFg = Console.ForegroundColor;
      ConsoleColor oldBg = Console.BackgroundColor;
      Console.ForegroundColor = foregroundColor;

<!-- p.2202 -->

        Console.BackgroundColor = backgroundColor;
        Console.WriteLine(value);
        Console.ForegroundColor = oldFg;
        Console.BackgroundColor = oldBg;
    }

    /// <summary>
    /// Writes a debug message to the output display of the host.
    /// </summary>
    /// <param name="message">The debug message that is displayed.</param>
    public override void WriteDebugLine(string message)
    {
      this.WriteLine(
                      ConsoleColor.DarkYellow,
                      ConsoleColor.Black,
                      String.Format(CultureInfo.CurrentCulture, "DEBUG: {0}",
message));
    }

    /// <summary>
    /// Writes an error message to the output display of the host.
    /// </summary>
    /// <param name="value">The error message that is displayed.</param>
    public override void WriteErrorLine(string value)
    {
      this.WriteLine(
                      ConsoleColor.Red,
                      ConsoleColor.Black,
                      value);
    }

    /// <summary>
    /// Writes a newline character (carriage return)
    /// to the output display of the host.
    /// </summary>
    public override void WriteLine()
    {
      Console.WriteLine();
    }

       /// <summary>
    /// Writes a line of characters to the output display of the host
    /// and appends a newline character(carriage return).
    /// </summary>
    /// <param name="value">The line to be written.</param>
    public override void WriteLine(string value)
    {
      Console.WriteLine(value);
    }

    /// <summary>
    /// Writes a progress report to the output display of the host.
    /// </summary>
    /// <param name="sourceId">Unique identifier of the source of the record.
</param>

<!-- p.2203 -->

    /// <param name="record">A ProgressReport object.</param>
    public override void WriteProgress(long sourceId, ProgressRecord record)
    {

    }

    /// <summary>
    /// Writes a verbose message to the output display of the host.
    /// </summary>
    /// <param name="message">The verbose message that is displayed.</param>
    public override void WriteVerboseLine(string message)
    {
      this.WriteLine(
                      ConsoleColor.Green,
                      ConsoleColor.Black,
                      String.Format(CultureInfo.CurrentCulture, "VERBOSE: {0}",
message));
    }

    /// <summary>
    /// Writes a warning message to the output display of the host.
    /// </summary>
    /// <param name="message">The warning message that is displayed.</param>
    public override void WriteWarningLine(string message)
    {
      this.WriteLine(
                      ConsoleColor.Yellow,
                      ConsoleColor.Black,
                      String.Format(CultureInfo.CurrentCulture, "WARNING: {0}",
message));
    }

    /// <summary>
    /// Parse a string containing a hotkey character.
    /// Take a string of the form
    ///    Yes to &all
    /// and returns a two-dimensional array split out as
    ///    "A", "Yes to all".
    /// </summary>
    /// <param name="input">The string to process</param>
    /// <returns>
    /// A two dimensional array containing the parsed components.
    /// </returns>
    private static string[] GetHotkeyAndLabel(string input)
    {
      string[] result = new string[] { String.Empty, String.Empty };
      string[] fragments = input.Split('&');
      if (fragments.Length == 2)
      {
        if (fragments[1].Length > 0)
        {
          result[0] = fragments[1][0].ToString().
          ToUpper(CultureInfo.CurrentCulture);
        }

<!-- p.2204 -->

               result[1] = (fragments[0] + fragments[1]).Trim();
             }
             else
             {
               result[1] = input;
             }

             return result;
         }

         /// <summary>
         /// This is a private worker function splits out the
         /// accelerator keys from the menu and builds a two
         /// dimensional array with the first access containing the
         /// accelerator and the second containing the label string
         /// with the & removed.
         /// </summary>
         /// <param name="choices">The choice collection to process</param>
         /// <returns>
         /// A two dimensional array containing the accelerator characters
         /// and the cleaned-up labels</returns>
         private static string[,] BuildHotkeysAndPlainLabels(
              Collection<ChoiceDescription> choices)
         {
           // Allocate the result array
           string[,] hotkeysAndPlainLabels = new string[2, choices.Count];

             for (int i = 0; i < choices.Count; ++i)
             {
               string[] hotkeyAndLabel = GetHotkeyAndLabel(choices[i].Label);
               hotkeysAndPlainLabels[0, i] = hotkeyAndLabel[0];
               hotkeysAndPlainLabels[1, i] = hotkeyAndLabel[1];
             }

             return hotkeysAndPlainLabels;
         }
     }
 }

Example 4
The following code is the implementation of the
System.Management.Automation.Host.PSHostRawUserInterface class that is used by this host
application. Those elements that are not implemented throw an exception or return nothing.

 C#

 namespace Microsoft.Samples.PowerShell.Host
 {
   using System;
   using System.Management.Automation.Host;

<!-- p.2205 -->

/// <summary>
/// A sample implementation of the PSHostRawUserInterface for console
/// applications. Members of this class that easily map to the .NET
/// console class are implemented. More complex methods are not
/// implemented and throw a NotImplementedException exception.
/// </summary>
internal class MyRawUserInterface : PSHostRawUserInterface
{
  /// <summary>
  /// Gets or sets the background color of text to be written.
  /// This maps to the corresponding Console.Background property.
  /// </summary>
  public override ConsoleColor BackgroundColor
  {
    get { return Console.BackgroundColor; }
    set { Console.BackgroundColor = value; }
  }

 /// <summary>
 /// Gets or sets the host buffer size adapted from the Console buffer
 /// size members.
 /// </summary>
 public override Size BufferSize
 {
   get { return new Size(Console.BufferWidth, Console.BufferHeight); }
   set { Console.SetBufferSize(value.Width, value.Height); }
 }

 /// <summary>
 /// Gets or sets the cursor position. In this example this
 /// functionality is not needed so the property throws a
 /// NotImplementException exception.
 /// </summary>
 public override Coordinates CursorPosition
 {
   get { throw new NotImplementedException(
              "The method or operation is not implemented."); }
   set { throw new NotImplementedException(
              "The method or operation is not implemented."); }
 }

 /// <summary>
 /// Gets or sets the cursor size taken directly from the
 /// Console.CursorSize property.
 /// </summary>
 public override int CursorSize
 {
   get { return Console.CursorSize; }
   set { Console.CursorSize = value; }
 }

 /// <summary>
 /// Gets or sets the foreground color of the text to be written.
 /// This maps to the corresponding Console.ForegroundColor property.

<!-- p.2206 -->

    /// </summary>
    public override ConsoleColor ForegroundColor
    {
      get { return Console.ForegroundColor; }
      set { Console.ForegroundColor = value; }
    }

    /// <summary>
    /// Gets a value indicating whether a key is available. This maps to
    /// the corresponding Console.KeyAvailable property.
    /// </summary>
    public override bool KeyAvailable
    {
      get { return Console.KeyAvailable; }
    }

    /// <summary>
    /// Gets the maximum physical size of the window adapted from the
    /// Console.LargestWindowWidth and Console.LargestWindowHeight
    /// properties.
    /// </summary>
    public override Size MaxPhysicalWindowSize
    {
      get { return new Size(Console.LargestWindowWidth,
Console.LargestWindowHeight); }
    }

    /// <summary>
    /// Gets the maximum window size adapted from the
    /// Console.LargestWindowWidth and console.LargestWindowHeight
    /// properties.
    /// </summary>
    public override Size MaxWindowSize
    {
      get { return new Size(Console.LargestWindowWidth,
Console.LargestWindowHeight); }
    }

    /// <summary>
    /// Gets or sets the window position adapted from the Console window position
    /// members.
    /// </summary>
    public override Coordinates WindowPosition
    {
      get { return new Coordinates(Console.WindowLeft, Console.WindowTop); }
      set { Console.SetWindowPosition(value.X, value.Y); }
    }

    /// <summary>
    /// Gets or sets the window size adapted from the corresponding Console
    /// calls.
    /// </summary>
    public override Size WindowSize
    {
      get { return new Size(Console.WindowWidth, Console.WindowHeight); }

<!-- p.2207 -->

    set { Console.SetWindowSize(value.Width, value.Height); }
}

/// <summary>
/// Gets or sets the title of the window mapped to the Console.Title
/// property.
/// </summary>
public override string WindowTitle
{
  get { return Console.Title; }
  set { Console.Title = value; }
}

/// <summary>
/// This API resets the input buffer. In this example this
/// functionality is not needed so the method returns nothing.
/// </summary>
public override void FlushInputBuffer()
{
}

/// <summary>
/// This API returns a rectangular region of the screen buffer. In
/// this example this functionality is not needed so the method throws
/// a NotImplementException exception.
/// </summary>
/// <param name="rectangle">Defines the size of the rectangle.</param>
/// <returns>Throws a NotImplementedException exception.</returns>
public override BufferCell[,] GetBufferContents(Rectangle rectangle)
{
  throw new NotImplementedException(
           "The method or operation is not implemented.");
}

/// <summary>
/// This API Reads a pressed, released, or pressed and released keystroke
/// from the keyboard device, blocking processing until a keystroke is
/// typed that matches the specified keystroke options. In this example
/// this functionality is not needed so the method throws a
/// NotImplementException exception.
/// </summary>
/// <param name="options">Options, such as IncludeKeyDown, used when
/// reading the keyboard.</param>
/// <returns>Throws a NotImplementedException exception.</returns>
public override KeyInfo ReadKey(ReadKeyOptions options)
{
  throw new NotImplementedException(
            "The method or operation is not implemented.");
}

/// <summary>
/// This API crops a region of the screen buffer. In this example
/// this functionality is not needed so the method throws a
/// NotImplementException exception.
/// </summary>

<!-- p.2208 -->

     /// <param name="source">The region of the screen to be scrolled.</param>
     /// <param name="destination">The region of the screen to receive the
     /// source region contents.</param>
     /// <param name="clip">The region of the screen to include in the operation.
 </param>
     /// <param name="fill">The character and attributes to be used to fill all
 cell.</param>
     public override void ScrollBufferContents(Rectangle source, Coordinates
 destination, Rectangle clip, BufferCell fill)
     {
       throw new NotImplementedException(
                 "The method or operation is not implemented.");
     }

     /// <summary>
     /// This API copies an array of buffer cells into the screen buffer
     /// at a specified location. In this example this functionality is
     /// not needed si the method throws a NotImplementedException exception.
     /// </summary>
     /// <param name="origin">The parameter is not used.</param>
     /// <param name="contents">The parameter is not used.</param>
     public override void SetBufferContents(Coordinates origin, BufferCell[,]
 contents)
     {
       throw new NotImplementedException(
                 "The method or operation is not implemented.");
     }

         /// <summary>
         /// This API Copies a given character, foreground color, and background
         /// color to a region of the screen buffer. In this example this
         /// functionality is not needed so the method throws a
         /// NotImplementException exception./// </summary>
         /// <param name="rectangle">Defines the area to be filled. </param>
         /// <param name="fill">Defines the fill character.</param>
         public override void SetBufferContents(Rectangle rectangle, BufferCell fill)
         {
           throw new NotImplementedException(
                     "The method or operation is not implemented.");
         }
     }
 }

Example 5
The following code reads the command line and colors the text as it is entered. Tokens are
determined by using the System.Management.Automation.PSParser.Tokenize* method.

 C#

 namespace Microsoft.Samples.PowerShell.Host
 {

<!-- p.2209 -->

using System;
using System.Collections.ObjectModel;
using System.Management.Automation;
using System.Text;

/// <summary>
/// This class is used to read the command line and color the text as
/// it is entered. Tokens are determined using the PSParser.Tokenize
/// method.
/// </summary>
internal class ConsoleReadLine
{
  /// <summary>
  /// The buffer used to edit.
  /// </summary>
  private StringBuilder buffer = new StringBuilder();

 /// <summary>
 /// The position of the cursor within the buffer.
 /// </summary>
 private int current;

 /// <summary>
 /// The count of characters in buffer rendered.
 /// </summary>
 private int rendered;

 /// <summary>
 /// Store the anchor and handle cursor movement
 /// </summary>
 private Cursor cursor;

 /// <summary>
 /// The array of colors for tokens, indexed by PSTokenType
 /// </summary>
 private ConsoleColor[] tokenColors;

 /// <summary>
 /// We do not pick different colors for every token, those tokens
 /// use this default.
 /// </summary>
 private ConsoleColor defaultColor = Console.ForegroundColor;

 /// <summary>
 /// Initializes a new instance of the ConsoleReadLine class.
 /// </summary>
 public ConsoleReadLine()
 {
   this.tokenColors = new ConsoleColor[]
   {
     this.defaultColor,       // Unknown
     ConsoleColor.Yellow,     // Command
     ConsoleColor.Green,      // CommandParameter
     ConsoleColor.Cyan,       // CommandArgument
     ConsoleColor.Cyan,       // Number

<!-- p.2210 -->

      ConsoleColor.Cyan,       // String
      ConsoleColor.Green,      // Variable
      this.defaultColor,            // Member
      this.defaultColor,            // LoopLabel
      ConsoleColor.DarkYellow, // Attribute
      ConsoleColor.DarkYellow, // Type
      ConsoleColor.DarkCyan,   // Operator
      this.defaultColor,            // GroupStart
      this.defaultColor,            // GroupEnd
      ConsoleColor.Magenta,    // Keyword
      ConsoleColor.Red,        // Comment
      ConsoleColor.DarkCyan,   // StatementSeparator
              this.defaultColor,            // NewLine
              this.defaultColor,            // LineContinuation
              this.defaultColor,            // Position
    };
}

/// <summary>
/// Read a line of text, colorizing while typing.
/// </summary>
/// <returns>The command line read</returns>
public string Read()
{
  this.Initialize();

    while (true)
    {
      ConsoleKeyInfo key = Console.ReadKey(true);

     switch (key.Key)
     {
       case ConsoleKey.Backspace:
            this.OnBackspace();
            break;
       case ConsoleKey.Delete:
            this.OnDelete();
            break;
       case ConsoleKey.Enter:
            return this.OnEnter();
       case ConsoleKey.RightArrow:
            this.OnRight(key.Modifiers);
            break;
       case ConsoleKey.LeftArrow:
            this.OnLeft(key.Modifiers);
            break;
       case ConsoleKey.Escape:
            this.OnEscape();
            break;
       case ConsoleKey.Home:
            this.OnHome();
            break;
       case ConsoleKey.End:
            this.OnEnd();
            break;

<!-- p.2211 -->

            case ConsoleKey.UpArrow:
            case ConsoleKey.DownArrow:
            case ConsoleKey.LeftWindows:
            case ConsoleKey.RightWindows:
            // ignore these
            continue;

            default:
            if (key.KeyChar == '\x0D')
            {
              goto case ConsoleKey.Enter;       // Ctrl-M
            }

            if (key.KeyChar == '\x08')
            {
              goto case ConsoleKey.Backspace;   // Ctrl-H
            }

            this.Insert(key);
            break;
        }
    }
}

/// <summary>
/// Initializes the buffer.
/// </summary>
private void Initialize()
{
  this.buffer.Length = 0;
  this.current = 0;
  this.rendered = 0;
  this.cursor = new Cursor();
}

/// <summary>
/// Inserts a key.
/// </summary>
/// <param name="key">The key to insert.</param>
private void Insert(ConsoleKeyInfo key)
{
  this.buffer.Insert(this.current, key.KeyChar);
  this.current++;
  this.Render();
}

/// <summary>
/// The End key was entered..
/// </summary>
private void OnEnd()
{
  this.current = this.buffer.Length;
  this.cursor.Place(this.rendered);
}

<!-- p.2212 -->

/// <summary>
/// The Home key was entered.
/// </summary>
private void OnHome()
{
  this.current = 0;
  this.cursor.Reset();
}

/// <summary>
/// The Escape key was entered.
/// </summary>
private void OnEscape()
{
  this.buffer.Length = 0;
  this.current = 0;
  this.Render();
}

/// <summary>
/// Moves to the left of the cursor position.
/// </summary>
/// <param name="consoleModifiers">Enumeration for Alt, Control,
/// and Shift keys.</param>
private void OnLeft(ConsoleModifiers consoleModifiers)
{
  if ((consoleModifiers & ConsoleModifiers.Control) != 0)
  {
    // Move back to the start of the previous word.
    if (this.buffer.Length > 0 && this.current != 0)
    {
      bool nonLetter = IsSeparator(this.buffer[this.current - 1]);
      while (this.current > 0 && (this.current - 1 < this.buffer.Length))
      {
        this.MoveLeft();

             if (IsSeparator(this.buffer[this.current]) != nonLetter)
             {
               if (!nonLetter)
               {
                 this.MoveRight();
                 break;
               }

                 nonLetter = false;
             }
         }
     }
    }
    else
    {
      this.MoveLeft();
    }
}

<!-- p.2213 -->

/// <summary>
/// Determines if a character is a separator.
/// </summary>
/// <param name="ch">Character to investigate.</param>
/// <returns>A value that indicates whether the character
/// is a separator.</returns>
private static bool IsSeparator(char ch)
{
  return !Char.IsLetter(ch);
}

/// <summary>
/// Moves to what is to the right of the cursor position.
/// </summary>
/// <param name="consoleModifiers">Enumeration for Alt, Control,
/// and Shift keys.</param>
private void OnRight(ConsoleModifiers consoleModifiers)
{
  if ((consoleModifiers & ConsoleModifiers.Control) != 0)
  {
    // Move to the next word.
    if (this.buffer.Length != 0 && this.current < this.buffer.Length)
    {
      bool nonLetter = IsSeparator(this.buffer[this.current]);
      while (this.current < this.buffer.Length)
      {
        this.MoveRight();

            if (this.current == this.buffer.Length)
            {
              break;
            }

            if (IsSeparator(this.buffer[this.current]) != nonLetter)
            {
              if (nonLetter)
              {
                break;
              }

                nonLetter = true;
            }
        }
      }
    }
    else
    {
      this.MoveRight();
    }
}

/// <summary>
/// Moves the cursor one character to the right.
/// </summary>
private void MoveRight()

<!-- p.2214 -->

{
    if (this.current < this.buffer.Length)
    {
      char c = this.buffer[this.current];
      this.current++;
      Cursor.Move(1);
    }
}

/// <summary>
/// Moves the cursor one character to the left.
/// </summary>
private void MoveLeft()
{
  if (this.current > 0 && (this.current - 1 < this.buffer.Length))
  {
    this.current--;
    char c = this.buffer[this.current];
    Cursor.Move(-1);
  }
}

/// <summary>
/// The Enter key was entered.
/// </summary>
/// <returns>A newline character.</returns>
private string OnEnter()
{
  Console.Out.Write("\n");
  return this.buffer.ToString();
}

/// <summary>
/// The delete key was entered.
/// </summary>
private void OnDelete()
{
  if (this.buffer.Length > 0 && this.current < this.buffer.Length)
  {
    this.buffer.Remove(this.current, 1);
    this.Render();
  }
}

/// <summary>
/// The Backspace key was entered.
/// </summary>
private void OnBackspace()
{
  if (this.buffer.Length > 0 && this.current > 0)
  {
    this.buffer.Remove(this.current - 1, 1);
    this.current--;
    this.Render();
  }

<!-- p.2215 -->

   }

   /// <summary>
   /// Displays the line.
   /// </summary>
   private void Render()
   {
     string text = this.buffer.ToString();

       // The PowerShell tokenizer is used to decide how to colorize
       // the input. Any errors in the input are returned in 'errors',
       // but we won't be looking at those here.
       Collection<PSParseError> errors = null;
       Collection<PSToken> tokens = PSParser.Tokenize(text, out errors);

       if (tokens.Count > 0)
       {
         // We can skip rendering tokens that end before the cursor.
         int i;
         for (i = 0; i < tokens.Count; ++i)
         {
           if (this.current >= tokens[i].Start)
           {
             break;
           }
         }

        // Place the cursor at the start of the first token to render. The
        // last edit may require changes to the colorization of characters
        // preceding the cursor.
        this.cursor.Place(tokens[i].Start);

        for (; i < tokens.Count; ++i)
        {
          // Write out the token. We don't use tokens[i].Content, instead we
          // use the actual text from our input because the content sometimes
          // excludes part of the token, e.g. the quote characters of a string.
          Console.ForegroundColor = this.tokenColors[(int)tokens[i].Type];
          Console.Out.Write(text.Substring(tokens[i].Start, tokens[i].Length));

          // Whitespace doesn't show up in the array of tokens. Write it out here.
          if (i != (tokens.Count - 1))
          {
            Console.ForegroundColor = this.defaultColor;
            for (int j = (tokens[i].Start + tokens[i].Length); j < tokens[i +
1].Start; ++j)
            {
              Console.Out.Write(text[j]);
            }
          }
        }

        // It's possible there is text left over to output. This happens when
there is
        // some error during tokenization, e.g. a string literal is missing a

<!-- p.2216 -->

closing quote.
         Console.ForegroundColor = this.defaultColor;
         for (int j = tokens[i - 1].Start + tokens[i - 1].Length; j < text.Length;
++j)
         {
            Console.Out.Write(text[j]);
         }
       }
       else
       {
         // If tokenization completely failed, just redraw the whole line. This
         // happens most frequently when the first token is incomplete, like a
string
         // literal missing a closing quote.
         this.cursor.Reset();
         Console.Out.Write(text);
       }

      // If characters were deleted, we must write over previously written
characters
      if (text.Length < this.rendered)
      {
        Console.Out.Write(new string(' ', this.rendered - text.Length));
      }

        this.rendered = text.Length;
        this.cursor.Place(this.current);
    }

    /// <summary>
    /// A helper class for maintaining the cursor while editing the command line.
    /// </summary>
    internal class Cursor
    {
      /// <summary>
      /// The top anchor for reposition the cursor.
      /// </summary>
      private int anchorTop;

        /// <summary>
        /// The left anchor for repositioning the cursor.
        /// </summary>
        private int anchorLeft;

        /// <summary>
        /// Initializes a new instance of the Cursor class.
        /// </summary>
        public Cursor()
        {
          this.anchorTop = Console.CursorTop;
          this.anchorLeft = Console.CursorLeft;
        }

        /// <summary>
        /// Moves the cursor.

<!-- p.2217 -->

       /// </summary>
       /// <param name="delta">The number of characters to move.</param>
       internal static void Move(int delta)
       {
         int position = Console.CursorTop * Console.BufferWidth + Console.CursorLeft
 + delta;

              Console.CursorLeft = position % Console.BufferWidth;
              Console.CursorTop = position / Console.BufferWidth;
          }

          /// <summary>
          /// Resets the cursor position.
          /// </summary>
          internal void Reset()
          {
            Console.CursorTop = this.anchorTop;
            Console.CursorLeft = this.anchorLeft;
          }

       /// <summary>
       /// Moves the cursor to a specific position.
       /// </summary>
       /// <param name="position">The new position.</param>
       internal void Place(int position)
       {
         Console.CursorLeft = (this.anchorLeft + position) % Console.BufferWidth;
         int cursorTop = this.anchorTop + (this.anchorLeft + position) /
 Console.BufferWidth;
         if (cursorTop >= Console.BufferHeight)
         {
           this.anchorTop -= cursorTop - Console.BufferHeight + 1;
           cursorTop = Console.BufferHeight - 1;
         }

              Console.CursorTop = cursorTop;
           }
         } // End Cursor
     }
 }

See Also
System.Management.Automation.Host.PSHost

System.Management.Automation.Host.PSHostUserInterface

System.Management.Automation.Host.PSHostRawUserInterface

Last updated on 05/20/2025

<!-- p.2218 -->

Runspace Samples
This section includes sample code that shows how to use different types of runspaces to run
commands synchronously and asynchronously. You can use Microsoft Visual Studio to create a
console application and then copy the code from the topics in this section into your host
application.

In This Section

  ７ Note

  For samples of host applications that create custom host interfaces, see Custom Host
  Samples.

Runspace01 Sample This sample shows how to use the
System.Management.Automation.PowerShell class to run the Get-Process cmdlet
synchronously and display its output in a console window.

Runspace02 Sample This sample shows how to use the
System.Management.Automation.PowerShell class to run the Get-Process and Sort-Object
cmdlets synchronously. The results of these commands is displayed by using a
System.Windows.Forms.DataGridView control.

Runspace03 Sample This sample shows how to use the
System.Management.Automation.PowerShell class to run a script synchronously, and how to
handle non-terminating errors. The script receives a list of process names and then retrieves
those processes. The results of the script, including any non-terminating errors that were
generated when running the script, are displayed in a console window.

Runspace04 Sample This sample shows how to use the
System.Management.Automation.PowerShell class to run commands, and how to catch
terminating errors that are thrown when running the commands. Two commands are run, and
the last command is passed a parameter argument that is not valid. As a result no objects are
returned and a terminating error is thrown.

Runspace05 Sample This sample shows how to add a snap-in to a
System.Management.Automation.Runspaces.InitialSessionState object so that the cmdlet of the

<!-- p.2219 -->

snap-in is available when the runspace is opened. The snap-in provides a Get-Proc cmdlet
(defined by the GetProcessSample01 Sample) that is run synchronously using a
System.Management.Automation.PowerShell object.

Runspace06 Sample This sample shows how to add a module to a
System.Management.Automation.Runspaces.InitialSessionState object so that the module is
loaded when the runspace is opened. The module provides a Get-Proc cmdlet (defined by the
GetProcessSample02 Sample) that is run synchronously using a
System.Management.Automation.PowerShell object.

Runspace07 Sample This sample shows how to create a runspace, and then use that runspace
to run two cmdlets synchronously by using a System.Management.Automation.PowerShell
object.

Runspace08 Sample This sample shows how to add commands and arguments to the pipeline
of a System.Management.Automation.PowerShell object and how to run the commands
synchronously.

Runspace09 Sample This sample shows how to add a script to the pipeline of a
System.Management.Automation.PowerShell object and how to run the script asynchronously.
Events are used to handle the output of the script.

Runspace10 Sample This sample shows how to create a default initial session state, how to add
a cmdlet to the System.Management.Automation.Runspaces.InitialSessionState, how to create a
runspace that uses the initial session state, and how to run the command by using a
System.Management.Automation.PowerShell object.

Runspace11 Sample This shows how to use the
System.Management.Automation.ProxyCommand class to create a proxy command that calls
an existing cmdlet, but restricts the set of available parameters. The proxy command is then
added to an initial session state that is used to create a constrained runspace. This means that
the user can access the functionality of the cmdlet only through the proxy command.

See Also

 Last updated on 05/20/2025

<!-- p.2220 -->

Runspace01 Sample
This sample shows how to use the System.Management.Automation.PowerShell class to run the
Get-Process cmdlet synchronously. The Get-Process cmdlet returns System.Diagnostics.Process
objects for each process running on the local computer. The values of the
System.Diagnostics.Process.ProcessName* and System.Diagnostics.Process.HandleCount*
properties are then extracted from the returned objects and displayed in a console window.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
      Creating a System.Management.Automation.PowerShell object to run a command.

      Adding a command to the pipeline of the System.Management.Automation.PowerShell
      object.

      Running the command synchronously.

      Using System.Management.Automation.PSObject objects to extract properties from the
      objects returned by the command.

Example
This sample runs the Get-Process cmdlet synchronously in the default runspace provided by
Windows PowerShell.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Management.Automation;
   using PowerShell = System.Management.Automation.PowerShell;

    /// <summary>
    /// This class contains the Main entry point for this host application.
    /// </summary>
    internal class Runspace01
    {

<!-- p.2221 -->

         /// <summary>
         /// This sample uses the PowerShell class to execute
         /// the Get-Process cmdlet synchronously. The name and
         /// handlecount are then extracted from the PSObjects
         /// returned and displayed.
         /// </summary>
         /// <param name="args">Parameter not used.</param>
         /// <remarks>
         /// This sample demonstrates the following:
         /// 1. Creating a PowerShell object to run a command.
         /// 2. Adding a command to the pipeline of the PowerShell object.
         /// 3. Running the command synchronously.
         /// 4. Using PSObject objects to extract properties from the objects
         ///    returned by the command.
         /// </remarks>
         private static void Main(string[] args)
         {
           // Create a PowerShell object. Creating this object takes care of
           // building all of the other data structures needed to run the command.
           using (PowerShell powershell = PowerShell.Create().AddCommand("Get-Process"))
           {
             Console.WriteLine("Process              HandleCount");
             Console.WriteLine("--------------------------------");

                 // Invoke the command synchronously and display the
                 // ProcessName and HandleCount properties of the
                 // objects that are returned.
                 foreach (PSObject result in powershell.Invoke())
                 {
                   Console.WriteLine(
                               "{0,-20} {1}",
                               result.Members["ProcessName"].Value,
                               result.Members["HandleCount"].Value);
                 }
             }

             System.Console.WriteLine("Hit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

See Also

Last updated on 05/20/2025

<!-- p.2222 -->

Runspace02 Sample
This sample shows how to use the System.Management.Automation.PowerShell class to run the
Get-Process and Sort-Object cmdlets synchronously. The Get-Process cmdlet returns
System.Diagnostics.Process objects for each process running on the local computer, and the
Sort-Object sorts the objects based on their System.Diagnostics.Process.Id* property. The

results of these commands is displayed by using a System.Windows.Forms.DataGridView
control.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

      Creating a System.Management.Automation.PowerShell object to run commands.

      Adding commands to the pipeline of System.Management.Automation.PowerShell object.

      Running the commands synchronously.

      Using a System.Windows.Forms.DataGridView control to display the output of the
      commands in a Windows Forms application.

Example
This sample runs the Get-Process and Sort-Object cmdlets synchronously in the default
runspace provided by Windows PowerShell. The output is displayed in a form using a
System.Windows.Forms.DataGridView control.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Collections;
   using System.Collections.ObjectModel;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;

<!-- p.2223 -->

  using System.Windows.Forms;
  using PowerShell = System.Management.Automation.PowerShell;

  /// <summary>
  /// This class contains the Main entry point for this host application.
  /// </summary>
  internal class Runspace02
  {
    /// <summary>
    /// This method creates the form where the output is displayed.
    /// </summary>
    private static void CreateForm()
    {
      Form form = new Form();
      DataGridView grid = new DataGridView();
      form.Controls.Add(grid);
      grid.Dock = DockStyle.Fill;

      // Create a PowerShell object. Creating this object takes care of
      // building all of the other data structures needed to run the command.
      using (PowerShell powershell = PowerShell.Create())
      {
        powershell.AddCommand("Get-Process").AddCommand("Sort-
Object").AddArgument("ID");
        if (Runspace.DefaultRunspace == null)
        {
          Runspace.DefaultRunspace = powershell.Runspace;
        }

            Collection<PSObject> results = powershell.Invoke();

            // The generic collection needs to be re-wrapped in an ArrayList
            // for data-binding to work.
            ArrayList objects = new ArrayList();
            objects.AddRange(results);

            // The DataGridView will use the PSObjectTypeDescriptor type
            // to retrieve the properties.
            grid.DataSource = objects;
        }

        form.ShowDialog();
    }

    /// <summary>
    /// This sample uses a PowerShell object to run the Get-Process
    /// and Sort-Object cmdlets synchronously. Windows Forms and
    /// data binding are then used to display the results in a
    /// DataGridView control.
    /// </summary>
    /// <param name="args">The parameter is not used.</param>
    /// <remarks>
    /// This sample demonstrates the following:
    /// 1. Creating a PowerShell object.
    /// 2. Adding commands and arguments to the pipeline of

<!-- p.2224 -->

         ///    the PowerShell object.
         /// 3. Running the commands synchronously.
         /// 4. Using a DataGridView control to display the output
         ///    of the commands in a Windows Forms application.
         /// </remarks>
         private static void Main(string[] args)
         {
           Runspace02.CreateForm();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2225 -->

Runspace03 Sample
This sample shows how to use the System.Management.Automation.PowerShell class to run a
script synchronously, and how to handle non-terminating errors. The script receives a list of
process names and then retrieves those processes. The results of the script, including any non-
terminating errors that were generated when running the script, are displayed in a console
window.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

      Creating a System.Management.Automation.PowerShell object to run a script.

      Adding a script to the pipeline of the System.Management.Automation.PowerShell object.

      Passing input objects to the script from the calling program.

      Running the script synchronously.

      Using System.Management.Automation.PSObject objects to extract and display
      properties from the objects returned by the script.

      Retrieving and displaying error records that were generated when the script was run.

Example
This sample runs a script synchronously in the default runspace provided by Windows
PowerShell. The output of the script and any non-terminating errors that were generated are
displayed in a console window.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Collections;

<!-- p.2226 -->

using System.Management.Automation;
using System.Management.Automation.Runspaces;
using PowerShell = System.Management.Automation.PowerShell;

/// <summary>
/// This class contains the Main entry point for this host application.
/// </summary>
internal class Runspace03
{
  /// <summary>
  /// This sample shows how to use the PowerShell class to run a
  /// script that retrieves process information for the list of
  /// process names passed to the script. It shows how to pass input
  /// objects to a script and how to retrieve error objects as well
  /// as the output objects.
  /// </summary>
  /// <param name="args">Parameter not used.</param>
  /// <remarks>
  /// This sample demonstrates the following:
  /// 1. Creating a PowerShell object to run a script.
  /// 2. Adding a script to the pipeline of the PowerShell object.
  /// 3. Passing input objects to the script from the calling program.
  /// 4. Running the script synchronously.
  /// 5. Using PSObject objects to extract and display properties from
  ///    the objects returned by the script.
  /// 6. Retrieving and displaying error records that were generated
  ///    when the script was run.
  /// </remarks>
  private static void Main(string[] args)
  {
    // Define a list of processes to look for.
    string[] processNames = new string[]
    {
      "lsass", "nosuchprocess", "services", "nosuchprocess2"
    };

   // The script to run to get these processes. Input passed
   // to the script will be available in the $input variable.
   string script = "$input | Get-Process -Name {$_}";

   // Create a PowerShell object. Creating this object takes care of
   // building all of the other data structures needed to run the script.
   using (PowerShell powershell = PowerShell.Create())
   {
     powershell.AddScript(script);

     Console.WriteLine("Process              HandleCount");
     Console.WriteLine("--------------------------------");

     // Invoke the script synchronously and display the
     // ProcessName and HandleCount properties of the
     // objects that are returned.
     foreach (PSObject result in powershell.Invoke(processNames))
     {
       Console.WriteLine(

<!-- p.2227 -->

                                     "{0,-20} {1}",
                                     result.Members["ProcessName"].Value,
                                     result.Members["HandleCount"].Value);
                 }

                 // Process any error records that were generated while running
                 // the script.
                 Console.WriteLine("\nThe following non-terminating errors occurred:\n");
                 PSDataCollection<ErrorRecord> errors = powershell.Streams.Error;
                 if (errors != null && errors.Count > 0)
                 {
                   foreach (ErrorRecord err in errors)
                   {
                     System.Console.WriteLine("    error: {0}", err.ToString());
                   }
                 }
             }

             System.Console.WriteLine("\nHit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2228 -->

Runspace04 Sample
This sample shows how to use the System.Management.Automation.PowerShell class to run
commands, and how to catch terminating errors that are thrown when running the commands.
Two commands are run, and the last command is passed a parameter argument that is not
valid. As a result, no objects are returned and a terminating error is thrown.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

      Creating a System.Management.Automation.PowerShell object.

      Adding commands to the pipeline of the System.Management.Automation.PowerShell
      object.

      Adding parameter arguments to the pipeline.

      Invoking the commands synchronously.

      Using System.Management.Automation.PSObject objects to extract and display
      properties from the objects returned by the commands.

      Retrieving and displaying error records that were generated during the running of the
      commands.

      Catching and displaying terminating exceptions thrown by the commands.

Example
This sample runs commands synchronously in the default runspace provided by Windows
PowerShell. The last command throws a terminating error because a parameter argument that
is not valid is passed to the command. The terminating error is trapped and displayed.

 C#

<!-- p.2229 -->

namespace Microsoft.Samples.PowerShell.Runspaces
{
  using System;
  using System.Management.Automation;
  using System.Management.Automation.Runspaces;
  using PowerShell = System.Management.Automation.PowerShell;

  /// <summary>
  /// This class contains the Main entry point for this host application.
  /// </summary>
  internal class Runspace04
  {
    /// <summary>
    /// This sample shows how to use a PowerShell object to run commands.
    /// The commands generate a terminating exception that the caller
    /// should catch and process.
    /// </summary>
    /// <param name="args">The parameter is not used.</param>
    /// <remarks>
    /// This sample demonstrates the following:
    /// 1. Creating a PowerShell object to run commands.
    /// 2. Adding commands to the pipeline of the PowerShell object.
    /// 3. Passing input objects to the commands from the calling program.
    /// 4. Using PSObject objects to extract and display properties from the
    ///    objects returned by the commands.
    /// 5. Retrieving and displaying error records that were generated
    ///    while running the commands.
    /// 6. Catching and displaying terminating exceptions generated
    ///    while running the commands.
    /// </remarks>
    private static void Main(string[] args)
    {
      // Create a PowerShell object.
      using (PowerShell powershell = PowerShell.Create())
      {
        // Add the commands to the PowerShell object.
        powershell.AddCommand("Get-ChildItem").AddCommand("Select-
String").AddArgument("*");

       // Run the commands synchronously. Because of the bad regular expression,
       // no objects will be returned. Instead, an exception will be thrown.
       try
       {
         foreach (PSObject result in powershell.Invoke())
         {
           Console.WriteLine("'{0}'", result.ToString());
         }

            // Process any error records that were generated while running the
commands.
            Console.WriteLine("\nThe following non-terminating errors occurred:\n");
            PSDataCollection<ErrorRecord> errors = powershell.Streams.Error;
            if (errors != null && errors.Count > 0)
            {

<!-- p.2230 -->

                     foreach (ErrorRecord err in errors)
                     {
                       System.Console.WriteLine("    error: {0}", err.ToString());
                     }
                 }
              }
              catch (RuntimeException runtimeException)
              {
                // Trap any exception generated by the commands. These exceptions
                // will all be derived from the RuntimeException exception.
                System.Console.WriteLine(
                              "Runtime exception: {0}: {1}\n{2}",
                              runtimeException.ErrorRecord.InvocationInfo.InvocationName,
                              runtimeException.Message,

 runtimeException.ErrorRecord.InvocationInfo.PositionMessage);
         }
       }

             System.Console.WriteLine("\nHit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2231 -->

Runspace05 Sample
This sample shows how to add a snap-in to a
System.Management.Automation.Runspaces.InitialSessionState object so that the cmdlet of the
snap-in is available when the runspace is opened. The snap-in provides a Get-Proc cmdlet
(defined by the GetProcessSample01 Sample) that is run synchronously by using a
System.Management.Automation.PowerShell object.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

     Creating a System.Management.Automation.Runspaces.InitialSessionState object.

     Adding the snap-in to the System.Management.Automation.Runspaces.InitialSessionState
     object.

     Creating a System.Management.Automation.Runspaces.Runspace object that uses the
     System.Management.Automation.Runspaces.InitialSessionState object.

     Creating a System.Management.Automation.PowerShell object that uses the runspace.

     Adding the snap-in's Get-Proc cmdlet to the pipeline of the
     System.Management.Automation.PowerShell object.

     Running the command synchronously.

     Extracting properties from the System.Management.Automation.PSObject objects
     returned by the command.

Example
This sample creates a runspace that uses a
System.Management.Automation.Runspaces.InitialSessionState object to define the elements

<!-- p.2232 -->

that are available when the runspace is opened. In this sample, a snap-in that defines a Get-
Proc cmdlet is added to the initial session state.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Collections.ObjectModel;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;
   using PowerShell = System.Management.Automation.PowerShell;

    /// <summary>
    /// This class contains the Main entry point for this host application.
    /// </summary>
    internal class Runspace05
    {
      /// <summary>
      /// This sample shows how to define an initial session state that is
      /// used when creating a runspace. The sample invokes a command from
      /// a Windows PowerShell snap-in that is present in the console file.
      /// </summary>
      /// <param name="args">The parameter is not used.</param>
      /// <remarks>
      /// This sample assumes that user has copied the GetProcessSample01.dll
      /// that is produced by the GetProcessSample01 sample to the current
      /// directory.
      /// This sample demonstrates the following:
      /// 1. Creating a default initial session state.
      /// 2. Adding a snap-in to the initial session state.
      /// 3. Creating a runspace that uses the initial session state.
      /// 4. Creating a PowerShell object that uses the runspace.
      /// 5. Adding the snap-in's Get-Proc cmdlet to the PowerShell object.
      /// 6. Using PSObject objects to extract and display properties from
      ///    the objects returned by the cmdlet.
      /// </remarks>
      private static void Main(string[] args)
      {
        // Create the default initial session state. The default initial
        // session state contains all the elements provided by Windows
        // PowerShell.
        InitialSessionState iss = InitialSessionState.CreateDefault();
        PSSnapInException warning;
        iss.ImportPSSnapIn("GetProcPSSnapIn01", out warning);

        // Create a runspace. Notice that no PSHost object is supplied to the
        // CreateRunspace method so the default host is used. See the Host
        // samples for more information on creating your own custom host.
        using (Runspace myRunSpace = RunspaceFactory.CreateRunspace(iss))
        {
          myRunSpace.Open();

<!-- p.2233 -->

              // Create a PowerShell object.
              using (PowerShell powershell = PowerShell.Create())
              {
                // Add the snap-in cmdlet and specify the runspace.
                powershell.AddCommand("GetProcPSSnapIn01\\Get-Proc");
                powershell.Runspace = myRunSpace;

                  // Run the cmdlet synchronously.
                  Collection<PSObject> results = powershell.Invoke();

                  Console.WriteLine("Process              HandleCount");
                  Console.WriteLine("--------------------------------");

                  // Display the results.
                  foreach (PSObject result in results)
                  {
                    Console.WriteLine(
                                      "{0,-20} {1}",
                                      result.Members["ProcessName"].Value,
                                      result.Members["HandleCount"].Value);
                  }
              }

              // Close the runspace to release any resources.
              myRunSpace.Close();
             }
             System.Console.WriteLine("Hit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2234 -->

Runspace06 Sample
This sample shows how to add a module to a
System.Management.Automation.Runspaces.InitialSessionState object so that the module is
loaded when the runspace is opened. The module provides a Get-Proc cmdlet (defined by the
GetProcessSample02 Sample) that is run synchronously by using a
System.Management.Automation.PowerShell object.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

     Creating a System.Management.Automation.Runspaces.InitialSessionState object.

     Adding the module to the System.Management.Automation.Runspaces.InitialSessionState
     object.

     Creating a System.Management.Automation.Runspaces.Runspace object that uses the
     System.Management.Automation.Runspaces.InitialSessionState object.

     Creating a System.Management.Automation.PowerShell object that uses the runspace.

     Adding the module's Get-Proc cmdlet to the pipeline of the
     System.Management.Automation.PowerShell object.

     Running the command synchronously.

     Extracting properties from the System.Management.Automation.PSObject objects
     returned by the command.

Example
This sample creates a runspace that uses a
System.Management.Automation.Runspaces.InitialSessionState object to define the elements

<!-- p.2235 -->

that are available when the runspace is opened. In this sample, a module that defines a Get-
Proc cmdlet is added to the initial session state.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Collections.ObjectModel;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;
   using PowerShell = System.Management.Automation.PowerShell;

    /// <summary>
    /// This class contains the Main entry point for this host application.
    /// </summary>
    internal class Runspace06
    {
      /// <summary>
      /// This sample shows how to define an initial session state that is
      /// used when creating a runspace. The sample invokes a command from
      /// a binary module that is loaded by the initial session state.
      /// </summary>
      /// <param name="args">Parameter not used.</param>
      /// <remarks>
      /// This sample assumes that user has copied the GetProcessSample02.dll
      /// that is produced by the GetProcessSample02 sample to the current
      /// directory.
      /// This sample demonstrates the following:
      /// 1. Creating a default initial session state.
      /// 2. Adding a module to the initial session state.
      /// 3. Creating a runspace that uses the initial session state.
      /// 4. Creating a PowerShell object that uses the runspace.
      /// 5. Adding the module's Get-Proc cmdlet to the PowerShell object.
      /// 6. Running the command synchronously.
      /// 7. Using PSObject objects to extract and display properties from
      ///    the objects returned by the cmdlet.
      /// </remarks>
      private static void Main(string[] args)
      {
          // Create the default initial session state and add the module.
        InitialSessionState iss = InitialSessionState.CreateDefault();
        iss.ImportPSModule(new string[] { @".\GetProcessSample02.dll" });

        // Create a runspace. Notice that no PSHost object is supplied to the
        // CreateRunspace method so the default host is used. See the Host
        // samples for more information on creating your own custom host.
        using (Runspace myRunSpace = RunspaceFactory.CreateRunspace(iss))
        {
          myRunSpace.Open();

           // Create a PowerShell object.
           using (PowerShell powershell = PowerShell.Create())

<!-- p.2236 -->

                 {
                     // Add the cmdlet and specify the runspace.
                     powershell.AddCommand(@"GetProcessSample02\Get-Proc");
                     powershell.Runspace = myRunSpace;

                     Collection<PSObject> results = powershell.Invoke();

                     Console.WriteLine("Process              HandleCount");
                     Console.WriteLine("--------------------------------");

                     // Display the results.
                     foreach (PSObject result in results)
                     {
                       Console.WriteLine(
                                         "{0,-20} {1}",
                                         result.Members["ProcessName"].Value,
                                         result.Members["HandleCount"].Value);
                     }
                 }

                 // Close the runspace to release any resources.
                 myRunSpace.Close();
             }

             System.Console.WriteLine("Hit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2237 -->

Runspace07 Sample
This sample shows how to create a runspace, and then use that runspace to run two cmdlets
synchronously by using a System.Management.Automation.PowerShell object.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

      Creating a System.Management.Automation.Runspaces.Runspace object by using the
      System.Management.Automation.Runspaces.RunspaceFactory class.

      Creating a System.Management.Automation.PowerShell object that uses the runspace.

      Adding cmdlets to the pipeline of the System.Management.Automation.PowerShell
      object.

      Running the cmdlets synchronously.

      Extracting properties from the System.Management.Automation.PSObject objects
      returned by the command.

Example
This sample creates a runspace that used by a System.Management.Automation.PSObject
object to run the Get-Process and Measure-Object cmdlets.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Collections.ObjectModel;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;
   using PowerShell = System.Management.Automation.PowerShell;

   /// <summary>

<!-- p.2238 -->

/// This class contains the Main entry point for this host application.
/// </summary>
internal class Runspace07
{
  /// <summary>
  /// This sample shows how to create a runspace and how to run commands
  /// using a PowerShell object. It builds a pipeline that runs the
  /// Get-Process cmdlet, which is piped to the Measure-Object
  /// cmdlet to count the number of processes running on the system.
  /// </summary>
  /// <param name="args">The parameter is not used.</param>
  /// <remarks>
  /// This sample demonstrates the following:
  /// 1. Creating a runspace using the RunspaceFactory class.
  /// 2. Creating a PowerShell object that uses the runspace.
  /// 3. Adding cmdlets to the pipeline of the PowerShell object.
  /// 4. Running the cmdlets synchronously.
  /// 5. Working with PSObject objects to extract properties
  ///    from the objects returned by the cmdlets.
  /// </remarks>
  private static void Main(string[] args)
  {
    Collection<PSObject> result;     // Will hold the result
                                     // of running the cmdlets.

   // Create a runspace. We can't use the RunspaceInvoke class
   // because we need to get at the underlying runspace to
   // explicitly add the commands. Notice that no PSHost object is
   // supplied to the CreateRunspace method so the default host is
   // used. See the Host samples for more information on creating
   // your own custom host.
   using (Runspace myRunSpace = RunspaceFactory.CreateRunspace())
   {
     myRunSpace.Open();

     // Create a PowerShell object and specify the runspace.
     PowerShell powershell = PowerShell.Create();
     powershell.Runspace = myRunSpace;

     // Use the using statement so we dispose of the PowerShell object
     // when we're done.
     using (powershell)
     {
       // Add the Get-Process cmdlet to the PowerShell object. Notice
       // we are specify the name of the cmdlet, not a script.
       powershell.AddCommand("Get-Process");

         // Add the Measure-Object cmdlet to count the number
         // of objects being returned. Commands are always added to the end
         // of the pipeline.
         powershell.AddCommand("Measure-Object");

         // Run the cmdlets synchronously and save the objects returned.
         result = powershell.Invoke();
     }

<!-- p.2239 -->

                 // Even after disposing of the pipeLine, we still need to set
                 // the powershell variable to null so that the garbage collector
                 // can clean it up.
                 powershell = null;

                 // Display the results of running the commands (checking that
                 // everything is ok first.
                 if (result == null || result.Count != 1)
                 {
                   throw new InvalidOperationException(
                             "pipeline.Invoke() returned the wrong number of objects");
                 }

                 PSMemberInfo count = result[0].Properties["Count"];
                 if (count == null)
                 {
                   throw new InvalidOperationException(
                             "The object returned doesn't have a 'count' property");
                 }

                 Console.WriteLine(
                            "Runspace07: The Get-Process cmdlet returned {0} objects",
                            count.Value);

                 // Close the runspace to release any resources.
                 myRunSpace.Close();
             }

             System.Console.WriteLine("Hit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2240 -->

Runspace08 Sample
This sample shows how to add commands and arguments to the pipeline of a
System.Management.Automation.PowerShell object and how to run the commands
synchronously.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

      Creating a System.Management.Automation.Runspaces.Runspace object by using the
      System.Management.Automation.Runspaces.RunspaceFactory class.

      Creating a System.Management.Automation.PowerShell object that uses the runspace.

      Adding cmdlets to the pipeline of the System.Management.Automation.PowerShell
      object.

      Running the cmdlets synchronously.

      Extracting properties from the System.Management.Automation.PSObject objects
      returned by the command.

Example
This sample runs the Get-Process and Sort-Object cmdlets by using a
System.Management.Automation.PowerShell object.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Collections.Generic;
   using System.Collections.ObjectModel;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;
