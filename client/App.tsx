import React, { useState } from "react";
import { APP_STATE } from './states';
import Home from "./components/Home";
import Game from "./components/Game";
import Decks from "./components/Decks";

const App = () => {
    const [appState, setAppState] = useState<APP_STATE>('home');

    const onNewGame = () => {
        setAppState('game');
    }

    switch (appState) {
        case 'home':
            return <Home onNewGame={onNewGame} onSelectDeck={() => setAppState('decks')} />
        case 'game':
            return <Game onQuitGame={() => setAppState('home')} />
        case 'decks':
            return <Decks returnToMainMenu={() => setAppState('home')} />
    }
};

export default App;