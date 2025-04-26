import React from "react";

const Decks = ({ returnToMainMenu }: { returnToMainMenu: () => void }) => {
    return <div><button onClick={returnToMainMenu}>Return to main menu</button><h1>Deck Builder</h1></div>
}

export default Decks;