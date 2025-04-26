import React from "react";

const Game = ({ onQuitGame }: { onQuitGame: () => void }) => {
    const checkQuitGame = () => {
        const reallyQuit = window.confirm('Really quit?')
        if (reallyQuit) {
            onQuitGame();
        }
    }

    return <div>
        <button onClick={checkQuitGame}>Quit</button>
        <h1>Game</h1>
    </div>
}

export default Game;