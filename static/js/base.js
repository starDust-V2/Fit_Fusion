
    const ham = document.querySelector(".ham");
    const navbar = document.querySelector("nav");
    const navLinks = document.querySelectorAll(".nav-link");
    const sideMenu = document.querySelector(".side-menu")
    const homeNavbar = document.querySelector("#home-nav");

    const hero = document.querySelector(".hero");
    const overlayOn = document.querySelector(".overlay.on")
    const overlay = document.querySelector(".overlay")

    const slider = document.querySelector('.slider')
    if(slider){
        // slider.style.top = `${2 + 4 * activeLinkPos}rem`
    }
    const sideMenuLinks = document.querySelectorAll(".side-menu-links a");
    const loc = ['home','chat','exercise','book','subscribe','analyze'];
    
    
    for(let i in Object.keys(sideMenuLinks)){
        sideMenuLinks[i].addEventListener("click", ()=>{
                window.location.href = `/${loc[i]}/`;
        });
    }



    ham.addEventListener('click',()=>{
        ham.classList.toggle("open");
        navbar.classList.toggle("open");  
        sideMenu.classList.toggle("open");
        
        // if home page is activate
        if(homeNavbar){
            hero.classList.toggle("normal-overlay");
            overlay.classList.toggle("on")

        } 
        
    });

    overlay.addEventListener('click',()=>{
        if(hero.classList.contains('normal-overlay')){
            ham.classList.toggle("open");
            navbar.classList.toggle("open");  
            sideMenu.classList.toggle("open");
            
            // if home page is activate
            if(homeNavbar){
                hero.classList.toggle("normal-overlay");
                overlayOn.classList.toggle("on")
            } 
        }   
    });

    navLinks.forEach((elem)=>{
        elem.addEventListener("click",()=>{
            ham.classList.toggle("open");
            navbar.classList.toggle("open"); 
        })
    })
