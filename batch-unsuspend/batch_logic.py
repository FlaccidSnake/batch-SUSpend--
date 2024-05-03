from aqt import mw
from anki.notes import Note
from . import const
from aqt.utils import showInfo

# modded so that mass SUSPENDS instead of unsuspends, but function names remain "unsuspend"

def unsuspend_cards():  # Function name remains unchanged
    if mw.col is None:
        showInfo("mw.col is None")
        # Collection is not available so return
        return

    for rule_name, rule in const.CONFIG.get("Rules", {}).items():
        tag = rule.get("tag")
        # enclose tag name with quotes if contains parentheses
        if "(" or ")" in tag:
            tag = f'"{tag}"'
        n = rule.get("cards_count")
        active = rule.get("active")
        # Set a checkpoint so batch suspension can be undone if needed
        mw.checkpoint(f"Suspend Cards")
        # Check if the rule is currently activated
        if active == True:
                # Find unsuspended cards for the tag
                card_ids = mw.col.findCards(f"tag:{tag} -is:suspended")
                # Sort by their ID (which is equivalent to sorting by creation date)
                card_ids.sort()
                n_unsus_available = len(card_ids)
                # Give user warning if not enough to suspend
                if n_unsus_available == 0:
                    showInfo(f"{rule_name} has no cards left available to suspend")
                elif n_unsus_available < n:
                    showInfo(f"{rule_name} had only {n_unsus_available} card(s) left to suspend rather than {n}")
                    # Suspend the remaining available cards
                    mw.col.sched.suspendCards(card_ids[:n_unsus_available])
                else:
                    # Suspend the cards
                    mw.col.sched.suspendCards(card_ids[:n])
        # Reset the collection to update UI
        mw.reset()
