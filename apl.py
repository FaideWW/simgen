from string import Template

SETTINGS_GLOBAL = Template("""
iterations=${iterations}
target_error=${target_error}
""")

SETTINGS_1T = """
optimal_raid=1
max_time=300
vary_combat_length=0.2
enemy=Fluffy_Pillow
"""

SETTINGS_3T = """
optimal_raid=1
max_time=300
vary_combat_length=0.2
enemy=Fluffy_Pillow
enemy=enemy2
enemy=enemy3
"""

SETTINGS_5T_INCARNUP = """
optimal_raid=1
override.bloodlust=0

max_time=30
vary_combat_length=0.0
fixed_time=1

enemy=Fluffy_Pillow
enemy=enemy2
enemy=enemy3
enemy=enemy4
enemy=enemy5
"""

SETTINGS_5T_INCARNDOWN = """
optimal_raid=1
override.bloodlust=0

max_time=30
vary_combat_length=0.0
fixed_time=1

enemy=Fluffy_Pillow
enemy=enemy2
enemy=enemy3
enemy=enemy4
enemy=enemy5
"""

SETTINGS_TEMPLATE = Template("""
${iteration_settings}
${sim_settings}
output=${output_path}
""")

def buildSettings(settings_preset, iterations, target_error, output_path = ""):
    return SETTINGS_TEMPLATE.substitute(
            iteration_settings = SETTINGS_GLOBAL.substitute(iterations = iterations, target_error = target_error),
            sim_settings = settings_preset,
            output_path = output_path)

gear_list = Template("""
neck=,id=142428${stat_template},enchant=mark_of_the_hidden_satyr
main_hand=claws_of_ursoc,id=128821,gem_id=133686/137412/137327/0${weapon_ilevel}
off_hand=claws_of_ursoc,id=128822,ilevel=${weapon_ilevel}
""")

def buildGearList(stat_template = "", weapon_ilevel = ""):
    return gear_list.substitute(stat_template = stat_template, weapon_ilevel = weapon_ilevel)

bear_proc_sephuz = "actions+=/proc_sephuz,if=cooldown.thrash_bear.remains=0"
cat_proc_sephuz = "actions.bear+=/proc_sephuz"

bear_use_trinket_1 = "actions+=/use_item,slot=trinket1"
bear_use_trinket_2 = "actions+=/use_item,slot=trinket2"
cat_use_trinket_1 = "actions.bear+=/use_item,slot=trinket1"
cat_use_trinket_2 = "actions.bear+=/use_item,slot=trinket2"

BEAR_1T_PULVERIZE_TALENTS = "talents=http://us.battle.net/wow/en/tool/talent-calculator#Ub!0000212"
BEAR_1T_RNT_TALENTS = "talents=http://us.battle.net/wow/en/tool/talent-calculator#Ub!0000210"
CAT_1T_TALENTS = "talents=http://us.battle.net/wow/en/tool/talent-calculator#Ub!0010210"
BEAR_3T_TALENTS = "talents=http://us.battle.net/wow/en/tool/talent-calculator#Uba!0000110"
BEAR_5T_TALENTS = "talents=http://us.battle.net/wow/en/tool/talent-calculator#Uba!0000110"


BEAR_1T_PULVERIZE_APL = Template("""
${talents_line}
actions.precombat=flask,type=flask_of_the_seventh_demon
actions.precombat+=/food,type=seedbattered_fish_plate
actions.precombat+=/augmentation,type=defiled
actions.precombat+=/bear_form
actions.precombat+=/snapshot_stats
actions.precombat+=/potion,name=old_war

actions=auto_attack
actions+=/potion,name=old_war,if=buff.rage_of_the_sleeper.up
actions+=/barkskin,if=talent.brambles.enabled&buff.rage_of_the_sleeper.up
actions+=/berserking,if=buff.rage_of_the_sleeper.up
actions+=/rage_of_the_sleeper,if=buff.bear_form.up&dot.moonfire.ticking
${maybe_proc_sephuz}
${maybe_use_trinket_1}
${maybe_use_trinket_2}
actions+=/maul
actions+=/pulverize,if=((cooldown.thrash_bear.remains<2&((dot.thrash_bear.stack=5&equipped.137067)|(dot.thrash_bear.stack=3&!equipped.137067)))|(dot.trash_bear.stack>=2&target.time_to_die<2)|(dot.trash_bear.stack>=4&target.time_to_die<4))
actions+=/thrash_bear
actions+=/mangle
actions+=/moonfire,if=buff.galactic_guardian.up
actions+=/swipe_bear
""")

