def add_time(start, duration, start_day=""):
  """
  Takes in two required parameters and one optional parameter:
  - a start time in the 12-hour clock format (ending in AM or PM)
  - a duration time that indicates the number of hours and minutes
  - (optional) a starting day of the week, case insensitive
  The function should add the duration time to the start time and return the result.
  """
  days_of_week = ["", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  m = ["AM", "PM"]

  start_hr = int(start[:start.find(":")]) + 12 * m.index(start[start.find(" ")+1:].upper())
  if start_hr == 12 or start_hr == 24:
    start_hr = start_hr - 12

  start_min = int(start[start.find(":")+1:start.find(" ")])

  try:
    start_day = days_of_week.index(start_day.title())
  except:
    start_day = 0
  
  add_min = 60*int(duration[:duration.find(":")]) + int(duration[duration.find(":")+1:])
  new_min_raw = start_min + add_min

  new_min = new_min_raw % 60

  add_hr = int(new_min_raw / 60)
  new_hr_raw = start_hr + add_hr

  new_hr = new_hr_raw % 24

  add_day = int(new_hr_raw / 24)
  
  if start_day:
    new_day_raw = start_day + add_day
    new_day = new_day_raw % 7
    day = ", "+days_of_week[new_day]
  else:
    new_day=0
    day = ""
  
  if new_hr > 0 and new_hr < 12:
    new_m = m[0]
  elif new_hr > 12:
    new_hr = new_hr - 12
    new_m = m[1]
  else:
    new_m = m[int(new_hr / 12)]
    new_hr = 12
  
  days_later=""
  if add_day == 1:
    days_later = " (next day)"
  elif add_day > 1:
    days_later = " ({} days later)".format(add_day)
  
  new_time = "{}:{:02d} {}{}{}".format(new_hr, new_min, new_m, day, days_later)


  return new_time