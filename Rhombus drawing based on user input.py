def print_star_line(number_of_stars, total_stars):
    number_of_spaces = (total_stars - number_of_stars) // 2
    print(' ' * number_of_spaces, end='')
    print('*' * number_of_stars, end='')
    print(' ' * number_of_spaces)

    # print(f"{' ' * number_of_spaces}{'*' * number_of_stars}{' ' * number_of_spaces}")

def draw_rhombus(num):
    print()
    number_of_stars = None
    for i in range(num):
        if i < num / 2:
            number_of_stars = i * 2 + 1
            # print_star_line(i * 2 + 1, num)
        else:
            number_of_stars = (num-i)* 2 - 1
            # print_star_line((num-i)*2 - 1, num)

        print_star_line(number_of_stars, num)


number_of_stars= int(input('Enter number: '))
draw_rhombus(number_of_stars)

    # for i in range(num//2+1):
    #         print(i*2 + 1)



    # for i in range(1, num, 2):
    #     print(i)
    
    # for i in range(0, num , 2):
    #     print(num - i )

