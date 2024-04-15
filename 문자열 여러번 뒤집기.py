def solution(my_string, queries):

    for query in queries:
        my_string1= my_string[:query[0]]
        #리스트 reverse: [::-1]
        my_string2= my_string[query[0]:query[1]+1][::-1]
        my_string3= my_string[query[1]+1:]
        my_string = my_string1+my_string2+my_string3


    return my_string

print(solution("rermgorpsam",[[2, 3], [0, 7], [5, 9], [6, 10]]))