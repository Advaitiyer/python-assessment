'''
Task 1:
- List comprehension-based solution

- Arguments of the function is (LIST OF DICTIONARIES, VALUE TO FILTER) 

- Iterating over list of dictionaries (WEBSITES) and filtering in only values which are greater than or equal to filter_value (4).

- Time complexity: O(n) since as the list of dictionary grows, the length which has to be searched grows linearly.

- Space complexity: In the worst case, all values are in the filtered list. Hence, the worst case space complexity would be O(n)
as we will need to store this new list whose size grows linearly.
'''

def task_one(list_of_dicts, filter_value):
    return [ls for ls in list_of_dicts if ls['value'] >= filter_value]

'''
Task 2:
- Arguments of the function is (LIST OF DICTIONARIES, STRING WHICH HAS TO BE PREPENDED, KEY FOR WHICH THE PREPEND IS TO BE DONE)

- Iterating over list of dictionaries (WEBSITES) and checking if the 'domain' key starts with 'www.'. If it does not, prepend 'www.'
at the beginning of the string. If it does, continue the for loop ignoring the dictionary which is currently in the iteration.

- Time complexity: For loop takes O(n) since the number of times looping occurs would increase as per the size of the list. If/Else
takes O(1) since it is only checking if the condition is True or False. Therefore, in total this algorithm has O(n) time complexity.

- Space complexity: In the worst case, all the values need to be prepended with 'www.', hence this algorithm has a space complexity of O(n).
Since it is not append, each character moves over by 4 places to make space for 'www.'.
'''

def task_two(list_of_dicts, string_to_add, key):
    for dict in list_of_dicts:
        if dict[key].startswith(string_to_add) == False:
            dict[key] = string_to_add + dict[key]
        else:
            continue
    return list_of_dicts

'''
Task 3:
- Arguments of the function is (LIST OF DICTIONARIES, STRING WHICH IS TO BE CHECKED, KEY TO BE CHECKED, KEY TO BE UPDATED)

- In my solution, all the websites with 'https://' are secure, and the ones with 'http://' are not secure. Accordingly the value of
dictionary['secure'] has been updated to True/False.

- We iterate over the list of dictionaries (WEBSITES) using for loop and check if the string value of the key to be checked starts
with 'https://'. If it does, we update the dictionary['secure'] value to True, and if it does not, we update the value to False.
Here, I assumed the worst case, i.e., all the secure values might be incorrect, therefore I went ahead and updated each and every instance
even if they might be correct. Since the value of this key is a Boolean (True/False), the amount of space that is consumed is very less,
so updating all the values is not a very expensive operation. 

- Time complexity: As the list grows, the number of iterations grow linearly. Therefore, the time complexity is O(n).

- Space complexity: We update each and every value of the 'secure' key, so the space complexity is O(n). This algorithm works well for
the worst case, but for an average case it consumes more space than needed. However, since it is a cybersecurity-related solution,
prioritizing security over space complexity was more important to me.
'''

def task_three(list_of_dicts, string_to_check, key_to_check, key_to_update):
    for dict in list_of_dicts:
        if dict[key_to_check].startswith(string_to_check) == True:
            dict[key_to_update] = True
        else:
            dict[key_to_update] = False
    return list_of_dicts

'''
Task 4:
- Arguments of the function is (LIST OF DICTIONARIES, VALUE KEY)

- Created a new int variable in the function. Iterated over the list of dictionaries, and updated the value of the new variable
by adding the value of the 'value' key.

- Time complexity: Since we have to iterate over each and every dictionary in the list, the complexity is O(n).

- Space complexity: In this case, the only update that consumes space is the value of the new variable. Hence, the space complexity
is O(1) as we only need to store the value of this new variable.
'''

def task_four(list_of_dicts, key):
    sum_total = 0
    for dict in list_of_dicts:
        sum_total += dict[key]
    return sum_total
        

