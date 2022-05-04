# Kata Rules

Below are some kata rules that can be used with different katas to learn some particular skills.

This list can be modified or added to; look to whatever it is you are trying to practise!

## Object Calisthenics (Jeff Bay)

Ref: [Object Calisthenics](https://bolcom.github.io/student-dojo/legacy-code/DevelopersAnonymous-ObjectCalisthenics.pdf)

These rules are most likely much more stringent that you will have ever used in projects before.

They are meant to provide a hard exercise to challenge you and ingrain certain rules of clean coding.

Going to this extreme level of constraint should help to ingrain these concepts so that they can be used without going to quite such extremes in projects, applying whichever rules make sense at the time. Try it out!

1. No more than one level of indentation per method.
2. Do not use the else keyword.
3. Wrap all primitives and strings.
4. Follow the rule of first class collections.
5. One dot per line.
6. Do not abbreviate.
7. Keep all entities small.
8. No classes with more than two instance variables.
9. No getters, setters, or properties.

## Clean Code (Robert C. Martin)

Ref: [Clean Code Gist](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29)

What follows is a list of some basics from the Clean Code book by Robert C. Martin.

This is another set of somewhat constraining rules, but these rules make sense in the general case almost all the time. Similar caveats apply here regarding practice, but these are much more directly translatable without too much thought needed.

#### Names

1. Names should be long enough to fully describe the intent, and no shorter.
2. For methods: the lower the scope, the longer the name.
3. For variables: the higher the scope, the longer the name.
4. Names should be pronounceable.
5. No acronyms.
6. No noise words (manager, info, data, etc).

#### Sizing

1. No methods with more than three arguments. For a challenge, try no more than two.
2. No methods with any boolean arguments.
3. Methods must do one thing. Extract methods to other methods/classes until you can't anymore.
4. Methods should contain one level of abstraction lower than the method name, and no lower. High-level business rules should not also contain errors, logs, message formatting, string buffers, or the like.
5. Classes must do one thing. If not, extract to another class.
6. Separate classes logically into files.
7. An extra challenge: 10 lines or fewer per method, 70 lines or fewer per class.

#### Comments

No comments!

If you have a comment, you have failed to describe intent with semantics and good names.

This should be especially the case in a small problem with a kata.

If you can understand, and the average programmer who knows the given programming language can understand it, you don't need the comment 99% of the time. If they can't understand it, your code is probably bad rather than needing commented. So refactor!

#### Errors

1. No error codes.
2. Use exceptions.
3. No try/catch or similar in a method unless it's the only thing in the method.

#### TDD

1. Do it.
2. Do it first, as per TDD rules.
3. Do not allow the production code to become more specific in between cycles of Red/Green/Refactor.
4. Do not allow the test code to become more generic in between cycles of Red/Green/Refactor.
5. Do not "go for the gold" of the problem at hand. Bite off small bits at the periphery until there is nothing else you can possibly think of to check before needing to write the meat of the algorithm/data structure/program/etc. This will help you to not become "stuck" in TDD.
6. Achieve 100% coverage.

## Simple OOP Design Guidelines

What follows are a list of simpler design guidelines that can be combined as you wish and practised. Practising one at a time can still be effective, but they could potentially be combined if the kata is simple enough.

### Command Query Separation

Ref: [Command Query Separation](https://martinfowler.com/bliki/CommandQuerySeparation.html)

This is a fairly simple principle that tries to separate method behavior which alters the system state, and that which doesn't.

Command can be thought of as telling the system to do something. This might be setting a variable, computing a value, etc. These usually change system state. Try to use predicates like set, compute, run, etc, and return null/none/void.

Queries can be thought of as asking a question of the system. This is often getting the value of a variable. These usually do not change system state. Try to use predicates like get, does, etc, and return some value.

1. A method should command OR query.
2. A command should return nothing and should change the state of the system.
3. A query should return something and should not change the state of the system. 

### Tell, Don't Ask

Ref: [Tell Don't Ask](https://martinfowler.com/bliki/TellDontAsk.html)

This principle's goal is to keep objects highly cohesive. Objects are supposed to be bundles of data and behavior related to that data, and this principle encourages keeping it that way. Do not ask an object for data and then act on it, tell an object what needs to happen and trust that it will "make it so".

1. Tell an object what to do.
2. Do not ask for an object's data and then do something yourself.
3. Do not ask an object what it can do.
4. Do not ask an object if it was successful.
5. Do not ask an object for its data!
6. Think of object-object interaction as simply exchanging messages that each would want to read and are not rude.

### No Wizards
###### Oddly enough, given that we waggle our fingers a lot, say arcane stuff (to most), and turn thoughts into reality...

This is simply a rule that says you need to deal with magic values sitting throughout the code that do not have one single home, where a team of developers could have a collision.

1. Do not use magic numbers.
2. Do not use magic strings.
4. Prefer enums where possible, or something similarly semantic.

### Law of Demeter

Ref: [Law of Demeter](https://www.geeksforgeeks.org/law-of-demeter-in-java-principle-of-least-knowledge/)

This is a principle that promotes high cohesion and loose coupling by encouraging fewer dependencies and not passing messages between objects that shouldn't be dependencies.

1. You may talk to yourself (your own scope).
2. You may talk to your friends (your direct dependencies).
3. You may not talk to your friends' friends.
4. In other words, don't talk to strangers.
5. Don't have very many dependencies, and don't talk to your dependencies' dependencies.

### Use Duck Typing if you Have It

This applies to only dynamic languages that have "duck typing", such as Python.

Duck typing means that your object's type is inferred by the interpreter rather than a required specification by the compiler.

For example, by implementing certain "dunder" methods, any Python class can be considered of a Collection type, and collection-oriented keywords used upon them.

1. Use duck typing where it makes sense rather than inheritance.
2. Use as little inheritance as possible.
3. Use protocols instead of interfaces where possible, or neither if impossible.

### Prefer Composition over Inheritance

If you do not have duck typing, prefer to compose objects with its natural dependencies rather than inheriting from them. Over time, complex inheritance can lead to objects that have boilerplate code it never uses and methods that make no sense or raise questions when initially reading the code.

1. Prefer to compose objects with other objects, preferably through a layer of abstraction.
2. Prefer to use inheritance only with interfaces / polymorphic dispatch abstraction.
3. Prefer to not use inheritance when you can.
4. Consider patterns like Strategy.

## SOLID Principles

Ref: [Wikipedia Article](https://en.wikipedia.org/wiki/SOLID)

Ref: [Clean Coder - SOLID Relevance](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)

Ref: [Clean Coders - SOLID](https://cleancoders.com/series/clean-code/solid-principles)

The SOLID principles are an acronym of five principles related specifically to object-oriented software, particularly those which are statically typed and compiled.

This is why we suggest above that this guide works best with OOP, as these and other design principles apply partially to functional, procedural, and multi-paradigm languages. This especially applies to SOLID.

That is not to say these don't apply to all software, they are simply geared with one type of software in mind, so you will have to do some extra work to think about how it may be different for you. 

Much more than what is below can be researched on your own, but focusing on one at a time can be helpful. Once you get a handle on them, try all five, but it may take you longer than a typical "kata".

### SOLID: Single Responsibility Principle (SRP)

1. Classes and their methods have one reason to change.
2. The reason for the change comes from one actor/role.
3. Classes are grouped by this actor.

### SOLID: Open/Close Principle (OCP)

1. Classes are open for extension: we can add on functionality with other classes / abstractions.
2. Classes are closed for modification: we do not need to modify them to add functionality.

### SOLID: Liskov Substitution Principle (LSP)

1. Subclasses implement everything their parent does (but may implement more).

### SOLID: Interface Segregation Principle (ISP)

1. Ensure no client uses or implements an interface or other abstraction containing any functionality they do not need.
2. Separate such interface/abstractions.
3. Reduce 'fat' interfaces/abstractions.

### SOLID: Dependency Inversion Principle (DIP)

1. Reduce dependency through polymorphic dispatch / abstraction / interfaces.
2. Ensure that dependencies all cross module/package/architectural boundaries in the same direction - FROM low-level details TOWARDS high-level business rules.

## Design Patterns

Ref: [Wikipedia Article](https://en.wikipedia.org/wiki/Software_design_pattern)

Ref: [Design Patterns Book on Amazon](https://www.amazon.com/dp/020163361)

Ref: [Head First Design Patterns on Amazon](https://www.amazon.com/dp/149207800X) (possibly easier read)

Ref: [Clean Coders - Design Patterns](https://cleancoders.com/series/clean-code/design-patterns)

Design Patterns refers to a collection of named OOP software designs which solve a specific problem in a re-usable way.

These patterns are great to know because they represent reusable ideas the software community has had to do for decades.

However, these named design patterns really shine when a team of developers is able to discuss possible solutions by referring to them. "That looks like a Visitor." "Definitely an Observer going on there." "We should probably use Factory to abstract the creation of these into their own structure."

I am not going to list all the patterns, but you can research these and learn them via available online and book resources, then try to make use of them in a kata. The kata may have to be a little bigger and take a little longer, but often not by much.