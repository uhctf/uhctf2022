# Solution
This is a white-box challenge as we are given the source code of the Discord bot.

Skimming the code should draw our attention to a few things:

## `commands/flag.cjs`
This is our goal. Notice how the bot requires `debug_mode` to be set on `command.user`.

We look up `command.user` in the [discord.js docs](https://discord.js.org/#/docs/discord.js/stable/class/CommandInteraction?scrollTo=user) and learn that this is an instance of an `User` object. The `User` object does not have `debug_mode` by default.

We can work backwards from here.

## `commands/debug.cjs`
This command is the only place where `debug_mode` is set directly. However, non-admins have no access to it.

There is little code here which could go wrong, so it's unlikely that this could be exploited.

## `commands/quiz.cjs`
The quiz commands seems like a fun random addition. However, it has a lot of code and complexity. There is also a notable TODO left by the author: "// TODO: does this have any side-effects? 🤔". Side-effects are not intrinsically "evil", but can easily lead to unexpected behaviour.

The function `merge_quiz_objects` merges objects (quizzes) recursively. If done incorrectly, this is a vulnerability in JavaScript.

## Prototype pollution
To understand the vulnerability, we must first understand how JavaScript works. Everything in JS is an object (even functions). However, it does not have classes but uses prototypes instead. The `class` keyword is only syntax sugar!

To create a class we would do the following:
```js
// this is the constructor
let MyClass = function () {
   this.a = 1;
};
let my_instance = new MyClass(); // {a: 1}
```

`MyClass` has a `prototype` property. `prototype` is an object itself and has `a = 1` set. This means the actual "class definition" is stored in this `prototype`.

To add a method we can do the following:
```js
MyClass.prototype.get_a = function () {
   return this.a;
};
my_instance.get_a(); // 1
```

Notice 2 things here:
1. we directly accessed the `prototype` of `MyClass`.
2. we added the method *after* the class/constructor/prototype was created, and the change was also applied to the instance of the class.

This is because instances of classes have a `__proto__` property which links to the `prototype` of its class:
```js
my_instance.__proto__ === MyClass.prototype // true
```

But if `get_a` is defined on `prototype`, why can we simply call `my_instance.get_a()`? Would it not have to be `my_instance.__proto__.get_a()`? This is where prototype chaining comes in.

If JS does not find a property (variable or function) on an object, it will try to look it up on its `__proto__`. Even better, if `__proto__` does not have it, the property will be looked up on the parent object's `__proto__`. This is called prototype chaining and is how JS implements inheritance. The chain continues all the way up to `Object.prototype`. `Object` is the ancestor of *every* object in JS!

We now know enough to understand the prototype pollution vulnerability! To get the flag, the code checks `command.user.debug_mode`. However, this `debug_mode` does not exist. Thus, JS would start walking up the chain all the way to `Object`. So we only have to figure out a way to add `debug_mode` to `Object`.

This is where the recursive merge function `merge_quiz_objects` comes in. By merging `{__proto__: {debug_mode: true}}` onto `{}`, the prototype of `Object` is changed.

## Payload
1. Create a new quiz: `/quiz create quiz_name:__proto__ question_count:1 `.
2. Add a question: `debug_mode: 1`.
3. Get flag!

## Conclusion
- **How would I recognise this vulnerability in the future?** Prototype pollution only occurs when recursively and dynamically assigning properties to an object. Thus, simply look for functions which merge objects, similar to `merge_quiz_objects`.
- [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
- [JavaScript prototype pollution attack in NodeJS](https://github.com/HoLyVieR/prototype-pollution-nsec18/blob/master/paper/JavaScript_prototype_pollution_attack_in_NodeJS.pdf)