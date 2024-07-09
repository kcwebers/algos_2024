# https://www.reddit.com/r/learnpython/comments/4d2yl7/i_need_list_comprehension_exercises_to_drill/



# Find all of the numbers from 1-1000 that are divisible by 7
number_div_by_seven = [i for i in range(1, 1000) if i % 7 == 0]
print(number_div_by_seven)
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308, 315, 322, 329, 336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504, 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 679, 686, 693, 700, 707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798, 805, 812, 819, 826, 833, 840, 847, 854, 861, 868, 875, 882, 889, 896, 903, 910, 917, 924, 931, 938, 945, 952, 959, 966, 973, 980, 987, 994]


# Find all of the numbers from 1-1000 that have a 3 in them
number_cont_three = [j for j in range(1, 1000) if '3' in str(j)]
print(number_cont_three)

# Count the number of spaces in a string
sample_str = "Hello there friendly peeps!"
number_of_spaces = len([k for k in sample_str if ' ' in k])
# kind of feels long winded compared to .spplit()
print(number_of_spaces)
# 3

alt_number_number_of_spaces = len(sample_str.split()) - 1
print(alt_number_number_of_spaces)
# 

# Remove all of the vowels in a string

# Find all of the words in a string that are less than 4 letters
