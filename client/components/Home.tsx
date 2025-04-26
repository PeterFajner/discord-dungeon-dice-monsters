import React, { CSSProperties } from "react";
import { APP_STATE } from "../states";

const Home = ({ onNewGame }: { onNewGame: () => void }) => {
    return <div>
        <h1>Main Menu</h1>
        <div><button onClick={() => onNewGame()}>New game</button></div>
    </div>
}

export default Home;