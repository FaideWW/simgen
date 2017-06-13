trinkets = {
        "manual": [
            {"name": "Stat stick (Crit)", "id": 134203, "bonusID": 603 },
            {"name": "Stat stick (Haste)", "id": 134203, "bonusID": 604 },
            {"name": "Stat stick (Mastery)", "id": 134203, "bonusID": 605 },
            {"name": "Stat stick (Versatility)", "id": 134203, "bonusID": 607 },
            {"name": "Stat stick (No secondary)", "id": 140806 }
            ],

        "crafted": [
            {"id":128705,"name":"Darkmoon Deck: Dominion", "ilevel": 875},
            ],

        "dungeons": [
            # Maw of Souls
            {"id":133641,"name":"Eye of Skovald"},
            {"id":133644,"name":"Memento of Angerboda"},
            {"id":137329,"name":"Figurehead of the Naglfar"},
            # Black Rook Hold
            {"id":136715,"name":"Spiked Counterweight"},
            {"id":136716,"name":"Caged Horror"},
            # Darkheart Thicket
            {"id":137306,"name":"Oakheart's Gnarled Root"},
            {"id":137312,"name":"Nightmare Egg Shell"},
            # Neltharion's Lair
            {"id":137349,"name":"Naraxas' Spiked Tongue"},
            {"id":137357,"name":"Mark of Dargrul"},
            # Eye of Azshara
            {"id":137367,"name":"Stormsinger Fulmination Charge"},
            {"id":137369,"name":"Giant Ornamental Pearl"},
            {"id":137373,"name":"Tempered Egg of Serpentrix"},
            # Arcway
            {"id":137406,"name":"Terrorbound Nexus"},
            {"id":137419,"name":"Chrono Shard"},
            # Violet Hold
            {"id":137433,"name":"Obelisk of the Void"},
            {"id":137439,"name":"Tiny Oozeling in a Jar"},
            {"id":137446,"name":"Elementium Bomb Squirrel Generator"},
            {"id":137459,"name":"Chaos Talisman"},
            # Court of Stars
            {"id":137486,"name":"Windscar Whetstone"},
            # Vault of the Wardens
            {"id":137537,"name":"Tirathon's Betrayal"},
            {"id":137539,"name":"Faulty Countermeasure"},
            {"id":137541,"name":"Moonlit Prism"},
            # Karazhan
            {"id":142166,"name":"Ethereal Urn"},
            # Halls of Valor
            {"id":133642,"name":"Horn of Valor"},
            ],

        "raid":[
                # Emerald Nightmare
                {"id":138224,"name":"Unstable Horrorslime"},
                {"id":139320,"name":"Ravaged Seed Pod"},
                {"id":139321,"name":"Swarming Plaguehive"},
                {"id":139323,"name":"Twisting Wind"},
                {"id":139325,"name":"Spontaneous Appendages"},
                {"id":139329,"name":"Bloodthirsty Instinct"},
                {"id":139334,"name":"Nature's Call"},
                {"id":139326,"name":"Wriggling Sinew"},
                {"id":139324,"name":"Goblet of Nightmarish Ichor"},
                {"id":139336,"name":"Bough of Corruption"},
                # Trial of Valor
                {"id":142506,"name":"Eye of Guarm"},
                # Nighthold
                {"id":140794,"name":"Arcanogolem Digit"},
                {"id":140796,"name":"Entwined Elemental Foci"},
                {"id":140798,"name":"Icon of Rot"},
                {"id":140801,"name":"Fury of the Burning Sky"},
                {"id":140802,"name":"Nightblooming Frond"},
                # {"id":140806,"name":"Convergence of Fates"},
                {"id":140808,"name":"Draught of Souls"},
                ],

        "world":[
                {"id":121808,"name":"Nether Conductors"},
                {"id":140026,"name":"The Devilsaur's Bite"},
                {"id":140027,"name":"Ley Spark"},
                {"id":141537,"name":"Thrice-Accursed Compass"},
                {"id":141585,"name":"Six-Feather Fan"},
                {"id":140030,"name":"Devilsaur Shock-Baton"},
                ],

        "pvp":[
                {"id":135691,"name":"Vindictive Gladiator's Badge of Conquest"},
                {"id":135692,"name":"Vindictive Gladiator's Accolade of Conquest"},
                {"id":135693,"name":"Vindictive Gladiator's Insignia of Conquest"},
                {"id":142660,"name":"Fearless Gladiator's Badge of Conquest"},
                {"id":142661,"name":"Fearless Gladiator's Accolade of Conquest"},
                {"id":142662,"name":"Fearless Gladiator's Insignia of Conquest"},
                ],

        "legendary": [
                {"id":144259,"name":"Kil'jaeden's Burning Wish", "ilevel":940},
                {"id":144249,"name":"Archimonde's Hatred Reborn", "ilevel":940}
                ],

        "karazhan": [
                {"id":142157,"name":"Aran's Relaxing Ruby"},
                {"id":142159,"name":"Bloodstained Handkerchief"},
                {"id":142160,"name":"Mrrgria's Favor"},
                {"id":142164,"name":"Toe Knee's Promise"},
                {"id":142165,"name":"Deteriorated Construct Core"},
                {"id":142167,"name":"Eye of Command"},

                {"id":142157,"name":"Aran's Relaxing Ruby (Chest)", "gear_override":"chest=,id=142203,stats=0agi_0crit_0vers"},
                {"id":142159,"name":"Bloodstained Handkerchief (Chest)", "gear_override":"chest=,id=142203,stats=0agi_0crit_0vers"},
                {"id":142160,"name":"Mrrgria's Favor (Chest)", "gear_override":"chest=,id=142203,stats=0agi_0crit_0vers"},
                {"id":142164,"name":"Toe Knee's Promise (Chest)", "gear_override":"chest=,id=142203,stats=0agi_0crit_0vers"},
                {"id":142165,"name":"Deteriorated Construct Core (Chest)", "gear_override":"chest=,id=142203,stats=0agi_0crit_0vers"},
                {"id":142167,"name":"Eye of Command (Chest)", "gear_override":"chest=,id=142203,stats=0agi_0crit_0vers"},
                ]
        }


every = trinkets["manual"] + trinkets["crafted"] + trinkets["dungeons"] + trinkets["raid"] + trinkets["world"] + trinkets["pvp"] + trinkets["legendary"] + trinkets["karazhan"]

trinkets["every"] = every
min_ilevel = 865
max_ilevel = 925
