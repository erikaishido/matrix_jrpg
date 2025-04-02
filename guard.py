import utilities

# ref: https://deviq.com/design-patterns/guard-clause

def against_matrix_out_of_bounds(newCoords, matrixSize):
    if newCoords[0] < 0 or newCoords[1] < 0:
        return False
    if newCoords[0] >= matrixSize[0] or newCoords[1] >= matrixSize[1]:
        return False
    return True

# only used in states to filter out invalid input
def against_invalid_key_input(input, validKeys):
    if input not in validKeys:
        utilities.clearScreen()
        print(f"input {input} is invalid. try again.")
        return False
    return True

def against_menu_out_of_bounds(currentIndex, listLen, inputValue):
    if currentIndex + inputValue < 0:
        return False
    if currentIndex + inputValue > listLen - 1 :
        return False
    return True
