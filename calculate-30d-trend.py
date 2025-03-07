import math

def calc_issue_trends(old_value, new_value):
  
    # if both values are 0, return 0% change (avoiding dividing by 0)
    if old_value == new_value:
      return "0%"

    # if the old value is 0 but new value is not, return +100% (avoiding dividing by 0)
    elif old_value == 0:
      return "↑100%"

    # if the new value is 0 but the old value is not, return 100% decrease
    elif new_value == 0:
      return "↓100%"

    # calculate the percentage change
    # rounds up if increase and rounds down if decrease
    else:
      change = ((new_value - old_value) / abs(old_value)) * 100
      rounded_change_up = math.ceil(abs(change)) * (-1 if change < 0 else 1)
      rounded_change_down = math.floor(abs(change)) * (-1 if change < 0 else 1)
      
      if change > 0:
        return f"↑{rounded_change_up}%"
      elif -1 < change <= 0:
        return f"0%"
      else:
        return f"↓{abs(rounded_change_down)}%"

# set values
old_value = <valueFrom30daysAgoHere>
new_value = <valueFromTodayHere>

#output
result = calc_issue_trends(old_value, new_value)
print(result, end='')