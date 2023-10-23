alert("dsfasdfdf")
const sidebar = document.querySelector('.sidebar-div')
const body = document.body
const sidebarResize = function(){
    const height = body.scrollHeight
    sidebar.style.height = 0 + 'px' 
    if(height < window.screen.availHeight){
        sidebar.style.height  = window.screen.availHeight + 'px'
    }
    else{sidebar.style.height = height + 'px'}
}
sidebarResize()
window.addEventListener('resize', () => {
    sidebarResize();
});
