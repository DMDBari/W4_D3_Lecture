# You are given a string s representing an attendance record for a student where each character
#  signifies whether the student was absent, late, or present on that day. The record only 
# contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

def attendance(str):
    a_fail = 0
    l_fail = 0
    for char in str:
        if char == 'A':
            l_fail = 0
            a_fail += 1
            if a_fail >= 2:
                return False
        elif char == 'L':
            l_fail += 1
            if l_fail >= 3:
                return False
        else:
            l_fail = 0
    return True
