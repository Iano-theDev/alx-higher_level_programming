#!/usr/bin/node
'use strict';
let arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
