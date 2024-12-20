import pandas as pd
import numpy as np

# Defining a function to linearly approximate the missing values and return a numpy array
def linearApproximate(column: np.ndarray) -> np.ndarray:
    weekly_prices = column.copy() # Storing the column's original values
    length = len(column) # Length of the column we are estimating

    # Looping through the column
    for i in range(1, length):
        # Stopping at NaN values, to estimate them
        if pd.isna(column[i]):
            # Marking previous index (which is never NaN)
            prevIndex = i - 1

            # Looking for the next non-NaN value
            nextIndex = i + 1
            while nextIndex < length and pd.isna(weekly_prices[nextIndex]):
                nextIndex += 1

            # In the case of the extra week in the future, there is no next point to use, so we use the last two points
            if nextIndex >= length:
                # Finding the second-to-last valid value
                farPrevIndex = prevIndex - 1
                while pd.isna(weekly_prices[farPrevIndex]):
                    farPrevIndex -= 1
                
                # We check once again if the farPrevIndex is valid before using it
                # We also make sure that the previous index is not NaN and actually in our data range
                if farPrevIndex >= 0 and not pd.isna(weekly_prices[prevIndex]):
                    # Setting the coordinates of the known original points
                    y1, y2 = weekly_prices[farPrevIndex], weekly_prices[prevIndex]
                    x1, x2 = farPrevIndex, prevIndex

            # In other cases, we use the next point as it is below the length's index
            elif nextIndex < length:
                # Setting the coordinates of the known original points
                y1, y2 = weekly_prices[prevIndex], weekly_prices[nextIndex]
                x1, x2 = prevIndex, nextIndex
            else:
                # This will never be reached, but its here for safety
                raise ValueError("Invalid state")

            # Calculating the slope
            slope = (y2 - y1) / (x2 - x1)

            # Filling in the missing values in the week
            for j in range(prevIndex + 1, nextIndex):
                # Using the line equation to estimate the missing value
                column[j] = weekly_prices[prevIndex] + (slope * (j - prevIndex))
                ## print(f"index {j} estimated with {x1}, {x2} and values {y1}, {y2}") # For debugging

    # Returning the updated column
    return column