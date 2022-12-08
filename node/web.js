'use strict';

const express = require('express');
const fs = require("fs");

//var numbersOneCSV = require('./data_files/numbers-1.csv');
//var numbersTwoCSV = require('./data_files/numbers-2.csv');
var testJson = require('./data_files/test.json');

const PORT = 3000;
const HOST = '0.0.0.0';

const app = express();

app.get('/headers', (req, res) => {
    res.send(testJson);
});

app.get('/csv_one', (req, res) => {
    fs.readFile("./data_files/numbers-1.csv", "utf8", function (err, data) {
        res.send(data);
    });

    //var numbersOneCSV = fs.readFileSync('./data_files/numbers-1.csv', 'utf8')
    //res.send(numbersOneCSV)

    //res.send("one, 1\ntwo, 2\nthree, 3");
});

app.get('/csv_two', (req, res) => {
    fs.readFile("./data_files/numbers-2.csv", "utf8", function (err, data) {
        res.send(data);
    });

    //res.send("ten, 10\neleven, 11\ntwelve, 12");
});

app.listen(PORT, HOST, () => {
    console.log(`Running on http://${HOST}:${PORT}`);
});