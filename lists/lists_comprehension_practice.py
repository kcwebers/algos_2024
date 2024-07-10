# https://www.reddit.com/r/learnpython/comments/4d2yl7/i_need_list_comprehension_exercises_to_drill/



# Find all of the numbers from 1-1000 that are divisible by 7
number_div_by_seven = [i for i in range(1, 1000) if i % 7 == 0]
print(number_div_by_seven)
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308, 315, 322, 329, 336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504, 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 679, 686, 693, 700, 707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798, 805, 812, 819, 826, 833, 840, 847, 854, 861, 868, 875, 882, 889, 896, 903, 910, 917, 924, 931, 938, 945, 952, 959, 966, 973, 980, 987, 994]


# Find all of the numbers from 1-1000 that have a 3 in them
number_cont_three = [j for j in range(1, 1000) if '3' in str(j)]
print(number_cont_three)
# [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53, 63, 73, 83, 93, 103, 113, 123, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 143, 153, 163, 173, 183, 193, 203, 213, 223, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 243, 253, 263, 273, 283, 293, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 403, 413, 423, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 443, 453, 463, 473, 483, 493, 503, 513, 523, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 543, 553, 563, 573, 583, 593, 603, 613, 623, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 643, 653, 663, 673, 683, 693, 703, 713, 723, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 743, 753, 763, 773, 783, 793, 803, 813, 823, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 843, 853, 863, 873, 883, 893, 903, 913, 923, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 943, 953, 963, 973, 983, 993]

# Count the number of spaces in a string
sample_str = "Hello there friendly peeps!"
number_of_spaces = len([k for k in sample_str if ' ' in k])
# kind of feels long winded compared to .split()
print(number_of_spaces)
# 3

alt_number_number_of_spaces = len(sample_str.split()) - 1
print(alt_number_number_of_spaces)
# 3

# Remove all of the vowels in a string
sample_str_b = "Hello World! Oh, Hi!"
vowels = ['a', 'e', 'i', 'o', 'u']
no_vowels = [x for x in sample_str_b.lower() if x not in vowels]
print(''.join(no_vowels))
# Hll Wrld! h, H!

# Find all of the words in a string that are less than 4 letters
sample_str_c = "I went to the marketplace to purchase some new sneakers and a hat"
strings_shorter_than_four = [y for y in sample_str_c.split() if len(y) < 4]
print(strings_shorter_than_four)
# doesn't really clarify datatype of output, so will leave as list
# ['I', 'to', 'the', 'to', 'new', 'and', 'a', 'hat']
