const { log } = require("console");

class Person {
    constructor(name) {
        this.name = name
    }

    introduce() {
        console.log(`Hey, my name is ${this.name}`)
    }
}

class Developer extends Person {
    constructor(name, language) {
        super(name);
        this.language = language
    }

    sayHi() {
        console.log(`Hi im ${this.name}`);
    }

    proffession() {
        console.log(`im a ${this.language} developer!`)
    }
}

let ian = new Developer("Nyoix", "Python")
ian.introduce();
ian.sayHi();
ian.proffession();