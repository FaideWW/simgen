import os
import sys
import time
import argparse
from itertools import combinations

import apl
import legendaries

temp_path = "temp"
output_path = "result"

start_time = time.time()

def runLegendarySims(ilevel = 920):
    def curriedSettings(settings, path):
        return apl.buildSettings(settings, args.iterations, args.error, output_path + path)

    print("Building profiles...")
    profile_start_time = time.time()
    # Single legendary profiles
    profile_bear_1t_singles = buildProfile(
            ilevel,
            apl.buildBear1TAPL,
            legendaries.bear,
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_bear_singles.txt"))

    profile_cat_1t_singles = buildProfile(
            ilevel,
            apl.buildCat1TAPL,
            legendaries.bear + legendaries.cat,
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_cat_singles.txt"))

    profile_bear_3t_singles = buildProfile(
            ilevel,
            apl.buildBear3TAPL,
            legendaries.bear,
            curriedSettings(apl.SETTINGS_3T, "/" + str(ilevel) + "_3t_singles.txt"))

    profile_bear_5t_incarnup_singles = buildProfile(
            ilevel,
            apl.buildBear5TIncarnUpAPL,
            legendaries.bear,
            curriedSettings(apl.SETTINGS_5T_INCARNUP, "/" + str(ilevel) + "_5t_incarnup_singles.txt"))

    profile_bear_5t_incarndown_singles = buildProfile(
            ilevel,
            apl.buildBear5TIncarnDownAPL,
            legendaries.bear,
            curriedSettings(apl.SETTINGS_5T_INCARNDOWN, "/" + str(ilevel) + "_5t_incarndown_singles.txt"))

    # Paired legendary profiles
    profile_bear_1t_pairs = buildProfile(
            ilevel,
            apl.buildBear1TAPL,
            buildPairs(legendaries.bear),
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_bear_pairs.txt"))

    profile_cat_1t_pairs = buildProfile(
            ilevel,
            apl.buildCat1TAPL,
            buildPairs(legendaries.bear + legendaries.cat),
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_cat_pairs.txt"))

    profile_bear_3t_pairs = buildProfile(
            ilevel,
            apl.buildBear3TAPL,
            buildPairs(legendaries.bear),
            curriedSettings(apl.SETTINGS_3T, "/" + str(ilevel) + "_3t_pairs.txt"))

    profile_bear_5t_incarnup_pairs = buildProfile(
            ilevel,
            apl.buildBear5TIncarnUpAPL,
            buildPairs(legendaries.bear),
            curriedSettings(apl.SETTINGS_5T_INCARNUP, "/" + str(ilevel) + "_5t_incarnup_pairs.txt"))

    profile_bear_5t_incarndown_pairs = buildProfile(
            ilevel,
            apl.buildBear5TIncarnDownAPL,
            buildPairs(legendaries.bear),
            curriedSettings(apl.SETTINGS_5T_INCARNDOWN, "/" + str(ilevel) + "_5t_incarndown_pairs.txt"))



    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(temp_path + "/" + str(ilevel) + "_1t_bear_singles.simc", 'w+') as fp:
        fp.write(profile_bear_1t_singles)
    with open(temp_path + "/" + str(ilevel) + "_1t_cat_singles.simc", 'w+') as fp:
        fp.write(profile_cat_1t_singles)
    with open(temp_path + "/" + str(ilevel) + "_3t_singles.simc", 'w+') as fp:
        fp.write(profile_bear_3t_singles)
    with open(temp_path + "/" + str(ilevel) + "_5t_incarnup_singles.simc", 'w+') as fp:
        fp.write(profile_bear_5t_incarnup_singles)
    with open(temp_path + "/" + str(ilevel) + "_5t_incarndown_singles.simc", 'w+') as fp:
        fp.write(profile_bear_5t_incarndown_singles)

    with open(temp_path + "/" + str(ilevel) + "_1t_bear_pairs.simc", 'w+') as fp:
        fp.write(profile_bear_1t_pairs)
    with open(temp_path + "/" + str(ilevel) + "_1t_cat_pairs.simc", 'w+') as fp:
        fp.write(profile_cat_1t_pairs)
    with open(temp_path + "/" + str(ilevel) + "_3t_pairs.simc", 'w+') as fp:
        fp.write(profile_bear_3t_pairs)
    with open(temp_path + "/" + str(ilevel) + "_5t_incarnup_pairs.simc", 'w+') as fp:
        fp.write(profile_bear_5t_incarnup_pairs)
    with open(temp_path + "/" + str(ilevel) + "_5t_incarndown_pairs.simc", 'w+') as fp:
        fp.write(profile_bear_5t_incarndown_pairs)


    print("Done - Took " + str(time.time() - profile_start_time) + "s")

    if not args.nosim:
        print("Running sims...")
        sim_start_time = time.time()
        # Run simc
        print("=======================")
        print("Simming 1T Bear Singles...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_1t_bear_singles.simc")
        print("=======================")
        print("Simming 1T Cat Singles...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_1t_cat_singles.simc")
        print("=======================")
        print("Simming 3T Bear Singles...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_3t_singles.simc")
        print("=======================")
        print("Simming 5T Bear (Incarnation Up) Singles...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_5t_incarnup_singles.simc")
        print("=======================")
        print("Simming 5T Bear (Incarnation Down) Singles...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_5t_incarndown_singles.simc")

        print("=======================")
        print("Simming 1T Bear Pairs...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_1t_bear_pairs.simc")
        print("=======================")
        print("Simming 1T Cat Pairs...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_1t_cat_pairs.simc")
        print("=======================")
        print("Simming 3T Bear Pairs...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_3t_pairs.simc")
        print("=======================")
        print("Simming 5T Bear (Incarnation Up) Pairs...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_5t_incarnup_pairs.simc")
        print("=======================")
        print("Simming 5T Bear (Incarnation Down) Pairs...");
        print("=======================")
        os.system(args.path_to_simc + " " + temp_path + "/" + str(ilevel) + "_5t_incarndown_pairs.simc")

        print("Done - Took " + str(time.time() - sim_start_time) + "s")

# def buildProfile(ilevel, targets, apl_template, talents, settings):
def buildProfile(ilevel, apl_builder, copy_source, settings):
    char_gear = apl.buildGearList(
            stat_template = apl.getStatTemplate(ilevel),
            weapon_ilevel = apl.getWeaponLevel(ilevel))

    gear_reset = apl.buildGearReset(ilevel)

    action_list = apl_builder()
    # action_list = apl.buildAPL(
    #         apl_template = apl_template,
    #         talents = talents)

    copy_data = {
            "gear_reset": gear_reset,
            "apl_builder": apl_builder }

    def copy_constructor(d): return buildCopyFromData(**copy_data, **d)
    copies = map(copy_constructor, copy_source)

    return apl.buildProfile(
            sim_settings = settings,
            char_gear = char_gear,
            action_list = action_list,
            copy_constructors = '\n'.join(copies))


# def buildCopyFromData(target_count, gear_reset, apl_reset, name, line, isTrinket, isRNT, isProcSephuz, isBear = True):
def buildCopyFromData(gear_reset, apl_builder, name, line, isTrinket = 0, isProcSephuz = False, talents_override = None):
    apl_override = apl_builder(
            talents = talents_override,
            proc_sephuz = isProcSephuz,
            use_trinket = isTrinket)
    # if target_count == 1 and isRNT and isBear:
    #     apl_override = apl.buildAPL(
    #         apl_template = apl.BEAR_1T_PULVERIZE_APL, talents = apl.BEAR_1T_RNT_TALENTS)
    return apl.buildCopy(
            copy_name = name,
            gear_reset = gear_reset,
            gear_override = line,
            apl_override = apl_override)

def buildPairs(list):
    def mergePair(p):
        first = p[0]
        second = p[1]
        return {
                "name": first.get("name") + "+" + second.get("name"),
                "line": first.get("line") + "\n" + second.get("line"),
                "isProcSephuz": first.get("isProcSephuz") or second.get("isProcSephuz"),
                "isTrinket": first.get("isTrinket", 0) + second.get("isTrinket", 0),
                "talents_override": first.get("talents_override") or second.get("talents_override")
                }
    pairs = [pair for pair in combinations(list, 2)]
    return map(mergePair, pairs)

parser = argparse.ArgumentParser()
parser.add_argument("type", help="Either 'legendary' or 'trinket'")
parser.add_argument("ilevel", help="Either '920' or '900'", type=int)
parser.add_argument("path_to_simc", help="Path to the simc CLI binary")
parser.add_argument("-i", "--iterations", help="Override the amount of iterations", type=int, default=10000)
parser.add_argument("-e", "--error", help="Override the target_error", type=float, default=0.05)
parser.add_argument("--nosim", help="Override the target_error", action="store_true")

args = parser.parse_args()

sim_type = args.type
ilevel = args.ilevel

if sim_type == 'legendary':
    print("Running legendary sims...")
    if ilevel != 920 and ilevel != 900:
        print("Unsupported item level")
        sys.exit()
    runLegendarySims(ilevel)


elif sim_type =='trinket':
    print("Running trinket sims...")
    print("[Not implemented yet]")
else:
    print("Unsupported sim type")