if __name__ == "__main__":
    from data import WEBSITES
    print("Task 1 Solution: --->")
    print(task_one(list_of_dicts = WEBSITES, filter_value=4)) 
    # Output of task 1: [{'name': 'Google', 'url': 'https://www.google.co.uk', 'secure': True, 'domain': 'google.co.uk', 'value': 5}, {'name': 'Facebook', 'url': 'https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/', 'secure': True, 'domain': 'facebook.com', 'value': 4}, {'name': 'YouTube', 'url': 'https://www.youtube.com/watch?v=09Cd7NKKvDc', 'secure': True, 'domain': 'youtube.com', 'value': 5}]
    print("Task 2 Solution: --->")
    print(task_two(list_of_dicts = WEBSITES, string_to_add = 'www.', key = 'domain'))
    # Output of task 2: [{'secure': True, 'url': 'https://www.google.co.uk', 'name': 'Google', 'domain': 'www.google.co.uk', 'value': 5}, {'secure': True, 'url': 'https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/', 'name': 'Facebook', 'domain': 'www.facebook.com', 'value': 4}, {'secure': False, 'url': 'https://www.bing.com/search?q=athlete&qs=n&form=QBLH&sp=-1&pq=athlete&sc=8-7&sk=&cvid=53830DD7FB2E47B7A5D9CF27F106BC9A', 'name': 'Bing', 'domain': 'www.bing.com', 'value': 3}, {'secure': False, 'url': 'https://uk.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q=jupiter', 'name': 'Ask', 'domain': 'www.ask.com', 'value': 1}, {'secure': True, 'url': 'http://duckduckgo.com/?q=plane&t=h_&ia=web', 'name': 'Duck Duck Go', 'domain': 'www.duckduckgo.com', 'value': 2}, {'secure': False, 'url': 'https://vimeo.com/53812885', 'name': 'Vimeo', 'domain': 'www.vimeo.com', 'value': 2}, {'secure': True, 'url': 'https://www.youtube.com/watch?v=09Cd7NKKvDc', 'name': 'YouTube', 'domain': 'www.youtube.com', 'value': 5}, {'secure': True, 'url': 'http://www.dailymotion.com/search/football', 'name': 'Daily Motion', 'domain': 'www.dailymotion.com', 'value': 1}]
    print("Task 3 Solution: --->")
    print(task_three(list_of_dicts=WEBSITES, string_to_check='https://', key_to_check='url', key_to_update='secure'))
    # Output of task 3: [{'domain': 'google.co.uk', 'url': 'https://www.google.co.uk', 'name': 'Google', 'secure': True, 'value': 5}, {'domain': 'facebook.com', 'url': 'https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/', 'name': 'Facebook', 'secure': True, 'value': 4}, {'domain': 'bing.com', 'url': 'https://www.bing.com/search?q=athlete&qs=n&form=QBLH&sp=-1&pq=athlete&sc=8-7&sk=&cvid=53830DD7FB2E47B7A5D9CF27F106BC9A', 'name': 'Bing', 'secure': True, 'value': 3}, {'domain': 'ask.com', 'url': 'https://uk.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q=jupiter', 'name': 'Ask', 'secure': True, 'value': 1}, {'domain': 'duckduckgo.com', 'url': 'http://duckduckgo.com/?q=plane&t=h_&ia=web', 'name': 'Duck Duck Go', 'secure': False, 'value': 2}, {'domain': 'vimeo.com', 'url': 'https://vimeo.com/53812885', 'name': 'Vimeo', 'secure': True, 'value': 2}, {'domain': 'youtube.com', 'url': 'https://www.youtube.com/watch?v=09Cd7NKKvDc', 'name': 'YouTube', 'secure': True, 'value': 5}, {'domain': 'dailymotion.com', 'url': 'http://www.dailymotion.com/search/football', 'name': 'Daily Motion', 'secure': False, 'value': 1}]
    print("Task 4 Solution: --->")
    print(task_four(list_of_dicts=WEBSITES, key='value'))
    # Output of task 4: 23