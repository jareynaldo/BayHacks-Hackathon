let displayingData = document.getElementById('currently-displaying');
let gameStats = document.getElementById('game-stats');
let health = document.getElementById('health');

let tittle  = document.getElementById('Tittle');
const bottomSection = document.getElementById('bottom-section')
const topSection = document.getElementById('top-section')
let textOutput = null;
let player_name = "";


const bottomClass = document.getElementsByClassName('bottom')
const btn = document.getElementsByTagName('button');

function starGame(){
console.log("hello");
}

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
        bottomSection.style.animation = "arriveQuietly 4s ease-out forwards";
        health.value = 10;

        bottomSection.style.display = "flex";
        
        doTheTHings();
        let yuhsuh = document.createElement('p');
        yuhsuh.id = "text-output"
        displayingData.append(yuhsuh);
        

        setTimeout(() =>  { 
            topSection.style.height = 40;
            tittle.remove();

        } , 3000);

        textOutput = document.getElementById('text-output');
        textOutput.style.animation = "arriveQuietly 4s ease-out forwards";
        textOutput.classList.add('show');
        textOutput.innerHTML = "Welcome to HyperGator!\n" 
        + "We hired you to bring back unobtainium from the end of the Black Hole." + 
        " Ya know... on account of it being unobtainium and all." + 
        " Anywayssss, that's why we hired you.... <br>What was your name again?"
        + " <br> <br> Enter player name:                         ";    
    });
   
});


function doTheTHings(){
    bottomSection.style.height = "40vh";
    bottomSection.style.marginTop = "10vh";
    bottomSection.style.opacity = "100%";
    bottomSection.style.backgroundImage = "url('images/console.jpeg')";

    
};
let counter = 0;
let stats = [];
let inputValue = null; 

function handleInput() {
    inputValue = document.getElementById('textInput');
    
    let name = getData();
    
    if(counter == 0){
        let numRuns = 0;
        let points = 0;
        let health = 5;
        let attack = 5;
        let defense = 5;
        let speed = 5;
        let skills=["Ram", "-", "-"]; 
    
        stats = [points, health, attack, defense, speed, skills, numRuns];
    
        
        textOutput.innerHTML = 'Ah yes, the infamoussss Gator Pirate ' + response + "."+        
        "<br> Next time you pop around, I'll have a sssshop open for you <br>" + 
        " <br>You don't have any money?" + "<br>..." +  "<br>..."
        + " <br> Well if you find any unobtainium sssshardssss in there, you can buy my waressss with those" +
        "<br> Go on then! Go get me some unobtainium (hit enter to continue)";

        counter = 1;
    };
    

    

}

function getData(){

    response = inputValue.value;
    inputValue.value = "";
    return response;
    
}


let numOfShards = document.getElementById("number-of-shards");
let numOfHealth = document.getElementById("health");
let attackPoints = document.getElementById("number-of-attack");
let deffensePoints= document.getElementById("number-of-deffense");
let speedPoints= document.getElementById("number-of-speed");



