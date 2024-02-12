#!/usr/bin/node
const { argv } = require('node:process');
const count  = 0;

argv.forEach((arg) =>{
    count++;
});

if (count === 0){
    console.log("No argument")
} else if (count === 1){
    console.log("Argument found")
} else if (count > 1){
    console.log("Arguments found")
}
