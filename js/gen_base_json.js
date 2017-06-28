const t = require('./trinkets_scrape');
const fs = require('fs');

const itemIDs = Object.keys(t);

const relevant_itemIDs = itemIDs.filter((itemID) => {
  const itemData = t[itemID];
  return itemData.jsonequip && itemData.jsonequip.reqlevel > 100 && itemData.name_enus;
});

const curated_t = relevant_itemIDs.map((itemID) => {
  const itemData = t[itemID];
  console.log(itemData);
  return {
    id: itemID,
    name: itemData.name_enus,
  };
});

fs.writeFileSync('scraped_trinkets.json', JSON.stringify(curated_t));