CAT_1T_APL = Template("""
${talents_line}
actions.precombat=flask,type=flask_of_the_seventh_demon
actions.precombat+=/food,type=seedbattered_fish_plate
actions.precombat+=/augmentation,type=defiled
actions.precombat+=/cat_form
actions.precombat+=/prowl
actions.precombat+=/snapshot_stats
actions.precombat+=/potion,name=old_war

actions=rake,if=buff.prowl.up&buff.cat_form.up
actions+=/auto_attack
actions+=/potion,name=old_war,if=buff.rage_of_the_sleeper.up
actions+=/call_action_list,name=cat,if=(cooldown.thrash_bear.remains>0&cooldown.mangle.remains>0&buff.rage_of_the_sleeper.down&buff.incarnation.down&buff.galactic_guardian.down)|(buff.cat_form.up&energy>20)|(dot.rip.ticking&dot.rip.remains<3&target.health.pct<25)
actions+=/call_action_list,name=bear

actions.bear=bear_form
${maybe_proc_sephuz}
${maybe_use_trinket_1}
${maybe_use_trinket_2}
actions.bear+=/incarnation
actions.bear+=/barkskin,if=talent.brambles.enabled&buff.rage_of_the_sleeper.up
actions.bear+=/berserking,if=buff.rage_of_the_sleeper.up&dot.moonfire.ticking
actions.bear+=/moonfire,if=!dot.moonfire.ticking&(talent.incarnation.enabled|talent.soul_of_the_forest.enabled)
actions.bear+=/lunar_beam,if=(dot.rip.remains>10&buff.bear_form.up)
actions.bear+=/rage_of_the_sleeper,if=(dot.rip.remains>10&buff.bear_form.up)
actions.bear+=/thrash_bear,if=(buff.incarnation.up=1&dot.thrash_bear.remains<=2)|talent.rend_and_tear.enabled&dot.thrash_bear.stack<3|talent.rend_and_tear.enabled&equipped.137067&dot.thrash_bear.stack<5|equipped.137056
actions.bear+=/maul
actions.bear+=/mangle
actions.bear+=/thrash_bear
actions.bear+=/moonfire,if=buff.galactic_guardian.up
actions.bear+=/swipe_bear

actions.cat=dash,if=buff.cat_form.down
actions.cat+=/cat_form,if=buff.cat_form.down
actions.cat+=/ferocious_bite,if=(combo_points>3&target.time_to_die<3)|(combo_points=5&energy>=50&dot.rip.remains>10)|(dot.rip.ticking&target.health.pct<25&combo_points=5&energy>=50)|(dot.rip.ticking&dot.rip.remains<3&target.health.pct<25)
actions.cat+=/rip,if=(!dot.rip.ticking&combo_points=5)|(dot.rip.remains<8&combo_points=5)
actions.cat+=/shadowmeld,if=dot.rake.remains<8
actions.cat+=/rake,if=dot.rake.remains<8|(combo_points=4&time<10)
actions.cat+=/shred
""")

BEAR_3T_APL = Template("""
${talents_line}
actions.precombat=flask,type=flask_of_the_seventh_demon
actions.precombat+=/food,type=seedbattered_fish_plate
actions.precombat+=/augmentation,type=defiled
actions.precombat+=/bear_form
actions.precombat+=/snapshot_stats
actions.precombat+=/potion,name=prolonged_power

actions=auto_attack
actions+=/potion,name=prolonged_power,if=buff.rage_of_the_sleeper.up
actions+=/barkskin,if=talent.brambles.enabled&buff.rage_of_the_sleeper.up
actions+=/berserking,if=buff.rage_of_the_sleeper.up
actions+=/incarnation,if=((dot.thrash_bear.stack=5&equipped.137067)|(dot.thrash_bear.stack=3&!equipped.137067))&cooldown.thrash_bear.remains>0
actions+=/rage_of_the_sleeper,if=buff.bear_form.up
${maybe_proc_sephuz}
${maybe_use_trinket_1}
${maybe_use_trinket_2}
actions+=/maul
actions+=/thrash_bear
actions+=/moonfire,if=dot.moonfire.remains<4.8&!buff.incarnation.up,cycle_targets=1,max_cycle_targets=2
actions+=/mangle
actions+=/moonfire,if=dot.moonfire.remains<4.8&!buff.incarnation.up,cycle_targets=1
actions+=/swipe_bear
""")

