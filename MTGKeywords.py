# do this if i have time later, categorize all the keywords
# https://en.wikipedia.org/wiki/List_of_Magic:_The_Gathering_keywords#
keywords_actions = []


keywords = []
keywords_favorites = {}

# Keyword Actions
formatted_description = "[b]Attach[/b] - The term attach is used on Auras [color=#00bfff](see enchant)[/color], Equipment [color=#00bfff](see equip)[/color], and Fortifications [color=#00bfff](see fortify)[/color], which provide effects to certain other cards for an indeterminate amount of time. These types of cards are used by designating something (usually a permanent) for them to be 'attached' to."
keywords.append(formatted_description)

formatted_description = "[b]Counter[/b] - To counter a spell or ability is to remove it from the stack without resolving its effects, putting it directly into its owner's graveyard.[5]: 112  Some spells and abilities have an additional clause that replaces the graveyard with another game zone. There are instant spells that will explicitly counter other spells, generally known as 'counterspells' after the original card with this effect.[citation needed] Some cards specify that they 'cannot be countered'."
keywords.append(formatted_description)

formatted_description = "[b]Exile[/b] - To exile a card is to put it into the exile zone, usually as part of a card's effect.[5]: 113  Starting from the Magic 2010 rules changes, cards that 'remove [something] from the game' or 'set [something] aside' were issued errata to say 'exile [something]' instead.[6]"
keywords.append(formatted_description)

formatted_description = "[b]Fight[/b] - When two creatures fight each other, each creature deals damage equal to its power to the other creature.[5]: 114  Multiple creatures may fight each other at the same time. Fight is a keyword action that has been sporadically printed in some form since the card Gargantuan Gorilla, but it was not keyworded until Innistrad."
keywords.append(formatted_description)

formatted_description = "[b]Mill[/b] - When a player Mills x cards, they put the top x cards of that library into their graveyard.[5]: 114  Mill is an action that has been around since Antiquities with Millstone but was never given a keyword until M21, though the term 'mill' had been used informally for years prior to the official keywording.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Sacrifice[/b] - To sacrifice a permanent is to put it into its owner's graveyard. A player can only sacrifice a permanent they control. Note that this term is separate from other ways permanents can be put into their owners' graveyards, such as destruction (meaning regeneration has no effect on sacrifice) and state-based actions (a creature having 0 toughness, for example).[5]: 116  Players are not allowed to sacrifice unless prompted to by a game effect.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Scry[/b] - Scry x allows the player to take the top x cards from their deck, examine them, and place any number of them on the bottom of their deck and the rest on top in any order desired.[5]: 116  Scry originally appeared in Fifth Dawn as a keyword ability, primarily on instants and sorceries as 'Scry 2', though it was designed to allow other values. Future Sight added values 1 through 4 and redefined scry to be a keyword action, allowing it to be placed in the middle of an ability rather than as a 'tack-on' to other abilities. Scry then appeared in Magic 2011, becoming the first mechanic to be revisited in a core set. Scry also returned in Theros block before becoming an evergreen keyword in Magic Origins.\n\nAs of Pro Tour 2015 in Vancouver, the Scry mechanic was introduced to the official tournament rules when taking a mulligan. After all mulligans have resolved, any player whose opening hand contains fewer cards than their starting hand size may Scry 1. This is known colloquially as the 'Vancouver mulligan' or 'Vancouver rule'.[7] However, it has since been changed to a 'London mulligan.'"
keywords.append(formatted_description)

formatted_description = "[b]Tap/Untap[/b] - To untap a permanent is to return it to a vertical orientation, allowing it to be tapped again. A tapped permanent must be untapped before it can be tapped again. However, as introduced in the Shadowmoor block, untapping can also be a cost for activated abilities. It has its own special untap symbol (often called 'Q'), and is separate from normal untapping. To pay a cost including the untap symbol, the permanent must be already tapped. If that permanent is also a creature, then, as with the tap symbol, that ability can only be used if the creature has been under its controller's control since the beginning of their most recent turn."
keywords.append(formatted_description)


# Keywords
formatted_description = "[b]Deathtouch[/b] - Deathtouch is a static ability that causes a creature to be destroyed as a result of having been dealt damage by a source with deathtouch. In this way, for a creature with deathtouch, any nonzero amount of damage it deals to another creature is considered enough to kill it. Deathtouch appears mostly on black cards and green cards, and is often thematically associated with poisonous or cursed creatures. Prior to the introduction of the keyword, similar abilities have appeared mostly on green and black cards, but in most cases those abilities were functionally different (typically triggering on combat damage and/or at end of combat). This ability was first printed on a single timeshifted creature from Future Sight, Thornweald Archer. Older cards with similar or identical abilities, such as Cruel Deceiver, were not changed to gain deathtouch."
keywords.append(formatted_description)

