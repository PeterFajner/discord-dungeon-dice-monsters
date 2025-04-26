import cardJson from '../../assets/all_cards.json';

type Crest = keyof typeof cardJson.image_urls.crest;
type CardType = keyof typeof cardJson.image_urls.type;
type Movement = keyof typeof cardJson.image_urls.movement;

// type AllCardsJSON = {
//     cards: {
//         name: string;
//         properties: Card;
//     }[],
//     image_urls: {
//         crest: {
//             [key: string]: string;
//         };
//         type: {
//             [key: string]: string;
//         };
//         movement: {
//             [key: string]: string;
//         };
//     };
// };

type Card = {
    name: string;
    img_url: string;
    japanese: string;
    romaji?: string;
    type: CardType;
    movement?: Movement;
    level: number;
    hp?: number;
    atk?: number;
    defense?: number;
    number: string;
    crests: Crest[];
};

const loadCards = (): Card[] => {
    return cardJson.cards.map(card => ({
        ...card.properties,
        type: card.properties.type as CardType,
        crests: card.properties.crests as Crest[],
        movement: card.properties.movement as (Movement | undefined),
    }));
};