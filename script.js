let displayingData = document.getElementById('currently-displaying');
let gameStats = document.getElementById('game-stats');

let tittle  = document.getElementById('Tittle');
const bottomSection = document.getElementById('bottom-section')
const bottomClass = document.getElementsByClassName('bottom')
const btn = document.getElementsByTagName('button');


[...btn].forEach(nexty => {
    nexty.addEventListener("click", () => {
        // clear out display, create new div element, set the content inside the 
        // new div, and append to a particlar element
        displayingData.innerHTML = "";
        let gameOutput = document.createElement('div');
        gameOutput.id = 'gameOutput';  
        displayingData.append(gameOutput);

let newText = document.createElement('div');
newText.className = 'putting-text';   
displayingData.appendChild(newText);

        displayingData.innerHTML = '<img id="blackhole" src="images/Black_hole_representation.gif" alt="This is a gif of a blackhole"/>';




        displayingData.classList.add('show');

        tittle.style.animation = "leaveQuietly 2s ease-out forwards";
        console.log(bottomSection);
        bottomSection.style.display = "flex";
    
        setTimeout(() =>  { tittle.remove();
            tittle.remove()
            bottomSection.style.backgroundImage = "url('images/console.jpeg')";

        } , 5000);

        let yuhsuh = document.createElement('p');
        yuhsuh.className = "text-output"
        displayingData.append(yuhsuh);
    });
});


