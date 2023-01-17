
def trading_mechanics(volatileSupply: float, stableSupply: float, reserveSupply: float, choice: Choices) -> None:
    if choice == 'mintV':
        # mint volatile tokens
    elif choice == 'sellV':
        # sell volatile tokens
    elif choice == 'mintboth':
        # mint both volatile and stable tokens
    elif choice == 'mintS':
        # mint stable tokens
    elif choice == 'sellS':
        # sell stable tokens
    else:
        print("Invalid choice")
    return (volatileSupply, stableSupply, reserveSupply)
