module.exports = {
	"env": {
		"browser": true,
		"es6": true
	},
	"extends": "eslint:recommended",
	"globals": {
		"Atomics": "readonly",
		"SharedArrayBuffer": "readonly"
	},
	"parserOptions": {
		"ecmaVersion": 2018,
		"sourceType": "module"
	},
	"rules": {
        "indent": [
            "error",
            4,
            {SwitchCase: 1}
        ],
		"linebreak-style": [
			"error",
			"unix"
		],
		"quotes": [
            "error",
            "double",
            {"allowTemplateLiterals": true}
		],
		"semi": [
			"error",
			"never"
		]
	}
}