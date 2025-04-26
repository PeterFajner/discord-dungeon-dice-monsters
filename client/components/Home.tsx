import React, { CSSProperties } from "react";
import { APP_STATE } from "../states";

const Home = ({ onNewGame, onSelectDeck }: { onNewGame: () => void, onSelectDeck: () => void }) => {
    return <div>
        <h1>Main Menu</h1>
        <div><button onClick={() => onNewGame()}>New game</button> <button onClick={() => onSelectDeck()}>Select deck</button></div>
    </div>
}

export default Home;