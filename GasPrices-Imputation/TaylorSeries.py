import pandas as pd
import numpy as np

# Defining a function to quadratically approximate the missing values and return a numpy array
def quadraticApproximate(column: np.ndarray) -> np.ndarray:
    weekly_prices = column.copy() # Storing the column's original values
    length = len(column) # Length of the column we are estimating

    # Looping through the column
    for i in range(1, length):
        # Stopping at NaN values, to estimate them
        if pd.isna(column[i]):
            # Marking previous index (which is never NaN)
            prevIndex = i - 1

            # Looking for the first next non-NaN value
            nextIndex = i + 1
            while nextIndex < length and pd.isna(weekly_prices[nextIndex]):
                nextIndex += 1

            # Looking for the second next non-NaN value
            farNextIndex = nextIndex + 1
            while farNextIndex < length and pd.isna(weekly_prices[farNextIndex]):
                farNextIndex += 1

            # Looking for the second previous non-NaN value
            farPrevIndex = prevIndex - 1
            while pd.isna(weekly_prices[farPrevIndex]):
                farPrevIndex -= 1

            # Looking for the third previous non-NaN value
            farFarPrevIndex = farPrevIndex - 1
            while pd.isna(weekly_prices[farFarPrevIndex]):
                farFarPrevIndex -= 1

            # In the case of the extra week in the future, there is no next point(s) to use, so we use the last three points
            # this case happens when nextIndex is greater than or equal to the length (out of our data range) which will also mean farNextIndex is out of range
            if nextIndex >= length:
                # Setting the coordinates of the known original points
                y1, y2, y3 = weekly_prices[prevIndex], weekly_prices[farPrevIndex], weekly_prices[farFarPrevIndex]
                x1, x2, x3 = prevIndex, farPrevIndex, farFarPrevIndex
            
            # In the case of the last week recorded (not the week into future), we use the last two points and the next point (as we don't have a second next point)
            # this case happens when farNextIndex is greater than or equal to the length (out of our data range) but the first next point exists
            elif farNextIndex >= length and nextIndex < length:
                # Setting the coordinates of the known original points
                y1, y2, y3 = weekly_prices[prevIndex], weekly_prices[nextIndex], weekly_prices[farPrevIndex]
                x1, x2, x3 = prevIndex, nextIndex, farPrevIndex
            
            # In the case of the other weeks, we use the previous point, the next point, and the second next point
            # this case happens when farNextIndex is within our data range
            elif farNextIndex < length:
                # Setting the coordinates of the known original points
                y1, y2, y3 = weekly_prices[nextIndex], weekly_prices[prevIndex], weekly_prices[farNextIndex]
                x1, x2, x3 = nextIndex, prevIndex, farNextIndex
            else:
                # This will never be reached, but its here for safety
                raise ValueError("Invalid State")

            # Calculating the slopes
            slope1 = (y2 - y1) / (x2 - x1)
            slope2 = (y3 - y2) / (x3 - x2)

            # Calculating derivatives
            delta_x = (x3 - x1) / 2 # Average distance between two points 

            f_prime = slope1  # first derivative
            f_double_prime = (slope2 - slope1) / delta_x # second derivative

            # Filling in the missing values in the week
            for j in range(prevIndex + 1, nextIndex):
                if pd.isna(column[j]): 
                    # Using the quadratic taylor series to estimate the missing value
                    column[j] = y1 + f_prime * (j - x1) + 0.5 * f_double_prime * (j - x1) ** 2
                    ## print(f"index {j} estimated with {x1}, {x2}, {x3} and values {y1}, {y2}, {y3}") # For debugging

    # Returning the updated column
    return column