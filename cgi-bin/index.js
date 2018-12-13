#!/usr/bin/env python3

print('''
//JS for index page buttons

document.getElementById("create").addEventListener('click', create_nav);
document.getElementById("explore").addEventListener('click', explore_nav);

function create_nav() {
  var create = document.getElementById("create_nav");
  create.submit();
}

function explore_nav() {
  var explore = document.getElementById("explore_nav");
  explore.submit();
}
''')
