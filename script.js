let displayingData = document.getElementById('currently-displaying');
let tittle  = document.getElementById('Tittle');
const btn = document.getElementsByTagName('button');

console.log("yellor");

[...btn].forEach(nexty => {
    nexty.addEventListener("click", () => {

        // Remove any existing content
        displayingData.innerHTML = "";

        // Add the image with the 'blackhole' ID
        displayingData.innerHTML = '<img id="blackhole" src="images/Black_hole_representation.gif" alt="This is a gif of a blackhole"/>';

        // Add the 'show' class to trigger the animation
        displayingData.classList.add('show');

        tittle.style.animation = "leaveQuietly 5s ease forwards";
        setTimeout(() =>  tittle.innerHTML = "" , 5000); 

    });
});