BEAR_5T_INCARNUP_APL = Template("""
${talents_line}
actions.precombat=flask,type=flask_of_the_seventh_demon
actions.precombat+=/food,type=seedbattered_fish_plate
actions.precombat+=/augmentation,type=defiled
actions.precombat+=/bear_form
actions.precombat+=/snapshot_stats
actions.precombat+=/potion,name=prolonged_power

actions=auto_attack
actions+=/potion,name=prolonged_power,if=buff.rage_of_the_sleeper.up
actions+=/barkskin,if=talent.brambles.enabled&buff.rage_of_the_sleeper.up
actions+=/berserking,if=buff.rage_of_the_sleeper.up
actions+=/incarnation,if=cooldown.thrash_bear.remains>0
actions+=/rage_of_the_sleeper,if=buff.bear_form.up
${maybe_proc_sephuz}
${maybe_use_trinket_1}
${maybe_use_trinket_2}
actions+=/maul
actions+=/thrash_bear
actions+=/moonfire,if=dot.moonfire.remains<4.8&!buff.incarnation.up,cycle_targets=1
actions+=/swipe_bear
""")

BEAR_5T_INCARNDOWN_APL = Template("""
${talents_line}
actions.precombat=flask,type=flask_of_the_seventh_demon
actions.precombat+=/food,type=seedbattered_fish_plate
actions.precombat+=/augmentation,type=defiled
actions.precombat+=/bear_form
actions.precombat+=/snapshot_stats
actions.precombat+=/potion,name=prolonged_power

actions=auto_attack
actions+=/potion,name=prolonged_power,if=buff.rage_of_the_sleeper.up
#actions+=/barkskin,if=talent.brambles.enabled&buff.rage_of_the_sleeper.up
actions+=/berserking,if=buff.rage_of_the_sleeper.up
${maybe_proc_sephuz}
${maybe_use_trinket_1}
${maybe_use_trinket_2}
actions+=/maul
actions+=/thrash_bear
actions+=/moonfire,if=dot.moonfire.remains<4.8&!buff.incarnation.up&(target.time_to_die*1.6)>(16+dot.moonfire.remains),cycle_targets=1
actions+=/swipe_bear
""")

def buildAPL(apl_template = "", talents = "", proc_sephuz = "", use_trinket_1 = "", use_trinket_2 = ""):
    return apl_template.substitute(
            talents_line = talents,
            maybe_proc_sephuz = proc_sephuz,
            maybe_use_trinket_1 = use_trinket_1,
            maybe_use_trinket_2 = use_trinket_2)

def buildBear1TAPL(talents = None, proc_sephuz = False, use_trinket = 0):
    if talents is None:
        talents = BEAR_1T_PULVERIZE_TALENTS
    return buildAPL(
            apl_template = BEAR_1T_PULVERIZE_APL,
            talents = talents,
            proc_sephuz = bear_proc_sephuz if proc_sephuz == True else "",
            use_trinket_1 = bear_use_trinket_1 if use_trinket % 2 == 1 else "",
            use_trinket_2 = bear_use_trinket_2 if use_trinket > 0 and use_trinket % 2 == 0 else "")


def buildCat1TAPL(talents = None, proc_sephuz = False, use_trinket = 0):
    return buildAPL(
            apl_template = CAT_1T_APL,
            talents = CAT_1T_TALENTS,
            proc_sephuz = cat_proc_sephuz if proc_sephuz == True else "",
            use_trinket_1 = cat_use_trinket_1 if use_trinket % 2 == 1 else "",
            use_trinket_2 = cat_use_trinket_2 if use_trinket > 0 and use_trinket % 2 == 0 else "")


