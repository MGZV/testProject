# candidates = [
#     {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
#     {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
#     {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1}
# ]
#
#
# def find_top_20():
#     winers = list()
#     for can in candidates:
#         for ck, cv in can.items():
#             temp = list()
#             score = 0
#             if ck == "scores":
#                 for k, v in cv.items():
#                     score += v
#                     temp = [can["name"], score+can["extra_scores"],
#                             cv["math"]+cv["computer_science"]]
#                 winers.append(temp)
#     winers.sort(key=lambda i: (i[1], i[2]))
#     winers.reverse()
#     win_20 = list()
#     for name in (winers[:20]):
#         win_20.append(name[0])
#     print(win_20)
#
#
# find_top_20()
#

# names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo"]
# birthday_years = [1962,1995,2000,None,2000,None,None,1998,2001]
# genders = ["Male","Female","Male","Female",None,None,"Male",None,None]
#
#
# def get_inductees():
#     big_list = list()
#     doubt = list()
#     unlucky = list()
#     for x in range(len(names)):
#         big_list.append((names[x], birthday_years[x], genders[x]))
#     for list_value in big_list:
#         if list_value[1]:
#             if 1991 < list_value[1] <= 2003:
#                 if list_value[2] == 'Male':
#                     unlucky.append(list_value[0])
#                 elif list_value[2] is None:
#                     doubt.append(list_value[0])
#         else:
#             if list_value[2] != 'Female' or list_value[2] is None:
#                 doubt.append(list_value[0])
#     print(unlucky)
#     print(doubt)
#
#
# get_inductees()

# know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
# sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
# more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]
#
#
# def find_athlets():
#     swimmer = list()
#     for english in know_english:
#         if english in sportsmen:
#             if english in more_than_20_years:
#                 swimmer.append(english)
#     print(swimmer)
#
#
# find_athlets()

# students_avg_s

class Point:
    color = 'black'
    circle = 2