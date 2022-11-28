const fs      = require('fs')
const {JSDOM} = require("jsdom");

class Signer {
	__window__ = null;

    constructor() {
        const script_01 = fs.readFileSync(__dirname + "/files/louder.min.js", "utf-8");
        const script_02 = fs.readFileSync(__dirname + "/files/cloudobf.min.js", "utf-8");
        const script_03 = fs.readFileSync(__dirname + "/files/index.min.js", "utf-8");
        const jQuery    = fs.readFileSync(__dirname + "/files/jquery.min.js", "utf-8");
        const funcs     = fs.readFileSync(__dirname + "/func.js", "utf-8");

        const {window}  = new JSDOM("", {
            runScripts: "outside-only",
        });

        this.__window__ = window;
        this.__window__.eval(jQuery)
        this.__window__.eval(script_01);
        this.__window__.eval(script_02);
        this.__window__.eval(script_03);
        this.__window__.eval(funcs);
    }

    sign(data, _input, ts) {
        return this.__window__.sign(data, _input, ts);
    }

    init() {
        return this.__window__.init();
    }
}

// const signer = new Signer()
// let sig = signer.sign("a=1&b=2")
// console.log(sig)

module.exports = Signer;