import os
import sys
import time
import argparse
from math import inf
from string import Template
from itertools import combinations

import apl
import legendaries
import trinkets

temp_path = "temp"
output_path = "result"

start_time = time.time()

def runLegendarySims(ilevel = 920):
    def curriedSettings(settings, path):
        return apl.buildSettings(settings, args.iterations, args.error, output_path + path)

    print("Building profiles...")
    profile_start_time = time.time()
    # Single legendary profiles
    profile_bear_1t_singles = buildLegendaryProfile(
            ilevel,
            apl.buildBear1TAPL,
            legendaries.bear,
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_bear_singles.txt"))

    profile_cat_1t_singles = buildLegendaryProfile(
            ilevel,
            apl.buildCat1TAPL,
            legendaries.bear + legendaries.cat,
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_cat_singles.txt"))

    profile_bear_3t_singles = buildLegendaryProfile(
            ilevel,
            apl.buildBear3TAPL,
            legendaries.bear,
            curriedSettings(apl.SETTINGS_3T, "/" + str(ilevel) + "_3t_singles.txt"))

    profile_bear_5t_incarnup_singles = buildLegendaryProfile(
            ilevel,
            apl.buildBear5TIncarnUpAPL,
            legendaries.bear,
            curriedSettings(apl.SETTINGS_5T_INCARNUP, "/" + str(ilevel) + "_5t_incarnup_singles.txt"))

    profile_bear_5t_incarndown_singles = buildLegendaryProfile(
            ilevel,
            apl.buildBear5TIncarnDownAPL,
            legendaries.bear,
            curriedSettings(apl.SETTINGS_5T_INCARNDOWN, "/" + str(ilevel) + "_5t_incarndown_singles.txt"))

    # Paired legendary profiles
    profile_bear_1t_pairs = buildLegendaryProfile(
            ilevel,
            apl.buildBear1TAPL,
            buildPairs(legendaries.bear),
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_bear_pairs.txt"))

    profile_cat_1t_pairs = buildLegendaryProfile(
            ilevel,
            apl.buildCat1TAPL,
            buildPairs(legendaries.bear + legendaries.cat),
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_cat_pairs.txt"))

    profile_bear_3t_pairs = buildLegendaryProfile(
            ilevel,
            apl.buildBear3TAPL,
            buildPairs(legendaries.bear),
            curriedSettings(apl.SETTINGS_3T, "/" + str(ilevel) + "_3t_pairs.txt"))

    profile_bear_5t_incarnup_pairs = buildLegendaryProfile(
            ilevel,
            apl.buildBear5TIncarnUpAPL,
            buildPairs(legendaries.bear),
            curriedSettings(apl.SETTINGS_5T_INCARNUP, "/" + str(ilevel) + "_5t_incarnup_pairs.txt"))

    profile_bear_5t_incarndown_pairs = buildLegendaryProfile(
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

# def buildLegendaryProfile(ilevel, targets, apl_template, talents, settings):
def buildLegendaryProfile(ilevel, apl_builder, copy_source, settings):
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

    def copy_constructor(d): return buildLegendaryCopyFromData(**copy_data, **d)
    copies = map(copy_constructor, copy_source)

    return apl.buildProfile(
            sim_settings = settings,
            char_gear = char_gear,
            action_list = action_list,
            copy_constructors = '\n'.join(copies))


# def buildLegendaryCopyFromData(target_count, gear_reset, apl_reset, name, line, isTrinket, isRNT, isProcSephuz, isBear = True):
def buildLegendaryCopyFromData(gear_reset, apl_builder, name, line, isTrinket = 0, isProcSephuz = False, talents_override = None):
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

def buildPairs(l):
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
    pairs = [pair for pair in combinations(l, 2)]
    return list(map(mergePair, pairs)) + legendaries.unique_pairs


def runTrinketSims(ilevel = 920):
    def curriedSettings(settings, path):
        return apl.buildSettings(settings, args.iterations, args.error, output_path + path)
    
    groups = args.group.split(",")
    if not all([x in trinkets.trinkets for x in groups]):
        raise KeyError("Group "+args.group+" not found in trinkets")

    trinket_count = sum([len(trinkets.trinkets[g]) for g in groups])
    print("Simming trinket groups: "+args.group+" ("+str(trinket_count)+" trinkets)")
    print("Building profiles...")
    profile_start_time = time.time()
    
    profiles_bear_1t = buildTrinketProfiles(
            ilevel,
            apl.buildBear1TAPL,
            args.chunk,
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_bear_trinkets"))

    profiles_cat_1t = buildTrinketProfiles(
            ilevel,
            apl.buildCat1TAPL,
            args.chunk,
            curriedSettings(apl.SETTINGS_1T, "/" + str(ilevel) + "_1t_cat_trinkets"))

    profiles_bear_3t = buildTrinketProfiles(
            ilevel,
            apl.buildBear3TAPL,
            args.chunk,
            curriedSettings(apl.SETTINGS_3T, "/" + str(ilevel) + "_3t_trinkets"))

    profiles_bear_5t_incarnup = buildTrinketProfiles(
            ilevel,
            apl.buildBear5TIncarnUpAPL,
            args.chunk,
            curriedSettings(apl.SETTINGS_5T_INCARNUP, "/" + str(ilevel) + "_5t_incarnup_trinkets"))

    profiles_bear_5t_incarndown = buildTrinketProfiles(
            ilevel,
            apl.buildBear5TIncarnDownAPL,
            args.chunk,
            curriedSettings(apl.SETTINGS_5T_INCARNDOWN, "/" + str(ilevel) + "_5t_incarndown_trinkets"))

    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if args.profile == "all" or args.profile == "1t_bear":
        for idx, profile in enumerate(profiles_bear_1t):
            with open(temp_path + "/" + str(ilevel) + "_1t_bear_trinkets_" + str(idx) + ".simc", 'w+') as fp:
                fp.write(profile)

    if args.profile == "all" or args.profile == "1t_cat":
        for idx, profile in enumerate(profiles_cat_1t):
            with open(temp_path + "/" + str(ilevel) + "_1t_cat_trinkets_" + str(idx) + ".simc", 'w+') as fp:
                fp.write(profile)

    if args.profile == "all" or args.profile == "3t":
        for idx, profile in enumerate(profiles_bear_3t):
            with open(temp_path + "/" + str(ilevel) + "_3t_trinkets_" + str(idx) + ".simc", 'w+') as fp:
                fp.write(profile)

    if args.profile == "all" or args.profile == "5t_incarnup":
        for idx, profile in enumerate(profiles_bear_5t_incarnup):
            with open(temp_path + "/" + str(ilevel) + "_5t_incarnup_trinkets_" + str(idx) + ".simc", 'w+') as fp:
                fp.write(profile)

    if args.profile == "all" or args.profile == "5t_incarndown":
        for idx, profile in enumerate(profiles_bear_5t_incarndown):
            with open(temp_path + "/" + str(ilevel) + "_5t_incarndown_trinkets_" + str(idx) + ".simc", 'w+') as fp:
                fp.write(profile)

    print("Done - Took " + str(time.time() - profile_start_time) + "s")

    if not args.nosim:
        print("Running sims...")
        sim_start_time = time.time()
        # Run simc
        if args.profile == "all" or args.profile == "1t_bear":
            print("=======================")
            print("Simming 1T Bear Trinkets...");
            print("=======================")
            numChunks = len(profiles_bear_1t) + 1
            for idx, profile in enumerate(profiles_bear_1t):
                print("Chunk " + str(idx + 1) + " of " + str(numChunks))
                filepath = str(ilevel) + "_1t_bear_trinkets_" + str(idx)
                os.system(args.path_to_simc + " " + temp_path + "/" + filepath + ".simc output=" + output_path + "/" + filepath + ".txt")

        if args.profile == "all" or args.profile == "1t_cat":
            print("=======================")
            print("Simming 1T Cat Trinkets...");
            print("=======================")
            numChunks = len(profiles_cat_1t) + 1
            for idx, profile in enumerate(profiles_cat_1t):
                print("Chunk " + str(idx + 1) + " of " + str(numChunks))
                filepath = str(ilevel) + "_1t_cat_trinkets_" + str(idx)
                os.system(args.path_to_simc + " " + temp_path + "/" + filepath + ".simc output=" + output_path + "/" + filepath + ".txt")

        if args.profile == "all" or args.profile == "3t":
            print("=======================")
            print("Simming 3T Bear Trinkets...");
            print("=======================")
            numChunks = len(profiles_bear_3t) + 1
            for idx, profile in enumerate(profiles_bear_3t):
                print("Chunk " + str(idx + 1) + " of " + str(numChunks))
                filepath = str(ilevel) + "_3t_trinkets_" + str(idx)
                os.system(args.path_to_simc + " " + temp_path + "/" + filepath + ".simc output=" + output_path + "/" + filepath + ".txt")

        if args.profile == "all" or args.profile == "5t_incarnup":
            print("=======================")
            print("Simming 5T Bear (Incarnation Up) Trinkets...");
            print("=======================")
            numChunks = len(profiles_bear_5t_incarnup) + 1
            for idx, profile in enumerate(profiles_bear_5t_incarnup):
                print("Chunk " + str(idx + 1) + " of " + str(numChunks))
                filepath = str(ilevel) + "_5t_incarnup_trinkets_" + str(idx)
                os.system(args.path_to_simc + " " + temp_path + "/" + filepath + ".simc output=" + output_path + "/" + filepath + ".txt")

        if args.profile == "all" or args.profile == "5t_incarndown":
            print("=======================")
            print("Simming 5T Bear (Incarnation Down) Trinkets...");
            print("=======================")
            numChunks = len(profiles_bear_5t_incarndown) + 1
            for idx, profile in enumerate(profiles_bear_5t_incarndown):
                print("Chunk " + str(idx + 1) + " of " + str(numChunks))
                filepath = str(ilevel) + "_5t_incarndown_trinkets_" + str(idx)
                os.system(args.path_to_simc + " " + temp_path + "/" + filepath + ".simc output=" + output_path + "/" + filepath + ".txt")

        print("Done - Took " + str(time.time() - sim_start_time) + "s")

def buildTrinketProfiles(ilevel, apl_builder, chunk_size, settings):
    groups = args.group.split(",")
    if not all([x in trinkets.trinkets for x in groups]):
        raise KeyError("Group "+args.group+" not found in trinkets")


    # nested comprehension trick - flattens list of lists into single list
    copy_source = [trinket for group in (trinkets.trinkets[g] for g in groups) for trinket in group]
    char_gear = apl.buildGearList(
            stat_template = apl.getStatTemplate(ilevel),
            weapon_ilevel = apl.getWeaponLevel(ilevel))

    action_list = apl_builder(use_trinket = 1)

    copy_data = { "apl_builder": apl_builder }
    
    def copy_constructor(d): return buildTrinketCopiesFromData(**copy_data, **d)
    # we flatten again after generating
    copies = [copy for trinket in list(map(copy_constructor, copy_source)) for copy in trinket]

    clamped_chunk_size = min(max(1, chunk_size), len(copies))
    chunked_copies = [copies[i:i+clamped_chunk_size] for i in range(0, len(copies), clamped_chunk_size)]

    return [apl.buildProfile(
            sim_settings = settings,
            char_gear = char_gear,
            action_list = action_list,
            copy_constructors = '\n'.join(c)) for c in chunked_copies]

def buildTrinketCopiesFromData(apl_builder, name, id, gear_override="", bonusID=None, ilevel=None):
    ilevel_range = range(trinkets.min_ilevel, trinkets.max_ilevel+1, 5)
    trinket_template = Template("${maybe_gear}trinket1=,id=${id}${maybe_bonus},ilevel=${ilevel}")

    if ilevel is not None:
        ilevel_range = [ilevel]

    def buildSingleTrinketCopy(gear_override, id, bonusID, ilevel):
        copy_line = trinket_template.substitute(
                maybe_gear = ("" if gear_override == "" else gear_override+"\n"),
                id = id,
                maybe_bonus = ("" if bonusID is None else ",bonus_id="+str(bonusID)),
                ilevel = ilevel
                )

        return apl.buildCopy(copy_name = name+" ("+str(ilevel)+")", gear_override = copy_line)

    return map(lambda ilevel: buildSingleTrinketCopy(gear_override, id, bonusID, ilevel), ilevel_range)
    # return apl.buildCopy(
    #         copy_name = name,
    #         gear_reset = gear_reset,
    #         gear_override = line,
    #         apl_override = apl_override)

parser = argparse.ArgumentParser()
parser.add_argument("type", help="Either 'legendary' or 'trinket'")
parser.add_argument("ilevel", help="Either '920' or '900'", type=int)
parser.add_argument("path_to_simc", help="Path to the simc CLI binary")
parser.add_argument("-i", "--iterations", help="Override the amount of iterations", type=int, default=10000)
parser.add_argument("-e", "--error", help="Override the target_error", type=float, default=0.05)
parser.add_argument("-p", "--profile", help="Specific profile to run", default="all")
parser.add_argument("-g", "--group", help="Specific trinket group to run (only applies to trinket sims)", default="every")
parser.add_argument("-c", "--chunk", help="How many items to sim per invocation of simc (higher increases memory consumption)", type=int, default=inf)
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
    if ilevel != 920 and ilevel != 900:
        print("Unsupported item level")
        sys.exit()
    runTrinketSims(ilevel)
else:
    print("Unsupported sim type")
