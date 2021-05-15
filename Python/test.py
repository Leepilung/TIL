monthMap = {
  0: 31,
  1: 28,
  2: 31,
  3: 30,
  4: 31,
  5: 30,
  6: 31,
  7: 31,
  8: 30,
  9: 31,
  10: 30,
  11: 31
}
#입력 날짜를 쪼개주는 역할
def parseDate(date):
  return [int(split) for split in date.split('/')]
#윤년 확인 역할
def getIsLeafYear(year):
  return year % 4 == 0 and year % 100 != 0 and year % 400 ==0
#입력 날짜로부터 시작날짜를 판단하는 역할
def getDayFromDate(year, month, day):
  result = (year - 1) * 365
  # 윤년일때 예외처리
  for i in range(year):
    if getIsLeafYear(i + 1):
      result += 1
  # 
  for i in range(11):
    if month <= i + 1: 
      break
    result = result + monthMap[i]
  result = result + day;
  return result % 7
  #캘린더에 공백 입력하는 함수
def printCalendarItem(value):
  return "{:^6}".format(value)
  #달에 입력하는 요일 정리해둔 함수
daysInKor = ["sun", "mon", "tur", "wen","thu", "fri", "sat"]
def printCalendar(dateString):
  [year, month, day] = parseDate(dateString)
  #입력날짜를 리스트로 쪼개 parsedate로 나눈다.
  isLeafYear = getIsLeafYear(year)
  startDay = getDayFromDate(year, month, 1)
  print("".join([printCalendarItem(day) for day in daysInKor]))
  print("".join(["------" for _ in range(7)]));
  counter = 0;
  # (달력의 공백 넣어주는 부분)
  for i in range(7):
    if i < startDay:
      counter += 1;
      print(printCalendarItem(""), end="")
    else:
      break
  # 출력하는 부분
  for i in range(31):
    counter += 1;
    day = i + 1
    print(printCalendarItem(day), end="")
    if counter % 7 == 0:
      print("")
    if day == monthMap[month] and not isLeafYear:
      print("")
      break
    if isLeafYear and month == 2 and day == monthMap[month] + 1:
      print("")
      break
  print("".join(["------" for _ in range(7)]))
while True:
  printCalendar(input("날짜를 입력하시오:"))