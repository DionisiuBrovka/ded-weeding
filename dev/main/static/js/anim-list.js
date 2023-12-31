document.addEventListener("DOMContentLoaded", function(e) {
    let animItems = document.getElementsByClassName('anim-items-list');
    
    if (animItems.length > 0 ){
        window.addEventListener('scroll', animOnScroll);
    
        function animOnScroll(){
  
            for (let index = 0; index < animItems.length; index++){
                const animItem = animItems[index];
                const animItemHeight = animItem.offsetHeight;
                const animItemOffset = offset(animItem).top;
                const animStart = 4;
    
                let animItemPoint = window.innerHeight - animItemHeight / animStart;
    
                if( animItemHeight > window.innerHeight ){
                    let animItemPoint = window.innerHeight - window.innerHeight / animStart;
                }
    
                if((pageYOffset >= animItemOffset - animItemPoint) && pageYOffset <= (animItemOffset + animItemHeight)) {
                    animItem.classList.add('active-anim');
                } else {

                }
            }
        }
    
        function offset(el){
            const rect = el.getBoundingClientRect(),
            scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
            scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            return { top: rect.top + scrollTop, left: rect.left + scrollLeft}
        }

        animOnScroll();
    }
})

