# # solution 1
# n = int(input("Enter a number : "))
# result = {}
# for i in range(1, n+1):
#     result[i] = i * i

# print(result)

# #solution 2 sort the dictionary by key in descending order
# result = dict(sorted(result.items(), reverse=True))

# print(result)

# # solution 3 
# result3 = {
#       }
# n = int(input("Enter the number of players : "))
# for i in range(n):
#     player_name = input("Enter the player name : ")
#     matches_played = int(input("Enter the number of matches played : "))
#     runs_scored = int(input("Enter the number of runs scored : "))
#     centuries = int(input("Enter the number of centuries scored : "))
#     half_centuries = int(input("Enter the number of half centuries scored : "))
#     result3[player_name] = (matches_played, runs_scored, centuries, half_centuries)
    


# print(result3,sep="\n")

# # solution 4
# sample_4 = {
#     "C++ Beginner Batch" : 70,
#     "Python Beginner Batch" : 180,
#     "Javascript Beginner Batch" : 150,
#     "Java Beginner Batch" : 220,
#     "Rust Beginner Batch" : 90
# }
# greatest = 0
# for i,value in sample_4.items():
#     greatest = max(greatest,value)

#     if value == greatest:
#         print(i, ":", value)
    

# solution 5
