<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GachaSim</title>
    <style>
        body {
            font-family: "Comic Sans MS", sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        canvas {
            display: block;
            position: absolute;
            top: 0;
            left: 0;
        }
        .button-container {
            position: absolute;
            bottom: 100px;
            width: 100%;
            text-align: center;
        }
        .button-container button {
            font-size: 14px;
            margin: 10px;
            padding: 10px 20px;
            background-color: white;
            color: #047DA1;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        .header-text {
            text-align: center;
            color: #1DEAEA;
            font-size: 20px;
        }
        #timer {
            color: black;
            font-size: 20px;
        }
        .error {
            color: red;
            font-size: 25px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<canvas id="gachaCanvas"></canvas>

<div class="button-container">
    <button id="roll1Btn">1 Pull</button>
    <button id="roll10Btn">10 Pull</button>
    <button id="historyBtn">History</button>
    <button id="rulesBtn">Rules</button>
    <button id="quitBtn">Quit</button>
    <button id="mainMenuBtn">Main Menu</button>
    <button id="startBtn">Start</button>
</div>

<script>
    const canvas = document.getElementById('gachaCanvas');
    const ctx = canvas.getContext('2d');

    let width = window.innerWidth;
    let height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;

    let wishes = 100;
    let time = 1200;
    let show = false;
    let stopAnimation = false;

    const charNames = {
        1: "Sienna Ines",
        2: "Raziel Sera",
        3: "Styx Ferryman",
        4: "Lost Sea of Polaris",
        5: "Hydra of Lerna",
        6: "Seraphim's Tome",
        7: "Beacon of Splendor",
        8: "Whiplash",
        9: "Swordfish",
        10: "Cerulean",
        11: "Charybdis"
    };

    // Event Listeners for Buttons
    document.getElementById('startBtn').addEventListener('click', startGame);
    document.getElementById('roll1Btn').addEventListener('click', rollOne);
    document.getElementById('roll10Btn').addEventListener('click', rollTen);
    document.getElementById('historyBtn').addEventListener('click', displayHistory);
    document.getElementById('rulesBtn').addEventListener('click', showRules);
    document.getElementById('quitBtn').addEventListener('click', quit);
    document.getElementById('mainMenuBtn').addEventListener('click', mainMenu);

    function startGame() {
        clearCanvas();
        ctx.fillStyle = "black";
        ctx.font = "25px Comic Sans MS";
        ctx.fillText("You will have 100 wishes and 20 minutes to get a character", width / 2 - 200, height / 2);
        document.getElementById('startBtn').style.display = 'none'; // Hide the start button
    }

    function rollOne() {
        if (wishes <= 0 || time <= 0) {
            showError("Can't wish anymore.");
            return;
        }
        // Logic for rolling 1 wish
        wishes -= 1;
        // Do animation and character generation here
    }

    function rollTen() {
        if (wishes <= 0 || time <= 0) {
            showError("Can't wish anymore.");
            return;
        }
        // Logic for rolling 10 wishes
        wishes -= 10;
        // Do animation and character generation here
    }

    function showError(message) {
        clearCanvas();
        ctx.fillStyle = "red";
        ctx.font = "30px Comic Sans MS";
        ctx.fillText(message, width / 2 - 100, height / 2);
        setTimeout(clearCanvas, 3000);  // Clear after 3 seconds
    }

    function displayHistory() {
        clearCanvas();
        ctx.fillStyle = "black";
        ctx.font = "25px Comic Sans MS";
        ctx.fillText("Character History:", width / 2 - 100, height / 4);

        // Show character history (you can replace this with dynamic data)
        let yPosition = height / 3;
        for (let i = 1; i <= 11; i++) {
            ctx.fillText(`${charNames[i]}: 0`, width / 2 - 100, yPosition);
            yPosition += 30;
        }
    }

    function showRules() {
        clearCanvas();
        ctx.fillStyle = "black";
        ctx.font = "25px Comic Sans MS";
        ctx.fillText("Rate Rules and Details:", width / 2 - 100, height / 5);

        // Display rules (example text)
        let yPosition = height / 4 + 40;
        ctx.fillText("5☆ character rate: 2%", width / 2 - 100, yPosition);
        ctx.fillText("4☆ character rate: 10%", width / 2 - 100, yPosition + 30);
        ctx.fillText("3☆ weapon rate: 38%", width / 2 - 100, yPosition + 60);
        ctx.fillText("2☆ weapon rate: 50%", width / 2 - 100, yPosition + 90);
    }

    function quit() {
        window.close();  // Close the window
    }

    function mainMenu() {
        // Logic for main menu screen
    }

    function clearCanvas() {
        ctx.clearRect(0, 0, width, height);  // Clears the canvas
    }

    // Timer logic
    function updateTime() {
        if (time <= 0) return;
        time -= 1;
        setTimeout(updateTime, 1000); // Update every second

        // Display time on screen
        ctx.clearRect(width / 2 - 100, 50, 200, 40);
        ctx.fillText("Time: " + Math.floor(time / 60) + "m " + (time % 60) + "s", width / 2 - 100, 50);
    }
</script>

</body>
</html>
