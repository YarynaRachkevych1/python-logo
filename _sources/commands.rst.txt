.. _commands:

Commands
===========================

This document provides an overview of the commands and expressions supported
by the python-logo parser and interpreter.

Turtle Visibility Commands
--------------------------

These commands control whether the turtle (the drawing cursor) is visible
on the screen.

**hideturtle** (alias: **ht**)

    Hides the turtle icon so that it is no longer visible on the drawing area.

    **Syntax:**

    .. code-block::

       hideturtle

    or

    .. code-block::

       ht

**showturtle** (alias: **st**)

    Shows the turtle icon if it has been hidden.

    **Syntax:**

    .. code-block::

       showturtle

    or

    .. code-block::

       st

Pen Control Commands
--------------------

These commands allow you to control the pen's state and appearance.

**penup** (alias: **pu**)

    Lifts the pen off the drawing surface so that subsequent movements
    do not produce a trail.

    **Syntax:**

    .. code-block::

       penup

    or

    .. code-block::

       pu

**pendown** (alias: **pd**)

    Lowers the pen onto the drawing surface so that movements will draw lines.

    **Syntax:**

    .. code-block::

       pendown

    or

    .. code-block::

       pd

**setpencolor**

    Changes the drawing (pen) color. The color is provided as a string.
    Available colors are **white**, **black**, **red**,
    **green**, **blue** and **cyan**.

    **Syntax:**

    .. code-block::

       setpencolor <color>

    **Example:**

    .. code-block::

       setpencolor red

**setpensize**

    Sets the thickness of the pen. The provided expression must evaluate to a number.

    **Syntax:**

    .. code-block::

       setpensize <expr>

    **Example:**

    .. code-block::

       setpensize 3

Movement Commands
-----------------

These commands control the movement and orientation of the turtle.

**forward** (alias: **fd**)

    Moves the turtle forward by the specified number of units.

    **Syntax:**

    .. code-block::

       forward <expr>

    or

    .. code-block::

       fd <expr>

**backward** (alias: **bk**)

    Moves the turtle backward by the specified number of units.

    **Syntax:**

    .. code-block::

       backward <expr>

    or

    .. code-block::

       bk <expr>

**left** (alias: **lt**)

    Rotates the turtle to the left by the specified angle in degrees.

    **Syntax:**

    .. code-block::

       left <expr>

    or

    .. code-block::

       lt <expr>

**right** (alias: **rt**)

    Rotates the turtle to the right by the specified angle in degrees.

    **Syntax:**

    .. code-block::

       right <expr>

    or

    .. code-block::

       rt <expr>

**setpos**

    Moves the turtle to a new absolute position specified by x and y coordinates.

    **Syntax:**

    .. code-block::

       setpos <expr> <expr>

    **Example:**

    .. code-block::

       setpos 100 200

Output Command
--------------

**print**

    Evaluates a logic expression (which may include numbers, variables,
    and more complex expressions) and prints its result.

    **Syntax:**

    .. code-block::

       print [<logic_expr>]

    **Example:**

    .. code-block::

       print [ 5 + 3 ]

Control Structures
------------------

These commands allow for conditional execution and looping.

**repeat**

    Repeats a block of commands a specified number of times. The expression
    determines the number of iterations.

    **Syntax:**

    .. code-block::

       repeat <expr> [ <command> ... ]

    **Example:**

    .. code-block::

       repeat 4 [ forward 100 right 90 ]

**if**

    Executes a block of commands if a given condition is true. An optional
    ``else`` block can be provided to execute alternative commands when the
    condition is false.

    **Syntax:**

    .. code-block::

       if <logic_expr> [ <command> ... ] [ else [ <command> ... ] ]

    **Example:**

    .. code-block::

       if :x > 10 [ forward 50 ] else [ backward 50 ]

    *Note:* Conditions can be Boolean values (``true`` or ``false``) or more
    complex logic expressions using comparison and logical operators.

Variable Commands
-----------------

**make**

    Creates or updates a variable with the specified name and assigns it the value
    of the evaluated expression. When referring to variables, use a preceding colon.

    **Syntax:**

    .. code-block::

       make <var_name> <logic_expr>

    **Example:**

    .. code-block::

       make size 100

    Variables can then be referenced as ``:size`` in subsequent expressions.

List Operations
---------------

These commands provide functionality for working with lists.

**list**

    Creates a new list variable, optionally initializing it with elements.

    **Syntax:**

    .. code-block::

       list <var_name> [ <logic_expr> ... ]

    **Example:**

    .. code-block::

       list myList [ 1 2 3 ]

