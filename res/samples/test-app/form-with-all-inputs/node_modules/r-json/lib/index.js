"use strict";

// Dependencies
var Fs = require("fs");
var WriteJson = require("w-json");

/**
 * rJson
 *
 * @name rJson
 * @function
 * @param {String} path The JSON file path.
 * @param {Function} callback An optional callback. If not passed, the function will run in sync mode.
 */
function rJson(path, callback) {

    if (typeof callback === "function") {
        Fs.readFile(path, "utf-8", function (err, data) {
            try {
                data = JSON.parse(data);
            } catch (e) {
                err = err || e;
            }
            callback(err, data);
        });
        return;
    }

    return JSON.parse(Fs.readFileSync(path));
}

/**
 * rJson_default
 * 
 * If there is some error in reading the JSON file, this would overwrite the file with the default
 *      value and return the same.
 * This uses [node-w-json](https://github.com/IonicaBizau/node-w-json) for writing the default JSON
 *      value and so you can pass configs to node-w-json to beautify the file written
 *
 * @name rJson_default
 * @function
 * @param {String} path The JSON file path.
 * @param {Object} def_value The Default Value
 * @param {Object|Number|Boolean} w_json_options Optional: w-json config object containing the fields below.
 * If boolean, it will be handled as `new_line`, if number it will be handled as `space`.
 *
 *  - `space` (Number): An optional space value for beautifying the json output (default: `2`).
 *  - `new_line` (Boolean): If `true`, a new line character will be added at the end of the stringified content.
 *
 * @param {Function} callback An optional callback. If not passed, the function will run in sync mode.
 */
function rJson_default(path, def_value, w_json_options, callback) {
    if (def_value == undefined) {
        def_value = {};
    }
    if (typeof w_json_options === "function") {
        callback = w_json_options;
        w_json_options = {};
    }

    if (typeof callback === "function") {
        return Fs.readFile(path, "utf-8", function (err, data) {
            try {
                data = JSON.parse(data);
                callback(null, data);
            } catch (e) {
                err = null;
                data = def_value;
                try {
                    WriteJson(path, def_value, w_json_options);
                } catch (e2) {
                    err = err || e2;
                }
                callback(err, data);
            }
        });
    }

    try {
        return JSON.parse(Fs.readFileSync(path));
    } catch (err) {
        WriteJson(path, def_value, w_json_options);
        return def_value;
    }
}

module.exports = rJson;
module.exports.defaultRead = rJson_default;