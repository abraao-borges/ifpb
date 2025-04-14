import React, { useState } from "react";

function TicTacToe() {
    const [boxes, setBoxes] = useState(Array(9).fill(null));
    const [turnO, setTurnO] = useState(true);
    const [winner, setWinner] = useState(null);
    const [msg, setMsg] = useState('');
    const [availableBoxes, setAvailableBoxes] = useState([0, 1, 2, 3, 4, 5, 6, 7, 8]);

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

    const handleClick = (index) => {
        if (winner || boxes[index]) return;

        const newBoxes = [...boxes];
        newBoxes[index] = turnO ? 'O' : 'X';
        setBoxes(newBoxes);

        setAvailableBoxes(availableBoxes.filter(i => i !== index));

        if (turnO) {
            setTurnO(false);
        }

        checkWinner(newBoxes);
        if(!checkWinner(newBoxes) && availableBoxes.length > 1) {
            computerMove(newBoxes);
        }
    };

    const computerMove = (currentBoxes) => {
        
    }
}