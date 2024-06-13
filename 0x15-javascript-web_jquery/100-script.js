#!/usr/bin/node
/**
 * Write a JavaScript script that updates the text color of the <header> element
 * to red (#FF0000):
 */

document.addEventListener('load', function () {
    const header = document.querySelector('header');
    header.style.color = '#FF0000';
});