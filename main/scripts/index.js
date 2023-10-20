const sidebar = document.querySelector('.sidebar-div')
const body = document.body
const height = Math.max(body.scrollHeight, body.offsetHeight)
console.log(height)
sidebar.style.height = height