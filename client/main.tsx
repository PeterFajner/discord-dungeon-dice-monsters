import React from "react";
import "./style.css";
// import { DiscordSDK } from "@discord/embedded-app-sdk";
import { createRoot } from 'react-dom/client';
import App from "./App";

// const discordSdk = new DiscordSDK(import.meta.env.VITE_DISCORD_CLIENT_ID);

// setupDiscordSdk().then(() => {
//   console.log("Discord SDK is ready");
// });



// Clear the existing HTML and render React
document.body.innerHTML = '<div id="app"></div>';
const app = document.getElementById("app");
if (app) {
  const root = createRoot(app);
  root.render(<App />)
}