**set**

    Sets the value at a specified index in a list.

    **Syntax:**

    .. code-block::

       set <variable> <number> <expr>

    **Example:**

    .. code-block::

       set :myList 1 42

**get**

    Retrieves the value from a list at the specified index.

    **Syntax:**

    .. code-block::

       get <variable> <number>

    **Example:**

    .. code-block::

       get :myList 2

**insert**

    Inserts a value into a list at the given index.

    **Syntax:**

    .. code-block::

       insert <variable> <number> <expr>

    **Example:**

    .. code-block::

       insert :myList 0 99

**remove**

    Removes the element at the specified index from a list.

    **Syntax:**

    .. code-block::

       remove <variable> <number>

    **Example:**

    .. code-block::

       remove :myList 1

**remove_value**

    Removes the first occurrence of an element that matches the evaluated expression.

    **Syntax:**

    .. code-block::

       remove_value <variable> <logic_expr>

    **Example:**

    .. code-block::

       remove_value :myList 42

**len**

    Returns the number of elements in the specified list.

    **Syntax:**

    .. code-block::

       len <variable>

    **Example:**

    .. code-block::

       len :myList

**empty**

    Checks if the specified list is empty.

    **Syntax:**

    .. code-block::

       empty <variable>

    **Example:**

    .. code-block::

       empty :myList

Function Definitions and Calls
-------------------------------

These commands enable the creation and invocation of custom functions.

**Function Definition (func_def)**

    Defines a new function using the ``to`` ... ``end`` block. Functions can have
    arguments (which are variables) and consist of one or more commands.

    **Syntax:**

    .. code-block::

       to <func_name> [<variable> ...]
         <command> ...
       end

    **Example:**

    .. code-block::

       to square :size
         repeat 4 [ forward :size right 90 ]
       end

**Function Call (func_call)**

    Calls a previously defined function and passes any required arguments.

    **Syntax:**

    .. code-block::

       <func_name> [<expr> ...]

    **Example:**

    .. code-block::

       square 50

Expressions and Operators
-------------------------

Logo expressions are used in many commands to calculate values and conditions.
Expressions are divided into three main categories:

- **Arithmetic Expressions (expr)**
- **Comparison Expressions (compare_expr)**
- **Logical Expressions (logic_expr)**

Arithmetic Expressions (expr)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Arithmetic expressions combine numbers, variables, and arithmetic operators
to produce numerical values. The supported operators include:

- Addition: ``+``
- Subtraction: ``-``
- Multiplication: ``*``
- Division: ``/``
- Exponentiation: ``^``
- Unary negation: ``-``

Parentheses can be used to change operator precedence.

**Examples:**

.. code-block::

   ; A simple arithmetic expression
   make result 5 + 3

.. code-block::

   ; Using variables and grouping
   make x 10
   make y 20
   make sum (x + y) * 2

Comparison Expressions (compare_expr)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comparison expressions evaluate relationships between arithmetic expressions.
They use operators such as:

- Greater than: ``>``
- Greater than or equal to: ``>=``
- Less than: ``<``
- Less than or equal to: ``<=``
- Equal to: ``=``
- Not equal to: ``<>``

These expressions are often used in conditional statements.

**Examples:**

.. code-block::

   ; A simple comparison
   if 5 > 3 [ print [true] ]

.. code-block::

   ; Comparing variables and expressions
   make x 15
   if (x + 5) = 20 [ forward 50 ]

Logical Expressions (logic_expr)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Logical expressions allow you to build more complex conditions by combining
comparison expressions using logical operators. The supported logical operators are:

- **AND:** Combines multiple expressions; all must be true.

  **Syntax:**

  .. code-block::

     AND [ <logic_expr> <logic_expr> ... ]

- **OR:** Combines multiple expressions; at least one must be true.

  **Syntax:**

  .. code-block::

     OR [ <logic_expr> <logic_expr> ... ]

- **NOT:** Inverts the truth value of an expression.

  **Syntax:**

  .. code-block::

     NOT [ <logic_expr> ]

Logical expressions are commonly used in ``if`` commands and loops.

**Examples:**

.. code-block::

   ; Using AND to combine conditions
   make x 15
   make y 5
   if AND [ x > 10 y < 10 ] [ forward 50 ]

.. code-block::

   ; Using OR for multiple possible conditions
   if OR [ :x > 10 :y > 10 ] [ forward 50 ] else [ backward 50 ]

.. code-block::

   ; Using NOT to invert a condition
   if NOT [ :x <= 0 ] [ forward 50 ]