formatted_description = "[b]Defender[/b] - Creatures with defender cannot attack. This ability was formerly associated with creature type Wall which had implicit 'rules baggage' that prevented attacking. This was simplified with the keyword, which was first used in the Kamigawa block."
keywords.append(formatted_description)

formatted_description = "[b]Double strike[/b] - A creature with double strike deals both first strike and normal combat damage. For instance, a creature such as Boros Swiftblade which has 1 power, 2 toughness, and double strike would defeat a creature with 2 power and 1 toughness in combat and survive, unless the latter creature also has first strike or double strike, as the first strike damage would destroy it before it would be able to deal damage. If the latter creature instead has 2 toughness, both creatures will be destroyed as the opposing creature survived the first strike, after which both creatures would simultaneously deal regular combat damage to each other. As with first strike, this keyword appears mostly on red and white cards. It first appeared in Legions and was first used in a Core Set in Tenth Edition."
keywords.append(formatted_description)

formatted_description = "[b]Enchant[/b] - This ability is written Enchant (quality) and appears on Auras, a subtype of enchantment spells. An Aura enters the battlefield attached to a permanent spell with the quality of its Enchant ability, and can only be attached to a permanent with that quality. If an Aura is no longer attached to a permanent with the required quality (such as if the object it enchants leaves the battlefield), it is put into its owner's discard pile. Like protection, the quality can be almost anything, but it normally has a permanent type associated with it, such as 'Enchant creature'. This ability was formerly seen in the type line instead of 'Enchantment - Aura'; the wording changed in the Ninth Edition core set, which introduced the Aura subtype."
keywords.append(formatted_description)

formatted_description = "[b]Equip[/b] - This ability is written Equip (cost).[5] It is found only on Equipment, a subtype of artifact spells that first appeared in Mirrodin. A player may pay the Equip cost as a sorcery (only during their own main phase when the stack is empty) to attach it to a creature they control.[5]: 126  That creature becomes 'equipped' and can then be referenced by the equipment as the 'equipped creature'.[5]: 50  The controller may pay the Equip cost again to move it to another creature. When a creature leaves the battlefield or stops being a creature by some effect, any equipment attached to it 'falls off', becoming unattached but remaining on the battlefield.[5]: 163  Equipment does not 'fall off' if another player gains control of either the creature or the equipment – the player who controls the equipment may pay the Equip cost to move it to a creature they control."
keywords.append(formatted_description)

formatted_description = "[b]First Strike[/b] - Creatures with first strike deal damage before other creatures in combat.[5]: 126 [8] Therefore, if a creature with first strike deals sufficient damage to kill an opposing creature without this ability, it will not suffer any combat damage from that creature in return.[5]: 126 [8] First strike is often found on red and white creatures, especially soldiers and knights who carry pikes or lances.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Flash[/b] - Flash is the keyword of an ability introduced in Mirage.[12] Artifacts, creatures or enchantments with flash may be played any time their controller could play an instant.[5]: 126  Older cards with that ability have been updated via rules errata to have flash; this allows them to work with cards such as Mystical Teachings."
keywords.append(formatted_description)