def buildBear3TAPL(talents = None, proc_sephuz = False, use_trinket = 0):
    return buildAPL(
            apl_template = BEAR_3T_APL,
            talents = BEAR_3T_TALENTS,
            proc_sephuz = bear_proc_sephuz if proc_sephuz == True else "",
            use_trinket_1 = bear_use_trinket_1 if use_trinket % 2 == 1 else "",
            use_trinket_2 = bear_use_trinket_2 if use_trinket > 0 and use_trinket % 2 == 0 else "")

def buildBear5TIncarnUpAPL(talents = None, proc_sephuz = False, use_trinket = 0):
    return buildAPL(
            apl_template = BEAR_5T_INCARNUP_APL,
            talents = BEAR_5T_TALENTS,
            proc_sephuz = bear_proc_sephuz if proc_sephuz == True else "",
            use_trinket_1 = bear_use_trinket_1 if use_trinket % 2 == 1 else "",
            use_trinket_2 = bear_use_trinket_2 if use_trinket > 0 and use_trinket % 2 == 0 else "")

def buildBear5TIncarnDownAPL(talents = None, proc_sephuz = False, use_trinket = 0):
    return buildAPL(
            apl_template = BEAR_5T_INCARNDOWN_APL,
            talents = BEAR_5T_TALENTS,
            proc_sephuz = bear_proc_sephuz if proc_sephuz == True else "",
            use_trinket_1 = bear_use_trinket_1 if use_trinket % 2 == 1 else "",
            use_trinket_2 = bear_use_trinket_2 if use_trinket > 0 and use_trinket % 2 == 0 else "")



trinket_stat_template_920 = ",stats=2264agi_1225vers_0crit_0mastery_0haste"
trinket_stat_template_900 = ",stats=1879agi_1137vers_0crit_0mastery_0haste"

gear_reset = Template("""
legs=
wrists=
waist=
chest=
finger1=
finger2=
hands=
shoulders=
trinket1=eye_of_guarm,id=142506${trinket_stat_template}
trinket2=eye_of_guarm,id=142506${trinket_stat_template}
""")

copy_template = Template("""
copy=${copy_name}
${gear_reset}
${gear_override}
${apl_override}
""")

def buildGearReset(ilevel):
    trinket_stats = trinket_stat_template_920 if ilevel == 920 else trinket_stat_template_900
    return gear_reset.substitute(trinket_stat_template = trinket_stats)

def buildCopy(copy_name = "", gear_reset = "", gear_override = "", apl_override = ""):
    return copy_template.substitute(
            copy_name = copy_name,
            gear_reset = gear_reset,
            gear_override = gear_override,
            apl_override = apl_override)

full_apl_template = Template("""
${sim_settings}
${char_info}
${char_gear}
${action_list}
${copy_constructors}
""")

apl_char_info = """
druid="Baseline"
level=110
race=tauren
role=tank
position=front
artifact=57:0:0:0:0:948:3:949:3:950:3:951:3:952:4:953:3:954:3:955:3:956:4:957:1:958:1:959:1:960:1:961:1:962:1:979:1:1334:1:1366:1:1509:4:1510:1:1511:1:1634:1
spec=guardian
"""
def buildProfile(sim_settings = "", char_info = apl_char_info, char_gear = "", action_list = "", copy_constructors = ""):
    return full_apl_template.substitute(
            sim_settings = sim_settings,
            char_info = char_info,
            char_gear = char_gear,
            action_list = action_list,
            copy_constructors = copy_constructors)


def getStatTemplate(ilevel):
    if ilevel == 900:
        return ",stats=15464agi_5143crit_5143haste_5143mastery_5143versatility"
    elif ilevel == 920:
        return  ",stats=18626agi_5653crit_5653haste_5653mastery_5653versatility"

def getWeaponLevel(ilevel):
    if ilevel == 920:
        return ",ilevel=942"
    elif ilevel == 900:
        return ",ilevel=924"

