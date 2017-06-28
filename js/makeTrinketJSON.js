const fs = require('fs');

const specialTrinkets = {
  137349: {
    fury: true,
    action: ['rancid_maw'],
  },
  137439: {
    fury: true,
    action: ['fetid_regurgitation'],
  },
  138224: {
    fury: true,
    action: ['volatile_ichor'],
  },
  139321: {
    fury: true,
    action: ['plague_swarm'],
  },
  140794: {
    fury: true,
    action: ['arcane_swipe'],
  },
  147017: {
    fury: true,
    action: ['spectral_blast', 'spectral_owl'],
  },
  147016: {
    fury: true,
    action: ['terror_from_below'],
  },
  147012: {
    fury: true,
    action: ['umbral_glaive_storm', 'shattering_umbral_glaives'],
  },
  121808: {
    fury: true,
    action: ['nether_energy'],
  },
  141585: {
    fury: true,
    action: ['wind_bolt'],
  },
  140030: {
    fury: true,
    action: ['devilsaur_shock_leash'],
  },
  142160: {
    fury: true,
    action: ['thunder_ritual_damage'],
  },
  142165: {
    fury: true,
    action: ['volatile_energy'],
  },
};

const trinketsToIgnore = {
  121808: true, // Nether Conductors - Not implemented
};

let trinketData = {};

function makeBucket(bucketid, bucketname) {
  if (!trinketData[bucketid]) trinketData[bucketid] = {
    name: bucketname,
    baselineDPS: 0,
    trinkets: {},
  };
}

function parseFile(bucketid, file, filename, deleteExisting = false) {
  console.log('Parsing file:', filename);
  const t = trinketData[bucketid].trinkets;
  const lines = fs.readFileSync(readFrom + '/' + filename).toString().split('\n');
  const dpsHeaderPattern = /DPS Ranking/;
  const hpsHeaderPattern = /HPS Ranking/;
  const raidHeader = /\d+ 100.0%  Raid/;
  const trinketDPSPattern = /\s*(\d+)\s+\d+\.\d+\%\s+(\d+)_(.*) \((\d+)\)/;
  const dpsBreakdownPattern = /\s+([a-z_]+).*pDPS=\s*(\d+).*/;
  const baselinePattern = / (\d+).+Baseline/;
  let trinketsReplaced = 0;
  let trinketsCreated = 0;
  // const playerBlockHeaderPattern = /Player: (\d+)_(.*) tauren druid guardian 110$/;

  let dpsBlockStarted = false;
  let dpsBlockEnded = false;

  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i];
    if (!dpsBlockStarted) {
      if (line.match(dpsHeaderPattern)) {
        console.log('DPS Block started');
        dpsBlockStarted = true;
      } else {
        continue;
      }
    }

    if (!dpsBlockEnded) {
      if (line.length === 0) {
        dpsBlockEnded = true;
        console.log('Finished finding trinkets');
        break;
      }

      const baselineLine = line.match(baselinePattern);
      if (baselineLine) {
        console.log(`Baseline DPS - ${baselineLine[1]}`);
        const baselineDPS = Number(baselineLine[1]);
        if (trinketData[bucketid].baselineDPS === 0 || trinketData[bucketid].baselineDPS > baselineDPS) {
          trinketData[bucketid].baselineDPS = baselineDPS;
        }
      }

      if (line.match(hpsHeaderPattern)) {
        console.log('DPS Block ended');
        dpsBlockEnded = true;
      }

      const dpsLine = line.match(trinketDPSPattern);
      console.log()
      if (dpsLine) {
        const [fullLine, dps, id, name, ilevel] = dpsLine;
        if (trinketsToIgnore[id]) {
          console.log(`${name} is on the ignore list - skipping`);
          continue;
        }
        if (!t[name] || deleteExisting) {
          t[name] = {
            name,
            id,
            results: {},
          };
        }

        if (t[name].results[ilevel]) {
          console.log(`Updating ${name}-${ilevel} - old value: ${t[name].results[ilevel]} - new value: ${dps}`);
          trinketsReplaced += 1;
        } else {
          console.log(`Creating new entry for ${name}-${ilevel}`);
          trinketsCreated += 1;
        }


        console.log(`DPS: ${name} (${ilevel}) = ${dps} [${fullLine}]`);
        t[name].results[ilevel] = Number(dps);
        if (specialTrinkets[id]) {
          console.log(`Trinket is modified by fury of nature, look for the pDPS`);
          const adjustedName = `${name} (cloak)`;
          let adjustedDPS = dps;
          let playerBlockFound = false;
          let actionsBlockFound = false;
          let actionFound = false;

          if (!t[adjustedName] || deleteExisting) {
            t[adjustedName] = {
              name: adjustedName,
              cloak: true,
              id,
              results: {},
            };
          }

          if (t[adjustedName].results[ilevel]) {
            console.log(`Updating ${adjustedName}-${ilevel} - old value: ${t[adjustedName].results[ilevel]} - new value: ${dps}`);
            trinketsReplaced += 1;
          } else {
            console.log(`Creating new entry for ${adjustedName}-${ilevel}`);
            trinketsCreated += 1;
          }

          for (let j = i; j < lines.length; j += 1) {
            const line2 = lines[j];

            if (!playerBlockFound) {
              if (!line2.includes(`Player: ${id}_${name} (${ilevel})`)) continue;
              console.log('Found player breakdown')
              playerBlockFound = true;
            } else if (!actionsBlockFound) {
              if (!line2.includes('Actions:')) continue;
              console.log('Found Actions block')
              actionsBlockFound = true;
            } else {
              if (line2.includes('Constant Buffs:')) {
                console.log('Out of actions: terminating');
                break;
              }
              const action = line2.match(dpsBreakdownPattern);
              if (!action) {
                console.log(`Line does not match: [${line2}]`);
                continue;
              }
              const [fullLine2, actionName, pDPS] = action;
              if (specialTrinkets[id].action.includes(actionName)) {
                actionFound = true;
                adjustedDPS = Number(adjustedDPS) + (Number(pDPS) * 0.3);
                console.log(`Modifying action ${actionName} by 1.3 - old DPS: ${dps} - new DPS: ${adjustedDPS}`);
                break;
              }
            }
          }

          if (!actionFound) throw new Error('No action found');
          console.log(`DPS: ${name} (${ilevel}) = ${adjustedDPS} [${fullLine}]`);
          t[adjustedName].results[ilevel] = Number(adjustedDPS);
        }
      }
    } else if (line.match(baselinePattern)) {
      dpsBlockEnded = true;
      console.log('Finished finding trinkets');
    }
  }
  console.log(`File finished: created ${trinketsCreated}, replaced ${trinketsReplaced}`);

  return {
    created: trinketsCreated,
    replaced: trinketsReplaced,
  };
}

