import React, { useState } from "react";
import { APP_STATE } from './states';
import Home from "./components/Home";
import Game from "./components/Game";

const App = () => {
    const [appState, setAppState] = useState<APP_STATE>('home');

    const onNewGame = () => {
        setAppState('game');
    }

    switch (appState) {
        case 'home':
            return <Home onNewGame={onNewGame} />
        case 'game':
            return <Game onQuitGame={() => setAppState('home')} />
    }
    return <div>
        <h1>Test</h1><p>Test</p>
    </div>
};

export default App;