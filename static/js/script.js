const icon = document.querySelector(".icon");
const nav = document.querySelector(".nav-bar");
const navLinks = document.querySelectorAll(".nav-link")

icon.addEventListener("click", () => nav.classList.toggle("active"));

navLinks.forEach(function(navLink) {
    navLink.addEventListener("click", () => {
        if(nav.classList.contains("active")){
            nav.classList.remove("active");
        }
    });
});

function changeTo(sectionId) {
    let navbarHeight = document.querySelector('#inicio').offsetHeight;
    let section = document.getElementById(sectionId);

    if (section) {
        let sectionPosition = section.getBoundingClientRect().top;
        let space = navbarHeight; // 10 pixels de margem

        window.scrollBy({
            top: sectionPosition - space,
            left: 0,
            behavior: "smooth",
          });
    }
}