formatted_description = "[b]Flying[/b] - Creatures with flying cannot be blocked except by other creatures with flying and/or reach.[5]: 127 [8] Flying is the most common keyword, and appears in all five colors, but chiefly in blue and white.[citation needed] Creatures with flying are often Dragons, Angels, Birds, and other creatures that have wings; flying can also be possessed by some monks and the Djinn.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Haste[/b] - Creatures with the haste ability are able to attack and use abilities that involve the tap symbol on the turn a player gains control of them, instead of waiting until their controller's next turn.[5]: 127 [8] (An effect dubbed 'summoning sickness' otherwise prevents a creature from attacking or using abilities with the tap symbol unless its controller controlled it since the start of their most recent turn.[5]: 52 ) Haste is an example of a retroactive keywording, as cards from almost every earlier set have possessed 'may attack the turn [they] come into play' or 'unaffected by summoning sickness', which was replaced by the word 'haste'. It was later changed to include untapping to activate abilities as well. Creatures with haste are most often red.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Hexproof[/b] - A player or permanent with hexproof cannot be the target of spells or abilities controlled by an opponent.[5]: 127 [8] This is similar to shroud, but it does not deny the player (or their allies) the ability to target their own hexproof permanents. Cards that previously had or granted this ability were updated via rules errata to have hexproof with the release of the Commander decks.[citation needed] The Dominaria set introduced a variant of this keyword, hexproof from (quality), which (similarly to protection) prevents a permanent or player from being targeted by spells and abilities with listed quality.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Indestructible[/b] - A permanent with indestructible cannot be destroyed by effects that say 'Destroy' or by lethal damage.[5]: 127 [8] However, they can be countered, exiled, returned to the hand or library, sacrificed, or killed with effects that lower their toughness to zero. Initially appearing as a quality, indestructible was changed to a keyword so that it can be removed from a card to make it susceptible to being destroyed.[citation needed] Indestructible first appeared in Darksteel, chiefly among artifacts made of the titular metal, and has appeared in colored creatures in subsequent sets.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Lifelink[/b] - Permanents with lifelink cause their controller to gain life whenever they deal damage equal to the amount of damage dealt.[5]: 128 [8] Lifelink as a keyword was introduced in Future Sight, though the ability had previously existed on numerous cards, with rules errata retroactively changing these to lifelink. Cards with similar abilities were not changed in this way. Lifelink was a triggered ability when it was issued but is now a static ability due to the Magic 2010 rules changes.[6] (Cards that previously had a lifelink-like ability have been issued further errata to return them to their original functionality. The lone exception to this is the Mirrodin card Loxodon Warhammer, which, since it was reprinted in Tenth Edition with the lifelink keyword, retains that rather than the original functionality on all editions).[6] Lifelink is found mostly on white cards, and also on black cards.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Menace[/b] - A creature with menace can only be blocked by two or more creatures.[5]: 153 [8] Menace was instituted as a keyword in Magic Origins, and was retroactively applied to previous cards with that ability.[citation needed] Menace appears chiefly on black cards and red cards.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Protection[/b] - This ability is written as Protection from (quality).[5]: 129  A creature with protection from a quality cannot be enchanted, equipped, blocked, or targeted by anything with that quality, and all damage that would be dealt by a source of that quality is prevented, barring exceptions which explicitly state otherwise.[5]: 129  For example, a creature with protection from red cannot be enchanted by red auras, blocked by red creatures, targeted by red spells and abilities, or take damage from red sources. A common mnemonic for which effects are prevented by protection is the acronym DEBT, standing for 'Damage, Enchant (or Equip), Block, Target'. Note that the protection ability does not prevent effects that do not target.[citation needed]\n\nIf a creature gains protection while some of these effects are present, different things may happen. Any aura, equipment or fortifications attached to it that are no longer legally attached to it 'fall off', becoming unattached.[5]: 129  Auras that are not attached to anything are then put into their owners' graveyards, while equipment and fortifications stay on the battlefield.[5]: 129  Any spells of that quality (or abilities of permanents of that quality) that target it lose that creature as a target (for example, a creature gained protection from red in response to being targeted with Lightning Bolt). If they no longer have any legal targets, the spell 'fizzles' and has no effect.[5]: 93  However, a creature gaining protection in response to being blocked by a creature does not cause it to become unblocked, though it will prevent all damage that blocking creature would do to the creature with protection.[citation needed]\n\nInitially this ability was limited to 'Protection from (color)', but was later expanded to allow 'Protection from artifacts' in Urza's Legacy, and officially expanded to allow 'Protection from (quality)' in Invasion with the printing of Shoreline Raider. In Conflux, a card called Progenitus has 'Protection from everything' – it cannot be blocked, cannot be equipped or enchanted, cannot be targeted by spells or abilities, and cannot be dealt damage. Most cards with protection are either white or an enemy color from the color of protection offered (i.e. most cards with protection from blues are red and green).[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Prowess[/b] - Prowess is a triggered ability. A creature with prowess gains +1/+1 (until end of turn) whenever a noncreature spell is cast by its controller.[5]: 152  If a creature has multiple instances of prowess, each triggers separately.[5]: 152  Prowess was introduced in Khans of Tarkir and became an evergreen keyword with Magic Origins.[citation needed] Prowess appears chiefly on blue cards, and also on red and some white cards.[citation needed] After the release of Hour of Devastation, Prowess is no longer considered Evergreen, and has a Storm scale value of 4, with complications in interactions cited as the cause.[citation needed] As of Core Set 2021, prowess has experienced somewhat of a comeback.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Reach[/b] - Reach is a countermeasure to block creatures with flying.[5]: 130 [8] Creatures with flying can only be blocked by creatures with flying or reach. The keyword was introduced in Future Sight, and the flying rules themselves were changed to clarify this interaction.[citation needed] Older cards with the ability to 'block as though [they] had flying' were issued rules errata to have reach. Reach is found primarily in green creatures, especially Spiders.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Trample[/b] - An attacking creature with trample which is blocked may deal any excess damage, above what is needed to kill the blocker, directly to the defending player.[5]: 130 [8] The choice is made by the attacking player, as circumstances can arise in which 'overkilling' the blocking creature is a more advantageous move.[5]: 130  Trample is most often found on green or red creatures.[citation needed]"
keywords.append(formatted_description)

formatted_description = "[b]Vigilance[/b] - Vigilance existed as an ability in Limited Edition Alpha, but was retroactively keyworded beginning with the Kamigawa block.[citation needed] Creatures with vigilance do not tap when attacking [5]: 131 [8] (prior to being keyworded, these creatures' rules text read 'Attacking doesn't cause this creature to tap'), meaning they can still be used during the opponent's turn to block.[8] Creatures with vigilance are primarily white and secondarily green.[citation needed]"
keywords.append(formatted_description)









