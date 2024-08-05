
// for active link effects
var nav_links = document.getElementsByClassName("nav-link")

for( link of nav_links){
    link.addEventListener('click',(ev)=>{
        var element = ev.target;

        element.classList.add("active-link");

        for (i of nav_links){
            if (i!= element){
                i.classList.remove('active-link');

            }
        }

    })
}