makeBucket('900_1t_bear', '1T Bear (900)');
makeBucket('900_3t_bear', '3T Bear (900)');
makeBucket('900_5t_incarnup', '5T Bear, Incarnation Up (900)');
makeBucket('900_5t_incarndown', '5T Bear, Incarnation Down (900)');

makeBucket('920_1t_bear', '1T Bear (920)');
makeBucket('920_3t_bear', '3T Bear (920)');
makeBucket('920_5t_incarnup', '5T Bear, Incarnation Up (920)');
makeBucket('920_5t_incarndown', '5T Bear, Incarnation Down (920)');

makeBucket('940_1t_bear', '1T Bear (940)');
makeBucket('940_3t_bear', '3T Bear (940)');
makeBucket('940_5t_incarnup', '5T Bear, Incarnation Up (940)');
makeBucket('940_5t_incarndown', '5T Bear, Incarnation Down (940)');


const readFrom = './result';
const writeTo = './trinket_data.json';
const validFilePrefixes = [
  '940_1t_bear',
  '940_3t_bear',
  // '940_3t_moon', // waiting until completion
  '940_5t_incarnup',
  '940_5t_incarndown',
  '920_1t_bear',
  '920_3t_bear',
  // '920_3t_moon',
  '920_5t_incarnup',
  '920_5t_incarndown',
  '900_1t_bear',
  '900_3t_bear',
  // '900_3t_moon',
  '900_5t_incarnup',
  '900_5t_incarndown',
];

console.log('existing: ', trinketData);

let trinketsCreated = 0;
let trinketsReplaced = 0;

if (process.argv.length < 3) {
  throw new Error('No manifest specificed');
}

const manifestPath = process.argv[2];
const deleteExisting = process.argv.includes('--delete-existing');

console.log('Deleting existing trinket entries:', deleteExisting);

const manifestPattern = /manifest_(.*).json/;
let manifestHash = null;
const manifestMatch = manifestPath.match(manifestPattern);
if (manifestMatch) {
  manifestHash = manifestMatch[1];
}

const manifestContents = JSON.parse(fs.readFileSync(manifestPath));
const files = manifestContents.sim_results;

if (fs.existsSync(writeTo)) {
  trinketData = JSON.parse(fs.readFileSync(writeTo));
}

console.log(files);
console.log('files:', files.length);

const pattern = /(.*)_trinkets_(.*)_(\d+).txt/;
files.forEach((file) => {
  const match = file.match(pattern);
  if (match !== null) {
    if (validFilePrefixes.includes(match[1])) {
      const fileResults = parseFile(match[1], match[2], match[0], deleteExisting);
      trinketsCreated += fileResults.created;
      trinketsReplaced += fileResults.replaced;
    }
  }
});

console.log(`Finished: Trinkets created: ${trinketsCreated} - Trinkets replaced: ${trinketsReplaced}`);

fs.writeFileSync(writeTo, JSON.stringify(trinketData));
console.log(`Wrote to file ${writeTo}`);
