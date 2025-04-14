let boxes = document.querySelectorAll('.box');
let resetBtn = document.querySelector('#reset');
let turnO = true; // Player 0 starts
let newGameBtn = document.querySelector('#new-btn');
let msgContainer = document.querySelector('.msg-container');
let availableBoxes = [0, 1, 2, 3, 4, 5, 6, 7, 8];

const winPatterns = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8]
];

boxes.forEach((box, index) => {
    box.addEventListener('click', function() {
        if (turnO) {
            box.innerText = 'O';
            box.style.color = 'green';
            turnO = false;
            box.disabled = true;

            // Remove the box index from availableBoxes
            availableBoxes = availableBoxes.filter(i => i !== index);

            checkWinner();
            if(!checkWinner() && availableBoxes.length>0){
                computerMove();
            }
        }
    });
});

const computerMove = () => {
    if (availableBoxes.length > 0) {
        let randomIndex = Math.floor(Math.random() * availableBoxes.length);
        let computerIndex = availableBoxes[randomIndex];
        let computerBox = boxes[computerIndex];

        computerBox.innerText = 'X';
        computerBox.style.color = 'black';
        computerBox.disabled = true;
        turnO = true;

        availableBoxes = availableBoxes.filter(i => i !== computerIndex);
        checkWinner();
    }
};

const enableBoxes = () => {
    for (let box of boxes) {
        box.disabled = false;
        box.innerText = "";
    }
};

const disableBoxes = () => {
    for (let box of boxes) {
        box.disabled = true;
    }
};

const showWinner = (winner) => {
    msgContainer.classList.remove('hide');
    msg.innerText = `Congratulations, Winner is ${winner}`;
    disableBoxes();
};

const checkWinner = () => {
    let hasWin = false;
    for (let pattern of winPatterns) {
        let pos1Val = boxes[pattern[0]].innerText;
        let pos2Val = boxes[pattern[1]].innerText;
        let pos3Val = boxes[pattern[2]].innerText;

        if (pos1Val !== "" && pos2Val !== "" && pos3Val !== "" && pos1Val === pos2Val && pos2Val === pos3Val) {
            showWinner(pos1Val);
            hasWin = true;
            return true;
        }
    }

    if (!hasWin) {
        const allBoxes = [...boxes].every((box) => box.innerText !== "");
        if (allBoxes) {
            msgContainer.classList.remove('hide');
            msg.innerText = "Match Drawn";
            return true;
        }else{
            return false;
        }
    }
    return false;
}

const resetGame = () => {
    turnO = true;
    enableBoxes();
    msgContainer.classList.add('hide');
    availableBoxes = [0, 1, 2, 3, 4, 5, 6, 7, 8]; // Reset available boxes
};

newGameBtn.addEventListener('click', resetGame);
resetBtn.addEventListener('click', resetGame);