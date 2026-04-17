# worlds/content_warning/options.py

from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions


# ===========================================================================
# GOAL
# ===========================================================================

class GoalChoice(Choice):
    """Choose the primary victory condition for your run.

    viral_sensation:  Reach 645,000 total views — the highest view milestone.
    views_goal:       Reach a configurable total view count (see Views Goal Target).
    quota_goal:       Reach and complete a configurable number of quotas
                      (see Quota Requirement and Quota Count; requires Quota Requirement on).
    monster_hunter:   Film a configurable number of different monsters (see Monster Hunter Count).
    hat_collector:    Purchase a configurable number of hats (see Hat Collector Count).
    item_collector:   Purchase a configurable number of store items and emotes
                      (see Item Collector Count)."""
    display_name = "Goal"
    option_viral_sensation = 0
    option_views_goal      = 1
    option_quota_goal      = 2
    option_monster_hunter  = 3
    option_hat_collector   = 4
    option_item_collector  = 5
    default = 0


class ViewsGoalTarget(Range):
    """When Goal is 'views_goal', this sets the required total views to win.
    The game uses the nearest view milestone at or above the configured value.
    Ignored when Goal is not 'views_goal'."""
    display_name = "Views Goal Target"
    range_start  = 1000
    range_end    = 645000
    default      = 128000


class MonsterHunterCount(Range):
    """When Goal is 'monster_hunter', the number of different monsters that must
    be filmed to win. Minimum 5, maximum 33."""
    display_name = "Monster Hunter Count"
    range_start  = 5
    range_end    = 33
    default      = 12


class HatCollectorCount(Range):
    """When Goal is 'hat_collector', the number of hats that must be purchased
    to win. Minimum 5, maximum 31 (total hats available)."""
    display_name = "Hat Collector Count"
    range_start  = 5
    range_end    = 31
    default      = 15


class ItemCollectorCount(Range):
    """When Goal is 'item_collector', the number of store items and emotes that
    must be purchased to win. Minimum 5, maximum 33."""
    display_name = "Item Collector Count"
    range_start  = 5
    range_end    = 33
    default      = 10


# ===========================================================================
# QUOTA
# ===========================================================================

class QuotaRequirement(DefaultOnToggle):
    """When enabled, quota checks are included in the location pool and
    completing quotas can be part of the goal.
    When disabled, ALL quota-related checks are removed from the pool
    (the 'quota_goal' Goal option becomes invalid and falls back to
    'viral_sensation')."""
    display_name = "Quota Requirement"


class QuotaCount(Range):
    """The number of quotas that must be reached and completed.
    Controls both how many quota locations exist in the pool and (if
    Goal is 'quota_goal') how many are required to win.
    Minimum 1, maximum 10.
    Requires Quota Requirement to be enabled."""
    display_name = "Quota Count"
    range_start  = 1
    range_end    = 10
    default      = 5


# ===========================================================================
# ADDITIONAL VICTORY REQUIREMENTS (stack on top of the main Goal)
# ===========================================================================

class ContentCompleteSanity(Toggle):
    """When enabled, you must ALSO film a certain number of different monsters
    to win, on top of the primary Goal.
    Configure the required count with Content Complete Monster Count.
    Suggested minimum: 12. Off by default."""
    display_name = "Content Complete Sanity"


class ContentCompleteMonsterCount(Range):
    """The number of different monsters that must be filmed as an additional
    victory requirement when Content Complete Sanity is enabled.
    Minimum 5, maximum 33. Default 12 (as suggested)."""
    display_name = "Content Complete Monster Count"
    range_start  = 5
    range_end    = 33
    default      = 12


class Itemsanity(Toggle):
    """When enabled, you must ALSO purchase a certain number of different store
    items and emotes to win (in addition to the primary Goal).
    Configure the required count with Itemsanity Count.
    Counts both Store Purchases and Emotes."""
    display_name = "Itemsanity"


class ItemsanityCount(Range):
    """The number of different store items/emotes that must be purchased as an
    additional victory requirement when Itemsanity is enabled.
    Minimum 5, maximum 33."""
    display_name = "Itemsanity Count"
    range_start  = 5
    range_end    = 33
    default      = 10


class Hatsanity(Toggle):
    """When enabled, you must ALSO purchase a certain number of hats to win
    (in addition to the primary Goal).
    Configure the required count with Hatsanity Count."""
    display_name = "Hatsanity"


class HatsanityCount(Range):
    """The number of hats that must be purchased as an additional victory
    requirement when Hatsanity is enabled.
    Minimum 5, maximum 31."""
    display_name = "Hatsanity Count"
    range_start  = 5
    range_end    = 31
    default      = 10


# ===========================================================================
# OPTIONAL LOCATION GROUPS
# ===========================================================================

class IncludeHats(DefaultOnToggle):
    """When enabled, purchasing each hat from Phil's Hat Shop is a check location.
    Disable to remove all hat locations from the pool."""
    display_name = "Include Hat Purchases"


class IncludeEmotes(DefaultOnToggle):
    """When enabled, purchasing each emote from the store is a check location.
    Disable to remove all emote locations from the pool."""
    display_name = "Include Emote Purchases"


class IncludeSponsorship(DefaultOnToggle):
    """When enabled, accepting sponsorships (3 checks) are check locations.
    Disable to remove all sponsorship acceptance locations from the pool."""
    display_name = "Include Sponsorships"


class Sponsorsanity(Toggle):
    """When enabled, completing each sponsorship difficulty
    (Easy, Medium, Hard, Very Hard) adds extra check locations.
    Requires Include Sponsorships to be enabled."""
    display_name = "Sponsorsanity"


class DifficultMonsters(Toggle):
    """When enabled, difficult/rare monsters (Flicker, Cam Creep, Infiltrator,
    Black Hole Bot, Ear, Snail Spawner, Big Slap, Ultra Knifo, Angler) can
    have real (non-filler) items behind their filming checks.
    When disabled (default), those checks always contain filler rewards."""
    display_name = "Difficult Monsters Have Real Items"


# ===========================================================================
# LOGIC
# ===========================================================================

class DungeonLogic(Choice):
    """How strictly survival gear is logically required to access dungeon checks.

    easy: Shock Stick, Rescue Hook, or Defibrillator are required before dangerous
          monster filming locations are in logic.
    hard: Nothing is required; the player may face dangerous situations without
          safety equipment."""
    display_name = "Dungeon Logic"
    option_easy = 0
    option_hard = 1
    default = 0


# ===========================================================================
# OPTIONS DATACLASS
# ===========================================================================

@dataclass
class ContentWarningGameOptions(PerGameCommonOptions):
    # Goal
    goal:                       GoalChoice
    views_goal_target:          ViewsGoalTarget
    monster_hunter_count:       MonsterHunterCount
    hat_collector_count:        HatCollectorCount
    item_collector_count:       ItemCollectorCount

    # Quota
    quota_requirement:          QuotaRequirement
    quota_count:                QuotaCount

    # Extra win conditions
    content_complete_sanity:         ContentCompleteSanity
    content_complete_monster_count:  ContentCompleteMonsterCount
    itemsanity:                      Itemsanity
    itemsanity_count:                ItemsanityCount
    hatsanity:                       Hatsanity
    hatsanity_count:                 HatsanityCount

    # Optional location groups
    include_hats:           IncludeHats
    include_emotes:         IncludeEmotes
    include_sponsorships:   IncludeSponsorship
    sponsorsanity:          Sponsorsanity
    difficult_monsters:     DifficultMonsters

    # Logic
    dungeon_logic:          DungeonLogic
